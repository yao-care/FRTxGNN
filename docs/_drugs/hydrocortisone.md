---
layout: default
title: Hydrocortisone
parent: Prédiction du modèle uniquement (L5)
nav_order: 381
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Hydrocortisone : nouvelle indication prédite, Pelade (alopecia areata) (niveau de preuve L5). Indication d'origine : Non précisée dans les textes d'AMM disponibles"
---

# Hydrocortisone
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

# Hydrocortisone : De l'insuffisance surrénalienne et des maladies inflammatoires à la pelade (alopecia areata)

## Résumé en Une Phrase

L'hydrocortisone est un corticostéroïde utilisé à l'origine dans l'insuffisance surrénalienne, les maladies auto-immunes et inflammatoires (maladie de Crohn, maladies inflammatoires de l'intestin) ainsi que dans certaines affections cutanées.
Le modèle TxGNN prédit qu'il pourrait être utile dans la **pelade (alopecia areata)**, mais les preuves directes restent faibles : **1 essai clinique** (où l'hydrocortisone sert de comparateur) et **une vingtaine de publications**, dont une seule est un essai randomisé et la plupart sont anciennes ou hors sujet.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les textes d'AMM disponibles ; les indications d'origine issues du graphe de connaissances incluent l'insuffisance surrénalienne, la maladie d'Addison, la maladie de Crohn et les maladies auto-immunes |
| Nouvelle Indication Prédite | Pelade (alopecia areata) |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L1 selon le classement automatique, à relativiser (voir ci-dessous) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 15 (toutes annulées) |
| Décision Recommandée | Hold |

**Remarque sur le niveau de preuve :** le niveau L1 affiché par le classement automatique repose sur un seul essai de phase 3 de petite taille (41 patients) dans lequel l'hydrocortisone 1 % était le **comparateur** à faible puissance face au clobétasol 0,05 %. Il ne démontre pas l'efficacité de l'hydrocortisone. Les critères stricts (au moins 2 essais de phase 3 menés à terme) ne sont pas remplis ; le niveau réel est plus proche de L3. La décision recommandée est donc prudente.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, l'hydrocortisone est un corticostéroïde qui freine l'activité immunitaire et l'inflammation locales ou systémiques. Son efficacité est établie dans l'insuffisance surrénalienne (traitement substitutif) et dans plusieurs maladies inflammatoires et auto-immunes.

La pelade est une maladie auto-immune à médiation par les lymphocytes T, qui attaque le follicule pileux. Un corticostéroïde peut donc, sur le plan théorique, réduire cette agression immunitaire. C'est probablement ce lien avec les maladies auto-immunes qui explique le score élevé du modèle.

Cependant, l'hydrocortisone est un corticostéroïde de **faible puissance**. Dans l'unique essai randomisé identifié, elle a servi de référence face à un corticoïde puissant (clobétasol). Ce lien mécanistique reste donc plausible, mais non démontré pour l'hydrocortisone elle-même.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Terminé | 41 | Clobétasol 0,05 % crème versus hydrocortisone 1 % crème chez l'enfant atteint de pelade ; l'hydrocortisone est le comparateur de faible puissance, d'où un soutien indirect seulement |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | ECR | JAMA Dermatology | Clobétasol 0,05 % versus hydrocortisone 1 % dans la pelade de l'enfant |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Série de cas historique | Medical Times | Traitement de la pelade par cortisone, hydrocortisone et analogues |
| [13610145](https://pubmed.ncbi.nlm.nih.gov/13610145/) | 1958 | Rapport clinique historique | Der Hautarzt | Repousse des cheveux après injection intradermique d'hydrocortisone |
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Rapports de cas | J Am Acad Dermatol | Quatre cas de pelade congénitale, traités notamment par minoxidil et corticoïdes topiques |
| [13525930](https://pubmed.ncbi.nlm.nih.gov/13525930/) | 1958 | Revue clinique | J Med Soc New Jersey | Aperçu de la pelade et d'autres problèmes du cuir chevelu |
| [24326563](https://pubmed.ncbi.nlm.nih.gov/24326563/) | 2013 | Préclinique (souris) | J Investig Dermatol Symp Proc | Agonistes et antagonistes de la PTH dans un modèle murin de pelade, sans rapport direct avec l'hydrocortisone |
| [19289325](https://pubmed.ncbi.nlm.nih.gov/19289325/) | 2009 | Rapport de cas | Endocr Pract | Syndrome polyglandulaire auto-immun de type 3 avec alopécie universelle |

Plusieurs autres publications (injections intralésionnelles d'hydrocortisone des années 1955 à 1973, enquête sur l'automédication, cas vétérinaire) sont très anciennes, sans résumé ou hors sujet ; elles n'apportent pas de preuve exploitable.

**Autres indications prédites (preuves insuffisantes) :** mucinose folliculaire (alopecia mucinosa), effluvium télogène, folliculite décalvante de Quinquaud, syndrome néphrotique idiopathique stéroïdosensible et plusieurs syndromes génétiques rares. Aucune ne dispose d'essai clinique ni de littérature directement pertinente. Le seul article indirect sur le syndrome néphrotique (1982) concerne la réponse surrénalienne et non l'efficacité de l'hydrocortisone. Toutes sont classées Hold.

## Informations de Marché en France

Toutes les AMM recensées sont annulées. Les textes d'indication ne sont pas disponibles dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62550143 | SOFTACORT 3,35 mg/ml, collyre | Collyre en solution | Non renseignée |
| 65008233 | COLOFOAM, mousse rectale | Mousse | Non renseignée |
| 67240376 | CORTISEDERMYL 0,5 %, crème | Crème | Non renseignée |
| 67369944 | LOCOID, crème épaisse | Crème épaisse pour application | Non renseignée |
| 66841235 | LOCOID 0,1 %, crème | Crème | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations déduites, non extraites d'une notice) : hypertension, épilepsie, ulcère gastrique, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, hyperglycémie, infections virales (rougeole, verrues, papillomavirus anogénital, kératite herpétique) et déficits en hormones hypophysaires.
- **Interactions médicamenteuses** (100 interactions recensées, extrait des principales) :
  - **Majeure :** adalimumab.
  - **Modérées :** zidovudine, isotrétinoïne, acarbose, acétazolamide, kétorolac, nifédipine, ibuprofène, éthinylestradiol, aldesleukine, alemtuzumab, albiglutide, certains vaccins.
  - **Mineures :** formotérol, salbutamol.

Les mises en garde et contre-indications issues de la notice officielle ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La seule preuve clinique directe est un essai pédiatrique de petite taille où l'hydrocortisone est le comparateur faible, ce qui n'établit pas son efficacité dans la pelade. Le niveau L1 automatique est trompeur.
- Les données de sécurité issues de la notice et le mécanisme d'action manquent, et aucune AMM n'est en vigueur en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice officielle (ANSM) pour les mises en garde et contre-indications, ce qui est bloquant pour le criblage de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Identifier ou conduire des essais comparant l'hydrocortisone à un placebo ou à un traitement actif dans la pelade, avec une formulation et une voie d'administration définies (topique ou intralésionnelle).
- Clarifier la compatibilité de la voie d'administration et la situation réglementaire, toutes les AMM étant annulées.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

