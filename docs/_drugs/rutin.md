---
layout: default
title: Rutin
parent: Prédiction du modèle uniquement (L5)
nav_order: 686
evidence_level: L5
indication_count: 8
---

# Rutin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

# Rutine : De la carence en acide ascorbique à la maladie fibrokystique du sein

## Résumé en Une Phrase

La rutine est un flavonoïde, initialement associé au traitement de la carence en acide ascorbique et du scorbut.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **maladie fibrokystique du sein**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carence en acide ascorbique, scorbut (selon le graphe de connaissances TxGNN ; le texte d'indication de l'AMM française n'est pas renseigné) |
| Nouvelle Indication Prédite | Maladie fibrokystique du sein |
| Score de Prédiction TxGNN | 99,74 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Retiré (AMM annulée uniquement) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la rutine est un flavonoïde aux propriétés antioxydantes, anti-inflammatoires et de protection capillaire. Elle a été rattachée à la carence en acide ascorbique et au scorbut, des états où la fragilité vasculaire joue un rôle.

Mécanistiquement, ces propriétés pourraient avoir un lien avec l'inflammation bénigne du tissu mammaire, mais aucune donnée directe ne vient étayer cette hypothèse. Le score élevé de TxGNN reflète une proximité dans le graphe de connaissances, et non une preuve indépendante.

Les autres prédictions du modèle vont dans le même sens : adénose apocrine du sein (99,64 %), adénose à canaux émoussés (99,64 %) et dysplasie mammaire bénigne (99,42 %). Elles concernent toutes des lésions mammaires bénignes et sont probablement redondantes entre elles. D'autres prédictions (candidose vulvovaginale, abcès du sein, cytostéatonécrose du sein, vaginite) ne disposent d'aucun appui mécanistique plausible dans les données fournies.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la maladie fibrokystique du sein.

Pour information, deux publications ont été retrouvées pour une autre prédiction (vaginite). Il s'agit d'études précliniques chez le rat, portant sur des extraits de plantes dans un modèle de syndrome des ovaires polykystiques induit par le létrozole. Elles n'étudient pas la rutine et ne concernent pas la vaginite : elles n'apportent donc aucun soutien direct.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68245006 | VELITEN, comprimé pelliculé (LABORATOIRES FRILAB) | Comprimé pelliculé | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : drépanocytose, persistance héréditaire de l'hémoglobine fœtale, hyperoxalurie primitive, hémochromatose héréditaire, hémosidérose, maladie du métabolisme du fer, maladie de Wilson.
- **Interactions médicamenteuses** : aucune interaction retrouvée dans les données compilées.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication pertinente. De plus, la seule AMM française est annulée et les données de sécurité officielles sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications) auprès de l'ANSM, étape bloquante pour tout examen de sécurité
- Obtenir les données sur le mécanisme d'action depuis DrugBank
- Mener une revue de la littérature ciblée sur la rutine/flavonoïdes dans les affections mammaires bénignes
- Évaluer la faisabilité de la voie d'administration et de la formulation, l'AMM étant annulée
- Examiner les contre-indications issues du graphe (troubles du métabolisme du fer, drépanocytose, etc.) dans la population cible
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

