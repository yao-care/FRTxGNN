---
layout: default
title: Carfilzomib
parent: Prédiction du modèle uniquement (L5)
nav_order: 143
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Carfilzomib : nouvelle indication prédite, CMM7 (rang 1 de la prédiction (niveau de preuve L5). Indication d'origine : Myélome plasmocytaire"
monitor_inn: "CARFILZOMIB"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "vulvar melanoma (disease)", "melanoma"]
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

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

# Carfilzomib : Du Myélome Plasmocytaire au Mélanome

## Résumé en Une Phrase

Carfilzomib est un inhibiteur irréversible du protéasome, initialement utilisé pour le traitement du myélome plasmocytaire (myélome multiple).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **mélanome** (et plusieurs sous-types : mélanome uvéal épithélioïde, mélanome vulvaire, mélanome leptoméningé pédiatrique), mais **aucun essai clinique** n'est enregistré et seules **4 publications précliniques ou computationnelles** sont disponibles, dont une seule étude *in vitro* directement pertinente.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Myélome plasmocytaire (source : graphe de connaissances TxGNN ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | CMM7 (rang 1 de la prédiction ; voir remarque ci-dessous) |
| Score de Prédiction TxGNN | 99,37 % |
| Niveau de Preuve | L5 (pour CMM7) ; L4 pour le mélanome (rang 5) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

**Remarque :** les cinq prédictions retenues sont toutes de la famille des mélanomes. La première (CMM7) est une entité mal documentée dans les données compilées. Le mélanome « général » (rang 5, score 99,03 %) est le seul à disposer de publications ; le reste du rapport s'appuie donc sur lui pour les preuves.

| Rang | Maladie prédite | Score TxGNN | Niveau de preuve | Recommandation |
|------|------|------|------|------|
| 1 | CMM7 | 99,37 % | L5 | Hold |
| 2 | Mélanome leptoméningé pédiatrique | 99,30 % | L5 | Hold |
| 3 | Mélanome uvéal à cellules épithélioïdes | 99,23 % | L5 | Hold |
| 4 | Mélanome vulvaire | 99,19 % | L5 | Hold |
| 5 | Mélanome | 99,03 % | L4 | Question de recherche |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des informations connues, le carfilzomib est un inhibiteur irréversible du protéasome, dont l'efficacité dans le myélome plasmocytaire est établie. Mécanistiquement, il pourrait être applicable à d'autres tumeurs dépendantes du protéasome, comme le mélanome.

Le lien repose sur la dépendance des cellules tumorales à la dégradation protéique par le protéasome. Une étude *in vitro* sur des cellules de mélanome murin B16-F1 (PMID 33671902) rapporte que le carfilzomib, seul ou associé au bortézomib, renforce l'apoptose avec activation de plusieurs caspases (3, 8, 9 et 12). C'est un argument plausible, mais préclinique.

Les extrapolations vers les sous-types sont beaucoup plus incertaines : aucune donnée ne montre que le carfilzomib atteint le système nerveux central ou les sites leptoméningés (mélanome leptoméningé pédiatrique) ; le mélanome uvéen est biologiquement distinct (mutations GNAQ/GNA11) ; le mélanome muqueux/vulvaire diffère du mélanome cutané. La similarité avec l'indication d'origine n'a pas été évaluée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Pour le mélanome (rang 5) ; aucune littérature n'est disponible pour les quatre autres prédictions.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | Étude *in vitro* | Biology | Carfilzomib associé au bortézomib : apoptose accrue dans les cellules de mélanome B16-F1, avec activation de plusieurs caspases |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Étude mécanistique préclinique | Matrix Biology | Bortézomib et carfilzomib activent la voie NF-κB et induisent l'expression de l'héparanase, associée à un phénotype tumoral plus agressif ; lien indirect avec le mélanome |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Étude mécanistique préclinique | Molecular Cancer Research | Le gène AIRAPL (ZFAND2A) régule la survie cellulaire dans le mélanome humain via l'E3-ligase cIAP2 ; lien indirect |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | Computationnelle (docking/simulation moléculaire) | J Biomol Struct Dyn | Repositionnement de médicaments contre des cibles kinases dans dix types de cancers, dont le mélanome ; preuve *in silico* uniquement |

## Informations de Marché en France

Les trois AMM sont annulées ; le texte des indications approuvées n'est pas renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 69270884 | KYPROLIS 30 mg | Poudre pour solution pour perfusion | Annulée |
| 62529551 | KYPROLIS 10 mg | Poudre pour solution pour perfusion | Annulée |
| 64296925 | KYPROLIS 60 mg | Poudre pour solution pour perfusion | Annulée |

Titulaire : AMGEN EUROPE.

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur du protéasome), utilisée en oncologie hématologique |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter la notice ; une surveillance hématologique (NFS), hépatique et rénale est habituelle pour les antinéoplasiques |
| Protection de Manipulation | Appliquer les règles de manipulation des médicaments antinéoplasiques en vigueur dans l'établissement |

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

**Interactions médicamenteuses** : 100 interactions ont été recensées (base DDInter) ; les 20 premières sont disponibles dans les données compilées.

- **Majeures** : oxandrolone, oxymétholone, stanozolol, déferiprone, samarium (153Sm) lexidronam, facteur antihémophilique recombinant, acide aminocaproïque, facteur von Willebrand humain, avatrombopag, inhibiteur de la C1-estérase humain, facteur VIIa de coagulation recombinant, facteur X de coagulation humain, conestat alfa.
- **Modérées** : métronidazole, naltrexone, rosuvastatine, simvastatine, tinidazole, palifermine, chlorure de strontium Sr-89.

Un grand nombre de ces interactions majeures concernent des agents pro-coagulants ou hémostatiques, ce qui justifie une revue pharmacologique détaillée avant toute utilisation dans une nouvelle indication.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose essentiellement sur le modèle (score élevé, ~99 %) ; aucun essai clinique n'existe et les seules données pour le mélanome sont précliniques ou indirectes (niveau L4 au mieux, L5 pour les quatre autres sous-types). Les AMM françaises sont toutes annulées, et les données de sécurité de la notice manquent.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mécanisme d'action détaillé (interrogation de DrugBank)
- Notice ANSM (mises en garde, contre-indications) pour lancer le criblage de sécurité
- Clarification de l'entité « CMM7 » et du sous-type de mélanome à cibler
- Données précliniques *in vivo* (modèles animaux de mélanome) et, si elles sont concluantes, un essai clinique de phase 1/2
- Données de pénétration du système nerveux central pour le mélanome leptoméningé, et de biologie propre au mélanome uvéen et muqueux
- Analyse de la compatibilité de voie d'administration et de la similarité avec l'indication d'origine (actuellement en attente)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

