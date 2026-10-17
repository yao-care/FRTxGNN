---
layout: default
title: Belimumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 92
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Belimumab : nouvelle indication prédite, Trouble de la libération plaquettaire primaire (niveau de preuve L5). Indication d'origine : Lupus érythémateux systémique (y compris pédiatrique)"
monitor_inn: "belimumab"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "severe nonproliferative diabetic retinopathy", "autosomal dominant macrothrombocytopenia"]
---

# Belimumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

# Bélimumab : Du Lupus Érythémateux Systémique au Trouble de la Libération Plaquettaire Primaire

## Résumé en Une Phrase

Le bélimumab est un anticorps ciblant BLyS (BAFF), un facteur de survie des lymphocytes B, initialement utilisé dans le traitement du lupus érythémateux systémique (y compris pédiatrique).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble de la libération plaquettaire primaire**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Lupus érythémateux systémique (y compris pédiatrique) |
| Nouvelle Indication Prédite | Trouble de la libération plaquettaire primaire |
| Score de Prédiction TxGNN | 99,96 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Annulé uniquement (aucune AMM valide) |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le bélimumab inhibe BLyS (BAFF), ce qui réduit la survie des lymphocytes B autoréactifs. Son efficacité dans le lupus érythémateux systémique repose sur ce mécanisme immunitaire.

Les troubles de la libération plaquettaire primaires sont des défauts héréditaires ou intrinsèques de la fonction plaquettaire, et non des maladies médiées par les lymphocytes B. **Aucun lien mécanistique n'est étayé par les données compilées pour ce rapport.** Le score élevé du modèle (99,96 %) reflète probablement la proximité dans le graphe de connaissances avec des nœuds plaquettaires et auto-immuns, et non une plausibilité biologique démontrée.

Cette prédiction doit donc être considérée comme une hypothèse purement computationnelle. Le champ du mécanisme d'action d'origine étant manquant, le lien n'a pas pu être vérifié de façon croisée.

### Autres indications prédites (pour information)

| Rang | Indication prédite | Score TxGNN | Plausibilité mécanistique |
|------|------|------|------|
| 2 | Pseudo-maladie de von Willebrand | 99,96 % | Aucun mécanisme plausible (variant gain de fonction de GP1BA) |
| 3 | Thrombasthénie de Glanzmann | 99,88 % | Aucune action sur l'intégrine αIIbβ3 ; pertinence hypothétique et indirecte pour l'alloimmunisation post-transfusionnelle |
| 4 | Thrombopénie alloimmune fœtale et néonatale | 99,59 % | La plus plausible biologiquement (alloanticorps maternels), mais effet limité sur les plasmocytes à longue durée de vie et préoccupations de sécurité pendant la grossesse |
| 5 | Rétinopathie diabétique non proliférante sévère | 99,05 % | Aucun rôle établi de l'inhibition de BLyS ; lien spéculatif |
| 6 | Macrothrombopénie autosomique dominante | 99,04 % | Trouble héréditaire de la mégacaryopoïèse, sans bénéfice mécanistique évident |

Aucune de ces indications ne dispose d'essai clinique ni de publication dans les données compilées.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les trois AMM identifiées sont toutes annulées. Le texte des indications approuvées n'est pas renseigné dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 65592934 | BENLYSTA 120 mg | Poudre pour solution à diluer pour perfusion | Annulée |
| 60205159 | BENLYSTA 200 mg | Solution injectable en stylo prérempli | Annulée |
| 65600733 | BENLYSTA 400 mg | Poudre pour solution à diluer pour perfusion | Annulée |

Titulaire : GlaxoSmithKline (Ireland).

---

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

- **Interactions médicamenteuses** : 69 interactions ont été recensées. Les principales sont :
  - **Majeures** : adalimumab, baricitinib, certolizumab pegol, bacille de Calmette-Guérin (souche Tice, vivant)
  - **Modérées** : roflumilast, azathioprine, anakinra, canakinumab, alemtuzumab, alefacept, ainsi que plusieurs vaccins (anatoxine tétanique, charbon, adénovirus de type 4, choléra vivant) et probiotiques/antigènes vivants
  - **Mineures** : sels de zinc (acétate, gluconate, sulfate, chlorure)

  Globalement, les interactions majeures concernent des associations avec d'autres immunosuppresseurs/biothérapies et des vaccins vivants, avec un risque accru d'infection.

- **Contexte particulier** : une utilisation pendant la grossesse (thrombopénie alloimmune fœtale et néonatale) soulèverait des préoccupations de sécurité supplémentaires.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et aucun lien mécanistique plausible n'est identifié pour l'indication principale.
- Le produit n'a plus d'AMM valide en France, et les données de sécurité de la notice sont manquantes (lacune bloquante).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Réaliser une revue de la littérature préclinique et clinique pour les indications prédites
- Si une piste est poursuivie, privilégier la thrombopénie alloimmune fœtale et néonatale (la plus plausible), avec une évaluation spécifique de la sécurité pendant la grossesse
- Clarifier la situation réglementaire (raisons de l'annulation des AMM et voies d'accès possibles)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

