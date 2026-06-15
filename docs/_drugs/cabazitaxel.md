---
layout: default
title: Cabazitaxel
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 10
---

# Cabazitaxel
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

En utilisant le skill `txgnn-pipeline` pour cadrer le travail, et en suivant le format de rapport v5 défini dans le système, voici le rapport généré :

---

# Cabazitaxel : Du Cancer de la Prostate Métastatique au Carcinome du Sein Féminin

## Résumé en Une Phrase

Cabazitaxel (Jevtana®) est un taxane de deuxième génération approuvé par la FDA pour le cancer de la prostate métastatique résistant à la castration (mCRPC) réfractaire au docétaxel, mais non enregistré à Taïwan.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Carcinome du Sein Féminin**,
avec **2 études cliniques publiées** (dont une Phase 2 randomisée) et **20 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer de la prostate métastatique résistant à la castration réfractaire au docétaxel (approbation FDA, non enregistré à Taïwan) |
| Nouvelle Indication Prédite | Carcinome du Sein Féminin |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L2 |
| Statut de Marché à Taïwan | Non enregistré |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action de cabazitaxel ne sont pas disponibles dans la base de données locale. Sur la base des informations publiées, cabazitaxel est un dérivé semi-synthétique de la famille des taxanes, agissant comme **agent stabilisateur de microtubules** : il inhibe la dépolymérisation des microtubules, bloque la mitose et induit l'apoptose des cellules tumorales à prolifération rapide. Sa caractéristique pharmacologique clé est sa **faible affinité pour la P-glycoprotéine (P-gp)**, principal mécanisme d'efflux de la résistance multi-médicamenteuse, lui permettant d'être actif dans des tumeurs résistantes au paclitaxel et au docétaxel.

Le cancer de la prostate et le carcinome du sein partagent une dépendance fondamentale à la dynamique des microtubules pour la division cellulaire — c'est la base biologique du réemploi de cabazitaxel dans le cancer du sein. Des études de résistance (PMID 25416788) ont développé des modèles spécifiquement à partir de cellules MCF-7 (sein), confirmant une activité antitumorale directe avec une résistance croisée bien moindre que celle observée avec paclitaxel ou docétaxel (15× vs. 200× dans MES-SA/Dx5). Ce profil est particulièrement pertinent pour les patientes atteintes de cancer du sein résistant aux taxanes classiques.

