---
layout: default
title: Doxorubicin
parent: Preuves élevées (L1-L2)
nav_order: 258
evidence_level: L1
indication_count: 8
last_modified_at: 2026-11-24
monitor_inn: "doxorubicin"
predicted_indications: ["Ewing sarcoma", "well-differentiated fetal adenocarcinoma of the lung", "primary pulmonary lymphoma", "pulmonary blastoma", "monocytic leukemia", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "parameningeal embryonal rhabdomyosarcoma", "rhabdomyosarcoma (disease)"]
description: "Doxorubicin : nouvelle indication prédite, Sarcome d'Ewing (Ewing sarcoma) (niveau de preuve L1). En France, AMM dans la BDPM : 9 (valides : 9)"
---

# Doxorubicin
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **8** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

## Doxorubicin: Sarcome d'Ewing (Ewing sarcoma)
{: .text-alpha }

## Résumé en Une Phrase

La doxorubicine est une anthracycline cytotoxique, initialement utilisée dans le traitement de la leucémie lymphoblastique aiguë, des lymphomes (hodgkinien et non hodgkinien) et de l'histiocytose à cellules de Langerhans.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **Sarcome d'Ewing**,
avec **26 essais cliniques** et **20 publications** soutenant actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Sarcome d'Ewing (Ewing sarcoma) |
| Score de Prédiction TxGNN | 0.9990 |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Commercialisé (autorisations valides : 9 sur 9) |
| Nombre d'AMM | 9 (valides : 9) |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Doxorubicin (traduction non officielle) : « L'effet cytotoxique du chlorhydrate de doxorubicine sur les cellules malignes et ses effets toxiques sur divers organes seraient liés aux activités d'intercalation entre les bases nucléotidiques et de liaison aux lipides des membranes cellulaires de la doxorubicine. L'intercalation inhibe la réplication des nucléotides et l'action des ADN et ARN polymérases. » Texte original en anglais : "The cytotoxic effect of doxorubicin hydrochloride on malignant cells and its toxic effects on various organs are thought to be related to nucleotide base intercalation and cell membrane lipid binding activities of doxorubicin. Intercalation inhibits nucleotide replication and action of DNA and RNA polymerases." ([DailyMed: Oxderys (doxorubicin hydrochloride) prescribing information, Avyxa Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f280fb2e-5070-46e1-a4ed-ba191359cedd), version du 2026-11-12 ; consulté le 2026-11-19). Sur la base des informations connues, la doxorubicine est une anthracycline qui inhibe la topoisomérase II et s'intercale dans l'ADN. Son efficacité a été établie dans les hémopathies lymphoïdes (leucémie lymphoblastique aiguë, lymphomes), et son action cytotoxique sur les cellules à prolifération rapide pourrait mécanistiquement s'appliquer au sarcome d'Ewing.

Dans les données compilées, la doxorubicine est un composant central des schémas de chimiothérapie multi-agents du sarcome d'Ewing (VDC/IE, VAC : vincristine, doxorubicine, cyclophosphamide, alternés avec ifosfamide et étoposide). Les tumeurs à petites cellules rondes, très prolifératives, y sont sensibles. Le lien avec l'indication originale tient donc à la chimiosensibilité de tumeurs à croissance rapide, plus qu'à une parenté histologique directe.

Il faut noter que la plupart des essais portent sur des associations : la contribution propre de la doxorubicine ne peut pas être isolée dans ces études. La toxicité cumulative cardiaque impose des limites de dose et une surveillance cardiaque.

## Preuves d'Essais Cliniques

