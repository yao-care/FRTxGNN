---
layout: default
title: Dutasteride
parent: Prédiction du modèle uniquement (L5)
nav_order: 266
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Dutasteride : nouvelle indication prédite, Hypertrichose universelle congénitale de type Ambras (niveau de preuve L5). Indication d'origine : Hyperplasie bénigne de la prostate"
monitor_inn: "dutasteride"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "migraine with brainstem aura", "familial isolated trichomegaly"]
---

# Dutasteride
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

## Dutasteride : De l'Hyperplasie Bénigne de la Prostate à l'Hypertrichose universelle congénitale de type Ambras
{: .text-alpha }

## Résumé en Une Phrase

Dutasteride est un inhibiteur de la 5-alpha-réductase, initialement utilisé pour le traitement de l'hyperplasie bénigne de la prostate.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertrichose universelle congénitale de type Ambras**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hyperplasie bénigne de la prostate |
| Nouvelle Indication Prédite | Hypertrichose universelle congénitale de type Ambras |
| Score de Prédiction TxGNN | 1,0000 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | 20 (dont 0 valide, 20 annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, dutasteride est un inhibiteur double de la 5-alpha-réductase (types 1 et 2) qui diminue le taux de dihydrotestostérone (DHT). Son efficacité dans l'hyperplasie bénigne de la prostate repose sur cette réduction de la DHT.

La relation avec la nouvelle indication est **faible**. Le syndrome d'Ambras est une hypertrichose congénitale liée à des remaniements génomiques touchant la régulation du gène TRPS1, et non à un excès d'androgènes. Une baisse de la DHT n'a donc pas de justification claire pour corriger cette pilosité d'origine génétique. Le score provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique ; aucun essai ni publication ne l'appuie.

Les autres prédictions du modèle (hypertrichose, anomalies génétiques de la tige pilaire, hypotrichose, alopécie en aires diffuse, etc.) présentent le même profil : preuves absentes ou très indirectes et liens mécanistiques peu convaincants. Pour l'alopécie en aires diffuse, la seule publication retrouvée porte sur l'alopécie androgénétique de la femme, une maladie différente.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'indication principale (Ambras).

## Informations de Marché en France

Les 20 AMM recensées sont annulées. Aucun texte d'indication approuvée n'est disponible dans les données compilées. Principales AMM :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 60051234 | AVODART 0,5 mg (GlaxoSmithKline) | Capsule molle | Active |
| 60008724 | Dutasteride Viatris 0,5 mg | Capsule molle | Active |
| 61398768 | Dutasteride Krka 0,5 mg | Capsule molle | Active |
| 69552766 | Dutasteride/Tamsulosine Cristers 0,5 mg/0,4 mg | Gélule | Active |
| 65218235 | Dutasteride/Tamsulosine Zentiva 0,5 mg/0,4 mg | Gélule | Active |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : atrophie multisystématisée, syndrome de tachycardie orthostatique posturale, hypotension orthostatique, maladie hépatique, maladie de la vésicule biliaire, priapisme, syndrome de l'iris hypotonique peropératoire.
- **Interactions médicamenteuses** : 122 interactions recensées. Les interactions de niveau modéré concernent l'aprépitant, la cimétidine, la clarithromycine, le clotrimazole et le miconazole. D'autres interactions, de niveau inconnu, concernent notamment la simvastatine, la metformine, l'oméprazole, la prednisone et la morphine.
- **Risque tératogène** : dutasteride est potentiellement tératogène (féminisation d'un fœtus masculin), ce qui plaide contre son usage dans les troubles du développement.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles ; veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et le lien mécanistique avec une hypertrichose génétique est faible. Par ailleurs, le médicament est commercialisé en France, avec 20 AMM valides.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (DrugBank) et analyse du lien mécanistique avec TRPS1
- Mises en garde et contre-indications officielles de la notice (ANSM), actuellement bloquantes pour le criblage de sécurité
- Données précliniques ou cliniques spécifiques à l'hypertrichose d'Ambras
- Évaluation du risque tératogène et de la disponibilité du produit en France (AMM annulées)
- Réexamen d'autres candidats plus plausibles, car le lien avec l'alopécie androgénétique n'est pas transposable à l'alopécie en aires
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

