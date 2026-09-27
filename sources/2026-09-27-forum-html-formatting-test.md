source: https://www.torn.com/forums.php#/p=threads&f=46&t=16051765&b=0&a=0&start=29080&to=27946100 (post by Noteasy_na, "Sweet Haven Training Slot Open!") + user's editor test
date: 2026-09-27

Observed DOM of the post (read via browser):

- Container: div.post-container.editor-content.bbcode-content > div.post.unreset
- No <img> elements; the whole card is HTML with inline style attributes.
- Outer box: background-color:#0b0f19; border:2px solid #38bdf8; border-radius:12px; padding:22px; color:#ffffff; font-family:'Segoe UI', Arial, sans-serif; max-width:620px; margin:0 auto;
- Badge span: background-color:#38bdf8; color:#0b0f19; font-size:10px; font-weight:800; padding:3px 12px; border-radius:20px; letter-spacing:1.5px; text-transform:uppercase;
- h1: color:#38bdf8; font-size:24px; margin:8px 0 2px 0; text-transform:uppercase; letter-spacing:1.5px; line-height:1.2;
- Subtitle div: color:#94a3b8; font-size:13px; margin-top:2px;
- Card div: background-color:#111827; border:1px solid #1e293b; border-radius:8px; padding:16px; margin-bottom:14px; text-align:center;
- Card label: color:#fbbf24; font-size:12px; font-weight:bold; text-transform:uppercase; letter-spacing:1px;
- Card value: color:#34d399; font-size:22px; font-weight:800;
- Emoji used directly as icons.

User's test in the forum post editor (Edit mode, Source Code "{}" button at the right end of the toolbar):

- Rendered correctly: border-radius pill badge, uppercase + letter-spacing title, nested card with background and border, border-left accent bar, inline colored span, highlight span, dashed border, linear-gradient background, box-shadow glow, display:flex two-column row, small gray footer.
- Rendering after actually submitting the post was not tested.
