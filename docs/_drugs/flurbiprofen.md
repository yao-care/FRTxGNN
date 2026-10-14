---
layout: default
title: Flurbiprofen
parent: Prédiction du modèle uniquement (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
---

# Flurbiprofen
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

# Flurbiprofène : De la Polyarthrite Rhumatoïde à la Dysplasie Acromésomélique de type Hunter-Thompson

## Résumé en Une Phrase

Le flurbiprofène est un anti-inflammatoire non stéroïdien (AINS) utilisé à l'origine dans les maladies rhumatismales : polyarthrite rhumatoïde, arthrose et arthropathies.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **dysplasie acromésomélique de type Hunter-Thompson**, une maladie génétique rare du squelette.
Aucun essai clinique ni aucune publication ne soutient actuellement cette prédiction (**0 essai clinique, 0 publication**) : elle repose uniquement sur le modèle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Polyarthrite rhumatoïde, arthrose, arthropathies (d'après le graphe de connaissances, car aucun texte d'indication d'AMM n'est disponible) |
| Nouvelle Indication Prédite | Dysplasie acromésomélique de type Hunter-Thompson |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 7 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. Le flurbiprofène est un inhibiteur non sélectif des cyclo-oxygénases (COX-1 et COX-2). Il réduit la production de prostaglandines, ce qui explique son effet anti-inflammatoire et antalgique dans les rhumatismes.

Pour cette prédiction précise, **aucun lien mécanistique plausible n'a pu être établi**. La dysplasie acromésomélique de type Hunter-Thompson est une dysplasie squelettique génétique rare, liée à la voie CDMP1/GDF5. Le flurbiprofène n'a pas d'action connue sur la signalisation BMP/GDF5, et l'inhibition des COX ne corrige pas une anomalie du développement du squelette.

Le score élevé du modèle reflète probablement un artefact du graphe de connaissances, dû à des annotations de phénotypes squelettiques et articulaires communes avec les indications d'origine. Il ne constitue pas une preuve d'efficacité.

**Note :** parmi les dix premières prédictions, la seule qui s'appuie sur de la littérature est la **spondylarthrite ankylosante** (rang 8, niveau L3). Elle correspond à une extension au sein de la même classe d'AINS, avec des essais comparatifs anciens (1974-1986) contre l'indométacine, la phénylbutazone et le naproxène, qui montrent une efficacité comparable. Elle mériterait une évaluation distincte.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les sept AMM du flurbiprofène sont annulées. Les textes d'indication approuvée ne sont pas disponibles pour ces AMM.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 64161831 | CEBUTID 50 mg, comprimé enrobé | Comprimé enrobé | Annulée |
| 66565705 | OCUFEN 0,12 mg/0,4 ml, collyre en récipient unidose | Collyre | Annulée |
| 61032482 | ANTADYS 100 mg, comprimé pelliculé | Comprimé pelliculé | Annulée |
| 65407780 | STREFEN 8,75 mg, pastille | Pastille | Annulée |
| 67184116 | CEBUTID 100 mg, comprimé enrobé | Comprimé enrobé | Annulée |

Deux autres AMM annulées ne figurent pas dans ce tableau : STREFEN 8,75 mg orange sans sucre (pastille) et CEBUTID LP 200 mg (gélule à libération prolongée).

---

## Considérations de Sécurité

- **Contre-indications (issues du graphe de connaissances, et non du texte de la notice)** : hypertension artérielle, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, ulcère gastroduodénal (y compris évolutif), infarctus du myocarde, thrombose coronaire, maladie cardiovasculaire et cardiopathie, troubles de la coagulation, hémoglobinopathie, abus ou dépendance à des substances.
- **Interactions médicamenteuses** : 352 interactions sont recensées. Parmi celles listées, la plupart sont de niveau modéré : acide acétylsalicylique, corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, budésonide), metformine, sulfamides hypoglycémiants (glimépiride, chlorpropamide), mésalazine, balsalazide, aprépitant, citrate et bicarbonate de potassium. Les interactions avec la famotidine, la cimétidine et le linaclotide sont de niveau mineur.

Les mises en garde du texte officiel de la notice n'étant pas disponibles, veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique, sans publication ni mécanisme plausible. Le score élevé semble être un artefact du graphe de connaissances.
- Les AMM françaises sont toutes annulées, et le profil de risque des AINS (digestif, rénal, cardiovasculaire) n'est pas justifié par un bénéfice attendu.

**Pour avancer, les éléments suivants sont nécessaires :**
- Des données sur le mécanisme d'action du flurbiprofène et sur un éventuel lien avec la voie GDF5/BMP.
- Des données précliniques ou des cas cliniques étayant un effet dans cette dysplasie.
- Les mises en garde et contre-indications officielles de la notice de l'ANSM.
- Une évaluation séparée de la spondylarthrite ankylosante, indication la mieux étayée par la littérature parmi les prédictions.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

