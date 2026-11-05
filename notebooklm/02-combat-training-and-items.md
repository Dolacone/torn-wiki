# Torn 戰鬥、Battlestats 訓練與道具參考 (Combat, Training & Items Reference)

本文件是 Torn 戰鬥機制、Battlestats 訓練 (Choco Jump、Happy Jump、Gym Gains 公式)、書籍與藥物成癮的參考來源。每節可獨立回答問題，數值與條件附在對應規則旁。

## 戰力總量與 Battle Stats Score (BS / BSS)

- BS (Battle Stats) = 四項屬性 (Strength, Defense, Speed, Dexterity) 合計總量。
- BSS (Battle Stats Score) = sqrt(str) + sqrt(def) + sqrt(spd) + sqrt(dex)。
- 屬性分配愈集中，相同 BSS 下的總屬性 (BS) 愈高。
- 相同 BSS 下，4:3:3:0 分配型的總 BS 比平均型高出約 34%。
- 無道具環境：防禦特化型 (Defense) 具備最高換血效率。
- 道具干擾環境：敏捷特化型 (Dexterity) 配合 Spd/5 道具能將生存率極大化，戰術見本文件「臨時戰術道具」一節。

## 命中率公式 (Hit Chance: Speed vs Dexterity)

- 核心邏輯：攻擊方 Speed 與防守方 Dexterity 的對抗。
- 比例門檻（基於 Wiki 實測數據）：
  - 50% 命中：Speed : Dexterity = 1:1。
  - 80% 命中：Speed 約為 Dexterity 的 4.5 倍。
  - 10% 命中：Dexterity 約為 Speed 的 10 倍。
  - 0% 命中：Dexterity 是對手 Speed 的 64 倍。
- 對稱性質：比值 R = Speed / Dexterity 與 1/R 的命中率相對於 50% 呈完美對稱，即 f(R) + f(1/R) = 1。
- 計算模型：
  - 簡化對數擬合：Hit Chance = MAX(0, MIN(1, 0.5 + 0.278 * LOG10(Speed / Dexterity)))
    - 局限：只在 64 倍極端值時準確。在中段 (1.5x 至 20x) 會嚴重低估命中率，例如 2 倍 Speed 時實際為 66.74%，此公式只算得 58.37%。
  - 中低倍數精確擬合 (4 倍以內)：Hit Chance ≈ 0.5 + 0.48 * LOG10(Speed / Dexterity)
  - 簡化 Logistic 理論模型：Hit Chance ≈ 1 / (1 + (Dexterity / Speed))
    - 在 1x 至 4x 區間誤差小於 1.5%。
    - Speed = Dexterity 時，命中率完全取決於武器的 Accuracy 數值，例如 65 Accuracy 即為 65% 命中率。
- Google Spreadsheet 簡化公式 (極端值擬合版)，A2 為敏捷、B2 為對手速度：

```excel
=MAX(0, MIN(1, 0.5 + 0.278 * LOG10(B2 / A2)))
```

## 傷害減免公式 (Damage Mitigation: Defense vs Strength)

- 核心邏輯：防守方 Defense 與攻擊方 Strength 的對抗。
- 屬性優勢段 (Defense >= Strength)：Mitigation = MAX(0, MIN(1, 0.5 + 0.435 * LOG10(Defense / Strength)))
  - 臨界點：Defense 為 Strength 的 14.11 倍 (約 14 倍) 時，減傷率達到 100%。
- 屬性劣勢段 (Defense < Strength)：Mitigation = MAX(0, MIN(1, 0.5 + 0.332 * LOG10(Defense / Strength)))
  - 臨界點：Strength 為 Defense 的 32 倍 (即 Defense 為 1/32 倍) 時，減傷率降至 0%。
- 護甲效果：D(A) = D(I) * (1 - A/100)
  - D(A) 為實收傷害，D(I) 為初始傷害，A 為護甲值。
  - 標準參考值：45% 護甲對應 0.55 的受傷係數。

## 部位命中率與部位傷害修正 (Body Part Hits & Damage Modifiers)

### 不同敵人暴擊率下的部位命中率 (%)

| 命中機率 (%) | 頭部 (Head) | 喉嚨 (Throat) | 心臟 (Heart) | 胸部 (Chest) | 胃部 (Stomach) | 手臂 (Arms) | 手部 (Hands) | 鼠蹊部 (Groin) | 腿部 (Legs) | 腳部 (Feet) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 敵人暴擊 12% | 9.6 | 1.2 | 1.2 | 22.0 | 17.6 | 8.8 | 8.8 | 4.4 | 17.6 | 8.8 |
| 敵人暴擊 20% | 16.0 | 2.0 | 2.0 | 20.0 | 16.0 | 8.0 | 8.0 | 4.0 | 16.0 | 8.0 |
| 敵人暴擊 25% | 20.0 | 2.5 | 2.5 | 18.8 | 15.0 | 7.5 | 7.5 | 3.8 | 15.0 | 7.5 |

### 各部位傷害修正係數

| 部位 | 頭部 | 喉嚨 | 心臟 | 胸部 | 胃部 | 手臂 | 手部 | 鼠蹊部 | 腿部 | 腳部 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 數值 | 3.5 | 3.5 | 3.5 | 2.0 | 2.0 | 1.0 | 0.7 | 2.0 | 1.0 | 0.7 |

### 各暴擊率下的傷害總量修正 (傷害 * 機率)

| 傷害 * 機率 | 頭部 | 喉嚨 | 心臟 | 胸部 | 胃部 | 手臂 | 手部 | 鼠蹊部 | 腿部 | 腳部 | 總和 (SUM) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 敵人暴擊 12% | 0.3360 | 0.0420 | 0.0420 | 0.4400 | 0.3520 | 0.0880 | 0.0616 | 0.0880 | 0.1760 | 0.0616 | 1.6872 |
| 敵人暴擊 20% | 0.5600 | 0.0700 | 0.0700 | 0.4000 | 0.3200 | 0.0800 | 0.0560 | 0.0800 | 0.1600 | 0.0560 | 1.8520 |
| 敵人暴擊 25% | 0.7000 | 0.0875 | 0.0875 | 0.3750 | 0.3000 | 0.0750 | 0.0525 | 0.0750 | 0.1500 | 0.0525 | 1.8550 |

## 護甲數值、覆蓋率與 End Game 等效傷害 (Armor Rating, Coverage & Final Damage Modifier)

### 各類護甲平均數值 (Average Armor Rating)

| Armor 類型 | 頭盔 (Helmet) | 身體 (Body) | 褲子 (Pants) | 手套 (Gloves) | 靴子 (Boots) |
| --- | --- | --- | --- | --- | --- |
| Combat (+flexible) | 40.5 | 44.5 | 40.5 | 40.5 | 40.5 |
| Riot | 37.5 | 47.5 | 47.5 | 47.5 | 47.5 |
| Assault | 48.5 | 48.5 | 48.5 | 48.5 | 48.5 |
| Dune | 46.5 | 46.5 | 46.5 | 46.5 | 46.5 |
| Delta | 51.5 | 51.5 | 51.5 | 51.5 | 51.5 |
| Marauder | 42.5 | 54.5 | 54.5 | 54.5 | 54.5 |
| Sentinel | 55.5 | 55.5 | 55.5 | 55.5 | 55.5 |
| Vanguard | 50.5 | 50.5 | 50.5 | 50.5 | 50.5 |
| EOD | 57.5 | 57.5 | 57.5 | 57.5 | 57.5 |

