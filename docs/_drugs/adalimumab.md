---
layout: default
title: Adalimumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 17
evidence_level: L5
indication_count: 6
---

# Adalimumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Adalimumab : De la polyarthrite rhumatoïde (indication d'origine non précisée dans les AMM) à la vascularite rhumatoïde

## Résumé en Une Phrase

Adalimumab est un anticorps monoclonal anti-TNF, indiqué dans la polyarthrite rhumatoïde selon l'argumentaire de repositionnement. Les libellés d'indication des AMM françaises ne sont pas renseignés dans les données.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **vascularite rhumatoïde**, avec **5 essais cliniques** (tous peu pertinents) et **20 publications**, principalement des cas cliniques.
Aucune donnée contrôlée n'existe pour cette indication, et le sens de l'effet reste incertain : les anti-TNF sont aussi décrits comme déclencheurs de vascularites paradoxales.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM ; polyarthrite rhumatoïde d'après l'argumentaire de repositionnement |
| Nouvelle Indication Prédite | Vascularite rhumatoïde |
| Score de Prédiction TxGNN | 99,80 % |
| Niveau de Preuve | L3 (une revue systématique et des cas cliniques, sans étude contrôlée ; le pack source indique L4) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les connaissances générales, adalimumab est un anticorps monoclonal entièrement humain qui neutralise le TNF-α. Il est utilisé dans la polyarthrite rhumatoïde et d'autres maladies inflammatoires chroniques.

La vascularite rhumatoïde est une complication extra-articulaire grave de la polyarthrite rhumatoïde, et le TNF y joue un rôle dans l'inflammation. Bloquer le TNF est donc biologiquement plausible. Une revue systématique de 2021 s'est intéressée aux traitements biologiques dans cette complication. Un cas de vascularite digitale a bien répondu à l'adalimumab.

Cependant, la direction de l'effet n'est pas claire. Plusieurs publications décrivent des vascularites, y compris à ANCA, survenant sous adalimumab ou d'autres anti-TNF. Un cas d'hypertension pulmonaire aiguë est survenu après une réduction de l'adalimumab dans une vascularite rhumatoïde. Sans données contrôlées, la plausibilité mécanistique ne suffit pas à conclure.

## Preuves d'Essais Cliniques

Les cinq essais associés sont tous classés de pertinence C : aucun n'évalue l'efficacité dans la vascularite.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Pas encore en recrutement | 80 | Gestion des immunosuppresseurs avant arthroplastie de l'épaule chez des patients rhumatologiques (poussées, douleur, complications). Pas d'évaluation de la vascularite. |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Terminé | 184 | Étude non interventionnelle sur le tocilizumab dans la polyarthrite rhumatoïde. Aucun critère propre à la vascularite. |
| [NCT05111743](https://clinicaltrials.gov/study/NCT05111743) | N/A | Terminé | 9261 | Étude de cohorte rétrospective sur le brolucizumab dans la DMLA humide. Association probablement fortuite. |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Terminé | 808 | Étude transversale sur les schémas de traitement par DMARD biologiques dans la polyarthrite rhumatoïde en Chine. Pas de données d'efficacité. |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Inconnu | 750000 | Risque de maladies inflammatoires à médiation immune incidentes sous biothérapies. Porte sur le risque, pas sur le bénéfice thérapeutique. |

## Preuves de la Littérature

Sélection des 10 publications les plus pertinentes, parmi 20.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Revue systématique | Clin Rheumatol | Revue selon PRISMA de l'usage des médicaments biologiques dans la vascularite rhumatoïde, forme sévère de manifestation extra-articulaire. |
| [18799049](https://pubmed.ncbi.nlm.nih.gov/18799049/) | 2008 | Revue systématique | Clin Exp Rheumatol | Comparaison des vascularites survenant ou non sous anti-TNF dans la polyarthrite rhumatoïde (2707 patients, 18 vascularites). |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohorte / pharmacovigilance | RMD Open | Risque d'événements de type lupus ou vascularite sous anti-TNF versus DMARD non biologiques dans la polyarthrite rhumatoïde (registre BSRBR-RA). |
| [25133007](https://pubmed.ncbi.nlm.nih.gov/25133007/) | 2014 | Cas clinique | Case Rep Rheumatol | Vascularite digitale nécrosante chez une patiente atteinte de polyarthrite rhumatoïde, bonne réponse à l'adalimumab. |
| [30773522](https://pubmed.ncbi.nlm.nih.gov/30773522/) | 2019 | Cas clinique | Intern Med | Crise aiguë d'hypertension pulmonaire huit mois après réduction de l'adalimumab dans une vascularite rhumatoïde. |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Cas clinique | Intern Med | Néphrite associée aux ANCA survenue sous abatacept et adalimumab, atténuée par le tocilizumab. |
| [28719435](https://pubmed.ncbi.nlm.nih.gov/28719435/) | 2018 | Cas clinique (effet indésirable) | Am J Dermatopathol | Vascularite leucocytoclasique avec hémophagocytose périvasculaire dermique liée à l'adalimumab. |
| [19482531](https://pubmed.ncbi.nlm.nih.gov/19482531/) | 2009 | Cas clinique | Néphrol Thér | Glomérulonéphrite extracapillaire nécrosante avec ANCA anti-myéloperoxydase chez une patiente sous adalimumab. |
| [23559388](https://pubmed.ncbi.nlm.nih.gov/23559388/) | 2013 | Cas clinique et revue | Clin Rheumatol | Premier cas de syndrome des antiphospholipides associé à l'adalimumab, avec revue des vascularites induites. |
| [36706240](https://pubmed.ncbi.nlm.nih.gov/36706240/) | 2023 | Étude de biopsies rénales | Kidney360 | Spectre des lésions rénales sous anti-TNF-α, incluant des atteintes auto-immunes. |

## Informations de Marché en France

Cinq AMM sur 20 sont listées. Le libellé d'indication n'est pas renseigné dans les données.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68619482 | AMGEVITA 20 mg, seringue préremplie (0,2 mL) | Solution injectable | Non renseignée |
| 62042376 | HULIO 40 mg, seringue préremplie | Solution injectable | Non renseignée |
| 61192750 | IMRALDI 40 mg, seringue préremplie | Solution injectable | Non renseignée |
| 65075488 | YUFLYMA 20 mg, seringue préremplie | Solution injectable | Non renseignée |
| 65973337 | LIBMYRIS 40 mg, seringue préremplie | Solution injectable | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été trouvée dans les données disponibles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucune étude contrôlée n'existe pour la vascularite rhumatoïde. Les preuves se limitent à une revue systématique et à des cas cliniques, dont plusieurs décrivent des vascularites induites par les anti-TNF, et les cinq essais listés ne sont pas pertinents.
- Les données de sécurité de la notice ANSM sont absentes, ce qui bloque le passage à l'étape de sélection de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Examiner en détail la revue systématique de 2021 pour évaluer l'efficacité des biothérapies dans la vascularite rhumatoïde
- Clarifier le risque de vascularite paradoxale sous anti-TNF avant toute étude prospective

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement nécessite une validation clinique.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

