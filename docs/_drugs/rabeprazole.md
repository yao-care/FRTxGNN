---
layout: default
title: Rabeprazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 645
evidence_level: L5
indication_count: 2
---

# Rabeprazole
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

# Rabéprazole : Des Maladies Acido-Peptiques à la Mastocytose Systémique Indolente (Smouldering)

## Résumé en Une Phrase

Le rabéprazole est un inhibiteur de la pompe à protons, initialement utilisé pour traiter l'ulcère gastroduodénal, le reflux gastro-œsophagien et le syndrome de Zollinger-Ellison.
Le modèle TxGNN prédit qu'il pourrait être utile dans la **mastocytose systémique indolente (smouldering)**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette prédiction.
Les données compilées pour ce rapport indiquent par ailleurs que la mastocytose figure déjà parmi les indications d'origine du médicament dans le graphe de connaissances.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie ulcéreuse gastroduodénale, reflux gastro-œsophagien, œsophagite, ulcère duodénal, syndrome de Zollinger-Ellison (selon le graphe de connaissances ; aucun texte d'indication n'est disponible dans les AMM) |
| Nouvelle Indication Prédite | Mastocytose systémique indolente (smouldering) |
| Score de Prédiction TxGNN | 99,44 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Annulé uniquement (aucune AMM valide) |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le rabéprazole appartient à la classe des inhibiteurs de la pompe à protons (IPP), qui réduisent la sécrétion d'acide gastrique. Son efficacité dans les pathologies acido-dépendantes est établie.

Dans la mastocytose, les mastocytes libèrent de l'histamine, qui stimule les récepteurs H2 des cellules pariétales et peut provoquer une hypersécrétion acide et des symptômes digestifs. Un IPP pourrait donc soulager ces manifestations. Il s'agirait d'un contrôle symptomatique : on n'attend pas d'effet sur la charge mastocytaire, la prolifération liée à KIT ni la progression de la maladie.

Point important : la mastocytose systémique et la mastocytose figurent déjà parmi les indications d'origine du rabéprazole dans le graphe de connaissances. La forme « smouldering » est vraisemblablement un sous-type d'une indication existante, et non une véritable nouvelle opportunité de repositionnement. Le score élevé reflète probablement la proximité dans le graphe.

Une seconde prédiction, la mastocytose lymphadénopathique avec éosinophilie (score 99,35 %), repose sur le même raisonnement, mais sans mécanisme connu agissant sur la lymphadénopathie, l'éosinophilie ou le processus hématologique clonal sous-jacent. Elle est également de niveau L5 et en statut Hold.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les 20 AMM recensées sont toutes annulées. Aucun texte d'indication approuvée n'est disponible. Principales AMM :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66035518 | PARIET 10 mg (Janssen Cilag) | Comprimé gastro-résistant | Non renseignée |
| 62909137 | PARIET 20 mg (Janssen Cilag) | Comprimé gastro-résistant | Non renseignée |
| 64710550 | RABEPRAZOLE KRKA 10 mg | Comprimé gastro-résistant | Non renseignée |
| 64546663 | RABEPRAZOLE KRKA 20 mg | Comprimé gastro-résistant | Non renseignée |
| 66787677 | RABEPRAZOLE VIATRIS 10 mg | Comprimé gastro-résistant | Non renseignée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie hépatique, maladie de la vésicule biliaire, ostéoporose, ostéoporose post-ménopausique, fracture osseuse.
- **Interactions médicamenteuses** : 486 interactions recensées. Parmi les exemples :
  - **Majeures** : acalabrutinib, atazanavir.
  - **Modérées** : amikacine, amphotéricine B (plusieurs formes), amphétamine, apalutamide, aprépitant, armodafinil, bosutinib, bendroflumethiazide.
  - **Mineures** : acide acétylsalicylique, axitinib.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication. Le bénéfice plausible se limite à un contrôle symptomatique de l'hypersécrétion acide, et l'indication semble déjà couverte par les indications d'origine du graphe.
- Les AMM françaises sont toutes annulées et les données de sécurité issues de la notice sont absentes (lacune bloquante).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice (mises en garde et contre-indications) auprès de l'ANSM
- Obtenir les données sur le mécanisme d'action via DrugBank
- Rechercher des essais cliniques ou des publications sur les IPP dans la mastocytose
- Vérifier si l'indication « smouldering » apporte une valeur au-delà de l'indication existante de mastocytose
- Clarifier la situation réglementaire (annulation des AMM) et la disponibilité réelle du produit en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

