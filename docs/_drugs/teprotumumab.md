---
layout: default
title: Teprotumumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 741
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Teprotumumab : nouvelle indication prédite, Monosomie X (niveau de preuve L5). Indication d'origine : Exophtalmie endocrinienne"
monitor_inn: "teprotumumab"
predicted_indications: ["monosomy X", "esophageal varices with bleeding", "esophageal varices without bleeding", "mixed gonadal dysgenesis", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "Turner syndrome due to structural X chromosome anomalies", "mosaic monosomy X", "sex chromosome disorder of sex development", "varicose disease", "X chromosome number anomaly"]
---

# Teprotumumab
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

# Téprotumumab : De l'exophtalmie endocrinienne au syndrome de Turner (monosomie X)

## Résumé en Une Phrase

Le téprotumumab est un anticorps monoclonal initialement utilisé pour traiter l'exophtalmie endocrinienne (ophtalmopathie associée à la thyroïde).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **monosomie X (syndrome de Turner)**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Exophtalmie endocrinienne (selon le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Monosomie X |
| Score de Prédiction TxGNN | 99,79 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Annulée uniquement (AMM annulée) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le téprotumumab est un anticorps monoclonal inhibiteur du récepteur du facteur de croissance analogue à l'insuline de type 1 (IGF-1R). Son efficacité dans l'exophtalmie endocrinienne repose sur ce blocage.

Le lien avec la monosomie X (syndrome de Turner) provient uniquement d'une prédiction du graphe de connaissances. La signalisation de l'IGF-1 intervient dans la croissance, qui est altérée dans le syndrome de Turner. Toutefois, inhiber l'IGF-1R irait plutôt à l'encontre de l'objectif habituel de stimulation de la croissance. **Aucune justification thérapeutique plausible n'est étayée par les données disponibles.**

Les autres prédictions du même classement appartiennent en grande partie à des groupes liés entre eux, ce qui indique qu'elles ne constituent pas des preuves indépendantes :
- **Groupe Turner / chromosome X** : mosaïque monosomie X, syndrome de Turner par anomalies structurelles du chromosome X, anomalie du nombre de chromosomes X, trouble du développement sexuel d'origine chromosomique, dysgénésie gonadique mixte.
- **Groupe varices** : varices œsophagiennes avec ou sans saignement, maladie variqueuse. Aucun lien mécanistique clair avec le blocage de l'IGF-1R ; le score reflète probablement des artefacts de topologie du graphe.
- **Maladie mitochondriale (anomalies de l'ADN nucléaire)** : lien indirect et spéculatif.

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
| 68452994 | TEPEZZA 500 mg, poudre pour solution à diluer pour perfusion (AMGEN EUROPE) | Poudre pour solution à diluer pour perfusion | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

Les mises en garde et contre-indications de la notice ne sont pas disponibles dans les données compilées ; veuillez consulter la notice pour ces informations.

**Interactions médicamenteuses** : 45 interactions de niveau modéré ont été identifiées, principalement avec des antidiabétiques (20 sont détaillées dans les données). Il s'agit probablement d'un risque de déséquilibre glycémique (hyperglycémie), ce qui est cohérent avec le blocage de l'IGF-1R, mais le mécanisme n'est pas précisé dans les données. Exemples :
- Inhibiteurs de l'alpha-glucosidase et biguanides : acarbose, metformine
- Thiazolidinediones : pioglitazone
- Sulfamides hypoglycémiants : chlorpropamide, glimépiride, glipizide, glibenclamide, acétohexamide
- Inhibiteurs de la DPP-4 : alogliptine, saxagliptine, linagliptine
- Inhibiteurs du SGLT2 : canagliflozine, dapagliflozine, empagliflozine, ertugliflozine
- Agonistes du GLP-1 : albiglutide, dulaglutide, sémaglutide, exénatide
- Insuline humaine

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication. Le mécanisme (inhibition de l'IGF-1R) semble en contradiction avec les objectifs thérapeutiques du syndrome de Turner. De plus, l'AMM française est annulée et les données de sécurité de la notice sont absentes, ce qui bloque le criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice sur le site de l'ANSM (donnée bloquante).
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Établir un argumentaire biologique plausible pour l'inhibition de l'IGF-1R dans le syndrome de Turner, ou envisager une indication candidate alternative plus cohérente.
- Clarifier les raisons de l'annulation de l'AMM et le statut de commercialisation actuel.
- Rechercher des études précliniques ou observationnelles avant tout développement clinique.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

