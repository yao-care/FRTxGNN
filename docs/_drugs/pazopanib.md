---
layout: default
title: Pazopanib
parent: Preuves modérées (L3-L4)
nav_order: 581
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Pazopanib : nouvelle indication prédite, Carcinome rénal non classé (niveau de preuve L3). Indication d'origine : Sarcome des tissus mous, carcinome rénal à cellules claires"
monitor_inn: "PAZOPANIB"
predicted_indications: ["ovarian myxoid liposarcoma", "heart fibrosarcoma", "fibroblastic neoplasm", "kidney fibrosarcoma", "dermatofibrosarcoma protuberans"]
---

# Pazopanib
{: .fs-9 }

Niveau de preuve: **L3** | Indications prédites: **10** 
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

# Pazopanib : Du Carcinome Rénal à Cellules Claires au Carcinome Rénal Non Classé

## Résumé en Une Phrase

Le pazopanib est un inhibiteur de tyrosine kinase multicible, initialement utilisé pour le traitement du sarcome des tissus mous et du carcinome rénal à cellules claires.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **carcinome rénal non classé**, avec **6 publications** soutenant actuellement cette direction (aucun essai clinique enregistré).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Sarcome des tissus mous, carcinome rénal à cellules claires (indications issues du graphe de connaissances ; le texte d'indication des AMM françaises n'est pas disponible) |
| Nouvelle Indication Prédite | Carcinome rénal non classé |
| Score de Prédiction TxGNN | 99,63 % |
| Niveau de Preuve | L3 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes annulées) |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le pazopanib est un inhibiteur de tyrosine kinase multicible (VEGFR, PDGFR, c-Kit) à activité anti-angiogénique. Son efficacité dans le carcinome rénal à cellules claires est établie, et il est également utilisé dans certains sarcomes des tissus mous.

Le carcinome rénal non classé appartient à la famille des carcinomes rénaux à cellules non claires. L'angiogenèse y joue aussi un rôle, ce qui rend plausible une extension du mécanisme. Le pazopanib étant déjà une référence en première ligne dans le carcinome à cellules claires, son utilisation dans les formes non claires est une extrapolation biologiquement raisonnable.

