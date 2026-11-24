---
layout: default
title: Propofol
parent: Preuves élevées (L1-L2)
nav_order: 636
evidence_level: L2
indication_count: 5
last_modified_at: 2026-11-24
description: "Propofol : nouvelle indication prédite, Migraine (« migraine disorder ») (niveau de preuve L2). Indication d'origine : Non renseignée dans les données d'AMM compilées (usage anesthésique c…"
monitor_inn: "PROPOFOL"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "Prinzmetal angina", "nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome"]
---

# Propofol
{: .fs-9 }

Niveau de preuve: **L2** | Indications prédites: **5** 
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

## Propofol : De l'anesthésie générale à la migraine
{: .text-alpha }

## Résumé en Une Phrase

Le propofol est un agent anesthésique intraveineux utilisé pour l'induction et l'entretien de l'anesthésie et pour la sédation.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **migraine** (« migraine disorder »),
avec **3 essais cliniques** et **19 publications** soutenant actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées (usage anesthésique connu) |
| Nouvelle Indication Prédite | Migraine (« migraine disorder ») |
| Score de Prédiction TxGNN | 0,9969 |
| Niveau de Preuve | L2 |
| Statut de Marché en France | Commercialisé (autorisations valides : 11 sur 12) |
| Nombre d'AMM | 12 (valides : 11) |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Propofol (traduction non officielle) : « Le mécanisme d'action, comme celui de tous les anesthésiques généraux, est mal compris. Cependant, on pense que le propofol produit ses effets sédatifs/anesthésiques par la modulation positive de la fonction inhibitrice du neurotransmetteur GABA via les récepteurs GABA A, canaux ioniques activés par un ligand. » Texte original en anglais : "The mechanism of action, like all general anesthetics, is poorly understood. However, propofol is thought to produce its sedative/anesthetic effects by the positive modulation of the inhibitory function of the neurotransmitter GABA through the ligand-gated GABA A receptors." ([DailyMed: Diprivan (propofol) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e3105799-a4b6-f3f4-e6e2-b2b29bbdb538), version du 2025-09-11 ; consulté le 2026-11-19). Sur la base des informations connues, le propofol est un modulateur allostérique positif du récepteur GABA-A. Il renforce l'inhibition GABAergique, ce qui pourrait atténuer la signalisation nociceptive trigémino-vasculaire et l'hyperexcitabilité corticale.

L'indication originale (anesthésie et sédation) et la migraine n'ont pas de lien direct de type « même maladie ». Le rapprochement repose sur le mécanisme : des travaux précliniques montrent que l'hémisuccinate de propofol supprime la dépression corticale envahissante, considérée comme le substrat physiologique de l'aura migraineuse. Cela offre une justification plausible.

