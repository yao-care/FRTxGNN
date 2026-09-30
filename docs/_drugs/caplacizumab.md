---
layout: default
title: Caplacizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 69
evidence_level: L5
indication_count: 10
---

# Caplacizumab
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

# Caplacizumab : Du Purpura Thrombotique Thrombocytopénique Acquis au Trouble de la Libération Plaquettaire Primaire

## Résumé en Une Phrase

Caplacizumab est un nanobody dirigé contre le domaine A1 du facteur von Willebrand (VWF), utilisé dans le traitement du purpura thrombotique thrombocytopénique acquis (PTTa). Le texte d'indication de l'AMM française n'est pas renseigné dans le dossier. Cette indication ressort de l'analyse des preuves.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble de la libération plaquettaire primaire** (*primary release disorder of platelets*), mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Purpura thrombotique thrombocytopénique acquis (déduit des preuves, texte d'AMM non renseigné) |
| Nouvelle Indication Prédite | Trouble de la libération plaquettaire primaire |
| Score de Prédiction TxGNN | 99,9998 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base de référence. Sur la base des informations connues, caplacizumab bloque l'interaction entre le VWF (domaine A1) et le récepteur plaquettaire GPIb. Son efficacité dans le PTT immun, où les multimères de VWF provoquent une microthrombose, a été prouvée.

Le trouble de la libération plaquettaire primaire est un déficit de la sécrétion plaquettaire. La prédiction du modèle repose donc sur la proximité des deux maladies dans le graphe de connaissances (plaquettes, adhésion, hémostase primaire).

Sur le plan mécanistique, la prédiction est peu plausible. Dans un trouble de la fonction plaquettaire, bloquer l'adhésion VWF-GPIb altérerait davantage l'hémostase primaire, sans justification thérapeutique. Le risque hémorragique propre au médicament serait aggravé. Il s'agit d'une prédiction du modèle uniquement.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64183564 | CABLIVI 10 mg, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | Non renseignée |

Titulaire : ABLYNX (Belgique).

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Cette indication est soutenue uniquement par le score du modèle (L5). Le mécanisme d'action irait dans le sens inverse du bénéfice attendu, avec un risque hémorragique accru.

**Autres candidats de la liste :**
- Les huit autres candidats prédits, dont l'hémophilie, la thrombasthénie de Glanzmann et le syndrome de Scott, sont aussi en Hold. Ils reposent sur la seule prédiction du modèle et présentent un risque hémorragique.
- Le PTT (rang 5) est le seul candidat solide (L1, Proceed with Guardrails). Ce n'est pas un repositionnement : c'est l'indication déjà commercialisée, qui sert de contrôle positif. Il est soutenu par l'essai de phase 3 HERCULES ([NCT02553317](https://clinicaltrials.gov/study/NCT02553317), [PMID 30625070](https://pubmed.ncbi.nlm.nih.gov/30625070/)) et l'essai de phase 2 TITAN ([NCT01151423](https://clinicaltrials.gov/study/NCT01151423), [PMID 26863353](https://pubmed.ncbi.nlm.nih.gov/26863353/)), ainsi que par les recommandations de l'ISTH.
- Ses garde-fous : surveillance du risque hémorragique, durée guidée par l'ADAMTS13 et le VWF, association à l'échange plasmatique et à l'immunosuppression.

**Pour avancer, les éléments suivants sont nécessaires :**
- Validation préclinique du mécanisme dans le trouble de la libération plaquettaire
- Notice de l'ANSM (mises en garde et contre-indications), à télécharger et analyser pour le dépistage de sécurité
- Données détaillées sur le mécanisme d'action (DrugBank)
- Texte d'indication de l'AMM française
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

