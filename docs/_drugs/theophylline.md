---
layout: default
title: Theophylline
parent: Prédiction du modèle uniquement (L5)
nav_order: 751
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Theophylline : nouvelle indication prédite, Maladie thrombotique (niveau de preuve L5). Indication d'origine : Asthme, bronchite, emphysème pulmonaire"
monitor_inn: "theophylline"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
---

# Theophylline
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

# Théophylline : De l'asthme à la maladie thrombotique

## Résumé en Une Phrase

La théophylline est un bronchodilatateur de la famille des méthylxanthines, initialement utilisé pour le traitement de l'asthme, de la bronchite et de l'emphysème pulmonaire.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **maladie thrombotique**, mais **aucun essai clinique** ni aucune publication pertinente ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Asthme, bronchite, emphysème pulmonaire (selon le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Maladie thrombotique |
| Score de Prédiction TxGNN | 99,62 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 6 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances pharmacologiques générales, la théophylline est un inhibiteur non sélectif des phosphodiestérases (PDE) et un antagoniste des récepteurs de l'adénosine. Son efficacité dans l'asthme et les maladies bronchiques obstructives est établie.

Sur le plan théorique, l'inhibition des PDE augmente l'AMPc plaquettaire, ce qui pourrait réduire l'activation des plaquettes et donc le risque thrombotique. Toutefois, l'antagonisme de l'adénosine, qui possède lui-même un effet antiagrégant, pourrait contrebalancer cet effet.

La littérature recensée est dominée par des travaux sur des biomarqueurs plaquettaires ou des méthodes de dosage, la pharmacocinétique de la ticlopidine et un capteur électrochimique de théophylline. Aucun de ces documents ne démontre un effet antithrombotique de la théophylline. Le score élevé du modèle ne constitue donc pas une preuve : la plausibilité mécanistique reste faible et non confirmée.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est actuellement enregistré pour cette indication.

---

## Preuves de la Littérature

Aucune publication ne soutient directement cette indication. Le tableau ci-dessous présente les références les plus proches, à titre indicatif.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Revue | Clinical Pharmacokinetics | Pharmacocinétique de la ticlopidine, antiagrégant plaquettaire ; ne concerne pas la théophylline |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Revue | CRC Critical Reviews in Biochemistry | Rôle des prostaglandines et des plaquettes dans l'athérosclérose ; la prostacycline stimule l'adénylate cyclase plaquettaire |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Étude in vitro | General Pharmacology | Milrinone et adénosine inhibent la réponse plaquettaire humaine via l'AMPc ; ne concerne pas la théophylline |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | Cohorte | Rheumatology | Activation plaquettaire et neutrophile dans la maladie de Behçet ; sans lien avec la théophylline |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Méthode de dosage | British Journal of Haematology | Dosage radio-immunologique du facteur plaquettaire 4 ; la théophylline n'y sert que comme composant de l'anticoagulant de prélèvement |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Méthode analytique | Analytica Chimica Acta | Aptacapteur électrochimique pour doser la théophylline ; aucune donnée d'efficacité |

---

## Informations de Marché en France

Les six AMM recensées sont annulées. Le texte des indications approuvées n'est pas disponible dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 65265758 | DILATRANE 300 mg | Gélule à libération prolongée | Annulée |
| 68957644 | DILATRANE 50 mg | Gélule à libération prolongée | Annulée |
| 64447761 | DILATRANE 100 mg | Gélule à libération prolongée | Annulée |
| 63514285 | TEDRALAN 200 mg | Gélule à libération prolongée | Annulée |
| 61848891 | DILATRANE 1 POUR CENT | Sirop | Annulée |

Une sixième AMM (DILATRANE 200 mg, gélule à libération prolongée, n° 62481804) est également annulée. Titulaire de toutes les AMM : SERP.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : hypertension, insuffisance hépatique, épilepsie, troubles anxieux, porphyries, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, thrombopénie, hypothyroïdie, ulcère gastroduodénal, glaucome à angle ouvert, troubles psychotiques, diabète et acidocétose diabétique, hypertrophie bénigne de la prostate, neutropénie et agranulocytose. La thrombopénie, la neutropénie et l'agranulocytose sont particulièrement pertinentes si l'on envisageait un usage dans un contexte thrombotique ou antiagrégant.
- **Interactions médicamenteuses** : 371 interactions recensées. La plus notable est de niveau **majeur** avec le **bupropion**. Plusieurs interactions de niveau modéré concernent les antiacides et anti-H2 (famotidine, ranitidine, cimétidine), les inhibiteurs de la pompe à protons (oméprazole, rabéprazole), les corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), les macrolides (clarithromycine) et les cyclines (doxycycline, minocycline, tétracycline). L'éphédrine présente une interaction mineure.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Cette prédiction repose uniquement sur le score du modèle (niveau L5) : aucun essai clinique, et aucune publication ne soutient un effet antithrombotique de la théophylline. De plus, toutes les AMM françaises sont annulées et le profil de sécurité (index thérapeutique étroit, nombreuses interactions) est contraignant.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action et analyse du lien mécanistique avec l'agrégation plaquettaire, en tenant compte de l'antagonisme de l'adénosine
- Études précliniques (agrégation plaquettaire, modèles de thrombose) démontrant un effet antithrombotique
- Texte de la notice (mises en garde et contre-indications) à récupérer auprès de l'ANSM
- Clarification de la situation réglementaire, toutes les AMM étant annulées

---

## Note sur les autres indications prédites

Pour information, les autres prédictions du modèle se répartissent ainsi :

| Indication prédite | Score TxGNN | Niveau de preuve | Recommandation |
|------|------|------|------|
| Maladie obstructive pulmonaire | 99,48 % | L1 | Proceed with Guardrails (recoupe les indications d'origine ; il ne s'agit pas d'un véritable repositionnement) |
| Maladie trachéale | 99,49 % | L3 | Question de recherche |
| Maladie de la cavité nasale | 99,53 % | L4 | Hold |
| Laryngotrachéite | 99,51 % | L5 | Hold |
| Pharyngite | 99,46 % | L5 | Hold |
| Laryngopharyngite aiguë | 99,35 % | L5 | Hold |

Les données compilées indiquent que, pour la maladie obstructive pulmonaire, des essais de phase 3 existent (dont NCT01599871, essai de 52 semaines en double aveugle contre placebo de la théophylline en ajout dans la BPCO sévère). Leurs résultats ne sont toutefois pas fournis, et plusieurs essais sont de petite taille.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

