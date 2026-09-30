---
layout: default
title: Norgestimate
parent: Prédiction du modèle uniquement (L5)
nav_order: 218
evidence_level: L5
indication_count: 1
---

# Norgestimate
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

# Norgestimate : D'une indication originale non renseignée à l'élévation du zinc plasmatique

## Résumé en Une Phrase

Le norgestimate est un progestatif, généralement associé à l'éthinylestradiol dans les contraceptifs oraux combinés (connaissance générale : les AMM françaises du dossier ne mentionnent aucune indication).
Le modèle TxGNN prédit qu'il pourrait être utile pour l'**élévation du zinc plasmatique**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Zinc plasmatique élevé (*zinc, elevated plasma*) |
| Score de Prédiction TxGNN | 99,06 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 7 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Le norgestimate est un progestatif, le plus souvent utilisé avec l'éthinylestradiol dans des contraceptifs oraux combinés. Aucune indication d'origine n'est renseignée dans les données réglementaires fournies.

Aucun mécanisme ne soutient cette prédiction dans les données disponibles. La littérature générale (hors dossier) rapporte que les contraceptifs hormonaux tendent à **abaisser** le zinc sérique et à **augmenter** le cuivre. L'effet irait donc à l'opposé d'un traitement de l'excès de zinc.

Le zinc plasmatique élevé est plutôt un phénotype biologique qu'une maladie avec une voie thérapeutique médicamenteuse établie. Le score élevé de TxGNN (0,99) est une prédiction du modèle seule et peut refléter des artefacts du graphe de connaissances.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Cinq des 7 AMM sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|------|
| 65464991 | NARAVELA 250 microgrammes/35 microgrammes, comprimé | Comprimé | Exeltis Healthcare (Espagne) |
| 67592737 | TRINARA CONTINU, comprimé pelliculé | Comprimé(s) | Exeltis Healthcare (Espagne) |
| 68322762 | TRIAFEMI, comprimé | Comprimé (3 types) | Effik |
| 69274060 | TRINARA, comprimé pelliculé | Comprimé pelliculé (3 types) | Exeltis Healthcare (Espagne) |
| 66449857 | OPTIKINZY 250 microgrammes/35 microgrammes, comprimé | Comprimé (2 types) | Laboratoires Majorelle |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Le contexte pharmacologique connu (baisse du zinc sous contraceptifs hormonaux) va dans le sens inverse de l'effet recherché. Enfin, la cible est un phénotype biologique et non une maladie bien définie.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice de l'ANSM (mises en garde et contre-indications), qui bloque toute évaluation de sécurité
- Données sur le mécanisme d'action (par exemple via l'API DrugBank)
- Indications AMM officielles de chaque spécialité
- Recherche de littérature ciblée sur norgestimate et zinc plasmatique, et vérification de la pertinence clinique de la cible
- Analyse de compatibilité de voie d'administration et de similarité avec l'indication d'origine

> Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement nécessite une validation clinique avant toute application.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

