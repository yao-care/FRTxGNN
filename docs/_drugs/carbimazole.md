---
layout: default
title: Carbimazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 71
evidence_level: L5
indication_count: 3
---

# Carbimazole
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

# Carbimazole : De l'hyperthyroïdie à la résistance aux hormones thyroïdiennes (mutation THRB)

## Résumé en Une Phrase

Le carbimazole est un antithyroïdien de synthèse (prodrogue du méthimazole), utilisé classiquement contre l'hyperthyroïdie. Les AMM françaises ne renseignent toutefois aucun texte d'indication.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **résistance aux hormones thyroïdiennes due à une mutation du récepteur bêta (THRB)**, avec un score élevé. Il n'existe cependant **aucun essai clinique** et **1 seule publication** (un cas clinique), ce qui rend cette piste peu crédible.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM (usage classique : hyperthyroïdie) |
| Nouvelle Indication Prédite | Résistance aux hormones thyroïdiennes due à une mutation du récepteur bêta des hormones thyroïdiennes |
| Score de Prédiction TxGNN | 99,71 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, le carbimazole est une prodrogue du méthimazole. Il inhibe la thyroperoxydase et réduit ainsi la synthèse des hormones thyroïdiennes.

Ce mécanisme est cohérent avec l'hyperthyroïdie, où la glande produit trop d'hormones. Dans la résistance aux hormones thyroïdiennes liée à THRB, le défaut se situe au niveau du **récepteur** : T4 et T3 circulantes sont déjà élevées de façon compensatrice et la TSH n'est pas freinée. Bloquer la synthèse hormonale augmenterait probablement encore la TSH. Cela exposerait à un goitre et à une hypothyroïdie iatrogène.

Le score élevé (99,71 %) reflète donc vraisemblablement une proximité dans le graphe de connaissances, due à un phénotype commun d'hyperthyroxinémie. Il ne traduit pas une logique thérapeutique. Cette prédiction doit être considérée comme un artefact probable du modèle.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/) | 2013 | Revue (classification automatique ; publication de type cas clinique) | BMJ Case Reports | Homme jeune avec T4 libre élevée (jusqu'à 36,9 pmol/L) et TSH non freinée (6,78 à 22,1 mUI/L), traité de façon intermittente par carbimazole pendant 10 ans sous un diagnostic d'hyperthyroïdie, avec un goitre ferme. Ce cas illustre la difficulté diagnostique et non un bénéfice thérapeutique. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61451683 | NEO-MERCAZOLE 20 mg, comprimé (AMDIPHARM) | Comprimé | Non renseignée dans les données |
| 63839179 | NEO-MERCAZOLE 5 mg, comprimé (AMDIPHARM) | Comprimé | Non renseignée dans les données |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Cette prédiction repose uniquement sur le modèle (L5). Elle ne s'appuie sur aucun essai et sur un seul cas clinique, qui ne démontre aucun bénéfice.
- Le mécanisme est contraire à la physiopathologie : le défaut est au niveau du récepteur, et freiner la synthèse hormonale risque d'aggraver la stimulation par la TSH.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour tout criblage de sécurité)
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Le texte des indications approuvées des deux AMM
- Des données pharmacologiques ou cliniques directes sur le carbimazole dans la résistance aux hormones thyroïdiennes, actuellement inexistantes

**À noter :** pour ce même médicament, le modèle propose deux autres indications mieux étayées. La **thyrotoxicose néonatale** (niveau L3, 19 publications observationnelles, recommandation « Proceed with Guardrails ») est mécanistiquement cohérente. L'**hyperthyroxinémie** relève du niveau L4 et d'une simple question de recherche. Elles méritent un rapport dédié, plus prioritaire que celui-ci.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

