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
| 許可證 | `scripts/sync_license_tables.py`（程式表前後有 `<!-- licenses:begin/end -->`，2026-11-24 起）、`snapshots/fr_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/frtxgnn/regulatory/licenses.py` | 快照存事實層、本藥號碼、程式表列；gate 依快照驗程式區塊、號碼屬於本藥、狀態列與張數列＝事實層、表格列狀態不跟事實相反 |
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
- 2026-11-24（用戶決定，反覆跳動防呆，見母 repo CLAUDE.md）：`verify(cis)` 讀 BDPM 產品頁的「Statut de l'autorisation」並換成 CIS_bdpm 的寫法（Valide→Autorisation active、Archivée→Autorisation archivée…）；排程遇到 28 天內翻回去的狀態變更時，產品頁確認新狀態才寫回，否則保留現狀、開 issue（11-13 那次的 10 張依產品頁都會擋下）。
- 2026-11-17 排程：新資料涵蓋 100%（5,820 張），狀態變動 0、改頁 0。

## 依 BDPM 物質代碼補收同成分 AMM（2026-11-24）

用戶 2026-11-24 決定「依成分補進證據包」「全站但排除離子類」：raloxifene、quinapril 的證據包只收到已廢止的舊 AMM，BDPM 另有現行 AMM。原因是 collectors/frfda.py 依 data/processed/drug_mapping.csv 的成分名對 DrugBank ID，
drug_mapping 只認得「RALOXIFÈNE (CHLORHYDRATE DE)」這種寫法，同一成分寫成「CHLORHYDRATE DE RALOXIFÈNE」（BDPM 物質代碼同為 79270）就收不到；不是新註冊的 AMM。
- `scripts/add_current_amm.py --cis CIS_bdpm.txt --compo CIS_COMPO_bdpm.txt [--dry-run] [--report out.tsv]`：本藥的物質代碼＝證據包既有 CIS 的 SA 列中、成分名跟 drug_mapping 對到本藥 DrugBank ID 的成分名完全相同的列（不去鹽類，避免 FLUORURE DE SODIUM→sodium）；
  現行 CIS_COMPO 有這些代碼、不在證據包的 CIS 照原規則補收（複方照收，只收 CIS_bdpm 有的 CIS，status＝CIS_bdpm 第 5 欄），欄位照 10-31 補入的格式並記 source（物質代碼、檔案日期）與 added；
  records 照原收集器最多 20 筆（單方優先），其餘記在 bdpm_not_stored 並算進 total_matches。只加不刪、可重複執行。
- 不擴充的離子／抗衡離子證據包（EXCLUDE，drug_mapping 本來就把鹽類成分名對到裸離子 DrugBank ID）：sodium（試跑會收 153 張：氯化鈉輸液、DURAPHAT 氟化鈉、fusidate de sodium）、potassium（65 張補鉀劑）、
  calcium（62 張，多是 FOLINATE DE CALCIUM）、zinc（16 張鋅鹽）、aluminium（10 張 MAALOX 等制酸劑）、ammonium（0 張）、magnesium、chloride（本站目前沒有這兩個證據包）。
- 2026-11-24 第一次跑（BDPM 全量檔 2026-11-24）：333 個證據包補 5,237 筆（存進 records 1,101 筆、超過上限只算張數 4,136 筆；其中 182 個證據包有原規則因成分名寫法漏收的 1,365 張，其餘是原規則對得到、只因 20 筆上限沒存的）；
  raloxifene 補 9 張現行（含 EVISTA 67365141）、quinapril 補 QUINAPRIL BIOGARAN 61168571 與 3 張複方。196 頁概覽表狀態列／張數列由程式同步。
- 正文依舊證據包寫的張數與「全部有效／沒有有效 AMM」：checker M3 抓到 61 句，另寫一支更寬的偵測（同句有 AMM／autorisation 字樣、數字不等於事實層總數／有效數／非有效數，或有否定與全稱字樣）全量掃 196 頁，
  再找到 40 句（checker 漏抓的例：verapamil「n'a plus d'AMM valide」、maprotiline「Aucune AMM n'est enregistrée」）；101 句改寫成事實層張數（90 筆新的 `fr-lic-20261124-*`、11 筆 11-06 紀錄同 id 重發，前版存 history；
  rivastigmine 的 11-06 刪句紀錄改錨）。只講表上幾張的句子改成明講「tableau ci-dessus」並補總數；待辦條目（bendamustine「des deux AMM」等）照規則不改。寬偵測複查剩 38 句，都是改寫後張數一致或不是張數句。
  `fr-lic-20261124-raloxifene-1`、`quinapril-1`（同日加的「證據包只收到舊 AMM」加註）撤回。checker 全量 0、gate 通過。
- `.github/workflows/license-refresh.yml` 在 license_refresh 前先跑這支（下載 CIS_bdpm.txt、CIS_COMPO_bdpm.txt），之後成分名寫法漏收或新註冊的同成分 AMM 會自動補進證據包；正文張數若因此矛盾，排程照常擋下該頁、要另寫紀錄。

