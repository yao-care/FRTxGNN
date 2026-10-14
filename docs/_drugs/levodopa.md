---
layout: default
title: Levodopa
parent: Prédiction du modèle uniquement (L5)
nav_order: 449
evidence_level: L5
indication_count: 1
---

# Levodopa
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Levodopa : De la maladie de Parkinson à l'encéphalite de Rasmussen

## Résumé en Une Phrase

Levodopa est un précurseur de la dopamine, utilisé à l'origine dans le traitement de la **maladie de Parkinson** et des syndromes parkinsoniens apparentés.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**encéphalite subaiguë de Rasmussen**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction issue du modèle uniquement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie de Parkinson (d'après le graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Encéphalite subaiguë de Rasmussen |
| Score de Prédiction TxGNN | 99,06 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Toutes les AMM sont annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la levodopa est un précurseur de la dopamine, généralement associé à un inhibiteur de la décarboxylase (carbidopa ou bensérazide) et parfois à l'entacapone. Son efficacité dans la maladie de Parkinson est établie : elle compense le déficit en dopamine dans les voies nigrostriatales.

L'encéphalite de Rasmussen est une maladie inflammatoire cérébrale rare, généralement unilatérale, à médiation lymphocytaire T. Elle provoque une épilepsie focale pharmacorésistante, une atrophie progressive d'un hémisphère et un déficit neurologique. Le lien avec l'indication d'origine reste hypothétique : le modèle a pu rapprocher les deux maladies par des phénotypes neurologiques communs (troubles moteurs, atteinte des noyaux gris centraux, hémiparésie ou hémiatrophie, comme dans le syndrome d'hémiparkinsonisme-hémiatrophie).

Aucun lien mécanistique direct n'est étayé par les données compilées pour ce rapport. La levodopa n'agit pas sur la pathologie immunitaire (attaque des neurones et des astrocytes par les lymphocytes T CD8+) ni sur le contrôle des crises, qui sont les moteurs de la maladie. Le score élevé du modèle ne doit donc pas être interprété comme une preuve d'efficacité.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les 20 AMM recensées sont au statut **annulé** ; aucune n'est actuellement valide. Le texte d'indication approuvée n'est pas disponible dans les données compilées. Les 5 premières AMM sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|---------|------|------|------|------|
| 69606865 | SINEMET 100 mg/10 mg | Comprimé | Organon France | Annulée |
| 60660790 | Levodopa/Bensérazide Teva 200 mg/50 mg | Gélule | Teva Santé | Annulée |
| 64793585 | Levodopa Carbidopa Teva LP 100 mg/25 mg | Comprimé à libération prolongée | Teva Santé | Annulée |
| 61721132 | Levodopa Carbidopa Teva 250 mg/25 mg | Comprimé sécable | Teva Santé | Annulée |
| 66818261 | SINEMET LP 100 mg/25 mg | Comprimé à libération prolongée | Organon France | Annulée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : atrophie multisystématisée, syndrome de tachycardie orthostatique posturale, hypotension orthostatique, dyskinésie d'origine médicamenteuse, épilepsie, ulcère gastrique et ulcère peptique, troubles anxieux et névrotiques, dysthymie, maladie rénale, pyo-uretère, maladie hépatique, maladie de la vésicule biliaire, glaucome à angle ouvert et à angle fermé, troubles psychotiques (schizophréniforme, schizoaffectif, trouble mental), diabète et acidocétose diabétique, mélanome, infarctus du myocarde et thrombose coronaire, hémoglobinopathie, maladie diarrhéique, arrêt cardiaque soudain, maladie de la conduction cardiaque.
  - **Point d'attention particulier** : l'épilepsie figure parmi ces contre-indications, alors que l'encéphalite de Rasmussen se manifeste précisément par une épilepsie focale intractable.
- **Interactions médicamenteuses** : 104 interactions recensées. Parmi celles listées :
  - Niveau modéré : épinéphrine, éphédrine, bupropion, métronidazole, pyridoxine, fer, métoclopramide, et anticholinergiques (atropine, hyoscyamine, méthscopolamine, glycopyrronium, clidinium, dicyclomine, mépenzolate).
  - Niveau mineur : antiacides (hydroxyde d'aluminium, carbonate de calcium, magaldrate, sels de magnésium).

Les mises en garde et contre-indications issues des notices ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et sans lien mécanistique plausible avec une maladie auto-immune et épileptogène. Le signal de sécurité lié à l'épilepsie et l'absence d'AMM valide en France renforcent cette position.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications des notices (source : site de l'ANSM), étape bloquante pour le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Mener une revue de la littérature sur la levodopa et l'encéphalite de Rasmussen ou les syndromes hémiatrophiques apparentés
- Examiner la compatibilité des voies d'administration et clarifier la situation réglementaire (AMM annulées)
- Évaluer, avant toute étude, le risque lié à l'épilepsie chez cette population
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

