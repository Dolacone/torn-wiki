# Torn Crimes、Faction 與 Jail 參考

涵蓋 Crimes 2.0、各 Crime 路線、Faction、Organized Crime 與 Jail Busting。

## Faction 對新手的核心利益

- 軍械庫 (Armory)：免費借用武器、防具與藥品，節省開銷。
- 訓練加成 (Steadfast)：直接提升健身房獲得的屬性量。
- 藥物容忍 (Toleration)：減少毒癮累積速度，讓你省下戒毒費。
- 旅行載貨 (Excursion)：增加每次出國能帶回的物品數量。

## 公司系統總覽 (Company System Overview)

### 如何尋找合適的派系 (How to Find a Faction)
- 避免隨機邀請：不要接受路邊隨機發送的派系邀請。
- 論壇搜尋：前往論壇的 Factions Wanted 板塊搜尋符合需求的派系。
- 檢查 Profile：在加入前先查看派系頁面的 Perks 分布，優先選擇具備 Steadfast 與 Toleration 的派系。
- 主動聯絡：聯絡派系的招募官 (Recruiter) 或 Leader，展現活躍度與配合度。

### 聲望機制 (Respect)
- 聲望是派系的基礎貨幣，用於解鎖與維持加成 (Perks)。
- 獲取途徑：攻擊玩家、排位戰、連擊、組織犯罪。

### 關鍵加成分支 (Upgrades & Perks)
- Steadfast：提升四項戰鬥屬性的訓練效率 (最高 30%)，詳見 訓練策略指南 (Training Strategy)。
- Toleration：減少藥物負面影響 (最高 50%)。
- Excursion：增加旅行載貨量 (+10) 並縮短飛行時間，詳見 旅遊與跨國貿易指南 (Traveling & Trading Guide)。
- Aggression：提升武器傷害與精準度。

### 如何參與連擊 (How to Participate in Chaining)
- 計時器管理：每次攻擊後有 5 分鐘的連擊計時器，一旦歸零連擊即中斷。
- 不要空跑：在計時器剩餘 1 分鐘左右再發動下一波攻擊，避免體力 (Energy) 過度重疊消耗。
- 倍率獎勵：連擊數達到 10, 25, 50, 100... 等特定門檻時，聲望獲取量會翻倍。
- 禁忌：嚴禁在連擊期間攻擊派系內隊友正在攻擊的目標。

### 如何參與排位戰 (How to Participate in Ranked War)
- 聽從指揮：戰爭期間務必遵循 Discord 或遊戲內部的攻擊名單 (Target List)。
- 留體力：在戰爭開始前確保體力已補滿。
- 補給箱 (Caches)：戰爭獲勝後派系會獲得 Caches。新手通常可分得積分或物資獎勵。

### 組織犯罪 (Organized Crimes 2.0)
- 詳細機制見 organized crime 2。
- 職位分配：每個 OC 職位都有其對應的屬性門檻。
- 準備期：一旦被分配到 OC，在任務開始前應避免住院或坐牢。
- 自動化：確保隨時都處於 OC 隊伍中，這是獲取長期獎勵的最佳途徑。

## 組織犯罪指南 (Organized Crime 2.0)

本指南整理自官方論壇與玩家研究，介紹 crimes 2 系統下的組織犯罪 (OC) 機制。

### 核心術語表 (Glossary)

- CPR (Checkpoint Pass Rate)：關卡通過率。玩家在其選擇的角色中通過各個 Checkpoints 的機率。
- Tier：OC 的生成等級，範圍為 1 到 5。影響 Scope 成本與獎勵。
- Level：OC 的難度等級，範圍為 1 到 10。影響 CPR、金錢、物品與 Respect 獎勵。
- Role：OC 內的職位。不同職位有不同的 CPR 判定標準。

### 基礎機制概念 (Basics)

- Scenario (情境)：決定 OC 的角色構成與預期獎勵。
- 難度等級 (Difficulty Level)：等級越高，挑戰難度與獎勵越高。在進度階段開始前，玩家可以自由退出。
- 加入方式：玩家必須手動前往 Organized Crimes 頁面點擊 JOIN。第一個成員加入後，計時器即開始執行。

### 成員角色指標 (Role Metrics)

每個角色有兩個核心指標：

#### 策劃進度說明 (Planning Completion)
- 追蹤個別玩家的策劃時程。
- 每個參與者通常需要 24 小時。
- 採順序計時：第一個玩家完成後，第二個才開始，依此類推。
- 策劃期間玩家可以出國或被住院 (permahosped)，不影響進度。

#### 關卡成功率說明 (Checkpoint Pass Rate)
- CPR 數值越高，該關卡成功機率越高。
- 由角色需求與玩家能力決定，受以下因素影響：
- Battlestats：Strength 與 Defense 影響戰鬥類角色 (如 Muscle/Enforcer)；Dexterity 影響手藝類 (如 Thief/Picklock)；Speed 影響反射類 (如 Sniper/Robber)。Battlestats 增益在 1b 左右達到上限，詳見 戰鬥機制與計算公式 (Combat Formulas)。 - Workstats：Endurance (END) 影響體能類 (如 Muscle)；Intelligence (INT) 影響智謀類 (如 Negotiator)；Manual (MAN) 效果尚不明確。Workstats 上限理論值為 300k。 - Crime Skills (CS)：特定的犯罪技能對應特定角色 (如 電腦破解犯罪策略指南 (Cracking Strategy) 對應 Hacker)。CS 超過 100 後仍會持續提升 CPR。 - CE (Crime Experience)：作為 CPR 計算的加權乘數。 - 其他技能：Hunting (對應 Assassin)、Racing (對應 Driver/Hijacker)、Reviving (對應 Reviver)。
- 建議選擇 CPR 為綠色 (75+) 的角色。

### 執行材料要求 (Materials)

- 種類：分為 Tools (工具，標示綠勾，不消耗) 與 Consumables (消耗品，標示箭頭，成功後消耗)。
- 檢查：成員若未攜帶必要材料，OC 將無法進入執行階段 (Execution Stage)。
- 借用：可直接從 Faction armories 借用角色所需材料。道具借用無限制，消耗品會優先使用借用的庫存。
- 圖示：若成員缺少材料，其角色旁會顯示紅色的禁止符號。

### 計時器與執行限制 (Timer & Limitations)

計時器結束且滿足以下所有條件後，OC 才會正式執行：

#### 暫停與阻塞條件 (Pause & Block Conditions)
- OC 未滿員且所有成員已完成 Planning。
- 至少一名成員在住院 (Hospitalized)。
- 至少一名成員在監獄 (Jail)。
- 至少一名成員正在出國途中或在國外 (Flying/Abroad)。
- 至少一名成員缺少必要材料 (Materials)。

### 偵查資源機制 (Scope)

Scope 是生成 OC 所需的資源。

- 再生速度：每日被動回復 1 點。
- 獲得途徑：成功完成 OC 可獲得 (1 + OC Tier) 點。
- 儲存上限：100 點。
- 每日生成成本：成本等於該 OC 的 Tier。

### 生成等級說明 (Spawning & Tiers)

OC 分為 5 個 Tier，需透過 Faction upgrades 解鎖。

- 成功率平衡：高難度 OC 可能導致 Scope 虧損，需維持特定成功率以保持穩定：
- Tier 1：50% - Tier 2：66% - Tier 3：75% - Tier 4：80% - Tier 5：50%

### 連鎖任務機制 (Chain OCs)

- 出現等級：Level 5 以上。
- 機制：完成後不直接領取獎勵，而是生成高一級的 OC。
- 獎勵：僅在連鎖最末端成功後發放。
- 特性：Tier 5 的 OC 均為連鎖形式。獎勵通常高於同等級的單一 OC。

### 進階執行策略 (Advanced Mechanics)

#### 分階段執行技術 (Staging)
- 利用 Planning 順序計時的特性，組建不完整團隊來進行 Planning。
- 當其他 OC 完成且玩家空出時再填入剩餘位置，以最大化團隊產出。
- 9 人架構執行 6 人 OC 可提升 33% 的每人小時收益；12 人架構可提升 50%。

#### 關卡類型解析 (Checkpoints)
1. Mainline (主線)：收益最高路徑。失敗後可能進入 Recovery。
2. Recovery (恢復)：失敗後的緩衝，成功後可回歸主線，通常不減收益。
3. Lenient (寬容)：寬鬆的關卡，通常提供兩次恢復機會，常見於 OC 開頭。
4. Critical (關鍵)：失敗即進入低收益分支出。
5. Determinant (決定性)：失敗可能導致 OC 直接終止或大幅扣除獎勵。

### 派系管理策略建議 (Strategic Advice)

- 安排成員：將 CPR 較弱的成員放在 Lenient roles，將強者放在 Critical roles。
- 預先生成：OC 在過期前可存放 7 天，建議在 Scope 達到 100 前預先生成。
- 獎勵比較：對於大多數派系，OC 2.0 的收益通常優於 1.0 的 PA (Political Assassination)，除非派系內主要由高回報 PA 組成。

## 犯罪 2.0 系統核心機制總覽 (Crimes 2.0 Overview)

本文件整理了 Crimes 2.0 的通用機制與重要優勢，適合所有剛從 1.0 遷移的玩家。

### 系統遷移優勢分析 (Migration Advantages Analysis)

- CE (Crime Experience)：現行 2.0 的 CE 獲取效率極佳，尤其是達成縱火 (Arson 2.0, 屬於 Vandalism 類別) 的進階目標後。沒有理由為了 CE 留在 1.0。
- 功勳 (Merits)：2.0 提供了更多的功勳，且未來 1.0 的功勳在系統強制遷移後可能會遺失。
- OC 2.0 連動：參與 Crimes 2.0 能極大提升組織犯罪 (OC 2.0) 的成功率。在系統判斷中，通常直接以 NNB 作為衡量玩家 CE 是否足以勝任該項組織犯罪的標準。
- 經濟效益：雖然 2.0 目前的直接金錢收益較低，但長期而言，技能提升帶來的效益更高。

