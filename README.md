# 輕旗艦模型測試結果

| 模型 | 出廠時間 (OpenRouter 上架日) | 測試時間 | 輪次 |
|---|---|---|---|
| Claude Opus 5.5 | 2026-09-23 | 2026-10-14 | 第一輪 |
| Claude Sonnet 5.5 | 2026-09-29 | 2026-10-14 | 第一輪 (API 補測 CG 題為第二輪) |
| GPT-6.1 Sol | 2026-09-30 | 2026-10-14 | 第二輪 |
| Muse Wonder | 2026-10-12 | 2026-10-14 | 第一輪 |
| Gemini 4 Argon | 2026-10-14 | 2026-10-14 | 第一輪 |
| Gemini 4 Carbon | 2026-11-11 | 2026-11-12 | 第三輪追評 |
| GPT-6.2 Sol | 2026-11-18 | 2026-11-19 | 第四輪追評 |
| Gemini 4 Neon | 2026-11-18 | 2026-11-19 | 第四輪追評 |

出廠時間取 OpenRouter 模型目錄的上架日 (GMT+8)，可能比官方發表晚一兩天；測試時間為送出 prompt 的日期。

> **本測試為 Oneshot 式測試**：每個模型每一題只作答一次，送出 prompt 後直接收下第一份輸出，中途沒有追問、提示、修正或重跑，也沒有挑選較好的一次。結果反映的是「一次到位」的表現，同一模型多跑幾次可能得到不同答案。唯一例外是 Gemini 4 Carbon 的數學題：第一次在 16,000 tokens 的輸出上限處被截斷，prompt 不變、上限調高到 32,000 後重跑一次，截斷版一併保留在 `answer_16k截斷.md`。Gemini 4 Neon 的數學題在 32,000 tokens 上限處截斷 (思考就用掉 31,398 tokens)，依 Oneshot 原則不重跑，只保留截斷版 `answer_32k截斷.md`。

同一組五道實務題 (CG 明信片設計、email 書寫、學測作文、經費配平、時事評論)，分別交給八個模型作答，再比較作答品質、事實正確性與成本。

