---
layout: default
title: Obinutuzumab
parent: 僅模型預測 (L5)
nav_order: 216
evidence_level: L5
indication_count: 3
---

# Obinutuzumab
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

# Obinutuzumab : De la Leucémie Lymphoïde Chronique au Lymphome Folliculaire

## Résumé en Une Phrase

Obinutuzumab est un anticorps monoclonal anti-CD20 initialement approuvé pour le traitement de la leucémie lymphoïde chronique (LLC), comme le confirment les données d'essais cliniques disponibles. Le modèle TxGNN identifie le **lymphome folliculaire** comme indication à fort potentiel (score 99,18 %), et il s'agit en réalité d'une indication déjà établie du médicament (non d'un signal de repositionnement inédit), soutenue par **50 essais cliniques** et **20 publications** dans ce jeu de données. Le modèle a également signalé deux sous-types de LLC/lymphome à petits lymphocytes (LLC/SLL) avec un score comparable, mais sans aucune preuve clinique associée — ces signaux sont traités séparément ci-dessous en raison d'un écart de données probable.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Leucémie lymphoïde chronique (LLC), en association avec le chlorambucil (source : résumé d'essai clinique NCT02877550) |
| Nouvelle Indication Prédite | Lymphome Folliculaire |
| Score de Prédiction TxGNN | 99,18 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✗ Non commercialisé (source : taiwan_regulatory) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Obinutuzumab est un anticorps monoclonal humanisé de type II dirigé contre l'antigène CD20, exprimé à la surface des lymphocytes B. Il agit en induisant la mort des cellules B malignes par cytotoxicité cellulaire dépendante des anticorps (ADCC), cytotoxicité dépendante du complément (CDC) et induction directe de l'apoptose.

