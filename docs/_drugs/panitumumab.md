---
layout: default
title: Panitumumab
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 2
---

# Panitumumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Panitumumab : Du Cancer Colorectal Metastatique (EGFR+) vers l'Osteoporose Induite par les Medicaments

## Resume en Une Phrase

Panitumumab est un anticorps monoclonal anti-EGFR, mentionne dans les donnees comme principalement utilise dans le cancer colorectal metastatique exprimant l'EGFR (le champ structure d'indication originale est toutefois vide dans le pack actuel).
Le modele TxGNN predit qu'il pourrait etre efficace pour l'**Osteoporose Induite par Medicament** (score 99,13%),
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction — il s'agit d'une prediction du modele seule.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Cancer colorectal metastatique EGFR+ (mentionne dans le rationnel mecanistique du modele ; le champ structure `original_indications` est vide dans les donnees actuelles) |
| Nouvelle Indication Predite | Osteoporose Induite par Medicament (drug-induced osteoporosis) |
| Score de Prediction TxGNN | 99,13% |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Non commercialise |
| Nombre d'AMM | 0 |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Les donnees structurees sur le mecanisme d'action (`original_moa`) sont actuellement en manque dans DrugBank. Le rationnel fourni par le modele indique cependant que le panitumumab est un anticorps monoclonal anti-EGFR (recepteur du facteur de croissance epidermique), utilise principalement dans le cancer colorectal metastatique exprimant l'EGFR.

La voie de signalisation EGFR participe en partie a la regulation de l'equilibre osteoclastes/osteoblastes, ce qui constitue le seul lien mecanistique invoque par le modele pour l'osteoporose induite par medicament. Toutefois, le rationnel lui-meme souligne l'absence de toute donnee preclinique ou clinique demontrant un benefice de l'inhibition de l'EGFR dans cette indication, et note que la direction de l'effet pourrait meme etre inverse : l'inhibition de l'EGFR est plutot associee a des effets negatifs sur le metabolisme osseux et a des effets secondaires cutanes/osseux connus.

Pour la seconde indication predite (retinopathie diabetique non proliferative severe), le traitement de reference repose sur l'inhibition du VEGF (bevacizumab, ranibizumab), une cible differente de l'EGFR vise par le panitumumab. Bien qu'il existe des interactions en aval entre les voies EGFR et VEGF dans la neoangiogenese tumorale, aucune donnee ne soutient un effet du panitumumab sur la microangiopathie retinienne diabetique, et le profil d'effets secondaires oculaires connus des anti-EGFR (conjonctivite, anomalies des cils) merite une vigilance particuliere. Ces deux predictions restent donc purement issues du score de similarite du modele, sans aucune validation experimentale ou clinique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associe enregistre actuellement.

---

## Preuves de la Litterature

Aucune litterature associee disponible actuellement.

---

## Indication Predite Secondaire (Signal Complementaire)

Le pack de preuves contient une seconde indication predite par le meme modele, avec un niveau de confiance similaire :

| Element | Contenu |
|------|------|
| Indication | Retinopathie Diabetique Non Proliferative Severe |
| Score de Prediction TxGNN | 99,05% |
| Niveau de Preuve | L5 |
| Decision Recommandee | Hold |

Aucun essai clinique ni litterature associee n'est disponible pour ce signal non plus. Comme pour l'osteoporose induite par medicament, il s'agit d'une prediction du modele seule, sans support mecanistique ou clinique direct.

---

## Cytotoxicite

| Element | Contenu |
|------|------|
| Classification de Cytotoxicite | Therapie ciblee — anticorps monoclonal anti-EGFR (base sur le mecanisme d'action mentionne dans le rationnel ; donnees structurees DrugBank de toxicite manquantes) |
| Risque de Myelosuppression | Non documente — veuillez consulter les mises en garde et precautions de la notice |
| Classification d'Emetogenicite | Non documentee — veuillez consulter les mises en garde et precautions de la notice |
| Elements de Surveillance | Non documentes — veuillez consulter les mises en garde et precautions de la notice |
| Protection de Manipulation | Non documentee — veuillez consulter les mises en garde et precautions de la notice |

---

## Considerations de Securite

Veuillez consulter la notice pour les informations de securite.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
Les deux indications predites reposent uniquement sur un score TxGNN (niveau de preuve L5), sans aucun essai clinique ni publication a l'appui. De plus, des donnees critiques manquent — les mises en garde/contre-indications TFDA (ecart bloquant DG001) et le mecanisme d'action structure (DG002) — ce qui empeche toute evaluation de securite initiale (S1). Le medicament n'est par ailleurs pas commercialise en France (0 AMM).

**Pour avancer, les elements suivants sont necessaires :**
- Obtenir la notice/l'etiquette TFDA (mises en garde, contre-indications) pour permettre l'evaluation de securite S1
- Completer les donnees structurees de mecanisme d'action (MOA) via l'API DrugBank
- Rechercher des etudes precliniques specifiques sur l'effet de l'inhibition EGFR sur le metabolisme osseux et la microangiopathie retinienne
- Surveiller l'apparition de nouveaux essais cliniques ou publications sur ces deux indications avant toute reevaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

