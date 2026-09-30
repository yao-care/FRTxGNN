---
layout: default
title: Fulvestrant
parent: Prédiction du modèle uniquement (L5)
nav_order: 137
evidence_level: L5
indication_count: 10
---

# Fulvestrant
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

# Fulvestrant : De l'indication d'origine (non renseignée) au VIH

## Résumé en Une Phrase

Fulvestrant est un médicament injectable commercialisé en France, dont l'indication d'origine n'est pas renseignée dans les données fournies.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infection par le VIH**, avec un score élevé (99,91 %).
Cette prédiction repose uniquement sur le modèle : **0 essai clinique** et **1 publication**, qui porte sur un autre virus (HTLV-1) et ne la soutient donc pas.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée (aucun texte d'indication dans les AMM ni dans les données du médicament) |
| Nouvelle Indication Prédite | Infection par le VIH (HIV infectious disease) |
| Score de Prédiction TxGNN | 99,91 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 10 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Les essais cliniques d'autres indications du dossier décrivent le fulvestrant comme un antagoniste et dégradeur des récepteurs des œstrogènes (SERD) utilisé en hormonothérapie. Sur la base de ces informations seulement, on ne peut pas conclure que ce mécanisme soit applicable au VIH.

Les données fournies ne soutiennent aucun lien plausible entre l'antagonisme du récepteur des œstrogènes et l'infection par le VIH. La seule publication associée concerne la myélopathie liée à HTLV-1, un rétrovirus différent, et ne peut pas servir de preuve pour le VIH.

Le score élevé reflète probablement la proximité du VIH dans le graphe de connaissances (maladies virales, rétrovirus) plutôt qu'un signal biologique indépendant. Les prédictions « infection par le SIV » et « SIDA félin » présentent exactement le même score (99,83 %), ce qui va dans le même sens. Cette prédiction doit donc être considérée comme une hypothèse non étayée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Cohorte / analyse multi-omique (HTLV-1, pas VIH) | Research Square | Analyse de biologie des systèmes de la myélopathie associée à HTLV-1 (HAM), qui identifie des mécanismes de la maladie et des cibles thérapeutiques. Cette étude ne concerne ni le VIH ni le fulvestrant. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 60446306 | FULVESTRANT EG 250 mg, solution injectable en seringue préremplie | Solution injectable | EG LABO - Laboratoires Eurogenerics |
| 66475706 | FULVESTRANT ARROW 250 mg, solution injectable en seringue pré-remplie | Solution injectable | Eugia Pharma (Malta) (Malte) |
| 69289895 | FULVESTRANT MYLAN 250 mg, solution injectable en seringue préremplie | Solution injectable | Mylan Pharmaceuticals (Irlande) |
| 63545028 | FASLODEX 250 mg, solution injectable | Solution injectable | AstraZeneca AB |
| 62062457 | FULVESTRANT SANDOZ 250 mg, solution injectable en seringue pré-remplie | Solution injectable | Sandoz |

Le texte de l'indication approuvée n'est pas renseigné pour ces AMM. Le dossier compte 10 AMM au total, dont les 5 principales sont listées ici.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5) : aucun essai clinique, et la seule publication concerne HTLV-1 et non le VIH. Aucun mécanisme plausible ne relie l'antagonisme du récepteur des œstrogènes au VIH.
- Les données de sécurité de la notice ANSM sont absentes. Cette lacune bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications, interactions).
- Obtenir les données de mécanisme d'action (MOA) via DrugBank.
- Renseigner l'indication d'origine à partir des textes d'AMM ou du RCP.
- Rechercher des données précliniques ou cliniques spécifiques au VIH et au fulvestrant. Sans elles, cette piste ne devrait pas progresser.
- Pour information, parmi les autres prédictions, seule la polyarthrite rhumatoïde (L4, statut « Research Question ») repose sur des données précliniques via la signalisation des œstrogènes. Son sens d'effet reste ambigu et aucun essai avec le fulvestrant n'est fourni.

*Ce rapport est fourni à titre de référence pour la recherche et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

