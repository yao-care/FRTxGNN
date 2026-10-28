---
layout: default
title: Methylergometrine
parent: Prédiction du modèle uniquement (L5)
nav_order: 489
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Methylergometrine : nouvelle indication prédite, Hypertrichose (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM compilées (usage utérotonique s…"
monitor_inn: "methylergometrine"
predicted_indications: ["hypertrichosis (disease)", "pulmonary hypertension", "migraine disorder", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "kyphoscoliotic heart disease", "migraine with brainstem aura", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Methylergometrine
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

## Méthylergométrine : De l'usage obstétrical à l'hypertrichose (prédiction sans soutien clinique)
{: .text-alpha }

## Résumé en Une Phrase

La méthylergométrine est un alcaloïde de l'ergot de seigle semi-synthétique, utilisé à l'origine comme utérotonique (forme injectable en ampoule). Le modèle TxGNN la prédit comme potentiellement efficace pour l'**hypertrichose**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction. Pour la migraine, troisième prédiction du classement, seules **2 publications indirectes** ont été identifiées.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées (usage utérotonique selon les connaissances pharmacologiques) |
| Nouvelle Indication Prédite | Hypertrichose |
| Score de Prédiction TxGNN | 0,9987 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances pharmacologiques générales, la méthylergométrine est un alcaloïde de l'ergot agissant sur les récepteurs sérotoninergiques, dopaminergiques et alpha-adrénergiques, avec un effet utérotonique.

**Pour l'hypertrichose, la prédiction n'est pas étayée.** Aucune voie biologique ne relie ce médicament à la croissance pilaire. Le score élevé semble résulter d'une proximité dans le réseau de connaissances et non d'un mécanisme identifié. Les autres prédictions du classement (formes génétiques d'hypertrichose, anomalies de la tige pilaire, syndromes malformatifs, syndrome néphrogénique d'antidiurèse inappropriée) sont dans la même situation : aucune justification mécanistique ni preuve clinique.

**Deux prédictions soulèvent des préoccupations de sécurité.** Les dérivés de l'ergot agissant sur les récepteurs 5-HT2B sont associés à l'hypertension pulmonaire et à la fibrose valvulaire : la prédiction « hypertension pulmonaire » va donc à l'opposé d'un bénéfice attendu. De même, les agents vasoconstricteurs de cette classe sont généralement évités dans la migraine avec aura du tronc cérébral.

**La migraine est la seule piste plausible**, via l'agonisme 5-HT1B/1D des ergotés (ergotamine, dihydroergotamine) et le lien avec le méthysergide, ancien traitement de fond de la migraine. Cependant, il n'existe aucun essai de la méthylergométrine dans la migraine, et des alternatives plus sûres sont disponibles (triptans, antagonistes du CGRP).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature disponible pour l'hypertrichose. Pour la migraine (prédiction n° 3), deux revues indirectes ont été identifiées :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [18644039](https://pubmed.ncbi.nlm.nih.gov/18644039/) | 2008 | Revue | Cephalalgia | Historique du méthysergide dans la migraine, synthétisé à partir de l'acide lysergique ; contexte de la théorie vasculaire et sérotoninergique de la migraine |
| [9665056](https://pubmed.ncbi.nlm.nih.gov/9665056/) | 1998 | Revue | Circulation | Comparaison du potentiel vasoconstricteur coronarien des antimigraineux (ergotamine, méthysergide et son métabolite la méthylergométrine, triptans) ; met en évidence le risque cardiovasculaire de cette classe |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66417119 (annulée) | METHERGIN 0,20 mg/1 ml, solution injectable, ampoule | Solution injectable | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie, et non texte de la notice) : hypertension et troubles hypertensifs, épilepsie, maladie rénale, pyo-uretère, maladie hépatique, maladie de la vésicule biliaire, accident vasculaire cérébral et troubles cérébrovasculaires, infarctus cérébral, artériopathie oblitérante, syndrome HELLP.
- **Interactions médicamenteuses** : 92 interactions recensées. Les principales de niveau **majeur** : isométheptène, épinéphrine (y compris formes ophtalmique et topique), éphédrine (y compris nasale), lorcasérine, clarithromycine. Interactions de niveau modéré, notamment : doxycycline, tétracycline, minocycline, aprépitant, dexaméthasone, cimétidine, miconazole, clotrimazole.
- **Risque de classe** : vasoconstriction (risque coronarien et cérébral), hypertension pulmonaire et valvulopathie liées aux récepteurs 5-HT2B.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction principale (hypertrichose) repose uniquement sur le modèle (niveau L5), sans mécanisme plausible, essai ni publication. Le profil de sécurité vasculaire de la classe et la seule AMM française annulée renforcent la recommandation de ne pas poursuivre. La migraine (niveau L4) peut au mieux constituer une question de recherche, mais elle est désavantagée par le risque cardiovasculaire et par l'existence d'alternatives approuvées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mécanisme d'action détaillé (DrugBank)
- Mises en garde et contre-indications de la notice (ANSM), actuellement bloquantes pour le criblage de sécurité
- Indication originale documentée dans l'AMM
- Pour la migraine : données précliniques ou cliniques directes et évaluation du rapport bénéfice/risque cardiovasculaire par rapport aux traitements existants
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

