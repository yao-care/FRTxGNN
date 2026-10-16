---
layout: default
title: Axitinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Axitinib : nouvelle indication prédite, Carcinome rénal associé aux translocations Xp11.2/fusions du gène TFE3 (niveau de preuve L5). Indication d'origine : Carcinome rénal à cellules claires / carci…"
---

# Axitinib
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

# Axitinib : Du Carcinome Rénal à Cellules Claires au Carcinome Rénal à Translocation Xp11.2/Fusion TFE3

## Résumé en Une Phrase

Axitinib est un inhibiteur sélectif des récepteurs VEGFR-1, -2 et -3 (tyrosine kinase), initialement utilisé dans le traitement du carcinome rénal à cellules claires.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **carcinome rénal associé aux translocations Xp11.2/fusions du gène TFE3**, mais les preuves directes restent minimes : **1 essai clinique de phase 2** (15 patients, sans résultats publiés) et **aucune publication** spécifique à cette indication.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carcinome rénal à cellules claires / carcinome rénal (indication issue du graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Carcinome rénal associé aux translocations Xp11.2/fusions du gène TFE3 |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L2 (essai randomisé de phase 2 en cours, très petit effectif ; preuve faible en pratique) |
| Statut de Marché en France | Uniquement annulé (aucune AMM valide) |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, l'axitinib est un inhibiteur sélectif des VEGFR-1 à -3 qui bloque l'angiogenèse tumorale. Son efficacité dans le carcinome rénal avancé est établie par de grands essais de phase 3.

Le carcinome rénal à translocation Xp11.2/TFE3 est un sous-type rare, porté par une fusion génique, qui présente une signalisation VEGF/MET accrue. L'activité anti-angiogénique de l'axitinib y est donc biologiquement plausible, et le score élevé du modèle reflète aussi la proximité de ce sous-type avec l'indication d'origine dans l'ontologie des maladies.

Il faut toutefois rester prudent : la seule preuve directe est un petit essai randomisé de phase 2 (axitinib + nivolumab contre nivolumab seul), encore en cours et sans résultats. L'association testée inclut un inhibiteur de point de contrôle immunitaire, ce qui ne permet pas d'isoler la contribution de l'axitinib.

## Preuves d'Essais Cliniques

Essai directement lié à l'indication prédite :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Phase 2 | Actif, hors recrutement | 15 | Axitinib + nivolumab contre nivolumab seul dans le carcinome rénal à translocation TFE (non résécable ou métastatique), tous âges ; aucun résultat publié |

À titre de contexte, 40 essais sont recensés pour le carcinome rénal au sens large (prédiction de rang 6, qui correspond à l'indication d'origine) ; ils ne constituent pas des preuves pour le sous-type à translocation.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour le carcinome rénal à translocation Xp11.2/TFE3.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64662504 | AXITINIB TEVA 3 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 69083347 | INLYTA 3 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 69115535 | AXITINIB TEVA 5 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 67939209 | INLYTA 5 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 62215554 | AXITINIB TEVA 7 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |

Au total, 20 AMM sont recensées (INLYTA et génériques Teva, EG, Biogaran, Sandoz), toutes annulées ; seules les 5 premières sont listées ici.

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase des VEGFR), non cytotoxique conventionnel |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter la notice ; une surveillance de la fonction thyroïdienne est évoquée dans la littérature disponible (hypothyroïdie sous inhibiteurs de tyrosine kinase) |
| Protection de Manipulation | Veuillez consulter la notice |

## Considérations de Sécurité

- **Interactions médicamenteuses** : 100 interactions sont recensées dans les données compilées ; les principales sont :
  - **Majeures** : clarithromycine, dexaméthasone
  - **Modérées** : aprépitant, clotrimazole, miconazole, naltrexone
  - **Mineures** : antiacides et antisécrétoires gastriques (famotidine, ranitidine, cimétidine, nizatidine, rabéprazole, ésoméprazole, lansoprazole, dexlansoprazole, hydroxyde d'aluminium, carbonate de calcium, sels de magnésium, magaldrate)

Veuillez consulter la notice pour les mises en garde et contre-indications.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le mécanisme (inhibition des VEGFR) est plausible pour ce sous-type, mais la seule preuve directe est un essai de phase 2 de 15 patients, sans résultats, avec une association à un immunothérapeutique. De plus, aucune AMM française n'est actuellement valide, et les données de sécurité issues de la notice sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Résultats de l'essai NCT03595124 (fin prévue en novembre 2026)
- Mécanisme d'action détaillé (DrugBank)
- Mises en garde et contre-indications de la notice ANSM
- Vérification de la disponibilité des produits et du statut réglementaire en France
- Données spécifiques au sous-type (séries de cas, études observationnelles)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

