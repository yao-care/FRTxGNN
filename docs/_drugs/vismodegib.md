---
layout: default
title: Vismodegib
parent: Prédiction du modèle uniquement (L5)
nav_order: 817
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Vismodegib : nouvelle indication prédite, Médulloblastome avec nodularité extensive (niveau de preuve L5). Indication d'origine : Carcinome basocellulaire (et autres cancers cutanés ou annexiels)"
monitor_inn: "vismodegib"
predicted_indications: ["medulloblastoma with extensive nodularity", "xeroderma pigmentosum", "annular epidermolytic ichthyosis", "epidermolysis bullosa simplex with mottled pigmentation", "prostate cancer/brain cancer susceptibility", "Brenner tumor", "cutaneous adenocystic carcinoma", "prostate leiomyoma", "skin cancer", "benign neoplasm of sweat gland"]
---

# Vismodegib
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

# Vismodégib : Du carcinome basocellulaire au médulloblastome avec nodularité extensive

## Résumé en Une Phrase

Le vismodégib (ERIVEDGE 150 mg, gélule) est un inhibiteur de la voie Hedgehog, initialement utilisé pour traiter le carcinome basocellulaire et d'autres cancers cutanés.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **médulloblastome avec nodularité extensive**.
Pour cette indication précise, **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carcinome basocellulaire (et autres cancers cutanés ou annexiels) |
| Nouvelle Indication Prédite | Médulloblastome avec nodularité extensive |
| Score de Prédiction TxGNN | 99,93 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Retiré (AMM annulée uniquement) |
| Nombre d'AMM | 1 (0 valide, 1 annulée) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les informations connues, le vismodégib inhibe la protéine Smoothened (SMO) de la voie de signalisation Hedgehog. Cette voie est anormalement activée dans le carcinome basocellulaire, ce qui explique l'efficacité du médicament dans cette indication.

Le médulloblastome du sous-groupe SHH est lui aussi porté par une activation de la voie Hedgehog. Le lien biologique est donc plausible : le même point d'action (SMO) pourrait être pertinent dans les deux maladies.

Cette plausibilité reste théorique. Les données compilées ne contiennent ni essai ni publication portant sur ce sous-type de médulloblastome. Le soutien se limite à la prédiction du modèle, sans confirmation clinique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67507605 | ERIVEDGE 150 mg, gélule (ROCHE REGISTRATION, Allemagne) | Gélule | Non précisée dans les données (AMM annulée) |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de la voie Hedgehog / SMO), et non cytotoxique conventionnel |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter la notice ; appliquer les règles de manipulation des médicaments anticancéreux oraux |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 56 interactions sont référencées. Parmi celles listées dans les données compilées :
  - **Modérée** : clarithromycine.
  - **Mineures** : antiacides et protecteurs gastriques, dont les inhibiteurs de la pompe à protons (oméprazole, ésoméprazole, lansoprazole, pantoprazole, rabéprazole, dexlansoprazole), les anti-H2 (famotidine, ranitidine, cimétidine, nizatidine), l'hydroxyde d'aluminium, le carbonate de calcium, les sels de magnésium, le bicarbonate de sodium et le citrate de sodium.
- **Contexte pour d'autres indications** : la littérature associée à d'autres indications prédites signale des effets indésirables connus (alopécie, spasmes musculaires, dysgueusie, perte de poids) et une tératogénicité. La sécurité chez l'enfant demande une attention particulière, ce qui est pertinent pour le médulloblastome, fréquent dans cette population.

Pour les mises en garde et contre-indications détaillées, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le lien mécanistique (inhibition de SMO dans un médulloblastome dépendant de Hedgehog) est plausible. Mais l'indication repose uniquement sur le score du modèle, sans essai ni publication, et l'unique AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Une recherche ciblée de données précliniques et cliniques sur le médulloblastome du sous-groupe SHH traité par inhibiteurs de SMO.
- Les données détaillées sur le mécanisme d'action.
- Les mises en garde et contre-indications officielles de la notice.
- Une évaluation de la sécurité pédiatrique (tératogénicité, effets sur la croissance).
- Une clarification du statut réglementaire en France, l'AMM étant annulée.

À titre d'orientation complémentaire, parmi les autres indications prédites, le **xeroderma pigmentosum** est la mieux documentée (trois publications, dont deux cas cliniques de traitement par vismodégib de carcinomes basocellulaires associés). L'effet est cependant indirect : il traite la complication tumorale et non le défaut de réparation de l'ADN.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