**線上瀏覽：** [展示頁](https://ag-0814.github.io/261014_LLM-Oneshot-Test/) (每個模型每一題的作答、思考過程、原始回應、明信片都可直接點開) · [AI 盲評報告](https://ag-0814.github.io/261014_LLM-Oneshot-Test/viewer.html?f=%E6%B8%AC%E8%A9%A6%E7%B5%90%E6%9E%9C/%E6%AF%94%E8%BC%83%E5%A0%B1%E5%91%8A/AI%E7%9B%B2%E8%A9%95%E5%A0%B1%E5%91%8A_Gemini4Neon.md) (Gemini 4 Neon 匿名評分) · [參考：Claude 評分與成本比較](https://ag-0814.github.io/261014_LLM-Oneshot-Test/%E6%B8%AC%E8%A9%A6%E7%B5%90%E6%9E%9C/%E6%AF%94%E8%BC%83%E5%A0%B1%E5%91%8A/%E5%8F%83%E8%80%83_Claude%E8%A9%95%E5%88%86/index.html)

| 模型 | 呼叫管道 | Prompt 版本 | 可用工具 |
|---|---|---|---|
| Claude Opus 5.5 | Claude Code 子代理 | `prompt_App.txt` | 讀檔、上網、執行程式 |
| Claude Sonnet 5.5 | Claude Code 子代理 | `prompt_App.txt` | 讀檔、上網、執行程式 (PDF 無法轉圖，作文題改用文字擷取) |
| Gemini 4 Argon | OpenRouter API | `prompt_API.txt` | 無 |
| Muse Wonder | OpenRouter API | `prompt_API.txt` | 無 |
| GPT-6.1 Sol | OpenRouter API | `prompt_API.txt` | 無 (第二輪補測) |
| Gemini 4 Carbon | OpenRouter API | `prompt_API.txt` | 無 (第三輪追評，2026-11-12) |
| GPT-6.2 Sol | OpenRouter API | `prompt_API.txt` | 無 (第四輪追評，2026-11-19) |
| Gemini 4 Neon | OpenRouter API | `prompt_API.txt` | 無 (第四輪追評，2026-11-19) |

思考強度一律設為 medium。另外補測了 Sonnet 5.5 走 OpenRouter API 的 CG 明信片題 (`sonnet-5.5_API`)，以及朋友代測的 Gemini 4 Argon App 版 CG 明信片題 (未上傳)，兩者都未列入總結表。數學題的客觀對照見 [`測試結果/數學計算excel表配平/README.md`](測試結果/數學計算excel表配平/README.md)。

## AI 評分總結 (Gemini 4 Neon 匿名盲評)

AI 評分交給 Gemini 4 Neon，評分時模型名稱全部換成 `ModelA` 至 `ModelJ`，評分者不知道哪份作答出自哪個模型 (包含它自己的作答)。每題 100 分制，評分者另以程式驗算數學題、實算字數。完整評語見 [`測試結果/比較報告/AI盲評報告_Gemini4Neon.md`](測試結果/比較報告/AI盲評報告_Gemini4Neon.md)。

| 題目 | Opus 5.5 | Sonnet 5.5 | Gemini 4 Argon | Muse Wonder | GPT-6.1 Sol | Gemini 4 Carbon | GPT-6.2 Sol | Gemini 4 Neon |
|---|---|---|---|---|---|---|---|---|
| CG 明信片 | **94** · #1 | 75 · #8 | 80 · #6 | 65 · #9 | 82 · #5 | 88 · #4 | 78 · #7 | 91 · #2 |
| email 書寫 | **97** · #1 | 77 · #7 | 72 · #8 | 85 · #4 | 83 · #5 | 81 · #6 | 87 · #3 | 92 · #2 |
| 學測作文 | 82 · #4 | 72 · #8 | 74 · #7 | 80 · #5 | 91 · #2 | 77 · #6 | **96** · #1 | 86 · #3 |
| 時事銳評 | **93** · #1 | 78 · #7 | 68 · #8 | 87 · #4 | 90 · #2 | 81 · #6 | 84 · #5 | 89 · #3 |
| 數學配平 | **98** · #1 | 96 · #2 | 68 · #7 | 92 · #4 | 89 · #5 | 76 · #6 | 93 · #3 | 15 · #8 |
| **五題均分** | **92.8** | 79.6 | 72.4 | 81.8 | 87.0 | 80.6 | 87.6 | 74.6 (四題均 89.5) |

- 格式為「分數 · 該題名次」。CG 題的名次把兩份補測也排進去 (Argon App 版 90 分第 3、Sonnet API 版 52 分第 10)，所以會跳號。
- Gemini 4 Neon 的數學題在 32k tokens 截斷、沒有交出方案，只拿 15 分；其餘四題均分 89.5，是 API 組最高。
- Claude 兩個模型可以上網和執行程式，API 呼叫的模型不行，解讀時請把這點算進去。
- 先前由 Claude 撰寫的評分 (優、良、可、弱四級，含成本比較) 保留在 [`測試結果/比較報告/參考_Claude評分/index.html`](測試結果/比較報告/參考_Claude評分/index.html) 作為參考。Claude 評分時知道模型名稱，而且自己也是受測者，所以主要評分改用匿名盲評。

## 人類排序 vs AI 評分

人類排序來自評審的主觀閱讀 ([評價全文](測試結果/比較報告/用戶主觀橫評.md))，AI 名次來自上方的匿名盲評。名次相同表示並列，兩者都只在同一題內比較。

| 題目 | Opus 5.5 | Sonnet 5.5 | Gemini 4 Argon | Muse Wonder | GPT-6.1 Sol | Gemini 4 Carbon | GPT-6.2 Sol | Gemini 4 Neon |
|---|---|---|---|---|---|---|---|---|
| CG 明信片 | **#1** · #1 | #2 · #8 | #6 · #6 | #10 · #9 | #4 · #5 | #6 · #4 | #4 · #7 | #3 · #2 |
| email 書寫 | #3 · #1 | #8 · #7 | #2 · #8 | #5 · #4 | #6 · #5 | **#1** · #6 | #7 · #3 | #3 · #2 |
| 學測作文 | **#1** · #4 | **#1** · #8 | #7 · #7 | #4 · #5 | #6 · #2 | #4 · #6 | #3 · #1 | #7 · #3 |
| 時事銳評 | #4 · #1 | #7 · #7 | **#1** · #8 | #4 · #4 | #8 · #2 | **#1** · #6 | #4 · #5 | #3 · #3 |
| 數學配平 | 未評 · #1 | 未評 · #2 | 未評 · #7 | 未評 · #4 | 未評 · #5 | 未評 · #6 | 未評 · #3 | 未評 · #8 |

格式為「人類名次 · AI 名次」。人類排序原文 (`>` 越多代表差距越大)：

| 題目 | 人類排序 |
|---|---|
| CG 明信片 | O5.5 > So5.5 >> G4N >> Sol6.1 = Sol6.2 > G4C = G4A = G4A_APP = So5.5_API > Mu2 |
| email 書寫 | G4C > G4A > O5.5 = G4N >>> Mu2 > Sol6.1 > Sol6.2 > So5.5 |
| 學測作文 | O5.5 = So5.5 > Sol6.2 > Mu2 = G4C >> Sol6.1 > G4A = G4N |
| 時事銳評 | G4A = G4C >> G4N > Mu2 = Sol6.2 = O5.5 > So5.5 >> Sol6.1 |
| 數學配平 | 未評 (評審表示交給客觀計算；各模型與實際採用配法的對照見 [`測試結果/數學計算excel表配平/README.md`](測試結果/數學計算excel表配平/README.md)) |

代稱：O5.5 = Opus 5.5、So5.5 = Sonnet 5.5、G4A = Gemini 4 Argon、G4A_APP = Gemini 4 Argon App 版補測、Mu2 = Muse Wonder、Sol6.1 = GPT-6.1 Sol、Sol6.2 = GPT-6.2 Sol、G4C = Gemini 4 Carbon、G4N = Gemini 4 Neon、So5.5_API = Sonnet 5.5 走 API 的補測。

對照下來的幾個差異：

- **一致的地方**：明信片題的 Opus 5.5 兩邊都第一，Gemini 4 Neon 也都在前三 (人類 #3、AI #2)；GPT-6.2 Sol 的作文兩邊都在前三。
- **分歧最大的是 Gemini 4 Argon 與 Carbon**：email 與時事兩題人類都排第一或第二，AI 卻排在後段 (Argon 兩題都 #8)。AI 扣的是編造價格、篇幅超出一倍、判斷過度肯定；人類看重的是方案實用、文章有說服力。
- **Claude 兩個模型的作文**：人類並列第一，AI 只給 #4 與 #8，理由是選材落入「半夜倒水、溫牛奶」等常見模板。
- **GPT-6.1 Sol 的時事銳評**：AI 給 #2 (思辨扎實、不帶風向)，人類排最後，嫌它是防禦型寫作、觀點模糊。
- **Gemini 4 Neon 的作文**：AI 給 #3，人類排最後並列，嫌文字太華麗、情節不真實。這份是評分者自己的作答，雖然是盲評，解讀時仍可留意。

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
  gpt-6.1-sol/<題名>/          第二輪補測，部分題目附 reasoning.md
  sonnet-5.5_API/CG圖明信片設計/  Sonnet 5.5 走 API 的補測 (僅 CG 題)
  gemini-4-carbon/<題名>/      第三輪追評；數學題另附 16k 截斷版 answer_16k截斷.md
  gpt-6.2-sol/<題名>/          第四輪追評 (2026-11-19)
  gemini-4-neon/<題名>/        第四輪追評 (2026-11-19)；數學題 32k 截斷，只有 answer_32k截斷.md
  數學計算excel表配平/README.md  數學題：各模型主方案與實際採用配法的對照
  比較報告/AI盲評報告_Gemini4Neon.md  Gemini 4 Neon 匿名盲評 (主要 AI 評分)
  比較報告/參考_Claude評分/     Claude 撰寫的評分與成本比較 (參考，第一至四輪)
  比較報告/用戶主觀橫評.md      人類主觀評價全文
  API用量紀錄.md / .jsonl      OpenRouter 逐筆 tokens、耗時與費用
  子代理token用量.md           Claude Code 子代理的 tokens 與耗時
```

## 資料說明

- 時事題的三篇新聞全文版權屬於原媒體，倉庫只放連結，見 [`測試題目/時事熱點銳評/新聞來源.md`](測試題目/時事熱點銳評/新聞來源.md)。
- 經費配平題的表格截圖已遮蔽人名。上傳時另將三個計畫的名稱改為計畫A、B、C (含 prompt、截圖檔名、各模型的作答與兩份 AI 評分報告)，截圖上的手寫計畫標題也已打碼；模型作答時看到的是原始名稱。
- 明信片題使用的遊戲 CG 與 Logo 版權屬於《明日方舟》(鷹角網路)，僅作模型測試用途。
- 作文題試卷為 115 學年度學測國文寫作試題。

## 授權

本倉庫以 [MIT License](LICENSE) 授權，範圍限於作者自行撰寫的內容 (prompt、比較報告、README、用量紀錄) 與模型產出。上方「資料說明」列出的第三方素材 (遊戲 CG 與 Logo、學測試卷、新聞) 版權仍屬原權利人，不在 MIT 授權範圍內。
