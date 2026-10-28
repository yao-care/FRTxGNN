---
layout: default
title: Palonosetron
parent: Preuves modérées (L3-L4)
nav_order: 574
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-28
description: "Palonosetron : nouvelle indication prédite, Migraine (« migraine disorder ») (niveau de preuve L4). Indication d'origine : Non renseignée dans les données d'AMM compilées"
monitor_inn: "palonosetron"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Palonosetron
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **4** 
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

## Palonosétron : Des Nausées et Vomissements Induits par la Chimiothérapie à la Migraine
{: .text-alpha }

## Résumé en Une Phrase

Le palonosétron est un antagoniste des récepteurs 5-HT3, commercialisé en France sous le nom d'ALOXI en solution injectable. Le texte de son indication autorisée n'est toutefois pas renseigné dans les données compilées pour ce rapport.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **migraine** (score élevé), mais **aucun essai clinique** n'existe et la seule publication associée est un **rapport de cas** décrivant une céphalée de type migraineux *induite* par le palonosétron, c'est-à-dire un signal d'effet indésirable plutôt que de bénéfice.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées |
| Nouvelle Indication Prédite | Migraine (« migraine disorder ») |
| Score de Prédiction TxGNN | 0,9974 |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le palonosétron fait partie de la classe des antagonistes des récepteurs 5-HT3 (sétrons), utilisés comme antiémétiques, et son blocage de la sérotonine au niveau de ces récepteurs pourrait, sur le plan théorique, être lié à la physiopathologie de la migraine.

Le lien est plausible mais non démontré. Les voies sérotoninergiques et trigémino-vasculaires interviennent dans la migraine, et les nausées et vomissements en sont une comorbidité fréquente. Le score provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

Il faut cependant rester prudent. Le score TxGNN est très élevé (0,9974), mais la seule publication spécifique rapporte une céphalée de type migraineux déclenchée par le palonosétron. Ce signal va dans le sens opposé à un bénéfice thérapeutique. Les autres prédictions (migraine avec aura du tronc cérébral, atrophodermie vermiculée, ulérythème ophryogène) reposent sur la seule prédiction informatique, sans mécanisme plausible. Les deux dernières semblent refléter des similarités apprises par le modèle TxGNN (apprentissage profond) entre maladies apparentées, et non des preuves biologiques.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Rapport de cas | Canadian Journal of Anaesthesia | Céphalée de type migraineux induite par le palonosétron : signal d'effet indésirable, non d'efficacité |

Une revue de 2026 ([42748473](https://pubmed.ncbi.nlm.nih.gov/42748473/), *European Heart Journal – Cardiovascular Pharmacotherapy*) porte sur l'allongement de l'intervalle QT associé aux antiémétiques. Elle est liée à la prédiction « susceptibilité à la migraine avec ou sans aura ». Elle relève de la sécurité et n'apporte aucune preuve d'efficacité dans la migraine.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61794949 | ALOXI 250 microgrammes, solution injectable (active) | Solution injectable | Non renseignée |
| 67538668 | PALONOSETRON KALCEKS 250 microgrammes, solution injectable (active) | Solution injectable | Non renseignée |

---

## Considérations de Sécurité

- **Interactions médicamenteuses** : 398 interactions sont recensées. Parmi celles affichées, plusieurs sont de niveau **majeur** :
  - opioïdes et apparentés : fentanyl, alfentanil, tramadol, dextrométhorphane ;
  - triptans : almotriptan, sumatriptan ;
  - médicaments à risque cardiaque ou de syndrome sérotoninergique : amiodarone, amisulpride, amitriptyline, anagrélide.
  
  Des interactions de niveau modéré concernent notamment l'abiratérone, la famotidine, le formotérol, l'adénosine, le salbutamol, l'alfuzosine, le propofol, le lopéramide, la codéine et la dihydrocodéine.
- **Allongement du QT** : la littérature récente souligne un risque d'allongement de l'intervalle QT pour la classe des antiémétiques.
- **Céphalée de type migraineux** : un cas documenté, déclenchée par le palonosétron.

Les mises en garde et contre-indications de la notice n'ont pas pu être obtenues. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est élevé, mais la prédiction repose sur aucun essai clinique et sur un seul rapport de cas indiquant un possible effet délétère (niveau de preuve L4). Les autres indications prédites sont de niveau L5.
- Les AMM françaises sont toutes annulées, et les données de sécurité de la notice sont manquantes, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde, contre-indications, indication autorisée).
- Obtenir les données sur le mécanisme d'action (par exemple via DrugBank).
- Examiner la littérature sur les antagonistes 5-HT3 dans la migraine pour déterminer si l'effet est protecteur ou aggravant.
- Évaluer le risque d'allongement du QT et des interactions majeures chez les patients migraineux, notamment avec les triptans.
- Clarifier la situation réglementaire (AMM annulées) et la compatibilité de la voie d'administration (injectable) avec un usage dans la migraine.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

