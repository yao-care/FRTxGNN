---
layout: default
title: Busulfan
parent: 僅模型預測 (L5)
nav_order: 62
evidence_level: L5
indication_count: 10
---

# Busulfan
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

# Busulfan : Du Conditionnement pour Leucémie au Syndrome Myélodysplasique

## Résumé en Une Phrase

Busulfan est un agent alkylant bisfonctionnel classiquement utilisé comme traitement de conditionnement myéloablatif avant la transplantation de cellules souches hématopoïétiques (TCSH) dans les leucémies et hémopathies malignes.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Syndrome Myélodysplasique (SMD)**, avec **plus de 10 essais cliniques de Phase 2/3** et **20 publications** soutenant cette direction — dont un essai pivotal de Phase 3 dans Lancet Haematology.
Il convient de noter que cette association est cliniquement établie : le modèle TxGNN valide ici une indication déjà fondée sur des preuves robustes plutôt qu'un repositionnement au sens traditionnel.

---

## Aperçu Rapide

| Élément | Contenu |
|---------|---------|
| Indication Originale | Conditionnement myéloablatif pour TCSH (leucémies, hémopathies malignes) |
| Nouvelle Indication Prédite | Syndrome Myélodysplasique |
| Score de Prédiction TxGNN | 99.62% |
| Niveau de Preuve | L1 |
| Statut de Marché | Non commercialisé (aucune AMM répertoriée dans les données disponibles) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action de busulfan ne sont pas disponibles dans ce dossier. Sur la base des informations connues, busulfan est un agent alkylant bisfonctionnel de la classe des sulfonates d'alkyls dont l'action myéloablative est bien établie : il forme des liaisons croisées entre les brins d'ADN des cellules hématopoïétiques, provoquant leur destruction. Administré par voie intraveineuse à doses myéloablatives ou d'intensité réduite, busulfan élimine les cellules souches hématopoïétiques anormales et crée un espace médullaire pour la greffe du donneur — mécanisme directement applicable au SMD.

Le syndrome myélodysplasique est un groupe de maladies clonales des cellules souches hématopoïétiques caractérisées par une hématopoïèse inefficace, des cytopénies et un risque de transformation en leucémie aiguë myéloïde. La TCSH allogénique demeure le seul traitement potentiellement curatif pour les patients à risque intermédiaire-2 et élevé (score IPSS-R). La connexion mécanistique est directe : en détruisant le clone myélodysplasique, busulfan prépare la moelle pour la reconstitution hématopoïétique par les cellules du donneur sain. Ce mécanisme est partagé entre leucémie (indication originale) et SMD (indication prédite), tous deux étant des hémopathies clonales d'origine médullaire.

