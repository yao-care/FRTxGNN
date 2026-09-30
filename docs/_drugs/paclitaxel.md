---
layout: default
title: Paclitaxel
parent: Preuves élevées (L1-L2)
nav_order: 227
evidence_level: L1
indication_count: 10
---

# Paclitaxel
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Paclitaxel : De l'indication d'origine (non renseignée) au carcinome mammaire féminin

## Résumé en une phrase

Le paclitaxel est un agent cytotoxique de la famille des taxanes. Les données fournies ne précisent pas son indication d'origine : les textes d'indication des AMM françaises sont vides.
Le modèle TxGNN prédit qu'il pourrait être efficace dans le **carcinome mammaire féminin**, avec **50 essais cliniques** et **20 publications** associés.
Le paclitaxel est déjà un médicament du cancer du sein largement utilisé, donc cette prédiction reflète probablement un usage établi plutôt qu'un vrai repositionnement.

---

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Non renseignée dans les données (textes d'indication des AMM vides) |
| Nouvelle indication prédite | Carcinome mammaire féminin (*female breast carcinoma*) |
| Score de prédiction TxGNN | 99,995 % |
| Niveau de preuve | L1 |
| Statut de marché en France | ✓ Commercialisé |
| Nombre d'AMM | 12 |
| Décision recommandée | Proceed with Guardrails |

---

## Pourquoi cette prédiction est-elle raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne figurent pas dans le dossier. Le paclitaxel appartient à la classe des taxanes, et la littérature fournie le décrit ainsi : il stabilise les microtubules et empêche le désassemblage du fuseau mitotique. Les cellules sont alors bloquées en phase G2/M et entrent en apoptose. Ce mécanisme est bien caractérisé dans le cancer du sein (revue PMID 31783552).

Ce mécanisme touche surtout les cellules qui se divisent rapidement, ce qui correspond bien aux tumeurs mammaires. Le paclitaxel est un traitement de première ligne fréquent dans le cancer du sein, seul ou associé au trastuzumab, à l'anthracycline ou au carboplatine.

Le dossier ne permet pas de dire si le cancer du sein figure déjà dans les indications des AMM françaises. Les textes d'indication sont vides. **Il faut donc vérifier le libellé des AMM avant de considérer ce signal comme un repositionnement.**

---

## Preuves d'essais cliniques

Sur les 50 essais associés à cette indication, voici les 10 plus pertinents (essais de phase 3 et essais jugés pertinents par l'évaluation).

| Numéro d'essai | Phase | Statut | Inscription | Résultats principaux |
|---------|------|------|------|---------|
| [NCT00003992](https://clinicaltrials.gov/study/NCT00003992) | Phase 2 | Terminé | 200 | Paclitaxel + trastuzumab en traitement adjuvant du cancer du sein précoce HER2+ (pertinence A) |
| [NCT00281658](https://clinicaltrials.gov/study/NCT00281658) | Phase 3 | Terminé | 444 | Lapatinib + paclitaxel contre placebo + paclitaxel, cancer du sein métastatique ErbB2+ (randomisé, double aveugle) |
| [NCT00003088](https://clinicaltrials.gov/study/NCT00003088) | Phase 3 | Terminé | 2005 | Doxorubicine, cyclophosphamide puis paclitaxel à 14 ou 21 jours, cancer du sein N+ stade II/IIIA |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Terminé | 3270 | Chimiothérapie adjuvante (dont paclitaxel hebdomadaire) avec ou sans trastuzumab, cancer du sein HER2-low |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | Terminé | 478 | FE75C dose-dense suivi de docétaxel contre paclitaxel, traitement adjuvant N+ |
| [NCT00513292](https://clinicaltrials.gov/study/NCT00513292) | Phase 3 | Terminé | 280 | FEC-75 suivi de paclitaxel + trastuzumab contre séquence inverse, cancer du sein opérable HER2+ |
| [NCT00016276](https://clinicaltrials.gov/study/NCT00016276) | Phase 3 | Arrêté | 396 | AC ± dexrazoxane puis paclitaxel ± trastuzumab, cancer du sein HER2+ avancé |
| [NCT00272987](https://clinicaltrials.gov/study/NCT00272987) | Phase 3 | Arrêté | 63 | Paclitaxel + trastuzumab + lapatinib contre placebo, cancer du sein métastatique ErbB2+ (arrêt précoce, pertinence B) |
| [NCT00455533](https://clinicaltrials.gov/study/NCT00455533) | Phase 2 | Terminé | 384 | AC suivi d'ixabépilone contre AC suivi de paclitaxel en néoadjuvant (le paclitaxel est le bras de référence) |
| [NCT00054028](https://clinicaltrials.gov/study/NCT00054028) | Phase 1/2 | Terminé | 31 | Suramine + paclitaxel dans le cancer du sein avancé (faisabilité de l'association, pertinence B) |

---

## Preuves de la littérature

Sur les 20 publications associées, voici les 10 plus pertinentes. Aucun ECR de phase 3 n'y figure directement.

| PMID | Année | Type | Revue | Résultats principaux |
|------|-----|------|------|---------|
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Revue | Biomolecules | Mécanismes d'action et effets cliniques du paclitaxel dans le cancer du sein ; la résistance est un obstacle majeur |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Revue | Drug Ther Bull | Paclitaxel et docétaxel dans les cancers du sein et de l'ovaire ; extension de licence au sein métastatique |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Essai clinique (phase II) | Cancer | Doxorubicine + paclitaxel dans le cancer du sein avancé ; rôle du traitement adjuvant antérieur par anthracycline |
| [15305399](https://pubmed.ncbi.nlm.nih.gov/15305399/) | 2004 | Essai randomisé | Cancer | Épirubicine et paclitaxel en concomitant ou en séquentiel en première ligne métastatique (non-infériorité) |
| [11751485](https://pubmed.ncbi.nlm.nih.gov/11751485/) | 2001 | Essai randomisé (phase II) | Clin Cancer Res | Chimiothérapie adjuvante dose-dense avec paclitaxel dans le cancer du sein N+ (résultats à 5 ans) |
| [24068539](https://pubmed.ncbi.nlm.nih.gov/24068539/) | 2013 | Essai clinique (phase I-II) | Breast Cancer Res Treat | Tipifarnib + paclitaxel hebdomadaire puis AC, cancer du sein localement avancé |
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | Cohorte (données réelles) | Biomed Res Int | Néoadjuvant épirubicine/cyclophosphamide puis paclitaxel-trastuzumab dans le cancer du sein HER2+ |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Étude clinique | Cancer | Rôle du paclitaxel dans le traitement multimodal du cancer du sein inflammatoire |
| [39009452](https://pubmed.ncbi.nlm.nih.gov/39009452/) | 2024 | Étude mécanistique | J Immunother Cancer | Rôle du paclitaxel sur les macrophages associés aux tumeurs, en association avec un anti-PD-1 dans le cancer du sein triple négatif |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Étude génomique | Nat Commun | Variations de TEKT4 associées à la résistance du cancer du sein au paclitaxel |

---

## Informations de marché en France

Le dossier compte 12 AMM ; les 5 principales sont listées ci-dessous.

| Numéro d'AMM | Nom du produit | Forme pharmaceutique | Indication approuvée |
|---------|------|------|-----------|
| 61516960 | APEXELSIN 5 mg/mL | Poudre pour dispersion pour perfusion | Non renseignée |
| 68739019 | ABRAXANE 5 mg/mL | Poudre pour dispersion injectable pour perfusion | Non renseignée |
| 67297982 | PACLITAXEL VIATRIS 6 mg/ml | Solution à diluer pour perfusion | Non renseignée |
| 64711759 | PACLITAXEL TEVA 6 mg/mL | Solution à diluer pour perfusion | Non renseignée |
| 69161632 | PACLITAXEL SANDOZ 6 mg/ml | Solution à diluer pour perfusion | Non renseignée |

APEXELSIN et ABRAXANE sont des formulations de paclitaxel lié à l'albumine (nab-paclitaxel). Les autres sont des formulations classiques en solution.

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de cytotoxicité | Cytotoxique conventionnel (taxane, agent antimicrotubules) |
| Risque de myélosuppression | Élevé (la neutropénie est classiquement le facteur limitant de la dose) |
| Classification d'émétogénicité | Faible |
| Éléments de surveillance | NFS avec formule, fonction hépatique (bilirubine, transaminases), neuropathie périphérique (documentée comme toxicité limitante dans les essais fournis) |
| Protection de manipulation | Oui : suivre les règles de manipulation des médicaments cytotoxiques |

Ces éléments viennent de la classe pharmacologique. Le dossier ne contient pas de données de toxicité propres à ce médicament, à confirmer avec la notice.

---

## Considérations de sécurité

Les données de sécurité de l'ANSM (mises en garde, contre-indications) ne sont pas disponibles dans le dossier. Veuillez consulter la notice pour les informations de sécurité.

Les essais et publications fournis signalent notamment la neuropathie périphérique induite par le paclitaxel, des pneumopathies interstitielles (séries de cas) et des toxicités cutanées ou oculaires (cas isolés).

---

## Conclusion et prochaines étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Le niveau de preuve est L1. Plusieurs essais de phase 3 terminés utilisent le paclitaxel dans le cancer du sein, et son mécanisme antimitotique est bien établi.
- Il s'agit très probablement d'un usage déjà établi et non d'un repositionnement nouveau. Sans les indications des AMM ni les données de sécurité de la notice, on ne peut pas aller plus loin.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser les notices ANSM (mises en garde, contre-indications), ce qui est bloquant pour le criblage de sécurité.
- Vérifier les indications des AMM pour savoir si le cancer du sein est déjà approuvé, en distinguant paclitaxel classique et nab-paclitaxel.
- Compléter le mécanisme d'action et l'indication d'origine via DrugBank.

**Note sur les autres prédictions :**
- Les rangs 2 à 4 (cancer du sein ER-négatif, hormono-résistant, ER-positif) et les rangs 6 à 8 (formes bilatérale, par profil d'expression, mamelon) sont des sous-types du même cancer du sein.
- Le rang 5 (tumeur d'Ehrlich) est un modèle murin, sans indication humaine.
- Les rangs 9 et 10 (rhabdomyosarcomes) reposent uniquement sur le modèle, sans aucune étude (niveau L5, décision Hold).

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement nécessite une validation clinique.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

