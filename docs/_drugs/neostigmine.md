---
layout: default
title: Neostigmine
parent: Prédiction du modèle uniquement (L5)
nav_order: 531
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Neostigmine : nouvelle indication prédite, Myasthénie grave avec hyperplasie du thymus (niveau de preuve L5). Indication d'origine : Myasthénie grave"
monitor_inn: "neostigmine"
predicted_indications: ["autoimmune disease of peripheral nervous system", "disease of receptor activity", "hypersplenism (disease)", "atypical hemolytic-uremic syndrome with B factor anomaly", "bronchitis", "fetal akinesia deformation sequence", "myasthenia, congenital, refractory to acetylcholinesterase inhibitors"]
---

# Neostigmine
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

## Néostigmine : De la myasthénie grave à la myasthénie grave avec hyperplasie du thymus
{: .text-alpha }

## Résumé en Une Phrase

La néostigmine est un inhibiteur réversible de l'acétylcholinestérase, initialement utilisé pour traiter la myasthénie grave et les maladies de la jonction neuromusculaire.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **myasthénie grave avec hyperplasie du thymus**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette indication précise.
Il s'agit donc d'une prédiction fondée uniquement sur le modèle, plus proche d'un sous-type d'une indication existante que d'un véritable repositionnement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Myasthénie grave (indication issue du graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Myasthénie grave avec hyperplasie du thymus |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement AMM annulée (non commercialisé) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les sources compilées. Sur la base des connaissances pharmacologiques établies, la néostigmine inhibe l'acétylcholinestérase, ce qui augmente l'acétylcholine disponible au niveau de la jonction neuromusculaire. Cela compense en partie la réduction des récepteurs fonctionnels observée dans la myasthénie grave.

L'hyperplasie du thymus est un sous-type fréquent de myasthénie grave. Le mécanisme symptomatique est donc le même que pour l'indication d'origine, et la prédiction est cohérente avec ce mécanisme. Le score élevé reflète toutefois la proximité dans le graphe de connaissances avec l'indication connue, et non une preuve clinique indépendante.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour cette indication.

*Pour information, parmi les autres indications prédites, la littérature disponible reste très majoritairement mécanistique, animale ou composée de cas isolés (par exemple, une revue sur les présentations inhabituelles de la myasthénie grave pour la forme des ceintures, PMID 27854225). Aucune ne fournit de données d'efficacité contrôlées propres à la néostigmine.*

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61601542 | PROSTIGMINE 0,5 mg/1 ml, solution injectable (VIATRIS MEDICAL) | Solution injectable | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : épilepsie, ulcère gastroduodénal, asthme (y compris intrinsèque et allergique), arrêt cardiaque soudain, maladie de la conduction cardiaque, péritonite, hyperthyroïdie (maladie de Basedow, thyrotoxicose), obstruction des voies urinaires, maladie de Hirschsprung et syndromes apparentés (dont le syndrome de Mowat-Wilson).
- **Interactions médicamenteuses** : 47 interactions recensées. Parmi celles qui sont listées, une est de niveau **majeur** (bupropion). Les autres sont de niveau modéré, notamment :
  - les corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, budésonide) ;
  - les anticholinergiques (atropine, hyoscyamine, glycopyrronium, dicyclomine, trospium, méthscopolamine, clidinium, mépenzolate) ;
  - les aminosides (néomycine, kanamycine, paromomycine) ;
  - certains agents de préparation colique (acide picosulfurique, polyéthylène glycol, sulfate de sodium).
- **Points de vigilance liés aux autres prédictions** : l'inhibition de la cholinestérase est mécanistiquement défavorable dans la bronchite (augmentation des sécrétions et bronchoconstriction). Elle est aussi potentiellement nocive dans certains syndromes myasthéniques congénitaux.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication spécifiques au sous-type. Elle concerne une indication déjà couverte par l'usage existant de la néostigmine.
- L'unique AMM française est annulée et les données de sécurité de la notice sont absentes (lacune bloquante pour la sélection de sécurité).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications officielles).
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Vérifier si la myasthénie grave avec hyperplasie du thymus constitue réellement une nouvelle indication ou un simple sous-type de l'indication existante.
- Clarifier la situation réglementaire actuelle (AMM annulée, disponibilité d'autres présentations).
- Pour la suite de l'évaluation, les autres candidats ayant un niveau de preuve plus avancé (par exemple la myasthénie néonatale, L4, au stade « question de recherche ») nécessiteraient une évaluation dédiée de la posologie et de la sécurité chez le nouveau-né.
- Ne pas poursuivre les prédictions jugées probablement fausses (par exemple la myasthénie congénitale réfractaire aux inhibiteurs de l'acétylcholinestérase, l'hypersplénisme, le syndrome hémolytique et urémique atypique).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

