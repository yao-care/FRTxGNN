---
layout: default
title: Oxitriptan
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 1
---

# Oxitriptan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Oxitriptan : D'une Indication d'Origine Non Documentee vers l'Insomnie

## Resume en Une Phrase

Oxitriptan (DB02959), correspondant au 5-hydroxytryptophane (5-HTP, precurseur metabolique de la serotonine), n'a pas d'indication d'origine documentee dans les donnees disponibles et n'est actuellement pas commercialise en France.
Le modele TxGNN predit qu'il pourrait etre efficace pour l'**Insomnie**, avec un score de prediction de **99,89%**.
**6 essais cliniques** et **13 publications** sont actuellement associes a cette piste, mais aucun essai de Phase 2/3 dedie specifiquement a l'oxitriptan dans l'insomnie n'a ete identifie.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non documentee (aucune indication d'origine enregistree dans le dossier actuel) |
| Nouvelle Indication Predite | Insomnie |
| Score de Prediction TxGNN | 99,89% |
| Niveau de Preuve | L3 |
| Statut de Marche en France | Non commercialise |
| Nombre d'AMM | 0 |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action et sur l'indication d'origine de l'oxitriptan ne sont pas disponibles dans ce dossier d'evidence. Sur la base des informations connues par ailleurs, l'oxitriptan correspond au 5-hydroxytryptophane (5-HTP), un acide amine precurseur direct de la synthese de la serotonine (5-HT), une information recurrente dans la litterature associee mais non confirmee par les champs MOA structures de ce dossier.

La litterature rassemblee autour de la piste "insomnie" converge largement vers la modulation du systeme serotoninergique : plusieurs etudes precliniques montrent que des composes agissant sur la voie 5-HT/GABA ameliorent le sommeil dans des modeles animaux d'insomnie induite (par exemple par PCPA), et un essai clinique complete (NCT04078724) a directement teste une supplementation en 5-HTP sur la qualite du sommeil. Ce faisceau d'indices constitue une plausibilite mecanistique raisonnable pour la prediction TxGNN, sans toutefois constituer une preuve d'efficacite clinique de niveau confirmatoire.

---

