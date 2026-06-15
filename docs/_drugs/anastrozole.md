---
layout: default
title: Anastrozole
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 6
---

# Anastrozole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Anastrozole : Du Statut Non Enregistré au Traitement du Carcinome Mammaire Féminin

## Résumé en Une Phrase

Anastrozole est un inhibiteur sélectif et non stéroïdien de l'aromatase (CYP19A1), reconnu mondialement comme traitement de référence du cancer du sein hormono-sensible chez les femmes ménopausées, mais actuellement non commercialisé sur le marché local analysé.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Carcinome Mammaire Féminin**, avec **50 essais cliniques** et **20 publications** soutenant cette direction, dont les données pivots de l'essai ATAC (n = 9 366).
Cette prédiction constitue une convergence remarquable entre le modèle d'intelligence artificielle et le consensus oncologique international établi.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Non disponible (médicament non enregistré localement) |
| Nouvelle Indication Prédite | Carcinome Mammaire Féminin |
| Score de Prédiction TxGNN | 99,68 % |
| Niveau de Preuve | L1 |
| Statut de Marché | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Anastrozole est un inhibiteur de l'aromatase de troisième génération, hautement sélectif et non stéroïdien. Son mécanisme d'action principal consiste à bloquer l'enzyme CYP19A1 (aromatase), responsable de la conversion des androgènes en estrogènes dans les tissus périphériques. Cette inhibition entraîne une réduction supérieure à 95 % du taux circulant d'estradiol chez les femmes ménopausées, supprimant ainsi la principale source d'estrogènes après la ménopause.

La pertinence de cette prédiction repose sur un lien mécanistique direct : le carcinome mammaire féminin de type hormono-récepteurs positifs (ER+/HER2-) représente environ 70 % de tous les cancers du sein. Ces tumeurs expriment des récepteurs aux estrogènes et dépendent de l'estradiol comme signal de prolifération cellulaire. En supprimant profondément la biosynthèse périphérique des estrogènes, anastrozole prive les cellules tumorales de leur principal facteur de croissance — sans les effets agonistes partiels sur l'endomètre et le système veineux associés au tamoxifène, la référence historique depuis plus de deux décennies.

