# 犯罪 2.0 系統核心機制總覽 (Crimes 2.0 Overview)

本文件整理了 Crimes 2.0 的通用機制與重要優勢，適合所有剛從 1.0 遷移的玩家。

## 系統遷移優勢分析 (Migration Advantages Analysis)

- CE (Crime Experience)：現行 2.0 的 CE 獲取效率極佳，尤其是達成縱火 ([[crimes/arson|Arson 2.0]], 屬於 Vandalism 類別) 的進階目標後。沒有理由為了 CE 留在 1.0。
- 功勳 (Merits)：2.0 提供了更多的功勳，且未來 1.0 的功勳在系統強制遷移後可能會遺失。
- OC 2.0 連動：參與 Crimes 2.0 能極大提升組織犯罪 ([[factions/organized-crime-2.0|OC 2.0]]) 的成功率。在系統判斷中，通常直接以 NNB 作為衡量玩家 CE 是否足以勝任該項組織犯罪的標準。
- 經濟效益：雖然 2.0 目前的直接金錢收益較低，但長期而言，技能提升帶來的效益更高。

## 核心機制說明 (Core Mechanics)

- CS (Crime Skill)：每項犯罪獨立的等級，直接影響該犯罪的成功率與高階目標解鎖。
- CE (Crime Experience)：隱藏的綜合數值，決定 NNB 的上限。雖然 2.0 的單次獲取量未公開，但達成高神經值犯罪目標是提升 CE 的關鍵。
- NNB (Natural Nerve Bar)：扣除所有加成後的基礎神經上限，是觀測 CE 進度的唯一量化指標。
- 大失敗 (Critical Failure)：不僅會導致 Nerve 浪費，還會造成 CS 與 CE 下降，並伴隨扣血、入獄、住院或相關道具遺失。
- 獨有掉落 (Unique)：特定犯罪在達成 CS 門檻後有機率出現（空心星星圖標），每種掉落每位玩家限領一次。

## 外部增益與加成匯整 (External Buffs & Bonuses)

- 城市工作：[[jobs/city-careers|Law 法律職業]]能顯著提升犯罪進度。
- 派系 Perk：最高可提供 10% 的犯罪進度加成。詳見 [[factions/overview|派系系統]]。
- 教育課程：心理學學士學位 (Psychology bachelor) 在 2.0 中非常強大。詳見 [[education/priorities|教育優先級]]。
- 增強器 (Enhancers)：
  - 使用方式：放在物品庫 (Inventory) 即可生效，無需裝備。
  - 核心價值：增加 CS/CE 獲取率、提升成功率、解鎖特殊項目或減少作業時間。
  - 大失敗風險：若遭遇大失敗 (Crit)，增強器有機率毀損或消失。

## 建議進度策略 (Recommended Progression Strategy)

為了最大化 Nerve 效率與功勳進度，建議採取 1 Active + Multi Passive 的並行模式，並注意以下原則：

- 平衡發展：不要盲目追求高 CE 而忽視 CS。若 CS 過低，即便 CE 足夠，嘗試高難度目標時的大失敗機率依然極高。
- 主動衝刺 (Active)：將每日主要的 Nerve 消耗在單一高品質、高神經值消耗的犯罪上。
  - 推薦：[[crimes/burglary|Burglary]] (直到 CS80+), [[crimes/pickpocketing|Pickpocketing]] (CS100 收益最佳), 或正在解鎖功勳的項目。
- 被動累積 (Passive)：利用時間或冷卻機制，作為背景操作，不應讓其佔用過多主動 Nerve。
  - [[crimes/card-skimming|Card Skimming]]：安裝後放著累積資料。
  - [[crimes/forgery|Forgery]]：啟動生產後等待冷卻，非必要不頻繁檢查。
  - [[crimes/scamming|Scamming]]：依賴受教育解鎖的被動郵件收集器，累積達 20,000 封後才集中消耗。
  - [[crimes/bootlegging|Bootlegging]]：將 DVD 交給員工處理，定期檢查庫存即可。
- 戰術調度：手頭保留低難度犯罪 (如 [[crimes/graffiti|Graffiti]]) 用於在高難度犯罪大失敗後快速清除負面狀態。
- 資訊查看：在遊戲介面點擊每種犯罪的圖片，可查看該項犯罪的詳細進度資訊。


## 功勳與勳章級距說明 (Merits & Medals Details)

每項犯罪通常包含：
- 1 個技能達 100 的功勳。
- 1 個特定行為功勳。
- 數個根據犯罪次數發放的勳章。

### 勳章發放級距標準 (Medal Tier Standards)
100, 200, 300, 500, 750, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 6000, 7500, 10000

## 參考資料連結 (Reference Sources)

- [Crimes 2.0 Deep Dive by Baldr](https://www.torn.com/forums.php#/p=threads&f=61&t=16374814&b=0&a=0)
