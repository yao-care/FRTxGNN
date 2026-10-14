---
layout: default
title: Cetuximab
parent: Prédiction du modèle uniquement (L5)
nav_order: 159
evidence_level: L5
indication_count: 10
---

# Cetuximab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Cétuximab : Du Cancer du Côlon à la Tumeur Bronchique Carcinoïde de l'Enfant

## Résumé en Une Phrase

Le cétuximab est un anticorps monoclonal dirigé contre le récepteur de l'EGFR, initialement utilisé pour le traitement du cancer colorectal et des carcinomes épidermoïdes de la tête et du cou.
Le modèle TxGNN prédit qu'il pourrait être efficace pour les **adénomes/carcinoïdes bronchiques de l'enfant**, avec un score très élevé (99,95 %).
En revanche, **aucun essai clinique ni aucune publication** ne soutient actuellement cette prédiction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer colorectal / néoplasme malin du côlon (selon le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Adénomes/carcinoïdes bronchiques de l'enfant |
| Score de Prédiction TxGNN | 99,95 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le cétuximab est un anticorps qui bloque l'EGFR (récepteur du facteur de croissance épidermique). Son efficacité a été établie dans le cancer colorectal exprimant l'EGFR et dans les carcinomes épidermoïdes de la tête et du cou.

Rien dans les données ne montre que la signalisation EGFR soit un moteur des carcinoïdes bronchiques pédiatriques. Le lien mécanistique n'est donc pas étayé, et la similarité avec l'indication d'origine n'a pas été évaluée. Le score élevé du modèle reflète une association statistique dans le graphe de connaissances, pas une preuve biologique ou clinique.

**Autres indications prédites (à titre de contexte)** : le modèle a produit plusieurs prédictions avec des scores quasi identiques. Deux d'entre elles disposent de preuves plus substantielles que la première et méritent d'être examinées en priorité :
- **Néoplasme prémalin** (niveau L2) : un essai de phase 2 terminé (NCT00524017) évalue le cétuximab en monothérapie dans des lésions prémalignes des voies aéro-digestives supérieures, avec un rationnel de chimioprévention (surexpression de l'EGFR dans ces lésions).
- **Néoplasme kystique** (niveau L2) : une étude de phase II dans les carcinomes des glandes salivaires et un essai de phase I/II dans le carcinome adénoïde kystique (NCT01192087). Les données sont précoces, sans signal d'efficacité clair.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour la nouvelle indication prédite principale (adénomes/carcinoïdes bronchiques de l'enfant).

Pour information, essais relatifs aux deux indications prédites les mieux documentées :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00524017](https://clinicaltrials.gov/study/NCT00524017) | Phase 2 | Terminé | 35 | Cétuximab en monothérapie dans des lésions prémalignes des voies aéro-digestives supérieures à haut risque (prémalin) ; résultats d'efficacité non fournis |
| [NCT01192087](https://clinicaltrials.gov/study/NCT01192087) | Phase 1/2 | Inconnu | 49 | Cétuximab + IMRT + boost d'ions carbone dans le carcinome adénoïde kystique (néoplasme kystique) ; étude de faisabilité/toxicité |
| [NCT00397384](https://clinicaltrials.gov/study/NCT00397384) | Phase 1 | Terminé | 43 | Erlotinib + cétuximab dans des cancers avancés ; sécurité du double blocage de l'EGFR, spécificité limitée (néoplasme kystique) |
| [NCT00101348](https://clinicaltrials.gov/study/NCT00101348) | Phase 1/2 | Terminé | 66 | Erlotinib, cétuximab ± bévacizumab dans des tumeurs solides ; population non spécifique (néoplasme kystique) |
| [NCT01637194](https://clinicaltrials.gov/study/NCT01637194) | Phase 1 | Terminé | 12 | Cétuximab + évérolimus dans des tumeurs solides ; petit effectif (néoplasme kystique) |
| [NCT00482222](https://clinicaltrials.gov/study/NCT00482222) | Phase 3 | Inconnu | 340 | Chimiothérapie à base d'oxaliplatine ± cétuximab dans les métastases hépatiques colorectales résécables ; ne concerne pas les lésions prémalignes |

---

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement pour la nouvelle indication prédite principale. Publications relatives aux indications prédites les mieux documentées :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [18804410](https://pubmed.ncbi.nlm.nih.gov/18804410/) | 2009 | Essai de phase II | Oral Oncology | Cétuximab dans les carcinomes des glandes salivaires récurrents/métastatiques (30 patients, dont 23 carcinomes adénoïdes kystiques), critère : bénéfice clinique ≥ 6 mois |
| [24412287](https://pubmed.ncbi.nlm.nih.gov/24412287/) | 2014 | Revue | Oral Oncology | Ciblage de l'EGFR pour la chimioprévention des cancers de la tête et du cou ; surexpression de l'EGFR dans les lésions orales prémalignes |
| [33243986](https://pubmed.ncbi.nlm.nih.gov/33243986/) | 2020 | Revue | Nature Reviews Disease Primers | Vue d'ensemble des carcinomes épidermoïdes de la tête et du cou |
| [35300246](https://pubmed.ncbi.nlm.nih.gov/35300246/) | 2022 | Essai de phase II randomisé | Clin Transl Radiat Oncol | Cétuximab, gemcitabine et radiothérapie dans le cancer du pancréas localement avancé (résultats à long terme, essai PARC) ; concerne la prolifération canalaire |
| [41546361](https://pubmed.ncbi.nlm.nih.gov/41546361/) | 2025 | Rapport de cas | Gan to Kagaku Ryoho | Carcinome intra-osseux primitif sur kyste odontogène de la mandibule |
| [30576676](https://pubmed.ncbi.nlm.nih.gov/30576676/) | 2019 | Rapport de cas | J Oral Maxillofac Surg | Régression d'une métastase médiastinale de carcinome intra-osseux primitif sous nivolumab |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66843357 | ERBITUX 5 mg/ml, solution pour perfusion (MERCK KGAA, Allemagne) | Solution pour perfusion | Non renseignée (AMM annulée) |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (anticorps monoclonal anti-EGFR) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter la notice ; la littérature signale des réactions cutanées fréquentes et des réactions graves à la perfusion |
| Protection de Manipulation | Veuillez consulter la notice |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 20 interactions ont été recensées. Les principales :
  - **Majeures** : acide aminolévulinique, thalidomide.
  - **Modérées** : inhibiteurs de la pompe à protons (rabéprazole, oméprazole, dexlansoprazole, ésoméprazole, lansoprazole, pantoprazole), méthoxsalène, acide aminolévulinique topique, capécitabine, carboplatine, cisplatine, fluorouracile, idélalisib, aminolévulinate de méthyle topique, omacétaxine, oxaliplatine, vertéporfine.
- **Réactions à la perfusion** : la littérature fournie mentionne que le cétuximab peut provoquer des réactions graves à la perfusion (rapport de cas, PMID 39415301).

Les mises en garde et contre-indications de la notice ne sont pas disponibles dans les données compilées : veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction principale (adénomes/carcinoïdes bronchiques de l'enfant) repose uniquement sur le score du modèle (niveau L5), sans essai ni publication, et sans lien mécanistique démontré. Par ailleurs, la seule AMM française recensée est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde et contre-indications), car l'absence de ces données bloque le criblage de sécurité.
- Obtenir les données sur le mécanisme d'action depuis DrugBank.
- Établir un lien biologique entre l'EGFR et les carcinoïdes bronchiques pédiatriques (expression de l'EGFR, études précliniques).
- Envisager de prioriser les indications mieux documentées (lésions prémalignes des voies aéro-digestives supérieures, tumeurs des glandes salivaires/carcinome adénoïde kystique), en obtenant les résultats d'efficacité des essais NCT00524017 et NCT01192087.
- Clarifier la situation réglementaire en France (AMM annulée) et la disponibilité réelle du produit.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

