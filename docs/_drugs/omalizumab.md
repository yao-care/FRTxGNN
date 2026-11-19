---
layout: default
title: Omalizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 559
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-04
monitor_inn: "OMALIZUMAB"
predicted_indications: ["bronchitis", "atopic eczema", "dermatitis", "bronchial neoplasm (disease)", "acne keloid", "acrodermatitis chronica atrophicans", "hydroa vacciniforme, familial", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease"]
description: "Omalizumab : nouvelle indication prédite, Bronchite (bronchitis) (niveau de preuve L5). En France, AMM dans la BDPM : 10 (valides : 10)"
---

# Omalizumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

## Omalizumab: Bronchite (bronchitis)
{: .text-alpha }

## Résumé en une phrase

L'omalizumab est un anticorps monoclonal qui neutralise les IgE libres. Le modèle TxGNN prédit qu'il pourrait être utile dans la **bronchite (bronchitis)**, mais aucune étude publiée ne soutient cette direction : les **2 essais cliniques** associés et les publications retrouvées concernent l'asthme, le chevauchement asthme-BPCO ou d'autres sujets, et non la bronchite elle-même.

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Non renseignée dans les données locales |
| Nouvelle indication prédite | Bronchite (bronchitis) |
| Score de prédiction TxGNN | 1.0000 |
| Niveau de preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 10 sur 10) |
| Nombre d'AMM | 10 (valides : 10) |
| Décision recommandée | Hold |

## Pourquoi cette prédiction est-elle raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Omalizumab (traduction non officielle) : « Asthme, rhinosinusite chronique avec polypes nasaux et allergie alimentaire médiée par les IgE Les produits à base d'omalizumab inhibent la liaison des IgE au récepteur de haute affinité des IgE (FcεRI) à la surface des mastocytes, des basophiles et des cellules dendritiques, ce qui entraîne une régulation négative du FcεRI sur ces cellules. Chez les asthmatiques allergiques, le traitement par les produits à base d'omalizumab inhibe l'inflammation médiée par les IgE, comme en témoignent la diminution des éosinophiles sanguins et tissulaires et la diminution des médiateurs inflammatoires, notamment IL-4, IL-5 et IL-13. » Texte original en anglais : "Asthma, Chronic Rhinosinusitis with Nasal Polyps, and IgE-Mediated Food Allergy Omalizumab products inhibit the binding of IgE to the high-affinity IgE receptor (FcεRI) on the surface of mast cells, basophils, and dendritic cells, resulting in FcεRI down-regulation on these cells. In allergic asthmatics, treatment with omalizumab products inhibit IgE-mediated inflammation, as evidenced by reduced blood and tissue eosinophils and reduced inflammatory mediators, including IL-4, IL-5, and IL-13." ([DailyMed: Omlyclo (omalizumab-igec) prescribing information, CELLTRION USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dbd8709f-1636-45d9-ba94-5a3bc5f22f84), version du 2026-10-06 ; consulté le 2026-11-19). D'après les informations connues, l'omalizumab se lie aux IgE libres, ce qui réduit l'expression du récepteur FcεRI sur les mastocytes et les basophiles et atténue l'inflammation allergique des voies respiratoires. La cible identifiée est la chaîne lourde epsilon de l'immunoglobuline (IGHE).

Ce mécanisme pourrait avoir un sens pour une bronchite d'origine allergique ou associée à l'asthme, ou pour le chevauchement asthme-BPCO. Il n'est en revanche pas établi pour les bronchites infectieuses ou chroniques sans composante allergique. Le lien avec la bronchite elle-même reste donc indirect et hypothétique.

## Preuves d'essais cliniques

| Numéro d'essai | Phase | Statut | Inscription | Résultats principaux |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | Terminé | 11 | Effet d'épargne de corticoïdes de l'omalizumab (contre placebo) chez des patients asthmatiques avec bronchite éosinophilique persistante ; échantillon très réduit, population relevant de l'asthme sévère avec éosinophilie des expectorations, et efficacité possiblement insuffisante |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2 | Terminé | 382 | Étude de détermination de dose (QGE031) dans l'urticaire chronique spontanée ; sans rapport direct avec la bronchite |

## Preuves de la littérature

| PMID | Année | Type | Revue | Résultats principaux |
|------|-----|------|------|---------|
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Analyse de sécurité groupée | Curr Med Res Opin | Sécurité de l'omalizumab chez l'enfant atteint d'asthme allergique |
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Cohorte | Postepy Dermatol Alergol | Omalizumab chez des patients d'âge moyen ou âgés avec asthme allergique sévère et chevauchement BPCO |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Revue | Clin Rev Allergy Immunol | Approbation et expérience post-commercialisation de l'omalizumab dans l'asthme |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Revue | Expert Opin Pharmacother | Prise en charge de l'asthme associé aux maladies des voies aériennes liées au tabac (dont bronchite chronique) |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Revue | Masui | Prise en charge préopératoire des patients asthmatiques ou atteints de bronchite chronique |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Revue | Allergol Immunopathol | Anticorps monoclonaux en pédiatrie |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Rapport de cas | J Investig Allergol Clin Immunol | Cas rare de bronchite plastique après thermoplastie bronchique |

Aucune de ces publications n'étudie l'omalizumab dans le traitement de la bronchite.

## Informations de marché en France

L'omalizumab est commercialisé en France. Les données compilées recensent 10 autorisations, toutes sous forme de solution injectable (seringue préremplie ou stylo prérempli), sans texte d'indication renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66107946 | OMLYCLO 75 mg, seringue préremplie | Solution injectable | Non renseignée |
| 62877141 | XOLAIR 75 mg, seringue préremplie | Solution injectable | Non renseignée |
| 61771263 | XOLAIR 300 mg, seringue préremplie | Solution injectable | Non renseignée |
| 61971520 | XOLAIR 150 mg, seringue préremplie | Solution injectable | Non renseignée |
| 61112487 | XOLAIR 75 mg, stylo prérempli | Solution injectable | Non renseignée |

## Considérations de sécurité

- **Interactions médicamenteuses** : 8 interactions ont été recensées. L'une est de niveau modéré (omacétaxine mépésuccinate). Les autres sont de niveau mineur (sulfate, acétate, gluconate et chlorure de zinc, échinacée, vitamine E), ainsi que la liaison à sa cible, la chaîne lourde epsilon de l'immunoglobuline.

Veuillez consulter la notice pour les mises en garde et contre-indications, qui ne sont pas disponibles dans les données compilées.

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
Aucune étude publiée ne démontre l'intérêt de l'omalizumab dans la bronchite : l'essai le plus proche porte sur l'asthme sévère avec éosinophilie persistante, sur 11 patients seulement, et suggère une efficacité possiblement insuffisante. La prédiction repose donc uniquement sur le modèle (niveau L5).

**Pour avancer, les éléments suivants sont nécessaires :**
- Des études cliniques ciblant spécifiquement un phénotype de bronchite (par exemple allergique ou éosinophilique)
- Des données détaillées sur le mécanisme d'action
- Les mises en garde et contre-indications issues de la notice officielle (ANSM)

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Omlyclo (omalizumab-igec) prescribing information, CELLTRION USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dbd8709f-1636-45d9-ba94-5a3bc5f22f84) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

