# Torn 經濟與公司參考 (Economy and Companies)

本文件涵蓋 Torn 的公司 (Company) 系統、各類公司 Special 與星級效果、員工 Effectiveness 計算、Oil Rig 收益試算、現金保護與儲存、城市商店轉售、出國旅遊貿易，以及 Private Island (PI) 規劃。

## 公司分類總覽 (Company Categories)

公司依功能分為五類：

- 能量與訓練公司：提供 Energy、Training 增益或 Happy。
- 犯罪公司：提升 Nerve、Crime Experience (CE) 或 Crime 成功率。
- 收入與貿易公司：增加現金、Travel Items 上限及 Awareness。
- 戰鬥與戰爭公司：戰鬥加成、Defense 與 Stealth 性能。
- 特殊與利基公司：Education 縮短、Racing 與 Addiction 管理。

### 員工 Effectiveness 的 Merits 投入時機

- Effectiveness 的完整組成與計算方式見本文件「員工 Effectiveness 計算」一節。
- 初級玩家：Workstats 較低時，建議先買 Trains 或加入有輪流訓練的公司，不要把 Merits 投在 Employee Effectiveness。
- 中後期玩家：Workstats 提高、目標是加入 10 星高階公司 (如 TV Network 電視台) 時，投入 Merits 的效益會隨屬性呈指數級增長。

### 新手工作推薦 (Starter Job Recommendations)

- 第 0 天：至少加入 3 星 Music Store (音樂商店)，持續服用 3 顆 Xanax 訓練，主攻 Dexterity。
- 解鎖最終 Gym 後：轉往 5 星以上的 Mining Corporation (礦業公司)，利用 JP 拉高 Defense，保持屬性平衡後再轉攻 Defense。

## 員工 Effectiveness 計算 (Employee Effectiveness)

- 來源範圍：working stats 公式來自官方 Torn Wiki Company 頁。
- 自行推算部分：BUS2110 倍率、取整方式、management 資料點，以 2026-10-15 一家 Nightclub 12 名員工的 Torn API 資料比對得出。

### Effectiveness Total 組成

API v2 `/company/employees` 的 `effectiveness` 欄位直接相加即為 `total` (12 人全部吻合)：

```
total = working_stats + settled_in + book + merits + director_education
      + management + wrong_gender + addiction + inactivity
```

| 欄位 | 說明 |
|---|---|
| working_stats | 依職位需求計算，見下節 |
| settled_in | 每連續 24 小時 +1，上限 +10 |
| book | 員工本人閱讀 Brown-nosing The Boss 期間 +50，持續 31 天 |
| merits | Employee Effectiveness merits 每點 +1 |
| director_education | Director 修完全部課程時為 +12 |
| management | working_stats 低於 100 時的補償，見下節 |
| addiction | 依 addiction points 扣分 |
| inactivity | 依未活動時間扣分 |

### Working Stats 公式

官方 wiki 公式：每個需求不為 0 的 stat 各算一次，各自 floor 後相加。

```
eff(stat, req) = FLOOR(MIN(45, (45 / req) * stat) + MAX(0, 5 * LOG(stat / req, 2)))
working_stats  = eff(primary) + eff(secondary)
```

自行推算的修正：

- Director 修完 BUS2110 時，stat 先乘 1.2 再代入公式。
- 取整必須每項各自 floor。先加總再 floor 會讓部分員工多 1 分。
- Effectiveness 每天只計算一次。之後調整職位或 stat 變動，都要等下一次計算才會反映。

```
eff(stat, req) = FLOOR(MIN(45, 45 / req * stat * 1.2) + MAX(0, 5 * LOG2(stat * 1.2 / req)))
```

範例 (BUS2110，req 13500 / 27000)：

| stat | 計算 | eff |
|---|---|---|
| 13500 / 27000 | 45 + 5*log2(1.2) = 46.3 | 46 + 46 = 92 |
| 6750 / 13500 | 45/13500*8100 = 27 | 27 + 27 = 54 |

