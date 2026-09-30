---
layout: default
title: Lamotrigine
parent: Prédiction du modèle uniquement (L5)
nav_order: 168
evidence_level: L5
indication_count: 9
---

# Lamotrigine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

# Lamotrigine : De l'Épilepsie au Néoplasme du Nerf Trijumeau

## Résumé en Une Phrase

La lamotrigine est un antiépileptique utilisé dans les crises d'épilepsie et les troubles bipolaires, d'après la littérature associée. Les textes d'indication des AMM ne sont pas renseignés dans le dossier.
Le modèle TxGNN prédit qu'elle pourrait être utile pour le **néoplasme du nerf trijumeau**, mais **aucun essai clinique** et seulement **2 publications** sont associés à cette prédiction. Ces deux publications portent sur la névralgie du trijumeau, non sur la tumeur.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les textes d'AMM (la littérature associée mentionne l'épilepsie et le trouble bipolaire) |
| Nouvelle Indication Prédite | Néoplasme du nerf trijumeau |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. La lamotrigine est un antiépileptique. On lui attribue en général un blocage des canaux sodiques voltage-dépendants et une réduction de la libération de glutamate. Ce mécanisme n'est pas documenté dans le champ MOA du dossier.

Ce mécanisme ne suggère aucune activité antitumorale. Le score élevé du modèle reflète plus probablement la proximité avec la **névralgie du trijumeau**, une douleur faciale paroxystique, que l'effet sur une tumeur. Les deux publications retrouvées portent sur la névralgie du trijumeau : une revue générale et un cas de névralgie liée à une malformation caverneuse traitée par radiochirurgie.

Rien dans les données ne montre que la lamotrigine traite le néoplasme lui-même. Au mieux, elle pourrait soulager de façon symptomatique une douleur neuropathique associée à la tumeur. Cette prédiction est donc peu solide sur le plan mécanistique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Revue | Expert Rev Neurother | Panorama des traitements médicaux et chirurgicaux de la névralgie du trijumeau. Cause probable : compression vasculaire de la racine du nerf, avec démyélinisation focale. Ne traite pas de tumeur. |
| [30650431](https://pubmed.ncbi.nlm.nih.gov/30650431/) | 2018 | Rapport de cas | Stereotact Funct Neurosurg | Première prise en charge par radiochirurgie (Gamma Knife) d'une névralgie du trijumeau secondaire à une malformation caverneuse du tronc cérébral, avec revue de la littérature. |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 65503120 | LAMOTRIGINE TEVA 25 mg (TEVA SANTÉ) | Comprimé dispersible ou à croquer |
| 69967246 | LAMOTRIGINE VIATRIS 100 mg (VIATRIS SANTÉ) | Comprimé dispersible |
| 63062684 | LAMOTRIGINE ZYDUS 200 mg (ZYDUS FRANCE) | Comprimé dispersible ou à croquer |
| 62000092 | LAMOTRIGINE ARROW LAB 50 mg (ARROW GÉNÉRIQUES) | Comprimé dispersible ou à croquer |
| 65667034 | LAMICTAL 200 mg (GLAXOSMITHKLINE) | Comprimé dispersible ou à croquer |

Le dossier liste 5 des 20 AMM. Les textes d'indication ne sont pas fournis.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur le seul score du modèle (niveau L5). Aucun essai n'est associé, et les deux publications concernent la névralgie du trijumeau, non le néoplasme.
- Aucune donnée ne suggère une action antitumorale de la lamotrigine. Le score élevé traduit probablement un signal symptomatique lié à la douleur.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications), car l'absence de ces données bloque le passage au premier filtre de sécurité.
- Compléter le mécanisme d'action (via l'API DrugBank) et les indications des AMM.
- Rechercher toute donnée précliniques ou cliniques d'activité antitumorale de la lamotrigine. Sinon, requalifier l'objectif comme un usage symptomatique (douleur neuropathique associée à la tumeur).
- Examiner en priorité l'indication voisine **névralgie du trijumeau** (2ᵉ rang de la prédiction), nettement mieux étayée. Elle est classée L2 et « Proceed with Guardrails » dans le dossier, avec un essai de phase 2/3 terminé comparant la lamotrigine à la carbamazépine (NCT00913107, 21 patients, donc de faible puissance) et un essai contrôlé contre placebo en traitement additionnel (NCT00203229, 20 patients).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