### 核心機制說明 (Core Mechanics)

- CS (Crime Skill)：每項犯罪獨立的等級，直接影響該犯罪的成功率與高階目標解鎖。
- CE (Crime Experience)：隱藏的綜合數值，決定 NNB 的上限。雖然 2.0 的單次獲取量未公開，但達成高神經值犯罪目標是提升 CE 的關鍵。
- NNB (Natural Nerve Bar)：扣除所有加成後的基礎神經上限，是觀測 CE 進度的唯一量化指標。
- 大失敗 (Critical Failure)：不僅會導致 Nerve 浪費，還會造成 CS 與 CE 下降，並伴隨扣血、入獄、住院或相關道具遺失。
- 獨有掉落 (Unique)：特定犯罪在達成 CS 門檻後有機率出現（空心星星圖標），每種掉落每位玩家限領一次。

### 外部增益與加成匯整 (External Buffs & Bonuses)

- 城市工作：Law 法律職業永久增加 5% Crime Experience 與 Skill Gain。
- 派系 Perk：最高可提供 10% 的犯罪進度加成。詳見 派系系統。
- 教育課程：心理學學士學位 (Psychology bachelor) 在 2.0 中非常強大。詳見 教育優先級。
- 增強器 (Enhancers)：
- 使用方式：放在物品庫 (Inventory) 即可生效，無需裝備。 - 核心價值：增加 CS/CE 獲取率、提升成功率、解鎖特殊項目或減少作業時間。 - 大失敗風險：若遭遇大失敗 (Crit)，增強器有機率毀損或消失。

### 建議進度策略 (Recommended Progression Strategy)

為了最大化 Nerve 效率與功勳進度，建議採取 1 Active + Multi Passive 的並行模式，並注意以下原則：

- 平衡發展：不要盲目追求高 CE 而忽視 CS。若 CS 過低，即便 CE 足夠，嘗試高難度目標時的大失敗機率依然極高。
- 主動衝刺 (Active)：將每日主要的 Nerve 消耗在單一高品質、高神經值消耗的犯罪上。
- 推薦：Burglary (直到 CS80+), Pickpocketing (CS100 收益最佳), 或正在解鎖功勳的項目。
- 被動累積 (Passive)：利用時間或冷卻機制，作為背景操作，不應讓其佔用過多主動 Nerve。
- Card Skimming：安裝後放著累積資料。 - Forgery：啟動生產後等待冷卻，非必要不頻繁檢查。 - Scamming：依賴受教育解鎖的被動郵件收集器，累積達 20,000 封後才集中消耗。 - Bootlegging：將 DVD 交給員工處理，定期檢查庫存即可。
- 戰術調度：手頭保留低難度犯罪 (如 Graffiti) 用於在高難度犯罪大失敗後快速清除負面狀態。
- 資訊查看：在遊戲介面點擊每種犯罪的圖片，可查看該項犯罪的詳細進度資訊。


### 功勳與勳章級距說明 (Merits & Medals Details)

每項犯罪通常包含：
- 1 個技能達 100 的功勳。
- 1 個特定行為功勳。
- 數個根據犯罪次數發放的勳章。

#### 勳章發放級距標準 (Medal Tier Standards)
100, 200, 300, 500, 750, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 6000, 7500, 10000

### 參考資料連結 (Reference Sources)

