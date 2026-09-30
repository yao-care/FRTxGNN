---
layout: default
title: Mirtazapine
parent: Prédiction du modèle uniquement (L5)
nav_order: 198
evidence_level: L5
indication_count: 3
---

# Mirtazapine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

# Mirtazapine : De l'antidépresseur au Syndrome d'Ohdo et variantes

## Résumé en Une Phrase

La mirtazapine est un antidépresseur noradrénergique et sérotoninergique. L'indication originale n'est pas renseignée dans les données ANSM fournies.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **Syndrome d'Ohdo et variantes**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM (médicament de la classe des antidépresseurs) |
| Nouvelle Indication Prédite | Syndrome d'Ohdo et variantes |
| Score de Prédiction TxGNN | 99,42 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 15 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les informations pharmacologiques connues, la mirtazapine agit comme antagoniste alpha-2 adrénergique et antagoniste des récepteurs 5-HT2, 5-HT3 et H1. Son efficacité est établie dans la dépression, mais rien dans le dossier ne la relie à la nouvelle indication.

Le syndrome d'Ohdo (forme liée à KAT6B) est une maladie rare du développement. Elle est causée par un dysfonctionnement d'un régulateur de la chromatine (histone acétyltransférase). Il s'agit d'un défaut épigénétique et développemental, peu susceptible de répondre à une modulation monoaminergique au niveau des récepteurs. **Aucun lien mécanistique étayé n'a donc pu être identifié.** Le score élevé de TxGNN (0,994) provient uniquement de la prédiction sur graphe de connaissances, sans confirmation par une étude réelle.

Deux autres prédictions figurent dans le dossier, avec la même absence de preuves :
- **Blépharophimosis - déficience intellectuelle, type Ohdo** (score 99,11 %) : cette entité recoupe la première prédiction, les deux signaux ne sont donc probablement pas indépendants.
- **Torticolis paroxystique bénin du nourrisson** (score 99,11 %) : seule une justification spéculative existe, car cette affection est apparentée aux équivalents migraineux ou aux canalopathies (certains cas liés à CACNA1A). Elle disparaît spontanément dans la petite enfance, et aucune donnée sur l'usage ou la sécurité de la mirtazapine chez le nourrisson n'est fournie.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69084246 | MIRTAZAPINE ARROW GENERIQUES 15 mg | Comprimé pelliculé sécable | Non renseignée |
| 68022786 | MIRTAZAPINE TEVA 15 mg | Comprimé pelliculé | Non renseignée |
| 66402996 | MIRTAZAPINE BIOGARAN 15 mg | Comprimé orodispersible | Non renseignée |
| 62485126 | MIRTAZAPINE ARROW 15 mg | Comprimé orodispersible | Non renseignée |
| 62106380 | MIRTAZAPINE SANDOZ 15 mg | Comprimé pelliculé | Non renseignée |

Le dossier compte 15 AMM au total. Seules les 5 premières sont listées ici.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le niveau de preuve est L5 : la prédiction repose uniquement sur le modèle, sans essai clinique ni publication.
- Aucun lien mécanistique n'est étayé entre la pharmacologie de la mirtazapine et l'origine épigénétique du syndrome d'Ohdo.
- Les données de sécurité (mises en garde, contre-indications) manquent, ce qui bloque un premier examen de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde et contre-indications, données de sécurité bloquantes).
- Obtenir le mécanisme d'action détaillé depuis DrugBank.
- Renseigner l'indication originale approuvée dans les AMM.
- Rechercher des données précliniques ou de la littérature qui relieraient la mirtazapine aux voies de KAT6B ou aux phénotypes concernés.
- Évaluer la sécurité en population pédiatrique, en particulier chez le nourrisson pour le torticolis paroxystique bénin.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

