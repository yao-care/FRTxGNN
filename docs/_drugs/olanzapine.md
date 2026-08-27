---
layout: default
title: Olanzapine
parent: 僅模型預測 (L5)
nav_order: 218
evidence_level: L5
indication_count: 3
---

# Olanzapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Olanzapine : D'un Antipsychotique Établi à Trois Pistes de Repositionnement Psychiatrique

## Résumé en Une Phrase

Olanzapine est un antipsychotique déjà utilisé en clinique (association fixe avec la fluoxétine dans la dépression résistante, augmentation dans le trouble panique), pour lequel les données d'indication d'origine et de mécanisme d'action ne sont pas disponibles dans ce dossier. Le modèle TxGNN identifie **3 pistes de repositionnement** — torticollis paroxystique bénin du nourrisson, agoraphobie et trouble dysthymique — avec une force de preuve très inégale : **0 essai clinique dédié** et **12 publications** au total, concentrées sur l'agoraphobie et la dysthymie.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans ce dossier (classe : antipsychotique) |
| Statut de Marché en France | Non commercialisé (0 AMM enregistrée) |
| Nombre d'AMM | 0 |

### Comparatif des Indications Prédites

| Indication Prédite | Score TxGNN | Niveau de Preuve | Essais Cliniques | Publications | Décision |
|---|---|---|---|---|---|
| Agoraphobie | 99.47% | L3 | 0 | 7 | Research Question |
| Trouble Dysthymique | 99.28% | L4 | 0 | 5 | Hold |
| Torticollis Paroxystique Bénin du Nourrisson | 99.54% | L5 | 0 | 0 | Hold |

---

## Pourquoi Ces Prédictions Sont-elles Raisonnables ?

Les données détaillées sur le mécanisme d'action (MOA) de l'olanzapine ne sont pas disponibles dans ce dossier. Sur la base des informations connues issues de la littérature associée, l'olanzapine est un **antipsychotique** dont l'association fixe avec la fluoxétine (Symbyax) est déjà approuvée dans la dépression majeure résistante au traitement, ce qui offre un point d'ancrage mécanistique indirect pour explorer d'autres troubles de l'humeur et anxieux.

**Agoraphobie (L3) :** l'antagonisme 5-HT2A/D2 et l'effet sédatif antihistaminique de l'olanzapine sont déjà utilisés en pratique comme traitement d'appoint (augmentation) dans le trouble panique résistant au traitement. L'agoraphobie étant fréquemment comorbide du trouble panique, la littérature disponible porte surtout sur le trouble panique plutôt que sur un diagnostic isolé d'agoraphobie — une extension mécanistique plausible mais non spécifique.

**Trouble dysthymique (L4) :** le support mécanistique reste indirect (via Symbyax dans la dépression résistante). Une seule étude ouverte concerne des patients avec trouble de la personnalité borderline et dysthymie *comorbide* (non un diagnostic principal de dysthymie) ; le reste de la littérature correspond à des revues ou à des travaux portant sur une molécule différente (amisulpride).

**Torticollis paroxystique bénin du nourrisson (L5) :** aucun essai clinique ni aucune littérature ne soutient cette piste. Il s'agit d'un trouble vestibulaire auto-limitant du nourrisson, sans lien mécanistique plausible avec un antipsychotique qui présente par ailleurs des réserves de sécurité connues chez l'enfant. Cette association provient uniquement du graphe de connaissances TxGNN, sans validation externe.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement, pour les trois indications prédites (agoraphobie, trouble dysthymique, torticollis paroxystique bénin du nourrisson).

---

## Preuves de la Littérature

