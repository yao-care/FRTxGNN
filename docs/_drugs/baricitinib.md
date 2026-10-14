---
layout: default
title: Baricitinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 90
evidence_level: L5
indication_count: 2
---

# Baricitinib
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Baricitinib : De la Polyarthrite Rhumatoïde au Syndrome de Microphtalmie Colobomateuse-Dysplasie Rhizomélique

## Résumé en Une Phrase

Baricitinib est un inhibiteur de JAK1/JAK2, initialement utilisé pour le traitement de la polyarthrite rhumatoïde.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de microphtalmie colobomateuse-dysplasie rhizomélique**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Polyarthrite rhumatoïde (selon le graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Syndrome de microphtalmie colobomateuse-dysplasie rhizomélique |
| Score de Prédiction TxGNN | 99,94 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Retiré (AMM annulées uniquement) |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le baricitinib est un inhibiteur de JAK1/JAK2 dont l'efficacité dans la polyarthrite rhumatoïde est reconnue ; son action passe par la modulation de la voie JAK-STAT et de la signalisation immunitaire.

Aucun lien mécanistique plausible ne peut être établi entre l'inhibition de JAK-STAT et ce syndrome développemental congénital rare. Un médicament immunomodulateur ne paraît pas intuitivement adapté à une malformation structurelle. Le score élevé (99,94 %) reflète très probablement une proximité dans la topologie du graphe de connaissances (voisins génétiques ou phénotypiques partagés), et non une preuve biologique.

La seconde prédiction du modèle, le **syndrome de brachydactylie-syndactylie** (score de 99,94 %), présente la même limite : aucune preuve clinique ni mécanistique, et un médicament symptomatique immunomodulateur peu susceptible de modifier une pathologie malformative.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61751780 | OLUMIANT 4 mg, comprimé pelliculé (statut : annulée) | Comprimé pelliculé | Non renseignée |
| 63788717 | OLUMIANT 2 mg, comprimé pelliculé (statut : annulée) | Comprimé pelliculé | Non renseignée |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 100 interactions ont été identifiées ; les principales sont :
  - **Majeures** : corticoïdes (hydrocortisone, triamcinolone, bétaméthasone, budésonide, dexaméthasone, prednisolone, prednisone), déférione, ibritumomab tiuxétan, iobenguane (I-131), tositumomab (I-131).
  - **Modérées** : morphine (y compris liposomale), acide acétylsalicylique, nitisinone, opium.
  - **Mineures** : sels de zinc (acétate, gluconate, sulfate).

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication ni lien mécanistique plausible. Les AMM françaises sont toutes annulées et les données de sécurité de la notice sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice (mises en garde et contre-indications) sur le site de l'ANSM, indispensable au dépistage de sécurité
- Données détaillées sur le mécanisme d'action (MOA) via DrugBank
- Démonstration d'un lien biologique entre la voie JAK-STAT et la physiopathologie de ces syndromes (études précliniques ou de mécanisme)
- Évaluation de la compatibilité des voies d'administration et de la similarité avec l'indication d'origine
- Vérification des registres d'essais (ClinicalTrials.gov, ICTRP) et de la littérature pour toute donnée émergente
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

