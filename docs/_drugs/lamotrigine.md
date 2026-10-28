---
layout: default
title: Lamotrigine
parent: Prédiction du modèle uniquement (L5)
nav_order: 433
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
monitor_inn: "LAMOTRIGINE"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia"]
description: "Lamotrigine : nouvelle indication prédite, Néoplasme du nerf trijumeau (trigeminal nerve neoplasm) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Lamotrigine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Lamotrigine: Néoplasme du nerf trijumeau (trigeminal nerve neoplasm)
{: .text-alpha }

## Résumé en Une Phrase

La lamotrigine est un antiépileptique utilisé à l'origine pour traiter l'épilepsie (notamment les épilepsies partielles et le syndrome de Lennox-Gastaut).
Le modèle TxGNN la prédit comme potentiellement efficace pour le **néoplasme du nerf trijumeau**, avec un score très élevé.
**Aucun essai clinique** et **aucune publication portant sur le traitement tumoral** ne soutiennent cette direction : les deux articles retrouvés concernent la névralgie du trijumeau, pas la tumeur.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Néoplasme du nerf trijumeau (trigeminal nerve neoplasm) |
| Score de Prédiction TxGNN | 0.9997 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 19) |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances pharmacologiques établies, la lamotrigine bloque les canaux sodiques voltage-dépendants et réduit la libération de glutamate. Son efficacité dans l'épilepsie est reconnue. Ce mécanisme peut soulager certaines douleurs neuropathiques.

Le score élevé provient du modèle TxGNN (apprentissage profond) et peut refléter des similitudes apprises par le modèle entre maladies voisines, notamment avec la **névralgie du trijumeau**, pour laquelle la lamotrigine est utilisée, et non une preuve biologique. Rien n'indique que le médicament agisse sur la tumeur elle-même. Le lien avec l'indication d'origine (épilepsie) est donc indirect et repose sur un symptôme neurologique voisin, non sur un effet antitumoral.

À titre d'information, la prédiction classée en deuxième position, la **névralgie du trijumeau**, est bien mieux étayée (2 essais cliniques, niveau L2). Elle est plus plausible que le néoplasme.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Revue | Expert Review of Neurotherapeutics | Panorama des traitements médicaux et chirurgicaux de la névralgie du trijumeau ; ne traite pas de la tumeur |
| [30650431](https://pubmed.ncbi.nlm.nih.gov/30650431/) | 2018 | Rapport de cas | Stereotactic and Functional Neurosurgery | Radiochirurgie Gamma Knife d'une névralgie du trijumeau secondaire à une malformation caverneuse ; ne concerne ni la lamotrigine ni une tumeur |

Ces deux publications portent sur la névralgie du trijumeau et ne constituent pas une preuve en faveur d'un traitement tumoral.

---

## Informations de Marché en France

Sur les 20 AMM recensées, 5 sont présentées ci-dessous. Toutes sont annulées et aucune n'a de texte d'indication renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65667034 | LAMICTAL 200 mg (GlaxoSmithKline) | Comprimé dispersible ou à croquer | Non renseignée |
| 69658075 | LAMICTAL 100 mg (GlaxoSmithKline) | Comprimé dispersible ou à croquer | Non renseignée |
| 61043653 | LAMICTAL 2 mg (GlaxoSmithKline) | Comprimé dispersible ou à croquer | Non renseignée |
| 62897973 | LAMOTRIGINE BIOGARAN 25 mg | Comprimé dispersible | Non renseignée |
| 65503120 | LAMOTRIGINE TEVA 25 mg | Comprimé dispersible ou à croquer | Non renseignée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : trouble anxieux, trouble névrotique, trouble dysthymique, maladie du foie, maladie de la vésicule biliaire, thrombopénie, neutropénie, agranulocytose, anémie, anémie macrocytaire, pancytopénie, anémie aplasique (dont idiopathique), méningite non infectieuse.
- **Interactions médicamenteuses** : 100 interactions recensées. Les interactions de niveau modéré les plus notables concernent la morphine (y compris liposomale), l'opium, le dronabinol, la nabilone, le métoclopramide et l'orlistat. L'interaction avec la metformine est de niveau mineur. Plusieurs autres interactions sont de niveau inconnu (par exemple inhibiteurs de la pompe à protons, doxycycline, vancomycine).

Les mises en garde et contre-indications officielles de la notice ne figurent pas dans les données compilées. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5). Aucun essai clinique n'existe et la littérature retrouvée concerne la névralgie du trijumeau, non le néoplasme.
- Toutes les AMM françaises de la lamotrigine sont annulées, ce qui limite aussi la faisabilité réglementaire.

**Pour avancer, les éléments suivants sont nécessaires :**
- Des données précoces (précliniques ou mécanistiques) montrant un effet antitumoral de la lamotrigine sur les tumeurs du nerf trijumeau, ou une confirmation que la prédiction reflète en réalité la névralgie du trijumeau
- Les données détaillées sur le mécanisme d'action
- Les mises en garde et contre-indications de la notice officielle de l'ANSM
- Une réorientation de l'évaluation vers la **névralgie du trijumeau** (Phase 2/3 contre carbamazépine, 21 patients, niveau L2, « Proceed with Guardrails »), qui dispose de preuves nettement plus solides
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

