---
layout: default
title: Temsirolimus
parent: Prédiction du modèle uniquement (L5)
nav_order: 302
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

# Temsirolimus : Vers le Liposarcome

## Résumé en Une Phrase

Le temsirolimus est un inhibiteur de mTOR commercialisé en France (TORISEL, perfusion). Son indication d'origine n'est pas renseignée dans les données fournies.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **liposarcome**,
avec **5 essais cliniques** (dont un seul testant directement le temsirolimus dans une population incluant le liposarcome) et **1 publication** (une revue) à l'appui.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Liposarcome |
| Score de Prédiction TxGNN | 99,54 % |
| Niveau de Preuve | L3 (voir la note ci-dessous) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

*Note sur le niveau de preuve : le dossier source indique L2, mais aucun essai randomisé de Phase 2/3 n'est présent. Les essais disponibles sont des Phases 1/2 et 2, sans randomisation ou sans résultat publié. Nous retenons donc L3.*

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le temsirolimus se lie à FKBP12 et inhibe mTOR, une kinase centrale de la voie PI3K/AKT/mTOR, qui contrôle la croissance et la survie cellulaires. Les données fournies ne décrivent pas son mécanisme d'action. Ce mécanisme provient de la pharmacologie générale, pas du dossier source.

Comme l'indication d'origine n'est pas renseignée, on ne peut pas comparer directement l'ancienne et la nouvelle indication. L'argument repose sur la voie : PI3K/AKT/mTOR est active dans les sarcomes des tissus mous, dont le liposarcome. Le score élevé du modèle (0,995) est cohérent avec cette hypothèse.

Des essais de Phase 2 avec d'autres inhibiteurs de mTOR (ridaforolimus, évérolimus) soutiennent l'hypothèse au niveau de la classe. En revanche, aucun résultat d'efficacité du temsirolimus propre au liposarcome n'est fourni, et il n'existe pas d'essai de Phase 3.

Deux autres indications sont prédites, sans aucune preuve associée : le liposarcome myxoïde de l'ovaire (99,47 %) et le sarcome de la vulve (99,09 %). Elles restent au stade de la prédiction seule (L5, Hold).

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Terminé | 24 | Temsirolimus (Torisel) + doxorubicine liposomale dans les sarcomes avancés des tissus mous et des os. Objectif : définir une posologie sûre, puis évaluer l'efficacité. Le résultat du sous-groupe liposarcome n'est pas fourni. |
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Terminé | 70 | Sirolimus + cyclophosphamide dans le liposarcome myxoïde et le chondrosarcome métastatiques ou non résécables. Étude à bras unique avec un analogue proche, pas le temsirolimus. |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Terminé | 46 | Cixutumumab + temsirolimus dans les tumeurs solides pédiatriques récidivantes ou réfractaires. Population pédiatrique, applicabilité limitée au liposarcome de l'adulte. |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Terminé | 216 | Ridaforolimus (autre inhibiteur de mTOR) dans les sarcomes avancés. Preuve au niveau de la classe, pas pour le temsirolimus. |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Actif, ne recrute plus | 48 | Ribociclib + évérolimus dans le liposarcome dédifférencié et le léiomyosarcome avancés. Histologie concordante, mais l'inhibiteur de mTOR est l'évérolimus. Résultats non disponibles. |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Revue | Bulletin du cancer | Traitements ciblés des tumeurs rares du tissu conjonctif et des sarcomes. Les auteurs distinguent six sous-groupes de sarcomes selon leurs altérations moléculaires spécifiques. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 60443413 | TORISEL 30 mg | Solution à diluer et solvant pour solution pour perfusion | PFIZER EUROPE MA EEIG (Belgique) |

Le texte de l'indication approuvée n'est pas disponible dans le dossier ANSM fourni.

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de mTOR) |
| Autres paramètres (myélosuppression, émétogénicité, surveillance, manipulation) | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun résultat d'efficacité du temsirolimus propre au liposarcome n'est disponible. Le seul essai testant directement le médicament dans cette population est petit (24 patients) et sans résultat par sous-groupe.
- Les mises en garde et contre-indications de la notice ANSM manquent. C'est un écart bloquant pour l'examen de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications)
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via l'API DrugBank)
- Obtenir les résultats du sous-groupe liposarcome de l'essai NCT00949325
- Suivre les résultats de l'essai NCT03114527 (évérolimus, liposarcome dédifférencié)
- Renseigner l'indication d'origine du produit pour analyser le lien avec la nouvelle indication

*Ces résultats sont fournis à titre de recherche et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