La LLC et le lymphome folliculaire sont tous deux des néoplasies des lymphocytes B matures exprimant CD20 : le mécanisme d'action est donc directement applicable aux deux pathologies, sans nécessiter d'extrapolation mécanistique. Il convient de noter que, selon les résumés d'essais cliniques inclus dans ce jeu de données (notamment NCT02877550), obinutuzumab est déjà approuvé en association avec le chlorambucil pour la LLC non traitée et en association avec la bendamustine (puis en monothérapie d'entretien) pour le lymphome folliculaire. La prédiction TxGNN sur le lymphome folliculaire correspond donc à une **indication déjà établie du médicament**, et non à un signal de repositionnement au sens strict — ce qui explique le très haut niveau de preuve (L1) et le grand nombre d'essais disponibles.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01332968](https://clinicaltrials.gov/study/NCT01332968) | Phase 3 | Terminé | 1401 | Étude GALLIUM : obinutuzumab + chimiothérapie vs rituximab + chimiothérapie en 1ère ligne du lymphome indolent avancé ; essai pivot ayant conduit à l'approbation de l'indication FL |
| [NCT01059630](https://clinicaltrials.gov/study/NCT01059630) | Phase 3 | Terminé | 413 | Bendamustine seule vs bendamustine + obinutuzumab chez des patients atteints de LNH indolent réfractaire au rituximab |
| [NCT03817853](https://clinicaltrials.gov/study/NCT03817853) | Phase 4 | Terminé | 114 | Étude post-commercialisation évaluant la sécurité d'obinutuzumab en perfusion courte (90 min) dans le FL non traité avancé |
| [NCT04034056](https://clinicaltrials.gov/study/NCT04034056) | N/A | Terminé | 299 | Étude en vie réelle, rétrospective/prospective, évaluant efficacité et sécurité d'obinutuzumab en 1ère ligne du FL avancé |
| [NCT02611323](https://clinicaltrials.gov/study/NCT02611323) | Phase 1/2 | Terminé | 133 | Obinutuzumab + polatuzumab vedotin + venetoclax dans le FL récidivant/réfractaire |
| [NCT02600897](https://clinicaltrials.gov/study/NCT02600897) | Phase 1/2 | Terminé | 114 | Obinutuzumab + polatuzumab vedotin + lénalidomide dans le FL récidivant/réfractaire |
| [NCT03113422](https://clinicaltrials.gov/study/NCT03113422) | Phase 2 | Terminé | 56 | Venetoclax + obinutuzumab + bendamustine en 1ère ligne du FL à forte masse tumorale |
| [NCT05899621](https://clinicaltrials.gov/study/NCT05899621) | N/A | En cours | 332 | Étude en vie réelle sur l'efficacité et la sécurité d'un traitement à base d'obinutuzumab en 1ère ligne du FL |
| [NCT05783596](https://clinicaltrials.gov/study/NCT05783596) | Phase 2 | Actif, non recrutant | 47 | Glofitamab + obinutuzumab en 1ère ligne du FL et du lymphome de la zone marginale |
| [NCT03332017](https://clinicaltrials.gov/study/NCT03332017) | Phase 2 | Terminé | 217 | Zanubrutinib + obinutuzumab vs obinutuzumab seul dans le FL récidivant/réfractaire (étude ROSEWOOD) |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | ECR | New England Journal of Medicine | Publication princeps de GALLIUM : chimiothérapie à base d'obinutuzumab vs rituximab dans le FL avancé non traité |
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | ECR | Journal of Clinical Oncology | GALLIUM : influence du type de chimiothérapie associée sur l'efficacité et la sécurité |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | ECR | Journal of Clinical Oncology | ROSEWOOD (Phase 2) : zanubrutinib + obinutuzumab vs obinutuzumab seul dans le FL récidivant/réfractaire |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | ECR | The Lancet Haematology | GALEN (Phase 2) : obinutuzumab + lénalidomide dans le FL récidivant/réfractaire |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | — | HemaSphere | Résultats finaux de GALLIUM : obinutuzumab vs rituximab en immunochimiothérapie de 1ère ligne |
| [37767550](https://pubmed.ncbi.nlm.nih.gov/37767550/) | 2024 | Cohorte | Haematologica | Polatuzumab vedotin + bendamustine et rituximab/obinutuzumab dans le FL récidivant/réfractaire (étude GO29365) |
| [39830356](https://pubmed.ncbi.nlm.nih.gov/39830356/) | 2024 | Revue | Frontiers in Pharmacology | Revue rapide sur l'efficacité, la sécurité et le coût-efficacité d'obinutuzumab dans le FL |
| [38660754](https://pubmed.ncbi.nlm.nih.gov/38660754/) | 2024 | Revue | Turkish Journal of Haematology | Revue complète de la prise en charge du lymphome folliculaire |
| [35180337](https://pubmed.ncbi.nlm.nih.gov/35180337/) | 2022 | Revue | Oncology (Williston Park) | Traitements actuels et émergents du lymphome folliculaire |
| [28324270](https://pubmed.ncbi.nlm.nih.gov/28324270/) | 2017 | Revue | Targeted Oncology | Revue sur obinutuzumab dans le FL réfractaire/récidivant au rituximab (étude GADOLIN) |

---

## Informations de Marché en France

Aucune AMM n'est enregistrée pour Obinutuzumab dans ce jeu de données (0 licence, statut « non commercialisé »).

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée / Immunothérapie (anticorps monoclonal anti-CD20, non cytotoxique conventionnel) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Autres Signaux TxGNN Non Retenus

Le modèle a également classé deux sous-types de LLC/lymphome à petits lymphocytes (« CLL/SLL avec hypermutation somatique du gène IGHV » et « CLL/SLL pré-centre germinatif ») à un score quasi identique (99,21 %), mais **sans aucun essai clinique ni publication associée** dans ce jeu de données. Le générateur de preuves signale lui-même une incohérence : les champs `original_indications` et `original_moa` du médicament sont vides alors qu'obinutuzumab dispose d'une indication LLC déjà approuvée — ce qui suggère un écart de collecte de données plutôt qu'une absence réelle de preuves. Ces deux signaux sont classés **L5 / Hold** et ne sont pas développés davantage tant que la source de données n'est pas corrigée.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Le lymphome folliculaire dispose du niveau de preuve le plus élevé (L1, ≥2 essais de Phase 3 terminés dont l'essai pivot GALLIUM) et correspond à une indication déjà approuvée du médicament ailleurs — il ne s'agit donc pas d'un signal de repositionnement spéculatif mais d'une extension de marché à documenter localement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtention du texte complet de l'AMM / notice TFDA (mises en garde, contre-indications) — actuellement bloquant pour l'évaluation de sécurité (S1)
- Confirmation ou correction des champs `original_indications` et `original_moa` du médicament dans la source de données
- Clarification du statut réel de commercialisation en France, étant donné l'incohérence entre l'absence d'AMM et l'existence d'essais cliniques matures sur cette molécule
- Réévaluation des deux signaux LLC/SLL après correction de l'écart de données identifié
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

