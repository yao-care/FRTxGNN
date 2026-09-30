---
layout: default
title: Mogamulizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 203
evidence_level: L5
indication_count: 7
---

# Mogamulizumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

# Mogamulizumab : Du Lymphome T Cutané (indication non documentée dans les données) au Carcinome Urothélial de l'Urètre Prostatique

## Résumé en Une Phrase

Le mogamulizumab est un anticorps monoclonal commercialisé en France sous le nom POTELIGEO. Le texte de son indication approuvée n'est pas renseigné dans les données fournies. D'après les connaissances générales, il est utilisé dans certains lymphomes T cutanés.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **carcinome urothélial de l'urètre prostatique**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans le texte d'AMM fourni |
| Nouvelle Indication Prédite | Carcinome urothélial de l'urètre prostatique |
| Score de Prédiction TxGNN | 99,44 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les connaissances générales, le mogamulizumab est un anticorps anti-CCR4 sans fucose. Il élimine les cellules qui portent CCR4, dont les lymphocytes T régulateurs (Treg), par cytotoxicité cellulaire dépendante des anticorps (ADCC).

Le lien hypothétique avec les carcinomes urothéliaux serait l'élimination des Treg dans le microenvironnement tumoral, ce qui pourrait relancer la réponse immunitaire antitumorale. **Ce lien n'est soutenu par aucun essai ni aucune publication dans ce jeu de données.**

Les quatre premières prédictions sont des entités urothéliales (urètre prostatique, bassinet du rein, vessie sarcomatoïde, bassinet papillaire), avec des scores presque identiques (99,37 % à 99,44 %). Cela suggère une prédiction groupée fondée sur la similarité dans le graphe de connaissances, plutôt qu'un signal biologique propre à chaque tumeur. Les trois autres prédictions sont encore plus fragiles :

- **Tumeur liée à l'HHV-8** : le lien reste spéculatif, et l'immunosuppression pourrait accroître le risque infectieux.
- **Ectomésenchymome** : aucun lien plausible avec CCR4 ne peut être établi, et la prédiction est probablement un artefact du graphe.
- **Tumeur cutanée à cellules granuleuses maligne** : seule la localisation cutanée est commune, ce qui n'est pas une biologie partagée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62292771 | POTELIGEO 4 mg/mL, solution à diluer pour perfusion (KYOWA KIRIN HOLDINGS, Pays-Bas) | Solution à diluer pour perfusion | Non renseignée dans les données |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Immunothérapie (anticorps monoclonal anti-CCR4, d'après les connaissances générales) |

Veuillez consulter les mises en garde et précautions de la notice pour le risque de myélosuppression, l'émétogénicité, les paramètres de surveillance et les mesures de manipulation.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (L5), sans essai clinique ni publication. Le mécanisme d'action et les données de sécurité de la notice ANSM manquent aussi, ce qui bloque l'évaluation de sécurité initiale.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications), puis compléter l'indication approuvée.
- Compléter le mécanisme d'action via DrugBank.
- Faire une recherche bibliographique ciblée sur l'expression de CCR4 et la présence de Treg dans les carcinomes urothéliaux.
- Rechercher des études précliniques ou des essais enregistrés (ClinicalTrials.gov, ICTRP) avant tout passage à une évaluation plus poussée.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

