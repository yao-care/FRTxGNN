---
layout: default
title: Flavoxate
parent: Prédiction du modèle uniquement (L5)
nav_order: 328
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Flavoxate : nouvelle indication prédite, Attention deficit hyperactivity disorder… (niveau de preuve L5). Indication d'origine : Non renseignée dans l'AMM (texte d'indication vide)"
monitor_inn: "FLAVOXATE"
predicted_indications: ["attention deficit hyperactivity disorder, inattentive type", "irritable bowel syndrome", "specific developmental disorder", "attention deficit-hyperactivity disorder", "cauda equina syndrome", "obsolete neurogenic bladder (disease)", "gastroduodenitis", "peptic ulcer disease"]
---

# Flavoxate
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

## Flavoxate : D'une indication urologique non documentée au Syndrome de l'intestin irritable
{: .text-alpha }

## Résumé en Une Phrase

Le flavoxate est un relaxant des muscles lisses connu pour son usage en urologie (urgences mictionnelles). L'indication d'origine figurant dans l'AMM française n'est pas renseignée dans les données compilées.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de l'intestin irritable** (prédiction la plus cohérente sur le plan mécanistique parmi les 8 candidates), mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans l'AMM (texte d'indication vide) |
| Nouvelle Indication Prédite | Attention deficit hyperactivity disorder, inattentive type (prédiction de rang 1 du modèle) ; voir ci-dessous pour le syndrome de l'intestin irritable, hypothèse la plus plausible |
| Score de Prédiction TxGNN | 99,75 % (rang 1) ; 99,74 % pour le syndrome de l'intestin irritable (rang 2) |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

> Remarque : le titre du rapport retient le syndrome de l'intestin irritable, car c'est la prédiction la plus cohérente sur le plan mécanistique. La prédiction de rang 1 (TDAH, forme inattentive) n'a aucun lien mécanistique établi avec le flavoxate.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la source. D'après les informations connues, le flavoxate est un relaxant des muscles lisses à propriétés antimuscariniques, inhibitrices des phosphodiestérases et antagonistes calciques, utilisé dans les urgences mictionnelles.

Pour le **syndrome de l'intestin irritable**, le raisonnement est plausible : la relaxation spasmolytique et antimuscarinique du muscle lisse est la base de l'usage d'agents apparentés (hyoscine, dicyclomine) dans cette pathologie. Il s'agit toutefois d'une hypothèse, sans aucune donnée clinique propre au flavoxate.

Les autres prédictions sont nettement plus fragiles :
- **TDAH (deux formes) et trouble spécifique du développement** : aucun lien mécanistique établi ; le signal reflète probablement une proximité dans le graphe de connaissances plutôt qu'une pharmacologie réelle. Toute pertinence neurologique serait spéculative.
- **Vessie neurogène** : mécanisme plausible (effet sur le détrusor), mais le terme est marqué comme obsolète dans l'ontologie et devrait être remplacé par un terme actuel (ex. hyperactivité neurogène du détrusor).
- **Ulcère peptique** : un rationnel de classe existe (antimuscariniques utilisés autrefois en appoint), mais ils ont été supplantés par les IPP et l'éradication d'*H. pylori*.
- **Gastroduodénite** : lien faible ; l'action antispasmodique ne traite pas l'inflammation ni la composante acide.
- **Syndrome de la queue de cheval** : lien indirect ; urgence neurochirurgicale, le flavoxate ne pourrait agir que sur les symptômes vésicaux secondaires.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63383409 | URISPAS 200 mg, comprimé pelliculé (BOUCHARA-RECORDATI) | Comprimé pelliculé | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie, et non texte de notice) : glaucome à angle fermé, sténose du pylore, iléus paralytique, occlusion intestinale, myopathie viscérale familiale, ulcère peptique actif, obstruction des voies urinaires.
  - À noter : l'ulcère peptique actif figure parmi ces contre-indications, ce qui va à l'encontre de la prédiction « ulcère peptique ».
- **Interactions médicamenteuses** : 74 interactions identifiées.
  - **Majeures** : chlorure de potassium, citrate de potassium.
  - **Modérées** (extraits) : hyoscyamine, atropine, scopolamine, glycopyrronium, clidinium, dicyclomine, trospium, propanthéline (effets anticholinergiques cumulés), lopéramide, morphine, métoclopramide, prucalopride, éluxadoline, dronabinol, nabilone.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Toutes les prédictions reposent uniquement sur le modèle (niveau L5), sans essai ni publication. De plus, l'AMM française est annulée et son indication d'origine n'est pas documentée.
- Le syndrome de l'intestin irritable est l'hypothèse la plus cohérente, mais elle reste à confirmer. Les prédictions neuropsychiatriques (TDAH) ne sont pas étayées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice ANSM (mises en garde et contre-indications), actuellement bloquante pour le criblage de sécurité
- Données sur le mécanisme d'action (via DrugBank)
- Revue de la littérature et des registres d'essais pour le flavoxate dans le syndrome de l'intestin irritable
- Réévaluation de la sécurité à la lumière des contre-indications (obstruction intestinale, ulcère actif) et des effets anticholinergiques cumulés
- Remplacement du terme obsolète « vessie neurogène » par un terme actuel avant toute évaluation
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

