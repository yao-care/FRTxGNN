---
layout: default
title: Cemiplimab
parent: Prédiction du modèle uniquement (L5)
nav_order: 153
evidence_level: L5
indication_count: 10
---

# Cemiplimab
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

# Cemiplimab : Du Carcinome Épidermoïde au Carcinome Adénosquameux de la Vésicule Biliaire

## Résumé en Une Phrase

Cemiplimab est un anticorps anti-PD-1, initialement utilisé pour le traitement du carcinome épidermoïde (carcinome épidermoïde cutané).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **carcinome adénosquameux de la vésicule biliaire**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carcinome épidermoïde (le texte d'indication de l'AMM n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Carcinome adénosquameux de la vésicule biliaire |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Annulée uniquement (AMM annulée) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier compilé pour ce rapport. D'après les données de pharmacologie, cemiplimab est un anticorps dirigé contre la cible PD-1 (PDCD1, CD279) humaine. Il bloque l'interaction PD-1/PD-L1 avec une IC50 inférieure à 1 nM lors d'un test ELISA. Son efficacité dans le carcinome épidermoïde cutané avancé a été démontrée : environ 50 % des patients ont répondu au traitement, avec des réponses durables chez 82 % des répondeurs ayant une maladie métastatique.

La composante épidermoïde (squameuse) de ce rare carcinome adénosquameux de la vésicule biliaire pourrait partager la biologie de l'axe PD-1/PD-L1. Cette hypothèse reste toutefois **non testée** : l'expression de PD-L1 ainsi que le statut MSI/TMB de cette tumeur sont inconnus.

La prédiction repose donc uniquement sur le score du modèle et sur une similarité histologique plausible, sans aucune preuve clinique ou publiée dans les données fournies.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Autres Indications Prédites (pour information)

| Rang | Maladie prédite | Score TxGNN | Niveau de preuve | Recommandation |
|------|------|------|------|------|
| 2 | Carcinome épidermoïde de la glotte | 99,99 % | L5 | Hold |
| 3 | Carcinome cloacogénique du rectum | 99,99 % | L5 | Hold |
| 4 | Carcinome basocellulaire de l'oreille externe | 99,99 % | L4 | Question de recherche |
| 5 | Carcinome adénosquameux de la prostate | 99,99 % | L5 | Hold |
| 6 | Carcinome verruqueux de l'urètre | 99,99 % | L5 | Hold |
| 7 | Carcinome épidermoïde occulte du poumon | 99,99 % | L5 | Hold |
| 8 | Carcinome adénosquameux du pancréas | 99,99 % | L5 | Hold |
| 9 | Carcinome épidermoïde sinonasal non kératinisant | 99,99 % | L5 | Hold |
| 10 | Carcinome épidermoïde de la supraglotte | 99,99 % | L5 | Hold |

Le seul élément de littérature disponible concerne le carcinome basocellulaire de l'oreille externe (rang 4) : un rapport de cas de 2021 ([PMID 34157152](https://pubmed.ncbi.nlm.nih.gov/34157152/), *Clinical and Experimental Dermatology*) décrivant une réponse durable après l'arrêt de cemiplimab chez un patient atteint d'un carcinome basocellulaire localement avancé. Il s'agit d'une observation individuelle ; la localisation à l'oreille ne peut pas être confirmée à partir des données fournies.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61660291 | LIBTAYO 350 mg, solution à diluer pour perfusion (REGENERON IRELAND DESIGNATED ACTIVITY COMPANY, Irlande) | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Immunothérapie (anticorps anti-PD-1) |
| Risque de Myélosuppression | Faible (pas de cytotoxicité conventionnelle) ; aucune donnée de toxicité détaillée disponible |
| Classification d'Émétogénicité | Faible |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 9 interactions de niveau modéré sont signalées, toutes avec des corticostéroïdes : hydrocortisone, triamcinolone, dexaméthasone, bétaméthasone, budésonide, prednisolone, prednisone, méthylprednisolone et déflazacort. Ces associations sont à examiner avec attention, car les corticostéroïdes peuvent réduire l'effet d'une immunothérapie.

Les mises en garde principales et les contre-indications issues de la notice ne sont pas disponibles dans les données compilées pour ce rapport. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour le carcinome adénosquameux de la vésicule biliaire repose uniquement sur le score du modèle (niveau L5) : aucun essai clinique ni publication n'est disponible. De plus, la seule AMM française de ce médicament est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), actuellement bloquant pour le dépistage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Rechercher des essais cliniques et des publications spécifiques à cette tumeur rare
- Caractériser l'expression de PD-L1 et le statut MSI/TMB dans ce type tumoral
- Clarifier la situation réglementaire en France (AMM annulée) et la disponibilité effective du produit
- Pour le carcinome basocellulaire (rang 4), vérifier les données d'essais hors du périmètre fourni avant toute réévaluation du niveau de preuve
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

