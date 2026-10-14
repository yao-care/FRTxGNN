---
layout: default
title: Alverine
parent: Preuves modérées (L3-L4)
nav_order: 51
evidence_level: L4
indication_count: 9
---

# Alverine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **9** 
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

# Alverine : Du Soulagement des Spasmes Digestifs au Trouble Anxieux

## Resume en Une Phrase

Alverine est un antispasmodique musculotrope, utilise a l'origine pour soulager les douleurs liees aux spasmes des muscles lisses digestifs.
Le modele TxGNN predit qu'il pourrait etre efficace pour le **trouble anxieux**, l'indication la mieux etayee parmi les 9 predictions generees.
Cette direction repose sur **aucun essai clinique** et **1 publication preclinique** (etude chez la souris), soit un niveau de preuve tres faible.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non renseignee dans les AMM disponibles (usage connu : spasmes des muscles lisses digestifs) |
| Nouvelle Indication Predite | Trouble anxieux (anxiety disorder) |
| Score de Prediction TxGNN | 99,45 % |
| Niveau de Preuve | L4 |
| Statut de Marche en France | Uniquement des AMM annulees |
| Nombre d'AMM | 2 (toutes annulees) |
| Decision Recommandee | Hold |

**Remarque sur le choix de l'indication :** la premiere prediction du classement TxGNN est le trouble dysthymique (score 99,83 %), mais elle ne repose sur aucune preuve. Ce rapport met en avant le trouble anxieux, seule prediction accompagnee d'une donnee experimentale directe. Les autres predictions sont resumees plus bas.

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action ne sont pas disponibles dans les sources compilees. Sur la base des informations connues, alverine est un relaxant des muscles lisses, utilise dans certains pays pour soulager les troubles gastro-intestinaux accompagnes de spasmes et les crampes associees aux dysmenorrhees. Son lien avec l'anxiete n'est pas etabli cliniquement.

L'etude preclinique disponible (Gupta et al., 2014) rapporte des effets de type anxiolytique du citrate d'alverine dans des modeles murins d'anxiete. Elle suggere une action possible via le recepteur serotoninergique 5-HT1A, dont l'antagonisme est implique dans le comportement anxieux. Les donnees de pharmacologie indiquent par ailleurs une interaction avec la cible HNF4A, dont la pertinence pour l'anxiete n'est pas documentee.

Ce lien reste une hypothese : il repose sur des donnees animales uniquement, sans validation chez l'humain. La relation avec l'indication d'origine (spasmes digestifs) n'a pas pu etre evaluee.

## Preuves d'Essais Cliniques

Aucun essai clinique associe enregistre actuellement.

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [25199966](https://pubmed.ncbi.nlm.nih.gov/25199966/) | 2014 | Etude preclinique (animale) | European Journal of Pharmacology | Effets de type anxiolytique du citrate d'alverine dans des modeles murins d'anxiete, possiblement via le recepteur 5-HT1A |

## Autres Predictions du Modele

| Rang | Maladie predite | Score TxGNN | Niveau de preuve | Recommandation | Commentaire |
|------|------|------|------|------|------|
| 1 | Trouble dysthymique | 99,83 % | L5 | Hold | Aucune preuve ; lien 5-HT1A speculatif |
| 2 | Trouble nevrotique | 99,59 % | L5 | Hold | Categorie large et ancienne, aucune preuve directe |
| 4 | Migraine | 99,25 % | L5 | Hold | Aucune preuve |
| 5 | Depression nevrotique | 99,16 % | L5 | Hold | Seule reference : etude computationnelle (PMID 30087074), non independante de la prediction |
| 6 | Melancolie | 99,14 % | L5 | Hold | Meme etude computationnelle, aucune donnee clinique |
| 7 | Torticolis paroxystique benin du nourrisson | 99,07 % | L5 | Hold | Aucun fondement mecanistique ; absence de donnees pediatriques |
| 8 | Agoraphobie | 99,06 % | L5 | Hold | Lien indirect avec le signal anxiolytique preclinique |
| 9 | Deficit congenital isole en ACTH | 99,02 % | L5 | Hold | Probablement un artefact de prediction |

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee | Statut |
|---------|------|------|-----------|------|
| 61204836 | METEOSPASMYL, capsule molle | Capsule molle | Non renseignee | Annulee |
| 60252027 | DOLOSPASMYL 60 mg/300 mg, capsule molle | Capsule molle | Non renseignee | Annulee |

Les deux AMM sont detenues par les Laboratoires Mayoly Spindler et sont annulees : aucune specialite a base d'alverine seule n'est actuellement valide dans les donnees compilees.

## Considerations de Securite

Veuillez consulter la notice pour les informations de securite. Les mises en garde et contre-indications de la notice ANSM n'ont pas pu etre recuperees, ce qui constitue une lacune bloquante pour l'evaluation de securite.

Interactions : la seule entree disponible est une interaction pharmacologique avec la cible HNF4A (Hepatocyte nuclear factor-4-alpha). Il ne s'agit pas d'une interaction medicamenteuse cliniquement caracterisee et aucun niveau de gravite n'est fourni.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- Le score TxGNN est tres eleve (99,45 %), mais le soutien se limite a une seule etude chez la souris, sans essai clinique. Les AMM francaises sont toutes annulees et les donnees de securite sont manquantes, ce qui bloque le passage a l'etape de criblage de securite.

**Pour avancer, les elements suivants sont necessaires :**
- Recuperer la notice ANSM (mises en garde et contre-indications) pour realiser le criblage de securite
- Obtenir les donnees detaillees sur le mecanisme d'action (par exemple via DrugBank), notamment l'activite sur le recepteur 5-HT1A
- Repliquer les resultats precliniques et verifier leur transposabilite chez l'humain
- Verifier le contexte de l'annulation des AMM (raisons reglementaires ou commerciales)
- Evaluer la compatibilite des voies d'administration avec la nouvelle indication (actuellement uniquement la voie orale, en capsule molle)
- Envisager, si les etapes precedentes sont concluantes, une etude clinique exploratoire de petite taille dans le trouble anxieux
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

