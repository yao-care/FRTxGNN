---
layout: default
title: Tinidazole
parent: 僅模型預測 (L5)
nav_order: 307
evidence_level: L5
indication_count: 10
---

# Tinidazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Utilisation du contexte fourni pour rédiger le rapport (aucun outil nécessaire — génération de texte pure à partir du JSON fourni).

Note méthodologique avant le rapport : le JSON contient 10 indications prédites. Le rang 1 (score TxGNN le plus élevé, 99.93 %) n'a **aucune** preuve clinique ni littérature associée, et le `repurposing_rationale` du dossier lui-même l'identifie comme un probable faux positif d'embedding (similarité lexicale « vaginite »). Seule l'indication rang 5 (**SIDA/VIH**) dispose d'un niveau de preuve réel (L2, `decision_stage: S2`, 1 essai clinique + 17 publications). J'ai donc centré le rapport sur cette indication, la seule exploitable pour une décision, et mentionné le rejet du rang 1 par transparence.

---

# Tinidazole : Des Infections à Protozoaires au VIH/SIDA

## Résumé en Une Phrase

Le tinidazole est un antiparasitaire de la classe des 5-nitroimidazolés, utilisé pour traiter les infections à protozoaires et bactéries anaérobies (trichomonase, giardiase, amibiase).
Le modèle TxGNN identifie plusieurs pistes de repositionnement, mais seule l'indication **VIH/SIDA** dispose de preuves reelles a ce stade,
avec **1 essai clinique** et **17 publications**, dont un essai de phase 1/2 montrant un effet direct sur la susceptibilité tissulaire au VIH.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infections à protozoaires/anaérobies (trichomonase, giardiase, amibiase) — classe 5-nitroimidazolé* |
| Nouvelle Indication Prédite | VIH/SIDA (AIDS) |
| Score de Prédiction TxGNN | 99.69 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold (piste de recherche à confirmer) |

\* Le champ réglementaire officiel (TFDA/AMM) de l'indication d'origine est un data gap (DG001/DG002) ; cette classification est dérivée des connaissances pharmacologiques générales et des publications figurant dans ce dossier (traitement de référence de la trichomonase notamment).

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action (MOA) ne sont pas disponibles dans ce dossier (data gap). Sur la base des informations connues, le tinidazole fait partie de la classe des 5-nitroimidazolés (proche du métronidazole), dont l'efficacité contre *Trichomonas vaginalis*, *Giardia intestinalis* et *Entamoeba histolytica* est bien établie, et qui agit en réduisant la charge microbienne anaérobie/protozoaire des muqueuses génitales et digestives.

Le lien avec le VIH/SIDA n'est pas un effet antiviral direct, mais une action sur le microbiome génital : les publications de ce dossier montrent que la flore anaérobie du prépuce augmente le recrutement de cellules cibles CD4+ sensibles au VIH. Un essai pilote de phase 1/2 (NCT03412071) a testé le tinidazole comme l'un des quatre agents antimicrobiens visant à réduire cette susceptibilité chez des hommes ougandais non circoncis, et a atteint son critère principal (réduction de la densité de cellules CD4+ sensibles au VIH dans le tissu préputial).

