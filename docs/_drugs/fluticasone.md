---
layout: default
title: Fluticasone
parent: Prédiction du modèle uniquement (L5)
nav_order: 342
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Fluticasone : nouvelle indication prédite, Migraine (migraine disorder) (niveau de preuve L5). Indication d'origine : Non précisée dans les données compilées (les textes d'indication des…"
---

# Fluticasone
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

# Fluticasone : D'un corticoïde inhalé/nasal à la migraine (prédiction à très faible niveau de preuve)

## Résumé en Une Phrase

Fluticasone est un corticoïde (glucocorticoïde) utilisé par voie nasale, inhalée et cutanée, commercialisé notamment sous les noms Flixonase, Flixotide et Avamys.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **migraine**, avec un score élevé, mais **aucun essai clinique** et **une seule publication** (qui traite d'effets indésirables, non d'efficacité) sont associés à cette prédiction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données compilées (les textes d'indication des AMM sont vides) |
| Nouvelle Indication Prédite | Migraine (*migraine disorder*) |
| Score de Prédiction TxGNN | 99,20 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les connaissances générales, la fluticasone est un glucocorticoïde à action anti-inflammatoire locale, administré par voie nasale, inhalée ou cutanée. Les données compilées ne permettent pas d'en tirer une indication d'origine officielle.

Un lien hypothétique existe : l'inflammation neurogène participe à la physiopathologie de la migraine, et un anti-inflammatoire pourrait théoriquement agir sur ce processus. Il s'agit toutefois d'une **hypothèse spéculative** : aucun mécanisme crédible n'est établi.

La seule publication retrouvée porte sur les troubles neuropsychiatriques associés aux corticoïdes intranasaux. Elle concerne la sécurité, non l'efficacité, et suggère plutôt un risque d'effets indésirables neurologiques qu'un bénéfice. Le score élevé du modèle peut refléter une proximité dans le graphe de connaissances plutôt qu'une relation pharmacologique réelle.

Deux autres prédictions de score comparable (angor de Prinzmetal, 99,19 % ; migraine avec aura du tronc cérébral, 99,09 %) ne reposent sur aucune étude. La seconde est un sous-type de la migraine et reflète probablement la même prédiction. Aucun lien plausible n'est établi pour l'angor de Prinzmetal.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [18681087](https://pubmed.ncbi.nlm.nih.gov/18681087/) | 2008 | Revue | Annals of Allergy, Asthma & Immunology | Analyse des signalements de pharmacovigilance de l'OMS : grappe de cas de troubles neuropsychiatriques lors de l'usage de corticoïdes intranasaux. Étude de sécurité, sans démonstration d'efficacité dans la migraine |

---

## Informations de Marché en France

Les 20 AMM recensées sont annulées. Les textes d'indication ne sont pas renseignés. Les cinq premières sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61748649 | Flixonase 50 µg/dose, suspension nasale en flacon pulvérisateur avec pompe doseuse | Suspension | Non renseignée |
| 62933355 | Flixotide 125 µg/dose, suspension pour inhalation en flacon pressurisé | Suspension pour inhalation | Non renseignée |
| 63872528 | Flixovate 0,005 %, pommade | Pommade | Non renseignée |
| 65156075 | Flixotide Diskus 500 µg/dose, poudre pour inhalation en récipient unidose | Poudre pour inhalation | Non renseignée |
| 60564219 | Fixorinox 50 µg/dose, suspension pour pulvérisation nasale | Suspension pour pulvérisation | Non renseignée |

---

## Considérations de Sécurité

- **Interactions médicamenteuses** : 474 interactions recensées. Parmi les principales :
  - **Majeure** : clarithromycine.
  - **Modérées** : aprépitant, insuline humaine inhalée (action rapide).
  - Plusieurs autres interactions (par ex. prednisone, triamcinolone, simvastatine, oméprazole) sont de niveau non précisé.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur un score du modèle (niveau L5), sans essai clinique ni preuve d'efficacité. La seule publication disponible évoque plutôt un risque neuropsychiatrique. De plus, toutes les AMM françaises sont annulées et les données de sécurité de la notice sont absentes (blocage pour le dépistage de sécurité).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice ANSM (mises en garde, contre-indications, indications d'origine).
- Données détaillées sur le mécanisme d'action (DrugBank).
- Recherche de preuves précliniques ou observationnelles reliant la fluticasone à la migraine.
- Évaluation de la compatibilité de la voie d'administration avec la migraine.
- Clarification du statut réglementaire actuel (AMM annulées).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

