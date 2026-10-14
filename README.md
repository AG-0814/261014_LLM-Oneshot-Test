# 五模型五題橫評 (2026-10-14)

> **本測試為 Oneshot 式測試**：每個模型每一題只作答一次，送出 prompt 後直接收下第一份輸出，中途沒有追問、提示、修正或重跑，也沒有挑選較好的一次。結果反映的是「一次到位」的表現，同一模型多跑幾次可能得到不同答案。

同一組五道實務題 (CG 明信片設計、email 書寫、學測作文、經費配平、時事評論)，分別交給五個模型作答，再比較作答品質、事實正確性與成本。

**線上瀏覽：** [展示頁](https://ag-0814.github.io/261014_LLM-Oneshot-Test/) (每個模型每一題的作答、思考過程、原始回應、明信片都可直接點開) · [AI 比較報告](https://ag-0814.github.io/261014_LLM-Oneshot-Test/%E6%B8%AC%E8%A9%A6%E7%B5%90%E6%9E%9C/%E6%AF%94%E8%BC%83%E5%A0%B1%E5%91%8A/index.html)

| 模型 | 呼叫管道 | Prompt 版本 | 可用工具 |
|---|---|---|---|
| Claude Opus 5.5 | Claude Code 子代理 | `prompt_App.txt` | 讀檔、上網、執行程式 |
| Claude Sonnet 5.5 | Claude Code 子代理 | `prompt_App.txt` | 讀檔、上網、執行程式 (PDF 無法轉圖，作文題改用文字擷取) |
| Gemini 4 Argon | OpenRouter API | `prompt_API.txt` | 無 |
| Muse Wonder | OpenRouter API | `prompt_API.txt` | 無 |
| GPT-6.1 Sol | OpenRouter API | `prompt_API.txt` | 無 (第二輪補測) |

思考強度一律設為 medium。數字以程式重算，事實對照新聞原文。另外補測了 Sonnet 5.5 走 OpenRouter API 的 CG 明信片題 (`sonnet-5.5_API`)，未列入總結表。

## 總結

| 題目 | Opus 5.5 | Sonnet 5.5 | Gemini 4 Argon | Muse Wonder | GPT-6.1 Sol |
|---|---|---|---|---|---|
| 數學配平 | 優 | 待定 | 弱 | 優 | 良 |
| email 書寫 | 優 | 可 | 可 | 良 | 良 |
| CG 明信片 | 優 | 良 | 優 | 可 | 良 |
| 學測作文 | 優 | 良 | 良 | 優 | 優 |
| 時事銳評 | 良 | 良 | 可 | 優 | 良 |

- 標籤是同一題內的相對評價，不同題之間不可直接比較。
- Claude 兩個模型可以上網和執行程式，API 三個模型不行，解讀時請把這點算進去。
- 各題的詳細評語、字數實算、成本比較，請看 [`測試結果/比較報告/index.html`](測試結果/比較報告/index.html) (線上版見上方「AI 比較報告」連結)。

## 人類排序 vs AI 評分

AI 評分來自上方比較報告；人類排序來自評審的主觀閱讀 ([評價全文](測試結果/比較報告/用戶主觀橫評.md))。名次相同表示並列，兩者都只在同一題內比較。

| 題目 | Opus 5.5 | Sonnet 5.5 | Gemini 4 Argon | Muse Wonder | GPT-6.1 Sol |
|---|---|---|---|---|---|
| CG 明信片 | **#1** · 優 | #2 · 良 | #4 · 優 | #6 · 可 | #3 · 良 |
| email 書寫 | #2 · 優 | #5 · 可 | **#1** · 可 | #3 · 良 | #4 · 良 |
| 學測作文 | **#1** · 優 | **#1** · 良 | #5 · 良 | #3 · 優 | #4 · 優 |
| 時事銳評 | #2 · 良 | #4 · 良 | **#1** · 可 | #2 · 優 | #5 · 良 |
| 數學配平 | 未評 · 優 | 未評 · 待定 | 未評 · 弱 | 未評 · 優 | 未評 · 良 |

格式為「人類名次 · AI 評分」。人類排序原文 (`>` 越多代表差距越大)：

| 題目 | 人類排序 |
|---|---|
| CG 明信片 | O5.5 > So5.5 >> Sol6.1 > G4A = So5.5_API > Mu2 |
| email 書寫 | G4A > O5.5 >>>> Mu2 > Sol6.1 > So5.5 |
| 學測作文 | O5.5 = So5.5 > Mu2 >> Sol6.1 > G4A |
| 時事銳評 | G4A >>> Mu2 = O5.5 > So5.5 >> Sol6.1 |
| 數學配平 | 未評 (評審表示交給客觀計算，以比較報告為準) |

代稱：O5.5 = Opus 5.5、So5.5 = Sonnet 5.5、G4A = Gemini 4 Argon、Mu2 = Muse Wonder、Sol6.1 = GPT-6.1 Sol、So5.5_API = Sonnet 5.5 走 API 的補測。

對照下來的幾個差異：

- **一致的地方**：Opus 5.5 在明信片與作文兩邊都拿第一；Sonnet 5.5 的 email 兩邊都墊底 (注音錯誤、措辭不妥)。
- **分歧最大的是 Gemini 4 Argon**：email 與時事兩題人類都排第一，AI 評分卻是五者最低的「可」。AI 評分扣的是過度肯定與篇幅超出一倍，人類看重的是方案實用、文章有說服力。
- **GPT-6.1 Sol 的作文**：AI 因選材獨特給「優」，人類嫌文字平板、換行過多，排第四。
- **明信片題的 Gemini 4 Argon**：AI 評「優」(版面元素最完整)，人類排第四，理由正是元素堆太滿、不做取捨。

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
  比較報告/index.html          五模型橫評報告
  比較報告/用戶主觀橫評.md      人類主觀評價全文
  API用量紀錄.md / .jsonl      OpenRouter 逐筆 tokens、耗時與費用
  子代理token用量.md           Claude Code 子代理的 tokens 與耗時
```

## 資料說明

- 時事題的三篇新聞全文版權屬於原媒體，倉庫只放連結，見 [`測試題目/時事熱點銳評/新聞來源.md`](測試題目/時事熱點銳評/新聞來源.md)。
- 經費配平題的表格截圖已遮蔽人名。上傳時另將三個計畫的名稱改為計畫A、B、C (含 prompt、截圖檔名、各模型的作答與比較報告)，截圖上的手寫計畫標題也已打碼；模型作答時看到的是原始名稱。
- 明信片題使用的遊戲 CG 與 Logo 版權屬於《明日方舟》(鷹角網路)，僅作模型測試用途。
- 作文題試卷為 115 學年度學測國文寫作試題。

## 授權

本倉庫以 [MIT License](LICENSE) 授權，範圍限於作者自行撰寫的內容 (prompt、比較報告、README、用量紀錄) 與模型產出。上方「資料說明」列出的第三方素材 (遊戲 CG 與 Logo、學測試卷、新聞) 版權仍屬原權利人，不在 MIT 授權範圍內。
