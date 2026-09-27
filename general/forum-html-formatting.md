# 論壇 HTML 排版 (Forum HTML Formatting)

Torn 論壇編輯器可以直接貼 HTML + inline CSS，做出卡片、膠囊標籤、漸層等排版。適合用在 [[event-trading]] 或 Train 買賣這類廣告貼文。

## 輸入方式

1. 開啟發文或 Edit 編輯器。
2. 按工具列最右邊的 `{}` (Source Code) 按鈕。
3. 貼上 HTML，所有樣式都寫在 `style="..."` 屬性。
4. 切回一般模式預覽。

- 不需要 `<img>`，圖示直接用 emoji。
- 不使用 `<style>` 區塊或 class，只用 inline style。
- 已驗證範圍：Edit 模式預覽。正式送出後是否被 server 過濾：未驗證。

## 已驗證可用的 CSS

| 效果 | 屬性 |
|---|---|
| 背景色、文字色 | `background-color`、`color` |
| 外框、圓角 | `border`、`border-radius` |
| 左側色條 | `border-left` |
| 虛線框 | `border: 1px dashed` |
| 字級、粗細 | `font-size`、`font-weight`、`font-family` |
| 全大寫、字距 | `text-transform:uppercase`、`letter-spacing` |
| 間距 | `padding`、`margin`、`line-height` |
| 置中、限寬 | `text-align:center`、`max-width` + `margin:0 auto` |
| 漸層背景 | `background: linear-gradient(...)` |
| 發光陰影 | `box-shadow` |
| 並排欄位 | `display:flex`、`flex:1`、`gap` |

## 配色 (深色主題)

| 用途 | 色碼 |
|---|---|
| 外框底色 | `#0b0f19` |
| 卡片底色 | `#111827` |
| 卡片邊框 | `#1e293b` |
| 主色 (藍) | `#38bdf8` |
| 強調 (綠) | `#34d399` |
| 標籤 (黃) | `#fbbf24` |
| 副文字 (灰) | `#94a3b8` |
| 註腳 (深灰) | `#64748b` |

## 元件

### 外框

```html
<div style="background-color:#0b0f19;border:2px solid #38bdf8;border-radius:12px;padding:20px;color:#ffffff;font-family:'Segoe UI', Arial, sans-serif;max-width:620px;margin:0 auto;">
  ...
</div>
```

### 膠囊標籤

```html
<span style="background-color:#38bdf8;color:#0b0f19;font-size:10px;font-weight:800;padding:3px 12px;border-radius:20px;letter-spacing:1.5px;text-transform:uppercase;">Exclusive</span>
```

### 標題 + 副標題

```html
<h1 style="color:#38bdf8;font-size:24px;margin:8px 0 2px 0;text-transform:uppercase;letter-spacing:1.5px;line-height:1.2;">Title</h1>
<div style="color:#94a3b8;font-size:13px;">Subtitle</div>
```

### 數字卡片

```html
<div style="background-color:#111827;border:1px solid #1e293b;border-radius:8px;padding:14px;margin-bottom:12px;text-align:center;">
  <div style="color:#fbbf24;font-size:12px;font-weight:bold;text-transform:uppercase;letter-spacing:1px;">🔥 Label</div>
  <div style="color:#34d399;font-size:22px;font-weight:800;">Big Number</div>
</div>
```

### 左側色條區塊

```html
<div style="border-left:4px solid #38bdf8;background-color:#111827;padding:12px;margin-bottom:12px;border-radius:0 8px 8px 0;">
  <div style="color:#38bdf8;font-weight:bold;margin-bottom:6px;">📋 Section</div>
  <div style="font-size:13px;">• Item: <span style="color:#34d399;font-weight:bold;">value</span></div>
</div>
```

### 行內高亮

```html
<span style="background-color:#38bdf8;color:#0b0f19;padding:1px 6px;border-radius:4px;">highlight</span>
```

### 虛線 CTA

```html
<div style="border:1px dashed #475569;border-radius:8px;padding:12px;text-align:center;">
  <div style="color:#fbbf24;font-weight:bold;">📩 Send me a message</div>
  <div style="color:#64748b;font-size:11px;">First come, first served</div>
</div>
```

### 漸層橫條

```html
<div style="background:linear-gradient(90deg,#38bdf8,#a855f7);padding:10px;border-radius:8px;text-align:center;font-weight:bold;">Gradient Banner</div>
```

### 發光框

```html
<div style="box-shadow:0 0 12px #38bdf8;padding:10px;border-radius:8px;text-align:center;">Glow Box</div>
```

### 兩欄並排

```html
<div style="display:flex;gap:8px;">
  <div style="flex:1;background-color:#1e293b;padding:8px;text-align:center;">Left</div>
  <div style="flex:1;background-color:#334155;padding:8px;text-align:center;">Right</div>
</div>
```

## 完整範本 (Train 販售廣告)

替換 `[...]` 內的文字後直接貼到 Source Code。

```html
<div style="background-color:#0b0f19;border:2px solid #38bdf8;border-radius:12px;padding:20px;color:#ffffff;font-family:'Segoe UI', Arial, sans-serif;max-width:620px;margin:0 auto;">
  <div style="text-align:center;margin-bottom:16px;">
    <span style="background-color:#38bdf8;color:#0b0f19;font-size:10px;font-weight:800;padding:3px 12px;border-radius:20px;letter-spacing:1.5px;text-transform:uppercase;">[Badge]</span>
    <h1 style="color:#38bdf8;font-size:24px;margin:8px 0 2px 0;text-transform:uppercase;letter-spacing:1.5px;line-height:1.2;">[Company] Trains For Sale</h1>
    <div style="color:#94a3b8;font-size:13px;">[One-line pitch]</div>
  </div>

  <div style="display:flex;gap:8px;margin-bottom:12px;">
    <div style="flex:1;background-color:#111827;border:1px solid #1e293b;border-radius:8px;padding:12px;text-align:center;">
      <div style="color:#fbbf24;font-size:11px;font-weight:bold;text-transform:uppercase;">Price</div>
      <div style="color:#34d399;font-size:20px;font-weight:800;">[$xxxk / train]</div>
    </div>
    <div style="flex:1;background-color:#111827;border:1px solid #1e293b;border-radius:8px;padding:12px;text-align:center;">
      <div style="color:#fbbf24;font-size:11px;font-weight:bold;text-transform:uppercase;">Daily</div>
      <div style="color:#34d399;font-size:20px;font-weight:800;">[N trains]</div>
    </div>
  </div>

  <div style="border-left:4px solid #38bdf8;background-color:#111827;padding:12px;margin-bottom:12px;border-radius:0 8px 8px 0;">
    <div style="color:#38bdf8;font-weight:bold;margin-bottom:6px;">📋 Details</div>
    <div style="font-size:13px;">• Duration: [xx days]</div>
    <div style="font-size:13px;">• Payment: <span style="background-color:#38bdf8;color:#0b0f19;padding:1px 6px;border-radius:4px;">[terms]</span></div>
    <div style="font-size:13px;">• Requirements: [none]</div>
  </div>

  <div style="border:1px dashed #475569;border-radius:8px;padding:12px;text-align:center;">
    <div style="color:#fbbf24;font-weight:bold;">📩 Send a message to apply</div>
    <div style="color:#64748b;font-size:11px;">[Limited slots]</div>
  </div>
</div>
```

## Sources

- https://www.torn.com/forums.php#/p=threads&f=46&t=16051765&b=0&a=0&start=29080&to=27946100
