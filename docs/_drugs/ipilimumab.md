---
layout: default
title: Ipilimumab
parent: 僅模型預測 (L5)
nav_order: 154
evidence_level: L5
indication_count: 2
---

# Ipilimumab
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

# Ipilimumab : Du Mélanome Cutané Avancé au Mélanome Non Cutané

## Résumé en Une Phrase

Ipilimumab est un anticorps monoclonal anti-CTLA-4, approuvé à l'origine pour le traitement du mélanome avancé (non résécable ou métastatique), majoritairement d'origine cutanée. Le modèle TxGNN prédit qu'il pourrait également être efficace pour le **Mélanome Non Cutané** (sous-types uvéal et muqueux), avec **plus de 50 essais cliniques identifiés** (dont plusieurs essais de Phase III achevés) et **5 publications** soutenant actuellement cette direction. Une seconde prédiction du modèle — la choroïdérémie — a été écartée de ce rapport : bien que son score TxGNN soit élevé (99,06 %), aucune preuve clinique ni mécanistique ne l'appuie, et elle est considérée comme du bruit du modèle (recommandation : Hold).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Mélanome avancé (non résécable ou métastatique) |
| Nouvelle Indication Prédite | Mélanome Non Cutané (uvéal / muqueux) |
| Score de Prédiction TxGNN | 99,02 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données formelles de mécanisme d'action issues de DrugBank ne sont actuellement pas disponibles pour ce médicament (écart de données identifié, sévérité élevée). Sur la base des informations disponibles dans les preuves cliniques et la littérature, ipilimumab est un anticorps monoclonal dirigé contre CTLA-4, une molécule inhibitrice exprimée sur les lymphocytes T. En bloquant CTLA-4, ipilimumab lève un frein physiologique sur l'activation des lymphocytes T, ce qui restaure et amplifie la réponse immunitaire anti-tumorale spécifique de la tumeur.

Ce mécanisme ne dépend pas de l'origine histologique du mélanome (cutané vs uvéal vs muqueux) : il agit sur le système immunitaire de l'hôte plutôt que sur une cible moléculaire propre aux cellules tumorales. Il existe donc une plausibilité biologique directe pour étendre l'usage d'ipilimumab au mélanome non cutané, dont le mélanome uvéal et le mélanome muqueux, qui partagent avec le mélanome cutané la caractéristique d'être des tumeurs immunogènes potentiellement sensibles au blocage des points de contrôle immunitaire.