職位需求由 API v2 `/torn/{typeId}/companies` 的 `positions[].working_stats.required` 取得。

### Management 補償

- working_stats 越低，management 越高，上限 30。
- working_stats 100 以上時 management 為 0。
- 公式未知，而且不只跟 working_stats 有關。

2026-11-03 以同一家 Nightclub 82 筆不同的非 Manager 員工效能明細比對：

- 同一個 working_stats 會對應不同的 management，例如 63 對應 13-16、82 對應 6-7、94 對應 2-4。
  - 推測與當天 Manager 的狀態有關，未驗證。
- book 會計入：一名 working_stats 90、book +50 的員工 management 為 0，同 working_stats 無 book 的員工為 5。
  - x 改用 100 - (working_stats + book) 後與此吻合，目前只有這 1 筆資料。
- 最佳候選 ceil(0.54 * x^0.885) 完全吻合 60/82 筆 (x 含 book 時 61/82)。

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

以下候選公式都吻合上表 (x = 100 - working_stats，結果上限 30)。working_stats 40-70 之間的預測互不相同，需要更多資料點才能決定：

```
floor(0.84 * x^0.795)
round(0.70 * x^0.83)
ceil (0.54 * x^0.885)
ceil (46.5 * ln(1 + x/105))
```

- Manager 本人是否也拿得到 management 加成未驗證。

## 能量與訓練公司 (Energy & Training Companies)

### JP 換 Energy：基礎兌換 (1 JP = 3 Energy)

- Furniture Store (家具店)：1 星。
- Pub (酒吧)：1 星。
- Restaurant (餐廳)：1 星。

### JP 換 Energy：進階兌換

- Candle Shop (蠟燭店)：7 星，1 JP 換 5 Energy。
- Game Shop (遊戲店)：10 星，1 JP 換 1 Nerve、5 Energy、50 Happy。
- Farm (農場)：10 星，1 JP 換 7 Energy，全遊戲最高的 JP 轉 Energy 比率。

### Nerve 相關公司

- Pub (酒吧)：
  - 5 星：25 JP 換 Nerve 全額補滿 (Nerve Refill)。
  - 10 星：被動 +15 最大 Nerve，犯罪必備。
- Candle Shop (蠟燭店)：5 星，1 JP 換 2 Nerve。

### 訓練與 Happy 增益

- Adult Novelty (成人用品店)：
  - 10 星 Indecent (被動)：Erotic DVD 的 Happy 加成提升 100%。
  - 建議：適合能負擔頻繁 Happy Jump 的玩家。
- Sweet Shop (甜食店)：
  - 10 星 Voracious (30 JP)：提供 4.5k Happy。
  - 7 星 Energy Rush (15 JP)：獲得 Cans。
- Music Store (音樂商店)：
  - 3 星：Gym XP 提升 30%，可快速解鎖進階 Gym。
  - 建議：解鎖高級 Gym 的最佳跳板。
- Fitness Center (健身中心)：10 星，被動 Gym gains +3%。
- TV Network (電視台)：10 星獎勵，25 JP 隨機獲得 300 Energy。

## 犯罪公司 (Crime Companies)

在 Crimes 2.0 中，部分公司提供被動的 +15% Crime Experience (CE) 與 Crime Skill (CS) 加成。這是練技能 (衝刺 CS100) 的最快路徑。

| 犯罪類別 | 包含犯罪 | 官方推薦公司 | 星級 |
|---|---|---|---|
| Theft (盜竊) | Search for Cash、Shoplifting、Pickpocketing、Burglary | Furniture Store (家具店) | 5 星，全遊戲最低星級門檻 |
| Fraud (詐騙) | Card Skimming、Hustling、Scamming | Car Dealership (汽車經銷商) | 7 星 |
| Counterfeiting (仿冒) | Bootlegging、Forgery | Theater (劇院) | 7 星 |
| Illicit Services (非法服務) | Disposal | Nightclub (夜總會) | 3 星，極易進入 |
| Cybercrime (網路犯罪) | Cracking | Software Corporation (軟體公司) | 7 星 |
| Vandalism (破壞) | Arson 2.0、Graffiti | 官方未提供 15% 加成公司 | - |

