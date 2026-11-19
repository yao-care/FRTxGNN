---
layout: default
title: Benzylpenicillin
parent: Prédiction du modèle uniquement (L5)
nav_order: 100
evidence_level: L5
indication_count: 7
monitor_inn: "benzylpenicillin"
predicted_indications: ["pericoronitis", "gingival recession", "canker sore", "ulcerative stomatitis", "denture stomatitis", "chemotherapy-induced oral mucositis", "leukoplakia of gingiva"]
last_modified_at: 2026-10-28
description: "Benzylpenicillin : nouvelle indication prédite, Péricoronarite (pericoronitis) (niveau de preuve L5). En France, AMM dans la BDPM : 2 (valides : 2)"
---

# Benzylpenicillin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

## Benzylpénicilline : antibiotique de la famille des pénicillines → Péricoronarite (pericoronitis)
{: .text-alpha }

## Résumé en Une Phrase

La benzylpénicilline est un antibiotique de la famille des pénicillines, administré par voie parentérale.
Le modèle TxGNN prédit qu'elle pourrait être utile pour la **péricoronarite (pericoronitis)**,
mais aucun essai clinique ni aucune publication ne soutient actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Péricoronarite (pericoronitis) |
| Score de Prédiction TxGNN | 0,9936 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Clinical Pharmacology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Benzylpenicillin (traduction non officielle) : « Les pénicillines se lient aux protéines sériques, principalement à l'albumine. Des concentrations thérapeutiques de pénicillines sont facilement atteintes, dans des circonstances normales, dans le liquide extracellulaire et la plupart des autres tissus de l'organisme. Les pénicillines se distribuent à des degrés divers dans les liquides pleural, péricardique, péritonéal, d'ascite, synovial et interstitiel. » Texte original en anglais : "Penicillins bind to serum proteins, mainly albumin. Therapeutic levels of the penicillins are easily achieved under normal circumstances in extracellular fluid and most other body tissues. Penicillins are distributed in varying degrees into pleural, pericardial, peritoneal, ascitic, synovial, and interstitial fluids." ([DailyMed: Pfizerpen (penicillin g potassium) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=efef4846-9497-41af-8dd6-518f86eca7f2), version du 2026-11-04 ; consulté le 2026-11-19). Sur la base des informations connues, la benzylpénicilline appartient à la classe des pénicillines, antibiotiques actifs sur les streptocoques et sur de nombreuses bactéries anaérobies de la bouche.

La péricoronarite est une infection polymicrobienne (anaérobies mixtes et streptocoques) des tissus mous autour d'une dent partiellement sortie. L'activité antibactérienne de la benzylpénicilline rend donc la prédiction plausible sur le plan biologique, et les pénicillines sont déjà utilisées dans les infections d'origine dentaire.

Cette plausibilité repose toutefois uniquement sur le score du modèle (0,9936) et sur un raisonnement antibactérien général. Aucune donnée clinique n'a été compilée pour la confirmer.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60243544 | PENICILLINE G PANPHARMA 1 000 000 UI, poudre pour usage parentéral | Poudre pour usage parentéral | Non renseignée |
| 65922570 | PENICILLINE G PANPHARMA 5 000 000 UI, poudre pour usage parentéral | Poudre pour usage parentéral | Non renseignée |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 21 interactions ont été recensées dans les données compilées pour ce rapport.
  - **Majeure** : méthotrexate.
  - **Modérées** : doxycycline, minocycline, tétracycline, déméclocycline, oxytétracycline, chloramphénicol, warfarine, dicoumarol, éthinylestradiol, acide mycophénolique, acide picosulfurique, iodure I-123, iodure I-131.
  - **Mineures** : clarithromycine, érythromycine.
  - **Niveau non précisé** : salbutamol, aciclovir, gentamicine, lévothyroxine.

Veuillez consulter la notice pour les autres informations de sécurité (mises en garde et contre-indications).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau de preuve L5) : aucun essai clinique ni publication ne porte sur la péricoronarite. Le mécanisme d'action et les données de sécurité de la notice font en outre défaut.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice (mises en garde et contre-indications) auprès de l'ANSM.
- Compléter les données sur le mécanisme d'action.
- Rechercher des essais cliniques ou des publications portant directement sur la benzylpénicilline dans la péricoronarite.
- Vérifier la compatibilité de la voie d'administration (parentérale) avec cette infection buccale.

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Pfizerpen (penicillin g potassium) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=efef4846-9497-41af-8dd6-518f86eca7f2) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

