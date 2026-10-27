---
layout: default
title: Sulfamethoxazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 720
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Sulfamethoxazole : nouvelle indication prédite, Conjonctivite aiguë contagieuse (niveau de preuve L5). Indication d'origine : Non précisée dans les données d'AMM"
monitor_inn: "sulfamethoxazole"
predicted_indications: ["acute contagious conjunctivitis"]
---

# Sulfamethoxazole
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Sulfaméthoxazole : Des infections bactériennes à la conjonctivite aiguë contagieuse
{: .text-alpha }

## Résumé en Une Phrase

Le sulfaméthoxazole est un antibiotique de la famille des sulfamides, initialement utilisé pour traiter diverses infections (otite moyenne infectieuse, nocardiose, toxoplasmose, pneumocystose, shigellose, conjonctivite, maladie des griffes du chat, entre autres).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **conjonctivite aiguë contagieuse**. Cette indication figure toutefois déjà parmi ses indications d'origine : il ne s'agit donc pas d'un véritable repositionnement.
Les preuves actuelles se limitent à **1 publication** (étude de cohorte) et **aucun essai clinique**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données d'AMM ; les indications d'origine proviennent du graphe de connaissances (otite moyenne infectieuse, nocardiose, toxoplasmose, pneumocystose, shigellose, conjonctivite, etc.) |
| Nouvelle Indication Prédite | Conjonctivite aiguë contagieuse |
| Score de Prédiction TxGNN | 99,63 % |
| Niveau de Preuve | L4 (niveau attribué dans les données compilées ; une seule étude de cohorte observationnelle, aucun essai clinique) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 6 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances pharmacologiques générales, le sulfaméthoxazole inhibe la dihydroptéroate synthase bactérienne et bloque ainsi la synthèse des folates, ce qui freine la croissance des bactéries. Cette inférence ne provient pas des données fournies.

Ce mécanisme antibactérien est cohérent avec une conjonctivite d'origine bactérienne. Cependant, la conjonctivite figure déjà parmi les indications d'origine du médicament dans le graphe de connaissances. Le score élevé du modèle (99,63 %) reflète probablement cette association existante plutôt qu'une découverte nouvelle, et il reste une simple prédiction.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31788487](https://pubmed.ncbi.nlm.nih.gov/31788487/) | 2019 | Cohorte (rétrospective) | Medical Hypothesis, Discovery & Innovation Ophthalmology Journal | Analyse de la bactériologie et de la sensibilité aux antibiotiques dans les conjonctivites bactériennes aiguës de l'enfant, dans l'ouest de la Grèce (hôpital pédiatrique de Patras, 2013 et après) |

Cette étude décrit les profils de sensibilité aux antibiotiques ; le résumé disponible ne permet pas de confirmer qu'elle évalue directement le sulfaméthoxazole.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69464049 | BACTRIM 40 mg/mL + 8 mg/mL, suspension buvable | Suspension buvable | Non renseignée |
| 67891013 | COTRIMOXAZOLE TEVA 800 mg/160 mg, comprimé | Comprimé | Non renseignée |
| 69233327 | BACTRIM, solution injectable pour perfusion | Solution injectable pour perfusion | Non renseignée |
| 64121235 | BACTRIM FORTE, comprimé sécable | Comprimé sécable | Non renseignée |
| 65880598 | BACTRIM, suspension buvable | Suspension buvable | Non renseignée |

Les 6 AMM sont annulées ; aucune n'est actuellement valide. Seules 5 sont listées ci-dessus (limite du format).

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie, et non texte de la notice) : porphyries (héréditaire et autres troubles du métabolisme des porphyrines), maladie rénale, insuffisance rénale, urémie, glomérulonéphrite, maladie hépatique, maladie de la vésicule biliaire, thrombopénie, neutropénie, agranulocytose, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, déficit en G6PD, anémie par carence en acide folique, glycogénose, cystinurie, galactosémie.
- **Interactions médicamenteuses** : 151 interactions recensées. Parmi celles listées :
  - Niveau modéré : sulfamides hypoglycémiants (chlorpropamide, glimépiride, acétohexamide, glipizide, glibenclamide), insulines (humaine, asparte, dégludec, détémir, glargine, glulisine), balsalazide, acide picosulfurique.
  - Niveau mineur : famotidine, clarithromycine, dolasétron, palonosétron, cisapride, granisétron.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La conjonctivite figure déjà parmi les indications d'origine du médicament : il ne s'agit pas d'un vrai repositionnement. Les preuves se limitent à une étude de cohorte, sans essai clinique, et toutes les AMM françaises sont annulées. Les données de sécurité de la notice manquent, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications)
- Obtenir les données sur le mécanisme d'action via DrugBank
- Clarifier la pertinence d'une évaluation, compte tenu de l'indication déjà existante et du statut annulé des AMM
- Vérifier si la formulation (notamment ophtalmique) est compatible avec l'indication, aucune donnée de voie d'administration n'étant disponible
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

