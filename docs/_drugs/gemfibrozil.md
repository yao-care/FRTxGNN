---
layout: default
title: Gemfibrozil
parent: Preuves modérées (L3-L4)
nav_order: 359
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-14
monitor_inn: "GEMFIBROZIL"
predicted_indications: ["rheumatoid arthritis", "multiple endocrine neoplasia", "HIV infectious disease", "hypoalphalipoproteinemia", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "methemoglobinemia, alpha type", "sclerosing cholangitis", "methemoglobin reductase deficiency"]
description: "Gemfibrozil : nouvelle indication prédite, Polyarthrite rhumatoïde (rheumatoid arthritis) (niveau de preuve L4). Indication d'origine : Non renseignée dans les données locales"
---

# Gemfibrozil
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **9** 
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

## Gemfibrozil: Polyarthrite rhumatoïde (rheumatoid arthritis)
{: .text-alpha }

## Résumé en Une Phrase

Gemfibrozil est un fibrate, initialement utilisé pour le traitement de l'hypertriglycéridémie.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **polyarthrite rhumatoïde**, mais aucun essai clinique n'est enregistré et seules **4 publications** (surtout précliniques, dont une seule porte sur le gemfibrozil) existent à ce jour. Le niveau de preuve reste donc faible.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Polyarthrite rhumatoïde (rheumatoid arthritis) |
| Score de Prédiction TxGNN | 0.9990 |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le gemfibrozil appartient à la classe des fibrates, agonistes du récepteur PPAR-alpha, et son efficacité sur les triglycérides est établie.

L'activation de PPAR-alpha pourrait exercer des effets anti-inflammatoires et immunomodulateurs, par exemple une baisse des cytokines pro-inflammatoires et une action sur la différenciation des lymphocytes T. Ces mécanismes sont pertinents dans une maladie auto-immune inflammatoire comme la polyarthrite rhumatoïde.

Les données de soutien restent toutefois limitées : une étude préclinique sur un fibrate apparenté (le bézafibrate, agoniste pan-PPAR) et une étude chez le rat combinant gemfibrozil et corticoïdes à dose réduite. Aucune donnée humaine contrôlée n'existe pour le gemfibrozil dans la polyarthrite rhumatoïde.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | Préclinique (rat, arthrite induite par adjuvant) | Modern Rheumatology | Gemfibrozil associé à une dose réduite de prednisolone : tableau de prise en charge comparable à celui de la dose complète de corticoïde |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | Préclinique (médicament apparenté : bézafibrate) | International Immunopharmacology | Le bézafibrate, agoniste pan-PPAR, atténue la polyarthrite expérimentale via la modulation de voies inflammatoires dépendantes de PPAR, notamment PPAR-γ |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | Préclinique (mécanistique) | Journal of Immunology | Étude sur l'expression de Foxp3 dans les lymphocytes T régulateurs et le rôle du monoxyde d'azote ; lien indirect |
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | Commentaire / revue | American Journal of Clinical Dermatology | Revue de l'érythème palmaire ; pertinence faible |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68696386 | LIPUR 450 mg, comprimé pelliculé (PFIZER HOLDING FRANCE) | Comprimé pelliculé | Non renseignée (AMM active) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie hépatique, maladie de la vésicule biliaire, lithiase biliaire (cholélithiase, cholécystolithiase, cholédocholithiase), cholangite biliaire primitive, insuffisance rénale, thrombopénie, leucopénie, anémie (dont anémie macrocytaire), syndrome de Reynolds.
- **Interactions médicamenteuses** (100 interactions recensées ; principales listées) :
  - **Majeures** : rosuvastatine, simvastatine (risque musculaire, notamment rhabdomyolyse), pioglitazone, répaglinide, éluxadoline, lopéramide.
  - **Modérées** : insulines (asparte, dégludec, détémir, glargine, glulisine, humaine), natéglinide, rosiglitazone, tolazamide, chlorpropamide, acide chénodésoxycholique, rifaximine.

Les mises en garde et contre-indications de la notice française n'ont pas pu être consultées. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur un score de modèle élevé, mais les preuves se limitent à des études précliniques, dont une seule sur le gemfibrozil. Il n'y a ni essai clinique ni donnée humaine contrôlée, et la seule AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications), donnée bloquante pour le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Réaliser des études précliniques complémentaires avec le gemfibrozil lui-même dans la polyarthrite rhumatoïde, puis un essai clinique de phase 2
- Évaluer le profil de sécurité, en particulier les interactions (statines, antidiabétiques) et les atteintes hépatobiliaires, chez des patients atteints de polyarthrite rhumatoïde

## Remarque sur les Autres Indications Prédites

Parmi les autres indications prédites, deux présentent un niveau de preuve L2 : l'**infection par le VIH** et l'**hypoalphalipoprotéinémie**.

- **VIH** : le bénéfice observé concerne la dyslipidémie associée aux inhibiteurs de protéase, non une activité antivirale. Un essai randomisé en double aveugle (PMID 12409741) soutient cet effet hypolipémiant.
- **Hypoalphalipoprotéinémie** : plusieurs petites études (1989-2000) montrent des effets sur le HDL-cholestérol, mais cette indication est proche de l'indication lipidique d'origine.

Ces deux pistes pourraient être évaluées en priorité si l'objectif est d'identifier une indication mieux étayée que la polyarthrite rhumatoïde.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

