---
layout: default
title: Doxylamine
parent: Prédiction du modèle uniquement (L5)
nav_order: 260
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Doxylamine : nouvelle indication prédite, Urticaire allergique (niveau de preuve L5). Indication d'origine : Rhinite allergique"
monitor_inn: "doxylamine"
predicted_indications: ["nasal cavity disease"]
---

# Doxylamine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

# Doxylamine : De la rhinite allergique à l'urticaire allergique

## Résumé en Une Phrase

La doxylamine est un antihistaminique H1 de première génération (éthanolamine), initialement utilisé pour la rhinite allergique, le rhume, la conjonctivite allergique et l'urticaire.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**urticaire allergique**, mais cette prédiction recoupe en grande partie les indications déjà connues.
Aucun essai clinique ni aucune publication ne soutient actuellement cette prédiction (**0 essai clinique**, **0 publication**).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Rhinite allergique (les textes d'indication des AMM ne sont pas renseignés ; indications issues du graphe de connaissances : rhinite allergique, rhinite vasomotrice, pharyngite, rhume, conjonctivite, urticaire, angio-œdème) |
| Nouvelle Indication Prédite | Urticaire allergique |
| Score de Prédiction TxGNN | 99,85 % |
| Niveau de Preuve | L5 (aucune étude réelle disponible ; la classification de l'analyse initiale était L4) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 4 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances pharmacologiques générales, la doxylamine est un antagoniste des récepteurs H1 de première génération, doté également d'effets anticholinergiques et sédatifs. Dans l'urticaire allergique, la libération d'histamine par les mastocytes provoque la papule et l'érythème : le blocage des récepteurs H1 est donc mécanistiquement plausible.

L'urticaire et l'angio-œdème figurent déjà parmi les indications d'origine de ce médicament. Il ne s'agit donc pas d'un véritable repositionnement : le score élevé (0,998) reflète très probablement ce chevauchement avec les indications existantes.

Les autres prédictions du modèle vont dans le même sens. La « maladie de la cavité nasale » (99,36 %) et la « laryngopharyngite aiguë » (99,34 %) reprennent des usages déjà connus. L'« urticaire au froid » (99,26 %) est plausible par effet de classe, mais les antihistaminiques de seconde génération non sédatifs, souvent à doses plus élevées, sont préférés par les recommandations en raison de leur meilleure tolérance.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62382724 | DONORMYL 15 mg, comprimé pelliculé sécable (UPSA) | Comprimé pelliculé sécable | Non renseignée (AMM annulée) |
| 67103299 | DONORMYL 15 mg, comprimé effervescent sécable (UPSA) | Comprimé effervescent sécable | Non renseignée (AMM annulée) |
| 64881366 | LIDENE 15 mg, comprimé pelliculé sécable (COOPER) | Comprimé pelliculé sécable | Non renseignée (AMM annulée) |
| 61447165 | CARIBAN 10 mg/10 mg, gélule à libération modifiée (EFFIK) | Gélule à libération modifiée | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : hypertension, insuffisance hépatique et maladie du foie, pancréatite, maladie de la vésicule biliaire, ulcère gastroduodénal, diabète et acidocétose diabétique, hypertrophie bénigne de la prostate, obstruction du col vésical, glaucome à angle fermé et hypertension oculaire, maladie coronarienne, infarctus du myocarde, athérosclérose, tachycardie ventriculaire, hyperthyroïdie (maladie de Basedow), hémoglobinopathie, abus/dépendance de substances, intoxication au paracétamol.
- **Interactions médicamenteuses** : 289 interactions recensées.
  - *Majeures* : chlorure de potassium, citrate de potassium.
  - *Modérées* (principales) : anticholinergiques (atropine, scopolamine, hyoscyamine, glycopyrronium, dicyclomine, propanthéline), opioïdes et apparentés (morphine, opium, lopéramide, éluxadoline), cannabinoïdes (dronabinol, nabilone), métoclopramide. Ces associations majorent surtout les effets anticholinergiques et sédatifs.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, non disponibles dans les données compilées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction recoupe largement les indications existantes (urticaire, angio-œdème), sans essai ni publication spécifiques. Toutes les AMM françaises sont annulées, ce qui limite le développement pratique. Les antihistaminiques de seconde génération sont préférés dans l'urticaire.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité).
- Obtenir les données sur le mécanisme d'action (par exemple via DrugBank).
- Rechercher des essais cliniques et des publications sur l'urticaire allergique et l'urticaire au froid avec la doxylamine.
- Clarifier la valeur ajoutée par rapport aux antihistaminiques de seconde génération et la faisabilité réglementaire, compte tenu du statut « annulé » des AMM.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