## Preuves d'Essais Cliniques

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT04078724](https://clinicaltrials.gov/study/NCT04078724) | N/A | Termine | 33 | Essai randomise controle evaluant l'impact d'une supplementation en 5-HTP sur la qualite du sommeil et le microbiome intestinal chez des personnes agees (cognition normale vs. trouble cognitif leger) |
| [NCT06893822](https://clinicaltrials.gov/study/NCT06893822) | N/A | En cours de recrutement | 20 | Essai croise randomise en double aveugle sur Griffonia simplicifolia (source naturelle de 5-HTP) et son effet sur l'intensite de la douleur et la sensibilisation centrale/peripherique |
| [NCT03364101](https://clinicaltrials.gov/study/NCT03364101) | N/A | Termine | 60 | Etude "PowerOff" explorant l'effet d'un supplement (vs placebo) sur la qualite du sommeil, mesuree par actigraphie |
| [NCT00001918](https://clinicaltrials.gov/study/NCT00001918) | N/A | Termine | 20 | Evaluation clinique du syndrome eosinophilie-myalgie (EMS) associe historiquement a des supplements de L-tryptophane/5-HTP contamines, utilises pour l'insomnie et la depression |
| [NCT06365801](https://clinicaltrials.gov/study/NCT06365801) | N/A | Pas encore en recrutement | 100 | Etude de cohorte prospective sur les points d'acupuncture dans le syndrome de l'intestin irritable (lien indirect via l'axe intestin-cerveau) |
| [NCT06718452](https://clinicaltrials.gov/study/NCT06718452) | N/A | Pas encore en recrutement | 100 | Etude sur le traitement des acouphenes cible sur la neuroinflammation (umPEALUT) ; lien avec l'oxitriptan non etabli directement |

---

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [2962265](https://pubmed.ncbi.nlm.nih.gov/2962265/) | 1987 | Revue | Revue medicale de la Suisse romande | Indications du L-5-hydroxytryptophane en neurologie |
| [4128428](https://pubmed.ncbi.nlm.nih.gov/4128428/) | 1974 | Rapport de cas | Electroencephalography and Clinical Neurophysiology | Cas d'agrypnie (4 mois sans sommeil) dans la maladie de Morvan, avec action favorable du 5-hydroxytryptophane |
| [4548556](https://pubmed.ncbi.nlm.nih.gov/4548556/) | 1974 | Rapport de cas | Revue neurologique | Etudes polygraphiques et metaboliques d'une insomnie persistante avec hallucinations (chorée fibrillaire de Morvan) |
| [33634088](https://pubmed.ncbi.nlm.nih.gov/33634088/) | 2021 | Revue | Frontiers in Bioengineering and Biotechnology | Avancees dans la synthese microbienne du 5-HTP, utilise dans la depression, l'insomnie et la migraine |
| [32006050](https://pubmed.ncbi.nlm.nih.gov/32006050/) | 2020 | Etude preclinique | Applied Microbiology and Biotechnology | Production amelioree de 5-HTP, precurseur de la serotonine utilise dans l'insomnie et d'autres troubles |
| [40350945](https://pubmed.ncbi.nlm.nih.gov/40350945/) | 2025 | Etude preclinique | China Journal of Chinese Materia Medica | Effet de la decoction Fushen sur le systeme 5-HT et l'expression du GABA dans un modele murin d'insomnie induite par PCPA |
| [40493075](https://pubmed.ncbi.nlm.nih.gov/40493075/) | 2025 | Etude preclinique | Psychopharmacology | Le ginsenoside Rg1 attenue l'insomnie induite par PCPA via l'inhibition de l'inflammasome NLRP3 et la voie Nrf2/HO-1 |
| [40160035](https://pubmed.ncbi.nlm.nih.gov/40160035/) | 2025 | Etude preclinique | International Journal of Neuropsychopharmacology | Effets sedatifs et hypnotiques de la nuciferine via modulation du systeme serotoninergique chez le rongeur |
| [40367689](https://pubmed.ncbi.nlm.nih.gov/40367689/) | 2025 | Etude preclinique | International Immunopharmacology | Promotion du sommeil par l'acide cinnamique dans un modele d'insomnie induite par parachlorophenylalanine chez le rat |
| [24785966](https://pubmed.ncbi.nlm.nih.gov/24785966/) | 2014 | Etude preclinique | Fitoterapia | La gomisine N (Schisandra chinensis) potentialise le sommeil induit par le pentobarbital via les systemes serotoninergique et GABAergique |

---

## Considerations de Securite

Veuillez consulter la notice pour les informations de securite.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
Un ecart de donnees bloquant (avertissements/contre-indications de l'etiquette officielle indisponibles) empeche toute evaluation de securite preliminaire, et l'oxitriptan n'est ni commercialise ni approuve en France. Les preuves d'efficacite pour l'insomnie reposent principalement sur des etudes precliniques et un essai clinique non stratifie par phase (NCT04078724), ce qui correspond a un niveau de preuve L3 — insuffisant pour avancer sans donnees de securite de base.

**Pour avancer, les elements suivants sont necessaires :**
- Recuperation des mises en garde/contre-indications officielles (source TFDA/notice) — ecart bloquant DG001
- Donnees de mecanisme d'action (MOA) via l'API DrugBank — ecart DG002
- Confirmation de l'indication d'origine approuvee (le cas echeant) de l'oxitriptan
- Resultats detailles et publication complete de l'essai NCT04078724 pour confirmer le signal d'efficacite sur le sommeil
- Criblage des interactions medicamenteuses (DDI), actuellement non trouve dans les bases interrogees
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

