---
layout: default
title: Nordazepam
parent: Prédiction du modèle uniquement (L5)
nav_order: 543
evidence_level: L5
indication_count: 7
---

# Nordazepam
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

# Nordazépam : De l'indication d'origine non renseignée à l'insomnie

## Résumé en Une Phrase

Nordazépam est une benzodiazépine, également métabolite actif du diazépam et d'autres benzodiazépines. Ses deux autorisations de mise sur le marché françaises (AMM) sont annulées et ne mentionnent aucune indication approuvée.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**insomnie**, mais **aucun essai clinique** ni **aucune publication clinique** ne soutient actuellement cette direction : la prédiction repose uniquement sur la similarité avec la classe des benzodiazépines.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM |
| Nouvelle Indication Prédite | Insomnie |
| Score de Prédiction TxGNN | 99,94 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Annulé uniquement (aucune AMM valide) |
| Nombre d'AMM | 2 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le nordazépam fait partie de la classe des benzodiazépines : c'est un modulateur allostérique positif des récepteurs GABA-A, et un métabolite actif du diazépam et d'autres molécules de cette famille. Il produit des effets sédatifs, hypnotiques et anxiolytiques.

Ce profil pharmacologique est cohérent avec le traitement de l'insomnie, car la potentialisation GABAergique favorise la sédation. Le score élevé du modèle (99,94 %) reflète probablement la similarité avec les benzodiazépines hypnotiques déjà approuvées, et non une preuve propre au nordazépam.

Les autres prédictions du modèle suivent la même logique de classe : trouble du sommeil (initiation et maintien), sevrage alcoolique avec delirium, abus de barbituriques et anxiété. Elles restent au niveau L5, sauf l'anxiété (L4, uniquement des données indirectes). Certaines prédictions, comme l'abus d'antidépresseurs, n'ont pas de justification mécanistique claire et reflètent probablement un regroupement de termes dans le graphe de connaissances.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune publication n'est associée à l'insomnie. Pour l'indication prédite en rang 6 (anxiété), 20 publications ont été retrouvées, mais aucune n'est une étude d'efficacité clinique du nordazépam. Voici les plus pertinentes (études précliniques, pharmacocinétiques ou analytiques, à titre indicatif) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [1971091](https://pubmed.ncbi.nlm.nih.gov/1971091/) | 1990 | Étude préclinique de métabolisme | Molecular Pharmacology | Rôle des enzymes CYP3A dans l'hydroxylation en C3 du diazépam et du nordazépam (microsomes de foie de rat) |
| [35235842](https://pubmed.ncbi.nlm.nih.gov/35235842/) | 2022 | Caractérisation physicochimique | J Pharm Sci | Mobilité moléculaire à l'état solide amorphe du diazépam et du nordazépam |
| [33041783](https://pubmed.ncbi.nlm.nih.gov/33041783/) | 2020 | Étude préclinique d'interaction pharmacocinétique | Front Pharmacol | Effet inhibiteur de l'impératorine sur la pharmacocinétique du diazépam |
| [18586210](https://pubmed.ncbi.nlm.nih.gov/18586210/) | 2008 | Rapport de cas | J Forensic Leg Med | Intoxication fatale associant milnacipran et six autres molécules dont le nordazépam |
| [42037156](https://pubmed.ncbi.nlm.nih.gov/42037156/) | 2026 | Étude pharmacocinétique | Br J Pharmacol | Pharmacocinétique materno-fœtale du diazépam et de ses métabolites chez la souris gestante |
| [35102409](https://pubmed.ncbi.nlm.nih.gov/35102409/) | 2023 | Étude analytique de stabilité | J Anal Toxicol | Stabilité à long terme des benzodiazépines et des hypnotiques Z dans le sang |
| [32871413](https://pubmed.ncbi.nlm.nih.gov/32871413/) | 2020 | Méthode analytique | J Pharm Biomed Anal | Méthode LC-MS/MS multi-analytes pour benzodiazépines et hypnotiques Z |
| [32092690](https://pubmed.ncbi.nlm.nih.gov/32092690/) | 2020 | Suivi de consommation | J Pharm Biomed Anal | Surveillance de la consommation de benzodiazépines par analyse capillaire |

Pour l'abus d'hallucinogènes (rang 3), la seule publication, [33882283](https://pubmed.ncbi.nlm.nih.gov/33882283/) (2021, Clinical Biochemistry), évalue un dispositif de dépistage salivaire de substances et n'apporte aucune preuve de bénéfice thérapeutique.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67581406 | NORDAZ 7,5 mg, comprimé sécable (annulée) | Comprimé sécable | Non renseignée |
| 61056483 | NORDAZ 15 mg, comprimé quadrisécable (annulée) | Comprimé quadrisécable | Non renseignée |

Les deux AMM sont détenues par BOUCHARA-RECORDATI. Il n'existe actuellement aucune formulation commercialisée en France.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Points à noter issus des données compilées :
- Aucune interaction médicamenteuse n'a été retrouvée dans la base interrogée, ce qui ne signifie pas absence d'interactions.
- Les benzodiazépines comportent un risque de mésusage, de dépendance et de tolérance, à évaluer avec soin pour toute nouvelle indication, en particulier dans les contextes d'abus de substances.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction est plausible sur le plan pharmacologique, mais elle repose uniquement sur l'effet de classe des benzodiazépines : aucun essai ni publication clinique sur le nordazépam dans l'insomnie (niveau L5). De plus, les deux AMM françaises sont annulées et les données de sécurité de la notice sont manquantes, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), étape bloquante.
- Documenter le mécanisme d'action détaillé du nordazépam (par exemple via DrugBank).
- Rechercher des études cliniques directes du nordazépam dans l'insomnie ou l'anxiété, et comparer avec les benzodiazépines hypnotiques déjà approuvées.
- Évaluer la pertinence d'un repositionnement compte tenu de l'annulation des AMM et du risque de dépendance.
- Préciser l'indication d'origine, absente des AMM actuelles, et la compatibilité des voies d'administration.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

