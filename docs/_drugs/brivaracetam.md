---
layout: default
title: Brivaracetam
parent: Prédiction du modèle uniquement (L5)
nav_order: 116
evidence_level: L5
indication_count: 1
monitor_inn: "brivaracetam"
predicted_indications: ["beta-ketothiolase deficiency"]
last_modified_at: 2026-11-20
description: "Brivaracetam : nouvelle indication prédite, Déficit en bêta-cétothiolase (beta-ketothiolase deficiency) (niveau de preuve L5). En France, AMM dans la BDPM : 7 (valides : 7)"
---

# Brivaracetam
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Brivaracetam : inhibiteur de la liaison SV2A → déficit en bêta-cétothiolase (beta-ketothiolase deficiency)
{: .text-alpha }

## Résumé en Une Phrase

Le brivaracétam est un médicament antiépileptique dont les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Le modèle TxGNN prédit qu'il pourrait être utile pour le **déficit en bêta-cétothiolase (beta-ketothiolase deficiency)**. Aucun essai clinique ni aucune publication ne soutient actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Déficit en bêta-cétothiolase (beta-ketothiolase deficiency) |
| Score de Prédiction TxGNN | 0,9914 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 7 sur 7) |
| Nombre d'AMM | 7 (valides : 7) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Brivaracetam (traduction non officielle) : « Le mécanisme précis par lequel BRIVIACT exerce son activité anticonvulsivante n'est pas connu. Le brivaracétam présente une affinité élevée et sélective pour la protéine 2A des vésicules synaptiques (SV2A) dans le cerveau, ce qui pourrait contribuer à l'effet anticonvulsivant. » Texte original en anglais : "The precise mechanism by which BRIVIACT exerts its anticonvulsant activity is not known. Brivaracetam displays a high and selective affinity for synaptic vesicle protein 2A (SV2A) in the brain, which may contribute to the anticonvulsant effect." ([DailyMed: Briviact (brivaracetam) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3cf2f439-0e97-443e-8e33-25ecef616f6c), version du 2026-11-05 ; consulté le 2026-11-19). Le brivaracétam est connu comme un ligand de la protéine SV2A (protéine des vésicules synaptiques), mais cette information ne permet pas, à elle seule, d'expliquer un effet dans la maladie prédite.

Le déficit en bêta-cétothiolase est une maladie héréditaire du métabolisme des corps cétoniques et de l'isoleucine. Son lien avec un ligand de SV2A reste peu clair. Il reflète probablement une association indirecte détectée par le modèle, par exemple via des manifestations de type crises convulsives ou encéphalopathie métabolique. Il n'existe aucune preuve clinique ou préclinique à l'appui. La similarité avec l'usage d'origine n'a pas été évaluée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les données locales recensent 7 AMM pour des spécialités à base de brivaracétam (Briviact), toutes à substance unique, exploitées par UCB Pharma Belgique. Les formes disponibles sont les comprimés pelliculés, la solution buvable et la solution injectable ou pour perfusion. Le brivaracétam est commercialisé en France.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 64065772 | BRIVIACT 10 mg, comprimé pelliculé | comprimé pelliculé |
| 67429003 | BRIVIACT 10 mg/ml, solution buvable | solution buvable |
| 63546596 | BRIVIACT 100 mg, comprimé pelliculé | comprimé pelliculé |
| 64872342 | BRIVIACT 25 mg, comprimé pelliculé | comprimé pelliculé |
| 60579228 | BRIVIACT 10 mg/ml, solution injectable/pour perfusion | solution injectable ou pour perfusion |

## Considérations de Sécurité

- **Interactions médicamenteuses** : 69 interactions sont recensées. Parmi les principales, de niveau modéré : morphine (y compris liposomale), opium, dronabinol, nabilone, métoclopramide, sibutramine, difénoxine, diphénoxylate, éthanol, prométhazine et clopidogrel. De niveau mineur : inhibiteurs de la pompe à protons (oméprazole, ésoméprazole, lansoprazole, dexlansoprazole, pantoprazole), chlorpropamide, tolbutamide et cilostazol.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (score 0,9914), sans aucun essai clinique ni publication portant sur le déficit en bêta-cétothiolase, et le lien mécanistique est incertain. Le niveau de preuve est L5.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action du brivaracétam
- Études précliniques ou de mécanisme explorant un lien avec le métabolisme des corps cétoniques et de l'isoleucine
- Mises en garde et contre-indications issues de la notice de l'ANSM, pour permettre un examen de sécurité
- Évaluation de la compatibilité des voies d'administration et de la similarité avec l'usage d'origine

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Briviact (brivaracetam) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3cf2f439-0e97-443e-8e33-25ecef616f6c) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

