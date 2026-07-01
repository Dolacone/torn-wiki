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
- 更新了 [combat-mechanics.md](file:///C:/Users/Dolacone/Dropbox/wiki/torn/attacking/combat-mechanics.md) 的 End Game (25% 暴擊) 傷害修正分析表，並附上詳細的算式與參數以利重現。

## [2026-07-01] edit | Fuelling Your Way To Failure prep calculation

- Added Energy Drink prep calculation to items/books-catalog.md.
- Derived from user-provided Restaurant Professional Metabolism perk (25% consumable CD reduction) and known multipliers (faction x1.5, book x2, event x2).
- Confirmed two-cycle (Fuelling Your Way To Failure + Memories And Mammaries repeat) can total (~992) matches existing ~1000 can estimate.