### Agoraphobie (7 publications)

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [16415705](https://pubmed.ncbi.nlm.nih.gov/16415705/) | 2006 | Essai ouvert (12 semaines) | Journal of Clinical Psychopharmacology | Augmentation par olanzapine (5 mg/j) chez 31 patients avec trouble panique résistant aux ISRS, avec ou sans agoraphobie |
| [26635099](https://pubmed.ncbi.nlm.nih.gov/26635099/) | 2016 | Revue | Expert Opinion on Pharmacotherapy | Revue systématique sur le trouble panique résistant au traitement, environ un tiers des patients restant symptomatiques |
| [40946318](https://pubmed.ncbi.nlm.nih.gov/40946318/) | 2025 | Revue | Psychotherapy and Psychosomatics | Revue intégrative des options pharmacologiques, psychothérapeutiques et neurostimulatoires dans les troubles anxieux résistants |
| [25012437](https://pubmed.ncbi.nlm.nih.gov/25012437/) | 2014 | Étude de cohorte | Journal of Affective Disorders | Impact des troubles anxieux comorbides (dont l'agoraphobie) sur l'évolution à 24 mois du trouble bipolaire de type I |
| [10739446](https://pubmed.ncbi.nlm.nih.gov/10739446/) | 2000 | Rapport de cas | American Journal of Psychiatry | Association clinique entre olanzapine et crises de panique (résumé non disponible) |
| [15470803](https://pubmed.ncbi.nlm.nih.gov/15470803/) | 2004 | Rapport de cas | Pharmacopsychiatry | Rémission complète d'un trouble panique réfractaire sous olanzapine + paroxétine associées |
| [17099612](https://pubmed.ncbi.nlm.nih.gov/17099612/) | 2006 | Rapport de cas | Psychiatria Danubina | Trouble panique avec agoraphobie comorbide d'une psychose, traité avec succès par TCC |

### Trouble Dysthymique (5 publications)

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Revue systématique (Cochrane) | Cochrane Database of Systematic Reviews | Antipsychotiques de seconde génération en association dans la dépression majeure et la dysthymie |
| [10578457](https://pubmed.ncbi.nlm.nih.gov/10578457/) | 1999 | Essai ouvert | Biological Psychiatry | Essai ouvert d'olanzapine chez des patients avec trouble borderline et dysthymie comorbide |
| [22938165](https://pubmed.ncbi.nlm.nih.gov/22938165/) | 2012 | Revue | Bipolar Disorders | Options fondées sur les preuves pour le trouble bipolaire résistant au traitement chez l'adulte |
| [11920152](https://pubmed.ncbi.nlm.nih.gov/11920152/) | 2002 | Revue narrative | Molecular Psychiatry | Benzamides substitués et leur potentiel dans la dysthymie et les symptômes négatifs de la schizophrénie |
| [34727399](https://pubmed.ncbi.nlm.nih.gov/34727399/) | 2021 | Revue systématique (molécule différente : amisulpride) | Human Psychopharmacology | Méta-analyse de l'amisulpride sur les symptômes dépressifs, non spécifique à l'olanzapine |

### Torticollis Paroxystique Bénin du Nourrisson

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

L'olanzapine n'est pas commercialisée en France selon ce dossier (0 AMM active enregistrée).

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision Globale : Hold**

**Justification :**
- Aucune des trois pistes ne dépasse le stade S2 (Recherche de piste) ; aucun essai clinique dédié n'existe pour ces indications.
- L'agoraphobie (L3) est la piste la plus étayée, portée par un essai ouvert positif dans le trouble panique/agoraphobie comorbide — elle mérite d'être suivie comme question de recherche, mais pas encore une décision d'avancement.
- La dysthymie (L4) et le torticollis paroxystique bénin du nourrisson (L5) manquent de fondement mécanistique ou clinique direct ; ce dernier soulève en outre une réserve de sécurité pédiatrique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications TFDA/ANSM (donnée bloquante, actuellement indisponible — nécessaire avant toute évaluation de sécurité S1)
- Mécanisme d'action détaillé (MOA) de l'olanzapine
- Un essai contrôlé randomisé ciblant spécifiquement l'agoraphobie (au-delà du trouble panique comorbide) pour faire progresser cette piste au-delà de L3
- Clarification du statut réglementaire réel en France (les données actuelles indiquent 0 AMM, à vérifier compte tenu de la commercialisation connue de l'olanzapine dans d'autres marchés)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

