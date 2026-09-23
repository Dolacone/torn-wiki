# Torn Wiki — Log

Append-only chronological record of all Ingest operations.

---

## [2026-06-27] migration | llm-wiki schema bootstrap

- Migrated AGENTS.md to llm-wiki three-layer schema (sources/wiki/schema).
- Added Ingest, Query, Lint workflow definitions.
- Created index.md cataloging 60 existing wiki pages across 15 directories.
- Created log.md as the append-only operation record.
- sources/ directory established for future raw source ingestion.

## [2026-06-28] ingest | 防具特效與屬性公式折算

- 讀取並整合了 Wiki 上的防具特殊加成 (Advanced Armor Bonuses) 與最低屬性數值。
- 驗證了防禦減傷與敏捷命中公式，並將其轉化為等效 EHP 傷害折算因子。
- 更新了 [[combat-mechanics]] 的 End Game (25% 暴擊) 傷害修正分析表，並附上詳細的算式與參數以利重現。

## [2026-07-08] ingest | Ignorance Is Bliss Guide

- 導入關於稀有書籍 Ignorance Is Bliss 使用策略的論壇指南。
- 新增專屬 Wiki 頁面 [[ignorance-is-bliss]]，詳細解析 Happy 提升與訓練策略。
- 更新 [[books-catalog]] 與 [[happy-jumping]] 中的交叉連結。

## [2026-07-11] edit | 戰鬥公式與防具特效修正

- 修正 [[combat-formulas]] 中的防禦減傷公式，細分屬性優勢與劣勢段的分段係數（14倍與32倍）。
- 檢驗並指出原有簡化命中率對數公式在中低倍數區間的低估誤差，補充更精準的中低倍數對數擬合與 Logistic 理論模型。
- 更新 [[combat-mechanics]]，基於對稱插值重新計算 Vanguard 套裝敏捷被動提升後的命中率與防護等效係數（從 0.9560 修正為 0.7255）。

## [2026-08-28] ingest | 淘汰賽活動指南 (Elimination Event Guide)

- 新增 [[elimination]]，彙整 Elimination 全服淘汰賽之核心機制、報名門檻、新手生存策略與商業機會。
- 更新 [[index]]，在 events 分類新增 elimination 導覽索引。

