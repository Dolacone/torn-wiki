"""Monte Carlo comparison of Torn firearms. Usage: python3 -I weapon_compare.py input.json"""
import json
import math
import random
import statistics
import sys
from pathlib import Path

DEFAULT_SCENARIO = {
    "strength": 3e9,           # attacker effective Strength (after passives)
    "target_defense": 0,
    "target_hp": 9000,
    "armor": 37.5,             # uniform armor rating on every body part
    "ammo": "PI",              # STD, PI, HP, IN, TR
    "crit_chance": 25,
    "speed_dex_ratio": 2,      # attacker Speed / target Dexterity
    "merit_damage": 10,
    "merit_accuracy": 2,
    "ammo_conservation": [25, 25],  # education, Recoil Pad; stacked multiplicatively
    "reloads": 2,
    "max_turns": 25,
    "iterations": 20000,
    "seed": 1,
}

AMMO = {  # (armor penetration divisor, damage multiplier, accuracy bonus)
    "STD": (1, 1, 0),
    "PI": (2, 1, 0),
    "HP": (1 / 1.5, 1.5, 0),
    "IN": (1, 1.4, 0),
    "TR": (1, 1, 10),
}

# (probability %, damage multiplier) for non-critical hits; critical hits use 1
NON_CRIT_PARTS = [(6, 1 / 1.75), (10, 1 / 3.5), (10, 1 / 5), (10, 1 / 5), (20, 1 / 3.5), (20, 1 / 1.75), (24, 1 / 1.75)]

SUPPORTED_BONUSES = {"Powerful", "Specialist", "Deadeye", "Conserve", "Sure Shot", "Expose", "Penetrate"}


def max_damage(strength):
    l = math.log10(strength / 10)
    return 7 * l * l + 27 * l + 30


def damage_mitigation(defense, strength):
    if defense <= 0:
        return 0
    ratio = defense / strength
    if ratio >= 14:
        return 100
    if ratio >= 1:
        return 50 + 50 / math.log(14) * math.log(ratio)
    if ratio > 1 / 32:
        return 50 + 50 / math.log(32) * math.log(ratio)
    return 0


def base_hit_chance(ratio):
    if ratio >= 64:
        return 100
    if ratio >= 1:
        return 100 - 50 / 7 * (8 * math.sqrt(1 / ratio) - 1)
    if ratio > 1 / 64:
        return 50 / 7 * (8 * math.sqrt(ratio) - 1)
    return 0


def apply_accuracy(hit, accuracy):
    accuracy = max(accuracy, 0)
    if hit > 50:
        hit += (accuracy - 50) / 50 * (100 - hit)
    else:
        hit += (accuracy - 50) / 50 * hit
    return min(max(hit, 0), 100)


def variance(rng):
    while True:
        n = 1 + 0.02 * rng.gauss(0, 1)
        if 0.95 <= n <= 1.05:
            return n


class Gun:
    def __init__(self, spec, weapons, sc):
        name = spec["name"]
        if name not in weapons:
            sys.exit(f"Unknown weapon '{name}'. Known: {', '.join(weapons)}")
        base = weapons[name]
        b = spec.get("bonuses", {})
        self.label = spec.get("label") or f"{name} {spec['damage']}/{spec['accuracy']} " + " ".join(f"{k} {v}%" for k, v in b.items())
        self.price = spec.get("price")
        self.ignored = sorted(set(b) - SUPPORTED_BONUSES)
        self.clip = base["clip"]
        self.rof = base["rate_of_fire"]
        self.clips = 1 if "Specialist" in b else sc["reloads"] + 1
        self.flat = sc["merit_damage"] + b.get("Powerful", 0) + b.get("Specialist", 0)
        self.crit_bonus = b.get("Deadeye", 0)
        self.crit = (sc["crit_chance"] + b.get("Expose", 0)) / 100

        pen, ammo_mult, ammo_acc = AMMO[sc["ammo"]]
        armor = sc["armor"] * (1 - b.get("Penetrate", 0) / 100) / pen
        self.base_dmg = (max_damage(sc["strength"])
                         * (100 - damage_mitigation(sc["target_defense"], sc["strength"])) / 100
                         * spec["damage"] / 10 * (100 - armor) / 100 * ammo_mult)

        hit = apply_accuracy(base_hit_chance(sc["speed_dex_ratio"]), spec["accuracy"] + sc["merit_accuracy"] + ammo_acc) / 100
        self.hit = hit + (1 - hit) * b.get("Sure Shot", 0) / 100

        self.keep = 1.0
        for pct in sc["ammo_conservation"] + [b.get("Conserve", 0)]:
            self.keep *= 1 - pct / 100

    def attack(self, rng):
        if rng.random() >= self.hit:
            return 0
        v = variance(rng)
        if rng.random() < self.crit:
            return round(self.base_dmg * v * (1 + (self.flat + self.crit_bonus) / 100))
        r = rng.uniform(0, 100)
        for p, mult in NON_CRIT_PARTS:
            if r < p:
                break
            r -= p
        return round(mult * self.base_dmg * v * (1 + self.flat / 100))

    def rounds_used(self, rng):
        x = rng.randint(*self.rof) * self.keep
        return math.floor(x) + (rng.random() < x - math.floor(x))

    def fight(self, rng, max_turns, hp=None):
        """Return (turns until hp reaches 0 or None, total damage) under the turn cap; reloading costs a turn."""
        ammo, reloads, dealt = self.clip, self.clips - 1, 0
        for turn in range(1, max_turns + 1):
            if ammo <= 0:
                if reloads == 0:
                    break
                ammo, reloads = self.clip, reloads - 1
                continue
            ammo -= self.rounds_used(rng)
            dealt += self.attack(rng)
            if hp is not None and dealt >= hp:
                return turn, dealt
        return None, dealt

    def clip_damage(self, rng):
        ammo, dealt = self.clip, 0
        while ammo > 0:
            ammo -= self.rounds_used(rng)
            dealt += self.attack(rng)
        return dealt


