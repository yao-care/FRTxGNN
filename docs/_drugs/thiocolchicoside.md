---
layout: default
title: Thiocolchicoside
parent: Prédiction du modèle uniquement (L5)
nav_order: 753
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Thiocolchicoside : nouvelle indication prédite, Insomnie (niveau de preuve L5). Indication d'origine : Non précisée dans les données compilées"
monitor_inn: "THIOCOLCHICOSIDE"
predicted_indications: ["insomnia (disease)", "alcohol withdrawal delirium"]
---

# Thiocolchicoside
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Thiocolchicoside : D'un myorelaxant à l'insomnie, une prédiction non étayée

## Résumé en Une Phrase

Le thiocolchicoside est un dérivé semi-synthétique de la colchicoside, commercialisé en France sous forme de comprimés, gélules et solution injectable. Les données compilées pour ce rapport ne précisent pas son indication d'origine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**insomnie**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données compilées |
| Nouvelle Indication Prédite | Insomnie |
| Score de Prédiction TxGNN | 99,89 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Toutes les AMM sont annulées |
| Nombre d'AMM | 9 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances pharmacologiques disponibles, le thiocolchicoside agirait comme antagoniste compétitif des récepteurs GABA-A et, selon certains rapports, des récepteurs de la glycine.

Cette pharmacologie va **à l'opposé** de l'effet sédatif-hypnotique des modulateurs positifs du GABA-A. L'antagonisme GABA-A est associé à des effets convulsivants et pro-excitateurs. Le score élevé du modèle (99,89 %) est donc une simple prédiction issue d'un graphe de connaissances, sans mécanisme plausible, et la direction mécanistique est contradictoire.

Un éventuel bénéfice ne pourrait être qu'indirect, par exemple par le soulagement des spasmes musculaires et de la douleur qui perturbent le sommeil. Cette hypothèse reste spéculative.

**Autre prédiction du modèle : le delirium de sevrage alcoolique** (score de 99,21 %). Le traitement standard repose sur des agonistes GABA-A (benzodiazépines). L'antagonisme GABA-A du thiocolchicoside risquerait d'aggraver l'hyperexcitabilité du système nerveux central et le risque de convulsions, déjà majeur lors du sevrage alcoolique. Cette piste est sans aucun appui clinique ni bibliographique, et le raisonnement mécanistique laisse craindre un préjudice potentiel.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement.

---

## Informations de Marché en France

Les 9 AMM recensées sont toutes annulées. Le texte des indications approuvées n'est pas renseigné dans les données compilées. Les 5 premières sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 69999429 | THIOCOLCHICOSIDE EG 4 mg | Comprimé sécable | Annulée |
| 63646098 | THIOCOLCHICOSIDE ZENTIVA 4 mg | Comprimé | Annulée |
| 68086109 | THIOCOLCHICOSIDE CRISTERS 4 mg | Comprimé | Annulée |
| 65617572 | MIOREL 4 mg | Gélule | Annulée |
| 66305209 | MIOREL 4 mg/2 ml | Solution injectable (IM) en ampoule | Annulée |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

À titre d'alerte, les données précliniques et de pharmacovigilance indiquent un potentiel pro-convulsivant du thiocolchicoside, ce qui plaide contre son utilisation dans les contextes à risque d'hyperexcitabilité du système nerveux central, comme le sevrage alcoolique.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les deux prédictions reposent uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Le mécanisme connu (antagonisme GABA-A) contredit l'effet recherché dans l'insomnie et suggère un risque dans le delirium de sevrage alcoolique.
- Toutes les AMM françaises sont annulées, et les données de sécurité issues de la notice font défaut.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse des notices ANSM (mises en garde et contre-indications), étape bloquante pour tout criblage de sécurité
- Données détaillées sur le mécanisme d'action (via DrugBank)
- Clarification de l'indication d'origine et des raisons de l'annulation des AMM
- Études précliniques ou cliniques justifiant un bénéfice réel dans l'insomnie, avec évaluation du risque convulsivant
- Aucune poursuite n'est recommandée pour le delirium de sevrage alcoolique en l'état, compte tenu du risque mécanistique
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

