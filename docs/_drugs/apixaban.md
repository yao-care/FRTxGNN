---
layout: default
title: Apixaban
parent: Prédiction du modèle uniquement (L5)
nav_order: 68
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-04
monitor_inn: "APIXABAN"
predicted_indications: ["migraine disorder"]
description: "Apixaban : nouvelle indication prédite, Trouble migraineux (migraine disorder) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Apixaban
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

## Apixaban: Trouble migraineux (migraine disorder)
{: .text-alpha }

## Résumé en une phrase

L'apixaban est un anticoagulant oral, inhibiteur direct du facteur Xa.
Le modèle TxGNN le prédit comme potentiellement efficace pour le **trouble migraineux (migraine disorder)**, mais le niveau de preuve est **L5** : aucune étude ne soutient cette direction. Les données compilées pour ce rapport contiennent **1 essai clinique** (sur la prévention des récidives d'AVC, indirect) et **3 publications**, dont deux cas cliniques décrivant une migraine avec aura aggravée ou non résolue sous apixaban.

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Non renseignée dans les données locales |
| Nouvelle indication prédite | Trouble migraineux (migraine disorder) |
| Score de prédiction TxGNN | 0.9902 |
| Niveau de preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 6 sur 6) |
| Nombre d'AMM | 6 (valides : 6) |
| Décision recommandée | Hold |

## Pourquoi cette prédiction est-elle raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances générales, l'apixaban est un inhibiteur direct du facteur Xa de la coagulation.

Une hypothèse théorique relierait la migraine avec aura au foramen ovale perméable, aux micro-embolies paradoxales ou à un état prothrombotique (par exemple en présence d'anticorps antiphospholipides) : une anticoagulation pourrait alors réduire les déclencheurs micro-emboliques. Il s'agit toutefois d'une hypothèse, sans voie biologique établie.

Les données disponibles ne la confortent pas. Un cas rapporte une migraine avec aura aggravée après l'instauration de l'apixaban ; un autre décrit une rémission sous warfarine, mais pas sous apixaban. Cela ne plaide pas pour un bénéfice de classe des anticoagulants et suggère que l'apixaban pourrait être inefficace, voire délétère. Le score élevé du modèle reflète une prédiction fondée sur des relations statistiques, pas une démonstration biologique.

## Preuves d'essais cliniques

| Numéro d'essai | Phase | Statut | Inscription | Résultats principaux |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Terminé | 664 | Fermeture du foramen ovale perméable ou anticoagulants versus antiagrégants pour prévenir la récidive d'AVC. Population et critère principal portent sur l'AVC cryptogénique, pas sur la migraine ; preuve indirecte. |

## Preuves de la littérature

| PMID | Année | Type | Revue | Résultats principaux |
|------|-----|------|------|---------|
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Cas clinique / revue | The Neurologist | Migraine avec aura aggravée après l'initiation de l'apixaban ; l'effet des anticoagulants oraux directs sur la migraine reste peu clair, la littérature étant rare et controversée. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Cas clinique | Headache | Patiente dont la migraine avec aura était en rémission sous warfarine ; les symptômes sont revenus en 3 semaines sous apixaban et ont disparu après la reprise de la warfarine. |
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Étude rétrospective (75 patients) | Lupus | Réponse au traitement antithrombotique chez des patients atteints de migraine réfractaire avec anticorps antiphospholipides ; données spécifiques à l'apixaban non vérifiées. |

## Informations de marché en France

L'apixaban est commercialisé en France (6 AMM valides, spécialité ELIQUIS, Bristol-Myers Squibb / Pfizer EEIG).

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62111096 | ELIQUIS 0,15 mg, granulés en gélule à ouvrir | Granulés en gélule | Non renseignée (AMM active) |
| 61902218 | ELIQUIS 5 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM active) |
| 69340279 | ELIQUIS 2,5 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM active) |
| 63078845 | ELIQUIS 0,5 mg, granulés enrobés en sachet | Granulés enrobés | Non renseignée (AMM active) |
| 61425336 | ELIQUIS 2 mg, granulés enrobés en sachet | Granulés enrobés | Non renseignée (AMM active) |

## Considérations de sécurité

- **Interactions médicamenteuses** : 100 interactions sont recensées dans les données compilées ; parmi les principales, de niveau **majeur** : acide acétylsalicylique, cobicistat, déférasirox, ibritumomab tiuxétan, tositumomab (y compris marqué à l'iode 131). Interactions de niveau **modéré** : aprépitant, clarithromycine, clotrimazole, dexaméthasone, miconazole, rolapitant, fenfluramine, dexfenfluramine, sibutramine, éliglustat, troglitazone, sugammadex, iodure I-123 et I-131.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
- Le niveau de preuve est L5 : aucune étude ne soutient l'apixaban dans la migraine, et les deux cas cliniques disponibles décrivent une aggravation ou une absence de résolution sous apixaban. Le score TxGNN élevé (0,9902) ne suffit pas à justifier une avancée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action et sur un lien biologique plausible avec la migraine
- Mises en garde et contre-indications issues de la notice
- Études cliniques évaluant directement l'apixaban dans la migraine (notamment avec aura ou associée à un foramen ovale perméable), avec une attention particulière à un éventuel effet délétère
- Analyse du rapport bénéfice/risque hémorragique dans cette population

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

