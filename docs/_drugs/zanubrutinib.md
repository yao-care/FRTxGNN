---
layout: default
title: Zanubrutinib
parent: 僅模型預測 (L5)
nav_order: 333
evidence_level: L5
indication_count: 6
---

# Zanubrutinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Zanubrutinib : Des Néoplasmes Lymphoïdes B à la Leucémie Myéloïde

## Resume en Une Phrase

Zanubrutinib est un inhibiteur de BTK (Bruton's tyrosine kinase) de seconde generation, utilise pour le traitement des tumeurs malignes lymphoides a cellules B (LLC/LPL, macroglobulinemie de Waldenstrom, lymphome a cellules du manteau, lymphome de la zone marginale). Le modele TxGNN predit qu'il pourrait etre efficace pour la **Leucemie Myeloide**, mais seulement **2 essais cliniques** et **9 publications** sont actuellement associes a cette piste — et aucun ne demontre directement l'efficacite du zanubrutinib lui-meme dans cette indication.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Tumeurs malignes lymphoides a cellules B (LLC/LPL, macroglobulinemie de Waldenstrom, lymphome a cellules du manteau, lymphome de la zone marginale) |
| Nouvelle Indication Predite | Leucemie Myeloide |
| Score de Prediction TxGNN | 99.65% |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Non commercialise |
| Nombre d'AMM | 0 |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Zanubrutinib inhibe la tyrosine kinase de Bruton (BTK), une enzyme cle de la voie de signalisation du recepteur des cellules B (BCR). Cette voie est le moteur pathogenique des tumeurs lymphoides B, ce qui explique l'efficacite etablie du medicament dans la LLC/LPL et les pathologies apparentees.

La leucemie myeloide (LAM/LMC/SMD), en revanche, est portee par des mecanismes moleculaires distincts — mutations FLT3-ITD, fusion BCR-ABL, NPM1, ou dereglements epigenetiques — qui ne recoupent pas la voie BCR/BTK de maniere etablie. Le lien mecanistique entre l'inhibition de BTK et la leucemie myeloide est donc juge faible et largement speculatif : quelques travaux suggerent une expression accessoire de BTK dans certaines lignees de LAM, mais elle n'est pas reconnue comme une cible therapeutique validee.

Le score eleve attribue par TxGNN refleche vraisemblablement une similarite dans l'espace d'embedding du graphe de connaissances plutot qu'une base biologique solide. Aucune donnee clinique ne vient a ce stade etayer une transposition directe.

---

## Preuves d'Essais Cliniques

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Phase 1 | Termine | 86 | Etude du PRT2527 (inhibiteur de CDK9), evalue en monotherapie et en combinaison avec le zanubrutinib ou le venetoclax dans les hemopathies malignes R/R ; le zanubrutinib n'est utilise qu'en association, l'agent teste est PRT2527. |
| [NCT04477291](https://clinicaltrials.gov/study/NCT04477291) | Phase 1a/b | Termine (arret premature) | 45 | Etude du CG-806 (luxeptinib, inhibiteur multi-kinase FLT3/BTK) dans la LAM R/R ou les SMD a haut risque ; ne teste pas le zanubrutinib, et l'essai a ete interrompu. |

*Aucun de ces deux essais ne constitue une preuve directe de l'efficacite du zanubrutinib dans la leucemie myeloide.*

---

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | ECR (suivi) | J Clin Oncol | Suivi a 5 ans de l'essai SEQUOIA : zanubrutinib vs bendamustine-rituximab dans la LLC/LPL naive de traitement (hors leucemie myeloide). |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Cohorte (Phase 2) | Blood Adv | Tolerance et efficacite du zanubrutinib chez des patients LLC/LPL intolerants a l'ibrutinib/acalabrutinib. |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Analyse poolee | Blood Adv | Efficacite du zanubrutinib dans la LLC/LPL avec del(17p)/mutation TP53, donnees issues de SEQUOIA et ALPINE. |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Cohorte (Phase 2) | Lancet Haematol | Zanubrutinib chez des patients intolerants aux inhibiteurs de BTK anterieurs, hemopathies a cellules B. |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Revue | Pharmaceutics | Revue sur les inhibiteurs de tyrosine kinase dans la LMC et la LLC — mentionne le zanubrutinib dans le contexte BTK/BCR, pas de donnees myeloides directes. |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Revue | Leukemia | Prise en charge de la macroglobulinemie de Waldenstrom par inhibiteurs de BTK. |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Rapport de cas | Front Immunol | Cas de coexistence macroglobulinemie de Waldenstrom / LAL-B, sans lien direct avec le zanubrutinib en leucemie myeloide. |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Revue | Clin Lymphoma Myeloma Leuk | Reactivation du VHB sous inhibiteurs de BTK (dont zanubrutinib) dans les hemopathies a cellules B. |
| [38288815](https://pubmed.ncbi.nlm.nih.gov/38288815/) | 2024 | Revue (chimie de synthese) | Anticancer Agents Med Chem | Revue methodologique sur la synthese de medicaments anticancereux approuves par la FDA (2018-2021), sans donnees d'efficacite clinique. |

*L'ensemble de ces publications documente l'usage du zanubrutinib dans les hemopathies lymphoides a cellules B (LLC/LPL, macroglobulinemie de Waldenstrom) ; aucune n'evalue son efficacite dans la leucemie myeloide.*

---

## Informations de Marche en France

Zanubrutinib n'est actuellement associe a aucune Autorisation de Mise sur le Marche (AMM) enregistree en France (statut : non commercialise, 0 licence).

---

## Cytotoxicite

| Element | Contenu |
|------|------|
| Classification de Cytotoxicite | Therapie ciblee (inhibiteur de BTK) |
| Risque de Myelosuppression | Veuillez consulter les mises en garde et precautions de la notice |
| Classification d'Emetogenicite | Veuillez consulter les mises en garde et precautions de la notice |
| Elements de Surveillance | Veuillez consulter les mises en garde et precautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et precautions de la notice |

---

## Considerations de Securite

Veuillez consulter la notice pour les informations de securite.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
Le lien mecanistique entre l'inhibition de BTK et la leucemie myeloide est juge faible et speculatif, et aucune des preuves disponibles (2 essais cliniques, 9 publications) ne porte reellement sur l'efficacite du zanubrutinib dans cette indication — les essais testent d'autres molecules (ou sont arretes prematurement) et la litterature concerne exclusivement les hemopathies lymphoides B. Le niveau de preuve global est L5 (prediction du modele seule).

**Pour avancer, les elements suivants sont necessaires :**
- Obtention des mises en garde/contre-indications TFDA (donnee bloquante actuellement manquante)
- Donnees detaillees sur le mecanisme d'action (MOA) via DrugBank
- Etudes precliniques dediees testant specifiquement le zanubrutinib dans des modeles de leucemie myeloide (LAM/LMC/SMD)
- Le cas echeant, un essai clinique de phase precoce evaluant le zanubrutinib (seul, et non en association) dans cette population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

