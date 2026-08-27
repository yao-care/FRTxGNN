---
layout: default
title: Sirolimus
parent: 僅模型預測 (L5)
nav_order: 280
evidence_level: L5
indication_count: 10
---

# Sirolimus
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

# Sirolimus : De la Prévention du Rejet de Greffe Rénale au Liposarcome

## Résumé en Une Phrase

Sirolimus est un inhibiteur de mTOR, initialement développé et utilisé comme immunosuppresseur pour prévenir le rejet de greffe rénale.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Liposarcome**,
avec **5 essais cliniques** et **12 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Prévention du rejet de greffe rénale (immunosuppresseur) |
| Nouvelle Indication Prédite | Liposarcome |
| Score de Prédiction TxGNN | 99.89% |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action de Sirolimus ne sont pas disponibles dans le pack de preuves fourni. Sur la base des informations pharmacologiques connues, Sirolimus est un inhibiteur de mTOR (mammalian target of rapamycin), initialement approuvé comme immunosuppresseur pour la prévention du rejet de greffe rénale ; son efficacité dans cette indication est établie depuis les années 1990.

Le liposarcome — en particulier le sous-type dédifférencié — présente fréquemment une activation des voies Akt-mTOR et MAPK (PMID 26518767), ce qui fournit une base mécanistique théorique pour l'usage d'un inhibiteur de mTOR dans cette tumeur. Cependant, la majorité des preuves cliniques disponibles concernent des molécules apparentées de la même classe (temsirolimus, ridaforolimus, évérolimus) plutôt que le sirolimus lui-même, dont les données directes restent limitées.

Un essai de Phase 2 à bras unique (NCT02821507) a néanmoins testé directement la combinaison sirolimus + cyclophosphamide chez 70 patients atteints de liposarcome myxoïde et de chondrosarcome métastatiques ou non résécables, et a été mené à son terme — ce qui constitue la preuve directe la plus solide du dossier. Cette étude ne couvrant qu'un sous-type spécifique (liposarcome myxoïde), l'extrapolation à l'ensemble des liposarcomes reste à confirmer.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Terminé | 70 | Sirolimus + cyclophosphamide dans le liposarcome myxoïde et le chondrosarcome métastatiques/non résécables ; hypothèse d'inhibition de mTOR pour freiner la croissance tumorale |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Terminé | 24 | Torisel (temsirolimus) + doxorubicine liposomale dans les sarcomes des tissus mous et osseux avancés ; recherche du schéma posologique sûr |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Terminé | 46 | Cixutumumab + temsirolimus chez des patients pédiatriques atteints de tumeurs solides récidivantes ou réfractaires |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Terminé | 216 | Ridaforolimus (AP23573, inhibiteur de mTOR), 5 jours consécutifs toutes les deux semaines, chez des patients atteints de sarcome avancé |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Actif, non recrutant | 48 | Ribociclib + évérolimus dans le liposarcome dédifférencié avancé et le léiomyosarcome, après au moins une ligne de traitement systémique |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | ECR (Phase 2, SAR-096) | Clin Cancer Res | Ribociclib (CDK4/6) + évérolimus (mTOR) montre une inhibition synergique dans le liposarcome dédifférencié et le léiomyosarcome |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Revue | Cancers | Panorama des nouvelles thérapies ciblées approuvées par la FDA dans les sarcomes des tissus mous |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Revue | Curr Opin Oncol | Rationnel et résultats des essais récents sur les agents ciblés moléculaires dans les sarcomes avancés |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Étude mécanistique | Tumour Biol | Activation des voies Akt-mTOR et MAPK dans 99 spécimens de liposarcome dédifférencié ; effet antitumoral d'un inhibiteur de mTOR observé in vitro |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | Préclinique | Cancer Genomics Proteomics | Combinaison chloroquine + rapamycine comme inhibiteur puissant de l'autophagie, efficace contre le liposarcome bien différencié |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | Préclinique | In Vivo | Chloroquine + rapamycine freine la croissance tumorale dans un modèle murin PDOX de liposarcome dédifférencié |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | Préclinique | Mol Cancer Ther | MLN0128, inhibiteur ATP-compétitif de mTOR, montre une activité antitumorale in vitro/in vivo dans les sarcomes osseux et des tissus mous |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Revue | Bull Cancer | Panorama des traitements ciblés dans les tumeurs conjonctives rares et les sarcomes, classés par altération moléculaire |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | Cohorte | J Am Soc Nephrol | Le passage à un traitement par sirolimus après transplantation rénale réduit le risque de cancer par rapport à la ciclosporine |
| [32711543](https://pubmed.ncbi.nlm.nih.gov/32711543/) | 2020 | Série de cas | Diagn Pathol | 3 cas de malformation fibro-adipeuse vasculaire (FAVA) liés à une activation de la voie mTOR, traités par sirolimus |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'indication liposarcome dispose du meilleur niveau de preuve de tout le dossier (L2, essai de Phase 2 terminé — NCT02821507, n=70) et d'un rationnel mécanistique cohérent, mais cet essai ne porte que sur le sous-type myxoïde et reste un essai à bras unique sans comparateur ; les données directes sur le sirolimus (par opposition aux molécules apparentées de sa classe) demeurent limitées.
- Une lacune bloquante (DG001 — absence des mises en garde/contre-indications officielles) empêche toute évaluation de sécurité (étape S1), et le médicament n'est actuellement pas commercialisé en France (0 AMM).

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les données officielles de sécurité (mises en garde, contre-indications, interactions) pour lever le blocage DG001
- Clarifier le mécanisme d'action détaillé (DG002)
- Confirmer l'applicabilité au-delà du sous-type myxoïde du liposarcome
- Évaluer une voie d'accès (importation, ATU) en l'absence de commercialisation en France
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