### 各類護甲部位覆蓋率 (%)

| Armor 類型 | 頭部 | 喉嚨 | 心臟 | 胸部 | 胃部 | 手臂 | 手部 | 鼠蹊部 | 腿部 | 腳部 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Combat (+flexible) | 67.49 | 0.00 | 100.00 | 95.73 | 100.00 | 36.48 | 100.00 | 100.00 | 100.00 | 100.00 |
| Riot | 99.61 | 79.06 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| Assault | 66.53 | 85.15 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| Dune | 64.83 | 83.83 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| Delta | 27.13 | 88.81 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| Marauder | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| Sentinel | 74.24 | 95.81 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| Vanguard | 39.60 | 83.53 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| EOD | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |

### 等效傷害修正係數 (End Game，敵人暴擊率 25%)

係數越低對穿著者越有利。

| Armor 類型 | 基礎傷害修正 (無特效) | 等效傷害修正 (計入特效最低值) | 特效觸發情境與折算說明 |
| --- | --- | --- | --- |
| Combat (標準值) | 1.2868 | 1.2868 | 商店白板防具，無特效 |
| Riot | 1.1625 | 0.8200 | 計入對近戰 30% 減傷 (部位觸發) |
| Assault | 1.1705 | 0.8936 | 計入對子彈 30% 減傷 (部位觸發) |
| Dune | 1.2105 | 0.7829 | 計入血量低於 25% 時 45% 減傷 (部位觸發) |
| Delta | 1.2528 | 1.2528 | 特效為負面狀態抗性，無直接減傷 |
| Marauder | 1.0339 | 0.8271 | 計入生命值 +25% 被動加成 (等效傷害乘以 0.80) |
| Sentinel | 1.0173 | 0.6651 | 計入防禦力 +150% 被動加成 (等效傷害乘以 0.6538) |
| Vanguard | 1.2275 | 0.7255 | 計入敏捷閃避 +150% 被動加成 (等效傷害乘以 0.5910) |
| EOD | 0.8806 | 0.6165 | 計入 30% 全時免傷機率 (等效傷害乘以 0.70) |

### 等效傷害修正的計算公式與參數

本表數值可用以下參數完全重現。

- 敵人暴擊率 25% 時的部位命中機率 (Prob)：頭部 20.0%、喉嚨 2.5%、心臟 2.5%、胸部 18.75%、胃部 15.0%、手臂 7.5%、手部 7.5%、鼠蹊部 3.75%、腿部 15.0%、腳部 7.5%。
- 部位傷害修正係數 (Part_Modifier)：頭部/喉嚨/心臟 3.5，胸部/胃部/鼠蹊部 2.0，手臂/腿部 1.0，手部/腳部 0.7。
- 基礎防具護甲值 (最低值)：
  - Combat：Helmet 40.5, Body 44.5, Pants 40.5, Gloves 40.5, Boots 40.5
  - Riot：Helmet 35, Body 45, Pants 45, Gloves 45, Boots 45
  - Assault：Helmet 46, Body 46, Pants 46, Gloves 46, Boots 46
  - Dune：Helmet 44, Body 44, Pants 44, Gloves 44, Boots 44
  - Delta：Helmet 49, Body 49, Pants 49, Gloves 49, Boots 49
  - Marauder：Helmet 40, Body 52, Pants 52, Gloves 52, Boots 52
  - Sentinel：Helmet 53, Body 53, Pants 53, Gloves 53, Boots 53
  - Vanguard：Helmet 48, Body 48, Pants 48, Gloves 48, Boots 48
  - EOD：Helmet 55, Body 55, Pants 55, Gloves 55, Boots 55
- 防具部位防護對應 (Mapping)：
  - Helmet 保護：頭部、喉嚨
  - Body 保護：心臟、胸部、胃部、手臂
  - Gloves 保護：手部
  - Pants 保護：鼠蹊部、腿部
  - Boots 保護：腳部
- 部位覆蓋率 (Coverage)：見上方「各類護甲部位覆蓋率」表。
- 每個部位的傷害期望值 (D_p)：
  - D_p = Prob_p × Part_Modifier_p × [ (Coverage_p / 100) × (1 - Armor_rating_p / 100) × (1 - Active_Reduction_p) + (1 - Coverage_p / 100) ]
  - 部位減傷特效 (Active_Reduction)：Riot 對近戰為 30% (0.30)；Assault 對子彈為 30% (0.30)；Dune 為 45% (0.45)；其餘防具為 0。
  - 10 個部位的 D_p 加總，得到該防具的基礎受傷修正值 (D_base)。
- 最終等效傷害修正 (D_final) = D_base × EHP_Multiplier：
  - EOD (全時免傷 30%)：EHP_Multiplier = 0.70
  - Marauder (生命值 +25%)：EHP_Multiplier = 1 / 1.25 = 0.80
  - Sentinel (防禦力 +150%)：
    - 依減傷公式 Mitigation = 0.5 + 0.435 × LOG10(Defense / Strength)。
    - 假設基礎屬性比為 1:1 (減傷 50%)，防禦力變為 2.5 倍後，減傷率提升至 67.31%。
    - 折算因子 = (1 - 0.6731) / (1 - 0.50) = 0.6538
  - Vanguard (敏捷度 +150%)：
    - 依 Wiki 實測數據的對稱插值：比值變為 1/2.5 = 0.4 倍，對應之優勢 2.5 倍命中率約為 70.45%。
    - 敏捷變為 2.5 倍後，命中率實際降低至約 29.55%，而非簡化公式算出的 38.94%。
    - 折算因子 = 29.55% / 50.00% = 0.5910

### 護甲結論

1. EOD 套裝在 End Game 擁有最頂級的生存能力 (等效係數 0.6165)。考量性價比，Sentinel 套裝在屬性對等下提供極高的防禦被動增幅，等效係數 0.6651 直逼 EOD。
2. Marauder 套裝 (0.8271) 提供穩定的 25% 生命值增幅，防護表現與 Riot 套裝在近戰環境下相當，且不受對手屬性壓制影響，是穩定的全時防護裝備。
3. Delta 在純減傷期望值上表現較差，價值在於負面狀態抗性。Vanguard 計入敏捷被動提升後等效係數可達 0.7255，生存能力直逼 Sentinel (0.6651)，且具備高敏捷帶來的閃避與隱匿優勢。

## 傳奇裝備評核與購買建議 (Legendary Gear Evaluation)

### 武器評鑑標準

- 購買任何傳奇武器前，先與「裝滿模組的白色 Armalite」對比。
  - 標準：Armalite ML-60 + Sights + Lights。
  - 結論：花費 1b 買的傳奇步槍性能若低於白板 Armalite，就是浪費錢。

### 武器類別排名

- 主武器 (Rifles)：
  1. Armalite ML-60：永遠的王者，平衡性最高。
  2. Enfield SA-80：極高 Accuracy，適合對付 Dexterity Whore。
  3. Tarvor TAR-21 / Sig 552：次選，性能略遜。
- 副武器 (Secondary)：
  1. BT MP9：若帶有 Revitalize (恢復 Energy) 屬性，則是神級裝備。
  2. Luger / DB Beretta：特定屬性加成下可用。
- 近戰武器 (Melee)：
  1. Diamond Blade：穩定高 Damage。
  2. Macana：高 Accuracy，適合補刀。

### 護甲配置建議

- 入門配置：
  - Riot Helmet：提供全臉保護 (遮擋面部，大幅減少 Critical Hit 傷害)，CP 值最高。
  - Dune Body：在中價位中表現優異。
