---
layout: default
title: Cabergoline
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 5
---

# Cabergoline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Cabergoline : De l'Hyperprolactinémie au Cancer de l'Hypophyse

## Résumé en Une Phrase

La cabergoline est un agoniste dopaminergique D2 hautement sélectif, établi comme traitement de première ligne mondial de l'hyperprolactinémie et des prolactinomes hypophysaires.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **Cancer de l'Hypophyse** (pituitary cancer),
avec **20 essais cliniques** et **20 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Hyperprolactinémie / Prolactinome (traitement de référence mondial) |
| Nouvelle Indication Prédite | Cancer de l'Hypophyse (Pituitary Cancer) |
| Score de Prédiction TxGNN | 99.04% |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Non commercialisé (aucune AMM répertoriée dans ce registre) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

> **Note sur l'indication originale** : Les données réglementaires françaises ne répertorient pas de licences actives. Cependant, les essais cliniques et la littérature confirment que la cabergoline (Dostinex®) est largement approuvée et commercialisée dans de nombreux pays pour l'hyperprolactinémie et les prolactinomes. L'absence d'AMM dans ce registre peut refléter une lacune de données ou une situation réglementaire spécifique à vérifier.

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action (MOA) officiel n'étant pas disponibles dans les sources interrogées, la reconstitution mécanistique repose sur les données cliniques et la littérature scientifique. La cabergoline est un agoniste dopaminergique D2 hautement sélectif qui agit directement sur les récepteurs D2 (D2R) des cellules lactotropes de la glande hypophysaire. Elle inhibe la voie cAMP-PKA, réduisant la synthèse de prolactine et la prolifération cellulaire tumorale. Ce mécanisme est si bien établi pour les prolactinomes que la cabergoline constitue le traitement de première ligne international depuis plusieurs décennies.

La pertinence de son extension au cancer de l'hypophyse au sens large repose sur plusieurs observations convergentes : les adénomes hypophysaires non fonctionnels (NFPA), bien que moins riches en D2R que les prolactinomes, présentent une réponse tumorale chez 20 à 30 % des patients ; une étude translationnelle récente (PMID 38989697) a démontré que l'inhibition de HTR2B potentialise l'effet antiprolifératif de la cabergoline via l'axe Gαq/PLC/PKCγ/STAT3, élargissant la compréhension mécanistique au-delà du seul récepteur D2 ; enfin, plusieurs essais de Phase 3 complétés et en cours (dont NCT03271918, n=140 ; NCT02288962, n=60) confirment un bénéfice clinique dans les NFPA.

