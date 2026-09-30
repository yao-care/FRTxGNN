---
layout: default
title: Nicardipine
parent: Prédiction du modèle uniquement (L5)
nav_order: 212
evidence_level: L5
indication_count: 5
---

# Nicardipine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

# Nicardipine : D'une Indication d'Origine Non Renseignée à l'Hypertension Pulmonaire

## Résumé en Une Phrase

La nicardipine est un inhibiteur calcique de la famille des dihydropyridines, à effet vasodilatateur. Elle est commercialisée en France sous le nom LOXEN, mais le dossier ne précise pas son indication d'origine.
Le modèle TxGNN prédit qu'elle pourrait être utile dans l'**hypertension pulmonaire à mécanisme multifactoriel mal défini**.
Actuellement, **aucun essai clinique** et **aucune publication** ne soutiennent cette piste.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans le dossier (texte d'indication vide pour les 3 AMM) |
| Nouvelle Indication Prédite | Hypertension pulmonaire à mécanisme multifactoriel mal défini |
| Score de Prédiction TxGNN | 99,26 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les connaissances générales, la nicardipine est un inhibiteur calcique de type dihydropyridine, dont l'effet vasodilatateur repose sur le blocage des canaux calciques. Son efficacité dans son indication d'origine n'a pas pu être vérifiée dans ce dossier, car les textes d'indication des AMM sont vides.

Sur le plan mécanistique, une vasodilatation pourrait en théorie agir sur le tonus vasculaire pulmonaire, ce qui rend le lien plausible. Il s'agit toutefois de pharmacologie générale, et rien dans les données fournies ne relie la nicardipine à ce phénotype précis d'hypertension pulmonaire.

Le score élevé de TxGNN (99,26 %) est le seul élément en faveur de cette piste. Il ne remplace pas des données cliniques.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

Pour la deuxième prédiction (hypertension pulmonaire liée à une maladie pulmonaire ou à l'hypoxie), 20 publications ont été recensées. Aucune ne porte sur la nicardipine ni sur l'hypertension pulmonaire : elles traitent de la biologie générale de l'hypoxie (vieillissement cérébral, cognition, signalisation HIF, cancer, altitude). Elles n'apportent donc aucun soutien propre à ce médicament.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65984700 | LOXEN 20 mg, comprimé sécable | Comprimé sécable | Non renseignée |
| 60718902 | LOXEN 10 mg/10 mL, solution injectable (I.V.) | Solution injectable | Non renseignée |
| 69198890 | LOXEN LP 50 mg, gélule à libération prolongée | Gélule à libération prolongée | Non renseignée |

Les trois AMM appartiennent au Laboratoire XO.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai ni publication spécifique à la nicardipine.
- Les données de sécurité de la notice ANSM sont absentes, ce qui bloque le passage à l'étape de sélection de sécurité. Les vasodilatateurs peuvent aussi aggraver l'appariement ventilation-perfusion dans l'hypertension pulmonaire liée aux maladies pulmonaires, un point à clarifier avant toute suite.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications), élément bloquant.
- Obtenir les données de mécanisme d'action (par exemple via l'API DrugBank).
- Confirmer l'indication d'origine à partir des RCP des 3 AMM.
- Réaliser une revue de littérature ciblée sur la nicardipine et l'hypertension pulmonaire.
- Évaluer la compatibilité des voies d'administration (orale et intraveineuse disponibles) avec l'usage envisagé.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

