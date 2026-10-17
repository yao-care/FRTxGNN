---
layout: default
title: Atezolizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 78
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Atezolizumab : nouvelle indication prédite, Carcinome urothélial de l'urètre prostatique (niveau de preuve L5). Indication d'origine : Carcinome à cellules transitionnelles"
monitor_inn: "atezolizumab"
predicted_indications: ["prostatic urethra urothelial carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "renal pelvis papillary urothelial carcinoma", "uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
---

# Atezolizumab
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

# Atézolizumab : Du Carcinome Urothélial au Carcinome Urothélial de l'Urètre Prostatique

## Résumé en Une Phrase

L'atézolizumab est un anticorps monoclonal bloquant PD-L1, initialement associé au traitement du carcinome à cellules transitionnelles (carcinome urothélial).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **carcinome urothélial de l'urètre prostatique**, avec **1 essai clinique** (phase 1b, en association) et **aucune publication** soutenant actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carcinome à cellules transitionnelles (source : graphe de connaissances TxGNN ; aucun texte d'indication dans les AMM) |
| Nouvelle Indication Prédite | Carcinome urothélial de l'urètre prostatique |
| Score de Prédiction TxGNN | 99,98 % |
| Niveau de Preuve | L5 (un seul essai de phase 1b indirect, en association, sans résultat spécifique au site ; la prédiction repose donc essentiellement sur le modèle) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

> Remarque : la fiche de données attribue le niveau L3 à cette indication. Au regard des règles de détermination (aucun ECR de phase 2/3, aucune étude observationnelle ni revue systématique), le niveau L5 est retenu ici, ou au mieux L4 de manière prudente.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, l'atézolizumab est un inhibiteur de point de contrôle immunitaire ciblant PD-L1. Son activité dans le carcinome urothélial est l'indication d'origine, et il pourrait mécanistiquement être applicable à d'autres tumeurs urothéliales.

Le carcinome urothélial de l'urètre prostatique est une tumeur urothéliale anatomiquement et histologiquement proche du carcinome vésical. La biologie de la voie PD-1/PD-L1 pourrait donc se transposer plausiblement. Cependant, l'unique essai disponible est une étude de phase 1b d'escalade de dose associant cabozantinib et atézolizumab dans de nombreuses tumeurs solides. Il n'est pas spécifique à ce site tumoral et le lien reste au mieux indirect.

D'autres indications prédites figurent aussi dans les données, avec des scores comparables (carcinome urothélial sarcomatoïde du bassinet du rein, variante sarcomatoïde du carcinome urothélial infiltrant de la vessie, carcinome urothélial papillaire du bassinet). Elles ne disposent ni d'essais ni de publications. Seul le carcinome endocervical présente davantage de données (voir plus bas).

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1 (1b) | Actif, ne recrute plus | 914 | Cabozantinib seul ou associé à l'atézolizumab dans des tumeurs solides localement avancées ou métastatiques, dont le carcinome urothélial (vessie, bassinet, uretère, urètre) ; évaluation de la sécurité, de la tolérance, de l'efficacité préliminaire et de la pharmacocinétique. Pertinence partielle : phase précoce, association, pas de données spécifiques à l'urètre prostatique |

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69209340 | TECENTRIQ 1 875 mg, solution injectable | Solution injectable | Non renseignée (AMM annulée) |
| 64422886 | TECENTRIQ 840 mg, solution à diluer pour perfusion | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |
| 60345905 | TECENTRIQ 1200 mg, solution à diluer pour perfusion | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Immunothérapie (anticorps anti-PD-L1) |
| Risque de Myélosuppression | Faible (non cytotoxique conventionnel ; pas de données de toxicité spécifiques dans les données compilées) |
| Classification d'Émétogénicité | Faible |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice. Surveillance usuelle des effets indésirables immunologiques : fonction hépatique, rénale, thyroïdienne, NFS |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 75 interactions ont été recensées au total ; les principales parmi les 20 premières affichées sont :
  - **Majeures** : adalimumab, baricitinib, vaccin BCG (souche Tice, vivant).
  - **Modérées** : corticoïdes (hydrocortisone, triamcinolone, bétaméthasone, budésonide, dexaméthasone, prednisolone, prednisone, méthylprednisolone, déflazacort), roflumilast, alefacept, alemtuzumab, anakinra, azathioprine, vaccin anthrax, anatoxine tétanique, antigène d'adénovirus de type 4.

Il s'agit pour l'essentiel d'interactions de type immunomodulateur/immunosuppresseur ou vaccinal. Veuillez consulter la notice pour les mises en garde et contre-indications, non disponibles dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'indication prédite n'est soutenue que par un essai de phase 1b indirect, mené en association et sans données spécifiques à l'urètre prostatique, ni aucune publication. Par ailleurs, les trois AMM françaises sont annulées et les données de sécurité issues de la notice sont absentes (lacune bloquante).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications) auprès de l'ANSM
- Obtenir les données détaillées sur le mécanisme d'action (via DrugBank)
- Confirmer les indications précédemment approuvées et la raison de l'annulation des AMM
- Rechercher des données cliniques spécifiques aux tumeurs urothéliales de l'urètre prostatique (séries de cas, études observationnelles, cohortes dédiées)
- Pour une piste alternative, examiner le carcinome endocervical, qui dispose de deux essais de phases 1 et 2 de petite taille (NCT02921269, 11 patientes ; NCT03738228, 40 patientes), mais sans confirmation de phase 3
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

