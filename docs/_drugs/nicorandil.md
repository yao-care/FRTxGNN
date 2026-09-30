---
layout: default
title: Nicorandil
parent: Preuves modérées (L3-L4)
nav_order: 213
evidence_level: L4
indication_count: 7
---

# Nicorandil
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **7** 
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

# Nicorandil : De l'Indication d'Origine (non renseignée) à l'Hyperplasie Bénigne de la Prostate

## Résumé en Une Phrase

Nicorandil est un vasodilatateur, ouvreur des canaux K-ATP et donneur de nitrate, commercialisé en France. Les données ANSM fournies ne précisent pas son indication d'origine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Hyperplasie Bénigne de la Prostate (HBP)**,
mais cette piste ne repose que sur **0 essai clinique** et **3 publications** (1 étude préclinique chez l'animal et 2 revues narratives).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM fournies |
| Nouvelle Indication Prédite | Hyperplasie bénigne de la prostate |
| Score de Prédiction TxGNN | 99,71 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 14 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base. Sur la base des informations connues, le nicorandil est un ouvreur des canaux potassiques ATP-dépendants (K-ATP) et un donneur de nitrate. Ces deux propriétés provoquent une vasodilatation.

Plusieurs auteurs proposent qu'une baisse du débit sanguin prostatique, voire une ischémie de la prostate, contribue à l'HBP et aux symptômes du bas appareil urinaire. Des données cliniques associent l'HBP à des maladies athéroscléreuses comme l'hypertension. Un vasodilatateur pourrait donc, en théorie, corriger ce déficit de perfusion.

Le soutien expérimental reste limité. Une étude chez le rat spontanément hypertendu (SHR) a montré qu'une ischémie prostatique induit une hyperplasie de la prostate ventrale, et le rat a été traité par nicorandil pendant six semaines. Le score TxGNN élevé est cohérent avec cette hypothèse, mais il ne constitue pas une preuve clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [24448152](https://pubmed.ncbi.nlm.nih.gov/24448152/) | 2014 | Étude préclinique chez l'animal | Scientific Reports | Chez le rat SHR, l'ischémie prostatique induit une hyperplasie prostatique ventrale. Le nicorandil a été administré pendant 6 semaines, avec mesure de la pression artérielle, du flux sanguin prostatique et de marqueurs de stress oxydatif. |
| [31735753](https://pubmed.ncbi.nlm.nih.gov/31735753/) | 2019 | Revue | Nihon Yakurigaku Zasshi | Le flux sanguin prostatique est présenté comme une cible de l'HBP. Une altération de l'apport sanguin du bas appareil urinaire favoriserait son développement, avec un lien avec les maladies athéroscléreuses. |
| [26165338](https://pubmed.ncbi.nlm.nih.gov/26165338/) | 2015 | Revue | Nihon Yakurigaku Zasshi | Les symptômes du bas appareil urinaire sont abordés comme une dysfonction vasculaire, avec l'effet du nicorandil comme vasodilatateur (résumé non disponible). |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Fabricant |
|---------|------|------|-----------|
| 64614712 | NICORANDIL EG 10 mg, comprimé sécable | Comprimé sécable | DOUBLE-E PHARMA (Irlande) |
| 66925249 | NICORANDIL ALMUS 10 mg, comprimé sécable | Comprimé sécable | BIOGARAN |
| 61503831 | NICORANDIL ZENTIVA 10 mg, comprimé sécable | Comprimé sécable | ZENTIVA FRANCE |
| 61630825 | NICORANDIL SANDOZ 10 mg, comprimé sécable | Comprimé sécable | SANDOZ |
| 61536799 | NICORANDIL ZENTIVA 20 mg, comprimé | Comprimé | ZENTIVA FRANCE |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune mise en garde ni contre-indication n'a pu être extraite de la notice ANSM, et aucune interaction médicamenteuse n'a été trouvée dans la base.

À titre d'hypothèse issue de l'analyse (et non d'une donnée de la notice) : le principal point d'attention serait une hypotension additive chez l'homme âgé, en particulier en association avec des alpha-bloquants ou des inhibiteurs de la PDE5, fréquemment utilisés dans l'HBP. Ce risque doit être évalué avant tout travail clinique.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose sur un score de modèle élevé, une seule étude animale et deux revues narratives, sans aucun essai clinique. Les données de sécurité de la notice sont manquantes, ce qui bloque le passage à l'étape de criblage de sécurité. À ce stade, il s'agit d'une question de recherche et non d'une candidature prête à être développée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications, indications approuvées), élément bloquant
- Obtenir les données détaillées sur le mécanisme d'action via DrugBank
- Évaluer le risque d'hypotension chez l'homme âgé, notamment avec les alpha-bloquants et les inhibiteurs de la PDE5
- Rechercher des données cliniques ou des études observationnelles chez des patients atteints d'HBP traités par nicorandil
- Confirmer l'indication d'origine, absente des textes d'AMM fournis

Les autres indications prédites (alopécie, hypotrichose, alopécie areata, arthrose) n'ont ni essai ni publication associés (niveau L5). Elles restent en Hold.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