- Illicit Services 備註 (Crimes 1.0 遺產)：Law Firm (律師事務所，3 星) 與 Meat Warehouse (肉類倉庫，7 星) 的 25% 加成主要針對 1.0 的成功率。在 2.0 中建議優先選 Nightclub 以加速進度。
- Vandalism 替代方案：Amusement Park (遊樂園) 10 星提供全類別 10% 進度加成，是目前破壞類別的最高加成路徑。

### 犯罪相關的其他公司功能

- Pub (酒吧)：10 星 +15 最大 Nerve，是所有犯罪路徑的必經之處。
- Meat Warehouse (肉類倉庫)：5 星，失敗時的 CE 懲罰減免 50%，適合高風險犯罪衝刺。
- Candle Shop (蠟燭店)：7 星，1 JP 換 5 Energy。此為 JP 兌換，不是被動犯罪加成。

## 收入與貿易公司 (Income & Trading Companies)

### Travel Items 攜帶上限加成

- Lingerie Store (內衣店)：
  - 10 星：免費商務艙飛行 (額外 10 個攜帶量，快速飛行)。
  - 3 星：Travel Items 上限 +2。
  - 建議：最活躍海外旅行玩家的首選。
- Cruise Line Agency (郵輪代理)：
  - 10 星：Travel Items 上限 +3。
  - 3 星：Travel Items 上限 +2。
- Flower Shop (花店) / Toy Shop (玩具店)：
  - 7 星：國外可多攜帶 5 個花朵或玩偶。
  - 10 星：查看各國庫存。

### Oil Rig (鑽油平台) Specials

- 10 星：銀行投資金額上限 +50%。
- 7 星：Cayman Islands 利息 +10%。
- 建議：養老與最大化被動收入，搭配現金保護策略使用。

| 星級 | Special | 花費 | 效果 |
|---|---|---|---|
| 1★ | Danger Money | 1 JP | 換取現金，約 $10k/JP |
| 3★ | Embargo | 50 JP | 目標 Happy 減半，可出售此服務 |
| 5★ | Oil Mogul | 3 JP | 銀行投資剩餘時間 -1 小時 |
| 7★ | Tax Haven | 被動 | Cayman 利息 +10% |
| 10★ | Fat Cat | 被動 | 銀行投資上限 +50% ($2b -> $3b) |

- 員工每日 JP = 公司星級。10★ 每日 10 JP。
- 一次 Oil Mogul 的價值 = 全部銀行本金 1 小時的利息。

### Oil Rig 收益試算 (2026-10-17，不含薪資)

試算前提：$2b 銀行投資 90 天收益 $390m。$1b 的其他用途收益以 $1.6b 穩定賺 $850k/day 等比例換算。

```
每日利息 / $1b        = $390m / 90 / 2        ≈ $2.167m
機會成本 / $1b        = $850k / 1.6b × 1b     ≈ $0.531m

Fat Cat 淨值          = $2.167m - $0.531m     ≈ $1.635m/day
Oil Mogul (10 JP)     = $3b 的 3.33 小時利息  ≈ $0.903m/day
------------------------------------------------------------
10★ 淨合計                                    ≈ $2.538m/day ≈ $228m / 90 天
```

- 驗算：每日 3.33 次 Oil Mogul 把 90 天週期縮短為 79.02 天。$3b 一期 $585m，每日 $7.403m。減去 $2b 的每日 $4.333m，毛利 $3.069m，與 Fat Cat 毛利加 Oil Mogul 相同。
- 本金只有 $2b 時：Fat Cat 無效益，Oil Mogul 10 JP ≈ $0.60m/day，無機會成本。
- 5★ 公司 (5 JP/day)，本金 $2b：Oil Mogul ≈ $0.30m/day。
- Embargo 以 $6m/次出售時約 $120k/JP，高於 Oil Mogul 的 $90k/JP (本金 $3b)，前提是有穩定買家。
- Tax Haven 收益 = Cayman 每日利息 × 10%，未計入上表。

