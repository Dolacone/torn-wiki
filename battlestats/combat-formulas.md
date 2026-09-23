# 戰鬥機制與計算公式 (Combat Formulas)

## 戰力總量計算 (Battle Stats Score)
- BS (Battle Stats) = 四項屬性合計總量。
- BSS (Battle Stats Score) = sqrt(str) + sqrt(def) + sqrt(spd) + sqrt(dex)。
- 計算原理：屬性分配愈集中，相同 BSS 下的總屬性 (BS) 愈高。

## 命中率計算 (Hit Chance)
- 核心邏輯：速度 (Speed) 與 敏捷 (Dexterity) 的對抗。
- 比例門檻（基於 Wiki 實測數據）：
  - 50% 命中：比例 1:1。
  - 80% 命中：速度約為敏捷的 4.5 倍。
  - 10% 命中：敏捷約為速度的 10 倍。
  - 0% 命中：敏捷是對手速度的 64 倍（或速度為 0% 命中時的 64 倍）。
- 命中率對稱性質：比值 R = Speed / Dexterity 與 1/R 的命中率相對於 50% 呈完美對稱，即 f(R) + f(1/R) = 1。
- 計算模型：
  - 簡化對數擬合：
    公式：Hit Chance = MAX(0, MIN(1, 0.5 + 0.278 * LOG10(Speed / Dexterity)))
    局限：此公式僅在 64 倍極端值時準確，但在中段（1.5x 至 20x）會嚴重低估命中率（例如 2 倍速度時，實際為 66.74%，此公式僅算得 58.37%）。
  - 中低倍數精確擬合（4 倍以內）：
    公式：Hit Chance ≈ 0.5 + 0.48 * LOG10(Speed / Dexterity)
  - 簡化 Logistic 理論模型：
    公式：Hit Chance ≈ 1 / (1 + (Dexterity / Speed))
    說明：在 1x 至 4x 區間誤差小於 1.5%。特別地，當 Speed = Dexterity 時，命中率完全取決於武器的 Accuracy 數值（例如 65 Accuracy 即為 65% 命中率）。

### Google Spreadsheet 簡化公式（極端值擬合版）
- 假設 A2 為敏捷，B2 為對手速度。
- 公式內容：
```excel
=MAX(0, MIN(1, 0.5 + 0.278 * LOG10(B2 / A2)))
```

## 傷害減免與護甲 (Damage Mitigation & Armor)
- 核心邏輯：防禦 (Defense) 與 力量 (Strength) 的對抗。
- 減傷門檻與分段公式：
  - 屬性優勢段（Defense >= Strength）：
    公式：Mitigation = MAX(0, MIN(1, 0.5 + 0.435 * LOG10(Defense / Strength)))
    臨界點：當 Defense 為 Strength 的 14.11 倍（約 14 倍）時，減傷率達到 100%。
  - 屬性劣勢段（Defense < Strength）：
    公式：Mitigation = MAX(0, MIN(1, 0.5 + 0.332 * LOG10(Defense / Strength)))
    臨界點：當 Strength 為 Defense 的 32 倍（即 Defense 為 1/32 倍）時，減傷率降至 0%。
- 護甲效果：D(A) = D(I) * (1 - A/100)
  - D(A) 為實收傷害，D(I) 為初始傷害，A 為護甲值。
  - 標準參考值：45% 護甲對應 0.55 的受傷係數。詳細護甲機制參見 [[attacking/combat-mechanics]]。

## 屬性分配強度總結
- 相同 BSS 下，4:3:3:0 分配型的總 BS 比平均型高出約 34%。
- 無道具環境：防禦特化型 (D) 具備最高換血效率。
- 道具干擾環境：敏捷特化型 (X) 配合 Spd/5 道具能將生存率極大化，詳見 [[attacking/temporary-tactics]]。
- 屬性比例分配原則參見 [[battlestats/training-ratios]]。
