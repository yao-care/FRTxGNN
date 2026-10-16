---
layout: default
title: Varenicline
parent: Prédiction du modèle uniquement (L5)
nav_order: 806
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Varenicline : nouvelle indication prédite, Trouble migraineux (migraine disorder) (niveau de preuve L5). Indication d'origine : Non renseignee dans les donnees d'AMM compilees (le texte d'indicatio…"
---

# Varenicline
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

# Varenicline : Du Sevrage Tabagique au Trouble Migraineux

## Resume en Une Phrase

La varenicline (CHAMPIX) est un medicament d'aide au sevrage tabagique. Le modele TxGNN predit qu'elle pourrait etre efficace pour le **trouble migraineux**, mais **aucun essai clinique** ni **aucune publication evaluant le traitement de la migraine** ne soutient actuellement cette direction : la prediction repose uniquement sur le modele.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non renseignee dans les donnees d'AMM compilees (le texte d'indication est vide) |
| Nouvelle Indication Predite | Trouble migraineux (migraine disorder) |
| Score de Prediction TxGNN | 99,92 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Uniquement des AMM annulees |
| Nombre d'AMM | 3 (toutes annulees) |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action ne sont pas disponibles dans les donnees compilees. Sur la base des informations connues, la varenicline est un agoniste partiel des recepteurs nicotiniques de l'acetylcholine alpha4beta2 et un agoniste complet des recepteurs alpha7. Elle est utilisee pour l'aide au sevrage tabagique, ou elle reduit l'envie de fumer et les symptomes de sevrage.

La signalisation cholinergique nicotinique intervient dans les voies trigemino-vasculaires et dans la depression corticale envahissante, impliquees dans la migraine. Un mecanisme est donc plausible, mais il reste **speculatif** et n'a pas ete demontre.

Plusieurs elements plaident par ailleurs contre un benefice : les cephalees et les nausees sont des effets indesirables frequents de la varenicline. Le score TxGNN tres eleve (0,999) est une prediction du modele, pas une preuve clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associe enregistre actuellement.

## Preuves de la Litterature

Une seule publication est rattachee a la migraine dans les donnees compilees, et il s'agit d'un rapport de cas d'un effet indesirable, non d'une etude de benefice therapeutique :

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [19585710](https://pubmed.ncbi.nlm.nih.gov/19585710/) | 2009 | Rapport de cas | Therapie | Arret cardiaque sous varenicline (resume non disponible) ; ne concerne pas le traitement de la migraine |

Pour la categorie voisine « trouble cephalalgique » (13 publications), les articles recuperes portent sur le sevrage tabagique et la securite du medicament, et la cephalee y apparait comme un **effet indesirable** (par exemple, un cas de cephalee liee au bain induite par la varenicline, PMID 23175211), et non comme une cible therapeutique.

## Informations de Marche en France

Les 3 AMM listees ci-dessous sont toutes **annulees**. Le texte d'indication approuvee n'est pas renseigne.

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 66287152 | CHAMPIX 0,5 mg et 1 mg, comprime pellicule | Comprime pellicule | Non renseignee |
| 65586162 | CHAMPIX 0,5 mg, comprime pellicule | Comprime pellicule | Non renseignee |
| 60442838 | CHAMPIX 1 mg, comprime pellicule | Comprime pellicule | Non renseignee |

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances (non issues de la notice)** : trouble anxieux, trouble nevrotique, trouble dysthymique, trouble bipolaire, trouble affectif majeur, abus/dependance a une substance, syndrome coronarien aigu, maladie vasculaire peripherique, claudication intermittente, arteriopathie peripherique, schizophrenie.
- **Interactions Medicamenteuses** : 104 interactions repertoriees. Parmi celles listees, la cimetidine est d'un niveau mineur ; les autres (par exemple vitamine A, phentermine, pantoprazole, metformine, morphine, simvastatine, prednisone, epinephrine) sont de niveau non precise.
- **Signaux de la litterature** : cephalees et nausees comme effets indesirables courants ; un cas d'arret cardiaque rapporte.

Les mises en garde et contre-indications de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de securite completes.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prediction est au niveau L5 (modele seul) : aucun essai clinique, aucune etude therapeutique, et un profil d'effets indesirables (cephalees) allant a l'encontre d'un benefice. Les AMM francaises sont toutes annulees, et les donnees de securite de la notice sont absentes.
- Les autres indications predites (alopecie, glaucome, hypertension pulmonaire, etc.) sont egalement au niveau L5 sans preuve.

**Pour avancer, les elements suivants sont necessaires :**
- Recuperer les mises en garde et contre-indications de la notice aupres de l'ANSM (point bloquant pour le criblage de securite)
- Obtenir les donnees de mecanisme d'action detaillees (DrugBank)
- Obtenir des donnees precliniques ou cliniques specifiques a la migraine
- Clarifier le statut reglementaire (AMM annulees) et l'indication originale
- Evaluer la contre-indication potentielle liee aux troubles psychiatriques et cardiovasculaires dans la population migraineuse
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

