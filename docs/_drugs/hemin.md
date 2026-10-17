---
layout: default
title: Hemin
parent: Prédiction du modèle uniquement (L5)
nav_order: 376
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Hemin : nouvelle indication prédite, Purpura thrombopénique (niveau de preuve L5). Indication d'origine : Porphyrie aiguë intermittente"
monitor_inn: "hemin"
predicted_indications: ["thrombocytopenic purpura", "hemophilia", "C1 inhibitor deficiency", "acquired coagulation factor deficiency", "serpinopathy with toxic serpin polymerization", "hereditary angioedema with C1Inh deficiency", "inherited thrombophilia", "symptomatic form of hemophilia in female carriers", "hereditary von Willebrand disease", "congenital factor XI deficiency"]
---

# Hemin
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

# Hémine : De la porphyrie aiguë intermittente à la purpura thrombopénique

## Résumé en Une Phrase

L'hémine est un médicament initialement utilisé pour le traitement de la porphyrie aiguë intermittente.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **purpura thrombopénique**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Porphyrie aiguë intermittente (d'après le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Purpura thrombopénique |
| Score de Prédiction TxGNN | 99,79 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Retiré du marché (AMM annulée uniquement) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'hémine induit l'hème oxygénase-1 et freine la biosynthèse de l'hème (enzyme ALA synthase) dans la porphyrie. C'est ce qui explique son efficacité dans la porphyrie aiguë intermittente.

Aucun lien mécanistique avec le purpura thrombopénique (immunologique ou thrombotique) n'est établi dans les données compilées pour ce rapport. Le score élevé du modèle reflète probablement une proximité dans le réseau de connaissances, et non une raison pharmacologique démontrée.

L'hémine est par ailleurs connue pour des effets pro-coagulants et des effets possibles sur les plaquettes. Dans ce contexte, un bénéfice thérapeutique est mécanistiquement douteux et un risque pour la sécurité est plausible.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour le purpura thrombopénique.

À titre d'information, la deuxième indication prédite (hémophilie) a ramené trois publications, mais elles concernent le givosiran ou la porphyrie hépatique aiguë, et non l'hémine dans l'hémophilie. Elles n'apportent donc aucune preuve en faveur d'une indication hors porphyrie.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65109937 | NORMOSANG 25 mg/ml, solution à diluer pour perfusion (RECORDATI RARE DISEASES) | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 74 interactions ont été identifiées. Parmi celles listées :
  - **Majeures** : éthinylestradiol, estradiol, estrogènes conjugués, butalbital, amobarbital, phénobarbital.
  - **Modérées** : acide acétylsalicylique, abciximab, alteplase, anagrélide, dipyridamole, apixaban, bétrixaban, acalabrutinib, avapritinib, antithrombine III (humaine et alfa), trastuzumab emtansine, ibritumomab tiuxétan, tositumomab (I-131).
- Beaucoup de ces associations concernent l'hémostase (anticoagulants, antiagrégants, thrombolytiques). Elles sont particulièrement pertinentes pour une indication touchant les plaquettes ou la coagulation.
- Des effets pro-coagulants et une thrombophlébite ont été rapportés avec l'hémine. Un risque est plausible chez les patients présentant un trouble de la coagulation ou une thrombopénie.

Veuillez consulter la notice pour les mises en garde et contre-indications détaillées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5) : aucun essai clinique ni publication pertinente, et aucun mécanisme plausible. Les effets connus de l'hémine sur la coagulation suggèrent plutôt un risque qu'un bénéfice.
- L'AMM française est annulée et les données de sécurité issues de la notice sont manquantes, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde, contre-indications).
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Mener une revue de la littérature ciblée sur l'hémine et le purpura thrombopénique, ainsi que sur ses effets hématologiques.
- Évaluer la compatibilité de la voie d'administration (perfusion) avec l'indication visée.
- Réaliser des études précliniques sur les effets de l'hémine sur les plaquettes avant toute étude clinique.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

