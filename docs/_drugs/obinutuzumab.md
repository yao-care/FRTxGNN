---
layout: default
title: Obinutuzumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 550
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Obinutuzumab : nouvelle indication prédite, LLC / lymphome lymphocytique à petites cellules avec hypermutation so… (niveau de preuve L5). Indication d'origine : Leucémie lymphoblastique aiguë, syndro…"
---

# Obinutuzumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

## Obinutuzumab : De la leucémie lymphoblastique aiguë à la leucémie lymphoïde chronique / lymphome lymphocytique à petites cellules (sous-type avec hypermutation somatique IGHV)
{: .text-alpha }

## Résumé en Une Phrase

Obinutuzumab est un anticorps monoclonal anti-CD20. Selon le graphe de connaissances utilisé par le modèle, il est associé à la leucémie lymphoblastique aiguë et au syndrome de Richter.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **leucémie lymphoïde chronique / lymphome lymphocytique à petites cellules avec hypermutation somatique des gènes IGHV**.
Pour ce sous-type précis, **aucun essai clinique ni publication** ne soutient actuellement la prédiction, qui repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Leucémie lymphoblastique aiguë, syndrome de Richter (d'après le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | LLC / lymphome lymphocytique à petites cellules avec hypermutation somatique IGHV |
| Score de Prédiction TxGNN | 99,21 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM abrogées (aucune AMM valide) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, l'obinutuzumab est un anticorps dirigé contre l'antigène CD20 des lymphocytes B. Les cellules de LLC et de lymphome lymphocytique à petites cellules expriment CD20, ce qui rend une activité mécanistiquement plausible.

Il faut toutefois nuancer. La LLC est une catégorie de maladie plus large, et le sous-type IGHV muté n'en est qu'une subdivision. Il ne s'agit donc pas vraiment d'une cible de repositionnement nouvelle. Le modèle attribue d'ailleurs exactement le même score (99,21 %) au sous-type « LLC/lymphome lymphocytique à petites cellules prégerminal ». Les deux nœuds de l'ontologie sont probablement très proches, voire dupliqués. Aucune donnée fournie ne permet d'affirmer une efficacité spécifique à un sous-type.

Les données compilées contiennent aussi une prédiction pour le **lymphome folliculaire** (score 99,18 %), beaucoup mieux documentée. Elle est détaillée dans la conclusion.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour ce sous-type de LLC/lymphome lymphocytique à petites cellules.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour ce sous-type.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61042996 | GAZYVARO 1000 mg (ROCHE REGISTRATION) | Solution à diluer pour perfusion | Non précisée ; AMM abrogée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Immunothérapie (anticorps monoclonal anti-CD20, glycoingénieré de type II) |
| Risque de Myélosuppression | Non documenté dans les données compilées ; des cytopénies (neutropénie, thrombopénie) sont décrites avec cette classe, notamment en association à la chimiothérapie |
| Classification d'Émétogénicité | Faible (selon la catégorie du médicament) |
| Éléments de Surveillance | NFS avec formule, fonction hépatique (dont statut vis-à-vis du virus de l'hépatite B), réactions à la perfusion, infections |
| Protection de Manipulation | Médicament non cytotoxique conventionnel ; veuillez consulter la notice et les recommandations locales de manipulation des antinéoplasiques |

## Considérations de Sécurité

Les mises en garde et contre-indications de la notice ne sont pas disponibles dans les données compilées.

- **Interactions Médicamenteuses** : 81 interactions sont répertoriées, dont 20 détaillées ici.
  - **Majeures** : déféripone, samarium (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribine, clozapine.
  - **Modérées** : strontium-89, roflumilast, chloramphénicol, zidovudine, alemtuzumab, azathioprine, anakinra, canakinumab, aléfacept, ainsi que plusieurs vaccins (tétanos, charbon, choléra vivant).
  - **Interprétation** : ces interactions concernent surtout des agents myélosuppresseurs ou immunosuppresseurs et des vaccins, ce qui impose une vigilance sur le risque infectieux et hématologique.

Veuillez consulter la notice pour les autres informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Pour le sous-type IGHV muté de la LLC/lymphome lymphocytique à petites cellules, la prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication spécifique.
- Le statut réglementaire français (AMM unique abrogée) et l'absence de données de notice limitent aussi toute décision.

**Pour avancer, les éléments suivants sont nécessaires :**
- **Lymphome folliculaire.** C'est la prédiction la mieux documentée dans les données compilées : niveau L1, recommandation « Proceed with Guardrails ». Elle s'appuie sur des essais randomisés de phase 3 (étude GALLIUM, publiée dans NEJM 2017, J Clin Oncol 2018 et HemaSphere 2023). Elle s'appuie aussi sur l'étude de phase 2 randomisée ROSEWOOD (zanubrutinib + obinutuzumab) et sur de nombreux essais en cours ou terminés. Il s'agit probablement d'une indication déjà établie plutôt que d'un vrai repositionnement. Cette prédiction devrait faire l'objet d'une évaluation distincte.
- Vérifier l'incohérence apparente des données : indications d'origine (leucémie lymphoblastique aiguë, syndrome de Richter) et AMM abrogée, alors que l'usage dans le lymphome folliculaire et la LLC est connu. Le statut réglementaire actuel doit être confirmé auprès de l'ANSM.
- Récupérer le texte de la notice (mises en garde, contre-indications) auprès de l'ANSM.
- Compléter les données sur le mécanisme d'action.
- Rechercher des données cliniques spécifiques au sous-type IGHV (mutation ou non) de la LLC.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