Au-delà de l'effet cytotoxique pur, des données précliniques récentes (PMID 33753567) montrent que cabazitaxel peut « rééduquer » les macrophages associés aux tumeurs et potentialiser les thérapies immunologiques anti-CD47 dans le cancer du sein triple-négatif (TNBC), élargissant son potentiel thérapeutique à une dimension immunologique. L'étude GENEVIEVE (PMID 28768217), un ECR de Phase 2 randomisé, et une étude de Phase 1/2 multicentrique (PMID 21339064) apportent les premières preuves cliniques directes de l'activité de cabazitaxel dans le cancer du sein, consolidant la pertinence de la prédiction TxGNN.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement sur ClinicalTrials.gov ou ICTRP pour la combinaison cabazitaxel / carcinome du sein féminin lors de la requête du 20 avril 2026. Des études cliniques pertinentes ont été identifiées dans la littérature publiée (voir section suivante).

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | ECR Phase 2 | Eur J Cancer | Étude GENEVIEVE : cabazitaxel vs paclitaxel hebdomadaire en néoadjuvant chez des patientes atteintes de cancer du sein HER2-négatif opérable (TNBC ou luminal B) ; évaluation du taux de réponse pathologique complète |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Phase 1/2 multicentrique | Eur J Cancer | Cabazitaxel + capécitabine en escalade de doses dans le cancer du sein métastatique réfractaire aux anthracyclines et taxanes ; évaluation de la DMT, sécurité, PK et activité |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | Préclinique / Mécanistique | J Immunother Cancer | Cabazitaxel améliore l'immunothérapie anti-CD47 dans le TNBC via la rééducation des macrophages tumoraux et stimulation de la phagocytose (PrCR) |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Revue (mécanismes de résistance) | Mol Cancer Ther | Mécanismes de résistance à cabazitaxel dans des modèles MCF-7 (sein) ; résistance croisée nettement moindre que paclitaxel/docétaxel, expliquant l'intérêt dans les tumeurs résistantes |
| [33247980](https://pubmed.ncbi.nlm.nih.gov/33247980/) | 2021 | Revue | Br J Clin Pharmacol | Ajustements de doses basés sur le TDM pour taxanes (cabazitaxel inclus) dans les tumeurs solides avancées ; pharmacocinétique et relations PK-PD |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | Préclinique (PDX) | J Control Release | Nanoparticules de cyanoacrylate chargées en cabazitaxel : 6/8 rémissions complètes dans un modèle PDX de cancer du sein basal-like, efficacité supérieure au médicament libre |
| [36918084](https://pubmed.ncbi.nlm.nih.gov/36918084/) | 2023 | Préclinique | J Control Release | Nanomédicament redox-responsive (CS-DTM-CTX) co-assemblé avec dasatinib : inhibition de la croissance tumorale mammaire en modulant le dialogue CAF-tumeur |
| [33360926](https://pubmed.ncbi.nlm.nih.gov/33360926/) | 2021 | Préclinique | Colloids Surf B | NLC (Nanostructured Lipid Carriers) chargés en cabazitaxel, optimisés par DoE ; caractérisation physico-chimique et évaluation contre lignées de cancer du sein |
| [30521787](https://pubmed.ncbi.nlm.nih.gov/30521787/) | 2019 | Préclinique | Chem Phys Lipids | Liposphères co-chargées cabazitaxel + thymoquinone : activité synergique sur tumeurs mammaires via p53, Bax, BCL-2, STAT3 et NF-κB |
| [34309357](https://pubmed.ncbi.nlm.nih.gov/34309357/) | 2021 | Préclinique | Bioconjug Chem | Conjugué CBT-cCPP ciblant l'intégrine et EDB-Fn : délivrance intracellulaire ciblée de cabazitaxel dans le cancer du sein et de la prostate via biomarqueurs de la matrice extracellulaire |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (classe Taxane — agent stabilisateur de microtubules ; semi-synthèse à partir de 10-désacétylbaccatine III) |
| Risque de Myélosuppression | **Élevé** — la neutropénie sévère (Grade 3/4) constitue la toxicité dose-limitante principale documentée dans les études de Phase 1/2 (PMID 21339064) ; risque de neutropénie fébrile à surveiller impérativement |
| Classification d'Émétogénicité | Faible à modérée (profil similaire aux autres taxanes selon les revues de classe, PMID 33247980) |
| Éléments de Surveillance | NFS avec formule leucocytaire (avant chaque cycle), fonction hépatique et rénale, neuropathie périphérique, diarrhée, hypersensibilité |
| Protection de Manipulation | Manipulation obligatoire selon les réglementations des médicaments cytotoxiques : tenue de protection complète, préparation en isolateur ou hotte à flux laminaire, gestion des déchets cytotoxiques |

---

## Considérations de Sécurité

> Les données sur les mises en garde, contre-indications et interactions médicamenteuses ne sont pas disponibles dans la base de données locale pour ce médicament. Veuillez consulter la notice officielle (FDA Prescribing Information Jevtana® / SmPC EMA) pour les informations de sécurité complètes, notamment concernant la neutropénie fébrile, la neuropathie périphérique, les contre-indications en cas d'insuffisance hépatique sévère et les précautions d'emploi avec les inducteurs/inhibiteurs puissants du CYP3A4.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Une étude de Phase 2 randomisée (GENEVIEVE) et une étude de Phase 1/2 multicentrique fournissent des preuves cliniques initiales de l'activité de cabazitaxel dans le cancer du sein, soutenues par de nombreuses données précliniques concordantes et une rationalité mécanistique solide (stabilisation des microtubules, contournement de la résistance P-gp, rééducation immunitaire des macrophages tumoraux). Le niveau de preuve L2 justifie d'avancer avec des garde-fous adaptés.

**Pour avancer, les éléments suivants sont nécessaires :**
- Compléter les données de mécanisme d'action (MOA) via l'API DrugBank (DG002)
- Obtenir la fiche de sécurité complète (mises en garde TFDA / SmPC EMA Jevtana®) pour lever le blocage DG001
- Élargir la requête ClinicalTrials.gov avec des termes génériques (« cabazitaxel breast cancer ») pour identifier d'éventuels essais enregistrés non capturés par la requête initiale
- Évaluer la faisabilité réglementaire d'un développement en cancer du sein à Taïwan (statut Non enregistré → voie d'accès accéléré possible)
- Définir une population cible prioritaire (TNBC réfractaire, luminal B résistant aux taxanes classiques) pour un éventuel design d'étude de Phase 2
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

