---
layout: default
title: Everolimus
parent: Prédiction du modèle uniquement (L5)
nav_order: 311
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Everolimus : nouvelle indication prédite, Liposarcome (niveau de preuve L5). Indication d'origine : Carcinome rénal à cellules claires"
---

# Everolimus
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

# Évérolimus : Du Carcinome Rénal à Cellules Claires au Liposarcome

## Résumé en Une Phrase

L'évérolimus est un inhibiteur de mTOR, initialement utilisé pour le traitement du carcinome rénal à cellules claires, du cancer du sein, de l'angiomyolipome rénal et de la sclérose tubéreuse de Bourneville.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **liposarcome**,
avec **1 essai clinique** (phase II, en association) et **4 publications** (dont une seule directement liée à l'évérolimus) soutenant actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carcinome rénal à cellules claires (les textes d'indication des AMM ne sont pas renseignés ; l'indication provient du graphe de connaissances) |
| Nouvelle Indication Prédite | Liposarcome |
| Score de Prédiction TxGNN | 99,88 % |
| Niveau de Preuve | L2 (à interpréter avec prudence : phase II en association, à bras unique) |
| Statut de Marché en France | ✗ Toutes les AMM sont annulées |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, l'évérolimus est un inhibiteur de la voie mTOR (mTORC1). Son efficacité a été établie dans le carcinome rénal avancé et dans d'autres indications oncologiques (sein, angiomyolipome, sclérose tubéreuse).

Le liposarcome dédifférencié se caractérise par une amplification de MDM2/CDK4 et une activation fréquente de la voie PI3K/AKT/mTOR. Bloquer mTOR par l'évérolimus tout en inhibant CDK4/6 par le ribociclib constitue un double blocage rationnel du cycle cellulaire et de la signalisation de croissance et de survie.

Cette hypothèse reste toutefois à confirmer : le seul soutien clinique est un essai de phase II à bras unique, dont les résultats d'efficacité ne figurent pas dans les données fournies. La contribution propre de l'évérolimus ne peut pas être isolée de celle du ribociclib.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Actif, hors recrutement | 48 | Ribociclib + évérolimus dans le liposarcome dédifférencié avancé et le léiomyosarcome après au moins une ligne systémique ; objectif : évaluer l'activité antitumorale. Résultats non confirmés dans les données fournies. |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Essai clinique de phase II | Clin Cancer Res | Rapport de l'essai ribociclib + évérolimus dans le liposarcome dédifférencié et le léiomyosarcome ; synergie d'inhibition de croissance observée dans des modèles tumoraux |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Revue (préclinique) | Front Oncol | Modèles PDOX de sarcomes et combinaisons avec le palbociclib ; non spécifique à l'évérolimus |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | Préclinique | Oncogene | L'inhibiteur de XPO1 KPT-330 (sélinexor) compromet la viabilité des cellules de liposarcome dédifférencié ; non spécifique à l'évérolimus |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Préclinique | Anticancer Res | Activité de l'éribuline en association avec d'autres anticancéreux ; non spécifique à l'évérolimus |

## Informations de Marché en France

Les 20 AMM recensées sont toutes annulées, aucune n'est valide actuellement. Les textes d'indication approuvée ne sont pas renseignés. Principales AMM (5 sur 20) :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 64444441 | EVEROLIMUS SANDOZ 10 mg, comprimé | Comprimé | Annulée |
| 64201368 | AFINITOR 10 mg, comprimé | Comprimé | Annulée |
| 66520037 | VOTUBIA 10 mg, comprimé | Comprimé | Annulée |
| 60658711 | CERTICAN 0,5 mg, comprimé | Comprimé | Annulée |
| 64945242 | VOTUBIA 3 mg, comprimé dispersible | Comprimé dispersible | Annulée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de mTOR) |
| Risque de Myélosuppression | Moyen : les données de graphe de connaissances signalent des contre-indications liées à la thrombopénie, la neutropénie, l'agranulocytose, la leucopénie et l'anémie |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | NFS, fonction hépatique et rénale, glycémie, bilan lipidique |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, thrombopénie, hyperglycémie, diabète, acidocétose diabétique, neutropénie, agranulocytose, leucopénie, anémie, hypertriglycéridémie, hyperlipidémie, pneumopathie interstitielle, syndrome hémolytique et urémique, purpura thrombopénique, insuffisance cardiaque congestive, épanchement péricardique, stomatite, lymphome.
- **Interactions médicamenteuses** : 383 interactions recensées. Parmi les principales :
  - Majeures : amphotéricine B (y compris complexe lipidique), aprépitant, dexaméthasone, clarithromycine.
  - Modérées : antidiabétiques (metformine, acarbose, glimépiride, gliflozines, gliptines, albiglutide, dulaglutide), cimétidine, éliglustat, éluxadoline.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le seul soutien clinique est un essai de phase II à bras unique associant l'évérolimus au ribociclib, sans résultats d'efficacité confirmés, et la contribution de l'évérolimus ne peut être isolée.
- Les données de sécurité officielles sont manquantes (bloquant pour le criblage de sécurité), et toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Résultats publiés d'efficacité de l'essai NCT03114527 (taux de réponse, survie sans progression), idéalement avec une comparaison permettant d'isoler l'effet de l'évérolimus
- Mises en garde et contre-indications de la notice ANSM
- Données détaillées sur le mécanisme d'action (DrugBank)
- Clarification de la disponibilité commerciale en France, compte tenu de l'annulation de toutes les AMM
- Plan de surveillance de sécurité (hématologique, métabolique, hépatique, rénal, pulmonaire) et gestion des interactions, notamment avec les inhibiteurs du CYP3A4

**Autres indications prédites (à titre informatif) :** le rhabdomyosarcome (rang 7) présente un niveau L2, avec deux essais pédiatriques précoces en population mixte, sans efficacité spécifique démontrée. Le dermatofibrosarcome protubérant relève du niveau L4 (littérature préclinique non spécifique à l'évérolimus). Les autres prédictions (sous-types rares de liposarcome et de rhabdomyosarcome, carcinomes rénaux rares) relèvent du niveau L5, sans essai ni publication, et sont à maintenir en Hold.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

