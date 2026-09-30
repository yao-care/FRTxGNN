---
layout: default
title: Flubendazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 131
evidence_level: L5
indication_count: 10
---

# Flubendazole
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

# Flubendazole : De l'antihelminthique au carcinome de la vessie

## Résumé en Une Phrase

Le flubendazole est un antiparasitaire de la famille des benzimidazoles, commercialisé en France sous le nom Fluvermal pour traiter les vers intestinaux.
Le modèle TxGNN prédit qu'il pourrait être efficace contre le **carcinome de la vessie (urinary bladder carcinoma)**.
Cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **aucune publication** spécifique au flubendazole ne la soutiennent actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Antihelminthique (benzimidazole) ; le texte d'indication officiel n'est pas renseigné dans les données |
| Nouvelle Indication Prédite | Carcinome de la vessie (urinary bladder carcinoma) |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Le flubendazole appartient à la classe des benzimidazoles antihelminthiques. Ces molécules se lient généralement à la bêta-tubuline et perturbent les microtubules des parasites. Ce mécanisme pourrait s'appliquer aux cellules tumorales, dont la division dépend aussi des microtubules. C'est une piste plausible, mais **aucune donnée du dossier ne la confirme**.

Le lien entre l'indication d'origine (infections parasitaires) et le cancer de la vessie est donc uniquement hypothétique et fondé sur la classe pharmacologique. Une publication de 2024 (PMID 39128990) étudie une instillation intravésicale associant CRISPR-Cas13a et le **fenbendazole**, un benzimidazole apparenté, dans le cancer de la vessie. Elle porte sur une autre molécule et semble préclinique d'après son titre (résumé non examiné). Elle ne constitue qu'un indice indirect, au niveau de la classe.

Il faut aussi rester prudent sur le score. Les dix premières prédictions concernent toutes des termes « vessie », avec des scores quasi identiques (99,98 % à 99,99 %). Cela suggère un signal lié à la proximité de ces termes dans le graphe de connaissances plutôt qu'une preuve spécifique à une indication.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour cette indication précise.

Pour le terme voisin « urinary bladder neoplasm », seule l'étude préclinique sur le fenbendazole citée plus haut a été retrouvée. Elle ne concerne pas le flubendazole.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 68636624 | FLUVERMAL 2 POUR CENT | Suspension buvable | KENVUE FRANCE |
| 60968336 | FLUVERMAL | Comprimé | KENVUE FRANCE |

Ces deux formes sont orales. Aucune forme adaptée à l'instillation intravésicale n'existe actuellement dans les données.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (L5), sans essai clinique ni publication propre au flubendazole. Les données de sécurité et de mécanisme d'action sont absentes, ce qui empêche toute évaluation de sécurité à ce stade.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications) pour la revue de sécurité, ce qui est bloquant
- Compléter les données de mécanisme d'action via DrugBank
- Réaliser une vérification préclinique du flubendazole sur des lignées ou modèles de cancer de la vessie
- Évaluer la faisabilité d'une formulation et d'une voie d'administration intravésicale
- Surveiller l'apparition d'essais cliniques ou de publications spécifiques au flubendazole

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

