---
layout: default
title: Ramucirumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 258
evidence_level: L5
indication_count: 10
---

# Ramucirumab
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

# Ramucirumab : Du Cancer Gastrique à l'Adénocarcinome du Ligament Utérin

## Résumé en Une Phrase

Ramucirumab est un anticorps monoclonal antagoniste du VEGFR2, indiqué à l'origine dans l'adénocarcinome gastrique et de la jonction gastro-œsophagienne (d'après l'analyse de rationalité du dossier, le texte d'indication de l'AMM étant vide).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**adénocarcinome du ligament utérin**, avec un score élevé mais **aucun essai clinique** et **aucune publication** dans les données fournies.
Cette prédiction reste donc purement algorithmique à ce stade.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Adénocarcinome gastrique et de la jonction gastro-œsophagienne (d'après l'analyse de rationalité ; non renseigné dans l'AMM) |
| Nouvelle Indication Prédite | Adénocarcinome du ligament utérin |
| Score de Prédiction TxGNN | 99,95 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base. Sur la base des informations connues, ramucirumab est un antagoniste du récepteur VEGFR2, et le blocage de cette voie limite l'angiogenèse tumorale. Un traitement anti-angiogénique est plausible dans les adénocarcinomes de l'appareil génital féminin.

Les autres prédictions du modèle se concentrent aussi sur des cancers gynécologiques, en particulier du col utérin (carcinome endocervical, carcinome adénoïde kystique du col, etc.). Pour le carcinome endocervical, l'anticorps anti-VEGF bevacizumab a déjà un rôle connu dans le cancer du col, ce qui donne une plausibilité biologique au blocage de la voie VEGF/VEGFR2.

Cependant, le ligament utérin est un site tumoral rare. Aucun essai ni publication spécifique au ramucirumab n'a été fourni pour cette indication. Le seul appui est le score de prédiction (0,9995), qui n'est pas une preuve clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63848228 | CYRAMZA 10 mg/ml, solution à diluer pour perfusion | Solution à diluer pour perfusion | Non renseignée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (anticorps monoclonal anti-VEGFR2) |

Veuillez consulter les mises en garde et précautions de la notice pour le risque de myélosuppression, l'émétogénicité, les paramètres de surveillance et les mesures de protection lors de la manipulation.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score TxGNN (niveau L5), sans essai clinique ni publication. Les données de sécurité de l'ANSM sont également manquantes, ce qui empêche toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération de la notice ANSM (mises en garde, contre-indications, indication approuvée) : lacune bloquante
- Données détaillées sur le mécanisme d'action (MOA), à obtenir via DrugBank
- Recherche d'essais cliniques et de littérature spécifiques au ramucirumab dans les cancers gynécologiques, en priorité le col utérin, où le rationnel anti-VEGF est le mieux étayé
- Évaluation de la compatibilité des voies d'administration et de la similarité avec l'indication originale, aujourd'hui en attente

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement nécessite une validation clinique avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