### 其他收入公司

- TV Network (電視台)：工資極高，10 星獎勵包含高價值的隨機支付。
- Property Broker (房地產經紀)：
  - 7 星：150 JP 換取隨機地產。
  - 10 星：地產升級 10% 折扣。
- Logistic Management (物流管理)：10 星，250 JP 提升指定公司生產力，可出售此服務。

### 市場交易與 Awareness 增益

- Car Dealership (汽車經銷商) / Property Broker (房地產經紀)：5 星，Item Market 與 Auction House 上架免手續費。
- Candle Shop (蠟燭店) / Firework Stand (煙火攤) / Zoo (動物園)：3 星或 7 星提升 Awareness，增加獲得高品質物品與 SE 的機率。

### 特殊收入服務

- Adult Novelty (成人用品店) / Sweet Shop (甜食店)：低星級可換取現金。
- Cyber Cafe (賽博咖啡店)：查看玩家投資帳戶詳情。
- Software Corporation (軟體公司)：駭入公司資金。
- Detective Agency (偵探事務所)：增加飛行時間服務、查看好友/黑名單服務。

## 戰鬥與戰爭公司 (Combat & Warring Companies)

### 攻擊輸出與武器加成

- Gun Shop (槍店)：
  - 10 星：主/副武器 Damage +10%。
  - 7 星：額外一個彈夾 (適合 Peppered Merits)。
  - 5 星：可查看目標的裝備與彈藥。
  - Meta 價值：後期最重要的 Job Points 消耗處之一，用於兌換 Special Ammo (如 Incendiary)。
- Furniture Store (家具店)：
  - 10 星：Fist & Kick Damage +100%。
  - 7 星：被動 Strength +25%。
- Restaurant (餐廳)：3 星，近戰武器 Damage +10%。
- Hair Salon (美髮沙龍)：10 星，Slashing 武器 Damage +20%。

### 防禦與生存能力

- Gas Station (加油站)：
  - 5 星：被動 10% 機率 Restore 20% Life (Cauterize)。
  - 7 星：燒傷 Damage 減少 50%。
  - 建議：Defense 型玩家 (Tank) 的最強 Armor 公司。
- Mining Corporation (礦業公司)：
  - 10 星：25 JP 將當前 Life 提升至 150%。
  - 7 星：最大 Life +10%。
- Clothing Store (服飾店)：
  - 10 星：Armor 係數 +20%。
  - 5 星：被動 Dexterity +25%。
- Private Security Firm (私人保全公司)：
  - 7 星：Armor 套裝加成 +25%。
  - 3 星：閃光彈強度 +50%。
- Strip Clubs (脫衣舞俱樂部)：
  - 10 星：1/4 機率閃避近戰 (男子)；近戰 Damage 減少 30% (女子)。
  - 5 星：Tyrosine (Dexterity) 或 Serotonin (Defense) 效果 +50%。
  - Meta 價值：2021 戰鬥更新後的頂級公司，大幅強化 Needles 的效果與持久戰能力。必須配合 Loadouts 操作。

### 隱密與戰略功能

- Music Store (音樂商店) / Theater (劇院)：7 星 / 3 星，提供最高 Stealth (Maximum Stealth)。
- Hair Salon (美髮沙龍) / Music Store (音樂商店)：5 星，降低敵方 Stealth (易於反擊)。
- Zoo (動物園)：10 星，+3.00 Accuracy。
- Logistic Management (物流管理)：5 星，允許在住院期間從國外飛回。
- Amusement Park (遊樂園)：7 星，Epinephrine 效果與持續時間 +25%。

## 特殊與利基公司 (Specialized & Niche Companies)

### Education 加速