Il convient néanmoins de distinguer soigneusement trois entités : (1) les **prolactinomes** (adénomes bénins sécrétants, répondant excellemment à la cabergoline — indication établie), (2) les **adénomes non fonctionnels** (NFPA, réponse partielle documentée), et (3) les **adénocarcinomes hypophysaires** (tumeurs malignes extrêmement rares, < 200 cas mondiaux recensés), pour lesquels la transposabilité mécanistique reste à démontrer et constitue une indication distincte classée en « Research Question » par le modèle.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---|---|---|---|---|
| [NCT04107480](https://clinicaltrials.gov/study/NCT04107480) | Phase 4 | Inconnu | 880 | PRolaCT : trois RCT multicentriques comparant chirurgie endoscopique vs agoniste dopaminergique en première et deuxième ligne — plus grand essai dans le domaine |
| [NCT02288962](https://clinicaltrials.gov/study/NCT02288962) | Phase 3 | En cours | 60 | RCT évaluant le traitement des adénomes hypophysaires non fonctionnels (NFPA) par dopamine agoniste vs surveillance — essai de référence international en cours jusqu'en 2028 |
| [NCT03271918](https://clinicaltrials.gov/study/NCT03271918) | Phase 3 | Terminé | 140 | Cabergoline pour les NFPA résiduels post-chirurgie transsphénoïdale — essai monocentrique, ouvert, randomisé, définissant l'efficacité du traitement médical post-opératoire |
| [NCT07034859](https://clinicaltrials.gov/study/NCT07034859) | Phase 4 | Recrutement sur invitation | 30 | Cabergoline vs observation comme thérapie primaire des NFPA — évalue la réduction tumorale à 48 semaines avec visites toutes les 12 semaines |
| [NCT01620138](https://clinicaltrials.gov/study/NCT01620138) | Phase 2/3 | Terminé | 21 | Expression des récepteurs somatostatine et D2 dans les NFPA et prolactinomes résistants — fournit la base moléculaire pour la sélection des patients |
| [NCT07045935](https://clinicaltrials.gov/study/NCT07045935) | Phase 4 | En recrutement | 60 | RCT comparant les effets de différentes stratégies de dopamine agoniste sur le métabolisme glucidique dans les prolactinomes — en cours jusqu'en 2029 |
| [NCT01915303](https://clinicaltrials.gov/study/NCT01915303) | Phase 2 | Terminé (arrêté prématurément) | 68 | Pasireotide seul ou en association avec cabergoline dans la maladie de Cushing hypophysaire — terminé prématurément, données de combinaison disponibles |
| [NCT00889525](https://clinicaltrials.gov/study/NCT00889525) | Phase 3 | Terminé | N/A | Cabergoline dans les adénomes corticotropes (maladie de Cushing) — évalue l'efficacité du D2 agoniste sur les tumeurs hypophysaires sécrétant de l'ACTH |
| [NCT00376064](https://clinicaltrials.gov/study/NCT00376064) | Phase 4 | Terminé | 20 | Octreotide + cabergoline sur 8 mois dans les acromégalies partiellement répondantes aux analogues de somatostatine — preuve de concept de la combinaison |
| [NCT07124221](https://clinicaltrials.gov/study/NCT07124221) | Phase 3 | En recrutement | 382 | RCT en double aveugle comparant cabergoline vs bromocriptine dans l'hyperprolactinémie féminine — essai comparateur actif à grande échelle |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [35902444](https://pubmed.ncbi.nlm.nih.gov/35902444/) | 2022 | Revue Systématique & Méta-analyse | *Pituitary* | Méta-analyse des études évaluant la cabergoline dans les NFPA : synthèse quantitative de l'efficacité sur la stabilisation et la réduction tumorale |
| [37097352](https://pubmed.ncbi.nlm.nih.gov/37097352/) | 2023 | Revue | *JAMA* | Diagnostic et prise en charge des adénomes hypophysaires : revue clinique de référence couvrant les options médicales incluant les D2 agonistes |
| [36974474](https://pubmed.ncbi.nlm.nih.gov/36974474/) | 2023 | Revue Clinique | *J Clin Endocrinol Metab* | Approche du patient avec prolactinome : dopamine agonistes comme traitement standard, gestion de l'hypogonadisme et des effets de masse |
| [36013562](https://pubmed.ncbi.nlm.nih.gov/36013562/) | 2022 | Revue | *Medicina* | Traitement des prolactinomes incluant les thérapies multimodales pour les formes agressives résistantes — panorama historique et moderne |
| [38989697](https://pubmed.ncbi.nlm.nih.gov/38989697/) | 2024 | Étude Translationnelle | *Neuro-oncology* | L'inhibition de HTR2B supprime la croissance des NFPA et potentialise la cabergoline via l'axe Gαq/PLC/PKCγ/STAT3 — nouveau mécanisme de sensibilisation |
| [31597135](https://pubmed.ncbi.nlm.nih.gov/31597135/) | 2020 | Revue | *Neuroendocrinology* | Nouveaux mécanismes antiprolifératifs et inducteurs de mort cellulaire de la cabergoline — applications potentielles au-delà des prolactinomes |
| [28973192](https://pubmed.ncbi.nlm.nih.gov/28973192/) | 2017 | Étude Préclinique/Combinaison | *J Clin Endocrinol Metab* | Synergie cabergoline + chloroquine dans la suppression tumorale hypophysaire via induction de l'autophagie et de la mort cellulaire autophagique |
| [40170221](https://pubmed.ncbi.nlm.nih.gov/40170221/) | 2025 | Étude Biomarqueur | *Eur J Endocrinology* | miR-20a-5p circulant comme biomarqueur prédictif de la réponse à la cabergoline dans les prolactinomes — outil potentiel de sélection des patients |
| [25732645](https://pubmed.ncbi.nlm.nih.gov/25732645/) | 2015 | Revue | *Endocrinol Metab Clin North Am* | Cabergoline dans les tumeurs hypophysaires : efficacité établie et débat sur le risque valvulaire cardiaque lors des traitements prolongés |
| [28025719](https://pubmed.ncbi.nlm.nih.gov/28025719/) | 2017 | Revue | *Pituitary* | Cabergoline dans l'acromégalie : rôle des D2 agonistes en deuxième ligne pour les adénomes somatotropes partiellement répondants |

---

## Informations de Marché en France

Aucune AMM enregistrée dans le registre disponible.

> **Contexte important** : La cabergoline (Dostinex®, Cabaser®) est commercialisée dans de nombreux pays européens, aux États-Unis et au Japon pour le traitement de l'hyperprolactinémie. L'absence d'AMM dans le présent registre nécessite une vérification directe auprès de l'ANSM (Agence Nationale de Sécurité du Médicament) avant toute conclusion sur la disponibilité réelle en France.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité complètes (données ANSM non disponibles dans ce pack).

> **Signal de sécurité notable — Glaucome par fermeture d'angle** : Un cas documenté de glaucome par fermeture d'angle bilatéral aigu a été rapporté chez une patiente traitée par cabergoline pour galactorrhée ([PMID 21347189](https://pubmed.ncbi.nlm.nih.gov/21347189/)). Bien que ce signal soit rare, il doit être pris en compte lors de l'extension à de nouvelles populations.

> **Risque valvulaire cardiaque** : Des études ont investigué l'association entre traitement chronique par cabergoline et régurgitation valvulaire cardiaque (NCT00460616 ; PMID 25732645). La majorité des études n'objectivent pas d'augmentation significative du risque aux doses utilisées en endocrinologie, mais une surveillance cardiologique reste recommandée lors des traitements prolongés.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Plusieurs essais cliniques de Phase 3 complétés (NCT03271918, n=140 ; NCT00889525) et un essai Phase 4 multicentrique de grande envergure (PRolaCT, n=880) confirment l'efficacité de la cabergoline dans les tumeurs hypophysaires fonctionnelles et non fonctionnelles. La méta-analyse (PMID 35902444) et les données mécanistiques émergentes (PMID 38989697) consolident un niveau de preuve L1 pour les adénomes hypophysaires. La cabergoline constitue déjà un traitement médical validé dans ce domaine ; le repositionnement porte essentiellement sur l'élargissement à des sous-types tumoraux moins documentés (NFPA, formes agressives).

**Pour avancer, les éléments suivants sont nécessaires :**

- **Vérification réglementaire France** : Confirmer le statut AMM auprès de l'ANSM — une AMM Dostinex® pourrait déjà exister, rendant le repositionnement partiellement hors périmètre
- **Données MOA complètes** : Récupérer la fiche DrugBank (DB00248) pour les cibles moléculaires officielles et les catégories pharmacologiques
- **Stratification par sous-type tumoral** : Distinguer clairement prolactinome (L1, indication établie), NFPA (L2-L3, en développement) et adénocarcinome hypophysaire (L4, « Research Question » — entité maligne distincte avec très peu de cas mondiaux)
- **Plan de surveillance cardiaque** : Protocole d'évaluation valvulaire pour les traitements de longue durée dans de nouvelles populations
- **Biomarqueur de sélection** : Évaluer le statut D2R tumoral (PET-MR, immunohistochimie) et miR-20a-5p comme prédicteurs de réponse avant inclusion dans des essais prospectifs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

