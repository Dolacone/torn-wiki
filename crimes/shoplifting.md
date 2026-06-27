# 商店偷竊犯罪策略指南 (Shoplifting Strategy)

Shoplifting 是一項涉及安保規律與聲名狼藉度 (Notoriety) 管理的犯罪，屬於盜竊 (Theft) 類別。

- 完成所需 Nerve：9700 (約 25 天，但建議拉長時間以刷特殊彈藥)
- 增強器 (Enhancer)：Mountain Bike
- 其他關鍵道具：Torn City Times (報紙)


## 基礎需求與輔助道具清單 (Requirements & Items List)

- 核心消耗：每次嘗試消耗 Nerve (視地點而定，通常為低 Nerve)。
- 輔助道具 (不具扣除性)：
    - Mountain Bike (增強器)：提升 CS/CE 獲得，並解鎖高價值產出。取得途徑：Junkyard 搜尋或扒竊 Cyclist。
    - Torn City Times (報紙)：解鎖所有地點的額外結果。取得途徑：SFC 地鐵 (Subway) 唯一發現。
    - 著裝建議：著裝（外套、內衣等）被認為能減少部分 Crit 結果。

## 店鋪分類與風險等級詳解 (Shops & Security Risks)

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

## 安保維護與攝像頭規律 (Security & Camera Measures)

每個地點有不同層級的安保系統，當系統在線時，Notoriety 增長會大幅提升。

### 攝像頭監控機制 (Camera Monitoring Mechanism)
- 影響：增加 Notoriety 增長。
- 循環：每日幾次維護 30-60 分鐘。攝像頭越多，維護間隔越長。

### 安全檢查點機制 (Security Checkpoint Mechanism)
- 影響：導致失敗機率增加。
- 循環：約每 3-4 天維護一次，每次持續 8-12 小時。

### 保全守衛巡邏規律 (Security Guard Patrol)
- 影響：顯著提升失敗與 Crit 機率。
- 循環：每 4-8 小時休息 10-15 分鐘。這是最高價值的操作窗口。

## 聲名狼藉度核心機制 (Notoriety Core Mechanics)

- 累積：成功偷竊會緩慢增加，失敗/Crit 增加更多。
- 門檻區間：
    - 低 (<10%) / 中 (>10%) / 高 (>30%) / 極高 (>60%)
- 影響：Notoriety 越高，失敗率越高；Crit 時導致的監禁時間越長（最高可達 17 小時）。
- 衰減：每 5 分鐘衰減 1%（從上次嘗試起算）。完全清空需 8 小時 20 分鐘。

## 戰術路徑建議

### 聲名狼藉度功勳路徑 (Notoriety Merit Path)
- 建議儘快完成：CS 越低越容易達成。CS 提高後成功率上升，反而難以推滿 Notoriety。
- 衝刺方式：堆疊 Nerve (Alcohol, Refill, Job Points)，在短時間內連續偷竊同一個保安完好的高風險店鋪。
- 反向策略：暫時將 Mountain Bike 與 Newspaper 移入 Display Case 以降低成功率。

### 戰術路徑建議彙整 (Tactical Path Recommendations)
- 目標：Big Al's Gun Shop。
- 核心：僅在安保系統（特別是守衛）處於維護/休息狀態時進入。這不但是為了安全，更是獲取特殊彈藥 (Special Ammo) 的唯一機會。
- 武器篩選：獲得的彈藥有一半機率是為你目前裝備的武器量身打造。如果你不想要某種爛武器的彈藥，請在刷之前先將其從裝備欄移除。
- 外部工具：建議使用相關 Userscript 在 Big Al 安保關閉時發送通知。



### 快速技能升級路徑 (Quick Leveling Path)
- 優先地點：Sally's Sweet Shop 或 Bits 'n' Bobs。
- 策略：這兩個地點難度極低，適合在高 Notoriety 時持續作業以累積 CS。CS 到達 50 後，穩定在 Super Store 偷取電子零件是中後期的主要經驗來源。

### 最佳收益獲利策略 (Best Income Strategy)
- 目標地點：Big Al's Gun Shop。
- 收益來源：特殊彈藥 (Special Ammo)。
- 策略：僅在安保最薄弱（守衛不在）時進入，獲取特殊彈藥後在市場販售，這是 Shoplifting 獲利最高的途徑。

## 推薦從事公司 (Best Recommended Companies)

- **首選：家具店 (Furniture Store)**：**5星**福利提供被動的 **15% Theft 經驗與技能加成**。能有效降低 Notoriety 對成功率的負面影響，並加速衝刺 CS100。
- **功能選擇：遊樂園 (Amusement Park)**：10星福利 (10% 加成) 適合同時進行多項不同類別犯罪的玩家。

## 嚴重失敗風險評估 (Serious Failure Risk Assessment)

- 損失生命值或住院。
- 監禁：時間受當前 Notoriety 影響很大。
- 道具損失：極低機率損失 Mountain Bike 或 Torn City Times 報紙。

## 參考資料 (References)

https://www.torn.com/forums.php#/p=threads&f=61&t=16346491
