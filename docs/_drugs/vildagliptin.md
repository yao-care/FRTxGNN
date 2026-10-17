---
layout: default
title: Vildagliptin
parent: Prédiction du modèle uniquement (L5)
nav_order: 812
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Vildagliptin : nouvelle indication prédite, Syndrome de la personne raide classique (niveau de preuve L5). Indication d'origine : Diabète de type 2"
monitor_inn: "vildagliptin"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Vildagliptin
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

# Vildagliptine : Du diabète de type 2 au syndrome de la personne raide classique

## Résumé en une phrase

La vildagliptine est un antidiabétique oral, initialement utilisé pour le traitement du diabète de type 2.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome de la personne raide classique**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette prédiction.

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Diabète de type 2 |
| Nouvelle indication prédite | Syndrome de la personne raide classique |
| Score de prédiction TxGNN | 99,88 % |
| Niveau de preuve | L5 |
| Statut de marché en France | Uniquement des AMM annulées (aucune AMM valide) |
| Nombre d'AMM | 18 (toutes annulées) |
| Décision recommandée | Hold |

## Pourquoi cette prédiction est-elle raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. La vildagliptine est un inhibiteur de la dipeptidyl peptidase 4 (DPP-4). Les données de pharmacologie indiquent qu'elle se lie aussi à DPP-8, DPP-9 et TRPV4. En bloquant la DPP-4, elle augmente les taux d'incrétines actives (GLP-1, GIP), ce qui améliore le contrôle de la glycémie dans le diabète de type 2.

Le syndrome de la personne raide est un trouble neurologique rare, souvent d'origine auto-immune (anticorps anti-GAD65 dans de nombreux cas), avec une altération de la signalisation GABAergique. **Il n'existe aucun lien mécanistique identifiable** avec l'inhibition de la DPP-4. Tout rapprochement reste spéculatif, par exemple une modulation immunitaire via CD26/DPP-4. Le score élevé du modèle semble refléter une proximité dans le graphe de connaissances, notamment le lien entre auto-immunité et diabète, plutôt qu'une justification biologique démontrée. Le « syndrome du membre raide focal », une forme localisée de la même famille de maladies, obtient exactement le même score, ce qui renforce cette lecture.

## Preuves d'essais cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la littérature

Aucune littérature associée disponible actuellement.

## Informations de marché en France

Les 18 AMM recensées sont toutes annulées. Le texte d'indication approuvée n'est pas renseigné pour ces AMM. Les 5 premières sont listées ci-dessous.

| Numéro d'AMM | Nom du produit | Forme pharmaceutique | Titulaire | Statut |
|---------|------|------|------|------|
| 67520378 | GALVUS 50 mg | Comprimé | Novartis Europharm (Irlande) | Annulée |
| 63144220 | VILDAGLIPTINE EG 50 mg | Comprimé | EG Labo – Laboratoires Eurogenerics | Annulée |
| 66153274 | VILDAGLIPTINE SANDOZ 50 mg | Comprimé | Sandoz | Annulée |
| 61163720 | VILDAGLIPTINE VIATRIS 50 mg | Comprimé | Viatris Santé | Annulée |
| 60892792 | EUCREAS 50 mg/1000 mg (avec metformine) | Comprimé pelliculé | Novartis Europharm (Irlande) | Annulée |

## Considérations de sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicament-médicament n'a été identifiée dans les données compilées. Seules des interactions pharmacologiques avec des cibles protéiques (DPP-4, DPP-8, DPP-9, TRPV4) sont documentées.

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5). Aucun essai clinique ni publication ne la soutient, et aucun lien mécanistique plausible n'a pu être établi.
- Le médicament n'a plus d'AMM valide en France, ce qui limite aussi sa disponibilité pratique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Des données mécanistiques détaillées, et notamment une hypothèse biologique crédible reliant l'inhibition de la DPP-4 à la physiopathologie du syndrome de la personne raide.
- Des données précliniques ou des séries de cas dans cette maladie.
- Les mises en garde et contre-indications issues de la notice, aujourd'hui manquantes.
- Une clarification du statut réglementaire du produit.

**Remarque :** parmi les autres indications prédites pour la vildagliptine, le diabète de type 1 dispose de preuves nettement plus étoffées, de niveau L2. Elles comprennent un essai de phase 2 randomisé en double aveugle (rapamycine plus vildagliptine) et un essai de phase 3 de petite taille et de statut inconnu. Cette piste mérite une évaluation distincte.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

