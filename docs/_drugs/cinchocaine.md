---
layout: default
title: Cinchocaine
parent: Prédiction du modèle uniquement (L5)
nav_order: 171
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Cinchocaine : nouvelle indication prédite, Bronchite (niveau de preuve L5). Indication d'origine : Dermatite"
monitor_inn: "cinchocaine"
predicted_indications: ["bronchitis", "acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "acne keloid", "hydroa vacciniforme, familial", "amyopathic dermatomyositis"]
---

# Cinchocaine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

## Cinchocaïne : De la Dermatite à la Bronchite
{: .text-alpha }

## Résumé en Une Phrase

La cinchocaïne (dibucaïne) est un anesthésique local de type amide, initialement utilisé pour le traitement de la dermatite (notamment sous forme de suppositoires).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **bronchite**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Dermatite (d'après le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Bronchite |
| Score de Prédiction TxGNN | 99,77 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Annulé uniquement |
| Nombre d'AMM | 2 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la cinchocaïne est un anesthésique local de type amide qui bloque les canaux sodiques voltage-dépendants, et son usage dermatologique et proctologique repose sur un soulagement symptomatique de la douleur et du prurit.

Un lien théorique avec la bronchite serait la suppression de l'activité des fibres sensitives des voies aériennes (réflexe de toux), comme avec d'autres anesthésiques locaux topiques. Ce raisonnement reste hypothétique, sans donnée à l'appui.

Il faut également noter que l'usage systémique ou inhalé de la cinchocaïne pose un problème de sécurité, sa toxicité étant élevée par rapport à d'autres anesthésiques locaux. Le score élevé du modèle reflète une association computationnelle et ne constitue pas une preuve d'efficacité.

D'autres indications prédites présentent le même niveau de preuve (L5, sans essai ni publication) : acrodermatite chronique atrophiante (99,76 %), dermatomyosite néonatale (99,72 %), pneumopathie interstitielle secondaire de l'enfant associée à une connectivite (99,72 %), acné chéloïdienne (99,67 %), hydroa vacciniforme familial (99,66 %) et dermatomyosite amyopathique (99,65 %). Pour la plupart, seul un soulagement symptomatique local serait concevable, sans mécanisme modifiant la maladie.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65569519 | DELIPROCT, suppositoire (annulée) | Suppositoire | Non renseignée |
| 63394747 | ULTRAPROCT, suppositoire (annulée) | Suppositoire | Non renseignée |

Les deux AMM sont annulées (fabricant : KARO PHARMA, Suède) ; aucune AMM valide n'est actuellement recensée.

## Considérations de Sécurité

Les données de sécurité issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité.

À titre indicatif, le graphe de connaissances associe la cinchocaïne à des contre-indications pour les affections suivantes (il ne s'agit pas du texte de la notice) :
- **Neurologiques et neuromusculaires** : épilepsie, myasthénie grave (dont la forme de l'adulte), maladie de la jonction neuromusculaire
- **Cardiovasculaires** : arrêt cardiaque soudain, maladie de la conduction cardiaque, maladie cardiovasculaire, maladie cardiaque
- **Respiratoires** : insuffisance respiratoire
- **Hépatiques, rénales et biliaires** : maladie hépatique, maladie rénale, pyo-uretère, maladie de la vésicule biliaire
- **Métaboliques** : déficit en butyrylcholinestérase

Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées. L'utilisation chez le nouveau-né ou l'enfant (dermatomyosite néonatale, pneumopathie interstitielle pédiatrique) soulève des préoccupations supplémentaires, notamment le risque de toxicité des anesthésiques locaux (méthémoglobinémie, absorption systémique). La contre-indication théorique en cas d'insuffisance respiratoire est également pertinente pour la bronchite.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai clinique ni publication, mécanisme d'action non documenté, et aucune AMM valide en France. Les préoccupations de sécurité en cas d'usage inhalé ou systémique, ainsi que les données de sécurité manquantes (blocage au stade de dépistage), empêchent d'aller plus loin.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice de l'ANSM (mises en garde et contre-indications)
- Données détaillées sur le mécanisme d'action (via DrugBank)
- Revue de la littérature préclinique sur les anesthésiques locaux dans la toux et les maladies des voies aériennes
- Évaluation de la compatibilité des voies d'administration (suppositoire vs voie respiratoire) et du profil de toxicité
- Clarification du statut réglementaire (AMM annulées)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

