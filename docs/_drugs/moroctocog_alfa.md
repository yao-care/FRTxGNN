---
layout: default
title: Moroctocog Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 205
evidence_level: L5
indication_count: 8
---

# Moroctocog Alfa
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

# Moroctocog alfa : De l'hémophilie A (déduite) au trouble de la sécrétion plaquettaire primaire

## Résumé en Une Phrase

Moroctocog alfa est un facteur VIII de coagulation recombinant (délété du domaine B), commercialisé en France sous le nom REFACTO AF. Le texte d'indication des AMM n'est pas renseigné dans les données, l'usage d'origine (hémophilie A) est donc déduit de la nature du produit.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble de la sécrétion plaquettaire primaire** (score de 99,97 %).
Cette prédiction repose sur la proximité dans un graphe de connaissances : **7 essais cliniques** ont été associés, mais aucun ne teste ce médicament dans cette maladie, et **aucune publication** ne la soutient.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM (hémophilie A déduite de la nature du produit) |
| Nouvelle Indication Prédite | Trouble de la sécrétion plaquettaire primaire (primary release disorder of platelets) |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 5 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Moroctocog alfa est un facteur VIII recombinant délété du domaine B. Il agit comme cofacteur dans le complexe de ténase intrinsèque, une étape clé de la cascade de coagulation. Son rôle est de remplacer le facteur VIII manquant.

**Cette prédiction est peu plausible sur le plan mécanistique.** Le trouble de la sécrétion plaquettaire est un défaut primaire de la fonction des plaquettes. Le remplacement du facteur VIII ne le corrige pas. Le score très élevé (0,9997) reflète la proximité du médicament et de la maladie dans le voisinage « troubles hémorragiques » du graphe, et non un mécanisme thérapeutique crédible.

Les 7 essais associés sont des correspondances par mots-clés (hémophilie A, hémostase, coagulation) et non des tests de ce médicament dans cette maladie.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Phase 3 | Terminé | 159 | rFVIIIFc-VWF-XTEN (BIVV001) en prophylaxie chez des patients ≥12 ans atteints d'hémophilie A sévère. Population différente. |
| [NCT04759131](https://clinicaltrials.gov/study/NCT04759131) | Phase 3 | Terminé | 74 | Même produit (BIVV001) chez des enfants <12 ans atteints d'hémophilie A sévère. Population différente. |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Phase 3 | Terminé | 30 | rFVIII pégylé (BAX 855) lors de chirurgies chez des patients atteints d'hémophilie A sévère. Produit et maladie différents. |
| [NCT07343687](https://clinicaltrials.gov/study/NCT07343687) | N/A | Pas encore en recrutement | 80 | Profils coagulation et hématologie dans la leucémie aiguë myéloïde nouvellement diagnostiquée. Sans rapport. |
| [NCT07400848](https://clinicaltrials.gov/study/NCT07400848) | N/A | En recrutement | 200 | Évaluation biologique du syndrome post-vaccination COVID-19. Sans rapport. |
| [NCT07329036](https://clinicaltrials.gov/study/NCT07329036) | N/A | En recrutement | 25 | Foie artificiel (DPMAS + échange plasmatique) dans l'insuffisance hépatique aiguë sur chronique. Sans rapport. |
| [NCT07439939](https://clinicaltrials.gov/study/NCT07439939) | N/A | En recrutement | 45 | Exploration de l'hémostase systémique et portale lors d'un shunt porto-systémique (TIPS). Sans rapport. |

Les 7 essais sont classés en pertinence « C » (non pertinents pour cette indication).

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64968807 | REFACTO AF 2000 UI (Pfizer Europe MA EEIG) | Poudre et solvant pour solution injectable | Non renseignée |
| 60106606 | REFACTO AF 250 UI (Pfizer Europe MA EEIG) | Poudre et solvant pour solution injectable | Non renseignée |
| 62981909 | REFACTO AF 1000 UI (Pfizer Europe MA EEIG) | Poudre et solvant pour solution injectable | Non renseignée |
| 66743830 | REFACTO AF 3000 UI (Pfizer Europe MA EEIG) | Poudre et solvant pour solution injectable | Non renseignée |
| 60937230 | REFACTO AF 500 UI (Pfizer Europe MA EEIG) | Poudre et solvant pour solution injectable | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5). Aucun essai ni publication ne teste ce médicament dans cette maladie, et le remplacement du facteur VIII n'a pas de rationnel mécanistique face à un défaut fonctionnel plaquettaire.
- Les données de sécurité de l'ANSM sont absentes, ce qui bloque le passage à l'étape de criblage de sécurité (S1).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications).
- Compléter le texte d'indication des AMM et les données de mécanisme d'action (DrugBank).
- Ne pas investir dans cette indication sans donnée mécanistique ou clinique nouvelle.
- Parmi les autres candidats prédits, seule la **carence acquise en facteurs de coagulation** (hémophilie A acquise) présente un lien mécanistique de classe (niveau L4). Les études de soutien utilisent toutefois du FVIII porcin, qui échappe à de nombreux inhibiteurs humains. Le facteur VIII humain de moroctocog alfa risque d'être neutralisé par ces mêmes inhibiteurs, et les agents de contournement restent le traitement de référence. Cette piste mérite une évaluation distincte.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

