---
layout: default
title: Povidone
parent: Prédiction du modèle uniquement (L5)
nav_order: 245
evidence_level: L5
indication_count: 1
---

# Povidone
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Povidone : Des Collyres (Indication Non Renseignée) à l'Érythrodermie Ichtyosiforme Congénitale

## Résumé en Une Phrase

La povidone (PVP) est un polymère synthétique surtout employé comme excipient, liant et agent filmogène ou viscosifiant. En France, elle est présente dans des collyres (Nutrivisc, Dulcilarmes, Unifluid), mais aucune indication approuvée n'est renseignée dans les données.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**érythrodermie ichtyosiforme congénitale**, avec **0 essai clinique** et **0 publication** à l'appui : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM (produits sous forme de collyre) |
| Nouvelle Indication Prédite | Érythrodermie ichtyosiforme congénitale |
| Score de Prédiction TxGNN | 99,11 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 7 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. La povidone est un polymère synthétique utilisé comme excipient, liant, agent filmogène ou viscosifiant. Aucune indication d'origine n'est enregistrée pour cette substance dans le dossier.

L'érythrodermie ichtyosiforme congénitale est un trouble génétique de la kératinisation (par exemple variants de *TGM1*, *ALOX12B* ou *ALOXE3*), avec une barrière épidermique altérée et une desquamation. Un polymère topique pourrait avoir un effet hydratant ou filmogène non spécifique. Cet effet resterait au mieux symptomatique et ne traiterait pas la pathologie sous-jacente.

**Aucun lien mécanistique crédible ne peut être établi.** Le score élevé (0,991) reflète une simple proximité dans le graphe de connaissances, par exemple des nœuds liés à la peau ou aux excipients. Il peut aussi résulter d'une confusion avec la povidone iodée. Il ne repose sur aucune preuve clinique ou bibliographique.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69449741 | NUTRIVISC 5 POUR CENT, collyre en solution (Laboratoires Alcon) | Collyre en solution | Non renseignée |
| 68403812 | DULCILARMES 1,5 %, collyre en solution en récipient unidose (Horus Pharma) | Collyre en solution | Non renseignée |
| 64035359 | NUTRIVISC 5 POUR CENT (20 mg/0,4 ml), collyre en solution en récipient unidose (Laboratoires Alcon) | Collyre en solution | Non renseignée |
| 65367581 | UNIFLUID 6 mg/0,4 ml, collyre en solution en récipient unidose (Théa) | Collyre en solution | Non renseignée |
| 63734630 | DULCILARMES 1,5 %, collyre en solution (Horus Pharma) | Collyre en solution | Non renseignée |

Sur 7 AMM au total, 5 sont listées ici. Toutes les formes disponibles sont des collyres (voie ophtalmique). Aucune forme dermatologique n'est référencée, et la compatibilité de voie avec l'indication prédite reste à évaluer.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et aucun lien mécanistique crédible n'est établi.
- Les formes commercialisées sont exclusivement ophtalmiques et les données de sécurité sont absentes, ce qui empêche de poursuivre vers un examen de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser les notices ANSM (mises en garde et contre-indications) : lacune bloquante
- Obtenir les données de mécanisme d'action via DrugBank
- Vérifier que la prédiction ne provient pas d'une confusion avec la povidone iodée
- Réaliser une revue de la littérature sur les polymères filmogènes topiques dans les ichtyoses
- Évaluer la compatibilité de voie d'administration (forme dermatologique) avec l'indication prédite
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

