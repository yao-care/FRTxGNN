---
layout: default
title: Sirolimus
parent: Prédiction du modèle uniquement (L5)
nav_order: 284
evidence_level: L5
indication_count: 10
---

# Sirolimus
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Sirolimus : De l'indication d'origine (non renseignée) au liposarcome

## Résumé en Une Phrase

Le sirolimus est un inhibiteur de mTORC1 commercialisé en France sous le nom RAPAMUNE, mais l'indication d'origine n'est pas renseignée dans les données réglementaires disponibles.
Le modèle TxGNN prédit qu'il pourrait être efficace dans le **liposarcome**, avec **5 essais cliniques** et **12 publications** associés.
Ces preuves restent surtout indirectes : un seul essai de phase 2 utilise le sirolimus, les autres portent sur d'autres inhibiteurs de mTOR.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les textes d'AMM fournis |
| Nouvelle Indication Prédite | Liposarcome |
| Score de Prédiction TxGNN | 99,89 % |
| Niveau de Preuve | L2 (phase 2 complétées à un seul bras, sans ECR de phase 3) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 4 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées du mécanisme d'action ne figurent pas dans la fiche du médicament. Le dossier indique cependant que le sirolimus inhibe mTORC1, une kinase centrale de la croissance et de la survie cellulaires. Cette voie est souvent dérégulée dans les sarcomes.

Dans le liposarcome dédifférencié, une activation des voies Akt-mTOR et MAPK a été observée sur 99 échantillons tumoraux (PMID 26518767). Des modèles précliniques montrent aussi une synergie entre la rapamycine (sirolimus) et la chloroquine, qui bloque l'autophagie, sur des xénogreffes dérivées de patients (PMID 36309387, 37400145).

Cette piste reste toutefois de niveau recherche. La plupart des essais cliniques cités utilisent d'autres analogues de la rapamycine (témsirolimus, ridaforolimus, évérolimus) ou des populations mixtes de sarcomes. Aucun résultat randomisé positif spécifique au liposarcome n'est présent dans le dossier.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Terminé | 70 | Sirolimus + cyclophosphamide dans le liposarcome myxoïde et le chondrosarcome métastatiques ou non résécables ; bras unique, résultats non fournis |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Terminé | 24 | Témsirolimus + doxorubicine liposomale dans les sarcomes récidivants des tissus mous et de l'os ; recherche de la dose sûre, puis efficacité |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Terminé | 46 | Cixutumumab + témsirolimus chez l'enfant avec tumeurs solides récidivantes ou réfractaires ; population peu applicable au liposarcome |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Terminé | 216 | Ridaforolimus (inhibiteur de mTOR) dans le sarcome avancé ; grande cohorte incluant des liposarcomes |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Actif, hors recrutement | 48 | Ribociclib + évérolimus dans le liposarcome dédifférencié et le léiomyosarcome avancés, après au moins une ligne systémique |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Essai de phase 2 | Clin Cancer Res | Ribociclib + évérolimus dans le liposarcome dédifférencié et le léiomyosarcome ; résumé tronqué, résultats non disponibles |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | ECR (indirect) | J Am Soc Nephrol | 430 greffés rénaux randomisés : le sirolimus après arrêt précoce de la ciclosporine réduit le risque de cancer. Contexte de transplantation, pas de sarcome |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Préclinique | Tumour Biol | Activation des voies Akt-mTOR et MAPK dans 99 liposarcomes dédifférenciés ; étude in vitro d'un inhibiteur de mTOR |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | Préclinique | Cancer Genomics Proteomics | Chloroquine + rapamycine : combinaison synergique sur l'autophagie dans le liposarcome bien différencié |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | Préclinique | In Vivo | Chloroquine + rapamycine : arrêt de la croissance tumorale dans un modèle de xénogreffe orthotopique de liposarcome dédifférencié |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | Préclinique | Mol Cancer Ther | Inhibiteur de mTOR ATP-compétitif MLN0128 : activité antitumorale dans les sarcomes osseux et des tissus mous. Les rapalogues ont eu une utilité clinique limitée |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Revue | Cancers | Panorama des nouvelles thérapeutiques dans les sarcomes des tissus mous |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Revue | Curr Opin Oncol | Justification et résultats des essais de thérapies ciblées dans les sarcomes avancés |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Revue | Bull Cancer | Traitements ciblés des tumeurs conjonctives rares et des sarcomes |
| [20534289](https://pubmed.ncbi.nlm.nih.gov/20534289/) | 2010 | Étude clinique (indirect) | Transplant Proc | Conversion à la rapamycine après une tumeur maligne chez des greffés rénaux ; contexte de transplantation |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61752409 | RAPAMUNE 1 mg/ml, solution buvable | Solution buvable | Non renseignée |
| 64597615 | RAPAMUNE 1 mg, comprimé enrobé | Comprimé enrobé | Non renseignée |
| 65164182 | RAPAMUNE 2 mg, comprimé enrobé | Comprimé enrobé | Non renseignée |
| 69171174 | RAPAMUNE 0,5 mg, comprimé enrobé | Comprimé enrobé | Non renseignée |

Les quatre AMM appartiennent à PFIZER EUROPE MA EEIG (Belgique).

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le soutien clinique direct est mince : un seul essai de phase 2 à bras unique utilise le sirolimus dans ce contexte, sans résultat exploitable dans le dossier.
- Les autres données concernent d'autres analogues de mTOR, des populations mixtes ou des modèles précliniques.
- Les données de sécurité de la notice ANSM manquent et bloquent l'étape de screening de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications, interactions).
- Obtenir les données détaillées du mécanisme d'action (DrugBank) et l'indication d'origine de l'AMM.
- Vérifier les résultats publiés de NCT02821507 et la répartition des sous-types histologiques (myxoïde, dédifférencié).
- Rechercher des données prospectives spécifiques au sirolimus dans le liposarcome.

Parmi les autres prédictions du même dossier, la **lymphangioléiomyomatose** (niveau L2, « Proceed with Guardrails ») est de loin la mieux étayée pour le sirolimus. Elle s'appuie notamment sur l'étude MIDAS (NCT02432560) et l'essai RESULT (NCT03253913). Ce résultat est fourni à titre indicatif et sans valeur de recommandation clinique : il s'agit d'une piste de recherche à valider avant toute application.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