- 頂級防禦：
  - EOD 套裝：最強防禦，但價格極其昂貴。
  - Sentinel / Marauder：優質的高級護甲。

### 購買策略

- 優先順序：模組 (Mods) > 入門高級護甲 (Riot/Dune) > 特殊屬性武器。
- 陷阱警示：避開 Accuracy 過低 (低於 60) 的傳奇主武器，除非它有極端強大的特殊屬性。

## 武器模組 (Weapon Mods)

安裝武器模組是提升戰鬥力最快且最具成本效益的方式之一。

### 模組系統規則

- 共有 12 個類別，約 30 種不同的模組。
- 階級系統 (Tiers)：多類別模組分為不同階級。必須先擁有前一個階級，才能在商店看到下一個階級。
- 安裝限制：並非所有武器都能安裝所有模組。
  - 雙武器 (Dual Weapons) 通常有限制。
  - 左輪手槍 (Revolvers) 無法安裝擴充彈匣。
  - 具有 Specialist 屬性 (彈夾限制為 1) 的武器無法安裝額外彈匣。
- 取得方式：
  - 來源：Mission Shop (任務商店)。
  - 貨幣：Mission Credits。
  - 階級解鎖：必須按順序購買 (Tier 1 -> Tier 2 -> ...)。商店中會隨機出現已解鎖階級的模組。

### 模組類別與效果 (數值以最高階 Max Tier 為準)

| 類別 (Category) | 效果 (Effect) | 最高階加成 (Max Tier) | 適用武器類型 |
| --- | --- | --- | --- |
| Sights | 提升 Accuracy | +1.75 Accuracy | MG, Pistol, Rifle, SMG |
| Lasers | 提升 Critical Hit 機率 | +5% Critical Rate | MG, Pistol, Rifle, Heavy, Shotgun, SMG |
| Suppressors | 提升 Stealth，但降低 Damage | +5 Stealth, -5% Damage | Pistol, Rifle, SMG |
| Extended Magazines | 提升彈匣容量 (Clip Size) | +30% Clip Size | MG, Pistol, Rifle, SMG |
| Extra Magazines | 增加起始彈匣數量 | +2 Extra Mags | 多數武器 (除 Specialist 外) |
| Triggers | 提升第一回合的命中率 | +7.50 Accuracy (Turn 1) | MG, Pistol, Rifle, Shotgun, SMG |
| Mounts | 提升 Accuracy，但大幅降低躲避能力 | +2.00 Accuracy, -30% Dex | MG, Rifle, Heavy |
| Grips | 提升 Accuracy | +0.75 Accuracy | MG, Pistol, Rifle, Shotgun, SMG |
| Chokes | 提升 Damage (霰彈槍專屬) | +10% Damage | Shotgun |
| Recoil Pads | 減少每回合彈藥消耗 (Ammo Control) | 25% Ammo Conservation | MG, Rifle, Shotgun |
| Brakes | 提升 Accuracy，但降低 Stealth | +1.50 Accuracy, -3 Stealth | MG, Pistol, Rifle, SMG |
| Lights | 降低對方的 Accuracy 與 Stealth | -5.00 Opponent Acc, -3 Opp Stealth | 多數遠程武器 |

### 模組配置建議

- 效能轉換：一個高品質的瞄準鏡 (Sights) 提供的 Accuracy 增益，等同於在健身房花費數萬 Energy 訓練 Speed。
- 裝備原則：所有常用武器都應該裝滿模組。
- 主武器 (Main Rifle) 最強配置：Laser + Recoil Pad + Special Ammo。
- 副武器：視用途而定。平衡型同樣建議 Accuracy 優先。
- 固定屬性：模組提供的數值是固定的。Battlestats 較低時，模組的影響力極其巨大。
- 成本：高品質模組價格昂貴，高階 (Tier 4) 模組需要大量 Mission Credits。

## 特殊彈藥 (Special Ammo)

特殊彈藥是高階戰鬥中不可或缺的增益，通常透過公司 Job Points (如 Gun Shop) 獲得。

### 彈藥性能評級

- 第一梯隊：燃燒彈 (Incendiary)
  - 加成：增加最多 40% 的額外 Damage。
  - 評價：戰鬥增益之王。配合 Armalite 能造成毀滅性打擊。
- 第二梯隊：曳光彈 (Tracer)
  - 加成：增加最多 10 點基礎 Accuracy。
  - 評價：對抗 Dexterity Whore 的最終手段，確保命中率。
- 第二梯隊：穿甲彈 (Piercing)
  - 加成：減少目標 50% 的 Armor 防護。
  - 評價：專門對付穿著高級護甲 (EOD/Marauder) 或 Defense Whore 的利器。
- 彈藥選擇陷阱：評價為垃圾。雖然有 Damage 加成，但會被對方的 Armor 嚴重削弱，實際效果不如 Incendiary。

### 使用策略

- 庫存管理：特殊彈藥難以取得且珍貴，平時應保持 Off，僅在戰爭 (Warring) 或對付關鍵對手時開啟。
- 武器對應：將最強的彈藥安裝在 Accuracy 最高、最穩定的 Rifles 上。

## 針劑 (Needles) 與 Needle Rolling

Needles 是一種 Temporary Weapons，使用後獲得持續 120 秒 (2 分鐘) 的對應 Stats 增益。

- Effects 跨戰鬥持續：Effects 在多場戰鬥間持續存在，直到兩分鐘結束或你被擊敗為止。
- 數值範例：1b 基礎 Defense 使用 Serotonin，獲得額外 300% Defense (3b)，總 Defense 來到 4b。

### 針劑效果

- Tyrosine：增加 500% Dexterity，持續 120 秒。
- Serotonin：增加 300% Defense，持續 120 秒，同時恢復 25% Life。
- Melatonin：增加 500% Speed，持續 120 秒。
- Epinephrine：增加 500% Strength，持續 120 秒。

### 疊加與切換規則

- 同種類限制：同時間只能有一種相同類型的 Needle 為 Active。重複使用同種 Needle 只會重置計時器。
- 異種類疊加：可以同時啟動全部四種不同屬性的 Needles。
- 此操作稱為 Needle Rolling 或 Temporary Boosting，效果極強，但需要在戰鬥與戰鬥之間切換裝備 Needles。
- 安全限制：只有在未被其他人 Attacking 的情況下，才能切換 Needles。

### 實戰策略

- 首選 Needle：
  - Defense 型玩家：優先選擇 Serotonin。
  - 其他類型玩家：優先選擇 Tyrosine。Tyrosine 配合低屬性隊友向敵方陣營投擲煙霧彈 (Smokes) 的戰術，能讓你變得極難被擊中。
- 起手選擇 (Attacking vs Defense)：
  - Defense 型 Needle 提供生存能力，Attacking 型 Needle 提供火力以快速結束戰鬥並進入下一個 Needle。
  - 切換 Needles 的速度不夠快時，使用對你自身增益最大的 Needle。
- Loadouts：強烈建議使用 Loadouts 功能加快切換速度，省去在物品欄中尋找物品的時間。

### 操作循環

1. Equip 第一種 Needle。Attacking 玩家，使用 Needle，擊敗目標。
2. Equip 第二種 Needle。Attacking 玩家，使用 Needle，擊敗目標。
3. Equip 第三種 Needle。Attacking 玩家，使用 Needle，擊敗目標。
4. Equip 第四種 Needle。Attacking 玩家，使用 Needle，擊敗目標。
5. 之後的戰鬥改用煙霧彈 (Smokes)，直到第一個增益效果結束。
6. 增益結束後，從第一種 Needle 重新開始 Loop。

