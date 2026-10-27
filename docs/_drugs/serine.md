---
layout: default
title: Serine
parent: Prédiction du modèle uniquement (L5)
nav_order: 699
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Serine : nouvelle indication prédite, Myopathie viscérale familiale (niveau de preuve L5). Indication d'origine : Glaucome à angle ouvert, tuberculose pulmonaire"
monitor_inn: "serine"
predicted_indications: ["familial visceral myopathy", "intestinal obstruction", "myopathic intestinal pseudoobstruction", "unclassified intestinal pseudoobstruction", "neuronal intestinal dysplasia, type B", "intestinal pseudoobstruction, neuronal, chronic idiopathic, X-linked", "exercise-induced malignant hyperthermia", "aqueous misdirection"]
---

# Serine
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

## Sérine : De le glaucome à angle ouvert à la myopathie viscérale familiale
{: .text-alpha }

## Résumé en Une Phrase

La sérine est un acide aminé présent dans de nombreuses solutions de nutrition parentérale. Selon le graphe de connaissances utilisé par TxGNN, ses indications d'origine seraient le glaucome à angle ouvert et la tuberculose pulmonaire.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **myopathie viscérale familiale**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction. Elle repose uniquement sur le modèle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Glaucome à angle ouvert, tuberculose pulmonaire (selon le graphe de connaissances ; aucun texte d'indication n'est renseigné dans les AMM) |
| Nouvelle Indication Prédite | Myopathie viscérale familiale |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. La sérine est un acide aminé intégré à des solutions de nutrition parentérale (perfusions d'acides aminés, émulsions et poches multicompartiments), mais les données compilées ne décrivent pas de mécanisme pharmacologique précis.

Aucun lien mécanistique n'est étayé par les données entre la sérine et la myopathie viscérale familiale. Cette maladie est un trouble génétique du muscle lisse (par exemple lié à *ACTG2*), et rien ne relie une supplémentation en sérine à sa physiopathologie. Le score élevé (99,99 %) est une prédiction issue du graphe uniquement. De plus, les indications d'origine du graphe (glaucome, tuberculose) sont très éloignées de l'usage nutritionnel des produits commercialisés, ce qui affaiblit toute inférence de similarité.

Les autres prédictions du modèle se regroupent autour de pathologies intestinales (pseudo-obstructions, obstruction intestinale) et du glaucome. Elles sont également sans soutien clinique, et plusieurs partagent des scores identiques, ce qui suggère un voisinage commun dans le graphe plutôt que des preuves indépendantes.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la myopathie viscérale familiale.

À titre d'information, pour la deuxième prédiction (obstruction intestinale), 17 publications ont été retrouvées, mais elles semblent issues d'une correspondance de mots-clés (par exemple « serine » dans des protéases ou des kinases) ou portent sur des causes d'obstruction (syndrome de Peutz-Jeghers, cohésinopathies, mésothéliome). Aucune n'évalue la sérine comme traitement. Il en va de même pour le glaucome à angle fermé, où les publications concernent le gène de la protéase à sérine PRSS56, ce qui n'est pas lié à un effet thérapeutique de l'acide aminé.

---

## Informations de Marché en France

Les 20 AMM recensées sont toutes annulées. Aucun texte d'indication approuvée n'est renseigné. Cinq exemples :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61960303 | AMINOVEN 10 POUR CENT | Solution pour perfusion | Non renseignée |
| 69667989 | AMINOVEN 5 POUR CENT | Solution pour perfusion | Non renseignée |
| 62947013 | AMINOPLASMAL 25 | Solution pour perfusion | Non renseignée |
| 61786735 | AMINOMIX 500 | Solution et solution pour perfusion | Non renseignée |
| 63183821 | AMINOPLASMAL 8 | Solution pour perfusion | Non renseignée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : épilepsie, troubles anxieux, troubles psychotiques et mentaux, maladie rénale (dont insuffisance rénale chronique et terminale), néphrolithiase, néphrocalcinose, hypercalcémie, diabète et acidocétose diabétique, maladies cardiaques et cardiovasculaires, fibrillation ventriculaire, intoxication digitalique, carence en vitamine B12 et anémie mégaloblastique, sarcoïdose, abus de substances, entre autres.
- **Interactions médicamenteuses** : aucune interaction trouvée dans les données compilées.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, car elles n'ont pas pu être extraites.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication pertinente, sans lien mécanistique plausible, et sans AMM valide en France. Les données de sécurité officielles manquent, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde et contre-indications) en téléchargeant et analysant le PDF.
- Obtenir les données sur le mécanisme d'action via DrugBank.
- Établir un lien mécanistique plausible entre la sérine et la physiopathologie de la myopathie viscérale familiale.
- Rechercher des études précliniques ou cliniques ciblées, puis évaluer la compatibilité des voies d'administration et de la formulation.
- Clarifier le statut réglementaire, toutes les AMM étant annulées.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

