---
layout: default
title: L-Lysine
parent: Prédiction du modèle uniquement (L5)
nav_order: 164
evidence_level: L5
indication_count: 3
---

# L-Lysine
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

# L-Lysine : Vers la gastroparésie (indication d'origine non renseignée)

## Résumé en Une Phrase

La L-lysine est un acide aminé présent dans deux spécialités commercialisées en France : une solution pour perfusion et une solution pour dialyse péritonéale. Les données disponibles ne précisent pas son indication d'origine.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **gastroparésie**, mais **aucun essai clinique** n'existe et l'**unique publication** retrouvée est préclinique et n'étudie pas la L-lysine.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Gastroparésie |
| Score de Prédiction TxGNN | 99,77 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. La L-lysine est un acide aminé utilisé dans des solutions de perfusion et de dialyse péritonéale. Aucun mécanisme établi ne la relie à la motricité gastrique ou à la gastroparésie.

Le score TxGNN très élevé (99,77 %) provient d'une prédiction fondée sur un graphe de connaissances. Il n'est soutenu par aucune donnée clinique ou mécanistique. Il doit donc être considéré comme une simple hypothèse à explorer, et non comme un signal d'efficacité.

La seule publication retrouvée porte sur la délivrance de cellules souches mésenchymateuses par hydrogel dans l'estomac. Elle n'évalue pas la L-lysine et ne permet pas de justifier cette piste.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [29414870](https://pubmed.ncbi.nlm.nih.gov/29414870/) | 2018 | Préclinique | Bioengineering (Basel) | Délivrance de cellules souches mésenchymateuses à partir d'hydrogels de gélatine-alginate vers la lumière gastrique pour traiter la gastroparésie. Aucune évaluation de la L-lysine. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 62789435 | PRIMENE 10 %, solution injectable pour perfusion (BAXTER) | Solution pour perfusion |
| 65461618 | NUTRINEAL PD4 A 1,1 % D'ACIDES AMINES, solution pour dialyse péritonéale (VANTIVE) | Solution pour dialyse péritonéale |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5). Il n'y a aucun essai clinique, aucun mécanisme plausible et aucune donnée de sécurité exploitable.
- Les deux autres indications prédites (déficit congénital en prothrombine, déficit en vitamine D) ne sont pas mieux étayées. La première repose sans doute sur une correspondance de mots-clés, et la seconde utilise un terme obsolète de l'ontologie.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), car ces données de sécurité manquantes bloquent le passage au criblage de sécurité.
- Obtenir le mécanisme d'action depuis DrugBank pour évaluer un lien mécanistique avec la motricité gastrique.
- Documenter l'indication d'origine des deux AMM.
- Rechercher des données précliniques ou cliniques évaluant directement la L-lysine dans la gastroparésie.
- Vérifier la compatibilité des voies d'administration (perfusion et dialyse péritonéale) avec un usage dans la gastroparésie.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

