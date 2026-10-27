---
layout: default
title: Methionine
parent: Prédiction du modèle uniquement (L5)
nav_order: 485
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Methionine : nouvelle indication prédite, Acné (prédiction de rang 1) (niveau de preuve L5). Indication d'origine : Non renseignée (le texte d'indication des AMM est vide)"
monitor_inn: "methionine"
predicted_indications: ["acne (disease)", "severe nonproliferative diabetic retinopathy", "craniostenosis cataract", "mature cataract", "nuclear senile cataract", "cortical cataract", "tetanic cataract", "immature cataract", "diabetic cataract"]
---

# Methionine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

## Méthionine : D'une indication non documentée à la cataracte diabétique
{: .text-alpha }

## Résumé en Une Phrase

La méthionine est un acide aminé essentiel, présent dans de nombreuses solutions de nutrition parentérale commercialisées en France. L'indication d'origine n'est pas renseignée dans les données compilées pour ce rapport.
Le modèle TxGNN la prédit comme potentiellement utile pour **l'acné**, première prédiction du classement (score de 99,9996 %). Le **cataracte diabétique** est toutefois la piste disposant des éléments indirects les plus pertinents.
Aucun **essai clinique** n'est enregistré, et la littérature disponible est **indirecte** (6 publications pour la cataracte diabétique, 2 pour l'acné).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée (le texte d'indication des AMM est vide) |
| Nouvelle Indication Predite | Acné (prédiction de rang 1) ; piste la plus documentée : cataracte diabétique (rang 10) |
| Score de Prediction TxGNN | 99,9996 % (acné) ; 99,9990 % (cataracte diabétique) |
| Niveau de Preuve | L4 (acné et cataracte diabétique) ; L5 pour plusieurs autres indications |
| Statut de Marche en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Decision Recommandee | Hold (pour l'acné) ; question de recherche pour la cataracte diabétique |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la méthionine est un acide aminé soufré entrant dans la composition de solutions de nutrition parentérale (acides aminés seuls ou associés à des lipides et du glucose). Son rôle principal est nutritionnel, et elle intervient dans le cycle de la méthionine et de l'homocystéine.

**Acné.** Aucun lien mécanistique direct n'est établi. La littérature récupérée est indirecte : une étude montre une élévation de l'homocystéine plasmatique chez des patients traités par isotrétinoïne pour une acné kystique, et un cas rapporté concerne une mutation de la MTHFR sans rapport thérapeutique. Le lien reste spéculatif et repose sur une modification de l'homocystéine induite par un médicament, et non sur un effet thérapeutique de la méthionine.

**Cataracte diabétique.** C'est la piste dont les éléments indirects sont les plus pertinents : une revue sur l'homocystéine dans les maladies oculaires et des travaux précliniques sur la méthionine sulfoxyde réductase B1 (MsrB1) dans l'apoptose des cellules épithéliales du cristallin induite par un excès de glucose. Ils suggèrent un lien plausible entre la réparation redox de la méthionine et la protection du cristallin en situation d'hyperglycémie. Il s'agit toutefois du système de réparation de la méthionine sulfoxyde, et non d'une supplémentation en méthionine. Une élévation de l'homocystéine constitue en outre un risque potentiel. Cela justifie une question de recherche mécanistique, pas une recommandation clinique.

**Autres cataractes (nucléaire sénile, corticale, mature).** Les publications décrivent l'oxydation de la méthionine dans les protéines du cristallin, ce qui est un marqueur de lésion et non une preuve d'un bénéfice de la méthionine. La rétinopathie diabétique non proliférante sévère et plusieurs formes rares ou précoces de cataracte reposent uniquement sur la prédiction du modèle (L5).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Litterature

**Cataracte diabétique (rang 10)**

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [26343924](https://pubmed.ncbi.nlm.nih.gov/26343924/) | 2015 | Revue | Clin Chim Acta | L'hyperhomocystéinémie est un facteur de risque possible de maladies oculaires (rétinopathie, cataracte, glaucome, etc.) |
| [8680624](https://pubmed.ncbi.nlm.nih.gov/8680624/) | 1996 | Cohorte (épidémiologie nutritionnelle) | Ann Epidemiol | Étude cas-témoins en Italie du Nord sur l'alimentation et l'extraction de cataracte (207 cas, 706 témoins) ; lien seulement indirect |
| [39656472](https://pubmed.ncbi.nlm.nih.gov/39656472/) | 2024 | Préclinique (souris) | Invest Ophthalmol Vis Sci | Métabolomique du cristallin et de la rétine de souris diabétiques, rôle de la lipocaline-2 |
| [23270945](https://pubmed.ncbi.nlm.nih.gov/23270945/) | 2013 | Préclinique in vitro | Life Sci | Le silençage de MsrB1 influence l'apoptose des cellules du cristallin induite par un excès de glucose |
| [22713178](https://pubmed.ncbi.nlm.nih.gov/22713178/) | 2012 | Préclinique in vitro | Exp Eye Res | MsrB1 régule l'équilibre redox et limite l'apoptose induite par le peroxynitrite dans les cellules du cristallin |
| [40172029](https://pubmed.ncbi.nlm.nih.gov/40172029/) | 2025 | Étude animale | Int J Dev Biol | Conséquences hépatiques du retard de croissance intra-utérin chez le rat ; lien très indirect |

**Cataracte nucléaire sénile (rang 6)**

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [861252](https://pubmed.ncbi.nlm.nih.gov/861252/) | 1977 | Cas-témoins / biochimique | Biochim Biophys Acta | Oxydation progressive de la cystéine puis de la méthionine dans les protéines du cristallin lors de la cataracte nucléaire |
| [6705843](https://pubmed.ncbi.nlm.nih.gov/6705843/) | 1984 | Préclinique in vitro | Exp Eye Res | Le peroxyde d'hydrogène oxyde la cystéine et la méthionine (jusqu'à 45 %) dans les protéines du cristallin |
| [2515071](https://pubmed.ncbi.nlm.nih.gov/2515071/) | 1989 | Préclinique in vitro | Exp Eye Res | Réaction des protéines avec l'acide 3-hydroxyanthranilique comme modèle de cataracte nucléaire |

**Acné (rang 1)**

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Cohorte | Int J Dermatol | Élévation de l'homocystéine plasmatique chez les patients sous isotrétinoïne pour acné kystique |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Cas clinique | BMJ Case Rep | Mutation de la MTHFR chez un nouveau-né avec encéphalopathie, acné néonatale et chute de cheveux |

Aucune de ces publications ne teste la méthionine comme traitement.

## Informations de Marche en France

Toutes les AMM sont annulées ; aucune n'est actuellement valide. Le texte d'indication n'est pas renseigné dans les données.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61960303 | AMINOVEN 10 POUR CENT | Solution pour perfusion | Non renseignée (AMM annulée) |
| 69667989 | AMINOVEN 5 POUR CENT | Solution pour perfusion | Non renseignée (AMM annulée) |
| 62947013 | AMINOPLASMAL 25 | Solution pour perfusion | Non renseignée (AMM annulée) |
| 61786735 | AMINOMIX 500 | Solution pour perfusion | Non renseignée (AMM annulée) |
| 63183821 | AMINOPLASMAL 8 | Solution pour perfusion | Non renseignée (AMM annulée) |

*5 AMM sur 20 affichées.*

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie du graphe PrimeKG, et non du texte de la notice) : hypertension, maladie rénale (dont insuffisance rénale chronique et terminale), diabète et acidocétose diabétique, hypercalcémie, néphrocalcinose, lithiase rénale, néphropathie urique aiguë, maladie cardiaque et cardiovasculaire, hyperlipidémie (dont familiale), sarcoïdose, trouble du métabolisme du phosphore, intoxication digitalique, fibrillation ventriculaire, phénylcétonurie et troubles du métabolisme de la phénylalanine.
- **Interactions médicamenteuses** (5 identifiées) :
  - Modérée : charbon actif
  - Mineures : éphédrine, pseudoéphédrine, méxilétine, flécaïnide
- **Point d'attention** : une supplémentation en méthionine pourrait élever l'homocystéine, ce qui irait à l'encontre d'un bénéfice dans les maladies oculaires.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être exploitées ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- Aucune prédiction n'est soutenue par un essai clinique, et la littérature est indirecte. Le niveau de preuve est L4 pour l'acné et la cataracte diabétique, et L5 pour les autres indications. Le lien avec la méthionine repose sur le métabolisme de l'homocystéine ou le stress oxydatif, pas sur un effet thérapeutique démontré.
- Toutes les AMM françaises sont annulées, et les données de sécurité issues de la notice font défaut. La cataracte diabétique peut être retenue comme question de recherche mécanistique (réparation redox via MsrB1), pas comme recommandation clinique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), étape bloquante pour le criblage de sécurité
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Préciser l'indication d'origine de la méthionine
- Mener des études précliniques testant directement la méthionine (ou la voie MsrB1) dans des modèles de cataracte diabétique, avec suivi de l'homocystéine
- Évaluer la compatibilité des voies d'administration (actuellement uniquement des formes pour perfusion et dialyse péritonéale)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