- [Crimes 2.0 Deep Dive by Baldr](https://www.torn.com/forums.php#/p=threads&f=61&t=16374814&b=0&a=0)

## 縱火犯罪策略指南 (Arson Crime Strategy)

縱火是一項高度戰術性的 Crimes 2.0 活動，屬於破壞 (Vandalism) 類別。涉及火場物理、材質組合與每日限量的任務管理。

### 術語與基礎定義 (Terminology & Basics)

- CS (Crime Skill)：在犯罪頁面頂部顯示的縱火技能等級。
- Unique：星號標記的唯一發現，每個角色僅能獲得一次。
- Crit (Critical Failure)：嚴重失敗，可能導致 CS 損失、物品遺失甚至住院/進監獄。
- Target：縱火目標，由地點與故事背景定義，影響易燃度與郊區度。
- Area：火場中的各個區域（火焰圖標表示）。
- Accelerant：用於助燃的助燃劑。
- Enhancer (增強器)：Windproof Lighter。取得途徑：Burglarize the Secluded Cabin (Unique)。可提升 5% 的 CE 與 CS 收益。

### 核心動作與神經值消耗 (Core Actions & Nerve)

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

### 火場物理力學機制 (Fire Physical Mechanics)

破壞進度 (Destruction Gauge) 取決於火場的兩個核心數值：

#### 強度 (Intensity)
- 代表火勢燃燒的猛烈程度。
- 強度越高，破壞速度越快。
- 當沒有動量 (Momentum) 時，強度會以 0.2/sec 的速度衰減。第一響應者到達後衰減增至 1/sec。
- 背景顏色：黃色最低，紅色最高。紅色強度時進行 Stoke/Dampen 極易發生 Crit。

#### 動量 (Momentum)
- 代表火場中尚未燃燒的燃料。
- 動量會被持續消耗轉化為強度。
- 液體助燃劑提供最強動量，氣體最弱。
- 在動量尚未衰減時進行操作會增加意外 (Accident) 風險。

#### 持續監控指標說明 (Monitoring Metrics Details)
- Suspicion (懷疑度)：影響「保險索賠 (Insurance Claim)」等任務的成功。Methane 可降低此值。
- Visibility (能見度)：影響消防隊被調度的時間。

### 環境影響參數分析 (Environment Parameter Analysis)

#### 易燃度 (Flammability)
等級 1-5。等級 5 目標完全燒毀僅需 50 秒，等級 1 則需 250 秒。

#### 郊區度 (Rurality)
影響反應時間 (Response Time)。等級 1 (都市) 給予 30 秒操作時間，等級 5 (荒郊) 給予增至 480 秒。

#### 火場區域 (Areas)
目標大小不同，區域數也不同 (1-5)。液體與氣體助燃劑具備擴散 (Spread) 屬性，可同時影響多個區域。

### 任務管理與保留機制 (Job Management & Preservation)

- 任務更新：每日 00:00 TCT 生成，所有玩家任務相同。
- 保留機制：與任務互動（如 Inquire）可防止其在換日後消失，但若新生成的任務與保留的任務重複，則會被阻擋生成。建議盡快清除保留任務。

### 晉升路徑與材質解鎖 (Progress & Materials Unlock)

#### 解鎖連絡人 (Contacts)
- Chase Swindlehurst (CS1)：解鎖入門任務。
- Marvelous Mudenda (CS5)：解鎖中階任務。
- Denise David (CS48)：解鎖高階博弈類任務。
- Ethan McChad (CS50)：解鎖高階鐘塔類任務。

#### 解鎖材質 (Materials)
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

### 戰術路徑建議彙整 (Tactical Path Recommendations)

#### 高效路徑 (Efficient Path)
- 每個區域放置 1 個液體助燃劑 (Gasoline/Diesel) + 1 個固體助燃劑。
- 除非有特定要求，不進行 Stoke 或 Dampen。
- 目標是儘早點火並觸發 Collect 領取 CS，因為 Collect 提供的 CS/N 倍率最高。

#### 快速路徑 (Fast Path)
- 啟動火場後，利用 Stoke 與 Dampen 的邊際遞減效應。
#### 組合與平衡 (Combination & Balance)
- 啟動助燃劑建議控制在 5 個以內，過多會增加 Ignition Crit 的機率。
- 專項 5% 屬性加成任務，建議在屬性達 200m 後使用。

#### 最佳收益獲利策略 (Best Income Strategy)
- 目標類別：高等級博弈 (Gambling) 任務 或 鐘塔 (Clock Tower) 任務。
- 獲利來源：Thermite。雖然高階任務風險大，但在 CS100 下使用 Thermite 能極大化破壞獎金。

### 推薦從事公司 (Best Recommended Companies)

- 首選：遊樂園 (Amusement Park)：10星福利提供全類別 10% 經驗與技能加成。由於官方目前未提供對位 Vandalism 的 15% 加成公司，遊樂園是目前的最優解。詳見 公司系統。
- 備選：肉類倉庫 (Meat Warehouse)：5星福利可減少 50% 失敗時的 CE 損失，適合在高強度 (Red Intensity) 下冒險操作的玩家。

### 功勳與勳章成就項 (Merit Medals & Achievements)

- Hotshot：CS 達 100。
- Arsonal：使用過每一種引燃器、助燃劑與滅火器。
- Cooking With Gas：在 30 秒內全毀一個 5 級大小的目標。需要 CS50 以上並使用大量 Thermite。

## 盜版燒錄犯罪指南 (Bootlegging Strategy)

Bootlegging 是一項結合手動燒錄與被動商店經營的犯罪，屬於仿冒 (Counterfeiting) 類別。本犯罪屬於 Crimes 2.0 系統的一部分。

- 完成所需 Nerve：7600 (約 19 天)
- 增強器 (Enhancer)：High-Speed Drive
- 其他關鍵道具：Laptop 或 Personal Computer, Blank DVDs


### 核心入門需求與道具 (Core Requirements & Items)

- 必備硬體：Laptop 或 Personal Computer。取得途徑：Super Store。
- 消耗品：Blank DVDs。取得途徑：Super Store。
- 增強器 (Enhancer)：High-Speed Drive。提升 5% 的 CS 獲得，並將燒錄速度翻倍。取得途徑：報廢場搜索 (Junkyard)、噴漆 (Graffiti)、商店偷竊 (Shoplifting) 或 公寓入室盜竊 (Burglary)。
- 推薦教育：CMT1520 (Introduction to Computing) 與 CMT2230 (Web Design and Development)。這是啟動線上商店 (Online Store) 的必要門檻。

### DVD 燒錄機制 (DVD Copying Mechanics)

- CS 影響力：CS 越高，每次嘗試燒錄的數量越多，且所需時間越短（每提升 CS 5 級，燒錄時間減少 2 秒）。
- 燒錄種類：所有分類提供的 CS 均相同，但為了後續銷售效益，建議依比例儲備庫存。
- 危險性：可能導致 Laptop/PC 毀損或丟失 High-Speed Drive。

### 實體販售機制 (Physical Selling Mechanics)

- 銷量最佳化：混合多種分類的 DVD 一起販售，能顯著提升單次銷售量、CS 獲得與金錢收益。
- 銷售比例建議 (Popularity Ratio)：
    - Action：10
    - Fantasy & Comedy：7
    - Drama：5.5
    - Thriller：4
    - Horror & Romance：3
    - Sci-Fi：2
- 戰術提示：Selling 提供的 CS 約為 Copying 的 4 倍（以每點 Nerve 計算），是刷技能的主要來源。

### 線上商店經營機制 (Online Store Management)

- 解鎖門檻：CS50 且完成上述教育課程。
- 建立流程：每次消耗 10N 增加 1%-9% 進度。成功率約 80%。
- 營運機制：自動販售庫存中的 DVD。
- 客戶群增長：若能維持所有分類庫存不中斷，客戶數量會呈指數增長。達到 10,000 客戶約需持續供貨 15.5 天。
- 自動化提示：網店開啟時會被動增加 CS（CS93 玩家回報 24 小時增長約 3%）。

### 戰術路徑建議彙整 (Tactical Path Recommendations)

#### 快速衝刺模式 (Fast Leveling)
- 忽視線上商店：網店會消耗掉你手動販售所需的庫存，且單位 Nerve 的 CS 收益較低。
- 操作流程：大量燒錄多樣化 DVD -> 手動大批量販售。

#### 功勳與成就模式 (Merits & Achievements)
- 啟動網店：一旦達到 CS50 且有教育背景，儘早開啟網店以累積客戶數。
- 達成標準：建議每種分類的 DVD 各燒錄 10,000 張，這能確保你在達成客戶數功勳的同時也完成所有分類銷售功勳。
- 時間預估：網店達到 10,000 客戶約需 2 週的持續營運。


#### 最佳收益策略分析 (Best Income Strategy)
- 核心：線上商店 (Online Store)。
- 策略：在 CS100 下，網店能支撐極大的客戶流量。確保 8 種分類庫存永不中斷，隨著客戶數突破 10k，被動收入將變得非常可觀，甚至超越手動販售。

### 推薦從事公司 (Best Recommended Companies)

- 首選：劇院 (Theater)：7星福利提供被動的 15% Counterfeiting 經驗與技能加成。這能加速燒錄階段的經驗累積，由於 Bootlegging 流程較短，7星劇院是衝刺 CS100 的首選。
- 早期過渡：遊樂園 (Amusement Park)：10星福利 (10% 加成) 適合尚未解鎖 7星劇院或正在同步進行多元犯罪的玩家。

### 唯一發現與功勳項目 (Unique Finds & Merits)

#### 唯一發現列表 (Unique Drops List)
- CS55：Special Ammunition。
- CS70：Lottery Voucher。
- CS85：Prayer Beads。
- CS100：Erotic DVD。

#### 功勳勳章成就項 (Merit Medals & Achievements)
- Box Office：CS 達 100。
- Online Entrepreneur：網店客戶達 10,000。
- Cinephile：所有分類均累計販售達 10,000 張。

## 入室盜竊犯罪策略指南 (Burglary Strategy)

Burglary 是一項涉及多階段操作、工具系統與「信心 (Confidence)」管理的深度犯罪，屬於盜竊 (Theft) 類別。本犯罪屬於 Crimes 2.0 系統的一部分。

- 完成所需 Nerve：17400 (約 44 天)
- 增強器 (Enhancer)：Flashlight
- 其他關鍵道具：Credit Card, Jemmy, Window Breaker, Lockpicks, Rope, Skeleton Key

### 工具系統與用途匯整 (Tool System & Usage)

這些工具為非消耗品，是解鎖 Unique 與高價值產出的門票：

- Flashlight (增強器)：提升 5% CS/CE，解鎖更多樣的產出。
- Jemmy (撬棍)：用於強力開啟特定的目標。
- Rope (繩索)：用於攀爬特定地形。
- Credit Cards (信用卡)：用於撬開簡易鎖頭。
- Lockpicks (鎖匠工具)：標準開鎖必備。
- Window Breaker (破窗器)：多數住宅入口必備。
- Skeleton Key (萬用鑰匙)：進入高級商業或工業場所必備。

### 犯罪三部曲執行流程 (The Three Phases Execution)

1. 偵查 (Scouting, 4N)：隨機產生一個特定類型的目標（住宅、商業或工業）。目標有效期 72 小時。
2. 勘查 (Casing)：觀察目標。每次操作會隨機增加 Confidence 信心條，並有機率出現 All Clear 狀態（下次必成）。
3. 偷竊 (Burgling)：執行最終犯罪。成功率受 Confidence 高低直接影響。

#### 信心值與成功率關聯 (Confidence & Success Rate Correlation)
- <30% Confidence：約 70% 成功率。
- 50% Confidence：甜蜜點 (Sweet Spot)。後續增加的邊際效益遞減，約 90% 成功率。
- 100% Confidence：最高約 98.5% 成功率。

### 地點與目標詳細分類 (Detailed Location & Target Categories)

#### 住宅目標 (Residential)
- 解鎖：初始至 CS100 (如 Manor House)。
- 特色：難度較低，適合衝刺 CS。產出以藥物 (Xanax)、雜物為主。
- 推薦路徑：CS 成長的首選地。

#### 商業目標 (Commercial)
- 特色：勘查難度增加，回報優於住宅。
- 產出：醫藥包、高級耗材、犯罪組件。

#### 工業目標 (Industrial)
- 特色：勘查極其困難，初期目標非常危險。
- 產出：最為豐厚。包含供應包 (Supply Packs)、稀有犯罪零件 (如 Brass Ingot)。

#### 成長與生存策略建議 (Growth & Survival Strategy)
- 住宅優先：在 CS 達到 80 之前，建議「只進行住宅類目標 (Residential)」。
- 絕對信心的必要性：強烈建議每次都勘查 (Case) 到 100% 信心。雖然這會消耗更多 Nerve，但在 Burglary 中，發生紅色嚴重失敗 (Critical Fail) 的代價極高（失去昂貴工具、住院、監禁且 CS 倒扣），這比多勘查幾次的成本更高。
- 功勳達成：當你達到 CS 100 後，系統會解鎖最後幾個特定目標。建議在你在其他犯罪（如 Cracking）中不幸遭遇嚴重失敗、正處於 Debuff 狀態時，用這些新解鎖的目標來達成勳章，因為此時你已經不在意 CS 收益了。


#### 最佳收益與利潤策略 (Best Income & Profit Strategy)
- 目標類別：工業目標 (Industrial)。
- 收益來源：Supply Packs (Drugs, Groceries等) 與 稀有零件。
- 策略：CS100 解鎖的 Advertising Agency 與 Manor House 也有極佳的產出，但穩定的工業區掃蕩（需高 Confidence）仍是最高金錢回報來源。

### 推薦從事公司 (Best Recommended Companies)

- 首選：家具店 (Furniture Store)：5星福利提供被動的 15% Theft 經驗與技能加成。這是目前門檻最低且最精確對位的盜竊類加成。
- 功能選擇：肉類倉庫 (Meat Warehouse)：5星福利可減少 50% 失敗時的 CE 損失，適合正在衝刺工業區 (Industrial) 高風險目標的玩家。

### 嚴重失敗風險評估 (Serious Failure Risk Assessment)

- 監禁與住院時間隨目標難度增加（最高級別可能導致長時間監禁）。
- 永久損失當前使用的 Key Item（Flashlight 除外）。
- 自我治療：Thug 或 Cyclist 是長效住院（自保）的選項。

### 功勳勳章成就項 (Merit Medals & Achievements)
- Breaking and Entering：CS 達 100。
- Key to the City：成功偷竊全數 34 種不同的目標。注意：Manor House 與 Advertising Agency 等目標需 CS100 才能偵查到。

## 信用卡側錄犯罪策略指南 (Card Skimming Strategy)

Card Skimming 是一項結合被動數據收集與主動回收的犯罪，屬於詐騙 (Fraud) 類別。本犯罪屬於 Crimes 2.0 系統的一部分。

- 完成所需 Nerve：2500 (若以最高 Nerve 效率進行，需耗時數月)
- 增強器 (Enhancer)：Duct Tape
- 其他關鍵道具：Spy Camera, Card Skimmer, Laptop 或 Personal Computer


### 基礎需求與道具清單 (Requirements & Items List)

- 核心階段：安裝 (Install)、回收 (Recover)、販售 (Sell)。
- 消耗性道具 (成功回收後返還)：
    - Card Skimmers：安裝時放置，$175 墨西哥、報廢場、或地鐵唯一發現取得。
    - Spy Cameras：安裝時放置，$130 Super Store、報廢場、或店舖偷竊取得。
- 必備硬體：Computer 或 Laptop (販售階段使用)。
- 增強器 (Enhancer)：Duct Tape。
    - 效果：提升 5% CS/CE 獲得。
    - 取得途徑：商店偷竊 Bits 'N' Bobs 唯一發現。

### 核心機制與地點效率評估 (Core Mechanics & Location Efficiency)

側錄器全地圖上限為 20 個。資料收集量 (Details) 會隨時間增加，但側錄器留在現場越久，或玩家離線越久，被發現毀損的風險越高。

| 地點 | 解鎖門檻 | 資料產出速度 (Details/hr) | 安全評估 |
| --- | --- | --- | --- |
| Gas Station | CS25 | 0.4 (最低) | 最安全 (Safest) |
| Bus Station | 初始 | 0.6 | 非常安全 |
| Post Office | 初始 | 0.75 | 安全 |
| Subway Station | 初始 | 0.9 | 低風險 (Minor) |
| College Campus | 初始 | 1.1 | 中等風險 |
| Airport Terminal | CS50 | 1.3 | 高風險 |
| Bank Branch | CS100 | 1.7 | 高風險 |
| Casino Lobby | CS75 | 2.15 (最高) | 極高風險 (Very High) |

### 側錄實戰戰術彙整 (Skimming Tactics Compilation)

#### 快速衝刺模式 (Fast Leveling)
- 操作：安裝 (Install) 後立即回收 (Recover)，無視資料量。
- 優點：CS 提升最快。
- 缺點：耗費極多 Nerve 與精力手動循環。

#### 最大神經值效率 (Nerve Efficiency)
- 地點選擇：
- 一般離線 < 7 小時：選擇 Bus Station。 - 經常離線 > 8 小時：選擇 Gas Station。
- 操作策略：一次裝滿全地圖上限的 20 個側錄器，然後放著「完全不管」。
- 回收時機：定期檢查狀態，直到發現「有 2 個側錄器被守護者移除/失效」時，才一次性手動回收所有剩餘的側錄器並由商店補貨重裝。
- 優點：這是獲取 CS 最神經值效率的方式，且能輕鬆達成單次回收 250 份資料的功勳。


#### 最佳收益獲利策略 (Best Income Strategy)
- 目標地點：Casino Lobby (需 CS75) 或 Bank Branch (需 CS100)。
- 策略：在這些最高回報地點安裝，並配合長時間離線（或出國）累積資料。一次性回收超過 10,000 份 Details 後販售，能獲得最高的單價加成。

### 數據販售與獲利機制 (Selling & Profits Mechanism)

- 販售價值：單次販售的卡片資料量越多，平均單價越高。
    - 100 份以下：$100 - $160 / 份
    - 1,001 - 9,999 份：$160 - $220 / 份
    - 10,000 份以上：$190 - $250 / 份
- 注意：販售階段獲得的 CS 非常微薄，獲利是主要目的。

### 嚴重失敗風險分析 (Serious Failure Risk Analysis)

- 損失 Card Skimmer 與 Spy Camera。
- 失去該側錄器已累積的所有卡片資料 (Details)。
- 監禁時間：約 1-3 小時。

### 功勳勳章成就項 (Merit Medals & Achievements)

- King PIN：CS 達 100。
- Zero Liability：單次回收動作中取得超過 250 份卡片資料。
    - 達成技巧：在 College Campus 或類似地點安裝 20 個側錄器，出國或離線兩週後回來回收（需承擔被發現損壞的風險）。

## 電腦破解犯罪策略指南 (Cracking Strategy)

Cracking 是一項結合手動解謎與硬體配置優化的犯罪，屬於網路犯罪 (Cybercrime) 類別。本犯罪屬於 Crimes 2.0 系統的一部分。

- 完成所需 Nerve：20000 (約 50 天)
- 增強器 (Enhancer)：Office Chair
- 其他關鍵道具：無


### 基礎需求與環境配置 (Requirements & Environment)

- 必備硬體：Computer 或 Laptop。
- 必備教育：完成 Computer Science 相關基礎課程 (CMT1520 等)。
- 增強器 (Enhancer)：Office Chair。
    - 效果：提升 5% CS/CE。由 店舖偷竊 Cyber Force 唯一發現取得。

### 核心解密機制 (Core Decryption Mechanics)

1. 暴力破解 (Brute-forcing, 7N)：
    - 消耗 Nerve 直接揭露字元或加密層 (Encryption Layers)。
    - CS 效益：每次動作獲得的經驗約為最後一步破解收益的一半。
2. 手動猜測 (Guessing, 0N)：
    - 手動輸入可能字元。猜對字元可節省大量 Nerve。
    - 限制：每個任務有 3 次錯誤額度，超過後僅能使用暴力破解，但不影響最終獎勵。
3. 加密層 (Encryption)：
    - 部分目標具備 1-9 層加密。每層加密需等同於一個字元的暴力破解循環才能移除。

### 破解機架構系統 (The Rig System Architecture)

- 解鎖門檻：CS25 (第一個機殼), CS50 (第二個), CS75 (第三個)。
- 組件類別：
    - CPUs (提供 MIPS)：分為 eCPU (低溫低耗)、CPU、HPCPU (高效能、極高溫熱 radiated、超頻強)。
    - PSUs (提供電力)：驅動 CPU 與 Fans。
    - Cooling (散熱)：
        - Fans：大範圍降溫，需消耗電力。
        - Water Blocks：短距離降溫、高效。
        - Heat Sinks：向相鄰四格提供百分比減熱，不耗電，但自身不減熱。

#### 破解強度與 MIPS 關聯 (BFS & MIPS Correlation)
BFS 決定每次暴力破解揭露的字元/層數。
- 100k MIPS = 1 BFS (啟動門檻)
- 425k MIPS = 3 BFS
- 1.3M MIPS = 5 BFS
- 2M MIPS = 6 BFS

#### 熱能管理與冷卻 (Heat Management & Cooling)
- 溫度 > 50：組件鎖定 (無法拔除/更換)。
- 溫度 > 100：Overheated 停機，冷卻速度極慢 (1% per minute)。
- 教育加成：完成「CMT2570」課程後，組件熱能產出減少 25%。

### 戰術路徑建議彙整 (Tactical Path Recommendations)

#### 經濟效率模式 (Economic Efficiency)
- 策略：暴力破解一次取得部分字元，搭配外部字典工具手動猜測剩餘密碼。
- 優點：極致節省 Nerve，快速達成「Character Assassination」功勳 (手動猜對 250 字元)。

#### 進階升級與效率策略 (Advanced Upgrade Strategy)
- 任务受限性：每日可用的破解任務數量有限。
- 追求極速升級 (Fast Skill Gain)：
- 專注於 Brute force (提供基礎 CS) 與 Crack (提供更優 CS)。 - 減少猜測行為：如果你的神經值充足且任務有限，過多猜測會消耗掉任務份額卻不提供 CS，導致神經值溢出卻無事可做。
- 追求最大 Nerve 效率 (Least Nerve)：
- 充分利用手動猜測 (Guessing)，雖然不給 CS，但能極大地節省神經值以用於其他犯罪。 - 配合高效能的 Rigs 來加速處理。


#### 最佳收益策略分析 (Best Income Strategy)
- 目標類別：高等級加密與長密碼資料庫。
- 策略：在 CS100 且擁有 3 個 Rig 的情況下，可以同時掛載數個高難度暴力破解任務。配合字典檔手動猜測，單位 Nerve 的金錢收益極高。

### 推薦從事公司 (Best Recommended Companies)

- 首選：軟體公司 (Software Corporation)：7星福利提供被動的 15% Cybercrime 經驗與技能加成。這是目前唯一專門針對 Cracking 的進度加成路徑。
- 功能選擇：遊樂園 (Amusement Park)：10星福利 (10% 加成) 適合需要平衡多項犯罪類別的玩家。

### 功勳勳章成就項 (Merit Medals & Achievements)

- Cryptographer：CS 達 100。
- Character Assassination：手動猜對 250 個密碼字元。

## 棄置犯罪策略指南 (Disposal Strategy)

Disposal 是一項每日限額的犯罪，屬於非法服務 (Illicit Services) 類別。特色在於多樣化的道具消耗與每日刷新的任務系統。本犯罪屬於 Crimes 2.0 系統的一部分。

- 完成所需 Nerve：5100 (約 35 天，因每日任務數量受限)
- 增強器 (Enhancer)：Latex Gloves
- 其他關鍵道具：Wheelbarrow, Shovel, Brick, Gas Can, Hydrochloric Acid, Disposable Mask

### 道具系統與消耗品清單 (Tools & Consumables List)

#### 增強器 (Enhancer)
- Latex Gloves：提升 5% CS/CE。由 店舖偷竊珠寶店或 入室盜竊牙醫診所唯一發現取得。

#### 核心可重複工具 (Core Reusable Tools)
- Shovel：用於 Bury 方法。
- Wheelbarrow：用於處理建築廢料 (Building Debris) 與工業廢物 (Industrial Waste)。
- Handkerchief：用於 Abandon 火器。
- Double Cut File：處理火器必備。

#### 消耗品 (Consumables)
- 處理特定任務時每次操作均會消耗，如 Gas Cans (Burn 用)、HCL (Dissolve 用)、Lye (屍體 Bury 用)、Bleach 與 Paper Towels (車輛/兇器用)。
- 注意：屍體 (Dead Body) 任務會消耗 5 倍量的消耗品。

### 每日任務機制說明 (Daily Job Mechanics)

- 每日 00:00 TCT 重置，所有玩家顯示相同的任務池。
- 任務數量與難度隨 CS 等級解鎖（最高 CS100 約每日 16 個任務）。
- 經驗乘數 (Complexity Multiplier)：
    - General Waste: 100%
    - Vehicle: 130%
    - Industrial Waste: 160%
    - Firearm: 220%
    - Body Part: 350%
    - Dead Body: 550%

### 處置方法與效益評估 (Methods & Efficiency Evaluation)

| 方法 | Nerve 成本 | CS 收益乘數 | 備註 |
| --- | --- | --- | --- |
| Abandon | 6N | 100% | 最低成本，通常成功率較低 |
| Bury | 8N | 120% | 需 Shovel |
| Burn | 10N | 144% | 燃燒文件或家具極為安全 |
| Sink | 12N | 173% | 處理重物（廢料、車輛）極佳 |
| Dissolve | 14N | 207% | 高級方法，通常僅適用於屍體 |

### 戰術路徑建議彙整 (Tactical Path Recommendations)

#### 成長與連鎖策略 (Growth & Chain Strategy)
- 高 Nerve 優勢：消耗神經值越高的處置選項，其提供的 CS 經驗呈現指數級成長。在安全前提下，務必選擇最高配置。
- 連鎖維持：由於每日任務有限，強烈建議在累積了 40+ 的犯罪連鎖 (Crime Chain) 後再進行處置，以最大化加成效果。
- 任務篩選：若神經值負擔較重，可優先處理 Firearm (火器)、Murder weapon (兇器)、Body part (肢體) 與 Body (屍體)，這類任務的技能報酬最為厚實。
- 組合建議：適合與 Hustling 等能輕易刷出高連鎖的犯罪交替進行。


#### 最佳收益獲利策略 (Best Income Strategy)
- 目標類別：Dead Body 與 Body Part。
- 策略：CS100 解鎖的任務數量最多，且包含最高價值的屍體處置任務。在資源充足下，使用 Dissolve (需 HCL) 處理這些任務是每點 Nerve 獲利與經驗最高的組合。

### 推薦從事公司 (Best Recommended Companies)

- 首選：夜總會 (Nightclub)：3星福利即可提供被動的 15% Illicit Services 經驗與技能加成。這是目前成本最低、效能最直接的對位選擇。
- 高階選擇：律師事務所 (Law Firm)：3星福利提供 25% 犯罪成功率加成，雖不增加 CS 獲得速度，但對於需要極高隱密性或降低失敗率的任務仍有其傳統價值。

### 功勳勳章成就項 (Merit Medals & Achievements)

- Trash Bandit：CS 達 100。
- Dissolving Agent：使用強酸 (Acid) 溶解屍體 (Dead Body)。

## 文書偽造犯罪策略指南 (Forgery Strategy)

Forgery 是一項長流程的專案型犯罪，屬於仿冒 (Counterfeiting) 類別。其特色在於極其龐雜的物資管理與多步驟的冷卻機制。本犯罪屬於 Crimes 2.0 系統的一部分。

- 完成所需 Nerve：24000 (約 60 天)
- 增強器 (Enhancer)：Magnifying Glass
- 其他關鍵道具：Printer + 依專案而異的大量材料


### 基礎需求與環境配置 (Requirements & Environment)

- 增強器 (Enhancer)：Magnifying Glass。
    - 效果：提升 5% CS/CE。由 店舖偷竊珠寶店唯一發現取得。
- 核心道具與鎖定機制：
    - Printer 與 Sand 是偽造的核心工具。在進行「Printing」或「Casting」等步驟時，該道具會被「鎖定 (Locked)」，無法同時用於其他專案。若要並行作業，需擁有多個備用道具。

### 專案標準工作流程 (Project Standard Workflow)

- 步驟與 Nerve：每個步驟消耗 5N。專案長度從 4 步到 12 步不等。
- 冷卻時間 (Cooldown)：部分步驟（如印製、油漆乾燥）需等待數小時，期間專案進度無法推進。
- 失敗與倒退：
    - 一般失敗：損失該步驟的耗材。
    - 嚴重失敗 (Crit)：專案進度可能倒退數步，甚至整件報廢 (Total Loss)，有時會損失工具 (如 Printer / Perforator)。無捕入獄風險。

### 技能收益分配原則 (Skill Gain Allocation)

- 過程步驟 (Process Steps)：均提供相同的基礎 CS 收益。
- 最終完成步驟 (Final Step)：根據專案難度具備加成乘數：
    - Driver's License: 200%
    - Birth Certificate: 300%
    - Travel Visa / ID Badge / Bank Check: 350%
    - License Plate: 400%
    - Police Badge: 450%
    - Passport: 750%

### 偽造專案詳細目錄 (Detailed Project Catalog)

| 專案 | 解鎖門檻 | 步驟數 | 安全性 | 備註 |
| --- | --- | --- | --- | --- |
| Driver's License | CS0 | 4 | SAFE | 最穩定的入門選擇，耗材極省 |
| Parking Permit | CS0 | 4 | SAFE | 經驗略優於駕照 |
| License Plate | CS25 | 6 | RISKY | 潛在的高階材料，早期極易 Crit |
| Birth Certificate | CS25 | 5 | UNSAFE | 獲利與經驗平衡點佳 |
| Skeleton Key | CS50 | 4 | RISKY | 需消耗 Sand 與 Brass Ingot，獲利極佳 |
| Prescription | CS50 | 4 | SAFE | 幾乎不 Crit，能將 Medical Bill 變現 |
| Travel Visa | CS50 | 5 | UNSAFE | CS 獲益/Nerve 效率最高的選擇 |
| Bank Check | CS75 | 6 | UNSAFE | 步驟 4 極度危險 |
| Passport | CS75 | 12 | UNSAFE | 最長專案，獲利約 $9k/N，經驗爆發高 |

### 戰術與功勳建議彙整 (Tactics & Merits Recommendations)

#### 穩健成長策略 (Stable Growth)
- CS 成長秘訣：在達到 CS 50 甚至 CS 100 之前，一直持續進行 Driver's license 專案被認為是最穩妥且 Nerve 效率極高的路徑。
- 轉向選擇：若感到厭倦且想微調收益，可以觀察專案面板底部的數值選擇報酬較高的任務。


#### 最佳收益獲利策略 (Best Income Strategy)
- 目標專案：Passport (需 CS75) 或 Skeleton Key (需 CS50)。
- 收益：Passport 每點 Nerve 收益高達 $9k；Skeleton Key 雖然難度高，但在市場上極其搶手。
- 策略：在 CS100 下，即便風險等級為 Unsafe 的專案也能穩定完成。

#### 流水線功勳 (Assembly Line Merit)
- 達成方式：同時讓 10 個相同專案處於冷卻狀態。
- 推薦路徑：解鎖 License Plate (CS25) 後，同時開啟 10 個專案並推進至步驟 2「Background Painting」(1小時冷卻)。

### 推薦從事公司 (Best Recommended Companies)

- 首選：劇院 (Theater)：7星福利提供被動的 15% Counterfeiting 經驗與技能加成。對於 Passport 這種超長流程專案，15% 的經驗增益能顯著縮短達成功勳的時間。
- 功能選擇：遊樂園 (Amusement Park)：10星福利 (10% 加成) 適合追求全方位加成、或經常切換至 Bootlegging 刷新材料的玩家。

## 塗鴉犯罪策略指南 (Graffiti Strategy)

Graffiti 是一項涉及區域聲望 (Reputation) 經營的犯罪，屬於破壞 (Vandalism) 類別。本犯罪屬於 Crimes 2.0 系統的一部分。

- 完成所需 Nerve：8300 (約 21 天)
- 增強器 (Enhancer)：Paint Mask
- 其他關鍵道具：Ladder, Wire Cutters


### 基礎需求與消耗品清單 (Requirements & Consumables List)

- 核心消耗：每次嘗試消耗 3N。
- 必備物資：Spray Cans (噴漆罐)。可從 Bits 'n' Bobs、Print Store 或物品市場取得。
- 關鍵道具與增強器：
    - Ladder (梯子)：取得途徑：West Side (CS15)。可防止高處作業相關的失敗結果。
    - Wirecutters (鐵絲網剪)：取得途徑：North Side (CS25)。用於進入特定封閉區域。
    - Paint Mask (防毒面具/增強器)：取得途徑：East Side (CS35)。提升 5% 的 CS/CE 獲得機率，並解鎖高額回報。建議儘早取得。

### 區域分布與聲望等級詳解 (Region & Reputation Details)

#### 區域一覽 (Region Overview)
- East Side / West Side / North Side：初始解鎖。
- Residential District：由 East Side 發展，CS50 解鎖。
- Red-Light District：由 West Side 發展，CS50 解鎖。
- Financial District / City Center：需加入幫派 (Crew) 才能解鎖。

#### 聲望級距機制 (Reputation Tiers Mechanism)，決定了 Unique 的出現機率與現金回報：
- R1 (25 塗鴉)：區域第一個 Unique。
- R2 (50 塗鴉)：區域第二個 Unique。
- R3 (100 塗鴉)：增加現金產出。
- R4 (250 塗鴉)：顯著增加現金產出。
- R5 (500 塗鴉)：可觸發加入 Crew 的 Unique。

#### 聲望衰減 (Reputation Decay)
執法部門會定期清理塗鴉。塗鴉累積越多、區域在列表越下方，衰減速度越快。每日損失約數個至數十個。

### 加入幫派流程與條件 (Joining a Crew Process)

- 加入門檻：在任一初始 5 個區域達到 R5 且 CS 達 70。
- 流程：達成條件後，該區域會出現一個特定的 Unique，取得該 Unique 即可加入 Crew。
- 收益：解鎖 Financial District 與 City Center，並獲得 Fresh Blud 勳章。

### 實戰戰術與成功率分析 (Tactics & Success Rate Analysis)

#### 配色建議 (Color Recommendations)
根據數據分析，特定顏色在不同區域有特定優勢（僅供參考）：
- East Side：Purple 適合刷錢，Red 適合刷聲望。
- West Side：Green 適合刷錢，Blue 適合刷聲望。
- North Side：Green 適合刷錢，Orange 適合刷聲望。
- Red-Light：Green 適合刷錢，Pink 適合刷聲望。
- City Center：Green 適合刷錢，Blue 適合刷聲望。

#### 成功率與潛在風險 (Success Rate & Potential Risks)
- East/West Side 較安全，失敗率低。
- North Side 與 Red-Light District 風險較高。
- 大約 10% 的失敗會轉化為 Crit (Critical Failure)，可能導致入獄、損失噴漆罐或設備（Wirecutters/Paint Mask）。

### 戰術路徑建議彙整 (Tactical Path Recommendations)

#### 幫派與功勳路徑 (Crew & Merits Path)
- 早期策略：專注於轟炸 (Spam) 前三個初始區域 (East, West, North)，直到聲望達到 500 (R5)。
- 目標：這會觸發加入幫派的事件，並達成相關功勳。
- 注意：由於多數玩家在 1.0 並未累積過 Vandalism 類別的勳章，這項犯罪是獲取該類別大量勳章的最佳途徑。

#### 犯罪功能性應用策略 (Functional Application Strategy)
- 清除 Debuff：當你在其他高難度犯罪 (如 Cracking 或 Burglary) 遭遇紅色嚴重失敗後，可以使用 Graffiti (消耗低且成功率高) 來快速累積 20 次成功，以消除嚴重的失敗 Debuff。
- 聲望維持：在 CS100 後，可以專注於維持高階區域 (Financial/City Center) 的 500 聲望以獲取穩定收益。

### 推薦從事公司 (Best Recommended Companies)

- 首選：遊樂園 (Amusement Park)：10星福利提供全類別 10% 經驗與技能加成。這是目前 Vandalism 類別（Arson / Graffiti）唯一的進度加成路徑。
- 功能選擇：肉類倉庫 (Meat Warehouse)：5星福利可減少 50% 失敗時的 CE 損失，適合正在衝刺加入幫派 (Join a Crew) 關鍵階段、且希望降低風險的玩家。


### 功勳勳章成就項 (Merit Medals & Achievements)

- Let Us Spray：CS 達 100。
- Fresh Blud：加入 Crew。
- Vandalism Medals：由於此犯罪是 Vandalism 分類目前唯一選項，是刷該類別勳章的最佳途徑。

## 街頭推銷犯罪策略指南 (Hustling Strategy)

Hustling 是一項高度依賴群眾心理與技術積累的犯罪，屬於詐騙 (Fraud) 類別。核心在於操控群眾的注意力與懷疑度，並透過特定的遊戲技術 (Technique) 獲取利潤。本犯罪屬於 Crimes 2.0 系統的一部分。

- 完成所需 Nerve：5900 (約 15 天)
- 增強器 (Enhancer)：Megaphone
- 其他關鍵道具：無


### 基礎需求與道具列表 (Requirements & Items List)

- 增強器 (Enhancer)：Megaphone。
    - 效果：提升 5% CS/CE，增加吸引群眾的效率。
    - 取得途徑：扒竊 (Pickpocketing) Laborer 唯一發現。

### 核心心理博弈機制 (Core Psychological Mechanics)

- 聚集群眾 (Gather Audience, 4N)：全等級上限 10 人。
- 注意力 (Attention)：透過遊戲演示 (Demo) 或炒作 (Hype) 提升。高注意力會增加投注機率與金額。若注意力歸零，群眾將離開。
- 懷疑度 (Suspicion)：透過贏家獲利 (Player Win) 提升。懷疑度越高，群眾的「最大注意力」上限就越低。
- 群眾特性：
    - 愛心圖示 (Favorite Game)：該名群眾對特定遊戲有狂熱，注意力提升快且持續投注，不受懷疑度影響。
    - 色調 (Wealth)：頭像色調由灰轉綠表示財富等級。越綠的群眾投注金額越高。

### 推銷遊戲與技術等級 (Games & Technique Levels)

共有四種遊戲，每種遊戲有獨立的技術等級，影響投注上限：

1. Cornhole (7 級)
2. Snail Racing (9 級)
3. Find the Lady (11 級)
4. Shell Game (12 級)

- 累積方式：透過贏 (Win) 或輸 (Lose) 累積（贏球累積較快）。Demo 與 Hype 不會增加技術經驗。

### 現場助手暗樁系統 (Shill & Plant System)

- 暗樁 (Shill, CS60 解鎖, 4N)：回收部分因「故意輸掉 (Intentional Loss)」而損失的賭金。
- 扒手 (Pickpocket, CS80 解鎖, 4N)：在玩遊戲或宣傳時隨機從群眾身上偷錢。
- 回收 (Collect, 2N)：取回助手累積的金額。

### 戰術與功勳達成建議 (Tactics & Merits Recommendations)

#### 快速衝刺模式 (Fast Leveling)
- 效益對應：Win (225%) > Lose (150%) > Demo/Hype (100%)。
- 策略：盡可能維持同一批群眾，利用 Demo/Hype 保持注意力，並以贏球作為主要 CS 來源。

#### 技術升級流程 (Technique Leveling)
- 準備工作：確保手頭有至少 40+ Nerve 以進行完整循環。
- 操作步驟：
1. 聚集群眾 (Gather Audience) 1-3 次。 2. 進行遊戲演示 (Demo)，由上而下逐一嘗試，直到群眾中出現「愛心圖示 (Favorite Game)」。 3. 故意輸球 (Lose) 2-3 次，直到該「愛心目標」的注意力達到最高。 4. 採取「一贏一輸、一贏一輸」的循環模式，直到該目標離開。 5. 如果仍有 40+ Nerve，回到步驟 1。
- 注意：如果沒有出現愛心目標，則直接在你能處理的最難遊戲上進行輸球循環。


#### 高額獲利實戰戰術 (High Profit Tactics)
- 達成條件：
    - 累積全數 10 名群眾。
    - 刷洗群眾直到出現複數「鮮綠色標記 (Wealthy)」或「愛心標記」的群眾。
    - 將技術 (Technique) 提升至高等級 (推薦 Shell Game)。
    - 將群眾注意力刷滿後，重複切換遊戲直到出現 $100k 以上的投注金額。

#### 最佳收益與技術路徑 (Best Income & Technique Path)
- 核心：Shell Game (技術等級 12)。
- 策略：雇用 扒手 (Pickpocket) 並讓其在人群中自選目標。在 CS100 下，針對富有 (Wealthy) 群眾進行高額賭局，配合助手的高額回收，每點 Nerve 的平均回報極高。

## 扒竊犯罪策略指南 (Pickpocketing Strategy)

Pickpocketing 是一項強調即時判斷與目標篩選的犯罪，屬於盜竊 (Theft) 類別。本犯罪屬於 Crimes 2.0 系統的一部分。

- 完成所需 Nerve：9400 (約 24 天)
- 增強器 (Enhancer)：Cut-Throat Razor
- 其他關鍵道具：無


### 基礎需求與技能增強器 (Requirements & Enhancers)

- 核心消耗：消耗 Nerve 進行單次扒竊。
- 增強器 (Enhancer)：Cut-Throat Razor。
    - 效果：提升 5% CS/CE，解鎖特定 Unique 與高價值產出（部分 Unique 必須持有此道具才能取得）。
    - 取得途徑：商店偷竊 Bits 'n' Bobs、入室盜竊 Barbershop 或扒竊 Thug。

### 核心機制與目標篩選原則 (Core Mechanics & Targeting)

- 動態目標：目標池每隔幾秒刷新，全球玩家共享。
- 三大判斷維度：身份 (Mark) > 狀態 (Status) > 體格 (Build)。
- 狀態黃金律：目標越分心越好。優先選擇「正在用手機 (On Phone)」、「聽音樂 (Listening to music)」或「酒醉 (Distracted/Stumbling)」的目標。

### 目標難度分級與分類 (Mark Tiers & Categories)

#### 安全級 (Safe)
- 目標：Drunk (Man/Woman), Homeless, Junkie, Elderly (Man/Woman)。
- 建議：CS 非常低時的首選，幾乎不會失敗。

#### 中等風險級目標 (Moderately Unsafe Marks)
- 目標：Young (Man/Woman), Student, Laborer, Postal Worker, Classy Lady。
- 建議：Young 人群出現頻率極高且經常分心，是中期穩定的 CS 來源。

#### 高風險級目標 (Unsafe Marks)
- 目標：Rich Kid, Sex Worker, Thug | Jogger, Businessman, Businesswoman, Gang Member, Mobster。
- 建議：報酬較高，但必須在對方處於「On Phone」或極度分心時出手。

#### 危險級目標 (Dangerous Marks)
- 目標：Cyclist。
- 建議：建議 CS80+ 再嘗試。有機率產出 Xanax。

#### 極度危險級目標 (Very Dangerous Marks)
- 目標：Police Officer。
- 建議：極高失敗率。建議僅在 CS 趨於滿級或為了衝刺勳章時嘗試。

#### 特殊功勳：警察徽章 (Police Badge Merit)
- 挑戰時機：由於扒竊 Police Officer 的失敗率極高，且失敗會倒扣 CS。建議在以下兩個時點嘗試：
- CS 0 時：此時沒有技能點數可以損失。 - CS 100 後：此時技能已達上限，損失點數不再影響功勳達成。
- 工具辅助：建議搭配 Userscript 來篩選目前的最佳（最分心）目標，以降低失敗率。


#### 最佳收益獲利策略 (Best Income Strategy)
- 目標：Cyclist, Businessman, Businesswoman。
- 收益：Xanax (Cyclist) 與大量現金 (Business 人群)。
- 策略：在 CS100 下，即便這些目標沒分心也能穩定出手，但為了 100% 成功，仍建議優先選擇正在使用手機的 Businesswoman。

### 嚴重失敗與技能損失風險 (Critical Failures & Skill Loss)

- 失敗懲罰：可能導致住院、監禁。
- 關鍵機制：失敗時損失的 CS 與目標難度成正比。扒竊警察失敗導致的 CS 倒扣遠大於扒竊醉漢。
- 建議：在 CS 較低時，絕對不要挑戰高難度目標，以免 CS 倒退。

### 功勳勳章成就項 (Merit Medals & Achievements)

- Pocketeer：CS 達 100。
- Pig Rustler：成功扒竊正在奔跑的 Police Officer，並取得警察徽章 (Police Badge)。這是本項犯罪最具挑戰性的特殊勳章。

## 詐騙犯罪策略指南 (Scamming Strategy)

Scamming 是一項結合長期名單經營與即時說服博弈的犯罪，屬於詐騙 (Fraud) 類別。其特色在於三階段的作業流程與複雜的心理博弈。本犯罪屬於 Crimes 2.0 系統的一部分。

- 完成所需 Nerve：28000 (約 70 天)
- 增強器 (Enhancer)：Ergonomic Keyboard
- 其他關鍵道具：眾多與特定詐騙相關的物品


### 基礎需求與教育門檻 (Requirements & Education)

- 增強器 (Enhancer)：Ergonomic Keyboard。
    - 效果：提升 5% CS/CE。由 店舖偷竊 Super Store 唯一發現取得。
- 必備教育課程：
    - Psychology (Interpersonal Dynamics)：解鎖說服條回應的內容預測範圍（以括號標註 landing 範圍）。
    - Computer Science：解鎖自動電郵收集工具 Phisher 與 Scraper。

### 犯罪三階段作業流程 (Three-Phase Workflow)

1. 電郵收集 (Email Farming, 8N)：
    - 初期建議手動累積 10k-20k 名單以啟動基礎詐騙。
    - 解鎖教育後，每次手動 Farming 動作有機會佈局 Phisher (慢速) 或 Scraper (快速) 進行被動收集。
2. 任務刷新 (Spam Waves)：
    - 將名單發送至不同類別的垃圾郵件。名單越多、發出的 Wave 越多，目標 (Marks) 出現的速度越快。
    - 注意衰減 (Diminishment)：短時間發出過多同型 Wave 效益會大幅下降。
3. 現場說服 (Scamming)：
    - 這是獲取 CS 最快的主動階段。

### 說服條核心機制說明 (Persuasion Bar Mechanics)

說服條共有 50 格。你的目標是移動指標 (Pip) 進入綠色的 Reward 區域進行結案。

#### 關鍵回應動作說明 (Key Responses Details)

- Strong Forward：大幅向右移動。
- Soft Forward：微幅向右移動，用於微調位置避開紅區。
- Backward：向左微動，避開障礙或微調。
- Accelerate：不移動，但百分比提升下一次動作的位移，最高可疊加 5 次，用於一次性越過大面積紅區。
- Capitalize (結案)：僅在 Reward 區域可用，完成詐騙領取獎勵。經驗與獎金隨 Low -> Medium -> High 遞增。

#### 區域類型與效果分類 (Cell Types & Effects)

- Reward (綠)：結案區域。
- Temptation (黃)：向右大幅位移，且保證跳過所有紅區/負面區域，直接降落在安全地帶。
- Sensitivity (紫)：向左位移，跳過獎勵區直接進入安全位。
- Hesitation (褐)：軟失敗並進入 1-2 小時冷卻。
- Concern (橙)：軟失敗並觸發疑慮，需額外花費 3N 嘗試解除 (Resolve)。
- Fail (紅)：致命失敗 (Critical Failure)，任務直接消失。

### 多疑度紅區擴張機制 (Suspicion Expansion Mechanism)

- 觸發：一旦指標離開初始第一格，多疑度即開始運作。
- 擴張規則：每執行一次動作，紅區會由左向右線性擴張（覆蓋除當前站位以外的所有格子）。
- 步數限制：通常一次詐騙只能承受 10-12 次動作，超過後說服條將被紅區填滿。

#### 基礎準備與升級路徑 (Preparation & Growth)
- 核心教育：
- CMT2130 & CMT2131 (Computer Science)：解鎖被動電郵收集器 (Passive Email Gatherers)。 - PSY2132 (Psychology)：極其關鍵，能讓你預見不同動作後的落點。
- 郵件農耕策略：建議手動與被動結合，累積達 20,000 封郵件。當被動收集器失效時應立即補上，期間可以進行其他犯罪。
- 升級路徑：當擁有 20k 郵件後，每日對 5 個最低級詐騙各發送一波郵件，並依照生成的目標進行詐騙，直到達到 CS 100。
- 安全至上：絕不冒險踩踏紅色點位 (Red Pip)。如果可跳轉範圍內包含紅區，寧可更換路徑或直接放棄 (Abandon) 該任務。在 Scamming 中，一次失敗導致的經驗損失往往需要 10 次以上的成功才能彌補。


#### 最佳收益獲利策略 (Best Income Strategy)

- 目標類別：Investment (需 CS80) 或 Job (需 CS60)。
- 收益：瞄準 Affluent (1000% 加成) 或 Professional (300% 加成) 的目標。
- 策略：在 CS100 下，即便指標位移波動大，也能透過五疊加的 Accelerate 穩定落入高額獎酬區，潛在獲利單次可達 $2.5m。

### 功勳勳章成就項 (Merit Medals & Achievements)

- Alpha Mail：CS 達 100。
- Decepticon：在單次成功的詐騙中，同時降落過 Temptation, Sensitivity, Hesitation 與 Concern 四個負面區域。

## 搜尋現金犯罪策略指南 (Search For Cash Strategy)

SFC (Search For Cash) 是 Crimes 2.0 的入門犯罪，也是解鎖後續許多犯罪零件的主要途徑。本犯罪屬於特殊 (Special) 類別。

- 完成所需 Nerve：6400 (約 16 天)
- 增強器 (Enhancer)：Glasses
- 其他關鍵道具：Metal Detector, Cemetery Key


### 關鍵道具與地點解鎖 (Items & Unlocks)

- Glasses (Enhancer)：提升 5% 的 CE 與 CS 獲得。取得途徑：地鐵搜索 (Subway) 或 扒竊商務女性 (Pickpocketing) Businesswoman。
- Metal Detector (關鍵道具)：解鎖海灘 (Beach) 位置。取得途徑：報廢場搜索 (Junkyard) 達 CS30。
- Cemetery Key (關鍵道具)：解鎖墓地 (Cemetery) 位置。取得途徑：海灘搜索 (Beach) 達 CS50。
- Lost and Found Office Key (Office Key)：解鎖地鐵 (Subway) 的額外高額回報結果。取得途徑：地鐵搜索達 CS85。

### 搜尋區域詳細分類與產出 (Region Details & Loot)

#### 垃圾桶 (Searching the Trash)
- 解鎖條件：無。
- 成功率循環：週循環。週一 18:00 TCT 從 0% 開始上升，週一 08:00 TCT 達到峰值，隨後驟降重啟。
- 重點產出：Card Skimmer (信用卡側錄器)、Spray Can (噴漆罐)。

#### 地鐵站搜尋區域 (Searching the Subway)
- 解鎖條件：無。
- 成功率循環：日循環。根據全服活躍玩家數量變動。
- 重點產出：Billfold (錢包)、Office Key (CS85)。

#### 報廢場搜尋區域 (Searching the Junkyard)
- 解鎖條件：無。
- 成功率循環：週規律但較不穩定。週日與週一上午為峰值。
- 重點產出：犯罪零件核心。Spray Can、Card Skimmer、Spy Camera、Rope、Blank DVD、Computer Parts 以及 Metal Detector (CS30)。

#### 海灘搜尋區域 (Searching the Beach)
- 解鎖條件：持有 Metal Detector。
- 成功率循環：潮汐機制。隨日期與月份變動，區分為高潮與低潮期。
- 重點產出：Cemetery Key (CS50)、Stash Box、Sand (低潮期 70%+ 產出)。風險較高，受傷機率大。

#### 墓地搜尋區域 (Searching the Cemetery)
- 解鎖條件：持有 Cemetery Key。
- 成功率循環：日間固定規律。週一至週五 09:00 - 17:00 管理員活動期成功率極低，其餘時間較高 (25%/75%)。
- 重點產出：Hit Contract (暗殺零件)、Car Keys (偷車零件)、Fertilizer、Candles。

#### 噴泉搜尋區域 (Searching the Fountain)
- 解鎖條件：CS75。
- 成功率循環：月循環。每月 1 號從 0% 開始上升，月底達到峰值。
- 重點產出：Loot Containers (戰利品箱)、Spray Can。收益普遍被認為較低，主要用於提升 CS。

### 戰術路徑建議彙整 (Tactical Path Recommendations)

#### 快速升級路徑 (Quick Leveling)
- 優先地點：垃圾桶 (Trash) 與 地鐵 (Subway)。
- 策略：這兩個地點 Nerve 消耗低且成功率回升快。CS20 以前專注於垃圾桶累積基礎零件，CS20 後轉向地鐵以獲取更穩定的 CS 成長。

##### 最佳收益獲利策略 (Best Income Strategy)
- 目標地點：地鐵 (Subway) 搭配 Office Key。
- 收益來源：持有 Office Key 時，地鐵會出現高額現金結果。
- 次選：海灘 (Beach) 搜尋 Stash Box，雖然風險高，但單件價值極大。

#### 實戰戰術執行總結 (Tactics Execution Summary)
- 除了尋找 Unique 外，平時應專注於選擇成功率百分比高的選項。
- 由於各犯罪地點的成功率隨時間循環，建議參考詳細攻略中的規律來安排神經值分配。


### 功勳勳章成就項 (Merit Medals & Achievements)

- Pay Dirt：CS 達 100。
- Spoiled Rotten：蒐集滿 7 種腐爛物品。僅限在「垃圾桶」中搜出才計數，無法透過交易取得。最後兩件通常需要 CS45+ 才會出現。
- Shore Thing：在海灘低潮期搜出 Sand。使用 Bucket (桶子) 道具可大幅提升機率。這不是 Unique 掉落，可能需要消耗 600+ Nerve 才能達成。

## 商店偷竊犯罪策略指南 (Shoplifting Strategy)

Shoplifting 是一項涉及安保規律與聲名狼藉度 (Notoriety) 管理的犯罪，屬於盜竊 (Theft) 類別。本犯罪屬於 Crimes 2.0 系統的一部分。

- 完成所需 Nerve：9700 (約 25 天，但建議拉長時間以刷特殊彈藥)
- 增強器 (Enhancer)：Mountain Bike
- 其他關鍵道具：Torn City Times (報紙)


### 基礎需求與輔助道具清單 (Requirements & Items List)

- 核心消耗：每次嘗試消耗 Nerve (視地點而定，通常為低 Nerve)。
- 輔助道具 (不具扣除性)：
    - Mountain Bike (增強器)：提升 CS/CE 獲得，並解鎖高價值產出。取得途徑：Junkyard 搜尋或 扒竊 Cyclist。
    - Torn City Times (報紙)：解鎖所有地點的額外結果。取得途徑：SFC 地鐵 (Subway) 唯一發現。
    - 著裝建議：著裝（外套、內衣等）被認為能減少部分 Crit 結果。

### 店鋪分類與風險等級詳解 (Shops & Security Risks)

| 店鋪名稱 | 風險等級 | 主要產出 |
| --- | --- | --- |
| Sally's Sweet Shop | 極小 (Minimal) | 糖果 (25H 為主) |
| Bits 'n' Bobs | 較小 (Minor) | 林雜工具 (Gasoline, Glow Stick, 增強器) |
| TC Clothing | 較低 (Low) | 各類服飾 |
| Super Store | 中等 (Moderate) | 電子零件 (Blank DVD, Spy Camera) |
| Pharmacy | 中等 (Moderate) | 醫療耗材 (Ipecac Syrup) |
| Cyber Force | 中等 (Moderate) | 電腦零件 (HPCPU, Heat Sink) |
| Jewelry Store | 高 (High) | 珠寶飾品 (手錶、戒指) |
| Big Al's Gun Shop | 極高 (Very High) | 武器、護甲、特殊彈藥 (Special Ammo) |

### 安保維護與攝像頭規律 (Security & Camera Measures)

每個地點有不同層級的安保系統，當系統在線時，Notoriety 增長會大幅提升。

#### 攝像頭監控機制 (Camera Monitoring Mechanism)
- 影響：增加 Notoriety 增長。
- 循環：每日幾次維護 30-60 分鐘。攝像頭越多，維護間隔越長。

#### 安全檢查點機制 (Security Checkpoint Mechanism)
- 影響：導致失敗機率增加。
- 循環：約每 3-4 天維護一次，每次持續 8-12 小時。

#### 保全守衛巡邏規律 (Security Guard Patrol)
- 影響：顯著提升失敗與 Crit 機率。
- 循環：每 4-8 小時休息 10-15 分鐘。這是最高價值的操作窗口。

### 聲名狼藉度核心機制 (Notoriety Core Mechanics)

- 累積：成功偷竊會緩慢增加，失敗/Crit 增加更多。
- 門檻區間：
    - 低 (<10%) / 中 (>10%) / 高 (>30%) / 極高 (>60%)
- 影響：Notoriety 越高，失敗率越高；Crit 時導致的監禁時間越長（最高可達 17 小時）。
- 衰減：每 5 分鐘衰減 1%（從上次嘗試起算）。完全清空需 8 小時 20 分鐘。

### 戰術路徑建議

#### 聲名狼藉度功勳路徑 (Notoriety Merit Path)
- 建議儘快完成：CS 越低越容易達成。CS 提高後成功率上升，反而難以推滿 Notoriety。
- 衝刺方式：堆疊 Nerve (Alcohol, Refill, Job Points)，在短時間內連續偷竊同一個保安完好的高風險店鋪。
- 反向策略：暫時將 Mountain Bike 與 Newspaper 移入 Display Case 以降低成功率。

#### 戰術路徑建議彙整 (Tactical Path Recommendations)
- 目標：Big Al's Gun Shop。
- 核心：僅在安保系統（特別是守衛）處於維護/休息狀態時進入。這不但是為了安全，更是獲取 特殊彈藥 (Special Ammo) 的唯一機會。
- 武器篩選：獲得的彈藥有一半機率是為你目前裝備的武器量身打造。如果你不想要某種爛武器的彈藥，請在刷之前先將其從裝備欄移除。
- 外部工具：建議使用相關 Userscript 在 Big Al 安保關閉時發送通知。



#### 快速技能升級路徑 (Quick Leveling Path)
- 優先地點：Sally's Sweet Shop 或 Bits 'n' Bobs。
- 策略：這兩個地點難度極低，適合在高 Notoriety 時持續作業以累積 CS。CS 到達 50 後，穩定在 Super Store 偷取電子零件是中後期的主要經驗來源。

#### 最佳收益獲利策略 (Best Income Strategy)
- 目標地點：Big Al's Gun Shop。
- 收益來源：特殊彈藥 (Special Ammo)。
- 策略：僅在安保最薄弱（守衛不在）時進入，獲取特殊彈藥後在市場販售，這是 Shoplifting 獲利最高的途徑。

### 推薦從事公司 (Best Recommended Companies)

- 首選：家具店 (Furniture Store)：5星福利提供被動的 15% Theft 經驗與技能加成。能有效降低 Notoriety 對成功率的負面影響，並加速衝刺 CS100。
- 功能選擇：遊樂園 (Amusement Park)：10星福利 (10% 加成) 適合同時進行多項不同類別犯罪的玩家。

### 嚴重失敗風險評估 (Serious Failure Risk Assessment)

- 損失生命值或住院。
- 監禁：時間受當前 Notoriety 影響很大。
- 道具損失：極低機率損失 Mountain Bike 或 Torn City Times 報紙。

## 劫獄技術建議指南 (Jail Busting Strategy)

劫獄 (Busting) 是將被囚禁在監獄中的玩家營救出來的行為。雖然其提供的 Crime Experience (CE) 較少，但在獲取 Merits (共 11 枚勳章，最高達 10,000 次) 與協助幫派成員方面具有極高價值。

### 劫獄成功率核心機制 (Core Busting Success Mechanics)

劫獄的成功機率並非固定，而是由以下變數動態計算：

- 你的等級 (Your Level)：等級越高，成功率越高。
- 目標難度 (Target Difficulty)：
    - 目標等級：等級越高，越難成功。
    - 剩餘刑期：刑期越長，難度越高。計算時通常會額外增加 3 小時的緩衝時間。
- 失敗後果：成功 (Success)、失敗但不入獄 (Fail)、失敗並入獄 (Caught)。入獄不會導致 CE 或 Nerve Bar 的實質損失。

### 劫獄加成資源匯整 (Busting Perks & Resources)

- 教育 (Education)：詳見 功勳分配指南 (Merits Assignment Guide)
    - LAW2920 / LAW2970：分別提升 5% 與 10% 的劫獄技能。
    - LAW3102：劫獄難度降低 50%。
- 公司 (Law Firm)：詳見 公司系統總覽 (Company System Overview)
    - 5星 (Closing Argument)：更容易一次劫出多人。
    - 10星 (Educated Decision)：可在嘗試前直接查看成功機率。
- 幫派 (Faction)：詳見 公司系統總覽 (Company System Overview)
    - Bust Skill：最高提升 50% 成功率。
    - Bust Nerve：將每次劫獄消耗降低至 2N (原為 5N)。
- 書籍 (Book)：詳見 書籍系統核心概覽 (Torn Books System Overview)
    - "Shawshank Sure Ain’t For me!"：31 天內大幅提升劫獄與越獄能力。建議在此期間衝刺 Merits。

### 劫獄失敗懲罰機制 (Busting Penalty Mechanism)

劫獄具備累積性的懲罰機制。每成功劫獄一次，後續的成功率會暫時下降。

- 持續時間：單次成功後的懲罰需 72 小時 (3 天) 才能完全消失。
- 恢復曲線：非線性恢復。10 小時後即可恢復約 50% 的懲罰。
- 等級優勢：你的等級越高，每次成功劫獄所累積的懲罰值就越小。
- 建議：若成功率顯著下降，應暫時停止並等待數小時恢復。

### 劫獄具體戰術建議 (Specific Busting Tactics)

#### 快速升級路徑 (Quick Leveling Path)
- 目標選擇：優先挑選低等級 (如 Level 1-10) 且刑期極短 (30 分鐘以內) 的目標。
- 頻率管理：在懲罰剛開始累積時，一天可嘗試數十次，但隨著成功率下降，應拉長操作間隔。

#### 極化收益考量 (Best Income Considerations)
- 注意：劫獄本身不提供金錢收益，其最高價值在於 Merits。詳見 功勳分配指南 (Merits Assignment Guide)
- 終極目標：達成 10,000 次劫獄以獲得最終獎勵。

### 越獄自我救贖機制 (Self-Busting Mechanics)
- 消耗：最大 Nerve 的 1/2。完成教育 LAW2990 後降為 1/3。
- 限制：不計入統計數據中的劫獄次數。成功率與一般劫獄機制不同，不建議作為常規手段。

## External sources

- https://www.torn.com/forums.php#/p=threads&f=61&t=16438960&b=0&a=0
- https://www.torn.com/forums.php#/p=threads&f=61&t=16510947&b=0&a=0
- https://www.torn.com/forums.php#/p=threads&f=61&t=16341811
- https://www.torn.com/forums.php#/p=threads&f=61&t=16353303
- https://www.torn.com/forums.php#/p=threads&f=61&t=16350490
- https://www.torn.com/forums.php#/p=threads&f=61&t=16373016
- https://www.torn.com/forums.php#/p=threads&f=61&t=16367936
- https://www.torn.com/forums.php#/p=threads&f=61&t=16388086
- https://www.torn.com/forums.php#/p=threads&f=61&t=16344567
- https://www.torn.com/forums.php#/p=threads&f=61&t=16363421
- https://www.torn.com/forums.php#/p=threads&f=61&t=16358739
- https://www.torn.com/forums.php#/p=threads&f=61&t=16418415
- https://www.torn.com/forums.php#/p=threads&f=61&t=16343473
- https://www.torn.com/forums.php#/p=threads&f=61&t=16346491
- https://www.torn.com/forums.php#/p=threads&f=61&t=16192039&b=0&a=0
