---
layout: default
title: Etonogestrel
parent: Prédiction du modèle uniquement (L5)
nav_order: 307
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "etonogestrel"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "apocrine adenosis of breast", "blunt duct adenosis of breast", "benign mammary dysplasia"]
description: "Etonogestrel : nouvelle indication prédite, Aménorrhée (amenorrhea (disease)) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Etonogestrel
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

## Etonogestrel: Aménorrhée (amenorrhea (disease))
{: .text-alpha }

## Résumé en Une Phrase

L'étonogestrel est un progestatif de synthèse, présent dans un implant sous-cutané contraceptif (Nexplanon) et dans un système de diffusion vaginal (anneau contraceptif associé à l'éthinylestradiol).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**aménorrhée**, mais **aucun essai clinique** n'est enregistré et la seule publication retrouvée n'a aucun lien avec cette indication (protocole d'étude sur la COVID-19).
Cette prédiction repose donc uniquement sur le modèle, sans preuve réelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Aménorrhée (amenorrhea (disease)) |
| Score de Prédiction TxGNN | 0.9984 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 6 sur 6) |
| Nombre d'AMM | 6 (valides : 6) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'étonogestrel est un progestatif puissant qui freine l'ovulation et provoque une atrophie de l'endomètre. Ces effets expliquent que l'aménorrhée soit un phénomène bien connu chez les utilisatrices de l'implant.

Cependant, l'aménorrhée est ici un **effet attendu, ou une modification du profil de saignements, liée à la contraception**, et non une maladie à traiter. Le lien avec une véritable indication thérapeutique est donc faible. Dans les aménorrhées d'origine hypothalamique ou fonctionnelle, une suppression purement progestative ne constituerait pas un traitement de fond adapté.

La prédiction est biologiquement plausible, mais elle reflète probablement un effet pharmacologique connu plutôt qu'une opportunité de repositionnement.

Les autres indications prédites (maladie fibrokystique du sein : 0.9961, adénose apocrine : 0.9929, adénose à canaux dilatés : 0.9929, dysplasie mammaire bénigne : 0.9921) sont issues du modèle TxGNN (apprentissage profond). Ces scores peuvent refléter des similarités apprises par le modèle entre maladies apparentées, et non des preuves biologiques. Elles reposent sur l'hypothèse théorique d'un antagonisme progestatif de la prolifération épithéliale induite par les œstrogènes. Aucun essai ni publication n'a été retrouvé pour elles, et elles restent non validées.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | Protocole d'ECR (sans rapport) | Trials | Protocole d'étude sur BIO101 pour prévenir la détérioration respiratoire dans la pneumonie COVID-19. Sans lien avec l'étonogestrel ni l'aménorrhée ; non retenue comme preuve. |

## Informations de Marché en France

Le médicament est commercialisé : 6 AMM valides sur 6.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66845924 | NEXPLANON 68 mg, implant pour usage sous-cutané | Implant | Non renseignée |
| 63713522 | ÉTHINYLESTRADIOL/ÉTONOGESTREL BIOGARAN 15 µg/120 µg/24 heures | Système de diffusion vaginal | Non renseignée |
| 67294185 | ÉTHINYLESTRADIOL/ÉTONOGESTREL ZENTIVA 15 µg/120 µg/24 heures | Système de diffusion vaginal | Non renseignée |
| 62148867 | NUVARING 15 µg/120 µg/24 heures | Système de diffusion vaginal | Non renseignée |
| 69356486 | ETORING 15 µg/120 µg/24 heures | Système de diffusion vaginal | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (non issues de la notice)** : hypertension, épilepsie, troubles anxieux, porphyries, maladies rénales, maladies hépatiques et de la vésicule biliaire, lupus érythémateux systémique, asthme, diabète (dont acidocétose), hypertriglycéridémie et hyperlipidémies, carcinome mammaire féminin, thrombophlébite, migraine, maladie coronarienne, obésité. Ces éléments sont indicatifs et doivent être confirmés par la notice officielle.
- **Interactions Médicamenteuses** : 117 interactions recensées. Parmi les principales, toutes de niveau modéré : antidiabétiques (acarbose, metformine, glimépiride, chlorpropamide, inhibiteurs de SGLT2 comme canagliflozine, dapagliflozine et empagliflozine, inhibiteurs de la DPP-4 comme alogliptine et saxagliptine, agonistes du GLP-1 comme sémaglutide, dulaglutide et albiglutide, insulines), ainsi qu'aprépitant, clarithromycine et linaclotide.

Les mises en garde et contre-indications de la notice n'ont pas pu être obtenues. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai clinique ni publication pertinente. L'aménorrhée est un effet attendu de la contraception progestative plutôt qu'une maladie à traiter.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications), ce qui bloque actuellement l'évaluation de sécurité
- Obtenir les données sur le mécanisme d'action depuis DrugBank
- Préciser si l'aménorrhée visée est une indication thérapeutique réelle (par exemple une aménorrhée pathologique) ou un simple effet de la contraception
- Vérifier les indications d'origine et le statut réglementaire actuel des produits (6 AMM valides sur 6)
- Rechercher des études spécifiques à l'étonogestrel dans l'aménorrhée et les pathologies bénignes du sein
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

