---
layout: default
title: Carfilzomib
parent: Prédiction du modèle uniquement (L5)
nav_order: 72
evidence_level: L5
indication_count: 5
---

# Carfilzomib
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

# Carfilzomib : Du Myélome Multiple au Mélanome (CMM7 et formes apparentées)

## Résumé en Une Phrase

Carfilzomib est un inhibiteur irréversible du protéasome. Son indication d'origine n'est pas renseignée dans les AMM ANSM du dossier, mais la littérature fournie le rattache au traitement du myélome. Le modèle TxGNN prédit qu'il pourrait être efficace pour **CMM7** (score 99,37 %), avec **0 essai clinique** et **0 publication** pour cette entité précise. Les seules données disponibles sont **5 publications précliniques ou in silico**, rattachées à l'entrée « mélanome » (rang 5).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée (texte d'indication vide dans les 3 AMM ANSM) |
| Nouvelle Indication Prédite | CMM7 |
| Score de Prédiction TxGNN | 99,37 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

Les autres indications prédites sont toutes des mélanomes :

| Rang | Indication prédite | Score TxGNN | Niveau de preuve | Recommandation |
|------|------|------|------|------|
| 1 | CMM7 | 99,37 % | L5 | Hold |
| 2 | Mélanome leptoméningé pédiatrique | 99,30 % | L5 | Hold |
| 3 | Mélanome uvéal à cellules épithélioïdes | 99,23 % | L5 | Hold |
| 4 | Mélanome vulvaire | 99,19 % | L5 | Hold |
| 5 | Mélanome | 99,03 % | L4 | Question de recherche |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Carfilzomib est un inhibiteur irréversible du protéasome. Son efficacité dans le myélome, tumeur très dépendante de la dégradation protéique, est le contexte cité dans la littérature fournie. Mécanistiquement, il pourrait être applicable aux mélanomes, mais ce lien n'est pas vérifié.

L'inhibition du protéasome peut induire l'apoptose des cellules de mélanome. La seule preuve directe fournie est une étude in vitro sur des cellules B16-F1 (mélanome murin), associant carfilzomib et bortézomib. Ce n'est pas une preuve clinique chez l'humain. L'argument reste générique pour tous les mélanomes et n'est soutenu que par des données précliniques.

Plusieurs incertitudes propres aux entités prédites s'ajoutent :
- **CMM7** : aucun essai ni publication spécifique n'a été fourni.
- **Mélanome leptoméningé pédiatrique** : la capacité de carfilzomib à atteindre le compartiment du système nerveux central n'est pas établie, et le contexte pédiatrique ajoute de l'incertitude.
- **Mélanome uvéal** : sa biologie diffère de celle du mélanome cutané, donc les données du mélanome ne peuvent pas être supposées transposables.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement (pour aucune des 5 indications prédites).

## Preuves de la Littérature

Aucune littérature associée disponible pour CMM7. Les 5 publications ci-dessous sont rattachées à l'entrée « mélanome » (rang 5). Toutes sont de niveau précliniques ou in silico, sans donnée clinique humaine.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | Étude préclinique in vitro | Biology | Carfilzomib associé au bortézomib induit l'apoptose des cellules de mélanome B16-F1, avec activation de plusieurs caspases (3, 8, 9, 12) |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | Étude in silico (docking/simulation) | J Biomol Struct Dyn | Repositionnement de médicaments cliniques contre des cibles kinases dans dix types de cancer, dont le mélanome ; lien indirect |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Étude préclinique in vitro | Matrix Biol | Bortézomib et carfilzomib activent la voie NF-κB et augmentent l'expression de l'héparanase, associée à un phénotype tumoral agressif ; contexte myélome |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Étude mécanistique préclinique | Mol Cancer Res | Rôle du gène AIRAPL (ZFAND2A) dans la survie des cellules de mélanome humain, lié à la biologie du protéasome ; lien indirect |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | Étude mécanistique préclinique | Leukemia | PROTAC ciblant les protéines BET, actifs dans des modèles précliniques de myélome ; lien indirect avec le mélanome |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69270884 | KYPROLIS 30 mg | Poudre pour solution pour perfusion | Non renseignée |
| 62529551 | KYPROLIS 10 mg | Poudre pour solution pour perfusion | Non renseignée |
| 64296925 | KYPROLIS 60 mg | Poudre pour solution pour perfusion | Non renseignée |

Les trois AMM sont détenues par AMGEN EUROPE.

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur irréversible du protéasome) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les cinq indications prédites reposent essentiellement sur le score du modèle : aucun essai clinique n'a été fourni, et les seules preuves (entrée « mélanome ») sont précliniques ou in silico.
- Les données de sécurité de la notice ANSM manquent (lacune bloquante), ce qui empêche de passer au criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications) pour lever la lacune bloquante de sécurité.
- Compléter le mécanisme d'action (MOA) via DrugBank.
- Renseigner l'indication d'origine à partir du RCP de KYPROLIS.
- Rechercher des données spécifiques à CMM7 et aux sous-types de mélanome (essais cliniques, études de xénogreffes).
- Évaluer la pénétration du SNC et la faisabilité pédiatrique pour le mélanome leptoméningé pédiatrique.
- Vérifier la compatibilité de la voie d'administration (perfusion IV) avec les besoins de chaque indication.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

