---
layout: default
title: Iobenguane
parent: 僅模型預測 (L5)
nav_order: 149
evidence_level: L5
indication_count: 4
---

# Iobenguane
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

# Iobenguane (MIBG) : De l'Oncologie Neuroendocrine vers les Troubles Hypotensifs

## Resume en Une Phrase

Iobenguane (MIBG) est un analogue de la noradrenaline historiquement utilise en imagerie et en traitement radio-isotopique des tumeurs neuroendocrines (pheochromocytome, paragangliome, neuroblastome) ; l'indication d'origine precise et le mecanisme d'action detaille ne sont toutefois pas documentes dans ce dossier (lacunes de donnees DG001/DG002).
Le modele TxGNN predit qu'il pourrait etre pertinent pour le **Trouble Hypotensif** (hypotensive disorder),
mais cette direction repose actuellement sur **0 essai clinique** et **20 publications**, dont la majorite concerne l'usage de la scintigraphie MIBG comme outil diagnostique de la dysautonomie, et non comme traitement de l'hypotension.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non documentee dans ce dossier (DG001/DG002) — usage historiquement connu : agent d'imagerie/radiotherapie des tumeurs neuroendocrines (pheochromocytome, paragangliome, neuroblastome) en tant qu'analogue de la noradrenaline |
| Nouvelle Indication Predite | Trouble Hypotensif (Hypotensive Disorder) |
| Score de Prediction TxGNN | 99.90 % |
| Niveau de Preuve | L4 |
| Statut de Marche en France | ✗ Non commercialise |
| Nombre d'AMM | 0 |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action ne sont pas disponibles (lacune DG002, severite Elevee). Sur la base des informations connues issues de la litterature associee, iobenguane (meta-iodobenzylguanidine, MIBG) est un analogue structurel de la noradrenaline, capte par les terminaisons nerveuses sympathiques via le transporteur de la noradrenaline. Cette propriete est exploitee depuis longtemps pour l'imagerie et le traitement radio-isotopique des tumeurs neuroendocrines secretant des catecholamines (pheochromocytome, paragangliome, neuroblastome).

Le lien avec le trouble hypotensif proposé par TxGNN repose sur cette meme propriete pharmacologique : la scintigraphie myocardique au MIBG est largement utilisee dans la litterature pour detecter une denervation sympathique cardiaque, laquelle est un mecanisme physiopathologique connu de l'hypotension orthostatique (notamment dans la maladie de Parkinson et les syndromes parkinsoniens). Le modele semble donc avoir capture une association reelle entre iobenguane et l'axe physiopathologique de l'hypotension autonome.

Il est toutefois essentiel de souligner une limite importante : la quasi-totalite des publications identifiees utilisent le MIBG comme **outil diagnostique** (mesure de la denervation sympathique, marqueur pronostique) chez des patients presentant deja une hypotension orthostatique, et non comme **agent therapeutique** visant a traiter ou prevenir l'hypotension. Aucune preuve clinique actuelle ne demontre un effet therapeutique d'iobenguane sur le trouble hypotensif lui-meme. La prediction doit donc etre interpretee comme une association mecanistique/diagnostique plausible, mais non comme une preuve d'efficacite therapeutique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associe enregistre actuellement.

---

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [11482743](https://pubmed.ncbi.nlm.nih.gov/11482743/) | 2001 | Revue | Drugs & Aging | Physiopathologie et prise en charge de l'hypotension orthostatique chez les patients parkinsoniens ; prevalence symptomatique jusqu'a 20 % |
| [27091624](https://pubmed.ncbi.nlm.nih.gov/27091624/) | 2016 | Revue | Movement Disorders | Relation entre hypotension orthostatique et declin cognitif dans la maladie de Parkinson (causalite vs association) |
| [26944118](https://pubmed.ncbi.nlm.nih.gov/26944118/) | 2016 | Cohorte | J Neurol Sci | Hypotension orthostatique et denervation sympathique cardiaque (MIBG) chez les patients Parkinson avec trouble du comportement en sommeil paradoxal |
| [34568970](https://pubmed.ncbi.nlm.nih.gov/34568970/) | 2021 | Cohorte | J Neural Transm | Neurofilament plasmatique et hypotension orthostatique dans la maladie de Parkinson precoce (77 patients, 54 controles) |
| [29880316](https://pubmed.ncbi.nlm.nih.gov/29880316/) | 2018 | Cohorte | Parkinsonism Relat Disord | Hypotension orthostatique a haute composante noradrenergique et denervation sympathique centrale en Parkinson precoce |
| [39232705](https://pubmed.ncbi.nlm.nih.gov/39232705/) | 2024 | Cohorte | BMC Neurology | Tachycardie emoussee et denervation sympathique cardiaque dans le trouble isole du comportement en sommeil paradoxal (phase prodromale) |
| [26853109](https://pubmed.ncbi.nlm.nih.gov/26853109/) | 2016 | Cohorte | Can J Neurol Sci | Monitoring ambulatoire de la pression arterielle sur 24h chez des patients parkinsoniens SWEDDs |
| [24332912](https://pubmed.ncbi.nlm.nih.gov/24332912/) | 2014 | Revue | Parkinsonism Relat Disord | Scintigraphie myocardique au MIBG dans la phase pre-motrice de la maladie de Parkinson |
| [30919499](https://pubmed.ncbi.nlm.nih.gov/30919499/) | 2019 | Revue | Movement Disorders | Decennie de progres sur les marqueurs prodromaux de la maladie de Parkinson (dont l'hypotension orthostatique) |
| [40616749](https://pubmed.ncbi.nlm.nih.gov/40616749/) | 2025 | Cohorte | Clin Auton Res | Illusions visuelles accrues associees a une defaillance autonome cardiovasculaire dans la maladie de Parkinson |

*Note : plusieurs autres publications recensees (ex. PMID 32169989, 2666677, 33998473) concernent le pheochromocytome, une pathologie associee a des crises **hypertensives** plutot qu'hypotensives ; elles ont ete ecartees de ce tableau car leur pertinence directe pour le trouble hypotensif est faible malgre le chevauchement thematique avec les catecholamines/MIBG.*

---

## Informations de Marche en France

Iobenguane n'est actuellement pas commercialise en France (0 AMM enregistree, statut : non commercialise). Aucune donnee de licence n'est disponible pour constituer un tableau des AMM.

---

## Considerations de Securite

Veuillez consulter la notice pour les informations de securite.

*A noter : l'absence de notice TFDA analysee (mises en garde, contre-indications, DDI) constitue une lacune de donnees de severite Bloquante (DG001), qui empeche toute evaluation de securite initiale (etape S1) pour cette molecule.*

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
Le lien entre iobenguane et le trouble hypotensif repose exclusivement sur des etudes observationnelles et des revues utilisant le MIBG comme outil diagnostique de denervation sympathique, sans aucun essai clinique interventionnel testant une efficacite therapeutique. Combine a la lacune bloquante sur les donnees de securite TFDA (DG001), le dossier ne peut pas encore progresser vers une evaluation clinique.

**Pour avancer, les elements suivants sont necessaires :**
- Obtenir la notice/les mises en garde TFDA (DG001, bloquant pour l'etape S1)
- Obtenir le mecanisme d'action detaille via DrugBank (DG002)
- Identifier si des essais interventionnels testent specifiquement iobenguane comme traitement (et non comme outil diagnostique) de l'hypotension orthostatique
- Clarifier aupres d'experts si la prediction TxGNN reflete une opportunite therapeutique reelle ou une simple correlation diagnostique (biomarqueur MIBG) avant tout investissement supplementaire
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