- Hair Salon (美髮沙龍)：7 星，1 JP 縮短 30 分鐘 Education 時間。想快速刷完 Education 課程的首選。
- Fitness Center (健身中心)：1 JP 縮短 30 分鐘 Education 時間。

### Racing 增益

- Mechanic Shop (機械店)：
  - 10 星：Driving Skill 獲得 +50%。
  - 1 星：5 JP 換 1 Racing Point。
  - 建議：追求 10 Racing Skill 與賽車獎牌的關鍵公司。
- Car Dealership (汽車經銷商)：1 星，5 JP 換 1 Racing Point。
- TV Network (電視台)：10 星獎項，有機率獲得 +0.25 Driving Skill。

### Addiction 與健康管理

- Night Club (夜總會)：
  - 7 星：被動 Overdose (OD) 機率減少 50%。
  - 5 星：降低 Addiction。
- Flower Shop (花店) / Cruise Line Agency (郵輪代理)：
  - 5 星：1 JP 降低 Addiction。
  - 建議：長期服用 Xanax 的玩家，用來減少 Rehab 次數的高效益選擇。

### 其他特殊功能

- Private Security Firm (私人保全公司)：獲得 Mission Credits，用於購買武器模組 (Weapon Mods)。
- Zoo (動物園)：提升狩獵技能與獎勵。
- Property Broker (房地產經紀)：Property 升級折扣。
- Lingerie Store (內衣店)：免除 Property 維護與員工成本。

## 現金保護與儲存 (Money Protection & Storage)

未受保護的現金隨時可能被 Mugged。

### 現金儲存方式

- Ghost Trades (幽靈交易)：
  - 方法：發起一筆為時 6 小時的物品交易，但不確認。
  - 作用：錢鎖定在交易中，直到 6 小時過期或取消。期間 muggers 無法搶走這筆錢。
- PI Vault (私人島嶼金庫)：
  - 方法：升級 Private Island 獲得 Vault。
  - 作用：最安全、最直接的現金儲存處，隨取隨放。Vault 建設費用極高。
- Asset Conversion (資產轉換)：
  - 方法：把現金換成傳奇武器、Points 或易流通物品 (如 Xanax)。
  - 作用：轉為實物後通常不會被搶，但有市場波動風險。
- Faction Vault (派系金庫)：
  - 方法：存入所屬 Faction 的金庫。
  - 風險：需信任 Faction 管理層。被踢出或 Faction 解散時可能損失。
- Hospital Stay (醫院避難)：
  - 方法：透過俄羅斯輪盤、血袋或故意戰敗進入 Hospital。
  - 作用：住院中無法被 Attack，現金安全。適合處理大額交易前避險。
- Stock Exchange (股票市場)：
  - 條件：花 50 Points 購買 Ticker。
  - 方法：把錢買入股票。賣出時有 0.1% 手續費。
- Bank Investment (銀行投資)：全遊戲最高的穩定 ROI，同時也是長期儲金位。

### 依階段的儲存策略

- 初期 (未租 PI)：主要使用 Ghost Trades 與購買 Points 儲值。
- 中後期：租用或購買帶 Vault 的 PI 作為核心錢包。

## 城市商店轉售套利 (Item Reselling from City Shops)

適用對象：未滿 15 級、資金有限的新手，利用城市商店的每日購買限額轉賣補貼收入。

- 每日限額：每位玩家每天最多在城市商店購買 100 件物品。
- 庫存：物品庫存隨時間變動，熱門物品常被搶購一空。

### 採購清單

- Bits 'N' Bobs (雜貨店)：
  - Beer (啤酒)：週轉率極高，玩家常用於增加 Nerve。
  - Basic Plushies (基礎填充玩偶)：利潤不如出國貿易，但初期仍有穩定套利空間。
- Sally's Sweet Shop (甜蜜商店)：
  - Lollipops (棒棒糖)：能在市場上以原價數倍的價格售出。

### 收益預期

- 每日完成 100 件轉賣，約可獲得 50k - 60k 純利潤 (撰寫時估計，隨市場變動)。
- 這筆錢在初期可用於支付房產租金或購買基本戰鬥裝備。