## 程式產生許可證表、正文張數自動改寫（2026-11-24）

用戶 2026-11-24 決定（30 站「許可證張數與狀態不再每週過期」）：每週排程只改得到概覽表狀態列／張數列，市場段落的 AI 自由格式許可證表（號碼格夾「(annulée)」、適應症欄全是「Non renseignée」）與正文張數句每週過期、checker 擋頁。
- A. `scripts/sync_license_tables.py`：「## Informations de Marché en France」段落的第一張表換成程式依證據包（tfda.records）產生的表
  `| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |`：列＝證據包全部紀錄（最多 20 筆），Active 在前；狀態＝BDPM Statut administratif 原文簡寫（Active／Abrogée／Archivée／Suspendue），
  bdpm_not_listed 的號碼寫「Ne figure plus dans la BDPM」；表後一句來源，證據包只收到部分 AMM 時加「Les données ne contiennent qu'une partie des autorisations ; la liste peut être incomplète.」；沒有紀錄時一句 NONE_LINE。
  2026-11-24 換表 786 頁、段落原本沒有表的 14 頁補表；`--migrate` 時拿掉緊鄰舊表、只講「表上列了幾筆」的句子或子句（CAPTION／CAP_CLAUSE），`--captions` 另掃整個市場段落（39 頁）；
  查核紀錄的更正文字所在的句子不動。錨在舊表列上的 30 筆 `fr-row-20261112-*` 標 `status: superseded`＋`superseded_by`（紀錄保留、頁面不顯示框）。
  快照存 rows／total（build_license_snapshot.py 用 rows_of），gate（licenses.py program_block_problems）驗程式區塊＝重算結果、市場段落不准有非程式表；
  `license_adapter.py` 的 `sync_tables` 讓每週排程對狀態有變的藥重排，`PAGE_NOTE` 放行程式區塊的非表格行；`build_license_snapshot.py` 結尾再全站重排一次（證據包補收、狀態沒變的藥也跟上）；
  `sync_notes_to_docs.py` 整頁重寫時用 `carry_block` 移植舊頁的程式區塊。
- B. `src/frtxgnn/regulatory/count_prose.py`、`scripts/rewrite_license_counts.py`（照 Kr／My 移植，法文句型）：「N AMM valides (sur M)」「N AMM sur M sont valides」「N des M AMM」「Au total, N AMM」「Les N AMM … sont valides」
  依快照事實層改寫；有保留、講表上筆數、相對數、劑型或廠商或單方子集、partial 頁不動；0／1 張（單複數配合）、說全部有效而事實不符的不改、列待查。
  `apply_drug_reviews.py`（非 --check）與 `build_license_snapshot.py` 結尾自動跑；gate 第 22 項擋「再跑一次會變」。2026-11-24 改寫 4 頁 4 句（estriol、lanreotide、micafungin、tretinoin 的「N AMM valides sur N」），判斷不了 1 句（bendamustine 待辦「des deux AMM」）列待查。
- 待查清單另加 55 句仍講舊表筆數的句子（source：程式許可證表取代舊表後…；34 句是查核紀錄的更正文字，例 oxaliplatin「Au total, 10 AMM sont recensées; seules les 5 premières sont listées ici.」，要同 id 重發改寫）。
- 驗證：checker 全量 0（改前 0）、gate exit 0；另寫的寬偵測（同句有 AMM 字樣、數字不在事實層任一讀法或程式表列數）全量掃，剩 31 句：講舊表筆數 21 句（已列待查）、partial 頁的「toutes valides」與前 20 筆一致 5 句、子集拆分張數正確 4 句、待辦 1 句。

## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 768 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour c」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `fr-moa-<日期>-<藥>-1`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：本站語言（français）的出處句＋節錄的忠實翻譯（標明「非官方翻譯」）＋英文原文（照引、為準）＋DailyMed 連結、仿單版本、取用日期（用戶 2026-11-19 決定「當地語言摘要＋英文原文」）。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 翻譯：節錄的翻譯是 AI 輔助的忠實翻譯（不增不減，藥名、基因與受體符號、數字、「[…]」照原文），2026-11-19 批次產生，存在紀錄 sources 的 translation（translation_lang、translation_note 註明非官方、英文原文為準）；頁面上同時列英文原文。`--translations <檔>` 讀翻譯、`--need <檔>` 列出還沒翻的節錄（這些頁那次不寫紀錄，gate 會擋，翻好再跑）。
- 2026-11-19 結果：659 頁寫入紀錄（美國仿單 566、ChEMBL 93），109 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 21 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 注意：節錄的是美國仿單，劑型與適應症可能跟本站市場的產品不同（例如取到外用仿單）；文字上已寫明是美國 FDA 核准仿單。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。
- 2026-11-20 補做：程式更新：同頁不只一句「不可得」時每句各一筆紀錄（-1、-2…）；同頁別筆紀錄的更正文字、錨點與已套上的節錄不再當成「不可得」句；gate 改成公開頁仍寫「不可得」、又沒列待查就擋（不再只看該頁有沒有紀錄）；同頁第二句起補 1 筆紀錄（id 結尾 -2）；ChEMBL 譯文（詞組清單）後補句號 93 筆；同 id 重發，前版 replacement 存 history。
- 2026-11-20 試跑母目錄「交付前驗證」規則時補做：偵測改成原條件不動、另加新增寫法（L2，比中的再用 NOT 排除以缺資料為前提的模型推論），字樣用獨立、更寬的偵測全量掃出的候選句逐句標註校準（A 沒有漏、B 沒有誤中）；同頁重複引用同一段節錄的 1 筆改成指向上方節錄的一句（附同一個來源連結）；以上同 id 重發，前版存 history。程式另加 reorder_src_tail、同頁已引用同一段節錄時改指向上方（產生器 txgnn/.claude/moa_rollout_20261119/fix_20261120/）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 藥物頁 description 句尾在地化（2026-11-19）