Il faut noter que le score TxGNN le plus élevé du dossier (vaginite atrophique post-ménopausique, 99.93 %) et plusieurs autres prédictions de rang supérieur (ulcération vulvaire, néoplasme vulvaire, pathologies mammaires bénignes) n'ont **aucune** preuve clinique ou littéraire associée ; le dossier les qualifie lui-même de probables faux positifs liés à une similarité d'embedding entre entités de maladies, et non à une plausibilité mécanistique réelle. L'indication VIH/SIDA est la seule des dix candidats à disposer d'un stade de décision avancé (S2) et d'un niveau de preuve L2.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03412071](https://clinicaltrials.gov/study/NCT03412071) | Phase 1/2 (pilote) | Inconnu | 125 | Étude sur des hommes ougandais non circoncis testant 4 agents antimicrobiens (dont tinidazole systémique) sur le microbiome préputial et la susceptibilité au VIH des lymphocytes T CD4+ dérivés du prépuce ; le bras tinidazole a atteint une réduction significative de la densité de cellules CD4+ sensibles au VIH. Critère de substitution (biomarqueur immunitaire), pas d'infection VIH clinique ; effectif limité et statut de suivi non confirmé. |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [8442923](https://pubmed.ncbi.nlm.nih.gov/8442923/) | 1993 | ECR (préliminaire) | AIDS (London) | Étude comparant tinidazole + thiabendazole + cotrimoxazole vs placebo dans la diarrhée liée au SIDA en Zambie. |
| [31324206](https://pubmed.ncbi.nlm.nih.gov/31324206/) | 2019 | Protocole d'ECR | Trials | Protocole de l'essai (lié à NCT03412071) testant l'effet d'agents antimicrobiens sur le microbiote pénien, l'immunologie et la susceptibilité au VIH chez des hommes ougandais. |
| [21931875](https://pubmed.ncbi.nlm.nih.gov/21931875/) | 2011 | Cohorte | PLoS Negl Trop Dis | Caractéristiques cliniques et réponse au traitement de l'amibiase chez 170 patients japonais co-infectés VIH-1, population à risque accru d'amibiase invasive. |
| [31996095](https://pubmed.ncbi.nlm.nih.gov/31996095/) | 2020 | Cohorte/Dépistage | Int J STD AIDS | Dépistage prénatal de la trichomonase (entre autres IST) chez 371 femmes enceintes en RD Congo, contexte pertinent pour la prévention des infections associées au VIH. |
| [34794678](https://pubmed.ncbi.nlm.nih.gov/34794678/) | 2022 | Revue | Pediatr Clin North Am | Revue sur l'amibiase, identifiant les personnes vivant avec le VIH/SIDA comme groupe à haut risque nécessitant une vigilance diagnostique accrue. |
| [19632225](https://pubmed.ncbi.nlm.nih.gov/19632225/) | 2010 | Revue | Exp Parasitol | Options thérapeutiques pour Cryptosporidium et Giardia, avec besoin non couvert de traitement efficace chez les patients immunodéprimés (dont VIH). |
| [30789955](https://pubmed.ncbi.nlm.nih.gov/30789955/) | 2019 | Revue | PLoS ONE | Caractéristiques cliniques et épidémiologiques de la colite amibienne en contexte non endémique, incluant patients immunodéprimés. |
| [35863010](https://pubmed.ncbi.nlm.nih.gov/35863010/) | 2022 | In vitro | Microbiol Spectr | Activité antitrichomonas in vitro de trois 5-nitroimidazolés (dont tinidazole) comparée au métronidazole sur 94 isolats cliniques. |
| [29393008](https://pubmed.ncbi.nlm.nih.gov/29393008/) | 2018 | Rapport de cas | Int J STD AIDS | Trichomonase réfractaire traitée par une combinaison incluant tinidazole oral et intravaginal chez une patiente post-bypass gastrique. |
| [21097745](https://pubmed.ncbi.nlm.nih.gov/21097745/) | 2010 | Rapport de cas | Int J STD AIDS | Trichomonase se présentant sous forme d'ulcération vulvaire, résolue après tinidazole oral. |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La seule preuve directement pertinente est un essai pilote unique (NCT03412071, n=125, statut de suivi non confirmé) reposant sur un critère de substitution immunologique et non sur une réduction clinique de l'incidence du VIH ; les autres publications documentent des infections opportunistes (amibiase, trichomonase) chez des patients VIH/SIDA plutôt qu'un effet du tinidazole sur le SIDA lui-même. Les 9 autres indications prédites par TxGNN (dont la mieux scorée) sont sans aucune preuve et jugées probables faux positifs par le dossier même.

**Pour avancer, les éléments suivants sont nécessaires :**
- Confirmation du statut et des résultats finaux de NCT03412071 (biomarqueurs + suivi clinique)
- Un essai contrôlé avec critère clinique (incidence d'infection VIH), pas seulement un biomarqueur tissulaire
- Données de sécurité TFDA/AMM (DG001) actuellement bloquantes pour toute évaluation S1
- Données de mécanisme d'action (DG002) pour asseoir la plausibilité biologique
- Le médicament n'étant pas commercialisé en France, une évaluation de faisabilité réglementaire/accès serait nécessaire avant toute étude clinique locale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

