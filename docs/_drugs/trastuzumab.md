---
layout: default
title: Trastuzumab
parent: Preuves élevées (L1-L2)
nav_order: 779
evidence_level: L1
indication_count: 10
---

# Trastuzumab
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

# Trastuzumab : Du Cancer du Sein HER2-Positif au Cancer du Sein à Récepteur de la Progestérone Positif

## Résumé en Une Phrase

Trastuzumab est un anticorps monoclonal dirigé contre le récepteur HER2, initialement utilisé pour le traitement du carcinome mammaire HER2-positif.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **cancer du sein à récepteur de la progestérone positif**, avec **14 essais cliniques** et **20 publications** soutenant actuellement cette direction.
Il s'agit toutefois surtout d'un sous-groupe défini par le statut hormonal au sein de l'indication d'origine : le bénéfice n'est attendu qu'en cas de tumeur HER2-positive.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carcinome mammaire HER2-positif |
| Nouvelle Indication Prédite | Cancer du sein à récepteur de la progestérone positif |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Autorisations uniquement annulées |
| Nombre d'AMM | 16 (toutes annulées) |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances établies, le trastuzumab se lie au récepteur HER2 (ERBB2) à la surface des cellules tumorales, bloque sa signalisation et favorise la destruction des cellules par cytotoxicité cellulaire dépendante des anticorps (ADCC).

Une partie des cancers du sein à récepteur de la progestérone positif (type luminal B/HER2-positif) co-exprime HER2. L'indication prédite est donc en grande partie un sous-groupe de l'indication d'origine, défini par le statut hormonal, et non une indication mécanistiquement distincte. Une interaction connue (« dialogue croisé ») existe entre la voie hormonale et la voie HER2, ce qui justifie l'association d'un traitement endocrinien et d'un blocage de HER2.

Le bénéfice dépend du statut HER2 et non du statut du récepteur de la progestérone. Les tumeurs PR-positives/HER2-négatives ne devraient pas bénéficier du trastuzumab.

---

## Preuves d'Essais Cliniques

