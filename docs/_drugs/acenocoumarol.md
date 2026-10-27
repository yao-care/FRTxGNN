---
layout: default
title: Acenocoumarol
parent: Prédiction du modèle uniquement (L5)
nav_order: 17
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Acenocoumarol : nouvelle indication prédite, Déficit en cofacteur II de l'héparine (niveau de preuve L5). Indication d'origine : Embolie pulmonaire, thrombophilie"
monitor_inn: "acenocoumarol"
predicted_indications: ["heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2"]
---

# Acenocoumarol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

## Acénocoumarol : De l'Embolie Pulmonaire et la Thrombophilie au Déficit en Cofacteur II de l'Héparine
{: .text-alpha }

## Résumé en Une Phrase

L'acénocoumarol est un anticoagulant antagoniste de la vitamine K, initialement utilisé pour l'embolie pulmonaire et la thrombophilie.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **déficit en cofacteur II de l'héparine**,
mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Embolie pulmonaire, thrombophilie (d'après le graphe de connaissances ; aucun texte d'indication n'est disponible dans les AMM) |
| Nouvelle Indication Prédite | Déficit en cofacteur II de l'héparine |
| Score de Prédiction TxGNN | 99,84 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement annulé (aucune AMM valide) |
| Nombre d'AMM | 2 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, l'acénocoumarol fait partie des antagonistes de la vitamine K : il inhibe VKORC1 et réduit la synthèse des facteurs de coagulation vitamine K-dépendants (II, VII, IX, X).

Le déficit en cofacteur II de l'héparine est une thrombophilie héréditaire, dans laquelle la capacité d'inhiber la thrombine est diminuée. Cette parenté avec l'indication originale (thrombophilie, embolie pulmonaire) rend plausible l'intérêt d'une anticoagulation pour prévenir la thrombose.

Ce lien repose uniquement sur le phénotype thrombotique commun. Aucune donnée spécifique à la maladie n'a été fournie, et le score élevé du modèle est une prédiction, non une preuve clinique.

Deux autres prédictions de même nature figurent dans les données : le **facteur V en excès avec thrombose spontanée** (99,78 %) et le **déficit en antithrombine de type 2** (99,77 %). Elles sont également de niveau L5, sans essai ni publication, et relèvent de la recommandation Hold.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61510352 | SINTROM 4 mg, comprimé quadrisécable | Comprimé quadrisécable | Non renseignée (AMM annulée) |
| 62148714 | MINI-SINTROM 1 mg, comprimé | Comprimé | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 117 interactions connues ont été recensées. Les niveaux de gravité ne sont pas précisés. Parmi les médicaments concernés :
  - inhibiteurs de la pompe à protons : oméprazole, pantoprazole, lansoprazole ;
  - corticoïdes : prednisone, prednisolone, hydrocortisone, dexaméthasone, budésonide ;
  - acide acétylsalicylique ;
  - métronidazole ;
  - statines : simvastatine, rosuvastatine ;
  - metformine, morphine, vancomycine, calcitriol.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les trois indications prédites reposent uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Le médicament n'a plus d'AMM valide en France, et les données de sécurité de la notice sont absentes, ce qui bloque l'étape de sélection de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications) ;
- Obtenir les données de mécanisme d'action depuis DrugBank ;
- Rechercher des essais cliniques et des publications spécifiques au déficit en cofacteur II de l'héparine ;
- Clarifier la situation réglementaire (AMM annulées) et la disponibilité d'une voie d'administration ;
- Évaluer la gravité des 117 interactions médicamenteuses.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