La robustesse de cette prédiction est confirmée par l'essai pivotal MC-FludT.14/L (Phase 3, PMID 31606445, Lancet Haematology 2020, n=476), qui compare directement busulfan+fludarabine versus tréosulfan+fludarabine chez des patients âgés atteints de SMD ou de LAM avant TCSH, établissant busulfan comme référence active. Deux autres essais (NCT06477549, NCT02250937) utilisent busulfan comme composant central du régime de conditionnement spécifiquement pour SMD.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|----------------|-------|--------|-------------|---------------------|
| [NCT06477549](https://clinicaltrials.gov/study/NCT06477549) | Phase 2 | En cours de recrutement | 220 | RCT comparant bendamustine vs ruxolitinib avec fludarabine+busulfan comme base de conditionnement pour TCSH haploidentique dans diverses hémopathies incluant SMD — busulfan comme médicament central du protocole |
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Phase 2 | Actif, recrutement terminé | 116 | Busulfan séquentiel timed + venetoclax + cladribine + fludarabine avant TCSH pour LAM et SMD — évalue l'ajout de venetoclax à un conditionnement busulfan-central |
| [NCT00863148](https://clinicaltrials.gov/study/NCT00863148) | Phase 2 | Terminé | 30 | Clofarabine + busulfan IV + thymoglobuline (CBT) en conditionnement d'intensité réduite pour TCSH chez adultes avec LAM, SMD ou LAL à haut risque |
| [NCT01643668](https://clinicaltrials.gov/study/NCT01643668) | Phase 2 | Terminé | 34 | Conditionnement d'intensité réduite busulfan/clofarabine suivi de TCSH allogénique pour hémopathies malignes |
| [NCT01252784](https://clinicaltrials.gov/study/NCT01252784) | N/A | Inconnu | 20 | Conditionnement d'intensité réduite + TCSH allogénique suivi de DLI prophylactiques dose-escalating pour SMD à haut risque — évalue la faisabilité et l'efficacité |
| [NCT01177371](https://clinicaltrials.gov/study/NCT01177371) | Phase 2 | Terminé | 13 | Haute dose busulfan + cyclophosphamide + TCSH allogénique pour leucémie, SMD, myélome multiple et lymphome |
| [NCT00186342](https://clinicaltrials.gov/study/NCT00186342) | N/A | Terminé | 120 | TCSH allogénique (apparenté et non apparenté) avec busulfan, étoposide et cyclophosphamide — évaluation tolérance et efficacité chez patients 51–60 ans avec SMD/MAP |
| [NCT03412266](https://clinicaltrials.gov/study/NCT03412266) | Phase 2 | Inconnu | 50 | Conditionnement d'intensité réduite pour SMD de faible et moyen risque en TCSH haploidentique — évaluation de l'efficacité du régime RIC dans cette population |
| [NCT00521430](https://clinicaltrials.gov/study/NCT00521430) | N/A | Terminé | 30 | TCSH haploidentique non déplété en cellules T après conditionnement d'intensité réduite (incluant busulfan) pour hémopathies malignes dont SMD |
| [NCT00014469](https://clinicaltrials.gov/study/NCT00014469) | Phase 2 | Terminé | N/A | Busulfan IV (Busulfex) + melphalan comme régime préparatoire avant TCSH allogénique pour hémopathies malignes avancées et à haut risque |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-------|------|-------|---------------------|
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | Phase 3 RCT — analyse finale | Am J Hematol | Analyse finale de l'essai MC-FludT.14/L (n=476) : tréosulfan non-inférieur à busulfan RIC chez patients âgés avec SMD/LAM avant TCSH — confirme busulfan comme référence clinique |
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | Phase 3 RCT | Lancet Haematol | MC-FludT.14/L : tréosulfan+fludarabine vs **busulfan+fludarabine** pour SMD/LAM chez patients âgés — comparateur busulfan établi comme standard actif (n=476) |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | Phase 3 RCT | Lancet Haematol | G-CSF+décitabine+**busulfan-cyclophosphamide** vs busulfan-cyclophosphamide seul : réduction significative des rechutes post-TCSH dans SMD-RAEB et LAM secondaire à SMD |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Méta-analyse / suivi long terme | Front Oncol | Résultats à long terme tréosulfan vs busulfan pour SMD/LAM avant TCSH — revue systématique et méta-analyse des données poolées |
| [28380315](https://pubmed.ncbi.nlm.nih.gov/28380315/) | 2017 | RCT prospective Phase 3 | J Clin Oncol | Conditionnement myéloablatif (MAC) vs RIC avant TCSH pour LAM/SMD : arbitrage mortalité liée traitement vs rechute — **busulfan** au cœur des deux bras |
| [37579918](https://pubmed.ncbi.nlm.nih.gov/37579918/) | 2023 | Cohorte prospective | Transplant Cell Ther | Dose myéloablative **busulfan+fludarabine** + déplétion T in vivo : sûre et efficace pour LAM et SMD, y compris patients avec score HCT-CI élevé |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Analyse de registre | Bone Marrow Transplant | **Fludarabine/busulfan** (Flu/Bu4) vs busulfan/cyclophosphamide (Bu4/Cy) en conditionnement myéloablatif pour SMD — analyse par score de propension sur registre national japonais |
| [35296446](https://pubmed.ncbi.nlm.nih.gov/35296446/) | 2022 | Analyse de registre | Transplant Cell Ther | MAC (**Flu/Bu4**) vs RIC (**Flu/Bu2**) pour SMD avant TCSH allogénique — analyse comparative par score de propension sur données nationales |
| [38648898](https://pubmed.ncbi.nlm.nih.gov/38648898/) | 2024 | Cohorte rétrospective | Transplant Cell Ther | Tréosulfan vs **busulfan** dans TCSH allogénique pour SMD : étude monocentrique avec score de propension (n=138, Princess Margaret Hospital) |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Revue contemporaine | Am J Hematol | TCSH allogénique pour myélofibrose et syndromes myélodysplasiques : revue 2025 incluant le rôle du **busulfan** dans le choix du régime de conditionnement |

---

## Cytotoxicité

| Élément | Contenu |
|---------|---------|
| Classification de Cytotoxicité | Cytotoxique conventionnel — agent alkylant bisfonctionnel (classe des sulfonates d'alkyls / busulfan) |
| Risque de Myélosuppression | **Élevé** — aplasie médullaire complète intentionnelle et attendue dans le cadre du conditionnement TCSH ; neutropénie et thrombocytopénie sévères systématiques |
| Classification d'Émétogénicité | **Modérée à élevée** — prophylaxie antiémétique systématique recommandée lors de l'administration |
| Éléments de Surveillance | NFS avec différentielle quotidienne pendant l'aplasie ; surveillance pharmacocinétique (PK-guided dosing) pour la forme IV ; bilan hépatique complet (ASAT, ALAT, bilirubine — risque de maladie veino-occlusive hépatique/VOD-SOS) ; créatinine et électrolytes ; EEG ou prophylaxie antiépileptique (risque convulsions à dose élevée) |
| Protection de Manipulation | Manipulation obligatoirement conforme aux réglementations sur les médicaments cytotoxiques : préparation sous hotte à flux laminaire en pharmacie hospitalière, équipement de protection individuelle (gants, blouse, masque), traçabilité des déchets cytotoxiques |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
L'utilisation de busulfan comme composant central du régime de conditionnement avant TCSH allogénique pour le syndrome myélodysplasique est soutenue par un essai pivotal de Phase 3 (MC-FludT.14/L, Lancet Haematology 2020, n=476), une méta-analyse et de multiples essais de Phase 2 — le niveau de preuve L1 est atteint, et cette indication est cliniquement établie dans les centres spécialisés en greffe.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les données détaillées sur le mécanisme d'action (MOA) via DrugBank (DG002 — sévérité : élevée)
- Récupérer la notice et les mises en garde réglementaires complètes (ANSM/EMA — DG001 — sévérité : bloquante) : avertissements VOD/SOS, interactions avec itraconazole et phénytoïne, précautions en insuffisance hépatique
- Vérifier le statut réglementaire précis en France auprès de l'EMA/ANSM (busulfan dispose d'une AMM européenne sous forme injectable — Busilvex® — non reflétée dans les données du dossier)
- Définir le protocole de surveillance pharmacocinétique (PK-guided dosing) pour optimiser l'aire sous la courbe (AUC cible) et minimiser le risque de VOD hépatique
- Préciser le sous-type de SMD (score IPSS-R, profil cytogénétique et moléculaire) pour adapter l'intensité du conditionnement (MAC vs RIC)
- Évaluer le rapport bénéfice/risque individuel selon l'âge, les comorbidités (score HCT-CI) et la disponibilité d'un donneur compatible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