def percentile(sorted_values, p):
    return sorted_values[max(math.ceil(p / 100 * len(sorted_values)) - 1, 0)]


def evaluate(gun, sc):
    rng = random.Random(sc["seed"])
    n = sc["iterations"]
    kills = [gun.fight(rng, sc["max_turns"], sc["target_hp"])[0] for _ in range(n)]
    killed = sorted(t for t in kills if t is not None)
    clip = statistics.mean(gun.clip_damage(rng) for _ in range(n))
    in_cap = statistics.mean(gun.fight(rng, sc["max_turns"])[1] for _ in range(n))
    per_turn = statistics.mean(gun.attack(rng) for _ in range(n * 10))
    return {
        "per_turn": per_turn,
        "turns": (statistics.mean(killed), percentile(killed, 50), percentile(killed, 90)) if killed else None,
        "kill_rate": len(killed) / n,
        "clip": clip,
        "all_clips": clip * gun.clips,
        "in_cap": in_cap,
    }


def fmt_money(v):
    return f"${v / 1e9:.2f}b" if v >= 1e9 else f"${v / 1e6:.0f}m"


def main():
    data = json.loads(Path(sys.argv[1]).read_text())
    weapons = json.loads((Path(__file__).parent / "weapons.json").read_text())["weapons"]
    sc = {**DEFAULT_SCENARIO, **data.get("scenario", {})}
    guns = [Gun(g, weapons, sc) for g in data["guns"]]
    results = [(g, evaluate(g, sc)) for g in guns]
    results.sort(key=lambda gr: -gr[1]["clip"])

    priced = [(g, r) for g, r in results if g.price]
    best = max(priced, key=lambda gr: gr[1]["per_turn"] / gr[0].price)[0] if priced else None
    frontier = {id(g) for g, r in priced
                if not any(o is not g and o.price <= g.price and q["per_turn"] >= r["per_turn"]
                           and (o.price < g.price or q["per_turn"] > r["per_turn"]) for o, q in priced)}

    hp, cap = sc["target_hp"], sc["max_turns"]
    print(f"| 槍 | 打 {hp} 回合數 (平均 / p50 / p90) | 一個彈匣總傷害 | 全部彈匣總傷害 | 一場 {cap} 回合內總傷害 | Price |")
    print("| --- | --- | --- | --- | --- | --- |")
    for g, r in results:
        tags = (["最佳 CP"] if g is best else []) + (["CP 邊界"] if id(g) in frontier else [])
        name = g.label + (f" [{', '.join(tags)}]" if tags else "")
        if r["turns"]:
            avg, p50, p90 = r["turns"]
            turns = f"{avg:.2f} / {p50} / {p90}"
            if r["kill_rate"] < 1:
                turns += f" ({r['kill_rate']:.0%} 在 {cap} 回合內打完)"
        else:
            turns = f"{cap} 回合內打不完"
        price = fmt_money(g.price) if g.price else "-"
        print(f"| {name} | {turns} | {r['clip']:,.0f} | {r['all_clips']:,.0f} ({g.clips} 匣) | {r['in_cap']:,.0f} | {price} |")

    print()
    print("命中率: " + ", ".join(f"{g.label} {g.hit:.2%}" for g, _ in results))
    print("每回合期望傷害 (CP 指標): " + ", ".join(f"{g.label} {r['per_turn']:,.0f}" for g, r in results))
    ignored = {b for g in guns for b in g.ignored}
    if ignored:
        print("未計入的 bonus: " + ", ".join(sorted(ignored)))
    print("情境: " + json.dumps({k: v for k, v in sc.items() if k not in ("iterations", "seed")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