用戶 2026-11-19 決定（「藥物頁簡述在地化」，SEO 工具判定 30 站藥物頁近似重複，原因之一是 description 句尾都是同一句「原適應症：本地資料未記載」）：公開藥物頁（排除 noindex、轉址頁）front matter description 句尾的「Indication d'origine : Non renseignée dans les données locales」換成本站許可證快照事實層（`snapshots/*_licenses.json.gz`，經 `src/*/regulatory/licenses.py` 的 snapshot()）的品項數句子，資料名稱照本站口徑：BDPM 的 AMM。藥名、預測新適應症、等級字樣不動（母目錄 sync_description_levels.py 照舊對得到）；已有原適應症原文的頁不動。
例：abatacept「Indication d'origine : Non renseignée dans les données locales」→「En France, AMM dans la BDPM : 5 (valides : 5)」；2026-11-19 改了 432 頁。
由母目錄 `.claude/drug_meta_description.py --apply --site FRTxGNN` 產生（站上複本 `tools/txgnn/.claude/drug_meta_description.py --apply --root .`），改動記在 `docs/_data/description_local_log.json`（pages＝目前句尾與原字樣、entries＝每次改動前後整行，可還原）。快照數字變了重跑會換新數字；`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾會自動 --apply，`check_seo_docs.py` 跑 --check 擋「還是未記載句尾」或「數字跟快照不符」。只改 front matter，lastmod_fix 不算正文改動、last_modified_at 不動。
同日修：`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾重算 local_facts 的 atexit 掛鉤在結束時取不到 `__file__`（NameError，之前其實沒跑成），改成先算好路徑。

## 第二輪：查核紀錄更正文字與說明裡的張數、舊表筆數（2026-11-24）

用戶 2026-11-24 第二輪決定（程式許可證表與正文張數改由程式維護後，查核紀錄裡寫死的張數不會跟著更新）：
- 張數樣板：`site_config.T["figures"]`（`reviews_from_edits.py` 寫紀錄說明時用）改成不寫數字（「Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché.」）；既有說明用這個樣板寫死張數的 709 筆同 id 重發（前版存 history，reason「程式許可證表／正文張數改由程式維護，2026-11-24 用戶決定」）。
- 更正文字（replacement）寫死張數或講舊表筆數（「seules les 5 premières sont listées ici」「Principales AMM (5 sur 19)」「12 AMM sur 14 sont valides」「(7 AMM valides sur 7)」等）的 140 筆同 id 重發：改成指向程式表與概覽表（「Les AMM recensées figurent dans le tableau ci-dessous／ci-dessus」「statut des AMM : voir l'Aperçu rapide」），哪張註銷、哪個劑型、哪個廠商的事實照留；ambrisentan、moxonidine、triptorelin 的紀錄把 claim 擴成整句（undo_retired 先還原原句再套）；錨在被改寫文字上的 isotretinoin-2、rivastigmine-1（11-06）改錨。
- 一般正文同類句子 16 句寫新紀錄 `fr-lic-20261124b-*`（待查清單 7 句、bendamustine 待辦 1 句，另寫的寬偵測在市場段落掃出、第一輪待查清單沒列的 8 句：amoxicillin、carvedilol、diosmin、risperidone、progesterone、tadalafil 的「Les 5 premières／principales…」，cysteine、sofosbuvir 的「Les N autres sont…」）；bendamustine 待辦「des deux AMM」只拿掉錯的前提（BDPM 6 張）。
- 待查清單 11-24 新增的 56 項全部標 resolved（附 record_ids 或理由：isoflurane、remimazolam、ritonavir 的更正文字沒有張數，只重發說明；benazepril、donepezil 的「dispose d'AMM actives」依事實層成立）。
- 沒改：42 筆紀錄的說明是附資料日期的查證依據（「d'après la BDPM (données du 2026-11-13), les 16 AMM … sont actives」），照原樣保留；正文其他寫死張數的句子（寬偵測 285 句，多是「N AMM valides sur M」）由 B（rewrite_license_counts.py）維護或第一輪已判定。
- 驗證：apply --check 0、gate exit 0、checker 全量 0（改前 0；中途 3 句 M3 已改寫）；last_modified_at 正文有變的頁為 2026-11-24。
