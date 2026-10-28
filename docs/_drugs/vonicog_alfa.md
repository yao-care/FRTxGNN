---
layout: default
title: Vonicog Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 820
evidence_level: L5
indication_count: 8
monitor_inn: "VONICOG ALFA"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "hemophilia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency"]
last_modified_at: 2026-10-23
description: "Vonicog Alfa : nouvelle indication prédite, Primary release disorder of platelets (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Vonicog Alfa
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

## Vonicog Alfa: Primary release disorder of platelets
{: .text-alpha }

## Résumé en Une Phrase

Vonicog alfa est un facteur von Willebrand recombinant, initialement utilisé pour traiter la maladie de von Willebrand (héréditaire ou acquise).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hémophilie** (3ᵉ prédiction du classement), mais **aucun essai clinique** et **aucune publication** ne porte directement sur l'hémophilie : seules 4 publications indirectes, centrées sur la maladie de von Willebrand, ont été retrouvées.

Remarque : la première prédiction du modèle est le « trouble primaire de la libération plaquettaire » (score le plus élevé), mais elle ne dispose d'aucune preuve. Ce rapport se concentre sur l'hémophilie, seule indication prédite assortie de publications, et résume les autres prédictions plus bas.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Primary release disorder of platelets |
| Score de Prédiction TxGNN | 0.9998 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

Le niveau L5 s'applique car aucune des publications retrouvées n'étudie directement l'hémophilie.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les informations connues, vonicog alfa est un facteur von Willebrand (VWF) recombinant. Le VWF favorise l'adhésion et l'agrégation des plaquettes sur les sites de lésion vasculaire, via la liaison à la GPIb et au collagène, et il transporte le facteur VIII.

Le lien avec l'hémophilie est indirect : le VWF stabilise le facteur VIII endogène et le protège de sa clairance, d'où un lien plausible avec l'hémophilie A. Cependant, le produit n'est pas conçu pour remplacer le facteur VIII et n'a pas de rôle établi dans l'hémophilie.

Le score élevé du modèle reflète probablement la proximité des deux maladies dans le réseau de l'hémostase plutôt qu'une véritable adéquation mécanistique. Cette prédiction relève donc de l'hypothèse de travail.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Les quatre publications suivantes concernent la maladie de von Willebrand ou l'hémostase en général. Elles sont **indirectes** et ne testent pas l'efficacité dans l'hémophilie. Les titres et résumés étant tronqués, leurs détails ne peuvent pas être vérifiés complètement.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35439298](https://pubmed.ncbi.nlm.nih.gov/35439298/) | 2022 | Essai clinique de phase 3 | Blood | Prophylaxie par VWF recombinant chez des adultes atteints de maladie de von Willebrand sévère, évaluant la réduction des saignements spontanés traités |
| [37332615](https://pubmed.ncbi.nlm.nih.gov/37332615/) | 2023 | Étude PK/PD comparative | Journal of Blood Medicine | Comparaison pharmacocinétique/pharmacodynamique du VWF recombinant et plasmatique dans la maladie de von Willebrand de type 3 |
| [31298165](https://pubmed.ncbi.nlm.nih.gov/31298165/) | 2019 | Revue narrative | Current Pharmaceutical Design | Panorama des agents hémostatiques nouveaux et renouvelés en contexte périopératoire |
| [37926687](https://pubmed.ncbi.nlm.nih.gov/37926687/) | 2024 | Étude de laboratoire / enquête | Haemophilia | Méthodes de dosage du VWF recombinant et plasmatique dans les laboratoires d'hémostase |

## Informations de Marché en France

Vonicog alfa est commercialisé en France (2 AMM, toutes deux valides, sans texte d'indication renseigné dans les données compilées).

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65346733 | VEYVONDI 650 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 69749137 | VEYVONDI 1 300 UI | Poudre et solvant pour solution injectable | Non renseignée |

## Autres Prédictions du Modèle

| Rang | Maladie prédite | Score TxGNN | Preuves | Appréciation |
|---|---|---|---|---|
| 1 | Trouble primaire de la libération plaquettaire | 0,9998 | Aucune | Défaut plaquettaire intrinsèque, non corrigé par le VWF exogène |
| 2 | Thrombasthénie de Glanzmann | 0,9998 | Aucune | Déficit du récepteur αIIbβ3, que le VWF ne peut pas remplacer |
| 4 | Syndrome de Scott | 0,9995 | Aucune | Défaut de scramblase plaquettaire, non corrigé par le VWF |
| 5 | Déficit acquis en facteur de coagulation | 0,9994 | Aucune | Catégorie large ; question de recherche à préciser par sous-type (par ex. maladie de von Willebrand acquise, hémophilie acquise) |
| 6 | Diathèse hémorragique par défaut de récepteur du collagène | 0,9992 | Aucune | Défaut au niveau du récepteur, peu probablement contourné par le VWF |
| 7 | Trouble hémorragique lié à une thrombopénie constitutionnelle | 0,9992 | Aucune | Le VWF n'agit ni sur le nombre ni sur la production des plaquettes |
| 8 | « Flood factor deficiency » | 0,9990 | Aucune | Terme ne correspondant à aucune entité clinique reconnue ; probable artefact d'ontologie à vérifier |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées, et les mises en garde et contre-indications de la notice n'ont pas pu être extraites.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour l'hémophilie repose uniquement sur le modèle : aucune étude retrouvée ne teste directement l'hémophilie, et le produit n'a pas de rôle établi dans cette maladie. Les autres prédictions n'ont ni preuve ni justification mécanistique solide.

**Pour avancer, les éléments suivants sont nécessaires :**
- Extraire les mises en garde et contre-indications de la notice ANSM (point bloquant pour l'évaluation de sécurité)
- Obtenir les données détaillées sur le mécanisme d'action depuis DrugBank
- Rechercher des études spécifiques à l'hémophilie (en particulier l'hémophilie A) et définir un sous-type précis pour les déficits acquis en facteur de coagulation
- Vérifier le terme « flood factor deficiency » dans l'ontologie source
- Confirmer le texte d'indication des deux AMM auprès de l'ANSM
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

