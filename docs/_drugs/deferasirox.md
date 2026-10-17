---
layout: default
title: Deferasirox
parent: Preuves modérées (L3-L4)
nav_order: 219
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Deferasirox : nouvelle indication prédite, Infection par le VIH (niveau de preuve L4). Indication d'origine : Bêta-thalassémie et hémoglobinopathies apparentées"
monitor_inn: "deferasirox"
predicted_indications: ["HIV infectious disease", "chronic hepatitis C virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "dermatofibrosarcoma protuberans"]
---

# Deferasirox
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **5** 
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

# Déférasirox : De la bêta-thalassémie au Virus de l'immunodéficience humaine (VIH)

## Résumé en Une Phrase

Le déférasirox est un chélateur du fer, initialement utilisé pour traiter la surcharge en fer associée aux hémoglobinopathies, notamment la bêta-thalassémie.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infection par le VIH**, mais cette prédiction repose sur **aucun essai clinique** et seulement **2 publications** (une revue générale et une étude préclinique).
Il s'agit donc d'une hypothèse très préliminaire.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Bêta-thalassémie et hémoglobinopathies apparentées (d'après le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Infection par le VIH |
| Score de Prédiction TxGNN | 99,40 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Toutes les AMM sont abrogées (aucune AMM valide) |
| Nombre d'AMM | 20 (dont 0 valide, 20 abrogées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le déférasirox est un chélateur du fer, utilisé pour réduire la surcharge en fer chez les patients atteints de bêta-thalassémie et d'hémoglobinopathies apparentées.

Le lien avec le VIH reste indirect. Une étude préclinique de 2021 (PMID 34550543) indique que le fer contenu dans les endolysosomes limite la transactivation du LTR du VIH-1 médiée par Tat, en favorisant l'oligomérisation de Tat et l'expression de la β-caténine. La disponibilité du fer influence donc la réplication virale. Toutefois, on ignore dans quel sens agirait une déplétion en fer : elle pourrait atténuer cet effet restrictif, et non le renforcer.

Ce lien est un lien de mécanisme uniquement. Il ne démontre pas qu'une chélation du fer serait bénéfique chez des patients infectés par le VIH.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [34550543](https://pubmed.ncbi.nlm.nih.gov/34550543/) | 2021 | Préclinique / in vitro | Journal of Neurovirology | Le fer endolysosomal limite la transactivation du LTR du VIH-1 par Tat, via une oligomérisation accrue de Tat et une expression accrue de la β-caténine |
| [16529348](https://pubmed.ncbi.nlm.nih.gov/16529348/) | 2006 | Revue | Journal of the American Pharmacists Association | Présentation générale de nouveaux médicaments dont le déférasirox ; aucune donnée spécifique sur le VIH |

---

## Informations de Marché en France

Les 20 AMM recensées sont abrogées. Les cinq premières sont listées ci-dessous ; le texte d'indication approuvée n'est pas disponible.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63539616 | Deferasirox Sandoz 360 mg | Comprimé pelliculé | Non renseignée |
| 63003134 | Deferasirox Teva 360 mg | Comprimé pelliculé | Non renseignée |
| 67963338 | Deferasirox Mylan 360 mg | Comprimé pelliculé | Non renseignée |
| 61736814 | Deferasirox Biogaran 180 mg | Comprimé pelliculé | Non renseignée |
| 66773987 | Deferasirox Sandoz 90 mg | Comprimé pelliculé | Non renseignée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : insuffisance hépatique, maladie hépatique, cirrhose, maladie rénale et insuffisance de la fonction rénale, thrombopénie, neutropénie (y compris formes congénitales), agranulocytose, anémie, hyperbilirubinémie (dont syndrome de Gilbert), maladie de la vésicule biliaire, ulcère gastroduodénal actif, hypertension oculaire, syndrome de défaillance multiviscérale et cancer.
- **Interactions médicamenteuses** : 518 interactions recensées. Parmi les principales, de niveau **majeur** : hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, acide acétylsalicylique, mésalazine, balsalazide et les formulations d'amphotéricine B. De niveau **modéré** : rabéprazole, pioglitazone, alosétron, aprépitant, clarithromycine, saxagliptine, hydroxyde d'aluminium, cisapride et dexfenfluramine.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles : veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur un score de modèle élevé, mais sans aucun essai clinique et avec une seule étude préclinique dont le sens de l'effet d'une chélation du fer est incertain. De plus, toutes les AMM françaises sont abrogées et le profil de sécurité (atteintes hépatiques, rénales, cytopénies) appelle une grande prudence.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action du déférasirox (DrugBank)
- Mises en garde et contre-indications officielles de la notice (site de l'ANSM), indispensables avant toute évaluation de sécurité
- Études précliniques supplémentaires déterminant si la chélation du fer favorise ou freine la réplication du VIH
- Clarification du statut réglementaire en France (AMM toutes abrogées)

**Remarque sur les autres prédictions :** les quatre autres indications prédites (hépatite C chronique, trouble neurodéveloppemental rare, hyperlipidémie familiale combinée obsolète, dermatofibrosarcome protubérant) ont un niveau de preuve L5 et une décision Hold. Elles ne disposent d'aucun essai clinique, et au plus d'une publication méthodologique indirecte (hépatite C).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

