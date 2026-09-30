---
layout: default
title: Rasburicase
parent: Prédiction du modèle uniquement (L5)
nav_order: 261
evidence_level: L5
indication_count: 10
---

# Rasburicase
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

# Rasburicase : De l'Hyperuricémie à l'Hypouricémie Rénale

## Résumé en Une Phrase

Rasburicase est une urate oxydase recombinante, une enzyme qui dégrade l'acide urique, et son usage d'origine est la réduction de l'uricémie.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hypouricémie rénale**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction. Le mécanisme d'action va même dans le sens inverse, donc la prédiction est très probablement un faux positif.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données d'AMM (le mécanisme correspond à la réduction de l'uricémie) |
| Nouvelle Indication Prédite | Hypouricémie rénale |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base de référence. Rasburicase est une urate oxydase recombinante. Elle convertit l'acide urique en allantoïne, ce qui fait baisser rapidement l'uricémie.

**Cette prédiction n'est pas raisonnable sur le plan mécanistique.** L'hypouricémie rénale est déjà un état d'acide urique bas. Rasburicase agirait donc dans le mauvais sens et pourrait aggraver la situation. Le score très élevé du modèle (0,9999) ressemble à un artefact du graphe de connaissances, pas à un signal propre au médicament. Il faut la considérer comme un probable faux positif.

Parmi les 10 indications prédites, la plus cohérente sur le plan mécanistique est le **déficit partiel en HPRT** (rang 2, score 99,97 %). Ce déficit provoque une surproduction de purines et une hyperuricémie, et rasburicase dégrade l'acide urique. Toutefois, rasburicase est un traitement de courte durée à usage aigu. Elle est immunogène et ne corrige ni le défaut métabolique en amont ni les atteintes neurologiques. Les autres candidats (porphyrie hépatique, hypertension portale, syndrome hépatopulmonaire, etc.) n'ont aucun lien mécanistique identifié. Plusieurs partagent le même score, ce qui évoque un artefact de voisinage dans le graphe.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69211156 | FASTURTEC 1,5 mg/ml (SANOFI WINTHROP INDUSTRIE) | Poudre et solvant pour solution à diluer pour perfusion | Non précisée dans les données |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Les données de sécurité de l'ANSM (mises en garde, contre-indications) ne sont pas encore intégrées, et aucune interaction médicamenteuse n'a été trouvée. À titre indicatif, l'analyse mécanistique signale les risques suivants de rasburicase : immunogénicité, hémolyse en cas de déficit en G6PD et méthémoglobinémie.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les 10 indications prédites sont au niveau L5 (prédiction du modèle uniquement, sans essai ni publication).
- Pour l'hypouricémie rénale, le mécanisme est contraire à l'effet recherché.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice ANSM (mises en garde et contre-indications), qui bloque actuellement le criblage de sécurité
- Données détaillées sur le mécanisme d'action (via DrugBank)
- Indication approuvée en France, absente des données d'AMM
- Pour le déficit partiel en HPRT, une revue de littérature ciblée et une évaluation de la faisabilité d'un usage aigu uniquement, avant toute décision
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

