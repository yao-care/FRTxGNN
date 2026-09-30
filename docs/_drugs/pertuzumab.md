---
layout: default
title: Pertuzumab
parent: Preuves élevées (L1-L2)
nav_order: 235
evidence_level: L1
indication_count: 10
---

# Pertuzumab
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
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

# Pertuzumab : Du cancer du sein HER2-positif (indication supposée) au cancer du sein à récepteurs de la progestérone positifs

## Résumé en Une Phrase

Le pertuzumab est un anticorps monoclonal anti-HER2. Le texte de son indication en France n'est pas renseigné dans les données reçues. Il est très probablement utilisé pour le cancer du sein HER2-positif, mais cela reste à confirmer.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **cancer du sein à récepteurs de la progestérone positifs**, avec **10 essais cliniques** et **20 publications** associés. Ces études portent surtout sur des populations HER2-positives, non stratifiées selon le statut des récepteurs de la progestérone (RP).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Cancer du sein à récepteurs de la progestérone positifs |
| Score de Prédiction TxGNN | 99,93 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données DrugBank sur le mécanisme d'action ne sont pas renseignées. L'analyse de repositionnement du dossier fournit toutefois l'explication suivante. Le pertuzumab se fixe sur le sous-domaine II de l'extérieur de la cellule du récepteur HER2 et empêche sa dimérisation avec HER3. Il agit donc sur les tumeurs HER2-positives, quel que soit leur statut RP.

Le lien avec la nouvelle indication passe par le sous-groupe de tumeurs qui expriment à la fois HER2 et les récepteurs hormonaux (RP/RE). Dans ces tumeurs, le blocage de HER2 peut être combiné à un traitement endocrinien. Plusieurs études du dossier vont dans ce sens (NEOADAPT, WSG-TP-II, PERTAIN, ADEPT).

**Points de vigilance :**
- Le texte de l'indication originale est vide dans les données. Cette prédiction relève probablement déjà de l'usage autorisé dans le cancer du sein HER2-positif. Il faut le confirmer avec le résumé des caractéristiques du produit avant de la considérer comme un vrai repositionnement.
- Les essais de Phase 3 portent sur des populations HER2-positives et ne sont pas stratifiés selon le statut RP.

## Preuves d'Essais Cliniques

