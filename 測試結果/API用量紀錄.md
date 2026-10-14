# 雲端 API 用量紀錄

- 日期：2026-10-14
- 呼叫方式：OpenRouter Chat Completions (`api_runner/run_openrouter.py`)
- Prompt 版本：prompt_API.txt (附件依呼叫端說明的順序傳送，每個附件前加檔名標籤)
- 參數：`reasoning.effort = medium`、`max_tokens = 32000`；作文題以原生 PDF 傳送 (file-parser engine: native)
- 原始逐筆紀錄：`API用量紀錄.jsonl`；每題完整回應：`<模型>/<題名>/response.json`

## 逐題紀錄

| 模型 | 題目 | 輸入 tokens | 輸出 tokens | 其中思考 | 耗時 (秒) | 費用 (USD) |
|---|---|---:|---:|---:|---:|---:|
| Gemini 4 Argon | CG 明信片設計 | 6,388 | 7,795 | 0 | 78.0 | 0.0907 |
| Gemini 4 Argon | email 書寫 | 2,801 | 2,226 | 0 | 39.2 | 0.0279 |
| Gemini 4 Argon | 作文書寫 | 3,417 | 900 | 0 | 71.0 | 0.0158 |
| Gemini 4 Argon | 數學計算 excel 表配平 | 6,492 | 9,103 | 0 | 110.3 | 0.1040 |
| Gemini 4 Argon | 時事熱點銳評 | 10,378 | 3,370 | 0 | 67.2 | 0.0545 |
| Muse Wonder | CG 明信片設計 | 3,814 | 4,907 | 1,094 | 51.2 | 0.1134 |
| Muse Wonder | email 書寫 | 4,710 | 4,245 | 1,707 | 71.0 | 0.1037 |
| Muse Wonder | 作文書寫 | 9,605 | 2,419 | 1,513 | 42.6 | 0.0868 |
| Muse Wonder | 數學計算 excel 表配平 | 9,317 | 17,633 | 14,304 | 207.9 | 0.3899 |
| Muse Wonder | 時事熱點銳評 | 9,509 | 2,695 | 888 | 47.7 | 0.0919 |
| GPT-6.1 Sol | CG 明信片設計 | 3,650 | 3,992 | 516 | 75.1 | 0.0490 |
| GPT-6.1 Sol | email 書寫 | 4,670 | 2,621 | 88 | 58.6 | 0.0379 |
| GPT-6.1 Sol | 作文書寫 | 6,631 | 1,187 | 115 | 36.0 | 0.0284 |
| GPT-6.1 Sol | 數學計算 excel 表配平 | 9,201 | 10,030 | 4,937 | 216.7 | 0.1233 |
| GPT-6.1 Sol | 時事熱點銳評 | 10,619 | 1,900 | 84 | 45.3 | 0.0455 |
| Sonnet 5.5 (API) | CG 明信片設計 | 4,341 | 5,327 | 0 | 37.0 | 0.0620 |

## 小計

| 模型 | 輸入 tokens | 輸出 tokens | 耗時 (秒) | 費用 (USD) |
|---|---:|---:|---:|---:|
| Gemini 4 Argon | 29,476 | 23,394 | 365.7 | 0.2929 |
| Muse Wonder | 36,955 | 31,899 | 420.4 | 0.7858 |
| GPT-6.1 Sol | 34,771 | 19,730 | 431.7 | 0.2842 |
| Sonnet 5.5 (API，僅 CG 題) | 4,341 | 5,327 | 37.0 | 0.0620 |
| 合計 | 105,543 | 80,350 | 1,254.8 | 1.4249 |

## 備註

- 費用取自 OpenRouter 每次回應附的 `usage.cost`。
- Gemini 4 Argon 回報的思考 tokens 全部為 0，但回應中帶有一段加密的 reasoning_details，可能有思考但沒有分開計數，無法確認 medium 設定是否生效。
- Muse Wonder 由 Meta 自家供應，模型標示為 is_moderated (有內容審查)，這次五題都正常完成，沒有被擋。
- 同一張圖片在兩家的輸入 token 計算方式不同 (例如作文 PDF：Gemini 3,417、Muse 9,605)，輸入 tokens 不宜直接橫向比較。
- 測完後 key 的剩餘額度查詢值為 US$4.40 (每月上限 US$5)。這比逐筆費用加總推算的值高，推測是額度統計有延遲。
- 第二輪 (GPT-6.1 Sol 五題、Sonnet 5.5 API 的 CG 題) 送出前查詢剩餘 US$3.92，跑完後為 US$3.68。
- Sonnet 5.5 (API) 回報的思考 tokens 為 0，和 Gemini 4 Argon 一樣無法確認 medium 是否生效；GPT-6.1 Sol 有正常回報。
- `sonnet-5.5` 資料夾是 Claude Code 子代理的結果，`sonnet-5.5_API` 才是這裡的 API 呼叫結果。
