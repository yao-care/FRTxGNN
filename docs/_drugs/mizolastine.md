---
layout: default
title: Mizolastine
parent: Prédiction du modèle uniquement (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Mizolastine
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

# Mizolastine : D'un antihistaminique H1 à la porphyrie aiguë intermittente

## Résumé en Une Phrase

La mizolastine est un antihistaminique H1 de seconde génération commercialisé en France (les textes d'indication des AMM ne sont pas renseignés dans les données disponibles).
Le modèle TxGNN prédit qu'elle pourrait être utile dans la **porphyrie aiguë intermittente**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM (antihistaminique H1) |
| Nouvelle Indication Prédite | Porphyrie aiguë intermittente |
| Score de Prédiction TxGNN | 99,76 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la mizolastine est un antihistaminique H1 de seconde génération, à action périphérique. Aucun lien mécanistique établi avec la porphyrie aiguë intermittente n'a pu être identifié.

Le score élevé (99,76 %) reflète une proximité dans le graphe de connaissances, pas une preuve biologique. Les autres candidats prédits présentent des scores quasi identiques (99,47 % à 99,71 %), ce qui suggère que le modèle ne discrimine guère entre eux. Il s'agit surtout de troubles neurologiques du mouvement, sans rapport avec l'action antihistaminique de la molécule.

Point de vigilance : les patients atteints de porphyrie sont exposés au risque de crises déclenchées par certains médicaments. La sécurité de la mizolastine dans cette population devrait donc être vérifiée avant tout autre travail.

| Rang | Maladie prédite | Score TxGNN | Niveau de preuve |
|------|------|------|------|
| 1 | Porphyrie aiguë intermittente | 99,76 % | L5 |
| 2 | Troubles du mouvement psychogènes | 99,71 % | L5 |
| 3 | Dyskinésie linguo-facio-buccale | 99,71 % | L5 |
| 4 | Trouble tic chronique | 99,71 % | L5 |
| 5 | Attaques de frissonnement bénignes | 99,70 % | L5 |
| 6 | Maladies extrapyramidales et du mouvement | 99,70 % | L5 |
| 7 | Tremblement orthostatique primaire | 99,69 % | L5 |
| 8 | Syndrome tremblement-nystagmus-ulcère duodénal | 99,69 % | L5 |
| 9 | Élévation tonique paroxystique bénigne du regard chez l'enfant avec ataxie | 99,68 % | L5 |
| 10 | Déficit en carbamoyl-phosphate synthétase I | 99,47 % | L5 |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64991179 | MIZOLLEN 10 mg, comprimé à libération modifiée | Comprimé pelliculé à libération modifiée | Non renseignée |
| 65120823 | MIZOCLER 10 mg, comprimé pelliculé à libération modifiée | Comprimé pelliculé à libération modifiée | Non renseignée |

Les deux AMM sont détenues par DESMA PHARMA.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucune preuve clinique ou bibliographique (niveau L5, stade S0), et aucun mécanisme plausible reliant l'antagonisme H1 périphérique à la porphyrie aiguë intermittente.
- Les données de sécurité de la notice ANSM manquent et bloquent toute progression vers le criblage de sécurité. Le risque de déclenchement de crises chez les patients porphyriques doit être écarté au préalable.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications, interactions), en vérifiant en particulier le caractère porphyrinogène de la mizolastine
- Obtenir les données de mécanisme d'action (MOA) via DrugBank
- Renseigner les indications approuvées des deux AMM
- Réaliser une revue de littérature ciblée (mizolastine ou antihistaminiques H1 et porphyries) pour rechercher un éventuel signal
- Examiner si une des autres prédictions (troubles du mouvement, tics) repose sur un signal plus crédible, sinon abandonner cette piste
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

