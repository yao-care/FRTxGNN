# FRTxGNN - Claude CLI 使用指引

本 repo 的維運以母 repo（yao-care/txgnn）CLAUDE.md 為準；本檔只記本站自己的機制。

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」兩節）與 UsTxGNN（第一個試做站）。
本站的規則與程式都在本 repo，頁面上的查核框與查核紀錄表用法文，依據是 BDPM（Base de données publique des médicaments）；在地字樣集中在 `src/frtxgnn/regulatory/site_config.py`。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、免責聲明前的查核紀錄表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/frtxgnn/regulatory/page_format.py` | 頁首＝Quick Overview 等級格的**第一個**等級（主預測）；這是本站產線原本的行為（2026-11-12 實測，見 site_config 的 HEADER_RULE_NOTE），不照 Tw 整格取最高。頁首 N/A 且沒有預測的頁不重算 |
| 撤回預測 | `src/frtxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `snapshots/fr_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/frtxgnn/regulatory/licenses.py` | 本站沒有程式產生的許可證表；gate 依快照驗市場段落表格的號碼屬於本藥、狀態列與張數列＝事實層、表格列狀態不跟事實相反 |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依 git 前後版本（或改寫前後目錄）把正文刪改轉成 correct 紀錄；site_config 的 COMMITS／REGEN_COMMITS 是 2026-10-31～11-06 的刪改與 AI 重產提交 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證，只列待查、不改頁面 |
| gate | `scripts/check_seo_docs.py` 第 17–20 項 | 紀錄都已套用、許可證＝快照、頁首＝主預測等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、每週許可證排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（每週排程會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31～11-06 正文裡跟許可證事實矛盾、直接刪掉的子句，2026-11-12 已用 `scripts/reviews_from_edits.py --git` 轉成 780 筆紀錄（511 頁；
其中 2 筆因報告在 11 月經 AI 重產、原句已不在頁面，標 resolved_by_regeneration）。
另外 2026-11-09 每週排程後 BDPM 有許可轉為註銷、正文仍寫「全部有效」的 5 頁（dalteparin、diosmin、docetaxel、letrozole、molsidomine），2026-11-12 以 5 筆 correct 紀錄（id fr-lic-20261112-*）只刪矛盾子句。
2026-11-12 正文許可證張數／狀態對事實層與證據包的掃描，以 10 筆 `fr-lic-20261112-*` 更正：fluvastatin、povidone、riluzole、ezetimibe（有效張數）、moxonidine（寫全註銷，實為全有效）、travoprost、simoctocog_alfa、finasteride（11-06 刪句後留下「也已註銷」的殘句）、primaquine（寫已無有效 AMM）、panobinostat（下一步的「(AMM annulées)」）。證據包只收前 20 張（partial）的頁在「下一步」寫「(AMM annulées)」的約 15 頁，前 20 張全 active、其餘未收，無法證明錯，未改。
2026-11-15 下載 BDPM 全量（CIS_bdpm、CIS_COMPO_bdpm）依成分代碼重算這批頁：22 頁以 `fr-lic-20261115-*` 更正——dasatinib、levodopa、tacrolimus、ustekinumab 全部 AMM 有效，拿掉「(AMM annulées)」；其餘大多數有效、少數廢止／歸檔，改成「(la plupart des AMM sont actives ; certaines sont abrogées ou archivées)」；entecavir（BARACLUDE 口服液實為有效）、fluconazole（廢止的是懸浮粉劑與膠囊，不是輸注液）、ketoprofen（列的劑型不是廢止的那些）照 BDPM 改寫。histidine、levetiracetam 講「已註銷 AMM」的待辦句確有廢止產品，不改。
2026-11-12 許可證表格列狀態對事實層（母目錄 check_drug_page.py --row-status）：20 列 BDPM「Autorisation active」的號碼格標成「(annulée)／(abrogée)」（拿掉標註）、10 列寫 active 但 BDPM 為「Autorisation archivée／abrogée」（改成原文 archivée／abrogée），以 30 筆 `fr-row-20261112-*` correct 紀錄更正（依證據包原始狀態逐列確認）。

## 新資料查不到的許可證（2026-11-17）

11-16 每週排程列出 40 張「新資料查不到」的 CIS（涵蓋 99.3%，沒開 issue）。2026-11-17 用戶要求確認實際狀態：下載 BDPM 同日全部公開檔逐號比對——
40 張都不在 CIS_bdpm.txt，但全在 CIS_CIP_bdpm.txt（包裝層級，Présentation active、有 Déclaration de commercialisation），BDPM 產品頁
（https://base-donnees-publique.medicaments.gouv.fr/medicament/<CIS>/extrait，「Dernière mise à jour le 03/11/2026」）40 張都寫「Statut de l'autorisation : Valide」，
證據包原本就是 Autorisation active，所以頁面不用改。CIS_bdpm.txt 本身不完整：同日 CIS_CIP 另有 478 個 CIS 不在 CIS_bdpm。
兩份檔與產品頁都沒有的號 0 張。
- `scripts/license_adapter.py`：下載網址改成 https 的 /download/file/<檔名>（舊的 index.php 路徑 301 到 http，雲端環境走不通）；另下載 CIS_CIP_bdpm.txt，
  只在 CIS_CIP 的本站 CIS 逐張讀產品頁，寫 Valide 的收成「Autorisation active」，其他寫法不收（包裝狀態不等於 AMM 狀態：兩份都有的 CIS 裡 593 個
  Autorisation abrogée 仍有 Présentation active，所以不拿包裝狀態推定）。兩份檔都沒有、產品頁 404 的本站 CIS 由 preprocess 標
  `license_status: cancelled`＋`bdpm_not_listed`（第一次發現日；BDPM 連 abrogée／archivée 都收，整個不收＝已不是現行許可），又出現就取消；
  任一份檔下載失敗、兩份合計少於 15,000 個 CIS、或產品頁讀不到時不判定。`confirmed_absent()` 讓排程把這些列成「主管機關現行清單確認已不列」，不算「查不到」。
- 2026-11-17 排程：新資料涵蓋 100%（5,820 張），狀態變動 0、改頁 0。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。