Sur les 10 essais retournés, 7 sont présentés ici. Les 3 exclus n'apportent pas d'information sur le pertuzumab :
- NCT06131424 : étude rétrospective sur la prévalence de HER2-low.
- NCT03058939 : essai retiré avec 0 patient inclus.
- NCT00999804 : essai sans bras pertuzumab visible.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Terminé | 517 | Biosimilaire QL1209 vs pertuzumab, avec trastuzumab et docétaxel, en néoadjuvant (cancer du sein HER2+ et RE/RP négatifs) |
| [NCT05802225](https://clinicaltrials.gov/study/NCT05802225) | Phase 3 | Actif, ne recrute plus | 398 | Biosimilaire BCD-178 vs Perjeta en néoadjuvant (HER2+, RE/RP négatifs) : démontre l'équivalence, pas une nouvelle indication |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Terminé | 454 | IMpassion050 : atezolizumab vs placebo ajouté à une chimiothérapie néoadjuvante avec trastuzumab et pertuzumab, cancer du sein HER2+ précoce |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Phase 2 | Terminé | 417 | Comparaison de 4 associations trastuzumab/docétaxel/pertuzumab sur la réponse pathologique complète (étude NeoSphere) |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | Actif, ne recrute plus | 164 | T-DM1 + pertuzumab en préopératoire : impact de l'hétérogénéité de HER2 |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | Arrêté | 139 | DECRESCENDO : désescalade de chimiothérapie avec pertuzumab-trastuzumab sous-cutané (HER2+, RE-négatif) ; lien indirect avec RP+ |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Phase 2 | Inconnu | 7 | NEOADAPT : inhibiteur de l'aromatase + pertuzumab/trastuzumab sans chimiothérapie (HR+/HER2+) ; le plus proche du contexte RP+, mais très petit effectif |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | ECR (Phase 2) | Lancet Oncol | NeoSphere : analyse à 5 ans de la survie sans progression et sans maladie sous pertuzumab + trastuzumab néoadjuvants |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | ECR (Phase 3) | Br J Cancer | Équivalence du biosimilaire QL1209 au pertuzumab de référence (HER2+, RE/RP négatifs) |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | ECR | JAMA Oncol | WSG-TP-II : hormonothérapie + double blocage HER2 vs chimiothérapie désescaladée dans le cancer du sein RH+/HER2+ |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | ECR (Phase 2) | Ann Oncol | WSG-ADAPT HER2+/HR- : 12 semaines de double blocage trastuzumab + pertuzumab, avec ou sans paclitaxel |
| [30106636](https://pubmed.ncbi.nlm.nih.gov/30106636/) | 2018 | ECR (Phase 2) | J Clin Oncol | PERTAIN : trastuzumab + inhibiteur de l'aromatase, avec ou sans pertuzumab, en première ligne (HER2+ et RH+) |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Recommandation | J Clin Oncol | Mise à jour des recommandations ASCO sur le traitement systémique du cancer du sein avancé HER2+ |
| [37609714](https://pubmed.ncbi.nlm.nih.gov/37609714/) | 2023 | Essai à un seul bras | Future Oncol | Protocole DECRESCENDO : désescalade de la chimiothérapie (HER2+, RH-négatif) |
| [40246081](https://pubmed.ncbi.nlm.nih.gov/40246081/) | 2025 | Étude rétrospective | Mod Pathol | Impact du statut des récepteurs hormonaux et de l'expression de HER2 sur la réponse au traitement ciblé néoadjuvant |
| [27057657](https://pubmed.ncbi.nlm.nih.gov/27057657/) | 2016 | Revue | Cancer Treat Rev | Cancer du sein RH+/HER2+ : état des connaissances et perspectives |
| [40983817](https://pubmed.ncbi.nlm.nih.gov/40983817/) | 2025 | Revue | Breast Cancer | Voies de signalisation et traduction clinique du cancer du sein HR+/HER2+ |

## Informations de Marché en France

Le texte de l'indication approuvée est vide pour les 3 AMM dans les données reçues. La colonne correspondante est donc omise.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 60912227 | PERJETA 420 mg | Solution à diluer pour perfusion | Roche Registration |
| 63806777 | PHESGO 600 mg/600 mg | Solution injectable | Roche Registration (Allemagne) |
| 67178992 | PHESGO 1200 mg/600 mg | Solution injectable | Roche Registration (Allemagne) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (anticorps monoclonal anti-HER2) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de Phase 3 terminés et des ECR de Phase 2 soutiennent le pertuzumab dans le cancer du sein HER2-positif. Des essais RH+/HER2+ (WSG-TP-II, PERTAIN, ADEPT) vont dans le sens de la prédiction. Il n'existe toutefois pas de preuve stratifiée selon le statut RP, et cette indication est probablement déjà couverte par l'AMM.
- Autres prédictions du dossier : « cancer du sein luminal A ou B » et « sous-type normal-like » sont au niveau L2 (question de recherche) ; « cancer du sein RP-négatif » est au niveau L1 (Proceed with Guardrails). Les 6 autres prédictions (tumeurs rares et urothéliales) sont au niveau L4-L5 (Hold).

**Pour avancer, les éléments suivants sont nécessaires :**
- Confirmer l'indication autorisée en France à partir du résumé des caractéristiques du produit de l'ANSM (texte d'indication vide dans les données).
- Obtenir la notice de l'ANSM (mises en garde et contre-indications). Cette lacune bloque l'étape de criblage de sécurité S1.
- Compléter le mécanisme d'action dans DrugBank.
- Rechercher des analyses en sous-groupes selon le statut RP dans les essais de Phase 3 (HER2+).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

