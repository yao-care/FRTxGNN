---
layout: default
title: Mercaptopurine
parent: Preuves élevées (L1-L2)
nav_order: 191
evidence_level: L2
indication_count: 10
---

# Mercaptopurine
{: .fs-9 }

Niveau de preuve: **L2** | Indications prédites: **10** 
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

# Mercaptopurine : De la Leucémie Aiguë Lymphoblastique à la Leucémie Myéloïde

## Résumé en Une Phrase

La mercaptopurine est un antimétabolite analogue de la purine. Son usage établi est le traitement d'entretien de la leucémie aiguë lymphoblastique, d'après les données de littérature du dossier, car le texte d'indication de l'AMM n'est pas renseigné.
Le modèle TxGNN prédit qu'elle pourrait être efficace dans la **leucémie myéloïde**, avec **29 essais cliniques** associés, dont 7 essais de Phase 3 terminés. Aucune publication n'a été retrouvée pour cette indication.
Dans la plupart de ces essais, la mercaptopurine n'est qu'un composant du traitement d'entretien de la leucémie aiguë promyélocytaire (ATRA + méthotrexate + 6-MP), si bien que sa contribution propre n'est pas isolée.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Leucémie myéloïde |
| Score de Prédiction TxGNN | 99,94 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

Le niveau L2 tient compte du fait qu'un seul essai de Phase 3 terminé est classé comme preuve directe (grade A). Les autres essais de Phase 3 ne permettent pas d'isoler l'effet de la mercaptopurine.

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action (DrugBank) ne sont pas disponibles actuellement. Le dossier fournit toutefois une explication mécanistique. La mercaptopurine est un antimétabolite purique : l'enzyme HGPRT la convertit en monophosphate de thioinosine, qui inhibe la synthèse de novo des purines. Ses métabolites, les nucléotides de thioguanine, s'incorporent à l'ADN et à l'ARN des cellules à division rapide, comme les blastes myéloïdes.

Dans la leucémie aiguë lymphoblastique, cette action est la base du traitement d'entretien. Les leucémies myéloïdes sont aussi des hémopathies à prolifération rapide, ce qui rend l'extension mécanistiquement plausible. Dans les essais retrouvés, la mercaptopurine intervient surtout dans le schéma d'entretien de la leucémie aiguë promyélocytaire (ATRA + méthotrexate + 6-MP). Elle n'a donc pas été évaluée seule dans la leucémie myéloïde.

Il s'agit d'une indication de niche plutôt que d'une extension large aux leucémies myéloïdes. Deux essais précoces récents testent directement la 6-MP dans la LAM : une association avec le vénétoclax (Phase 1) et une association avec l'acide valproïque (Phase 1/2). Aucun résultat n'est disponible pour l'instant.

---

## Preuves d'Essais Cliniques

29 essais sont associés à cette prédiction. Les 10 plus pertinents sont listés ci-dessous. Le dossier ne contient aucun résultat publié, donc la dernière colonne décrit le plan de chaque étude et non ses résultats.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00492856](https://clinicaltrials.gov/study/NCT00492856) | Phase 3 | Terminé | 105 | Entretien versus observation dans la LAP à risque faible/intermédiaire ; le schéma d'entretien est ATRA/méthotrexate/6-MP (preuve la plus directe, grade A) |
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Phase 3 | Terminé | 420 | LAP non traitée : trétinoïne + chimiothérapie avec ou sans trioxyde d'arsenic, puis entretien randomisé tretinoïne seule versus tretinoïne + mercaptopurine + méthotrexate |
| [NCT00408278](https://clinicaltrials.gov/study/NCT00408278) | Phase 4 | Terminé | 300 | PETHEMA LPA 2005 : LAP avec entretien ATRA + faibles doses de méthotrexate + mercaptopurine |
| [NCT01064557](https://clinicaltrials.gov/study/NCT01064557) | Non applicable | Inconnu | 1068 | Protocole AIDA : rôle de l'entretien par ATRA intermittent, méthotrexate + 6-MP, ou des deux |
| [NCT00180128](https://clinicaltrials.gov/study/NCT00180128) | Phase 4 | Inconnu | 80 | AIDA2000 : thérapie adaptée au risque dans la LAP, avec deux ans d'entretien 6-MP + méthotrexate + ATRA (non randomisé) |
| [NCT00866918](https://clinicaltrials.gov/study/NCT00866918) | Phase 3 | Terminé | 106 | LAP de l'enfant, traitement adapté au risque avec trioxyde d'arsenic en consolidation ; la 6-MP fait probablement partie de l'entretien |
| [NCT00482833](https://clinicaltrials.gov/study/NCT00482833) | Phase 3 | Terminé | 276 | Trioxyde d'arsenic + ATRA versus ATRA + chimiothérapie (AIDA) dans la LAP à risque non élevé |
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Phase 1 | En recrutement | 10 | Vénétoclax + 6-mercaptopurine dans la LAM en rechute ou réfractaire (étude de phase Ib) |
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Phase 1/2 | En recrutement | 48 | Hydroxyurée + acide valproïque, ou 6-MP + acide valproïque, dans la LAM ou le SMD à haut risque non éligibles au traitement standard |
| [NCT00465933](https://clinicaltrials.gov/study/NCT00465933) | Phase 4 | Terminé | Non disponible | LAP : induction AIDA, entretien ATRA + méthotrexate + mercaptopurine, traitement de rattrapage des rechutes moléculaires et hématologiques |

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 63377491 | PURINETHOL 50 mg, comprimé | Comprimé | ASPEN PHARMA TRADING (IRLANDE) |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (antimétabolite, analogue de la purine) |
| Risque de Myélosuppression | Élevé à modéré : la myélosuppression est la toxicité limitante, dépendante de la dose et des variants TPMT/NUDT15 |
| Classification d'Émétogénicité | Faible |
| Éléments de Surveillance | NFS avec formule, fonction hépatique, génotypage TPMT/NUDT15 avant traitement |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques |

Ces éléments sont établis à partir de la classe pharmacologique et de la littérature du dossier. Ils ne proviennent pas de la notice ANSM, qui n'a pas pu être exploitée. Veuillez consulter les mises en garde et précautions de la notice.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le criblage de sécurité est bloqué faute de mises en garde et contre-indications issues de la notice ANSM.
- L'effet propre de la mercaptopurine dans la leucémie myéloïde n'est pas isolé : elle n'est qu'un élément du schéma d'entretien de la LAP, et les seuls essais ciblant la LAM avec la 6-MP sont précoces et sans résultats.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications, interactions).
- Obtenir les données sur le mécanisme d'action depuis DrugBank.
- Exploiter les résultats de l'entretien randomisé de NCT00003934, qui compare tretinoïne seule et tretinoïne + mercaptopurine + méthotrexate, pour isoler la contribution de la 6-MP.
- Attendre les résultats de NCT05506332 et NCT06199557 pour la LAM.
- Prévoir un plan de sécurité : génotypage TPMT/NUDT15, suivi de la NFS et de la fonction hépatique, et soutien à l'observance.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

