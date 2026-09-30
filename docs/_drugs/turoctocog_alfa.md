---
layout: default
title: Turoctocog Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 328
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa
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

# Turoctocog alfa : De l'hémophilie A au trouble primaire de la libération plaquettaire

## Résumé en Une Phrase

Turoctocog alfa est un facteur VIII de coagulation recombinant, tronqué du domaine B (commercialisé sous le nom NovoEight). Il sert au traitement substitutif de l'hémophilie A, un déficit en facteur VIII. Cette indication vient de la connaissance générale du produit, car le texte d'indication ANSM est vide dans les données reçues.
Le modèle TxGNN prédit qu'il pourrait être utile dans le **trouble primaire de la libération plaquettaire**, mais **aucun essai clinique et aucune publication** ne soutiennent cette prédiction. Elle repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hémophilie A (déficit en facteur VIII) ; le texte d'indication n'est pas renseigné dans les AMM du pack |
| Nouvelle Indication Prédite | Trouble primaire de la libération plaquettaire |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 6 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Turoctocog alfa remplace le facteur VIII manquant, un cofacteur de la voie de la coagulation (complexe tenase). Son efficacité est établie dans l'hémophilie A, mais rien dans le dossier ne montre qu'il puisse agir sur un défaut propre aux plaquettes.

En pratique, cette prédiction est **peu convaincante sur le plan mécanistique**. Le trouble de la libération plaquettaire est un défaut intrinsèque de la fonction plaquettaire (sécrétion des granules), que le remplacement du facteur VIII ne corrige pas. Le score élevé (0,9999) semble refléter une proximité dans le graphe de connaissances, au sein du groupe des maladies hémorragiques, plutôt qu'un lien thérapeutique réel.

Les autres prédictions du top 10 suivent le même schéma. La plupart sont des défauts plaquettaires (thrombasthénie de Glanzmann, syndrome de Scott, déficit du récepteur du collagène, thrombopénies constitutionnelles) ou de la voie VWF (pseudo-maladie de Willebrand). Aucune n'est corrigée par un apport de facteur VIII. Deux points appellent une vigilance particulière :
- Le **purpura thrombotique thrombocytopénique** et la **thrombocytose héréditaire** sont des états prothrombotiques. Un apport de facteur VIII y poserait un problème de sécurité et non une opportunité thérapeutique.
- Le **déficit acquis en facteur de coagulation** (rang 5) est le candidat le plus plausible sur le plan biologique, car le facteur VIII est sa cible naturelle. La catégorie est toutefois hétérogène. Dans l'hémophilie A acquise, des auto-anticorps neutralisent le facteur VIII humain, et l'efficacité serait probablement nulle. Ce candidat est classé « Research Question » et non « Hold ».

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Cinq des six AMM sont listées ci-dessous. Elles correspondent toutes à des dosages du même produit.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64266526 | NOVOEIGHT 3000 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 67582344 | NOVOEIGHT 1500 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 65044350 | NOVOEIGHT 1000 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 66990599 | NOVOEIGHT 250 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 62333524 | NOVOEIGHT 2000 UI | Poudre et solvant pour solution injectable | Non renseignée |

Titulaire : Novo Nordisk (Danemark).

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été trouvée dans les données disponibles.

Une réserve liée aux prédictions s'impose : le facteur VIII élevé est un facteur de risque prothrombotique. Son administration dans des états à risque thrombotique, comme le purpura thrombotique thrombocytopénique ou la thrombocytose, serait potentiellement dangereuse.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai ni publication. Le mécanisme du facteur VIII ne correspond pas à un défaut plaquettaire.
- Les données de sécurité de la notice ANSM sont absentes. Ce manque est bloquant pour passer à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications), lacune bloquante.
- Obtenir le mécanisme d'action détaillé via DrugBank.
- Renseigner le texte des indications approuvées dans les AMM.
- Ne poursuivre l'évaluation que pour le déficit acquis en facteur de coagulation, après avoir précisé le sous-type et comparé avec les agents de contournement ou le facteur VIII porcin.
- Vérifier le terme « flood factor deficiency » dans l'ontologie source, car il n'a pu être associé à aucun déficit en facteur de coagulation reconnu.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

