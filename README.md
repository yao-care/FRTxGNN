# FRTxGNN - France : Repositionnement de Medicaments

[![Website](https://img.shields.io/badge/Website-frtxgnn.yao.care-blue)](https://frtxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Predictions de repositionnement de medicaments (drug repurposing) pour la France en utilisant le modele TxGNN.

## Avertissement

- Les resultats de ce projet sont uniquement a des fins de recherche et ne constituent pas un avis medical.
- Les candidats au repositionnement de medicaments necessitent une validation clinique avant application.

## Apercu du Projet

| Element | Nombre |
|---------|--------|
| **Rapports de Medicaments** | 315 |
| **Predictions Totales** | 7,046,174 |

## Methodes de Prediction

### Methode par Graphe de Connaissances (Knowledge Graph)
Interrogation directe des relations medicament-maladie dans le graphe de connaissances TxGNN, identifiant les candidats potentiels au repositionnement bases sur les connexions existantes dans le reseau biomedical.

### Methode par Apprentissage Profond (Deep Learning)
Utilise le modele de reseau neuronal pre-entraine TxGNN pour calculer les scores de prediction, evaluant la probabilite de nouvelles indications therapeutiques pour les medicaments approuves.

## Liens

- Site Web : https://frtxgnn.yao.care
- Article TxGNN : https://doi.org/10.1038/s41591-023-02233-x
