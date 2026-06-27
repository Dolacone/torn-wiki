# 縱火犯罪策略指南 (Arson Crime Strategy)

縱火是一項高度戰術性的 Crimes 2.0 活動，屬於破壞 (Vandalism) 類別。涉及火場物理、材質組合與每日限量的任務管理。

## 術語與基礎定義 (Terminology & Basics)

- CS (Crime Skill)：在犯罪頁面頂部顯示的縱火技能等級。
- Unique：星號標記的唯一發現，每個角色僅能獲得一次。
- Crit (Critical Failure)：嚴重失敗，可能導致 CS 損失、物品遺失甚至住院/進監獄。
- Target：縱火目標，由地點與故事背景定義，影響易燃度與郊區度。
- Area：火場中的各個區域（火焰圖標表示）。
- Accelerant：用於助燃的助燃劑。
- Enhancer (增強器)：Windproof Lighter。取得途徑：Burglarize the Secluded Cabin (Unique)。可提升 5% 的 CE 與 CS 收益。

## 核心動作與神經值消耗 (Core Actions & Nerve)

| 動作 | Nerve 消耗 | 說明 |
| --- | --- | --- |
| INQUIRE | 0 | 詢問背景故事。可用於保留 (Preserve) 任務不被跨日清除。 |
| BREACH | 3 | 進入目標建築。 |
| PLACE | 5 | 放置起始助燃劑 (Starters)。至少需放置一次才能 Ignition。 |
| IGNITE | 5 | 點火啟動量表成長。 |
| STOKE | 5 | 添加燃料 (Fuel)，增加強度與動量。 |
| DAMPEN | 5 | 降低火場強度與動量（用於控制破壞量）。 |
| COLLECT | 2 | 任務完成後領取獎勵。 |
| PLANT EVIDENCE | 5 | 部分任務的要求，需預先放置特定零件。 |

## 火場物理力學機制 (Fire Physical Mechanics)

破壞進度 (Destruction Gauge) 取決於火場的兩個核心數值：

### 強度 (Intensity)
- 代表火勢燃燒的猛烈程度。
- 強度越高，破壞速度越快。
- 當沒有動量 (Momentum) 時，強度會以 0.2/sec 的速度衰減。第一響應者到達後衰減增至 1/sec。
- 背景顏色：黃色最低，紅色最高。紅色強度時進行 Stoke/Dampen 極易發生 Crit。

### 動量 (Momentum)
- 代表火場中尚未燃燒的燃料。
- 動量會被持續消耗轉化為強度。
- 液體助燃劑提供最強動量，氣體最弱。
- 在動量尚未衰減時進行操作會增加意外 (Accident) 風險。

### 持續監控指標說明 (Monitoring Metrics Details)
- Suspicion (懷疑度)：影響「保險索賠 (Insurance Claim)」等任務的成功。Methane 可降低此值。
- Visibility (能見度)：影響消防隊被調度的時間。

## 環境影響參數分析 (Environment Parameter Analysis)

### 易燃度 (Flammability)
等級 1-5。等級 5 目標完全燒毀僅需 50 秒，等級 1 則需 250 秒。

### 郊區度 (Rurality)
影響反應時間 (Response Time)。等級 1 (都市) 給予 30 秒操作時間，等級 5 (荒郊) 給予增至 480 秒。

### 火場區域 (Areas)
目標大小不同，區域數也不同 (1-5)。液體與氣體助燃劑具備擴散 (Spread) 屬性，可同時影響多個區域。

## 任務管理與保留機制 (Job Management & Preservation)

- 任務更新：每日 00:00 TCT 生成，所有玩家任務相同。
- 保留機制：與任務互動（如 Inquire）可防止其在換日後消失，但若新生成的任務與保留的任務重複，則會被阻擋生成。建議盡快清除保留任務。

## 晉升路徑與材質解鎖 (Progress & Materials Unlock)

### 解鎖連絡人 (Contacts)
- Chase Swindlehurst (CS1)：解鎖入門任務。
- Marvelous Mudenda (CS5)：解鎖中階任務。
- Denise David (CS48)：解鎖高階博弈類任務。
- Ethan McChad (CS50)：解鎖高階鐘塔類任務。

### 解鎖材質 (Materials)
- Oxygen (CS5)：基礎增氧。
- Saltpetre (CS10)：提高極限破壞速度。
- Diesel (CS15)：高擴散、低 Crit 風險啟動。
- Magnesium (CS20)：提升能見度，對抗消防隊衰減。
- Methane (CS25)：降低懷疑度 (Suspicion)。
- Molotov Cocktail (CS30)：特殊啟動模式。
- Kerosene (CS40)：穩定且強力的液體助燃。
- Thermite (CS50)：突破破壞上限，解鎖特殊功勳。
- Sand (CS60)：中階滅火材質。
- Hydrogen (CS70)：高擴散氣體。
- Flamethrower (CS80)：高強度與動量，高風險。

## 戰術路徑建議彙整 (Tactical Path Recommendations)

### 高效路徑 (Efficient Path)
- 每個區域放置 1 個液體助燃劑 (Gasoline/Diesel) + 1 個固體助燃劑。
- 除非有特定要求，不進行 Stoke 或 Dampen。
- 目標是儘早點火並觸發 Collect 領取 CS，因為 Collect 提供的 CS/N 倍率最高。

### 快速路徑 (Fast Path)
- 啟動火場後，利用 Stoke 與 Dampen 的邊際遞減效應。
### 組合與平衡 (Combination & Balance)
- 啟動助燃劑建議控制在 5 個以內，過多會增加 Ignition Crit 的機率。
- 專項 5% 屬性加成任務，建議在屬性達 200m 後使用。

### 最佳收益獲利策略 (Best Income Strategy)
- 目標類別：高等級博弈 (Gambling) 任務 或 鐘塔 (Clock Tower) 任務。
- 獲利來源：Thermite。雖然高階任務風險大，但在 CS100 下使用 Thermite 能極大化破壞獎金。

## 推薦從事公司 (Best Recommended Companies)

- **首選：遊樂園 (Amusement Park)**：10星福利提供全類別 10% 經驗與技能加成。由於官方目前未提供對位 Vandalism 的 15% 加成公司，遊樂園是目前的最優解。
- **備選：肉類倉庫 (Meat Warehouse)**：5星福利可減少 50% 失敗時的 CE 損失，適合在高強度 (Red Intensity) 下冒險操作的玩家。

## 功勳與勳章成就項 (Merit Medals & Achievements)

- Hotshot：CS 達 100。
- Arsonal：使用過每一種引燃器、助燃劑與滅火器。
- Cooking With Gas：在 30 秒內全毀一個 5 級大小的目標。需要 CS50 以上並使用大量 Thermite。

## 參考資料 (References)

https://www.torn.com/forums.php#/p=threads&f=61&t=16510947&b=0&a=0
