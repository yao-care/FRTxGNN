---
layout: default
title: Atropine
parent: Preuves modérées (L3-L4)
nav_order: 48
evidence_level: L4
indication_count: 2
---

# Atropine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **2** 
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

# Atropine : Vers le Trouble Migraineux (indication d'origine non renseignée dans les données d'AMM)

## Résumé en Une Phrase

L'atropine est un antagoniste muscarinique commercialisé en France sous forme injectable et de collyre. Le texte des indications approuvées n'est pas renseigné dans les données disponibles.
Le modèle TxGNN prédit qu'elle pourrait être utile dans le **trouble migraineux**, mais **aucun essai clinique** et seulement **13 publications** (essentiellement précliniques) étayent cette piste.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Trouble migraineux (migraine) |
| Score de Prédiction TxGNN | 99,56 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 7 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. L'atropine est toutefois un antagoniste des récepteurs muscariniques (bloqueur cholinergique). Mécanistiquement, elle pourrait être applicable à la migraine, mais cela reste une hypothèse.

Des travaux précliniques décrivent un rôle de l'axe parasympathique dans la migraine. La stimulation du ganglion sphénopalatin provoque une extravasation de protéines plasmatiques dans la dure-mère chez le rat. Chez le rat également, une modulation cholinergique agit sur l'inflammation neurogène médiée par les mastocytes méningés. Bloquer les récepteurs muscariniques pourrait donc, en théorie, atténuer ces voies.

Ce lien reste **plausible mais non démontré**. Les données sont presque toutes issues de rongeurs ou de cobayes, ou sont indirectes. La seule observation humaine porte sur l'hémicrânie paroxystique chronique, un trouble céphalalgique voisin : l'atropine y a réduit la sudation, le larmoiement et les sécrétions nasales liés aux crises. Le score TxGNN est une prédiction du modèle, pas une preuve clinique.

Le modèle prédit aussi la **migraine avec aura du tronc cérébral** (score 99,42 %, niveau L5, décision Hold). La seule publication est une étude sur cortex de souris, où l'activation cholinergique **inhibe** la dépression corticale envahissante, substrat présumé de l'aura. L'atropine étant un antagoniste, l'effet pourrait donc aller dans le sens **opposé** au bénéfice prédit. Ce score reflète probablement un voisinage partagé dans le graphe avec le trouble migraineux plutôt qu'une preuve indépendante.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | Revue | J Appl Toxicol | Propriétés pharmacologiques de l'anisodamine, dérivé de l'atropine, moins puissant et moins toxique. Pas de données directes sur la migraine. |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | Observationnelle clinique | Cephalalgia | Chez 4 patients atteints d'hémicrânie paroxystique chronique, l'atropine systémique a nettement réduit la sudation, le larmoiement et les sécrétions nasales liés aux crises. |
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | Préclinique (rat) | Eur J Neurosci | Modulation cholinergique et mastocytes méningés dans l'inflammation neurogène d'un modèle de migraine induit par la nitroglycérine. |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | Préclinique (rat) | Exp Neurol | La stimulation du ganglion sphénopalatin parasympathique induit une extravasation de protéines plasmatiques dans la dure-mère. |
| [15882801](https://pubmed.ncbi.nlm.nih.gov/15882801/) | 2005 | Préclinique | Neurosci Lett | Rôle du CGRP et des récepteurs nicotiniques dans les variations du flux sanguin facial d'origine centrale. |
| [10193781](https://pubmed.ncbi.nlm.nih.gov/10193781/) | 1999 | Préclinique (cobaye) | Br J Pharmacol | Inhibition de la relaxation induite par la nicotine dans l'artère basilaire par certains antalgiques. L'atropine n'y sert que de réactif. |
| [8930196](https://pubmed.ncbi.nlm.nih.gov/8930196/) | 1996 | Préclinique (rongeur/cobaye) | J Pharmacol Exp Ther | Rôle du système cholinergique central dans l'antinociception induite par le sumatriptan. |
| [1786517](https://pubmed.ncbi.nlm.nih.gov/1786517/) | 1991 | Préclinique (porcelet) | Br J Pharmacol | L'ergotamine et la dihydroergotamine sont de puissants agonistes 5-HT1C. Lien indirect avec l'atropine. |

Cinq autres publications de la liste ont été écartées car leur pertinence est trop faible : botulinique et migraine chronique (cas clinique), cardiomyopathie de stress pédiatrique (cas clinique), deux articles sur les effets oculaires du topiramate, et un article de 1977 sur la bêta-phénéthylamine sans résumé.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 63667263 | ATROPINE (SULFATE) LAVOISIER 0,25 mg/1 ml | Solution injectable | Laboratoires Chaix et du Marais |
| 61397901 | ATROPINE (SULFATE) LAVOISIER 0,50 mg/ml | Solution injectable | Laboratoires Chaix et du Marais |
| 66063364 | ATROPINE (SULFATE) AGUETTANT 1 mg/mL | Solution injectable | Aguettant |
| 69984085 | ATROPINE ALCON 1 POUR CENT | Collyre | Laboratoires Alcon |
| 61883472 | ATROPINE (SULFATE) LAVOISIER 1 mg/ml | Solution injectable | Laboratoires Chaix et du Marais |

Sept AMM sont recensées au total ; les cinq principales sont listées ci-dessus.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur un score de modèle et sur des données précliniques ou indirectes (niveau L4). Il n'existe aucun essai clinique de l'atropine dans la migraine.
- Pour la migraine avec aura du tronc cérébral, le sens de l'effet pourrait même être inverse.
- Les informations de sécurité de la notice ANSM ne sont pas disponibles, ce qui empêche de passer à l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice ANSM (mises en garde, contre-indications) à télécharger et analyser
- Données détaillées sur le mécanisme d'action (requête DrugBank)
- Indications approuvées des AMM françaises, pour établir le point de départ du repositionnement
- Évaluation de la compatibilité des voies d'administration (injectable et collyre existants) avec un usage dans la migraine
- Preuves cliniques humaines, au minimum des études observationnelles ou un essai exploratoire de phase 2
- Confirmation du sens de l'effet (antagoniste ou agoniste muscarinique) avant toute hypothèse pour la migraine avec aura du tronc cérébral

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