## 出國旅遊與跨國貿易 (Traveling and Trading)

達到 15 級後，Traveling 是賺取日常開銷與進階物資最穩定的方式。

### 旅遊收益機制

- 模式：前往國外購買 Plushies 或 Flowers，回國後販售給玩家、Traders 或在市場出售。
- 獲利範圍：每日約 3m - 6m 收益 (撰寫時估計，隨市場變動)。

### 提升攜帶量的方式

承載量決定單趟利潤。

- Large Suitcase (大行李箱)：直接購買，+4 容量。可與 PI 配合使用。
- Faction Excursion 功勳：最高 +10 容量。
- Private Island：附帶 Airstrip 與飛行員 (Pilot)，可快速旅行並 +10 容量。
- 公司加成：
  - Toy Shop (7 星)：+5 Plushies。
  - Flower Shop (7 星)：+5 Flowers。
  - Lingerie Store (3 星)：總量 +2。
  - Cruise Line Agency (10 星)：總量 +3。

### 旅遊安全

- 停留風險：在國外時無法使用醫療道具。在國外進醫院會浪費極多時間。
- 登機前準備：
  - 已報名 Racing 時不能飛行。
  - 身上不要攜帶過多現金，防止被搶。
  - 先把 Energy 用完、確認 Drug Cooldown 已結束，避免在飛機上虛耗。
- 下飛機保護：抵達後有 15 秒保護期，需立即買完商品並準備回航。

### 商品販售管道

- Traders：最安全且方便，直接大宗交易，規避被 Buy-mugged 的風險。
- Item Market：需支付 3% 手續費，且有被路人搶劫的風險。
- Bazaar：免手續費但無法匿名，風險極高，建議中後期再使用。

## 私人島嶼規劃 (Private Island, PI)

Private Island 是 15 級後的標準配置，也是達成財務自由的核心工具。

### Landing Strip 配置

租用或購買 PI 時，必須確保配備 Landing Strip 與飛行員 (Pilot)：

- 旅遊加成：飛行時間減少 30%。
- 負重加成：物品攜帶量 +10。
- 成本：3600 Happy 的 PI 租金約每月 12m (撰寫時估計)，額外負重帶來的花卉/玩偶利潤能完全抵銷這筆開銷。

### 租用策略

- 預算有限時：可找 2550 Happy 左右的低階 PI，只要帶有 Landing Strip 即可開始旅遊獲利。
- 高階追求：儘量租用 3600 Happy 以上的 PI，以最大化 Gym Gains。
- 進階載貨：Large Suitcase 與 PI 配合使用，可再 +4 攜帶量。

## External sources

- [Torn Forum: Company guide](https://www.torn.com/forums.php#/p=threads&f=61&t=16215307&b=0&a=0)
- [Company - Torn Wiki](https://wiki.torn.com/wiki/Company)
- [Company Special List - Torn Wiki](https://wiki.torn.com/wiki/Company/Special_List)
- [Oil Rig - Torn Wiki](https://wiki.torn.com/wiki/Oil_Rig)
- [Torn Stats - Oil Rig](https://www.tornstats.com/companies/28)
- [Oil rig and other perks that gives money?](https://www.torn.com/forums.php?p=threads&f=3&t=16323914&b=0&a=0)
- [Selling Embargoes for $6m each](https://www.torn.com/forums.php?p=threads&f=10&t=16233493&b=0&a=0)
- [Torn Stats - Car Dealership](https://www.tornstats.com/companies/4)
- [Torn Stats - Property Broker](https://www.tornstats.com/companies/20)
- [Torn Forum: Money protection, reselling and PI guide](https://www.torn.com/forums.php#/p=threads&f=61&t=16034448&b=0&a=0)
- [Torn Forum: Traveling guide](https://www.torn.com/forums.php#/p=threads&f=61&t=16364169&b=0&a=0)
- 自行推算：2026-10-15 以 API v2 員工資料比對 Effectiveness 公式
