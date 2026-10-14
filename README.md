# 四模型五題橫評 (2026-10-14)

> **本測試為 Oneshot 式測試**：每個模型每一題只作答一次，送出 prompt 後直接收下第一份輸出，中途沒有追問、提示、修正或重跑，也沒有挑選較好的一次。結果反映的是「一次到位」的表現，同一模型多跑幾次可能得到不同答案。

同一組五道實務題 (CG 明信片設計、email 書寫、學測作文、經費配平、時事評論)，分別交給四個模型作答，再比較作答品質、事實正確性與成本。

| 模型 | 呼叫管道 | Prompt 版本 | 可用工具 |
|---|---|---|---|
| Claude Opus 5.5 | Claude Code 子代理 | `prompt_App.txt` | 讀檔、上網、執行程式 |
| Claude Sonnet 5.5 | Claude Code 子代理 | `prompt_App.txt` | 讀檔、上網、執行程式 (PDF 無法轉圖，作文題改用文字擷取) |
| Gemini 4 Argon | OpenRouter API | `prompt_API.txt` | 無 |
| Muse Wonder | OpenRouter API | `prompt_API.txt` | 無 |

思考強度一律設為 medium。數字以程式重算，事實對照新聞原文。

## 總結

| 題目 | Opus 5.5 | Sonnet 5.5 | Gemini 4 Argon | Muse Wonder |
|---|---|---|---|---|
| 數學配平 | 優 | 待定 | 弱 | 優 |
| email 書寫 | 優 | 可 | 可 | 良 |
| CG 明信片 | 優 | 良 | 優 | 可 |
| 學測作文 | 優 | 良 | 良 | 優 |
| 時事銳評 | 良 | 良 | 可 | 優 |

- 標籤是同一題內的相對評價，不同題之間不可直接比較。
- Claude 兩個模型可以上網和執行程式，API 兩個模型不行，解讀時請把這點算進去。
- 各題的詳細評語、字數實算、成本比較，請看 [`測試結果/比較報告/index.html`](測試結果/比較報告/index.html) (GitHub 不會直接顯示 HTML 網頁，請下載整個倉庫後用瀏覽器開啟)。

## 資料夾結構

```
測試題目/                     五道題的 prompt 與附件
  <題名>/prompt_App.txt        給 Claude Code 子代理的版本
  <題名>/prompt_API.txt        給 OpenRouter API 的版本 (含呼叫端說明)
測試結果/
  opus-5.5/<題名>/             各模型的作答 (answer.md，明信片題另有 HTML 與截圖)
  sonnet-5.5/<題名>/
  gemini-4-argon/<題名>/       API 模型另附完整回應 response.json
  muse-wonder/<題名>/          Muse 另附思考過程 reasoning.md
  比較報告/index.html          四模型橫評報告
  API用量紀錄.md / .jsonl      OpenRouter 逐筆 tokens、耗時與費用
  子代理token用量.md           Claude Code 子代理的 tokens 與耗時
```

## 資料說明

- 時事題的三篇新聞全文版權屬於原媒體，倉庫只放連結，見 [`測試題目/時事熱點銳評/新聞來源.md`](測試題目/時事熱點銳評/新聞來源.md)。
- 經費配平題的表格截圖已遮蔽人名。上傳時另將三個計畫的名稱改為計畫A、B、C (含 prompt、截圖檔名、四個模型的作答與比較報告)，截圖上的手寫計畫標題也已打碼；模型作答時看到的是原始名稱。
- 明信片題使用的遊戲 CG 與 Logo 版權屬於《明日方舟》(鷹角網路)，僅作模型測試用途。
- 作文題試卷為 115 學年度學測國文寫作試題。