La relation entre le mécanisme d'anastrozole et le carcinome mammaire est parfaitement validée sur le plan clinique. L'essai ATAC (n = 9 366, suivi médian > 68 mois) a démontré la supériorité d'anastrozole sur le tamoxifène en termes de survie sans maladie (575 vs 651 événements, HR 0,87 ; p < 0,01), avec une réduction du risque de cancer controlatéral et moins d'événements thromboemboliques et d'hyperplasie endométriale. Des essais subséquents ont confirmé son rôle en chimioprévention (IBIS-II), en adjuvant de longue durée, en néoadjuvant et en combinaison avec les inhibiteurs de CDK4/6. Le score TxGNN de 99,68 % reflète cette convergence exceptionnelle de preuves biologiques et cliniques.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---|---|---|---|---|
| [NCT00849030](https://clinicaltrials.gov/study/NCT00849030) | Phase 3 | Terminé | 9 358 | Essai ATAC : Arimidex (anastrozole) seul vs Nolvadex (tamoxifène) seul ou en combinaison en adjuvant chez les femmes ménopausées — anastrozole supérieur en survie sans maladie |
| [NCT00053898](https://clinicaltrials.gov/study/NCT00053898) | Phase 3 | Terminé | 3 104 | Anastrozole vs tamoxifène pour la prévention des récidives chez les femmes ménopausées avec carcinome canalaire in situ (DCIS) après tumorectomie et radiothérapie |
| [NCT00301457](https://clinicaltrials.gov/study/NCT00301457) | Phase 3 | Terminé | 1 914 | Durée optimale d'anastrozole adjuvant (3 ans vs 6 ans) après 2–3 ans de tamoxifène chez les patientes ménopausées avec cancer du sein hormono-sensible |
| [NCT00635713](https://clinicaltrials.gov/study/NCT00635713) | Phase 3 | Terminé | 588 | Fulvestrant (125/250 mg) vs Arimidex (anastrozole 1 mg) dans le cancer du sein avancé ménopausé post-tamoxifène — délai jusqu'à progression tumorale |
| [NCT00784680](https://clinicaltrials.gov/study/NCT00784680) | Phase 3 | Terminé | 308 | Qualité de vie comparée : Arimidex (anastrozole) seul vs Nolvadex seul vs combinaison, en adjuvant chez les femmes ménopausées avec cancer du sein |
| [NCT04964934](https://clinicaltrials.gov/study/NCT04964934) | Phase 3 | Actif, sans recrutement | 315 | AZD9833 (SERD de nouvelle génération) + CDK4/6 inhibiteur vs anastrozole/létrozole + CDK4/6 inhibiteur dans le cancer du sein métastatique HR+/HER2- avec mutation ESR1 — anastrozole utilisé comme bras de référence standard |
| [NCT02763566](https://clinicaltrials.gov/study/NCT02763566) | Phase 3 | Actif, sans recrutement | 463 | Abemaciclib + NSAI (anastrozole ou létrozole) vs abemaciclib + fulvestrant vs placebo dans le cancer du sein récurrent ou métastatique HR+/HER2- ménopausé |
| [NCT02441946](https://clinicaltrials.gov/study/NCT02441946) | Phase 2 | Terminé | 224 | neoMONARCH : Abemaciclib + anastrozole vs abemaciclib seul vs anastrozole seul en néoadjuvant pour les femmes ménopausées avec cancer du sein HR+/HER2- |
| [NCT01723774](https://clinicaltrials.gov/study/NCT01723774) | Phase 2 | Actif, sans recrutement | 84 | Palbociclib + anastrozole en néoadjuvant pour le cancer du sein ER+/HER2- de stade 2–3 — évaluation du taux de réponse pathologique complète vs historique des AI seuls |
| [NCT01626222](https://clinicaltrials.gov/study/NCT01626222) | Phase 3 | Terminé | 301 | Étude 4EVER : Évérolimus + exémestane chez les patientes en progression après NSAI (classe incluant anastrozole) dans le cancer du sein ER+ localement avancé ou métastatique |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [15639680](https://pubmed.ncbi.nlm.nih.gov/15639680/) | 2005 | ECR Phase III | Lancet | Résultats complets de l'essai ATAC (n = 9 366) : anastrozole prolonge la survie sans maladie vs tamoxifène (HR 0,87 ; p < 0,01) avec réduction des cancers controlatéraux et moins d'effets thromboemboliques |
| [31839281](https://pubmed.ncbi.nlm.nih.gov/31839281/) | 2020 | ECR Phase III (Prévention) | Lancet | IBIS-II suivi long terme : anastrozole réduit de 49 % l'incidence du cancer du sein invasif et DCIS chez les femmes à haut risque, avec bénéfice persistant après arrêt du traitement |
| [26686313](https://pubmed.ncbi.nlm.nih.gov/26686313/) | 2016 | ECR Phase III | Lancet | IBIS-II DCIS : anastrozole supérieur au tamoxifène pour la prévention des récidives locorégionales et controlatérales chez les femmes ménopausées avec DCIS HR+ (p = 0,03) |
| [9024711](https://pubmed.ncbi.nlm.nih.gov/9024711/) | 1997 | ECR Phase III | Cancer | Premier essai Phase III d'anastrozole (n = 386) vs acétate de mégestrol en 2e ligne dans le cancer du sein avancé : efficacité comparable avec meilleure tolérance cardio-métabolique |
| [28415634](https://pubmed.ncbi.nlm.nih.gov/28415634/) | 2017 | Méta-analyse d'ECR | Oncotarget | Méta-analyse comparative anastrozole vs tamoxifène : anastrozole associé à une meilleure survie sans progression, réduction des thromboses veineuses et de l'hyperplasie endométriale |
| [28614542](https://pubmed.ncbi.nlm.nih.gov/28614542/) | 2017 | Revue systématique | Rev Assoc Med Bras | Synthèse des données pharmacocinétiques, pharmacodynamiques et d'efficacité d'anastrozole en chimioprévention et traitement du cancer du sein hormono-sensible |
| [32701512](https://pubmed.ncbi.nlm.nih.gov/32701512/) | 2020 | Pharmacogénomique (GWAS) | JCI Insight | Étude GWAS de l'essai MA.27 (anastrozole vs exémestane) : SNP dans CSMD1 associé à moins de récidives distantes sous anastrozole via régulation des voies du complément |
| [34048027](https://pubmed.ncbi.nlm.nih.gov/34048027/) | 2021 | Étude génétique clinique | Clin Pharmacol Ther | Interaction SNP-traitement (n = 4 465) : identification de marqueurs génétiques différenciant l'efficacité adjuvante entre anastrozole et exémestane pour une médecine de précision |
| [19445563](https://pubmed.ncbi.nlm.nih.gov/19445563/) | 2009 | Revue comparative | Expert Opin Pharmacother | Revue comparative anastrozole, létrozole, exémestane dans le cancer du sein précoce : supériorité cohérente des trois AI vs tamoxifène dans les stratégies initial, switch et extended |
| [34667110](https://pubmed.ncbi.nlm.nih.gov/34667110/) | 2022 | Étude mécanistique | Mol Cancer Ther | Mécanisme additionnel d'anastrozole : régulation de la synthase des acides gras (FASN) dans le cancer du sein, distinct des autres AI — implications pour la résistance endocrine |

---

## Cytotoxicité

| Élément | Contenu |
|---|---|
| Classification de Cytotoxicité | Thérapie endocrine ciblée — Inhibiteur de l'Aromatase non stéroïdien de 3e génération (non cytotoxique conventionnel) |
| Risque de Myélosuppression | Faible (anastrozole n'est pas myélosuppresseur ; absence d'effets hématologiques significatifs de classe) |
| Classification d'Émétogénicité | Minimale (nausées légères possibles, non classé comme émétisant en oncologie standard) |
| Éléments de Surveillance | Densité minérale osseuse (DEXA recommandé — risque d'ostéoporose lié à la suppression œstrogénique), bilan hépatique, douleurs articulaires/arthralgie (effet de classe fréquent), bilan lipidique |
| Protection de Manipulation | Manipulation standard — ne nécessite pas les précautions réservées aux médicaments cytotoxiques conventionnels |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Anastrozole dispose d'un niveau de preuve L1 exceptionnel, confirmé par de multiples essais de Phase 3 complétés incluant plus de 15 000 patientes (ATAC, IBIS-II, IBIS-II DCIS, essais de durée optimale). Le score TxGNN de 99,68 % est parfaitement cohérent avec le consensus oncologique international ; cette prédiction représente une validation algorithmique d'un usage clinique mondial établi. La principale contrainte opérationnelle est l'absence d'enregistrement local.

**Pour avancer, les éléments suivants sont nécessaires :**
- Initiation d'une procédure d'AMM locale (TFDA) ou reconnaissance d'équivalence des AMM internationales existantes (FDA, EMA)
- Obtention et analyse de la notice locale complète (avertissements TFDA, contre-indications formelles, interactions médicamenteuses)
- Mise en place d'un plan de surveillance de la densité minérale osseuse (DEXA baseline et suivi annuel) en raison du risque d'ostéoporose lié à la déplétion œstrogénique prolongée
- Évaluation du profil de tolérance musculo-squelettique dans la population locale (arthralgie, syndrome des douleurs articulaires associées aux AI)
- Confirmation de la disponibilité de la chaîne d'approvisionnement locale et des modalités de remboursement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

