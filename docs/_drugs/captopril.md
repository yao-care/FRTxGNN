---
layout: default
title: Captopril
parent: 僅模型預測 (L5)
nav_order: 68
evidence_level: L5
indication_count: 4
---

# Captopril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Captopril : De l'Hypertension Artérielle à l'Hypertension Rénovasculaire Maligne

## Résumé en Une Phrase

Captopril est le premier inhibiteur de l'enzyme de conversion de l'angiotensine (IEC) mis au point, historiquement utilisé pour le traitement de l'hypertension artérielle essentielle et de l'insuffisance cardiaque.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Hypertension Rénovasculaire Maligne** (*malignant renovascular hypertension*),
avec **20 publications scientifiques** soutenant actuellement cette direction, bien qu'aucun essai clinique enregistré ne soit disponible à ce jour.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle / Insuffisance cardiaque (aucune AMM disponible en France) |
| Nouvelle Indication Prédite | Hypertension Rénovasculaire Maligne |
| Score de Prédiction TxGNN | 99,28 % |
| Niveau de Preuve | L3 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Captopril est le premier inhibiteur de l'ACE (angiotensin-converting enzyme) développé cliniquement. Son mécanisme repose sur le blocage direct de la conversion de l'angiotensine I en angiotensine II, un puissant vasoconstricteur, interrompant ainsi la cascade du système rénine-angiotensine-aldostérone (SRAA). Bien que les données formelles de MOA ne soient pas disponibles dans ce dossier, le mécanisme de Captopril est établi depuis plusieurs décennies dans la littérature scientifique internationale.

L'hypertension rénovasculaire maligne est une forme sévère d'hypertension secondaire dont la physiopathologie centrale repose précisément sur une sécrétion excessive de rénine, déclenchée par une ischémie rénale (le plus souvent une sténose de l'artère rénale). Cette hypersécrétion de rénine active massivement l'angiotensine II, entraînant une vasoconstriction intense, une élévation réfractaire de la pression artérielle, et des lésions d'organes cibles. Captopril brise ce cycle en inhibant l'ACE : le degré d'adéquation mécanistique entre l'action du médicament et la physiopathologie de la maladie est extrêmement élevé.

**Point de vigilance critique :** Captopril est formellement contre-indiqué en cas de sténose bilatérale des artères rénales ou de sténose sur rein unique fonctionnel, où son utilisation peut précipiter une insuffisance rénale aiguë. Une évaluation vasculaire rénale préalable (écho-Doppler, angio-IRM ou angiographie) est donc indispensable avant tout usage dans cette indication.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [6145432](https://pubmed.ncbi.nlm.nih.gov/6145432/) | 1984 | Série clinique | Biulleten' Vsesoiuznogo kardiologicheskogo nauchnogo tsentra | Utilisation de Captopril dans l'hypertension artérielle à évolution stable et maligne ; données d'efficacité directe |
| [2887673](https://pubmed.ncbi.nlm.nih.gov/2887673/) | 1987 | Étude expérimentale / cohorte | Japanese Heart Journal | Modifications neurohormonales (rénine, Ang I, Ang II) dans les phases bénigne et maligne du modèle Goldblatt 2K2C ; rôle central du SRAA dans la progression maligne |
| [3894732](https://pubmed.ncbi.nlm.nih.gov/3894732/) | 1985 | Cohorte | Japanese Journal of Medicine | Physiopathologie et pronostic des sujets hypertendus ; utilité diagnostique du captopril dans l'hypertension rénovasculaire et l'hyperaldostéronisme primaire |
| [2040938](https://pubmed.ncbi.nlm.nih.gov/2040938/) | 1991 | Revue | The Journal of Pediatrics | Hypertension maligne : présentation clinique, mécanismes physiopathologiques et stratégies thérapeutiques |
| [17008836](https://pubmed.ncbi.nlm.nih.gov/17008836/) | 2006 | Revue | Minerva Medica | Hypertension rénovasculaire : concepts cliniques, diagnostic différentiel et rôle des inhibiteurs de l'enzyme de conversion |
| [232024](https://pubmed.ncbi.nlm.nih.gov/232024/) | 1979 | Étude clinique | Clinical Science (London) | L'hyperréninémie réactive après administration de Captopril identifie l'hypertension rénovasculaire chez 43 patients sur 44 ; spécificité diagnostique démontrée |
| [8070421](https://pubmed.ncbi.nlm.nih.gov/8070421/) | 1994 | Revue | Endocrinology & Metabolism Clinics of North America | Tumeurs sécrétant de la rénine : baisse tensionnelle sous traitement par IEC (captopril) ; lien mécanistique avec la suractivation du SRAA |
| [10955932](https://pubmed.ncbi.nlm.nih.gov/10955932/) | 2000 | Série de cas | Pediatric Nephrology | Hypertension rénovasculaire dans la neurofibromatose de type 1 ; test au captopril utilisé comme outil diagnostique de référence |
| [11334320](https://pubmed.ncbi.nlm.nih.gov/11334320/) | 2001 | Rapport de cas + Revue | Clinical Nephrology | Hypertension rénovasculaire associée à la neurofibromatose : activité rénine plasmatique multipliée par 4,5 après administration de 50 mg de captopril |
| [1572120](https://pubmed.ncbi.nlm.nih.gov/1572120/) | 1992 | Rapport de cas | Clinical Nuclear Medicine | Scintigraphie rénale au captopril positive dans une hypertension maligne sans sténose confirmée à l'angiographie ; limites diagnostiques documentées |

---

## Considérations de Sécurité

Veuillez consulter la notice officielle pour les informations de sécurité complètes (mises en garde, contre-indications, interactions médicamenteuses).

> **Note importante issue de la rationale mécanistique :** la contre-indication en cas de sténose bilatérale des artères rénales est un point de sécurité critique identifié dans les données de repositionnement. Cette vérification anatomique préalable est non négociable dans le cadre de l'hypertension rénovasculaire maligne.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Le mécanisme d'action de Captopril (inhibition de l'ACE → réduction de l'angiotensine II) est directement et précisément aligné avec la physiopathologie de l'hypertension rénovasculaire maligne (hyperactivation du SRAA par sécrétion excessive de rénine). La littérature disponible (niveau L3, 20 publications) confirme l'utilisation clinique de Captopril dans ce contexte — notamment pour le diagnostic (test au captopril) et comme traitement antihypertenseur. Cependant, l'absence d'essais contrôlés randomisés et la contre-indication formelle en cas de sténose bilatérale imposent une approche encadrée et sélective.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération des données complètes de MOA et de sécurité depuis DrugBank et la notice officielle ANSM
- Protocole de sélection des patients avec imagerie vasculaire rénale préalable systématique (exclusion des sténoses bilatérales)
- Plan de surveillance de la fonction rénale (créatininémie, kaliémie) pendant le traitement
- Conduite d'une étude observationnelle prospective pour atteindre un niveau de preuve L2 ou supérieur avant recommandation formelle
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

