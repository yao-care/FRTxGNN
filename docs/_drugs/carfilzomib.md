---
layout: default
title: Carfilzomib
parent: 僅模型預測 (L5)
nav_order: 70
evidence_level: L5
indication_count: 5
---

# Carfilzomib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Carfilzomib : Du Myélome Multiple au Mélanome

## Résumé en Une Phrase

Carfilzomib est un inhibiteur irréversible du protéasome 20S, reconnu internationalement pour le traitement du myélome multiple en rechute ou réfractaire. Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Mélanome** et plusieurs de ses sous-types, avec **5 publications scientifiques précliniques** soutenant actuellement cette direction de recherche. Le médicament n'est pas commercialisé dans la région concernée et les données de sécurité complètes restent à collecter.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Myélome Multiple (indication internationale établie) |
| Nouvelle Indication Prédite | Mélanome |
| Score de Prédiction TxGNN | 99.03% |
| Niveau de Preuve | L4 |
| Statut de Marché | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action de Carfilzomib ne sont pas disponibles dans le pack de données actuel. Sur la base des informations publiées, Carfilzomib appartient à la classe des inhibiteurs de protéasome (epoxyketones), dont l'efficacité dans le myélome multiple a été établie cliniquement. Son action cible de manière irréversible les sous-unités β5 (CT-L) et β5i du protéasome 20S.

Le système ubiquitine-protéasome (UPS) joue un rôle central dans la survie, la prolifération et la résistance à l'apoptose des cellules de mélanome. L'inhibition de ce système peut : (1) déclencher la réponse aux protéines mal repliées (UPR) conduisant à un stress du réticulum endoplasmique et à l'apoptose ; (2) perturber la dégradation de NF-κB et réduire les signaux pro-survie ; (3) interférer avec les voies de régulation de la survie cellulaire via le gène ZNFAN1-2a (PMID 31540997). La preuve la plus directe provient d'une étude in vitro (PMID 33671902) démontrant une synergie de Carfilzomib avec le Bortezomib pour induire l'apoptose dans les cellules B16-F1 de mélanome.

Le myélome multiple et le mélanome partagent une dépendance accrue au protéasome pour la gestion du stress protéotoxique. Cependant, les indications prédites au rang 1 à 4 présentent des obstacles significatifs : CMM7 est un locus de susceptibilité génétique (non traitable directement), le mélanome leptoméningé pédiatrique est limité par la faible pénétrance hémato-encéphalique de Carfilzomib (MW ~721 Da), et le mélanome uvéal présente un profil génomique distinct (mutations GNAQ/GNA11 vs BRAF/NRAS). Le **mélanome** (rang 5) constitue donc l'indication la plus cliniquement pertinente du spectre prédit.

### Panorama des Indications Prédites

| Rang | Indication | Score TxGNN | Niveau de Preuve | Remarque |
|------|-----------|-------------|-----------------|---------|
| 1 | CMM7 | 99.37% | L5 | Locus de susceptibilité génétique — non traitable directement |
| 2 | Mélanome leptoméningé pédiatrique | 99.30% | L5 | Obstacle PK majeur (barrière hémato-encéphalique) |
| 3 | Mélanome uvéal (cellules épithélioïdes) | 99.23% | L5 | Profil génomique distinct, lien mécanistique non établi |
| 4 | Mélanome vulvaire | 99.19% | L5 | Aucune preuve directe disponible |
| 5 | Mélanome | 99.03% | L4 | Indication avec le plus de preuves précliniques disponibles |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | In vitro préclinique | Biology | Carfilzomib + Bortezomib induisent une apoptose synergique dans les cellules B16-F1 de mélanome via activation des caspases 3, 8, 9 et 12 ; quantification par cytométrie de flux (Annexin V-FITC) |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | In silico | J Biomol Struct Dyn | Criblage virtuel par docking moléculaire et simulations de dynamique identifiant Carfilzomib parmi les candidats au repositionnement contre 18 cibles kinases validées dans 10 types de cancer dont le mélanome |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Biologie moléculaire | Mol Cancer Res | Le gène ZNFAN1-2a régule la survie des cellules de mélanome humain via l'E3-ligase cIAP2 ; voie directement liée au système ubiquitine-protéasome ciblé par Carfilzomib |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Mécanistique préclinique | Matrix Biol | Bortezomib et Carfilzomib activent la voie NF-κB pour induire l'expression de l'héparanase dans les cellules tumorales, favorisant potentiellement un phénotype tumoral agressif — implication pharmacologique à surveiller |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | Préclinique — chimie biologique | Leukemia | Molécules PROTAC ciblant BRD4 combinées à l'inhibition protéasomique : activité dans des modèles précliniques, illustrant la fécondité des approches combinatoires avec le protéasome comme cible |

---

## Informations de Marché

Aucune autorisation de mise sur le marché enregistrée dans la région concernée.

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée — Inhibiteur de protéasome (classe des epoxyketones) |
| Risque de Myélosuppression | Modéré à élevé (anémie, neutropénie et thrombocytopénie fréquentes dans l'indication myélome) |
| Classification d'Émétogénicité | Faible à modérée |
| Éléments de Surveillance | NFS complète avec différentielle ; bilan hépatique et rénal ; surveillance cardiaque (cardiotoxicité et hypertension artérielle sont des effets indésirables reconnus) ; fonction pulmonaire |
| Protection de Manipulation | Administration IV uniquement ; doit suivre les réglementations de manipulation des médicaments cytotoxiques |

---

## Considérations de Sécurité

Veuillez consulter la notice officielle (FDA / EMA) pour les informations de sécurité complètes, notamment les mises en garde relatives à la cardiotoxicité, à la toxicité pulmonaire et aux contre-indications.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Les preuves actuelles se limitent à des études précliniques in vitro et in silico (niveau L4), sans aucun essai clinique enregistré dans l'indication mélanome. Le lien mécanistique entre l'inhibition du protéasome et la survie des cellules de mélanome est biologiquement plausible, mais insuffisant pour justifier une progression clinique immédiate. Par ailleurs, l'absence d'AMM dans la région et les lacunes en données de sécurité imposent une consolidation préalable.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données MOA complètes via DrugBank API (DG002)
- Informations de sécurité : contre-indications et mises en garde complètes depuis la notice TFDA/FDA/EMA (DG001)
- Étude préclinique in vivo dans un modèle murin de mélanome (validation de l'efficacité avant Phase I)
- Évaluation des interactions potentielles avec les immunothérapies standards du mélanome (anti-PD-1, anti-CTLA-4)
- Analyse pharmacocinétique de la pénétrance tissulaire selon les sous-types de mélanome ciblés
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