Cependant, l'hétérogénéité histologique des carcinomes rénaux à cellules non claires limite la solidité des conclusions. Les preuves disponibles reposent surtout sur des cohortes rétrospectives et des séries en vie réelle, complétées par une étude de phase II prospective à bras unique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [28546525](https://pubmed.ncbi.nlm.nih.gov/28546525/) | 2018 | Phase II, bras unique, multicentrique | Cancer Res Treat | Évaluation de l'efficacité et de la tolérance du pazopanib dans le carcinome rénal métastatique à cellules non claires |
| [28108284](https://pubmed.ncbi.nlm.nih.gov/28108284/) | 2017 | Cohorte rétrospective multicentrique | Clin Genitourin Cancer | Étude italienne PANORAMA : efficacité et toxicité du pazopanib en première ligne dans les carcinomes rénaux non à cellules claires |
| [27568124](https://pubmed.ncbi.nlm.nih.gov/27568124/) | 2017 | Cohorte rétrospective | Clin Genitourin Cancer | Résultats de patients atteints d'un carcinome rénal métastatique non à cellules claires traités par pazopanib |
| [31921344](https://pubmed.ncbi.nlm.nih.gov/31921344/) | 2019 | Étude en vie réelle | Ecancermedicalscience | Comparaison du sunitinib et du pazopanib en première ligne dans les formes non claires et sarcomatoïdes |
| [30268423](https://pubmed.ncbi.nlm.nih.gov/30268423/) | 2019 | Cohorte rétrospective | Clin Genitourin Cancer | Carcinomes de primitif inconnu à caractéristiques de carcinome rénal métastatique traités par thérapies ciblées |
| [41558869](https://pubmed.ncbi.nlm.nih.gov/41558869/) | 2026 | Cohorte rétrospective | Eur Urol Oncol | Résultats des traitements de première ligne contemporains ou traditionnels dans le carcinome rénal métastatique non à cellules claires (consortium IMDC) |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63803884 | VOTRIENT 400 mg, comprimé pelliculé (annulée) | Comprimé pelliculé | Non précisée |
| 62894653 | VOTRIENT 200 mg, comprimé pelliculé (annulée) | Comprimé pelliculé | Non précisée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase multicible) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter la notice ; au vu des contre-indications du graphe de connaissances, une surveillance de la fonction hépatique, de la tension artérielle, de l'ECG/QT, de la fonction thyroïdienne, des électrolytes et de la protéinurie est à envisager |
| Protection de Manipulation | Veuillez consulter la notice |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (et non du texte de la notice)** : hypertension, syndrome du QT long et torsades de pointes, insuffisance hépatique, atteinte hépatique d'origine médicamenteuse, hyperbilirubinémie (dont syndrome de Gilbert), hypothyroïdie, troubles électrolytiques (carence en potassium, hypercalcémie, néphrocalcinose, troubles du métabolisme du phosphore), infarctus du myocarde, hémoglobinopathie, maladie diarrhéique, ulcère peptique actif, hémorragie intracérébrale, pancréatite et protéinurie.
- **Interactions médicamenteuses** (100 interactions recensées ; principales interactions majeures) : famotidine, ranitidine, cimétidine, oméprazole, ésoméprazole, rabéprazole, dexlansoprazole (antiacides et inhibiteurs de la pompe à protons), clarithromycine, dolasétron. Interactions modérées notamment avec : pioglitazone, lopéramide, aprépitant, dexaméthasone, budésonide, saxagliptine, élig­lustat, bisacodyl, oxyde de magnésium et polyéthylène glycol.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Les preuves (une phase II prospective à bras unique et plusieurs cohortes rétrospectives) soutiennent une activité du pazopanib dans les carcinomes rénaux non à cellules claires, sans essai randomisé ni essai enregistré. Le niveau L3 et l'hétérogénéité histologique imposent la prudence. Les AMM françaises étant toutes annulées, l'accès en France est limité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications issues de la notice de l'ANSM (données bloquantes pour le dépistage de sécurité)
- Données détaillées sur le mécanisme d'action (DrugBank)
- Essais prospectifs ou randomisés spécifiques au carcinome rénal non classé
- Clarification du statut réglementaire et de l'accessibilité du pazopanib en France (AMM annulées, génériques éventuels)
- Plan de surveillance de la sécurité (hépatique, cardiovasculaire, tension artérielle) et revue des interactions, notamment avec les antiacides et inhibiteurs de la pompe à protons

---

## Autres Indications Prédites (Résumé)

| Rang | Indication Prédite | Score TxGNN | Niveau de Preuve | Décision |
|------|------|------|------|------|
| 4 | Liposarcome | 99,59 % | L2 | Proceed with Guardrails |
| 8 | Néoplasme fibroblastique | 99,35 % | L2 | Proceed with Guardrails |
| 10 | Dermatofibrosarcome protubérant | 99,29 % | L2 | Proceed with Guardrails |
| 2, 3, 5, 6, 7, 9 | Carcinome rénal associé au neuroblastome ; carcinome rénal à translocation Xp11.2/TFE3 ; carcinome rénal de l'enfant ; liposarcome myxoïde ovarien ; fibrosarcome cardiaque ; fibrosarcome rénal | 99,32 % à 99,63 % | L5 | Hold |

Pour les indications de niveau L2, les données compilées comprennent des essais de phase II dédiés (liposarcome : NCT01506596 ; dermatofibrosarcome : NCT01059656, terminé prématurément avec 23 patients, et étude de phase II publiée PMID 32956651). Les indications de niveau L5 ne disposent d'aucun essai ni d'aucune publication.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

