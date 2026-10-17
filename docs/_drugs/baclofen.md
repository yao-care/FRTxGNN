---
layout: default
title: Baclofen
parent: Prédiction du modèle uniquement (L5)
nav_order: 89
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Baclofen : nouvelle indication prédite, Dépendance à la nicotine (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM (spasticité d'après les formes…"
monitor_inn: "baclofen"
predicted_indications: ["attention deficit-hyperactivity disorder", "nicotine dependence"]
---

# Baclofen
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Baclofène : De la spasticité à la dépendance à la nicotine

## Résumé en Une Phrase

Le baclofène est un agoniste des récepteurs GABA-B, utilisé à l'origine dans le traitement de la spasticité (voie orale et voie intrathécale). Le modèle TxGNN prédit qu'il pourrait être efficace pour la **dépendance à la nicotine** (prédiction classée en premier : le trouble déficitaire de l'attention avec hyperactivité, TDAH, n'est étayé par aucune donnée clinique). Les données compilées pour ce rapport comptent **3 essais cliniques de Phase 2** et **18 publications** sur cette indication, sans résultat d'efficacité disponible.

> Remarque : l'indication d'origine n'est pas renseignée dans les données réglementaires compilées ; la spasticité est indiquée d'après les connaissances générales sur le baclofène et les formes pharmaceutiques recensées (intrathécales et orales).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM (spasticité d'après les formes pharmaceutiques) |
| Nouvelle Indication Prédite | Dépendance à la nicotine |
| Score de Prédiction TxGNN | 99,19 % |
| Niveau de Preuve | L2 (selon l'évaluation des données ; voir la réserve ci-dessous) |
| Statut de Marché en France | Retiré (toutes les AMM annulées) |
| Nombre d'AMM | 20 (dont 20 annulées) |
| Décision Recommandée | Hold |

> Réserve sur le niveau de preuve : la grille L1-L5 exige un essai de Phase 2/3 *complété* pour le niveau L2. Un seul essai de Phase 2 est complété (NCT01821560, n = 44), de nature mécanistique et sans résultat fourni ; les deux autres ont été arrêtés prématurément. Le niveau L2 est donc à considérer comme un plafond, un niveau L4 pouvant être plus prudent.

> Note : le premier candidat de la liste (TDAH, score 99,32 %) n'a aucune preuve clinique (niveau L5, Hold). Ce rapport retient la dépendance à la nicotine, seconde prédiction, car elle dispose de données cliniques.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances établies, le baclofène est un agoniste des récepteurs GABA-B. Son efficacité sur la spasticité repose sur l'inhibition de la transmission des réflexes au niveau médullaire.

Dans la dépendance à la nicotine, l'hypothèse est que l'activation des récepteurs GABA-B atténue la libération de dopamine dans le système mésolimbique. Cela réduirait les effets de récompense de la nicotine, ainsi que l'envie de fumer et les symptômes de sevrage. Des études précliniques chez le rongeur (PMID 24553576, 18682277, 19250803) rapportent une atténuation de la récompense nicotinique, du sevrage et de la reprise de la recherche de nicotine.

Le lien avec l'indication d'origine est indirect : il s'agit du même mécanisme pharmacologique (modulation GABAergique), appliqué à un circuit différent (neuromusculaire vs récompense). Des revues décrivent aussi le baclofène comme option de repositionnement dans l'alcoolo-dépendance, ce qui renforce la plausibilité d'une action sur les addictions. Ces revues ne constituent toutefois pas une preuve d'efficacité dans le sevrage tabagique.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01228994](https://clinicaltrials.gov/study/NCT01228994) | Phase 2 | Arrêté | 6 | Baclofène vs placebo sur l'abstinence tabagique ; arrêté avec 6 participants, sans puissance suffisante |
| [NCT00257894](https://clinicaltrials.gov/study/NCT00257894) | Phase 2 | Arrêté | 41 | Effet du baclofène sur l'envie de fumer, le sevrage et le renforcement chez les fumeurs modérés à importants ; arrêt précoce |
| [NCT01821560](https://clinicaltrials.gov/study/NCT01821560) | Phase 2 | Terminé | 44 | Effets sur le cerveau (IRM de perfusion) et le comportement face aux signaux associés au tabac ; étude surtout mécanistique, sans résultat fourni |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [24553576](https://pubmed.ncbi.nlm.nih.gov/24553576/) | 2014 | Préclinique (animal) | Psychopharmacology | Atténuation par le baclofène de la récompense nicotinique et du sevrage chez le rongeur |
| [18682277](https://pubmed.ncbi.nlm.nih.gov/18682277/) | 2008 | Préclinique (animal) | Neuroscience Letters | Effets du baclofène sur la préférence de place conditionnée induite par la nicotine chez le rat ; effet sélectif à forte dose (3 mg/kg) |
| [19250803](https://pubmed.ncbi.nlm.nih.gov/19250803/) | 2009 | Préclinique (animal) | Eur Neuropsychopharmacol | Prévention de la reprise de la recherche de nicotine chez le rongeur |
| [11841892](https://pubmed.ncbi.nlm.nih.gov/11841892/) | 2002 | Revue | Drug Alcohol Depend | Les agonistes GABA-B réduisent les effets renforçants de plusieurs substances, dont la nicotine |
| [24971600](https://pubmed.ncbi.nlm.nih.gov/24971600/) | 2015 | Revue | Neuropharmacology | Récepteurs GABA-B comme cible dans les troubles liés aux substances |
| [24654737](https://pubmed.ncbi.nlm.nih.gov/24654737/) | 2014 | Revue | Expert Opin Emerg Drugs | Mise à jour sur les médicaments émergents contre la dépendance au tabac |
| [29250815](https://pubmed.ncbi.nlm.nih.gov/29250815/) | 2018 | Revue | Pharmacotherapy | Traitements actuels et émergents du sevrage tabagique |
| [25868070](https://pubmed.ncbi.nlm.nih.gov/25868070/) | 2015 | Résumé de congrès (ECR) | Neuropsychopharmacology | Essai randomisé en double aveugle contre placebo sur la dépendance concomitante à l'alcool et à la nicotine ; résumé sans texte disponible |
| [38555115](https://pubmed.ncbi.nlm.nih.gov/38555115/) | 2024 | Revue | Int Rev Neurobiol | Repositionnement de médicaments dans le trouble de l'usage d'alcool (baclofène cité) |

## Informations de Marché en France

Les 20 AMM recensées sont toutes annulées ; aucun texte d'indication n'est renseigné. Cinq AMM sont présentées à titre d'illustration.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65672615 | BACLOFENE AGUETTANT 0,05 mg/ml | Solution injectable (intrathécale) | Non renseignée |
| 63914016 | BACLOFENE AGUETTANT 2 mg/ml | Solution pour perfusion (intrathécale) | Non renseignée |
| 62857313 | SPACYR 2 mg/mL | Solution injectable ou pour perfusion | Non renseignée |
| 65317023 | LIORESAL 10 mg/5 ml | Solution injectable (intrathécale) | Non renseignée |
| 60304050 | LIORESAL 10 mg | Comprimé sécable | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (non issues de la notice)** : épilepsie, maladie rénale, troubles psychotiques et schizophrénie (y compris schizo-affectif et schizophréniforme), troubles mentaux, accident vasculaire cérébral et maladies cérébrovasculaires, infarctus cérébral, maladies du système nerveux autonome (dont dysréflexie autonome et syndrome de Horner), maladie du col de la vessie, pyo-uretère.
- **Interactions médicamenteuses** : 120 interactions recensées. Principales interactions majeures : **morphine** (y compris liposomale), avec risque de dépression du système nerveux central. Interactions modérées : dronabinol, nabilone, métoclopramide, opium, sibutramine, difénoxine, diphénoxylate.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être compilées. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Trois essais de Phase 2 existent chez les fumeurs, mais deux ont été arrêtés prématurément (dont un avec 6 participants), et aucun résultat d'efficacité n'est disponible. Le mécanisme est plausible, mais les preuves cliniques restent insuffisantes.
- Toutes les AMM françaises sont annulées, et les données de sécurité officielles manquent (lacune bloquante), ce qui empêche d'avancer vers un dépistage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser les notices officielles (ANSM) pour les mises en garde et contre-indications
- Obtenir les données détaillées du mécanisme d'action (DrugBank)
- Obtenir les résultats publiés des essais NCT01821560 et NCT00257894, et vérifier le résumé de l'essai randomisé PMID 25868070
- Clarifier l'indication d'origine et le statut réglementaire actuel du baclofène en France
- Concevoir, si pertinent, un essai de Phase 2b/3 correctement dimensionné avec un critère principal d'abstinence tabagique
- Évaluer la faisabilité de la voie orale, la voie intrathécale étant inadaptée à cette indication
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

