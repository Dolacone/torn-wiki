# 戰鬥機制與計算公式 (Combat Formulas)

## 戰力總量計算 (Battle Stats Score)
- BS (Battle Stats) = 四項屬性合計總量。
- BSS (Battle Stats Score) = sqrt(str) + sqrt(def) + sqrt(spd) + sqrt(dex)。
- 計算原理：屬性分配愈集中，相同 BSS 下的總屬性 (BS) 愈高。

## 命中率計算 (Hit Chance)
- 核心邏輯：速度 (Speed) 與 敏捷 (Dexterity) 的對抗。
- 比例門檻：
  - 50% 命中：比例 1:1。
  - 80% 命中：速度約為敏捷的 4.5 倍。
  - 10% 命中：敏捷約為速度的 10 倍。
  - 0% 命中：敏捷是對手速度的 64 倍。

### Google Spreadsheet 公式
- 假設 A2 為敏捷，B2 為對手速度。
- 公式內容：
```excel
=MAX(0, MIN(1, 0.5 + 0.278 * LOG10(B2 / A2)))
```

## 傷害減免與護甲 (Damage Mitigation & Armor)
- 核心邏輯：防禦 (Defense) 與 力量 (Strength) 的對抗。
- 減傷門檻：
  - 50% 減傷：比例 1:1。
  - 100% 減傷：防禦約為力量的 14 倍。
- 護甲效果：D(A) = D(I) * (1 - A/100)
  - D(A) 為實收傷害，D(I) 為初始傷害，A 為護甲值。
  - 標準參考值：45% 護甲對應 0.55 的受傷係數。

## 屬性分配強度總結
- 相同 BSS 下，4:3:3:0 分配型的總 BS 比平均型高出約 34%。
- 無道具環境：防禦特化型 (D) 具備最高換血效率。
- 道具干擾環境：敏捷特化型 (X) 配合 Spd/5 道具能將生存率極大化。
