# Gym Gains 公式 (Vladar)

## 單次訓練的 stat 增加量

```
gain = (1/200000) * Dots * E * Mult * ( S_adj * ROUND(1 + 0.07 * ROUND(ln(1 + H/250), 4), 4) + 8 * H^1.05 + A * (1 - (H/99999)^2) + B )
```

- Dots：健身房該項 stat 的 gym dots，例如 Frontline Fitness strength 為 7.5。
- E：每次訓練消耗的 Energy。
- Mult：所有 gym gains 加成相乘，例如 Steadfast +10% 與 Property +2% 為 1.1 * 1.02。
- H：訓練當下的 Happy，上限 99,999。
- S_adj：調整後的 stat，見下節。
- A、B：依訓練的 stat 而定，見常數表。

## 50M 以上的 stat 調整

```
S_adj = S                                          (S < 50,000,000)
S_adj = (S - 50,000,000) / (8.77635 * log10(S)) + 50,000,000   (S >= 50,000,000)
```

- S：要訓練的那項 stat 目前數值。
- 50M 以上的 stat 仍會成長，但成長速度遞減。

## 各 stat 常數

| Stat | A | B | C |
| --- | --- | --- | --- |
| Strength | 1600 | 1700 | 700 |
| Speed | 1600 | 2000 | 1350 |
| Dexterity | 1800 | 1500 | 1000 |
| Defense | 2100 | -600 | 1500 |

- C 決定增加量的範圍：最小值用 B - C 代入，最大值用 B + C 代入。

## Sources

- [Vladar gym gains spreadsheet](https://docs.google.com/spreadsheets/d/1_-2F84ac3ggUD8I9fzrHiv_aTk5AA2hsjo7Cr365SCA)
