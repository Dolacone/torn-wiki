# 組織犯罪指南 (Organized Crime 2.0)

本指南整理自官方論壇與玩家研究，介紹 Crimes 2.0 系統下的組織犯罪 (OC) 機制。

## 核心術語表 (Glossary)

- CPR (Checkpoint Pass Rate)：關卡通過率。玩家在其選擇的角色中通過各個 Checkpoints 的機率。
- Tier：OC 的生成等級，範圍為 1 到 5。影響 Scope 成本與獎勵。
- Level：OC 的難度等級，範圍為 1 到 10。影響 CPR、金錢、物品與 Respect 獎勵。
- Role：OC 內的職位。不同職位有不同的 CPR 判定標準。

## 基礎機制概念 (Basics)

- Scenario (情境)：決定 OC 的角色構成與預期獎勵。
- 難度等級 (Difficulty Level)：等級越高，挑戰難度與獎勵越高。在進度階段開始前，玩家可以自由退出。
- 加入方式：玩家必須手動前往 Organized Crimes 頁面點擊 JOIN。第一個成員加入後，計時器即開始執行。

## 成員角色指標 (Role Metrics)

每個角色有兩個核心指標：

### 策劃進度說明 (Planning Completion)
- 追蹤個別玩家的策劃時程。
- 每個參與者通常需要 24 小時。
- 採順序計時：第一個玩家完成後，第二個才開始，依此類推。
- 策劃期間玩家可以出國或被住院 (permahosped)，不影響進度。

### 關卡成功率說明 (Checkpoint Pass Rate)
- CPR 數值越高，該關卡成功機率越高。
- 由角色需求與玩家能力決定，受以下因素影響：
  - Battlestats：Strength 與 Defense 影響戰鬥類角色 (如 Muscle/Enforcer)；Dexterity 影響手藝類 (如 Thief/Picklock)；Speed 影響反射類 (如 Sniper/Robber)。Battlestats 增益在 1b 左右達到上限。
  - Workstats：Endurance (END) 影響體能類 (如 Muscle)；Intelligence (INT) 影響智謀類 (如 Negotiator)；Manual (MAN) 效果尚不明確。Workstats 上限理論值為 300k。
  - Crime Skills (CS)：特定的犯罪技能對應特定角色 (如 Cracking 對應 Hacker)。CS 超過 100 後仍會持續提升 CPR。
  - CE (Crime Experience)：作為 CPR 計算的加權乘數。
  - 其他技能：Hunting (對應 Assassin)、Racing (對應 Driver/Hijacker)、Reviving (對應 Reviver)。
- 建議選擇 CPR 為綠色 (75+) 的角色。

## 執行材料要求 (Materials)

- 種類：分為 Tools (工具，標示綠勾，不消耗) 與 Consumables (消耗品，標示箭頭，成功後消耗)。
- 檢查：成員若未攜帶必要材料，OC 將無法進入執行階段 (Execution Stage)。
- 借用：可直接從 Faction armories 借用角色所需材料。道具借用無限制，消耗品會優先使用借用的庫存。
- 圖示：若成員缺少材料，其角色旁會顯示紅色的禁止符號。

## 計時器與執行限制 (Timer & Limitations)

計時器結束且滿足以下所有條件後，OC 才會正式執行：

### 暫停與阻塞條件 (Pause & Block Conditions)
- OC 未滿員且所有成員已完成 Planning。
- 至少一名成員在住院 (Hospitalized)。
- 至少一名成員在監獄 (Jail)。
- 至少一名成員正在出國途中或在國外 (Flying/Abroad)。
- 至少一名成員缺少必要材料 (Materials)。

## 偵查資源機制 (Scope)

Scope 是生成 OC 所需的資源。

- 再生速度：每日被動回復 1 點。
- 獲得途徑：成功完成 OC 可獲得 (1 + OC Tier) 點。
- 儲存上限：100 點。
- 每日生成成本：成本等於該 OC 的 Tier。

## 生成等級說明 (Spawning & Tiers)

OC 分為 5 個 Tier，需透過 Faction upgrades 解鎖。

- 成功率平衡：高難度 OC 可能導致 Scope 虧損，需維持特定成功率以保持穩定：
  - Tier 1：50%
  - Tier 2：66%
  - Tier 3：75%
  - Tier 4：80%
  - Tier 5：50%

## 連鎖任務機制 (Chain OCs)

- 出現等級：Level 5 以上。
- 機制：完成後不直接領取獎勵，而是生成高一級的 OC。
- 獎勵：僅在連鎖最末端成功後發放。
- 特性：Tier 5 的 OC 均為連鎖形式。獎勵通常高於同等級的單一 OC。

## 進階執行策略 (Advanced Mechanics)

### 分階段執行技術 (Staging)
- 利用 Planning 順序計時的特性，組建不完整團隊來進行 Planning。
- 當其他 OC 完成且玩家空出時再填入剩餘位置，以最大化團隊產出。
- 9 人架構執行 6 人 OC 可提升 33% 的每人小時收益；12 人架構可提升 50%。

### 關卡類型解析 (Checkpoints)
1. Mainline (主線)：收益最高路徑。失敗後可能進入 Recovery。
2. Recovery (恢復)：失敗後的緩衝，成功後可回歸主線，通常不減收益。
3. Lenient (寬容)：寬鬆的關卡，通常提供兩次恢復機會，常見於 OC 開頭。
4. Critical (關鍵)：失敗即進入低收益分支出。
5. Determinant (決定性)：失敗可能導致 OC 直接終止或大幅扣除獎勵。

## 派系管理策略建議 (Strategic Advice)

- 安排成員：將 CPR 較弱的成員放在 Lenient roles，將強者放在 Critical roles。
- 預先生成：OC 在過期前可存放 7 天，建議在 Scope 達到 100 前預先生成。
- 獎勵比較：對於大多數派系，OC 2.0 的收益通常優於 1.0 的 PA (Political Assassination)，除非派系內主要由高回報 PA 組成。

## 參考資料 (References)

- [Organized Crime 2.0 Guide by Roth](https://www.torn.com/forums.php#/p=threads&f=61&t=16438960&b=0&a=0)
