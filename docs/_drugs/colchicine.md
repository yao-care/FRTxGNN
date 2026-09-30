---
layout: default
title: Colchicine
parent: Preuves modérées (L3-L4)
nav_order: 90
evidence_level: L4
indication_count: 3
---

# Colchicine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **3** 
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

# Colchicine : Des usages décrits dans la littérature (goutte, fièvre méditerranéenne familiale) au paludisme à Plasmodium falciparum

## Résumé en Une Phrase

La colchicine est commercialisée en France (Colchimax, Colchicine Opocalcium). La littérature fournie la décrit comme utilisée surtout dans la goutte et la fièvre méditerranéenne familiale.
Le modèle TxGNN prédit qu'elle pourrait être efficace contre le **paludisme à Plasmodium falciparum**, avec un score élevé (99,60 %).
Cette prédiction n'est soutenue que par **0 essai clinique** et **6 références de littérature** (5 études distinctes, dont 4 in vitro), qui portent sur d'autres composés ciblant le cytosquelette et non sur la colchicine elle-même.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM de l'ANSM (texte d'indication vide). La littérature fournie cite la goutte et la fièvre méditerranéenne familiale |
| Nouvelle Indication Prédite | Paludisme à Plasmodium falciparum |
| Score de Prédiction TxGNN | 99,60 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base utilisée. D'après les informations connues, la colchicine se lie à la tubuline et perturbe les microtubules. Ce mécanisme antimitotique est celui qui fonde le rapprochement avec le paludisme.

Le lien avec la nouvelle indication est indirect. Plusieurs études in vitro montrent que des composés ciblant le cytosquelette (tubuline, actine) inhibent le développement intra-érythrocytaire de *P. falciparum*. Les auteurs de 1989 notent que les tubulines du parasite semblent différer des protéines de mammifères. Ils décrivent aussi un effet du colcémide, un analogue de la colchicine, sur la synthèse protéique du parasite, semblable à celui des tubulozoles. Cela rend l'hypothèse plausible, sans la démontrer.

Le lot de données ne contient **aucune donnée clinique propre à la colchicine** dans le paludisme. Le score TxGNN élevé est une prédiction informatique seulement. L'index thérapeutique étroit de la colchicine et l'existence d'antipaludiques efficaces rendent un développement à court terme peu attractif.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune de ces publications n'étudie la colchicine directement. Il n'y a ni ECR ni revue systématique. Les références sont listées par ordre de pertinence et non par type.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [2655935](https://pubmed.ncbi.nlm.nih.gov/2655935/) | 1989 | Étude in vitro | Cell Biol Int Rep | Neuf substances liant la tubuline et la cytochalasine B (actine) testées sur *P. falciparum*. Les tubulines du parasite semblent différentes de celles des mammifères. Le tubulozole-T apparaît comme un antipaludique prometteur (l'entrée PMID 2670249 en est un doublon) |
| [2221861](https://pubmed.ncbi.nlm.nih.gov/2221861/) | 1990 | Étude in vitro | Antimicrob Agents Chemother | Mode d'action des tubulozoles : la synthèse protéique diminue rapidement, sans effet primaire sur la glycolyse, les protéases ou les acides nucléiques. Le colcémide a un effet comparable sur la synthèse protéique |
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | Étude in vitro | PLoS One | Effets cellulaires de la curcumine sur *P. falciparum*, dont une perturbation des microtubules du parasite |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | Étude in vitro / cellulaire | Mol Cell Biol | Expression du gène pfmdr1 dans des cellules de mammifères associée à une sensibilité accrue à la chloroquine. Lien indirect avec la colchicine (transporteurs ABC) |
| [6362934](https://pubmed.ncbi.nlm.nih.gov/6362934/) | 1984 | Étude observationnelle | Clin Exp Immunol | Anticorps anti-filaments intermédiaires chez 82 % de 78 patients atteints de paludisme aigu. Intérêt limité pour l'efficacité thérapeutique |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 68066715 | COLCHICINE OPOCALCIUM 1 mg, comprimé sécable (Laboratoires Mayoly Spindler) | Comprimé sécable |
| 61331730 | COLCHIMAX, comprimé pelliculé sécable (Laboratoires Mayoly Spindler) | Comprimé pelliculé sécable |

Le texte de l'indication approuvée n'est pas renseigné dans les données ANSM fournies.

## Considérations de Sécurité

- **Toxicité** : la littérature fournie souligne l'index thérapeutique étroit de la colchicine, sans distinction nette entre doses non toxiques, toxiques et létales. Les intoxications non intentionnelles sont fréquentes et souvent de mauvais pronostic (PMID 20586571).

Aucune mise en garde ni contre-indication issue de la notice ANSM n'est disponible, et aucune interaction médicamenteuse n'a été retrouvée. Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur un score de modèle et sur des études in vitro portant sur d'autres composés. Aucun essai clinique ni donnée propre à la colchicine ne la soutient (niveau L4).
- La sécurité n'a pas pu être évaluée faute de notice ANSM, et l'index thérapeutique étroit du médicament limite l'intérêt d'un développement dans une indication où des traitements efficaces existent déjà.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications, interactions), qui bloque le passage au criblage de sécurité.
- Obtenir les données de mécanisme d'action depuis DrugBank.
- Disposer d'études in vitro ou animales testant directement la colchicine (ou le colcémide) sur *P. falciparum*, avec des concentrations atteignables sans toxicité chez l'humain.
- Comparer la valeur ajoutée potentielle aux antipaludiques existants.

**Remarque :** dans le même lot de données, la prédiction de rang 2 (fièvre méditerranéenne familiale) est bien mieux étayée (niveau L3, décision « Proceed with Guardrails »). La colchicine y est décrite comme traitement de première ligne, ce qui en fait un usage quasi établi plutôt qu'un repositionnement.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement nécessite une validation clinique avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

