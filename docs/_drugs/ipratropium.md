---
layout: default
title: Ipratropium
parent: 僅模型預測 (L5)
nav_order: 155
evidence_level: L5
indication_count: 10
---

# Ipratropium
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

Utilisation de la connaissance intégrée dans l'Evidence Pack (littérature et essais cliniques) pour compenser les champs structurés manquants (`original_moa`, `licenses`) — sans rien inventer au-delà de ce que les sources citées démontrent. Voici le rapport :

---

# Ipratropium : Du Bronchodilatateur Anticholinergique Historique à la Confirmation dans les Maladies Pulmonaires Obstructives

## Résumé en Une Phrase

Ipratropium est un anticholinergique inhalé historiquement utilisé pour le bronchospasme réversible associé à la BPCO et à l'asthme (commercialisé notamment sous le nom Atrovent®/Combivent®).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Maladie Pulmonaire Obstructive** (*obstructive lung disease*),
avec **plus de 50 essais cliniques** et **20 publications** soutenant cette direction — une prédiction qui, comme détaillé ci-dessous, correspond en réalité à son usage déjà établi plutôt qu'à un véritable repositionnement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Bronchospasme réversible associé à la BPCO/asthme (usage anticholinergique établi — aucune donnée d'AMM structurée disponible dans ce jeu de données) |
| Nouvelle Indication Prédite | Maladie Pulmonaire Obstructive (*Obstructive Lung Disease*) |
| Score de Prédiction TxGNN | 99.97 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le champ structuré de mécanisme d'action (`original_moa`) est marqué comme donnée manquante (DG002, sévérité *High*) dans ce dossier. Cependant, la littérature indexée dans ce même Evidence Pack documente clairement le mécanisme : ipratropium est un dérivé quaternaire isopropylé de l'atropine qui **bloque les récepteurs muscariniques M3** sur le muscle lisse bronchique, interrompant la bronchoconstriction et l'hypersécrétion muqueuse médiées par le nerf vague ([PMID 2977109](https://pubmed.ncbi.nlm.nih.gov/2977109/), [PMID 3155676](https://pubmed.ncbi.nlm.nih.gov/3155676/)). C'est un antagoniste compétitif de l'acétylcholine, sans effet systémique significatif du fait de sa faible absorption après inhalation.

Ce mécanisme cible **directement** la physiopathologie des maladies pulmonaires obstructives (BPCO, asthme) : l'hypertonie cholinergique des voies aériennes en est un moteur central. Il ne s'agit donc pas d'une extrapolation mécanistique spéculative — l'usage d'ipratropium dans les pathologies obstructives est déjà une pratique clinique de plusieurs décennies, comme en témoignent les marques historiques Atrovent® et Combivent® citées dans plusieurs essais du jeu de données (ex. [NCT02177344](https://clinicaltrials.gov/study/NCT02177344), [NCT00400153](https://clinicaltrials.gov/study/NCT00400153)).