Dix essais parmi les plus pertinents (sur 26 enregistrés) sont présentés.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Terminé | 587 | Essai randomisé comparant des schémas de chimiothérapie par compression d'intervalles dans le sarcome d'Ewing et tumeurs apparentées |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Terminé | 642 | Ajout de vincristine-topotécan-cyclophosphamide au traitement standard à 5 médicaments (dont doxorubicine) dans le sarcome d'Ewing non métastatique |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Terminé | 278 | Intensification de dose dans le sarcome d'Ewing non métastatique (traitement standard vs intensif) |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | Inconnu | 1200 | EURO-E.W.I.N.G.99 : chimiothérapie avec ou sans radiothérapie/chirurgie/greffe de cellules souches |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Actif, ne recrute plus | 312 | Ajout du ganitumab (anti-IGF-1R) à la chimiothérapie multi-agents dans le sarcome d'Ewing métastatique |
| [NCT00002516](https://clinicaltrials.gov/study/NCT00002516) | Phase 3 | Inconnu | Non renseigné | EICESS 92 : comparaison de schémas de chimiothérapie associés à chirurgie et radiothérapie |
| [NCT00038142](https://clinicaltrials.gov/study/NCT00038142) | Phase 2 | Arrêté | 46 | VAC avec dexrazoxane, avec ou sans ImmTher, dans le sarcome d'Ewing à haut risque ; arrêté avec effectif limité |
| [NCT00003667](https://clinicaltrials.gov/study/NCT00003667) | Phase 2 | Terminé | Non renseigné | Essai randomisé VAC + dexrazoxane avec ou sans ImmTher |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Phase 2 | Terminé | Non renseigné | Cyclophosphamide, doxorubicine, vincristine, étoposide et ifosfamide suivis de résection et radiothérapie |
| [NCT01946529](https://clinicaltrials.gov/study/NCT01946529) | Phase 2 | Terminé | 24 | Traitement stratifié des tumeurs de la famille du sarcome d'Ewing et des tumeurs desmoplastiques à petites cellules rondes |

## Preuves de la Littérature

Dix publications parmi les plus pertinentes (sur 20) sont présentées, avec priorité aux essais randomisés.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | ECR | N Engl J Med | Ajout d'ifosfamide et d'étoposide à la chimiothérapie standard dans le sarcome d'Ewing nouvellement diagnostiqué |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | ECR | J Clin Oncol | Chimiothérapie à intervalles compressés dans le sarcome d'Ewing localisé (Children's Oncology Group) |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | ECR (phase 3) | Lancet | EE2012 : comparaison de deux schémas de chimiothérapie dans le sarcome d'Ewing nouvellement diagnostiqué |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | ECR (phase 3) | J Clin Oncol | Ganitumab associé à la chimiothérapie à intervalles compressés dans le sarcome d'Ewing métastatique |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | Protocole d'ECR | Trials | Protocole de l'essai international EURO EWING 2012 |
| [39838616](https://pubmed.ncbi.nlm.nih.gov/39838616/) | 2025 | Cohorte | Pediatr Blood Cancer | Essai GALOP-2011 : chimiothérapie multi-agents à intervalles compressés (VDC/IE) dans le sarcome d'Ewing localisé |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Revue | Cancer | Recommandations consensuelles du National Ewing Sarcoma Tumor Board |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Revue | J Clin Oncol | Prise en charge actuelle du sarcome d'Ewing et perspectives de collaboration |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Revue | Lancet Oncol | Survie passée d'environ 10 % à environ 75 % pour les formes localisées grâce à la chimiothérapie |
| [1833556](https://pubmed.ncbi.nlm.nih.gov/1833556/) | 1991 | Analyse de dose-intensité | J Natl Cancer Inst | Influence de l'intensité de dose de doxorubicine sur la réponse et l'évolution dans l'ostéosarcome et le sarcome d'Ewing |

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 64367525 | ADRIBLASTINE 50 mg, poudre pour solution injectable en flacon | Poudre pour solution injectable | PFIZER HOLDING FRANCE | Active |
| 65771499 | ADRIBLASTINE 10 mg, poudre pour solution injectable en flacon | Poudre pour solution injectable | PFIZER HOLDING FRANCE | Active |
| 62362369 | CAELYX PEGYLATED LIPOSOMAL 2 mg/ml, solution à diluer pour perfusion | Solution à diluer pour perfusion | BAXTER HOLDING (PAYS-BAS) | Active |
| 62783375 | DOXORUBICINE ACCORD 2 mg/ml, solution pour perfusion | Solution pour perfusion | ACCORD HEALTHCARE FRANCE | Active |
| 63627532 | DOXORUBICINE TEVA 10 mg/5 ml, solution injectable | Solution injectable | TEVA SANTE | Active |
| 64912833 | ZOLSKETIL PEGYLATED LIPOSOMAL 2 mg/mL, dispersion à diluer pour perfusion | Dispersion à diluer pour perfusion | ACCORD HEALTHCARE (ESPAGNE) | Active |
| 66837710 | DOXORUBICINE ARROW 2 mg/mL, solution pour perfusion | Solution pour perfusion | EUGIA PHARMA (MALTA) (MALTE) | Active |
| 69467732 | DOXORUBICINE TEVA 200 mg/100 mL, solution injectable | Solution injectable | TEVA SANTE | Active |
| 69833133 | DOXORUBICINE TEVA 50 mg/25 mL, solution injectable | Solution injectable | TEVA SANTE | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

Les AMM ADRIBLASTINE, détenues par PFIZER HOLDING FRANCE, sont valides. Les autres AMM de doxorubicine figurent dans le tableau ci-dessus.

<!-- review:begin fr-lic-20261124-doxorubicin-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Les deux autorisations, détenues par PFIZER HOLDING FRANCE, sont valides. » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans l'Aperçu rapide. Le tableau des AMM de cette page est désormais généré à partir des données BDPM ; la mention du nombre d'AMM affichées dans l'ancien tableau et les nombres d'AMM écrits en dur sont retirés. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-doxorubicin-1 -->

<!-- review:begin fr-lic-20261124-doxorubicin-2 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Deux AMM valides sur deux sont donc recensées dans les données compilées. » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans l'Aperçu rapide. Les nombres d'AMM écrits en dur dans le texte corrigé sont retirés : le nombre et le statut à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché, générés à partir des données BDPM. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-doxorubicin-2 -->

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (anthracycline, inhibiteur de la topoisomérase II) |
| Risque de Myélosuppression | Élevé (les contre-indications du graphe de connaissances incluent neutropénie, leucopénie, thrombopénie, agranulocytose et anémie) |
| Classification d'Émétogénicité | Moyenne à élevée (selon la classe ; non précisée dans les données compilées) |
| Éléments de Surveillance | NFS avec formule, fonction hépatique (bilirubine) et rénale, fonction cardiaque (échocardiographie/FEVG) avec suivi de la dose cumulée |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques |

## Considérations de Sécurité

Les données de mises en garde et de contre-indications issues de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance et maladie hépatiques, insuffisance cardiaque congestive, cardiomyopathies, maladies cardiovasculaires, arrêt cardiaque soudain, maladies de la conduction cardiaque, thrombopénie, neutropénie, agranulocytose, leucopénie, anémie, hyperbilirubinémie (dont syndrome de Gilbert), maladies infectieuses et fongiques, déficit en G6PD.
- **Interactions médicamenteuses** : 665 interactions recensées. Parmi les principales, **majeures** : dolasétron, cisapride, papavérine ; **modérées** : ondansétron, granisétron, palonosétron, aprépitant, rolapitant, dexaméthasone, clarithromycine, lévofloxacine, famotidine, lopéramide, eliglustat, métréleptine, troglitazone.
- **Point de vigilance** : la toxicité cardiaque cumulative impose des limites de dose et une surveillance cardiaque ; elle est particulièrement préoccupante chez l'enfant. Les essais utilisent parfois le dexrazoxane comme cardioprotecteur.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Plusieurs essais randomisés de phase 3 et de grandes publications incluent la doxorubicine dans le traitement standard du sarcome d'Ewing, ce qui soutient fortement la prédiction (niveau L1). Toutefois, la doxorubicine y est administrée en association, son rôle propre n'est pas isolé et les données de sécurité de la notice sont absentes.

<!-- review:begin fr-lic-20261106-doxorubicin-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Toutefois, la doxorubicine y est administrée en association, son rôle propre n'est pas isolé, les AMM françaises sont toutes annulées et les données de sécurité de la notice sont absentes. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-doxorubicin-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice (mises en garde, contre-indications) auprès de l'ANSM, lacune bloquante pour le dépistage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Clarifier le statut réglementaire en France et identifier une présentation disponible, par exemple une autre spécialité de doxorubicine
- Confirmer la contribution propre de la doxorubicine dans les schémas VDC/IE à partir des résultats des essais de phase 3
- Établir un plan de surveillance cardiaque (limite de dose cumulée, évaluation de la FEVG, cardioprotection) et de la myélosuppression, notamment en pédiatrie

<!-- review:begin fr-lic-20261106-doxorubicin-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarifier le statut réglementaire en France (AMM annulées) et identifier une présentation disponible, par exemple une autre spécialité de doxorubicine » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-doxorubicin-2 -->

**Remarque sur les autres indications prédites :** le rhabdomyosarcome (niveau L1, Proceed with Guardrails) est également soutenu par des essais de phase 3 sur les sarcomes des tissus mous, mais ceux-ci ne sont pas spécifiques du rhabdomyosarcome. Les autres prédictions (adénocarcinome fœtal du poumon, lymphome pulmonaire primitif, blastome pulmonaire, leucémie myéloïde chronique BCR-ABL1, leucémie monocytaire, rhabdomyosarcome embryonnaire vaginal ou paraméningé, ganglioneuroblastome) reposent sur des preuves limitées ou indirectes (Hold ou question de recherche).

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « les AMM françaises sont toutes annulées » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « (AMM annulées) » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-12 | Tableau : l’AMM 64367525 (ADRIBLASTINE 50 mg) est active, non annulée | Remplacé par le tableau d'AMM généré par programme (auparavant : Corrigé) | [Base de données publique des médicaments (BDPM)](https://base-donnees-publique.medicaments.gouv.fr/) |
| 2026-11-12 | Tableau : l’AMM 65771499 (ADRIBLASTINE 10 mg) est active, non annulée | Remplacé par le tableau d'AMM généré par programme (auparavant : Corrigé) | [Base de données publique des médicaments (BDPM)](https://base-donnees-publique.medicaments.gouv.fr/) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Oxderys (doxorubicin hydrochloride) prescribing information, Avyxa Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f280fb2e-5070-46e1-a4ed-ba191359cedd) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

