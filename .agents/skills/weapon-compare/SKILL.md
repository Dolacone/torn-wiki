---
name: weapon-compare
description: Compare Torn firearms by simulated damage output and price, usually from item market or bazaar screenshots. Use when the user shares weapon listings (damage, accuracy, bonuses, price) and asks which gun is stronger, which has the best value (CP), or what a fair price is.
---

# Weapon Compare

## Goal

Rank firearms by simulated damage per clip and mark the best value by expected damage per attack turn. The model only reads inputs; `weapon_compare.py` does every calculation.

## Workflow

1. Extract every gun from the screenshots: weapon name, damage, accuracy, bonuses with %, price, and quality color (yellow / orange / red).
2. Show the extracted values to the user as a table and wait for confirmation before computing. A single misread digit can flip the value ranking.
3. Check each weapon name against `weapons.json`. If a weapon is missing, stop and ask the user for its clip size and Rate of Fire; never guess.
4. Write the confirmed input to a JSON file in the scratchpad directory (format below).
5. Run `python3 -I .agents/skills/weapon-compare/weapon_compare.py <input.json>`.
6. Reply with the script's table as-is, then the conclusion: the best value gun, the frontier, and any ignored bonus.

If the user restricts the comparison (for example "only orange guns"), filter before step 4.

## Input format

```json
{
  "scenario": {"strength": 3e9},
  "guns": [
    {"name": "Enfield SA-80", "label": "Enfield Specialist 29%", "damage": 71.77, "accuracy": 60.79, "bonuses": {"Specialist": 29}, "price": 1950000000}
  ]
}
```

- `name` must match a key in `weapons.json`.
- `label` is optional; set it when several guns share a name.
- `price` is optional; guns without a price are excluded from value marks.
- `scenario` overrides any key of `DEFAULT_SCENARIO` in the script. Override only what the user states.

## Default scenario

| Key | Default |
| --- | --- |
| Attacker effective Strength | 3b |
| Target Defense | 0 |
| Target HP | 9000 |
| Armor (all body parts) | 37.5 |
| Ammo | PI |
| Crit chance | 25% |
| Speed / target Dexterity | 2 |
| Merits | +10% damage, +2 accuracy |
| Ammo conservation | education 25% and Recoil Pad 25%, multiplied |
| Reloads | 2 (Specialist: 0) |
| Turn cap | 25 |

## Output columns

- 打 9000 回合數: turns to deal target HP, misses and reload turns included. Average / p50 / p90 over kills within the turn cap.
- 一個彈匣總傷害: average damage of one full clip, misses included. The table is sorted by this column.
- 全部彈匣總傷害: one clip times the number of clips (Specialist gets one).
- 一場 25 回合內總傷害: damage within the turn cap, reload turns included.
- `[最佳 CP]`: highest expected damage per attack turn per dollar, misses included. Ammo capacity does not count, so Conserve does not inflate it.
- `[CP 邊界]`: no other priced gun is both cheaper and higher in expected damage per attack turn.

## Model

- Damage per hit = body part multiplier x MaxDmg(Str) x (1 - mitigation) x damage/10 x (1 - armor/penetration) x variance x (1 + damage bonus %) x ammo multiplier.
- MaxDmg(Str) = 7 x log10(Str/10)^2 + 27 x log10(Str/10) + 30.
- Critical hits use multiplier 1; non-critical parts use 1/1.75, 1/3.5, or 1/5.
- Variance is a normal distribution clamped to 0.95-1.05.
- Merits, Powerful, and Specialist share one additive damage pool. Deadeye joins that pool on critical hits only.
- Hit chance comes from the Speed/Dexterity ratio, adjusted by accuracy. Sure Shot adds a guaranteed-hit chance on misses.
- Supported bonuses: Powerful, Specialist, Deadeye, Conserve, Sure Shot, Expose, Penetrate. The script lists any other bonus as ignored.
- Formulas come from the Dark Proxi fight simulator (tornarcadia.com), copied into `reference/formulas.md` of the local torn-fight-simulator project. They are community-derived, not official.
- The armor model uses one rating for every body part. Real armor sets differ by part and coverage.