**Point d'attention analytique important** : la prédiction TxGNN rang 1 (« obstructive lung disease ») correspond donc à une **confirmation de l'indication déjà établie** du médicament plutôt qu'à une véritable opportunité de repositionnement vers un nouveau champ thérapeutique. Le `repurposing_rationale` fourni le confirme explicitement : *« attribuant son core known mechanism of action, non spéculatif »*. Ceci renforce la fiabilité de la prédiction (d'où le niveau de preuve L1), mais réduit sa valeur en tant que candidat de *drug repurposing* au sens strict. Pour une vraie découverte de nouvelle indication, les candidats de rang inférieur (ex. rang 8, « tracheal disease », niveau L3) mériteraient davantage d'attention exploratoire malgré une preuve plus faible.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00393458](https://clinicaltrials.gov/study/NCT00393458) | Phase 3 | Terminé | 1732 | Indacaterol 300/600 µg vs formoterol vs placebo dans la BPCO, essai pivot 52 semaines en double aveugle |
| [NCT05890638](https://clinicaltrials.gov/study/NCT05890638) | Phase 3 | Statut inconnu | 74 | Non-infériorité de l'association fixe Ipratropium/Levosalbutamol vs association libre en BPCO stable modérée-sévère |
| [NCT02182479](https://clinicaltrials.gov/study/NCT02182479) | Phase 3 | Terminé | 631 | Berodual® (fénotérol/ipratropium) via Respimat® vs MDI dans l'asthme sur 12 semaines, non-infériorité démontrée |
| [NCT02172404](https://clinicaltrials.gov/study/NCT02172404) | Phase 3 | Terminé | 160 | Comparaison technique d'administration HandiHaler® vs MDI chez patients BPCO |
| [NCT00371527](https://clinicaltrials.gov/study/NCT00371527) | N/A | Terminé | 200 | Essai COUGH STOP, ipratropium inhalé vs placebo sur les symptômes de bronchite aiguë |
| [NCT02177344](https://clinicaltrials.gov/study/NCT02177344) | Phase 3 | Terminé | 646 | Ipratropium bromide 20/40 µg via Respimat® vs Atrovent® MDI sur 6 mois, comparabilité clinique confirmée en BPCO |
| [NCT00400153](https://clinicaltrials.gov/study/NCT00400153) | Phase 3 | Terminé | 1480 | Ipratropium/salbutamol Respimat® vs Combivent® MDI, non-infériorité sur le VEMS en BPCO |
| [NCT02177253](https://clinicaltrials.gov/study/NCT02177253) | Phase 3 | Terminé | 1118 | Ipratropium/salbutamol Respimat® vs Combivent® Inhalation Aerosol, étude d'efficacité et sécurité sur 12 semaines |
| [NCT01019694](https://clinicaltrials.gov/study/NCT01019694) | Phase 3 | Terminé | 470 | Acceptabilité patient et sécurité à long terme de Combivent Respimat® vs formulations CFC en BPCO |
| [NCT01136421](https://clinicaltrials.gov/study/NCT01136421) | Phase 3 | Terminé | 124 | Sulfate de magnésium vs ipratropium bromide en exacerbation aiguë de BPCO aux urgences |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Revue Cochrane (RCT) | Cochrane Database Syst Rev | Tiotropium vs ipratropium dans la BPCO stable — synthèse des essais comparatifs |
| [20163324](https://pubmed.ncbi.nlm.nih.gov/20163324/) | 2010 | ECR/Revue | Expert Opin Drug Metab Toxicol | Efficacité et sécurité de l'association albutérol/ipratropium dans la BPCO, approuvée depuis >15 ans |
| [2977109](https://pubmed.ncbi.nlm.nih.gov/2977109/) | 1988 | Revue | Clinical Pharmacy | Revue de la chimie, pharmacologie, efficacité clinique et effets indésirables de l'ipratropium bromide |
| [23170031](https://pubmed.ncbi.nlm.nih.gov/23170031/) | 2012 | Étude de cohorte | Ann Pharmacother | Utilisation concomitante d'ipratropium et de tiotropium dans la BPCO |
| [7813271](https://pubmed.ncbi.nlm.nih.gov/7813271/) | 1995 | ECR | Chest | Comparaison des effets non-bronchodilatateurs de pirbutérol et ipratropium sur les échanges gazeux en BPCO |
| [8181328](https://pubmed.ncbi.nlm.nih.gov/8181328/) | 1994 | ECR multicentrique | Chest | Essai fondateur COMBIVENT (85 jours) : l'association ipratropium/albutérol est plus efficace que chaque agent seul dans la BPCO |
| [15987237](https://pubmed.ncbi.nlm.nih.gov/15987237/) | 2005 | Revue | Treat Respir Med | Revue de la formulation HFA d'ipratropium bromide (reformulation post-CFC) |
| [15257628](https://pubmed.ncbi.nlm.nih.gov/15257628/) | 2004 | Revue | Drugs | Revue de Berodual (ipratropium/fénotérol) via Respimat dans l'asthme et la BPCO |
| [28461224](https://pubmed.ncbi.nlm.nih.gov/28461224/) | 2017 | Étude de cohorte | EBioMedicine | Différences de réponse au VEMS selon le sexe chez les patients BPCO légère à modérée traités par ipratropium |
| [3155676](https://pubmed.ncbi.nlm.nih.gov/3155676/) | 1985 | Revue | Drug Intell Clin Pharm | Mécanisme d'action par inhibition compétitive des récepteurs cholinergiques du muscle lisse bronchique |

---

## Considérations de Sécurité

Les champs structurés de mises en garde et de contre-indications (`safety.key_warnings`, `safety.contraindications`) sont marqués comme données manquantes, et la recherche d'interactions médicamenteuses (DDI) n'a retourné aucun résultat (`not_found`). Il s'agit du **gap DG001**, classé sévérité *Blocking* : il empêche formellement l'entrée en étape d'évaluation de sécurité initiale (S1) tant que le RCP/notice ANSM n'a pas été récupéré et analysé.

**Veuillez consulter la notice pour les informations de sécurité officielles.**

Signal à surveiller néanmoins : la littérature associée à un autre candidat de ce dossier (indication « anaphylaxis », rang 9) rapporte un cas d'anaphylaxie sévère déclenchée par l'inhalation d'ipratropium bromide lui-même ([PMID 8449120](https://pubmed.ncbi.nlm.nih.gov/8449120/), *Chest*, 1993). Ce signal, bien que rare (rapport de cas isolé), devra être intégré à l'évaluation de sécurité une fois les données officielles TFDA/ANSM disponibles.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- La base mécanistique et l'ampleur de la preuve clinique (≥2 essais de Phase 3 complétés, >1000 patients chacun) sont solides et cohérentes — mais elles confirment une indication déjà connue plutôt qu'une découverte de repositionnement.
- Un gap de sécurité *Blocking* (DG001 — absence des mises en garde et contre-indications officielles) empêche toute progression vers l'évaluation de sécurité formelle (S1) tant qu'il n'est pas résolu, malgré la robustesse de la preuve d'efficacité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser le RCP/notice officiel (TFDA et/ou ANSM) pour lever le gap DG001 (*Blocking*) avant toute évaluation de sécurité S1.
- Compléter les données structurées de mécanisme d'action via DrugBank (gap DG002) pour formaliser l'analyse mécanistique au-delà des extraits de littérature.
- Clarifier le statut réglementaire réel en France (le médicament apparaît non commercialisé avec 0 AMM dans ce jeu de données — à vérifier, car ipratropium dispose historiquement d'AMM dans d'autres marchés européens).
- Réévaluer la classification de ce candidat : puisque l'indication prédite recoupe l'usage déjà établi, envisager de réorienter l'effort de repositionnement vers des candidats à indication réellement novatrice de ce même dossier (ex. rang 8 « tracheal disease », niveau de preuve L3, mécanisme pharmacologique direct mais sans validation clinique en indication).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

