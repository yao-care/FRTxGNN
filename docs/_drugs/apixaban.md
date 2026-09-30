---
layout: default
title: Apixaban
parent: Preuves modérées (L3-L4)
nav_order: 41
evidence_level: L4
indication_count: 1
---

# Apixaban
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **1** 
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

# Apixaban : De l'Anticoagulation (indication d'origine non renseignée) à la Migraine

## Résumé en Une Phrase

Apixaban est un anticoagulant oral direct, inhibiteur du facteur Xa, commercialisé en France sous le nom ELIQUIS. Les données réglementaires disponibles ne précisent pas le texte de ses indications approuvées.
Le modèle TxGNN prédit qu'il pourrait être utile dans la **migraine**, mais les preuves restent très faibles : **1 essai clinique** sans lien direct avec la migraine et **4 publications** (surtout des cas cliniques), dont certaines vont à l'encontre de l'hypothèse.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM (textes d'indication vides) |
| Nouvelle Indication Prédite | Migraine (migraine disorder) |
| Score de Prédiction TxGNN | 99,02 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 6 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les informations connues, l'apixaban est un inhibiteur direct du facteur Xa de la coagulation. Son efficacité comme anticoagulant est établie, et l'hypothèse est qu'il pourrait agir sur certains mécanismes de la migraine liés à la coagulation.

Le score élevé du modèle (0,99) vient probablement de liens dans le graphe de connaissances entre l'anticoagulation, le foramen ovale perméable (FOP) avec embolie paradoxale, et la migraine avec aura. L'idée est que des micro-emboles ou un état d'hypercoagulabilité contribueraient à certaines formes de migraine, notamment avec aura ou en présence d'anticorps antiphospholipides.

Cependant, ce lien est **non prouvé et en partie contredit** par les cas publiés. Chez les patients décrits, l'aura s'est aggravée ou n'a pas disparu sous apixaban, alors que la warfarine semblait soulager les mêmes patients. Un éventuel effet ne serait donc pas un effet de classe des anticoagulants et pourrait être propre aux antivitamines K.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Terminé | 664 | Essai CLOSE : fermeture du FOP vs anticoagulants vs antiagrégants pour prévenir la récidive d'AVC. La migraine n'était ni la condition étudiée ni le critère principal, et les anticoagulants n'étaient pas spécifiques à l'apixaban. |

Cet essai de Phase 3 ne fournit aucune preuve directe pour l'apixaban dans la migraine (pertinence : grade C). Il ne permet donc pas d'atteindre le niveau L1.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Étude rétrospective (75 patients) | Lupus | Essai d'un traitement antithrombotique chez des patients atteints de migraine réfractaire avec anticorps antiphospholipides. Les données spécifiques à l'apixaban ne sont pas confirmées. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Cas clinique | Headache | Femme de 55 ans en rémission de sa migraine avec aura pendant 12 ans sous warfarine. Les symptômes sont revenus en 3 semaines après le passage à l'apixaban, puis ont disparu en quelques jours à la reprise de la warfarine. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Cas clinique avec revue de la littérature | The Neurologist | Migraine avec aura aggravée après l'introduction de l'apixaban. Les données sur les anticoagulants oraux directs dans la migraine sont rares et controversées. |
| [29611190](https://pubmed.ncbi.nlm.nih.gov/29611190/) | 2018 | Cas clinique | Headache | Migraine vestibulaire résolue sous warfarine et topiramate (pas d'apixaban). |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62111096 | ELIQUIS 0,15 mg, granulés en gélule à ouvrir | Granulés en gélule | Non renseignée |
| 61902218 | ELIQUIS 5 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 69340279 | ELIQUIS 2,5 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 63078845 | ELIQUIS 0,5 mg, granulés enrobés en sachet | Granulés enrobés | Non renseignée |
| 61425336 | ELIQUIS 2 mg, granulés enrobés en sachet | Granulés enrobés | Non renseignée |

Le dossier compte 6 AMM au total ; les 5 premières sont listées. Le titulaire est BRISTOL-MYERS SQUIBB / PFIZER EEIG (Irlande).

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le niveau de preuve est L4 : il n'existe aucun essai spécifique de l'apixaban dans la migraine, et la littérature se limite à des cas cliniques et à une étude rétrospective non spécifique. Les cas publiés suggèrent même une absence de bénéfice, voire une aggravation, sous apixaban.
- Le dossier de sécurité issu de la notice ANSM est absent, ce qui empêche toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications, indications approuvées).
- Compléter les données sur le mécanisme d'action (par exemple via DrugBank).
- Analyser le mécanisme, notamment la différence entre antivitamines K et inhibiteurs du facteur Xa dans la migraine avec aura.
- Rechercher des études spécifiques à l'apixaban chez des patients migraineux, en particulier avec FOP ou anticorps antiphospholipides.
- Évaluer le rapport bénéfice/risque hémorragique chez des patients migraineux non anticoagulés avant toute étude clinique.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