## 臨時戰術道具 (Temporary Items Tactics)

### 道具聯動策略

- 煙霧彈與閃避流 (Smoke + Dexterity Whore)：
  - 戰術：投擲煙霧彈 (Smoke Grenade) 減少對方的 Accuracy。
  - 效果：配合自身極高的 Dexterity，讓對方的命中率降至趨近於零。
- 閃光彈與防禦流 (Flashbang + Defense Whore)：
  - 戰術：投擲閃光彈 (Flashbang) 減少對方的 Speed 與 Strength。
  - 效果：結合自身極高 Defense，確保對方即使命中也無法擊穿護甲。
- 催淚瓦斯 (Tear Gas)：
  - 戰術：降低對方所有屬性。
  - 時機：對手屬性極其平均且遠超你時使用，作為最後手段。

### 進階操作技術

- 雙視窗操作 (Stacking)：
  - 方法：在兩個瀏覽器標籤頁 (Tabs) 或裝置上同時開啟戰鬥畫面。
  - 作用：一邊進行攻擊，另一邊隨時觀察 Needle 計時器並快速切換。
- 釣魚策略 (Baiting)：
  - 策略：故意不帶 Needle 進行弱攻擊，騙出對方的防禦性道具或其他資源。
  - 反制：在對方以為你沒招時，透過 Loadouts 切換至全副武裝的 Warring 配置。

### 道具克制建議

- 對付高 Dexterity：煙霧彈或高 Accuracy 武器 (Enfield/Macana)。
- 對付高 Defense：Piercing Ammo 或 Epinephrine (+Strength)。

## 戰鬥設定與 Loadouts (Attack Settings)

### 防禦配置 (離線或被動被攻擊時的反擊設定)

- 武器使用比例建議：
  - Primary (主武器)：18 (約佔 90%)
  - Secondary (副武器)：1
  - Melee (近戰武器)：1
  - 理由：確保防禦反擊絕大部分時間都在使用最強的 Rifles。
- 彈藥自動設定：
  - 優先使用裝有特殊彈藥 (Special Ammo) 的武器。
  - 設定在戰鬥中自動重新裝彈 (Reload)。

### 戰法細節

- 血清延遲技巧 (Serotonin Timing)：
  - 策略：不要在戰鬥開始就投擲 Serotonin。
  - 操作：等到 Life 降低約 25-30% 時，設定腳本或手動投擲。
  - 效果：獲得防禦增益的同時，最大限度利用恢復 25% Life 的效果。
- 藥品與增益：戰爭期間身上備有足夠的醫療用品，並使用對應的 Needles。

### Loadout 配置

- 建立至少三套 Loadouts：
  - Warring：最強武裝 + Needles。
  - Training：最大化 Gym Gains (若公司有提供加成)。
  - Stealth：最大化 Stealth。

## Gym Gains 公式 (Vladar)

Gym Gains 以 Vladar 試算表的公式計算單次訓練的 stat 增加量。

### 單次訓練的 stat 增加量

```
gain = (1/200000) * Dots * E * Mult * ( S_adj * ROUND(1 + 0.07 * ROUND(ln(1 + H/250), 4), 4) + 8 * H^1.05 + A * (1 - (H/99999)^2) + B )
```

- Dots：健身房該項 stat 的 gym dots，例如 Frontline Fitness strength 為 7.5。
- E：每次訓練消耗的 Energy。
- Mult：所有 gym gains 加成相乘，例如 Steadfast +10% 與 Property +2% 為 1.1 * 1.02。
- H：訓練當下的 Happy，上限 99,999。
- S_adj：調整後的 stat，見下方「50M 以上的 stat 調整」。
- A、B：依訓練的 stat 而定，見常數表。

### 50M 以上的 stat 調整

```
S_adj = S                                          (S < 50,000,000)
S_adj = (S - 50,000,000) / (8.77635 * log10(S)) + 50,000,000   (S >= 50,000,000)
```

- S：要訓練的那項 stat 目前數值。
- 50M 以上的 stat 仍會成長，但成長速度遞減。

### 各 stat 常數

| Stat | A | B | C |
| --- | --- | --- | --- |
| Strength | 1600 | 1700 | 700 |
| Speed | 1600 | 2000 | 1350 |
| Dexterity | 1800 | 1500 | 1000 |
| Defense | 2100 | -600 | 1500 |

- C 決定增加量的範圍：最小值用 B - C 代入，最大值用 B + C 代入。

## 健身房 Dots 與訓練比例 (Gym Dots & Training Ratios)

### 健身房加成基礎

- George's Gym：非專項健身房中最強者。每次訓練消耗 10 Energy (e)，加成為 7.3 dots。
- Specialized Gyms：加成更高，分別為 25e (7.5 dots) 與 50e (8.0 dots)。
- 比例訓練的核心目標：盡可能讓更多屬性在 7.5 或 8.0 dots 的專項健身房內訓練，而非留在 7.3 dots 的 George's。

### 三專項模式 (Hank's Ratio)

使用兩個專項健身房訓練三項屬性，第四項屬性留在 George's Gym。

- 比例構成：Strength 約 27.78%、Defense 約 34.72% (最高點)、Speed 約 27.78%、Dexterity 約 9.72% (最低點)。
- 健身房配置：Defense 在 Mr. Isoyamas (50e)；Strength 與 Speed 在 Frontline Fitness (25e)；Dexterity 在 George's (10e)。
- 優點：更高的總屬性獲取率，比 Baldr's 高約 5-7%。
- 缺點：極度不平衡。其中一項防禦屬性 (Defense 或 Dex) 必須保持在總額 10% 以下，成為防守上的巨大漏洞。
- 限制：某一屬性過高時，將會失去 25e 健身房的進入權限。

### 雙專項模式 (Baldr's Ratio)

使用兩個專項健身房訓練兩項屬性，另外兩項屬性在 George's Gym 訓練。

- 比例構成：Strength 約 30.86% (最高點)、Speed 約 24.69% (次高點)、Defense 約 22.22%、Dexterity 約 22.22%。
- 健身房配置：Strength 在 Gym 3,000 (50e)；Speed 在 Frontline Fitness (25e)；Defense 與 Dexterity 在 George's (10e)。
- 優點：更均衡的屬性配置。最低屬性仍能維持在 22% 左右，沒有明顯致命傷。
- 缺點：總增益低於 Hank's Ratio。
- 推薦：對於大多數非專業數據玩家，這是最理想的通用流派。

### 比例配置表

| 高點屬性 | 健身房 (50e) | 次要/平衡屬性 | 健身房 (25e) | 其餘屬性訓練地 |
| --- | --- | --- | --- | --- |
| Strength (Baldr) | Gym 3,000 | Speed | Frontline Fitness | George's |
| Speed (Baldr) | Total Rebound | Strength | Frontline Fitness | George's |
| Defense (Baldr/Hank) | Mr. Isoyamas | Dexterity/Others | Balboas/Frontline | George's |
| Dexterity (Baldr/Hank) | Elites | Defense/Others | Balboas/Frontline | George's |

### 比例選擇考量

