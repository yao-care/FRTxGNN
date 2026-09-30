---
layout: default
title: Lomustine
parent: Prédiction du modèle uniquement (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
---

# Lomustine
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

# Lomustine : Repositionnement vers le Lymphosarcome

## Résumé en Une Phrase

La lomustine est un agent alkylant de la famille des nitrosourées, disponible en France sous forme de gélules (LOMUSTINE MEDAC 40 mg et BELUSTINE 40 mg). Le texte de l'indication approuvée n'est pas renseigné dans les données AMM disponibles.
Le modèle TxGNN prédit qu'elle pourrait être utile dans le **lymphosarcome** (lymphome non hodgkinien), avec **17 essais cliniques enregistrés** (dont seule une minorité est directement pertinente) et **20 publications**. Ces preuves portent presque toutes sur des associations de chimiothérapies, dans de petites études.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données AMM disponibles |
| Nouvelle Indication Prédite | Lymphosarcome |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L2 (à nuancer : essais de phase 2 de petite taille, rôle propre de la lomustine non isolé) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans DrugBank. Le raisonnement ci-dessous repose donc sur la pharmacologie générale. La lomustine est une nitrosourée lipophile qui alkyle l'ADN : elle provoque une chloroéthylation et des pontages inter-brins. Elle traverse aussi la barrière hémato-encéphalique.

Ces propriétés cadrent bien avec les hémopathies lymphoïdes, surtout lorsque le système nerveux central est touché. La lomustine entre déjà dans plusieurs protocoles polychimiothérapiques du lymphome : LEMP, R-MPL (rituximab, méthotrexate, procarbazine, lomustine) pour le lymphome cérébral primitif, et un protocole oral associant lomustine, étoposide, cyclophosphamide et procarbazine pour les lymphomes liés au VIH.

**Limite importante :** la contribution propre de la lomustine ne peut pas être séparée de celle des autres médicaments de ces associations. Le terme « lymphosarcome » est ancien et recouvre aujourd'hui les lymphomes non hodgkiniens.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00049439](https://clinicaltrials.gov/study/NCT00049439) | Phase 2 | Terminé | 54 | Chimiothérapie orale à doses modifiées (lomustine, étoposide, cyclophosphamide, procarbazine) dans le LNH lié au SIDA. Jeu de données le plus important et directement pertinent, mais en association. |
| [NCT00003114](https://clinicaltrials.gov/study/NCT00003114) | Phase 2 | Terminé | 5 | Même type d'association orale dans la maladie de Hodgkin liée au SIDA. Effectif trop faible. |
| [NCT01775475](https://clinicaltrials.gov/study/NCT01775475) | Phase 2 | Terminé | 7 | Essai randomisé CHOP vs chimiothérapie orale dans le lymphome lié au VIH en Afrique subsaharienne. Régime oral probablement à base de lomustine (non confirmé). Sous-dimensionné. |
| [NCT00003113](https://clinicaltrials.gov/study/NCT00003113) | Phase 2 | Arrêté | 6 | Chimiothérapie orale avec G-CSF chez le sujet âgé atteint de LNH de grade intermédiaire/élevé. Trop petit pour conclure. |
| [NCT00074191](https://clinicaltrials.gov/study/NCT00074191) | Phase 2 | Terminé | 1 | Méthotrexate, procarbazine et CCNU avec traitement intraventriculaire dans le lymphome cérébral primitif. Non informatif sur l'efficacité. |
| [NCT00989352](https://clinicaltrials.gov/study/NCT00989352) | Phase 2 | Inconnu | 56 | Rituximab, méthotrexate à haute dose, lomustine et procarbazine, puis entretien, dans le lymphome cérébral primitif chez les plus de 65 ans. |
| [NCT00003929](https://clinicaltrials.gov/study/NCT00003929) | Phase 2 | Retiré | 0 | Lomustine, procarbazine, filgrastim et radiothérapie dans le lymphome cérébral primitif. Aucun patient inclus. |
| [NCT05518383](https://clinicaltrials.gov/study/NCT05518383) | Phase 4 | En recrutement | 300 | Protocole pédiatrique de LNH B mature. Rôle de la lomustine non évident. |
| [NCT00317408](https://clinicaltrials.gov/study/NCT00317408) | Non applicable | Inconnu | 96 | Protocole du lymphome anaplasique à grandes cellules pédiatrique en rechute. Rôle de la lomustine non précisé. |
| [NCT02551718](https://clinicaltrials.gov/study/NCT02551718) | Non applicable | Terminé | 34 | Traitement individualisé de la leucémie aiguë en rechute. Pathologie différente, rôle de la lomustine peu clair. |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [348294](https://pubmed.ncbi.nlm.nih.gov/348294/) | 1978 | ECR | Cancer | CCNU vs méthyl-CCNU en dose orale unique toutes les 6 semaines dans les lymphomes avancés, dont le lymphosarcome. |
| [2259920](https://pubmed.ncbi.nlm.nih.gov/2259920/) | 1990 | Phase 2 | Semin Oncol | Protocole CAMP (avec lomustine) dans le LNH résistant à la doxorubicine : rémission complète 27 %, partielle 20 % (30 patients). |
| [8436213](https://pubmed.ncbi.nlm.nih.gov/8436213/) | 1993 | Cohorte | Eur J Haematol | Protocole LEMP dans le LNH en rechute ou réfractaire (22 patients). |
| [8422281](https://pubmed.ncbi.nlm.nih.gov/8422281/) | 1993 | Cohorte | Eur J Cancer | Protocole PACET dans le LNH en rechute ou réfractaire : rémission complète 26 %, survie médiane 6 mois, myélosuppression intense. |
| [10711848](https://pubmed.ncbi.nlm.nih.gov/10711848/) | 1999 | Revue | Drugs | Chimiothérapie orale (lomustine, étoposide, cyclophosphamide, procarbazine) chez 38 patients atteints de LNH lié au SIDA. |
| [15803492](https://pubmed.ncbi.nlm.nih.gov/15803492/) | 2005 | Phase 2 | Cancer | Protocole CIBO-P (lomustine, ifosfamide, bléomycine, vincristine, cisplatine) dans le LNH agressif réfractaire ou en rechutes multiples. |
| [21303800](https://pubmed.ncbi.nlm.nih.gov/21303800/) | 2011 | Cohorte | Ann Oncol | Étude pilote R-MPL (rituximab, méthotrexate, procarbazine, lomustine) dans le lymphome cérébral primitif du sujet âgé. |
| [33336792](https://pubmed.ncbi.nlm.nih.gov/33336792/) | 2021 | Cohorte | Br J Haematol | Protocole oral DECC (dexaméthasone, étoposide, chlorambucil, lomustine) dans le lymphome diffus à grandes cellules B en rechute ou réfractaire. |
| [30197327](https://pubmed.ncbi.nlm.nih.gov/30197327/) | 2018 | Cohorte | J Cancer Res Ther | Conditionnement LACE (avec lomustine) avant autogreffe dans le lymphome réfractaire ou en rechute : toxicité et devenir à long terme. |
| [22888657](https://pubmed.ncbi.nlm.nih.gov/22888657/) | 2012 | Préclinique (souris) | Vopr Onkol | Gemcitabine et lomustine sur le lymphosarcome intracrânien LIO-1 : survie multipliée par 3,3 avec l'association. |

Plusieurs études vétérinaires (protocole LOPP dans le lymphome canin, lomustine dans le lymphome cérébral félin) vont dans le même sens, mais ne sont pas extrapolables à l'humain.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 66274639 | LOMUSTINE MEDAC 40 mg, gélule | Gélule | MEDAC GESELLSCHAFT FUR KLINISCHE SPEZIALPRAPARATE (Allemagne) |
| 69651223 | BELUSTINE 40 mg, gélule | Gélule | KYOWA KIRIN HOLDINGS (Pays-Bas) |

Le texte des indications approuvées n'est pas renseigné pour ces deux AMM.

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (agent alkylant, nitrosourée) |
| Risque de Myélosuppression | Élevé. Les publications du dossier signalent une myélosuppression intense en association (PACET) et une aplasie médullaire après surdosage (cas vétérinaire). |
| Classification d'Émétogénicité | Moyenne à élevée (selon la classe pharmacologique, à confirmer dans la notice) |
| Éléments de Surveillance | NFS avec plaquettes, fonction hépatique et rénale. Surveillance pulmonaire (toxicité pulmonaire documentée pour les nitrosourées). |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les preuves viennent de petits essais de phase 2 et de cohortes anciennes, toujours en association. La contribution propre de la lomustine n'est pas isolable, et plusieurs essais listés ne confirment pas sa présence dans le schéma.
- Les données de sécurité de la notice ANSM sont absentes (lacune bloquante), ce qui empêche le passage au criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications) et le texte des indications des deux AMM
- Compléter le mécanisme d'action depuis DrugBank
- Vérifier la présence réelle de la lomustine dans les protocoles de NCT01775475, NCT00989352 et NCT05518383
- Rechercher des essais randomisés comparant la lomustine seule ou en association à un traitement de référence dans le LNH

Les neuf autres indications prédites (surtout des tumeurs du système nerveux central) ne sont pas traitées ici.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

