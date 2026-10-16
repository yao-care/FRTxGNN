---
layout: default
title: Cortisone
parent: Preuves modérées (L3-L4)
nav_order: 199
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-14
description: "Cortisone : nouvelle indication prédite, Lymphome cutané primitif à cellules T (niveau de preuve L4). Indication d'origine : Non renseignée dans l'AMM"
---

# Cortisone
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **9** 
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

# Cortisone : De l'indication non documentée à la lymphome cutané primitif à cellules T

## Résumé en Une Phrase

La cortisone est un glucocorticoïde naturel (promédicament du cortisol) dont l'autorisation française (AMM) est une préparation homéopathique Boiron, aujourd'hui annulée ; aucune indication d'origine n'y est renseignée.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **lymphome cutané primitif à cellules T**, avec un score élevé mais seulement **5 publications historiques (1951-1964)** et **aucun essai clinique pertinent**.
À noter : parmi les 9 indications prédites, l'**insuffisance surrénalienne** est la mieux étayée (niveau L1 au niveau de la classe thérapeutique), mais elle repose sur des essais portant sur l'hydrocortisone, non sur la cortisone.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans l'AMM |
| Nouvelle Indication Predite | Lymphome cutané primitif à cellules T |
| Score de Prédiction TxGNN | 99,67 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | AMM annulée uniquement (non commercialisé) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances pharmacologiques générales, la cortisone est un promédicament : elle doit être convertie en cortisol actif par la 11-bêta-HSD1 (principalement hépatique). Elle appartient à la classe des glucocorticoïdes.

Les glucocorticoïdes ont une activité lympholytique et peuvent induire l'apoptose des cellules lymphoïdes sensibles. C'est une base plausible pour un effet palliatif dans le mycosis fongoïde, la forme la plus fréquente de lymphome cutané à cellules T. Cependant, le soutien disponible se limite à des cas cliniques et petites séries des années 1950-1960. Il n'existe aucune donnée contrôlée moderne.

Il faut aussi relever que l'indication d'origine n'étant pas documentée, la relation entre indication d'origine et nouvelle indication ne peut pas être établie dans les données disponibles.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04799275](https://clinicaltrials.gov/study/NCT04799275) | Phase 2/3 | Actif, ne recrute plus | 422 | R-miniCHOP avec ou sans azacitidine orale chez des patients de 75 ans et plus atteints de lymphome diffus à grandes cellules B. Ne concerne pas le lymphome cutané à cellules T et la cortisone n'est pas l'agent étudié : aucune preuve directe. |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [14884116](https://pubmed.ncbi.nlm.nih.gov/14884116/) | 1951 | Cas clinique | Svenska lakartidningen | Traitement combiné ACTH et cortisone dans un cas de mycosis fongoïde (avec impétigo herpétiforme et érythrodermie psoriasique) |
| [14896727](https://pubmed.ncbi.nlm.nih.gov/14896727/) | 1951 | Cas clinique | Dermatologica | Effets de la cortisone dans deux cas de mycosis fongoïde |
| [13612293](https://pubmed.ncbi.nlm.nih.gov/13612293/) | 1958 | Cas clinique | Lyon médical | Deux cas traités par delta-cortisone ; processus ulcéro-nécrotique terminal possiblement lié au traitement |
| [13536705](https://pubmed.ncbi.nlm.nih.gov/13536705/) | 1957 | Cas clinique | Bull. Soc. fr. dermatol. syphiligr. | Deux cas d'épithélioma bronchique chez des patients atteints de mycosis fongoïde traités par cortisone |
| [14169182](https://pubmed.ncbi.nlm.nih.gov/14169182/) | 1964 | Revue | J. méd. chir. prat. | Revue générale sur le mycosis fongoïde |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67948172 | CORTISONE BOIRON, dilution entre 3CH et 30CH ou entre 6DH et 60DH (statut : annulée) | Comprimé, solution, granules, poudre et pommade | Non renseignée |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées. À titre de contexte clinique général, les glucocorticoïdes sont immunosuppresseurs et augmentent le risque d'infection (y compris fongique) ; un cas historique mentionne aussi une nécrose ulcéreuse terminale chez un patient traité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Pour le lymphome cutané primitif à cellules T, les preuves se limitent à des cas cliniques anciens (L4), sans essai pertinent. La cortisone n'est plus commercialisée (AMM annulée) et a été supplantée par d'autres glucocorticoïdes (prednisone, dexaméthasone) dans les protocoles modernes.
- Autres indications prédites : l'insuffisance surrénalienne (niveau L1, « Proceed with Guardrails ») correspond à l'usage historique de la cortisone, mais les essais de phase 3 et 4 testent l'hydrocortisone, pas la cortisone ; il s'agit d'une extrapolation de classe, l'hydrocortisone étant aujourd'hui préférée. Le lymphosarcome, la maladie de Crohn colique et le syndrome myélodysplasique relèvent aussi de « Hold » (L4). La candidose est un artefact probable (la cortisone y sert à induire l'immunosuppression chez l'animal, et non à traiter) ; les trois dernières (cytopénie réfractaire de l'enfant, SMD non classé, délétion partielle du bras long du chromosome 5) n'ont aucune donnée (L5).

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action issues de DrugBank
- Mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Données comparatives modernes (cortisone vs glucocorticoïdes de référence) justifiant un intérêt dans le lymphome cutané à cellules T
- Évaluation de la faisabilité d'une voie d'administration, la seule AMM étant homéopathique et annulée
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