Sélection des essais les plus pertinents (14 essais recensés pour cette indication).

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Terminé | 3270 | Chimiothérapie adjuvante avec ou sans trastuzumab dans le cancer du sein invasif à ganglions positifs ou à haut risque ; essai randomisé de grande taille |
| [NCT01750073](https://clinicaltrials.gov/study/NCT01750073) | Phase 2 | Terminé | 92 | Chimiothérapie néoadjuvante (paclitaxel + cyclophosphamide) avec ou sans trastuzumab |
| [NCT00194779](https://clinicaltrials.gov/study/NCT00194779) | Phase 2 | Terminé | 50 | Chimiothérapie néoadjuvante dans le cancer du sein HER2-positif résécable, avec ou sans récepteurs hormonaux |
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Phase 2 | Terminé | 33 | Létrozole + trastuzumab dans le cancer du sein métastatique ERBB2-positif et RE et/ou RP positif |
| [NCT02260531](https://clinicaltrials.gov/study/NCT02260531) | Phase 2 | Terminé | 36 | Cabozantinib seul ou avec trastuzumab dans les métastases cérébrales du cancer du sein ; données exploratoires |
| [NCT02152943](https://clinicaltrials.gov/study/NCT02152943) | Phase 1 | Terminé | 37 | Évérolimus + létrozole + trastuzumab dans les cancers HER2-positifs à récepteurs hormonaux positifs |
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | En recrutement | 30 | Nératinib + traitement endocrinien + trastuzumab en préopératoire dans les cancers RE-positifs/HER2-positifs |
| [NCT04334330](https://clinicaltrials.gov/study/NCT04334330) | Phase 2 | Inconnu | 34 | Palbociclib, trastuzumab, pyrotinib et fulvestrant dans les métastases cérébrales RE/RP-positives, HER2-positives ; association confondante |
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Terminé | 517 | Biosimilaire du pertuzumab + trastuzumab + docétaxel dans le cancer du sein HER2-positif RE/RP-négatif |
| [NCT00053339](https://clinicaltrials.gov/study/NCT00053339) | Phase 3 | Retiré | 0 | Trastuzumab avec ou sans tamoxifène dans le cancer du sein de stade IV RE/RP et HER2-positif ; aucun patient inclus, donc aucune preuve |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | ECR (phase 2) | Lancet Oncol | NeoSphere : analyse à 5 ans de la survie sans progression et de la sécurité du pertuzumab + trastuzumab néoadjuvants |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | ECR (phase 2) | Ann Oncol | WSG-ADAPT HER2+/HR- : désescalade avec double blocage trastuzumab/pertuzumab ± paclitaxel |
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | ECR (phase 3) | Lancet Oncol | ExteNET : nératinib après traitement adjuvant à base de trastuzumab |
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | ECR (phase 2) | Lancet Oncol | monarcHER : abémaciclib + trastuzumab ± fulvestrant dans le cancer HR-positif/HER2-positif avancé |
| [29117498](https://pubmed.ncbi.nlm.nih.gov/29117498/) | 2017 | Méta-analyse | N Engl J Med | Risques de récidive à 20 ans après l'arrêt du traitement endocrinien à 5 ans |
| [15894097](https://pubmed.ncbi.nlm.nih.gov/15894097/) | 2005 | Méta-analyse | Lancet | Effets de la chimiothérapie et de l'hormonothérapie sur la récidive et la survie à 15 ans |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | Étude moléculaire | Theranostics | Profils moléculaires et réponse au trastuzumab des cancers triple-positifs (RE+, RP+, HER2+) |
| [21151204](https://pubmed.ncbi.nlm.nih.gov/21151204/) | 2011 | Revue | Nat Rev Clin Oncol | Cancer HER2-positif et à récepteurs hormonaux positifs : cibler la bonne voie |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Revue | Future Oncol | Tendances actuelles du traitement du cancer HR+/HER2+ |
| [40339592](https://pubmed.ncbi.nlm.nih.gov/40339592/) | 2025 | Phase 2a | Lancet Oncol | Zanidatamab + palbociclib + fulvestrant dans le cancer HR-positif/HER2-positif métastatique prétraité |

---

## Informations de Marché en France

Les 16 AMM recensées sont toutes annulées ; aucune n'est actuellement valide. Le texte des indications approuvées n'est pas renseigné dans les données.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61276045 | HERCEPTIN 150 mg | Poudre pour solution à diluer pour perfusion | Non renseignée |
| 62712079 | HERCEPTIN 600 mg | Solution injectable | Non renseignée |
| 68153262 | HERZUMA 420 mg | Poudre pour solution à diluer pour perfusion | Non renseignée |
| 60990496 | OGIVRI 150 mg | Poudre pour solution à diluer pour perfusion | Non renseignée |
| 67178992 | PHESGO 1200 mg/600 mg | Solution injectable | Non renseignée |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (anticorps monoclonal anti-HER2) |
| Risque de Myélosuppression | Faible en monothérapie ; risque accru en association avec une chimiothérapie |
| Classification d'Émétogénicité | Faible |
| Éléments de Surveillance | Fonction cardiaque (FEVG) ; NFS en cas d'association avec une chimiothérapie |
| Protection de Manipulation | Les précautions applicables aux produits antinéoplasiques sont à vérifier dans la notice |

Une publication jointe aux données (PMID 17687157) évoque la cardiotoxicité liée au trastuzumab et la remise en question de sa réversibilité.

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 94 interactions sont recensées. Parmi les principales de niveau majeur : défériprone, samarium (153Sm) lexidronam, adalimumab, baricitinib. Parmi les interactions de niveau modéré : paclitaxel, warfarine, alemtuzumab, azathioprine, anakinra, zidovudine, chloramphénicol.

Veuillez consulter la notice pour les mises en garde et les contre-indications, qui ne sont pas disponibles dans les données compilées.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Des preuves randomisées solides (dont un essai de phase 3 de 3270 patients et plusieurs ECR publiés) soutiennent le trastuzumab dans le cancer du sein HER2-positif, y compris les tumeurs à récepteurs hormonaux positifs. Il s'agit cependant d'un sous-groupe de l'indication d'origine plutôt que d'un véritable repositionnement.
- Le bénéfice est limité aux tumeurs HER2-positives. Les autorisations françaises recensées sont toutes annulées, et les données de sécurité de la notice sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Confirmation obligatoire du statut HER2 avant tout traitement (garde-fou principal)
- Récupération et analyse de la notice (mises en garde et contre-indications), qui bloque l'évaluation de sécurité
- Données détaillées sur le mécanisme d'action
- Clarification du statut réglementaire en France (AMM annulées, produits éventuellement autorisés par procédure centralisée européenne)
- Plan de surveillance cardiaque (FEVG) avant et pendant le traitement

---

### Note sur les autres indications prédites

- **Cancer du sein à récepteur de la progestérone négatif** (score 99,90 %, L1) : même logique de sous-groupe ; Proceed with Guardrails, sous réserve d'un statut HER2-positif.
- **Tumeur mammaire luminale A ou B** (score 99,90 %, L1) : pas d'essai enregistré, mais des preuves randomisées dans la littérature ; seul le sous-groupe luminal B HER2-positif est concerné.
- **Sous-type de type normal du carcinome mammaire** (L4, Hold) : pas de justification mécanistique claire, tumeur généralement HER2-négative.
- **Tumeur cutanée granulaire maligne, ectomésenchymome, tumeur liée à l'HHV-8, tumeur neuroendocrine de l'oreille moyenne** (L5, Hold) : prédictions du modèle uniquement, sans preuve clinique ni bibliographique.
- **Carcinome urothélial sarcomatoïde du bassinet rénal et carcinome urothélial de l'urètre prostatique** (L5, question de recherche) : hypothèse plausible en cas de surexpression de HER2, mais aucune donnée à l'appui.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

