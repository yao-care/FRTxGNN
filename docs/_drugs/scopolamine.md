---
layout: default
title: Scopolamine
parent: Prédiction du modèle uniquement (L5)
nav_order: 278
evidence_level: L5
indication_count: 6
---

# Scopolamine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

# Scopolamine : De l'indication originale (non renseignée) au Syndrome de la Queue de Cheval

## Résumé en Une Phrase

La scopolamine est un antagoniste muscarinique commercialisé en France sous forme de dispositif transdermique (Scopoderm TTS). L'indication approuvée n'est pas renseignée dans les données ANSM disponibles.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome de la queue de cheval**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM |
| Nouvelle Indication Prédite | Syndrome de la queue de cheval |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les connaissances pharmacologiques générales, la scopolamine est un antagoniste muscarinique non sélectif. Elle réduit notamment la contractilité du détrusor (le muscle de la vessie).

Le lien avec le syndrome de la queue de cheval passe uniquement par les troubles vésicaux associés. Or cette pathologie provoque le plus souvent une rétention urinaire ou une vessie aréflexique. Un anticholinergique risque donc d'**aggraver la rétention** au lieu de la soulager. Le mécanisme est ainsi faible, voire potentiellement contre-productif.

Le score TxGNN très élevé (99,99 %) provient d'une prédiction fondée sur un graphe de connaissances. Il ne s'appuie sur aucune donnée clinique. Il doit donc être interprété avec beaucoup de prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63958849 | SCOPODERM TTS 1 mg/72 heures, dispositif transdermique (BAXTER) | Dispositif | Non renseignée |
| 68731823 | SCOPODERM TTS 1 mg/72 heures, dispositif transdermique (DIFARMED, Espagne) | Dispositif | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans la base interrogée.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication.
- Le mécanisme antimuscarinique pourrait aggraver la rétention urinaire typique de la pathologie.
- Les cinq autres indications prédites sont également au niveau L5 avec une décision Hold :
  - vessie neurogène (terme obsolète) ;
  - conjonctivite papillaire ;
  - conjonctivite atopique ;
  - conjonctivite de la rosacée ;
  - conjonctivite vernale.
- Leur plausibilité mécanistique est faible, sauf pour la vessie neurogène. Pour celle-ci, il existe déjà des antimuscariniques mieux caractérisés et moins délétères pour le système nerveux central.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications, indication approuvée). Ce point est bloquant pour tout criblage de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action via DrugBank.
- Rechercher activement des essais cliniques et des publications pour le syndrome de la queue de cheval.
- Vérifier la faisabilité de la voie d'administration (aujourd'hui uniquement transdermique).
- Faire correspondre le terme de maladie obsolète (vessie neurogène) à une entrée d'ontologie actuelle avant toute revue.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement nécessite une validation clinique.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

