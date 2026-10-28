---
layout: default
title: Moxonidine
parent: Prédiction du modèle uniquement (L5)
nav_order: 517
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "MOXONIDINE"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "primary hereditary glaucoma"]
description: "Moxonidine : nouvelle indication prédite, Hypotrichose simple du cuir chevelu (hypotrichosis simplex of the scalp) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locale"
---

# Moxonidine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

## Moxonidine: Hypotrichose simple du cuir chevelu (hypotrichosis simplex of the scalp)
{: .text-alpha }

## Résumé en Une Phrase

Moxonidine est un antihypertenseur à action centrale, initialement utilisé pour le traitement de l'hypertension artérielle.
Le modèle TxGNN (apprentissage profond) prédit qu'il pourrait être efficace pour l'**hypotrichose simple du cuir chevelu**, mais **aucun essai clinique** et **aucune publication** ne soutiennent cette direction. Il s'agit d'une prédiction purement computationnelle : le score provient du modèle TxGNN et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Hypotrichose simple du cuir chevelu (hypotrichosis simplex of the scalp) |
| Score de Prédiction TxGNN | 0.9995 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 10 sur 10) |
| Nombre d'AMM | 10 (valides : 10) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, moxonidine est un agoniste central des récepteurs imidazoliniques I1 et alpha-2 adrénergiques (les données compilées confirment une liaison aux récepteurs α2A, α2B et α2C). Il réduit le tonus sympathique et son efficacité dans l'hypertension est établie.

**Pour l'hypotrichose simple du cuir chevelu, la prédiction ne paraît pas raisonnable.** Cette maladie est un trouble génétique du follicule pileux (variants de CDSN, APCDD1, RPL21, par exemple) et aucun lien pharmacologique avec une action sympatholytique n'est établi. Le score élevé provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

D'autres prédictions classées parmi les premières relèvent de la même logique (hypotrichose congénitale avec milia, alopécie areata diffuse, alopécie). Parmi les dix candidats, deux restent biologiquement cohérents avec la pharmacologie connue : l'hypertension rénale maligne et l'hypertension rénovasculaire maligne (niveau L4, « question de recherche », par extrapolation de l'indication approuvée). Le glaucome héréditaire primitif présente un lien plausible au niveau de la classe des agonistes alpha-2 (brimonidine, apraclonidine), mais reste spéculatif pour la moxonidine.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'hypotrichose simple du cuir chevelu.

À titre d'information, une publication a été retrouvée pour la prédiction voisine « alopécie » (rang 4) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [40007390](https://pubmed.ncbi.nlm.nih.gov/40007390/) | 2024 | Rapport de cas | Georgian Medical News | Cas d'un syndrome de Graham-Little-Piccardi-Lasseur (variante de lichen plan folliculaire) chez une patiente bulgare. Ne porte pas sur la moxonidine : non soutenant. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62425307 | MOXONIDINE TEVA SANTE 0,4 mg | comprimé pelliculé | Non renseignée (AMM active) |
| 64771724 | MOXONIDINE BIOGARAN 0,2 mg | comprimé pelliculé | Non renseignée (AMM active) |
| 62036633 | MOXONIDINE BIOGARAN 0,4 mg | comprimé pelliculé | Non renseignée (AMM active) |
| 68782718 | PHYSIOTENS 0,4 mg | comprimé pelliculé | Non renseignée (AMM active) |
| 63708322 | MOXONIDINE TEVA SANTE 0,2 mg | comprimé pelliculé | Non renseignée (AMM active) |

Cinq AMM sur dix sont affichées ; les dix sont annulées.

## Considérations de Sécurité

**Interactions médicamenteuses / pharmacologie :** les données compilées indiquent une action sur les récepteurs α2A, α2B et α2C-adrénergiques humains (ADRA2A, ADRA2B, ADRA2C). Il s'agit de données de cibles pharmacologiques, non d'interactions avec d'autres médicaments.

Pour les mises en garde et contre-indications, veuillez consulter la notice : les informations de l'ANSM n'ont pas pu être exploitées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication, et sans lien mécanistique plausible. Le statut de marché (toutes AMM annulées) limite aussi la faisabilité pratique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (DrugBank) pour mieux analyser le lien mécanistique
- Mises en garde et contre-indications de la notice ANSM (lacune bloquante pour tout examen de sécurité)
- Réorientation vers les candidats plus cohérents (hypertension rénale ou rénovasculaire maligne, glaucome) pour une revue de littérature ciblée
- Vérification des similarités apprises par le modèle TxGNN (apprentissage profond) pour les prédictions dermatologiques
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

