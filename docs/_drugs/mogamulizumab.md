---
layout: default
title: Mogamulizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 511
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Mogamulizumab : nouvelle indication prédite, Carcinome urothélial de l'urètre prostatique (niveau de preuve L5). Indication d'origine : Mycosis fongoïde et variantes"
monitor_inn: "MOGAMULIZUMAB"
predicted_indications: ["prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "renal pelvis papillary urothelial carcinoma", "human herpesvirus 8-related tumor", "ectomesenchymoma", "malignant cutaneous granular cell skin tumor"]
---

# Mogamulizumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

# Mogamulizumab : Du Lymphome T Cutané au Carcinome Urothélial de l'Urètre Prostatique

## Résumé en Une Phrase

Le mogamulizumab est un anticorps monoclonal anti-CCR4, initialement utilisé pour le traitement des lymphomes T cutanés (mycosis fongoïde et variantes, lymphomes T périphériques).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **carcinome urothélial de l'urètre prostatique**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Mycosis fongoïde et variantes ; lymphome T cutané primitif (selon le graphe de connaissances, le texte d'indication de l'AMM n'étant pas renseigné) |
| Nouvelle Indication Prédite | Carcinome urothélial de l'urètre prostatique |
| Score de Prédiction TxGNN | 99,44 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Annulée uniquement |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le mogamulizumab est un anticorps monoclonal dirigé contre le récepteur de chimiokine CCR4. Il élimine les cellules CCR4+, dont les lymphocytes T régulateurs (Treg), par cytotoxicité cellulaire dépendante des anticorps (ADCC). Son efficacité a été établie dans les lymphomes T cutanés.

Le lien théorique avec le carcinome urothélial serait la déplétion des Treg dans le microenvironnement tumoral, afin de renforcer l'immunité antitumorale. Ce raisonnement reste **spéculatif** : aucune donnée ne montre que CCR4 soit exprimé ou pertinent dans cette tumeur, et la similarité avec l'indication d'origine n'a pas été évaluée.

Le score TxGNN élevé reflète une prédiction du graphe de connaissances et ne constitue pas une preuve d'efficacité. Les autres cibles prédites (carcinomes urothéliaux du bassinet et de la vessie, tumeurs liées à HHV-8, ectomésenchymome, tumeur cutanée à cellules granuleuses maligne) reposent sur le même type de raisonnement, sans aucune donnée de soutien.

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
| 62292771 | POTELIGEO 4 mg/mL, solution à diluer pour perfusion | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 83 interactions répertoriées. Parmi celles présentées, les plus importantes sont de niveau **majeur** avec le défériprone, le samarium (153Sm) lexidronam, l'adalimumab et le baricitinib. Des interactions de niveau modéré concernent notamment l'alemtuzumab, l'azathioprine, l'anakinra, le canakinumab, l'alefacept, le roflumilast, le chloramphénicol, la zidovudine, le chlorure de strontium Sr-89 et certains vaccins (anthrax, anatoxine tétanique). Les interactions avec les sels de zinc sont de niveau mineur. Globalement, il s'agit surtout d'associations avec des immunosuppresseurs ou des agents myélosuppresseurs.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication, avec un mécanisme spéculatif.
- L'AMM française est annulée et les mises en garde et contre-indications de la notice sont indisponibles, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde et contre-indications) pour permettre le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Vérifier l'expression de CCR4 et la présence de Treg dans les tumeurs urothéliales (études précliniques)
- Rechercher des études publiées ou en cours sur l'anti-CCR4 dans les cancers urothéliaux
- Clarifier le statut réglementaire actuel du produit en France (AMM annulée)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

