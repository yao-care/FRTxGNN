---
layout: default
title: Digoxin
parent: Prédiction du modèle uniquement (L5)
nav_order: 241
evidence_level: L5
indication_count: 6
---

# Digoxin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

# Digoxine : De la fibrillation auriculaire à l'angor de Prinzmetal

## Résumé en Une Phrase

La digoxine est un glycoside cardiotonique, initialement utilisé pour traiter la fibrillation auriculaire et l'intoxication digitalique.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**angor de Prinzmetal**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction issue du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Fibrillation auriculaire ; intoxication digitalique (selon le graphe de connaissances, le texte d'indication des AMM n'étant pas renseigné) |
| Nouvelle Indication Prédite | Angor de Prinzmetal |
| Score de Prédiction TxGNN | 99,81 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 4 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, la digoxine inhibe la pompe Na+/K+-ATPase, ce qui augmente le calcium intracellulaire et renforce la contractilité myocardique, tout en ralentissant la conduction auriculo-ventriculaire. Ce mécanisme explique son usage dans la fibrillation auriculaire.

Le lien avec l'angor de Prinzmetal est en revanche **spéculatif**. Cet angor est dû à un vasospasme coronarien, habituellement traité par des inhibiteurs calciques et des dérivés nitrés. L'augmentation du calcium intracellulaire induite par la digoxine n'est pas évidemment compatible avec cette indication, et un effet vasoconstricteur potentiel pourrait même être défavorable.

Le score TxGNN très élevé (0,998) reflète une proximité dans le graphe de connaissances, et non une preuve clinique ou mécanistique. Les autres prédictions du modèle (obstruction duodénale, ulcère duodénal, reflux duodéno-gastrique, hypoalphalipoprotéinémie, ainsi qu'un terme obsolète de susceptibilité à l'AVC ischémique) ne présentent pas non plus de lien plausible identifié et ne sont pas développées ici.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'angor de Prinzmetal.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65458013 | DIGOXINE NATIVELLE ADULTES 0,50 mg/2 ml, solution injectable IV (annulée) | Solution injectable | Non renseignée |
| 63593820 | HEMIGOXINE NATIVELLE 0,125 mg, comprimé (annulée) | Comprimé | Non renseignée |
| 61917063 | DIGOXINE NATIVELLE 5 microgrammes/0,1 ml, solution buvable en gouttes (annulée) | Solution buvable en gouttes | Non renseignée |
| 67681303 | DIGOXINE NATIVELLE 0,25 mg, comprimé (annulée) | Comprimé | Non renseignée |

Les quatre AMM, détenues par TEOFARMA, sont annulées ; aucune AMM valide n'est recensée.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : insuffisance rénale, hypokaliémie, hypercalcémie, néphrocalcinose, troubles du métabolisme du phosphore, infarctus du myocarde, thrombose coronarienne, hémoglobinopathie, cœur pulmonaire, syndrome de Wolff-Parkinson-White, maladie du sinus (y compris familiale), fibrillation ventriculaire, cardiomyopathie hypertrophique (y compris familiale), bloc auriculo-ventriculaire, myxœdème et hypothyroïdie (y compris congénitale), myocardite, péricardite constrictive, cardiomyopathie restrictive, pyouretère.
- **Interactions médicamenteuses** : 304 interactions recensées. Parmi les exemples de niveau modéré : acarbose, rabéprazole, doxycycline, épinéphrine, hydrocortisone, cholécalciférol, metformine, amphotéricine B, bupropion, triamcinolone, acide acétylsalicylique, dexaméthasone, bétaméthasone, tétracycline, phosphate de calcium. Niveau mineur : albiglutide, hyoscyamine, atropine, glycopyrronium.

Les mises en garde et contre-indications issues de la notice ANSM n'ont pas pu être obtenues. Veuillez consulter la notice pour les informations de sécurité complètes. La digoxine a un index thérapeutique étroit ; un suivi de la kaliémie, de la fonction rénale et de la digoxinémie est classiquement requis.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, avec un lien mécanistique peu plausible et un risque potentiel de vasoconstriction. Aucune AMM valide n'existe en France, et les données de sécurité issues de la notice sont manquantes, ce qui empêche l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications)
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Mener une revue de la littérature ciblée sur la digoxine et le vasospasme coronarien, et rechercher d'éventuels essais
- Examiner la pertinence mécanistique au regard des traitements de référence (inhibiteurs calciques, dérivés nitrés)
- Clarifier le statut réglementaire, toutes les AMM étant annulées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