L'usage reste cependant limité à un cadre surveillé (service d'urgences) en raison des risques de sédation et de dépression respiratoire. Les doses évaluées dans la migraine sont sub-anesthésiques.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Phase 2/3 | Terminé | 74 | Propofol à faible dose en traitement abortif de la migraine pédiatrique aux urgences ; essai le plus pertinent |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | Non applicable | Terminé | 40 | Perfusion de propofol à faible dose dans la migraine pédiatrique : efficacité, limites de dosage, durée d'effet |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | Non applicable | Arrêté prématurément | 12 | Propofol à faible dose dans la migraine réfractaire sévère aux urgences ; faible puissance, motif d'arrêt à vérifier |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | ECR | J Emerg Med | Propofol à faible dose dans la migraine pédiatrique ; effet potentiel et durée de séjour possiblement réduite |
| [32705801](https://pubmed.ncbi.nlm.nih.gov/32705801/) | 2020 | ECR pilote | Emerg Med Australas | Propofol à dose de sédation procédurale vs traitement standard aux urgences |
| [33070469](https://pubmed.ncbi.nlm.nih.gov/33070469/) | 2021 | ECR | Emerg Med Australas | Propofol vs placebo chez l'adulte aux urgences, en double aveugle (critère : résolution à 1 h) ; migraine aiguë en général |
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | ECR | Arch Acad Emerg Med | Propofol + granisétron vs propofol + métoclopramide dans la migraine aiguë |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | ECR | Arch Acad Emerg Med | Sumatriptan + propofol vs sumatriptan seul dans la migraine aiguë |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | Revue systématique | Acad Emerg Med | Sécurité et efficacité du propofol dans la migraine aiguë aux urgences ; données limitées |
| [26790849](https://pubmed.ncbi.nlm.nih.gov/26790849/) | 2016 | Revue systématique | Headache | Traitements aigus de la migraine pédiatrique aux urgences |
| [39364614](https://pubmed.ncbi.nlm.nih.gov/39364614/) | 2024 | Revue systématique et méta-analyse en réseau | Headache | Efficacité des agents parentéraux pour limiter les rechutes après une migraine aiguë sévère |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Recommandations | Headache | Mise à jour 2025 des recommandations de l'American Headache Society sur les traitements parentéraux aux urgences |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | Revue | Expert Rev Neurother | Profil du propofol à dose sub-anesthésique dans la migraine super-réfractaire |

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 63558577 | PROPOFOL BAXTER 10 mg/ml, émulsion injectable/pour perfusion | Émulsion injectable pour perfusion | BAXTER HOLDING (PAYS-BAS) | Active |
| 62010414 | DIPRIVAN 20 mg/mL, émulsion injectable en seringue pré-remplie | Émulsion injectable | ASPEN PHARMA TRADING (IRLANDE) | Active |
| 66093051 | PROPOFOL BAXTER 20 mg/ml, émulsion injectable/pour perfusion | Émulsion injectable pour perfusion | BAXTER HOLDING (PAYS-BAS) | Active |
| 66110981 | PROPOFOL KABI 10 mg/mL, émulsion injectable/pour perfusion | Émulsion injectable ou pour perfusion | FRESENIUS KABI FRANCE | Active |
| 66701952 | PROPOFOL LIPURO 2 % (20 mg/ml), émulsion injectable ou pour perfusion | Émulsion injectable ou pour perfusion | B BRAUN MELSUNGEN | Active |
| 65591412 | PROPOFOL KABI 20 mg/mL, émulsion injectable | Émulsion injectable ou pour perfusion | FRESENIUS KABI FRANCE | Active |
| 62286195 | PROPOFOL LIPURO 5 mg/ml, émulsion injectable ou pour perfusion | Émulsion injectable ou pour perfusion | B BRAUN MELSUNGEN | Active |
| 62540042 | PROPOFOL LIPURO 1 % (10 mg/ml), émulsion injectable ou pour perfusion | Émulsion injectable ou pour perfusion | B BRAUN MELSUNGEN | Active |
| 60616445 | DIPRIVAN 10 mg/mL, émulsion injectable en seringue pré-remplie | Émulsion injectable | ASPEN PHARMA TRADING (IRLANDE) | Active |
| 68749814 | PROPOFOL KABI 20 mg/mL, émulsion injectable en seringue pré-remplie | Émulsion injectable | FRESENIUS KABI FRANCE | Active |
| 60692610 | PROPOFOL KABI 10 mg/mL, émulsion injectable en seringue pré-remplie | Émulsion injectable | FRESENIUS KABI FRANCE | Active |
| 66617123 | PROPOFOL MYLAN 20 mg/ml, émulsion injectable (IV) | Émulsion injectable | MYLAN SAS | Abrogée |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

Au total, 12 AMM sont recensées; seules les 5 premières sont listées ici.

<!-- review:begin fr-lic-20261106-propofol-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Au total, 11 AMM sont recensées, toutes annulées ; seules les 5 premières sont listées ici. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 11 AMM pour ce médicament, dont 11 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans le Résumé rapide. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261106-propofol-1 -->

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie, et non texte de notice) : épilepsie, trouble hypotensif, insuffisance respiratoire, artériosclérose intracrânienne, trouble héréditaire du métabolisme lipidique, hyperlipidémie familiale.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi les principales, de niveau modéré : morphine (y compris liposomale), opium, ondansétron, granisétron, dolasétron, clarithromycine, lévofloxacine, cisapride, famotidine, lopéramide et divers laxatifs (bisacodyl, lactulose, lactitol, huile de ricin, glycérine, citrate et hydroxyde de magnésium, huile minérale). Le métronidazole est de niveau mineur.
- **Signal de sécurité** : des cas rapportés de spasme coronarien induit par l'anesthésie ; la sédation et la dépression respiratoire imposent une surveillance en milieu hospitalier.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Un essai de Phase 2/3 terminé et plusieurs ECR dans la migraine soutiennent la prédiction (niveau L2), mais aucun ECR de Phase 3 confirmatoire n'est disponible.
- 11 AMM françaises sur 12 sont valides (médicament commercialisé), mais les données de sécurité de la notice manquent, d'où la nécessité de garde-fous (usage hospitalier surveillé uniquement).

<!-- review:begin fr-lic-20261124-propofol-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Les 11 AMM françaises sur 11 sont valides » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans le Résumé rapide. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-propofol-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications officielles de la notice (ANSM)
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Examiner les résultats publiés des essais NCT01604785 et NCT02485418, et vérifier le motif d'arrêt de NCT02492295
- Confirmer le statut réglementaire actuel du propofol en France, 11 AMM listées sur 11 étant valides
- Définir un protocole de dose sub-anesthésique, de surveillance cardiorespiratoire et de sélection des patients (exclusion de l'épilepsie, de l'hypotension, de l'insuffisance respiratoire)

**Autres indications prédites (non recommandées à ce stade) :**
- Migraine avec aura du tronc cérébral : question de recherche (L3), preuves extrapolées de la migraine en général
- Angor de Prinzmetal : Hold (L5), les publications décrivent des spasmes coronariens induits par l'anesthésie, soit un signal de sécurité défavorable
- Syndrome néphrogénique d'antidiurèse inappropriée : Hold (L5), aucun lien mécanistique ni preuve
- Syndrome de Gilles de la Tourette : Hold (L4), seul un usage procédural en sédation lors d'une chirurgie de stimulation cérébrale profonde est documenté

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-24 | Supprimé : « toutes annulées » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Diprivan (propofol) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e3105799-a4b6-f3f4-e6e2-b2b29bbdb538) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

