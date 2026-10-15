# 員工 Effectiveness 計算 (Employee Effectiveness)

本頁的 working stats 公式來自官方 wiki。BUS2110 倍率、取整方式、management 資料點為自行推算，以 2026-10-15 一家 Nightclub 12 名員工的 [[torn-api]] 資料比對得出。

## Total 組成

API v2 `/company/employees` 的 `effectiveness` 欄位直接相加即為 `total`（12 人全部吻合）：

```
total = working_stats + settled_in + book + merits + director_education
      + management + wrong_gender + addiction + inactivity
```

| 欄位 | 說明 |
|---|---|
| working_stats | 依職位需求計算，見下節 |
| settled_in | 每連續 24 小時 +1，上限 +10 |
| merits | Employee Effectiveness merits 每點 +1 |
| director_education | Director 修完全部課程時為 +12 |
| management | working_stats 低於 100 時的補償，見下節 |
| addiction | 依 addiction points 扣分 |
| inactivity | 依未活動時間扣分 |

## Working Stats

官方 wiki 公式（每個需求不為 0 的 stat 各算一次，各自 floor 後相加）：

```
eff(stat, req) = FLOOR(MIN(45, (45 / req) * stat) + MAX(0, 5 * LOG(stat / req, 2)))
working_stats  = eff(primary) + eff(secondary)
```

自行推算的修正：

- Director 修完 BUS2110 時，stat 先乘 1.2 再代入公式。
- 取整必須每項各自 floor。先加總再 floor 會讓部分員工多 1 分。
- effectiveness 不會在 stat 變動時即時重算。剛增加的 stat 可能還沒反映。

```
eff(stat, req) = FLOOR(MIN(45, 45 / req * stat * 1.2) + MAX(0, 5 * LOG2(stat * 1.2 / req)))
```

範例（BUS2110，req 13500 / 27000）：

| stat | 計算 | eff |
|---|---|---|
| 13500 / 27000 | 45 + 5*log2(1.2) = 46.3 | 46 + 46 = 92 |
| 6750 / 13500 | 45/13500*8100 = 27 | 27 + 27 = 54 |

職位需求由 API v2 `/torn/{typeId}/companies` 的 `positions[].working_stats.required` 取得。

## Management

只跟 working_stats 有關。working_stats 越低，management 越高，上限 30，working_stats 100 以上為 0。公式未知。

觀察到的資料點：

| working_stats | management |
|---|---|
| 0 | 30 |
| 9 | 30 |
| 14 | 28 |
| 37 | 22 |
| 72 | 11 |
| 87 | 6 |
| 90 | 5 |
| 94 | 3 |
| 98 | 1 |
| 100+ | 0 |

以下候選公式都吻合上表（x = 100 - working_stats，結果上限 30），working_stats 40-70 之間的預測互不相同，需要更多資料點才能決定：

```
floor(0.84 * x^0.795)
round(0.70 * x^0.83)
ceil (0.54 * x^0.885)
ceil (46.5 * ln(1 + x/105))
```

Manager 本人是否也拿得到 management 加成未驗證。

## Sources

- [Company - Torn Wiki](https://wiki.torn.com/wiki/Company)
- 自行推算：2026-10-15 以 API v2 員工資料比對公式