Cette plausibilité est en outre corroborée par des preuves cliniques directes : l'essai NCT02626962 évalue spécifiquement nivolumab + ipilimumab dans le mélanome uvéal métastatique, et la publication PMID 24999899 rapporte l'efficacité et la tolérance d'ipilimumab chez des patients atteints de mélanome cutané, uvéal et muqueux en contexte réel. Ipilimumab est par ailleurs déjà un composant standard de multiples associations thérapeutiques (avec nivolumab notamment) approuvées dans le mélanome avancé toutes localisations confondues.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02224781](https://clinicaltrials.gov/study/NCT02224781) | Phase 3 | Actif, non recruteur | 267 | Essai DREAMseq comparant l'ordre de traitement ipilimumab+nivolumab puis dabrafenib+trametinib vs l'inverse, mélanome de stade III-IV BRAF V600 mutant |
| [NCT02939300](https://clinicaltrials.gov/study/NCT02939300) | Phase 2 | Terminé | 18 | Ipilimumab + nivolumab pour métastases leptoméningées d'origine mélanique |
| [NCT03645928](https://clinicaltrials.gov/study/NCT03645928) | Phase 2 | En cours de recrutement | 245 | Thérapie cellulaire TIL (lifileucel) associée aux inhibiteurs de point de contrôle immunitaire dans les tumeurs solides |
| [NCT04133948](https://clinicaltrials.gov/study/NCT04133948) | Phase 1b/2 | Terminé | 44 | Combinaison néoadjuvante domatinostat + nivolumab ± ipilimumab, mélanome de stade III |
| [NCT01654692](https://clinicaltrials.gov/study/NCT01654692) | Phase 2 | Terminé | 86 | Ipilimumab + fotémustine dans le mélanome malin avancé non résécable ou métastatique |
| [NCT01496807](https://clinicaltrials.gov/study/NCT01496807) | Phase 1b | Terminé | 31 | Yervoy (ipilimumab) + Sylatron (peginterféron) dans le mélanome de stade IIIB/C/IV non résécable |
| [NCT01927419](https://clinicaltrials.gov/study/NCT01927419) | Phase 2 | Terminé | 142 | Nivolumab + ipilimumab vs ipilimumab seul, mélanome avancé non traité |
| [NCT01810016](https://clinicaltrials.gov/study/NCT01810016) | Phase 1 | Arrêté | 8 | Vaccin NY-ESO-1 + ipilimumab dans le mélanome non résécable ou métastatique |
| [NCT02452294](https://clinicaltrials.gov/study/NCT02452294) | Phase 2 | Statut inconnu | 22 | Buparlisib chez des patients en échec d'ipilimumab, mélanome métastatique avec métastases cérébrales |
| [NCT01940809](https://clinicaltrials.gov/study/NCT01940809) | Phase 1 | Arrêté | 15 | Ipilimumab ± dabrafenib/trametinib/nivolumab dans le mélanome métastatique BRAF muté |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [24999899](https://pubmed.ncbi.nlm.nih.gov/24999899/) | 2014 | Cohorte | The Medical Journal of Australia | Efficacité et tolérance d'ipilimumab en pratique clinique australienne, incluant mélanome uvéal et muqueux |
| [29466692](https://pubmed.ncbi.nlm.nih.gov/29466692/) | 2018 | Revue | Discovery Medicine | Mise à jour clinique des anti-PD-1 seuls ou associés à ipilimumab dans le mélanome avancé |
| [37887546](https://pubmed.ncbi.nlm.nih.gov/37887546/) | 2023 | Cohorte | Current Oncology (Toronto) | Comparaison de la survie globale selon l'âge chez des patients sous anti-PD-1 ± ipilimumab pour mélanome avancé |
| [28183255](https://pubmed.ncbi.nlm.nih.gov/28183255/) | 2018 | Revue | Current Cancer Drug Targets | Revue des essais de traitement adjuvant du mélanome (2000-2015) ; le mélanome non cutané représente ~5 % des cas |
| [40236344](https://pubmed.ncbi.nlm.nih.gov/40236344/) | 2025 | Rapport de cas | Cureus | Cas de métastase mélanique colique traité par immunothérapie, illustrant les effets indésirables gastro-intestinaux associés |

---

## Informations de Marché en France

Ipilimumab n'est actuellement **pas commercialisé** dans le périmètre réglementaire évalué (0 AMM recensée). Aucune donnée d'indication approuvée localement n'est donc disponible à ce stade.

---

## Cytotoxicité

Ipilimumab est un médicament antinéoplasique (traitement de tumeurs malignes), mais il s'agit d'une immunothérapie et non d'une chimiothérapie cytotoxique conventionnelle.

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Immunothérapie — inhibiteur de point de contrôle immunitaire anti-CTLA-4 (non cytotoxique au sens conventionnel) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Le niveau de preuve L1 repose sur plusieurs essais de Phase III achevés (dont NCT01515189, NCT02905266, NCT02388906/CheckMate 238) démontrant l'efficacité et le profil de sécurité connu d'ipilimumab dans le mélanome avancé, complétés par un essai ciblant spécifiquement le mélanome uvéal (NCT02626962) et une étude de cohorte réelle couvrant les sous-types uvéal et muqueux (PMID 24999899). Le mécanisme d'action, indépendant de l'origine histologique de la tumeur, renforce la plausibilité de cette extension d'indication. Toutefois, l'absence de données réglementaires locales (仿單/警語) et l'absence de commercialisation actuelle imposent une progression encadrée plutôt qu'une recommandation ferme.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les mises en garde, contre-indications et interactions médicamenteuses officielles (notice/仿單) — écart bloquant actuellement l'évaluation de sécurité (S1)
- Compléter les données formelles de mécanisme d'action (DrugBank)
- Constituer un dossier de preuves clinique spécifique aux sous-types non cutanés (uvéal, muqueux) en vue d'une éventuelle demande d'extension d'indication ou d'AMM locale
- Écarter la piste choroïdérémie de tout développement ultérieur (niveau de preuve L5, aucun lien mécanistique connu, recommandation Hold)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

