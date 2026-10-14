---
layout: default
title: Temsirolimus
parent: Prédiction du modèle uniquement (L5)
nav_order: 736
evidence_level: L5
indication_count: 3
---

# Temsirolimus
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

# Temsirolimus : Du Carcinome Rénal et du Lymphome du Manteau au Liposarcome

## Résumé en Une Phrase

Le temsirolimus est un inhibiteur de mTOR, initialement utilisé pour le traitement du carcinome rénal et du lymphome à cellules du manteau.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **liposarcome**, avec **2 essais cliniques** (phases 1/2 et 2) et **1 publication** (une revue) soutenant actuellement cette direction.
Ces preuves restent indirectes : aucune étude ne porte spécifiquement sur le liposarcome.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carcinome rénal à cellules claires, lymphome à cellules du manteau (texte d'indication de l'AMM française non renseigné) |
| Nouvelle Indication Prédite | Liposarcome |
| Score de Prédiction TxGNN | 99,54 % |
| Niveau de Preuve | L4 (voir note ci-dessous) |
| Statut de Marché en France | ✗ AMM abrogée/annulée uniquement |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

*Note sur le niveau de preuve : l'évaluation initiale attribuait L2, mais aucun essai de phase 2/3 terminé ne cible spécifiquement le liposarcome. Les deux essais sont de populations mixtes (sarcomes des tissus mous et des os, ou tumeurs solides pédiatriques) et la seule publication est une revue. D'après les règles de détermination, le niveau retenu ici est plutôt L4 (preuves précliniques/mécanistiques et essais indirects).*

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées. Sur la base des connaissances générales, le temsirolimus est un analogue de la rapamycine qui inhibe mTOR, une kinase centrale de la croissance et de la prolifération cellulaires. Son efficacité a été établie dans le carcinome rénal avancé et le lymphome à cellules du manteau.

La voie PI3K/AKT/mTOR est fréquemment activée dans les sarcomes des tissus mous. Dans les liposarcomes bien différenciés et dédifférenciés, amplifiés pour MDM2/CDK4, une dépendance aux signaux mTOR et IGF-1R a été évoquée. Cela fournit une justification mécanistique plausible, et l'association avec le cixutumumab (anti-IGF-1R) cible l'amont du même axe.

Le score TxGNN élevé (0,995) est cohérent avec ce lien au niveau de la voie, mais il s'agit d'une prédiction computationnelle et non d'une preuve clinique. Les deux autres prédictions (liposarcome myxoïde ovarien, sarcome vulvaire) ne reposent sur aucune donnée clinique ni bibliographique et sont purement spéculatives. Le liposarcome myxoïde est en général porté par la fusion FUS-DDIT3, et sa dépendance à mTOR n'est pas établie.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Terminé | 24 | Temsirolimus + doxorubicine liposomale dans les sarcomes avancés des tissus mous et des os : recherche d'un schéma posologique sûr, puis évaluation de l'efficacité. Population mixte, efficacité spécifique au liposarcome non confirmée. |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Terminé | 46 | Cixutumumab + temsirolimus chez des patients pédiatriques atteints de tumeurs solides récidivantes ou réfractaires (dont sarcomes). Applicabilité limitée au liposarcome de l'adulte, rare chez l'enfant. |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Revue | Bulletin du cancer | Traitements ciblés des tumeurs conjonctives rares et des sarcomes, selon six sous-groupes moléculaires (translocations avec gènes de fusion, mutations de tyrosine kinases, etc.). Pertinence pour le temsirolimus dans le liposarcome non évaluée. |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60443413 (abrogée) | TORISEL 30 mg, solution à diluer et solvant pour solution pour perfusion | Solution à diluer et solvant pour solution pour perfusion | Non renseignée |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de mTOR) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter la notice ; au vu des contre-indications issues du graphe de connaissances, une surveillance de la glycémie, du bilan lipidique, de la fonction hépatique et rénale et de la fonction pulmonaire est à envisager |
| Protection de Manipulation | Veuillez consulter la notice |

---

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées pour ce rapport. Veuillez consulter la notice pour ces informations.

- **Contre-indications issues du graphe de connaissances** (à titre indicatif, il ne s'agit pas du texte de la notice) : maladie rénale, maladie hépatique, maladie de la vésicule biliaire, hyperglycémie, diabète et acidocétose diabétique, hyperlipidémie (dont familiale), accident vasculaire cérébral et troubles cérébrovasculaires, hyperbilirubinémie (dont syndrome de Gilbert), pneumopathie interstitielle, ainsi que diverses tumeurs cérébrales (astrocytomes, glioblastome à cellules géantes, tumeurs oligodendrogliales, etc.).
- **Interactions médicamenteuses** : 100 interactions recensées, dont les principales de niveau **majeur** :
  - amphotéricine B (et sa forme complexe lipidique)
  - dexaméthasone
  - clarithromycine

  Des interactions de niveau **modéré** existent notamment avec les antidiabétiques (acarbose, albiglutide, alogliptine, metformine, pioglitazone, canagliflozine, dapagliflozine, chlorpropamide), les corticoïdes (hydrocortisone, triamcinolone, bétaméthasone, budésonide), l'aprépitant, la cimétidine, la mésalazine et le balsalazide.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le lien mécanistique via mTOR est plausible, mais aucun essai ne cible spécifiquement le liposarcome, et la seule publication est une revue générale. La seule AMM française est abrogée et les données de sécurité issues de la notice manquent, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice (mises en garde et contre-indications) depuis le site de l'ANSM
- Données détaillées sur le mécanisme d'action (DrugBank)
- Résultats publiés de NCT00949325 avec analyse du sous-groupe liposarcome
- Études ciblant spécifiquement le liposarcome (en particulier MDM2/CDK4-amplifié), idéalement de phase 2
- Évaluation de la faisabilité de la voie d'administration (perfusion intraveineuse) et de l'accès au médicament en France, compte tenu de l'abrogation de l'AMM
- Plan de surveillance de la sécurité tenant compte des comorbidités métaboliques, hépatiques, rénales et pulmonaires
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

