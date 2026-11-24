---
layout: default
title: Dipyridamole
parent: Prédiction du modèle uniquement (L5)
nav_order: 249
evidence_level: L5
indication_count: 6
monitor_inn: "DIPYRIDAMOLE"
predicted_indications: ["sick sinus syndrome 2, autosomal dominant", "sarcoglycanopathy", "Wildervanck syndrome", "macrocephaly, dysmorphic facies, and psychomotor retardation", "cavernous sinus thrombosis", "lateral sinus thrombosis"]
last_modified_at: 2026-11-24
description: "Dipyridamole : nouvelle indication prédite, Sick sinus syndrome 2, autosomal dominant (niveau de preuve L5). En France, AMM dans la BDPM : 2 (valides : 2)"
---

# Dipyridamole
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Dipyridamole: Sick sinus syndrome 2, autosomal dominant
{: .text-alpha }

## Résumé en une phrase

Le dipyridamole est un antiagrégant plaquettaire commercialisé en France sous forme de comprimé enrobé et de solution injectable.
Le modèle TxGNN prédit qu'il pourrait être utile dans le **syndrome du sinus malade de type 2, autosomique dominant (sick sinus syndrome 2, autosomal dominant)**.
Cette prédiction repose uniquement sur le score du modèle : **aucun essai clinique et aucune publication** ne la soutiennent actuellement.

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Non renseignée dans les données locales |
| Nouvelle indication prédite | Sick sinus syndrome 2, autosomal dominant |
| Score de prédiction TxGNN | 0.9989 |
| Niveau de preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision recommandée | Hold |

## Pourquoi cette prédiction est-elle raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Dipyridamole (traduction non officielle) : « Le dipyridamole inhibe la captation de l'adénosine dans les plaquettes, les cellules endothéliales et les érythrocytes in vitro et in vivo ; l'inhibition se produit de manière dose-dépendante aux concentrations thérapeutiques (0,5 à 1,9 mcg/mL). Cette inhibition entraîne une augmentation des concentrations locales d'adénosine, qui agit sur le récepteur A 2 plaquettaire, stimulant ainsi l'adénylate cyclase plaquettaire et augmentant les taux plaquettaires d'adénosine monophosphate cyclique-3',5' (AMPc). » Texte original en anglais : "Dipyridamole inhibits the uptake of adenosine into platelets, endothelial cells and erythrocytes in vitro and in vivo; the inhibition occurs in a dose-dependent manner at therapeutic concentrations (0.5 to 1.9 mcg/mL). This inhibition results in an increase in local concentrations of adenosine which acts on the platelet A 2 -receptor thereby stimulating platelet adenylate cyclase and increasing platelet cyclic-3',5'-adenosine monophosphate (cAMP) levels." ([DailyMed: dipyridamole prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=226099e2-70bb-4b9b-bb52-c20fbca2aec5), version du 2026-04-29 ; consulté le 2026-11-19). D'après les connaissances pharmacologiques générales, le dipyridamole augmente l'adénosine extracellulaire et exerce ainsi un effet antiagrégant et vasodilatateur.

Ce mécanisme ne plaide pas clairement en faveur de la nouvelle indication. L'adénosine ralentit la conduction du nœud sinusal et du nœud auriculo-ventriculaire. Un médicament qui augmente son taux pourrait donc, en théorie, aggraver une dysfonction du nœud sinusal plutôt que la traiter.

Le score élevé du modèle reste donc une piste computationnelle. Il n'est étayé par aucune donnée clinique ni aucun argument mécanistique favorable identifié à ce jour.

## Preuves d'essais cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la littérature

Aucune littérature associée disponible actuellement.

## Informations de marché en France

Le dipyridamole est commercialisé en France. Les deux AMM recensées sont valides.

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 60021216 | PERSANTINE 75 mg, comprimé enrobé | Comprimé enrobé | GLENWOOD GMBH PHARMAZEUTISCHE ERZEUGNISSE | Active |
| 68572748 | PERSANTINE 10 mg/2 mL, solution injectable, ampoule | Solution injectable | GLENWOOD GMBH PHARMAZEUTISCHE ERZEUGNISSE | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de sécurité

- **Mises en garde et contre-indications** : les données de la notice ne sont pas disponibles dans les informations compilées. Veuillez consulter la notice pour ces informations.
- **Interactions médicamenteuses** : 100 interactions ont été recensées. Les plus notables, de niveau modéré, concernent :
  - la dexfenfluramine ;
  - la sibutramine ;
  - la fenfluramine.

  D'autres interactions, de niveau non classé, concernent notamment l'acide acétylsalicylique, la cimétidine, la metformine, la morphine, l'oméprazole, le pantoprazole, la simvastatine et la prednisone.
- **Point d'attention propre à cette prédiction** : le dipyridamole pouvant ralentir la conduction sinusale et auriculo-ventriculaire par l'adénosine, un risque d'aggravation d'une dysfonction du nœud sinusal doit être évalué avant toute exploration.

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
La prédiction n'est soutenue que par le score du modèle (niveau de preuve L5). Aucun essai ni aucune publication n'existe, et le mécanisme connu pourrait aller à l'encontre de l'effet recherché.

**Pour avancer, les éléments suivants sont nécessaires :**
- Un argument mécanistique démontrant un bénéfice plausible, ou au moins l'absence d'aggravation de la fonction sinusale.
- Des données précliniques ou cliniques portant directement sur cette pathologie.
- Les mises en garde et contre-indications issues de la notice, afin de réaliser le dépistage de sécurité.
- Les données détaillées sur le mécanisme d'action.

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: dipyridamole prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=226099e2-70bb-4b9b-bb52-c20fbca2aec5) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

