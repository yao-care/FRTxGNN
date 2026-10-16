---
layout: default
title: Fentanyl
parent: Prédiction du modèle uniquement (L5)
nav_order: 323
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Fentanyl : nouvelle indication prédite, Syndrome néphrogénique d'antidiurèse inappropriée (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM"
---

# Fentanyl
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

# Fentanyl : D'un analgésique opioïde au Syndrome néphrogénique d'antidiurèse inappropriée

## Résumé en Une Phrase

Le fentanyl est un analgésique opioïde puissant, agoniste des récepteurs mu, commercialisé en France sous forme de dispositifs transdermiques et de comprimés buccogingivaux. L'indication originale n'est pas renseignée dans les données compilées pour ce report.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome néphrogénique d'antidiurèse inappropriée** (score de 99,46 %), mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction, qui reste purement algorithmique et biologiquement peu plausible.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Syndrome néphrogénique d'antidiurèse inappropriée |
| Score de Prédiction TxGNN | 99,46 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances générales, le fentanyl est un agoniste puissant des récepteurs opioïdes mu, utilisé en analgésie. Son efficacité dans la douleur n'est pas documentée ici par un texte d'indication d'AMM.

**La prédiction apparaît peu plausible.** Le syndrome néphrogénique d'antidiurèse inappropriée est dû à des mutations gain de fonction du récepteur V2 de la vasopressine (AVPR2), cible sur laquelle le fentanyl n'a aucune action connue. Par ailleurs, les opioïdes peuvent stimuler la libération d'ADH et provoquer une antidiurèse, ce qui aggraverait la maladie au lieu de la traiter.

Le score TxGNN élevé (99,46 %) résulte uniquement d'une prédiction par graphe de connaissances. Sans données de mécanisme validées, elle ne peut pas être recoupée avec la pharmacologie établie. Un signal de contre-indication possible est en outre suspecté.

**Seconde prédiction (pour information) :** le syndrome de Gilles de la Tourette (score de 99,05 %, niveau L5, Hold). Le lien est indirect et spéculatif (modulation de la dopamine striatale par le système opioïde endogène). Le risque de dépendance, de dépression respiratoire et d'abus du fentanyl rend un rapport bénéfice-risque favorable très improbable dans une affection neurodéveloppementale chronique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 20 AMM recensées sont toutes annulées ; aucune n'est valide. Le texte d'indication approuvée n'est pas disponible. Principales AMM :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65173904 | FENTANYL SANDOZ 100 µg/heure | Dispositif transdermique | Non renseignée |
| 60914025 | DUROGESIC 25 µg/heure | Dispositif transdermique | Non renseignée |
| 67439271 | MATRIFEN 12 µg/heure | Dispositif transdermique | Non renseignée |
| 66152400 | EFFENTORA 400 µg | Comprimé buccogingival | Non renseignée |
| 60616751 | DUROGESIC 50 µg/heure | Dispositif transdermique | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (TxGNN/PrimeKG, hors texte de notice)** : hypertension, hypotension orthostatique, syndrome du QT long et torsades de pointes, insuffisance hépatique et maladies du foie, maladie rénale, bronchopneumopathie chronique obstructive, asthme, pancréatite, maladies de la vésicule biliaire, maladies inflammatoires de l'intestin, hyperplasie bénigne de la prostate, troubles anxieux, abus ou dépendance aux substances, déficit en potassium, atrophie multisystématisée, syndrome de tachycardie orthostatique posturale, entre autres.
- **Interactions médicamenteuses** (100 interactions recensées ; principales) :
  - Majeures : alvimopan, aprépitant, bupropion, clarithromycine, clotrimazole, dexaméthasone, dexfenfluramine, fenfluramine, dolasétron, granisétron, lorcasérine.
  - Modérées : atropine, cimétidine, clidinium, dicyclomine, dronabinol, éluxadoline, glycopyrronium, hyoscyamine, phénylbutyrate de glycérol.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication. Elle est mécanistiquement contradictoire (les opioïdes favorisent l'antidiurèse) et le profil de sécurité est défavorable. Toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (bloquant pour l'étape de sécurité), en téléchargeant et analysant la notice.
- Les données sur le mécanisme d'action issues de DrugBank.
- Une justification mécanistique plausible reliant le fentanyl à la voie AVPR2/vasopressine, ou l'abandon de cette piste.
- Toute preuve préclinique ou clinique pour l'une ou l'autre des indications prédites.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

