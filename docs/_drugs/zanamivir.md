---
layout: default
title: Zanamivir
parent: Prédiction du modèle uniquement (L5)
nav_order: 826
evidence_level: L5
indication_count: 2
---

# Zanamivir
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Zanamivir : De la grippe à la pyélonéphrite

## Résumé en Une Phrase

Zanamivir est un inhibiteur de la neuraminidase virale, initialement utilisé pour le traitement de la **grippe** (y compris les formes sévères).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **pyélonéphrite**, mais cette prédiction repose uniquement sur le calcul : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Grippe (indication issue du graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Pyélonéphrite |
| Score de Prédiction TxGNN | 99,84 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Retiré (AMM annulée uniquement) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le zanamivir est un inhibiteur de la neuraminidase du virus de la grippe, dont l'efficacité a été établie dans la grippe.

Le lien mécanistique avec la pyélonéphrite n'est **pas établi**. La pyélonéphrite est une infection rénale principalement bactérienne, due surtout à des bactéries uropathogènes comme *E. coli*. Ces bactéries possèdent leurs propres sialidases, mais elles ne sont pas une cible reconnue du zanamivir, qui n'a pas d'activité antibactérienne connue.

Le score très élevé du modèle (0,998) reflète probablement des artefacts du graphe de connaissances, par exemple des associations communes avec des termes liés aux infections, plutôt qu'une plausibilité biologique. Cette prédiction doit donc être considérée avec une grande prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la pyélonéphrite.

Pour information, la deuxième prédiction du modèle (trouble du métabolisme de la tyrosine, score 99,02 %) n'est soutenue que par trois publications sans rapport réel avec cette indication. Elles portent sur la virologie de la grippe : résistance à l'oseltamivir, test de résonance plasmonique de surface, mutation N294S de la neuraminidase. Elles semblent avoir été retrouvées par simple correspondance de termes. Cette prédiction reste également au niveau L5, avec la recommandation Hold.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64427189 | DECTOVA 10 mg/1 mL, solution pour perfusion (GlaxoSmithKline Trading Services, Irlande) | Solution pour perfusion | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations du graphe, et non le texte de la notice) : épilepsie, bronchopneumopathie chronique obstructive (BPCO, y compris les formes précoces sévères), maladie bronchique, délire.
- **Interactions médicamenteuses** (8 identifiées) :
  - Modérée : insuline humaine (inhalée, à action rapide).
  - Niveau non déterminé : clarithromycine, loratadine, montélukast, kétotifène, fexofénadine, ibuprofène, diclofénac.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui n'ont pas pu être compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai ni publication pertinente, et aucun mécanisme plausible reliant un inhibiteur de neuraminidase virale à une infection bactérienne.
- L'AMM française est annulée et les données de sécurité officielles sont absentes, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications).
- Obtenir les données sur le mécanisme d'action (via DrugBank).
- Démontrer une activité *in vitro* ou préclinique du zanamivir contre les uropathogènes ou dans un modèle de pyélonéphrite.
- Vérifier la compatibilité de la voie d'administration (perfusion uniquement) avec le contexte clinique visé.
- Réévaluer la pertinence de la prédiction au regard d'éventuels artefacts du graphe de connaissances.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