- 戰鬥力 vs 總額：Hank's Ratio 追求最高的屬性總額，但在戰鬥中一項屬性極低，面對同等級對手時常處於劣勢。
- 使用 SE (Stat Enhancers) 會隨屬性飆升而迅速導致原本的 25e 專項健身房失效，僅剩該屬性的 50e 健身房可用。
- 推薦路徑：
  - 計畫性的數據型玩家，致力於極大化增益：Hank's Ratio。
  - 希望變強的同時保持穩定的戰鬥表現：Baldr's Ratio。

## Battlestats 訓練策略 (Training Strategy)

### 基礎核心觀念

- 屬性收益 (Gains)：屬性越高，單次訓練獲得的數值越多。50M 硬上限已取消，超過 50M 的部分改為遞減成長，計算方式見本文件「Gym Gains 公式」一節的 S_adj。
- 健身房 (Gyms)：解鎖新健身房是首要任務。普通健身房最高為 7.3 dots (George's)，專項健身房 (Specialized Gyms) 提供 7.5 或 8.0 dots。
- 比例重要性：屬性的「比例」往往比「總額」更能決定戰鬥勝負。

### 訓練流派對比

- 均衡型 (Balanced)：
  - 定義：四項屬性保持接近。
  - 優點：沒有明顯弱點，能應對大多數對手。
  - 缺點：解鎖專項健身房速度較慢。
- 專精型 (Whoring)：
  - 定義：極端投資某一項或兩項屬性。
  - Defense Whore：極高 Defense，能讓對方的傷害降至 0。傷害為 0 時，對方的 Weapon Bonus (如致傷加成) 不會生效，這對 Defense Whore 非常有利。
  - Dexterity Whore：極高 Dexterity，結合 Smoke Tactics 讓對方完全無法命中。
  - 優點：在特定比例下幾乎無敵，能進駐 8.0 dots 的專項健身房。
- 建議優先解鎖：根據你選擇的 Whore 路線，優先解鎖對應的專項健身房。

### 訓練里程碑

- 10m：Battlestats 的起點，此時 Needles 的效果開始顯著。
- 100m - 500m：多數玩家停留的區域，此時裝備 (Gear) 與模組 (Mods) 的比重增加。
- 1b：進入高階玩家行列，通常此時會開始考慮 SE (Stat Enhancers) 的投入。

### 進階增益與訓練週期

書籍 (Books) 是提升屬性的最強外部手段。

- 階段 1：單項 50m 前 (Uncapped)
  - 核心：此階段快樂值影響力極大。
  - 推薦路徑：Happy Jumping (快速提升基礎屬性的核心技術)。
  - 策略轉換點 (Switching Points，單項屬性)：
    - < 55k：使用 Choco Jump 是最高 CP 值方案。
    - < 200k：使用標準 Happy Jump (EDVD) 仍具顯著優勢。
    - < 850k：使用 99k Happy Jump (Book) 為極限方案。
    - 超過上述數值後，應轉向 3 Xanax/日 的自然 Energy 訓練。
  - 推薦書籍：Ignorance Is Bliss 或其他能提供過量 Happy 的資源。
- 階段 2：屬性 200m 以上
  - 核心：此階段屬性基數足夠，適合結算百分比加成。
  - 推薦書籍：Brawn Over Brains 系列 (5% 加成)。讀書結束時，加成會根據當時的數值結算。
- 階段 3：極限訓練週期 (God Tier Prep)
  - 條件：擁有數十億資金與 10 星特定公司 (能量相關公司)。
  - 推薦書籍：Fuelling Your Way To Failure (雙倍能量罐)。需配合 1000 罐能量罐與 31 天高密度的 FHC 使用。

## Happy 機制與房產 Happy 上限 (Happy Mechanics & Property)

快樂值 (Happy) 直接決定健身房訓練 (Gym Training) 的屬性收益，初期 Stats 較低時影響力極大。

### 15 分鐘重置規則

- 快樂值每 15 分鐘會在 xx:00, xx:15, xx:30, xx:45 重置回目前的房產上限值。
- 透過消耗品使快樂值超過上限時，必須在下一個重置點前消耗完所有 Energy。

### 房產等級與快樂值上限

- 初期建議：
  - Penthouse：提供 925 Happy。
  - Mansion：提供 1500 Happy。
  - 警語：避開低於 925 Happy 的房產 (如 Shack)，那會極大拖慢成長速度。
- 15 級目標：租用 Private Island (PI)，提供 3600 或更高的 Happy。

### 快樂值超限道具

- Candy (糖果)：如 Lollipops，可將快樂值推高到超過房產上限。
- Ecstasy (快樂丸)：直接將當前的快樂值翻倍 (Double)，通常用於 E-jump 或短時間的高強度訓練。

## Happy Jump 訓練 (Happy Jumping)

Happy Jumping 是透過道具將 Happy 提升至超越 Property 上限的行為，藉此提高每單位 Energy 的屬性收益，在單次訓練中獲得極大化的屬性成長。

### 核心機制

- Happy 收益：Happy 越高，每單位 Energy 獲得的屬性越多。Happy 翻倍時收益最多約 2 倍，stat 越高倍數越小，計算方式見本文件「Gym Gains 公式」一節。
- 15 分鐘重置：Happy 會在每小時的 XX:00, XX:15, XX:30, XX:45 準時重置回 Property 上限。必須在重置剛過後立即開始使用道具，確保有完整的 15 分鐘進行操作與訓練。
- 能量消耗與 Happy 損失：每次訓練會損失約等同於 Energy 消耗量 40-60% 的 Happy。

### 準備條件

- 居住環境：建議至少擁有最高規格的 Private Island (PI) 以獲得較高的基礎 Happy。
- 公司加成：在 10 星 Adult Novelties (AN) 工作可讓 Erotic DVD (EDVD) 的 Happy 收益翻倍 (從 2.5k 變為 5k)。

### 跳點方法

- Choco Jump：
  - 適用對象：初期資金有限的玩家。
  - Energy：自然上限加 1 個 Xanax。
  - Happy 道具：最多 49 份 Candy。
  - Drug：1 個 Xanax 與 1 個 Ecstasy。
  - 完整流程見本文件「Choco Jump」一節。
- Happy Jump：
  - 適用對象：資金足以使用 EDVD 的玩家。
  - Energy：使用 4 個 Xanax 堆疊至 1,000。
  - Happy 道具：5 個 EDVD。
  - Drug：4 個 Xanax 與 1 個 Ecstasy。
  - 流程：等待 Drug Cooldown 歸零，在重置點剛過後使用 EDVD 與 Ecstasy，再於下一個重置點前耗盡 Energy。

### 進階 Happy 訓練

- Ignorance is Bliss：
  - 條件：擁有書籍 Ignorance is Bliss。
  - 效果：書籍生效期間 Happy 不會重置。
  - 策略：使用大量 EDVD 與 Ecstasy 將 Happy 推升至 99k 滿值，並在 31 天內持續透過 Xanax 與 Refill 維持高 Happy 狀態訓練。
- Poison Mistletoe：
  - 條件：透過他人持有的 Ignorance is Bliss 書本效果。
  - 流程：對擁有 99k Happy 的目標使用 2 個 Poison Mistletoe (偷取 25% Happy) -> 使用 Ecstasy 補至 99k -> 訓練。
  - 優點：不消耗 Booster Cooldown，可額外配合 Energy Drinks 進行超高強度訓練。

## Choco Jump (巧克力跳躍訓練)

Choco Jump 是低成本 Candy 訓練法，適合初期資金有限的新手。它不使用 1,000 Energy 堆疊。

### 核心訓練機制

- 成本：約 $3m。
- 效果：介於自然 Energy 訓練與 Happy Jump 之間。
- 道具需求：
  - 最多 49 個 Bag of Candy Kisses (BCC) 或 Big Box of Chocolate Bars (BBC)。
  - 推薦：使用 BCC，因其價格與 BBC 相當，但每份額外提供 15 Happy。
  - 1 個 Xanax。
  - 1 個 Ecstasy。
  - 可選用一次 Points Refill。

### 執行步驟

1. 先讓 Energy 自然回滿。
2. 使用 1 個 Xanax。
3. 等待 Drug Cooldown 與 Booster Cooldown 歸零。
4. 在 15 分鐘重置點剛過後使用 Candy。
5. 使用 1 個 Ecstasy 將目前 Happy 加倍。
6. 在下一個重置點前耗盡 Energy。
7. 使用 Refill 後，再次耗盡 Energy。

### 每日雙次跳點 (Double Daily Jump Method)

- 原理：將 Booster Cooldown 控制在 12 小時內。
- 步驟：
  - 每次只使用 22-24 個 BCC/BBC。
  - 這會產生約 11-12 小時的冷卻時間。
  - 每次使用 1 個 Xanax 與 1 個 Ecstasy。
- 優點：每日可使用兩個 Booster 週期。

### 毒品風險與轉換點

- Choco Jump 每次使用 1 個 Xanax 與 1 個 Ecstasy。
- Happy Jump 使用 4 個 Xanax 與 1 個 Ecstasy，因此 Drug 次數較高。Addiction 與 Rehab 規則見本文件「毒品成癮與戒斷」一節。
- 隨著屬性提升，Choco Jump 的效益會遞減。單項屬性達到 55k 左右時，轉向更高階的 Happy Jump 或純 Energy 訓練。

## Stat Enhancer (SE) Cap 與能量罐效益 (SE Cap Analysis)

SE (Stat Enhancer) Cap 指使用 SE 的財務效益超越使用 Cans 時的 Battlestats 臨界點。

### 市場現況與計算假設

- 近年因 Halloween 與 Christmas Town 活動，大量 Cans 流入市場，價格創下歷史新低。
- 便宜的 Cans 配合新的 Exponential gym gains formula，使 Cans 在非常高的 Stats 階段依然比 SE 更具成本效益。
- 效益計算的假設基準：單個 SE 價格 450m、標準 Gym 加成、5025 Happy、在消耗 50 Energy 的專項 Gym 中訓練，並具有 19% 的 Steadfast Faction 加成。

### 各種 Cans 的 SE Cap 臨界點

- 5e Cans：
  - 降價後市價約 220k。
  - SE Cap 臨界點：約 250b Stats。
  - 結論：Single stat 小於 250b 時，吃 5e Cans 就比使用 SE 划算 (儘管屬性推進速度極為緩慢)。
- 15e Cans：
  - 降價後市價約 770k。
  - SE Cap 臨界點：約 30b Stats。
  - 結論：花費相對平易近人，適合中期玩家，每日大約只需花費 9.3m。約每 1 至 2 個月的訓練成果可等同於吃一顆 SE。
  - 變動趨勢：受活動週期影響，15e Cans 的價格逐年下跌，SE Cap 臨界點持續穩步上升，玩家可能需要數年甚至更長時間才能真正達到它的 SE Cap。
- 30e Cans：
  - 價格相對穩定。
  - SE Cap 臨界點：約 3.7b Stats。

### SE 結論

- 便宜的 Cans 現在具有非常高的成本效益。
- Booster Cooldown 冷卻完畢時，應堅持喝便宜 Cans。
- 結合便宜 Cans 與 Exponential gym gains formula，即便處於相對高的 Battlestats 階層，Cans 的性價比依然高於 SE。

## 書籍系統規則 (Books System Overview)

書籍 (Books) 是 Torn 中極稀有且具備強大戰術價值的一次性資源。

### 書籍取得途徑

- 月費訂閱獎勵 (Subscriber Rewards)：最常見途徑。
- 任務商店兌換 (Mission Shop)：次之。
- 城市隨機拾取 (City Finds)：極罕見。

### 閱讀規則

- 週期與限制：每本書需花費 31 天實時時間讀完，一次只能閱讀一本。
- 唯一性：書籍無法交易或出售，每位玩家每種書只能獲得/閱讀一次。
- 收藏化：閱讀後書籍會保留在物品欄中，但僅供展示。
- 續讀機制：只能透過 Book: Memories and Mammaries 或特殊道具 (如 Ladso Eye) 延長或重複前一本書的加成效果。

### 閱讀風險控管

- 閱讀高價值書籍期間，最大的威脅是敵對派系的髒彈攻擊。
- 放射病影響：未穿著防護衣時遭遇髒彈，Energy/Nerve/Happy 會瞬間歸零，且可能面臨長時間住院 (輻射病)，這會摧毀 31 天的密集訓練計畫。
- 對策：閱讀頂級書籍期間，考慮穿著或租借 Hazmat Suit 作為保險。

### 閱讀前置準備

- 流程演練：正式讀書前進行 5 天的「模擬操作」，確保 Job Points、Drug Addiction 等狀態能精確銜接。
- 資源對齊：確保所屬派系 (Faction) 與公司 (Company) 的相關加成在接下來的 31 天內保持穩定。

## 書籍完整目錄 (Torn Books Catalog, ID 744-787)

本目錄收錄 Torn Wiki 全部 44 本書 (ID 744-787)，含效果、Mission Credits 價格與使用時機建議。Mission Credits 為 Mission shop 的價格區間。

### 屬性結算增益類 (閱讀完成時結算)

| ID | 書名 | 效果 | Mission Credits | 戰術建議 |
| --- | --- | --- | --- | --- |
| 744 | Brawn Over Brains | Strength +5% (上限 10m) | 678 - 1960 | 建議等到 Strength 達 200m 後使用。 |
| 745 | Time Is In The Mind | Speed +5% (上限 10m) | 1611 - 1985 | 建議等到 Speed 達 200m 後使用。 |
| 746 | Keeping Your Face Handsome | Defense +5% (上限 10m) | 1265 - 1969 | 建議等到 Defense 達 200m 後使用。 |
| 747 | A Job For Your Hands | Dexterity +5% (上限 10m) | 1119 - 1974 | 建議等到 Dexterity 達 200m 後使用。 |
| 748 | Working 9 Til 5 | 所有 Workstats +5% (上限各 2500) | 1348 - 1941 | 建議 Manual, Int, End 均達 50k 後使用。 |

### 讀完結算功能類 (閱讀完成時生效一次)

| ID | 書名 | 效果 | Mission Credits | 戰術建議 |
| --- | --- | --- | --- | --- |
| 749 | Making Friends, Enemies, And Cakes | Friends、Enemies、Targets 清單容量各 +100 | 1215 - 1844 | - |
| 750 | High School For Adults | 免費重置 Merits 一次 | 765 - 1981 | - |
| 751 | Milk Yourself Sober | 移除大量 drug addiction | 984 - 1994 | - |

### 健身房訓練增益類 (閱讀期間持續 31 天)

| ID | 書名 | 效果 | Mission Credits | 戰術建議 |
| --- | --- | --- | --- | --- |
| 757 | Get Hard Or Go Home | 所有 Gym Gains +20% | 820 - 1956 | 建議配合 120+ Feathery Hotel Coupons (FHC) 與 85+ Xanax。 |
| 758 | Gym Grunting - Shouting To Success | Strength Gym Gains +30% | 969 - 1978 | 配合 Fitness Center 職位使用。 |
| 759 | Self Defense In The Workplace | Defense Gym Gains +30% | 811 - 1977 | 配合 Ladies Strip Club 職位使用。 |
| 760 | Speed 3 - The Rejected Script | Speed Gym Gains +30% | 1115 - 1993 | 配合 Fitness Center 並穿著 Sports Sneakers。 |
| 761 | Limbo Lovers 101 | Dexterity Gym Gains +30% | 1199 - 1995 | 配合 Gentlemen's Strip Club 職位使用。 |
| 770 | Ignorance Is Bliss | 快樂值可恢復至上限以上 | 1034 - 1994 | 適合 Stats 低於 50m 的玩家，使用策略見本文件「Ignorance Is Bliss」一節。 |

### 頂級戰略書籍 (閱讀期間持續 31 天)

| ID | 書名 | 效果 | Mission Credits | 戰術建議 |
| --- | --- | --- | --- | --- |
| 782 | Fuelling Your Way To Failure | 能量罐 (Energy Drinks) 效果翻倍 | 652 - 1999 | 遊戲中最強書籍。需準備 1000 罐能量罐 (約 3.5b) 與 10 星 Restaurant 職位。 |
| 785 | Memories And Mammaries | 複製前一本閱讀書籍的效果 | 919 - 1952 | 通常用於延長 Fuelling Your Way To Failure 或 Ugly Energy。 |
| 784 | Ugly Energy | 最大能量上限提升至 250 (含 energy refill) | 1242 - 1994 | 配合大幅增加能量上限與 124 FHC 使用。 |

### Fuelling Your Way To Failure 準備量精算 (Energy Drink Prep Calculation)

以最大值假設精算，全程無中斷使用，忽略睡眠/住院損耗。

- 基礎參數：
  - 單罐 Energy Drink 基礎恢復：30e。
  - 基礎冷卻：2h。配合 Restaurant 10 星特殊 Professional Metabolism (消耗品冷卻 -25%) 後，實際 CD = 1.5h。
  - 加成倍率：faction x1.5、book x2、event x2 (event 期間疊乘後為 6x，非 event 期間為 3x)。
- 單輪讀書週期 (31 天 = 744h)，event 掌握時機可延伸至 96h：
  - Event 96h：64 罐 x 30e x 6 = 11,520e
  - 非 Event 648h：432 罐 x 30e x 3 = 38,880e
  - 單輪合計：496 罐、50,400e
- 搭配 Memories And Mammaries 延長第二輪 (無 event 加成)：744h / 1.5h CD = 496 罐 x 30e x 3 = 44,640e
- 兩輪總計：
  - 總罐數：496 + 496 = 992 罐 (與約 1000 罐的估計吻合)
  - 總額外 Energy：50,400 + 44,640 = 95,040e

### 消耗品增益類 (閱讀期間持續 31 天)

| ID | 書名 | 效果 | Mission Credits | 戰術建議 |
| --- | --- | --- | --- | --- |
| 779 | Self Control Is For Losers | 所有消耗品冷卻 -50% | 1216 - 1985 | - |
| 780 | Going Back For More | 所有醫療品冷卻 -50% | 1753 - 1985 | - |
| 781 | Get Drunk And Lose Dignity | 酒類效果翻倍 | 968 - 1970 | - |
| 783 | Yes Please Diabetes | Candy 效果翻倍 | 1340 - 1993 | - |

### 自然恢復增益類 (閱讀期間持續 31 天)

| ID | 書名 | 效果 | Mission Credits | 戰術建議 |
| --- | --- | --- | --- | --- |
| 774 | Higher Daddy, Higher! | Energy 恢復 +20% | 1180 - 1948 | - |
| 775 | The Real Dutch Courage | Nerve 恢復翻倍 | 1526 - 1938 | - |
| 776 | Because I'm Happy - The Pharrell Story | Happy 恢復翻倍 | 1413 - 1965 | - |
| 777 | No More Sick Days | Life 恢復翻倍 | 1261 - 1988 | - |

### 戰鬥與戰爭書籍 (閱讀期間持續 31 天)

| ID | 書名 | 效果 | Mission Credits | 戰術建議 |
| --- | --- | --- | --- | --- |
| 752 | Fight Like An Asshole | 所有戰鬥屬性被動 +25% | 1095 - 1985 | 用於大型戰爭、Dog Tags 或越級打怪。 |
| 753 | Mind Over Matter | Strength 被動 +100% | 1321 - 1999 | - |
| 754 | No Shame No Pain | Defense 被動 +100% | 1069 - 1962 | - |
| 755 | Run Like The Wind | Speed 被動 +100% | 1653 - 1986 | - |
| 756 | Weaseling Out Of Trouble | Dexterity 被動 +100% | 1280 - 1994 | - |
| 768 | Stealthy Stealing of Underwear | 最大 Stealth | 1035 - 1947 | 戰爭期間避免暴露身份，需在戰鬥設定中開啟 Stealth 選項。 |
| 764 | Medical Degree Schmedical Degree | 醫院時間減少 50% | 1517 - 1992 | 戰爭或頻繁遭遇髒彈攻擊時非常有用。 |
| 778 | Duke - My Story | Duke 會隨機反擊你的攻擊者 | 目前無法取得 | 用於領土防守，增加對手的進攻難度。 |
| 787 | Running Away From Trouble | 攻擊中的逃跑必定成功 | 711 - 1999 | - |

### 犯罪與功能實用書籍 (閱讀期間持續 31 天)

| ID | 書名 | 效果 | Mission Credits | 戰術建議 |
| --- | --- | --- | --- | --- |
| 762 | The Hamburglar's Guide To Crime | 犯罪技能與 CE 獲取 +25% | ??? - 1771 | 配合 Crimes 2.0 或大量消耗神經值的活動使用。 |
| 765 | No More Soap On A Rope | 監獄時間減少 50% | 1261 - 1998 | - |
| 769 | Shawshank Sure Ain't For Me! | Jail bust 與越獄大幅加成 | 1096 - 1996 | - |
| 763 | What Are Old Folk Good For Anyway? | 升級 EXP 獲取 +25% | 1377 - 1978 | - |
| 771 | Winking To Win | Contract 的 credit 與金錢獎勵翻倍 | 582 - 1926 | - |
| 773 | Hot Turkey | 不累積 drug addiction | 1432 - 1947 | - |
| 772 | Finders Keepers | 大幅提升城市拾取機率 | 1167 - 1999 | 建議在意識週 (Awareness Week) 期間使用。 |
| 766 | Mailing Yourself Abroad | 旅遊時間減少 25% | 1026 - 1976 | 推薦 7 月狩獵週使用，或用於快速往返旅遊獲利。 |
| 767 | Smuggling For Beginners | 旅遊載貨量 +10 | 1094 - 1993 | 配合 PI 與 Large Suitcase 使用，極大化貿易收益。 |

### 公司與工作類 (閱讀期間持續 31 天)

| ID | 書名 | 效果 | Mission Credits | 戰術建議 |
| --- | --- | --- | --- | --- |
| 786 | Brown-nosing The Boss | 大幅提升讀者本人的員工效能 | 948 - 1981 | API 顯示為 employee effectiveness 的 `book` 項 +50。 |

## Ignorance Is Bliss 書籍 (99k Happy 訓練)

Ignorance Is Bliss 是極稀有書籍，讓 Happy 在 31 天閱讀期間不會重置。

### 書籍核心機制

- 主要效果：31 天閱讀期間內，Happy 值不會在每小時的 00, 15, 30, 45 分鐘重置回基礎上限。
- 數值上限：Happy 可手動推升至最高 99,999，且在此期間維持在該水準 (訓練會消耗少量 Happy，但不會因時間重置)。
- 屬性增益：Happy 越高，訓練時每單位 Energy 獲得的屬性越多。此增益對低屬性 (特別是低於 50m) 效果最為顯著。

### 閱讀前的準備

- 屬性調整：Happy 的邊際效益在低屬性時最高，建議閱讀前先將高屬性練高，開書後全力訓練最低的屬性。最低屬性在訓練期間追平時，可切換至新的最低屬性。
- 時間避讓：與派系領導人確認 31 天內無連擊 (Chain) 計畫，避免將 Energy 浪費在非訓練的攻擊上。
- 堆疊能量：開書前先使用 Xanax 將 Energy 堆疊至 1,000e。

### 提升 Happy 至 99k 的流程

提升過程主要依靠 Erotic DVD (EDVD) 與 Ecstasy。基礎 Happy 假設為居住在 Private Island (PI) 的 4,400 (滿配可達 5,025)。

- 方式一：4 EDVD 方案 (常規)
  1. 使用 4 個 EDVD (增加 10,000 Happy)，使 Happy 達到 14,400。
  2. 使用 1 個 Ecstasy 將 Happy 翻倍至 28,800。
  3. 等待 3.5 小時 (Ecstasy 冷卻結束) 後，使用第 2 個 Ecstasy 翻倍至約 57,600。
  4. 再等待 3.5 小時，使用第 3 個 Ecstasy 翻倍至 99,999。
  - 總計消耗：4 EDVD、3 Ecstasy，歷時約 11 小時。
- 方式二：9 EDVD 方案 (需派系 48 小時 Booster Cooldown 加成)
  1. 使用 9 個 EDVD (增加 22,500 Happy)，使 Happy 達到 26,900。
  2. 使用 1 個 Ecstasy 將 Happy 翻倍至 53,800。
  3. 等待冷卻後，使用第 2 個 Ecstasy 翻倍至 99,999。
  - 總計消耗：9 EDVD、2 Ecstasy。此方案更快速且減少一次 Ecstasy 的 OD 風險，但成本較高。

### 31 天訓練策略

- 每日消耗：每天服用 3 個 Xanax 並進行 1 次 Energy Refill (消耗 30 Points)。
- 能量罐搭配：資金充裕時，可每天使用 12 個能量罐 (10e, 20e 或 30e)。量力而為，維持 31 天的一致性。
- 股票收益：持有 MCS 股票時，應微調開書時間，確保在 31 天內能領取 5 次每週的能量產出。

### 過量服用 (OD) 應對

- 影響：使用 Xanax 或 Ecstasy 發生 OD 時，Happy 值會瞬間歸零。
- 重建流程：
  1. 進行 Rehab 戒毒，使 Happy 回復到基礎上限 (例如 4,400)。
  2. 等待 Booster Cooldown 清空。
  3. 重複上述提升 Happy 的流程，重新將 Happy 推回 99,999。
  4. 重建期間切勿堆疊 Energy，正常消耗即可。
- 防範 OD：可考慮加入 7-star Nightclub (OD 機率減少 50%)。

### 隱蔽性防範

- 絕對保密：不要在論壇、Discord 或派系公開頻道提及正在使用此書。
- 潛在威脅：其他玩家得知後，可能使用垃圾 (dog poop)、衛生紙 (toilet paper)、臭氣彈 (stink bombs)、槲寄生 (poison mistletoe) 等道具惡意摧毀你的 Happy。

### 相關公司職位加成

- 10-star Adult Novelties：Erotic DVD 效果翻倍 (極度推薦)。
- 7-star Nightclub：藥物 OD 機率降低 50%。
- 10-star Fitness Center：健身房屬性收益增加 3% 且 Happy 消耗減半。
- 7-star Candle Shop / 10-star Farm：提供高額 Energy 兌換。

## 毒品成癮與戒斷 (Drug Addiction & Rehab)

使用 Xanax 與其他毒品會累積成癮度 (Addiction)，長期忽視會對角色產生負面影響。

### 成癮的代價

- 屬性懲罰：降低 Gym 訓練增益與工作能力 (Work Stats)。
- 教育風險：成癮度達 6% 時，有機率被 Education 課程開除，需重頭開始。
- 職業風險：高等玩家經營的公司通常要求成癮度維持在 5% 以下，否則會被踢出。
- 監測：介面上的大腦圖示由灰轉紅，表示成癮程度加重。

### 戒斷方式

- 瑞士戒毒中心 (Switzerland Rehab Center)：
  - 方式：旅遊前往瑞士 (Switzerland)。
  - 成本：每單位 $250,000。
  - 策略：戒毒時保留一個單位不使用 (即差一個單位全清)，以減緩後續 Rehab 效益遞減。
- 自然衰減：停止吸毒，隨時間緩慢恢復。效率極低，不推薦。

### 成癮管理

- 派系 (Faction) Toleration 加成：最高可減少 50% 成癮累積與 30% 過量 (OD) 機率。
- 週期性清理：成癮度接近 5% 前，配合出國購物的行程順便在瑞士完成戒毒。

## External sources

- [Torn forum: combat and gear guide](https://www.torn.com/forums.php#/p=threads&f=61&t=16252083&b=0&a=0)
- [Torn forum: armor analysis](https://www.torn.com/forums.php#/p=threads&f=61&t=16399253&b=0&a=0)
- [Torn Wiki: Armor - Advanced Armor Bonuses](https://wiki.torn.com/wiki/Armor#Advanced_Armor_Bonuses)
- [Torn Wiki: Battle Stats](https://wiki.torn.com/wiki/Battle_Stats#Increasing.2FDecreasing_Battle_Stats)
- [Needles video](https://www.youtube.com/shorts/C_tB9OFw4IM?feature=share)
- [Torn Wiki: Weapon Mod](https://wiki.torn.com/wiki/Weapon_Mod)
- [Vladar gym gains spreadsheet](https://docs.google.com/spreadsheets/d/1_-2F84ac3ggUD8I9fzrHiv_aTk5AA2hsjo7Cr365SCA)
- [Torn forum: Happy Jumping guide](https://www.torn.com/forums.php#/p=threads&f=61&t=16287997&b=0&a=0)
- [Torn forum: SE Cap analysis](https://www.torn.com/forums.php#/p=threads&f=2&t=16528513&b=0&a=0)
- [Hank's Ratio / Baldr's Ratio Guide by Baldr](https://www.torn.com/forums.php#/p=threads&f=61&t=16132234&b=0&a=0)
- [Torn forum: Happy and property guide](https://www.torn.com/forums.php#/p=threads&f=61&t=16034448&b=0&a=0)
- [Torn forum: Books guide](https://www.torn.com/forums.php#/p=threads&f=61&t=16143719&b=0&a=0)
- [Torn Wiki: Books](https://wiki.torn.com/wiki/Books)
- [Torn forum: Ignorance Is Bliss guide](https://www.torn.com/forums.php#/p=threads&f=61&t=16225087&b=0&a=0)
- [Torn forum: Addiction and rehab guide](https://www.torn.com/forums.php#/p=threads&f=61&t=16364169&b=0&a=0)
- [Torn forum: Choco Jump guide](https://www.torn.com/forums.php#/p=threads&f=61&t=16077517&b=0&a=0)
