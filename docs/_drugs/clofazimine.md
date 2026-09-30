---
layout: default
title: Clofazimine
parent: Prédiction du modèle uniquement (L5)
nav_order: 83
evidence_level: L5
indication_count: 3
---

# Clofazimine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

# Clofazimine : De l'indication d'origine non documentée à la pneumocystose

## Résumé en Une Phrase

La clofazimine est commercialisée en France sous le nom LAMPRENE (Novartis Pharma), mais le dossier ne précise pas son indication d'origine. La littérature la montre utilisée dans des schémas contre la lèpre et la tuberculose résistante, ainsi que pour la prophylaxie de l'infection à *Mycobacterium avium* complex (MAC) chez des patients atteints du sida.
Le modèle TxGNN prédit qu'elle pourrait être efficace contre la **pneumocystose**, avec **1 essai clinique** et **4 publications** associés. Aucun de ces documents ne démontre une activité de la clofazimine contre *Pneumocystis*.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM fournies |
| Nouvelle Indication Prédite | Pneumocystose |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement, aucune étude directe sur la pneumocystose) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Aucun lien mécanistique entre la clofazimine et la pneumocystose ne peut donc être établi.

Dans la littérature retrouvée, la clofazimine apparaît dans la prophylaxie de l'infection à MAC chez des patients infectés par le VIH. La pneumocystose (*Pneumocystis carinii pneumonia*) y figure uniquement comme infection opportuniste associée. Dans un cas décrit, elle a été traitée par triméthoprime-sulfaméthoxazole, et non par la clofazimine. Le seul point commun est la population de patients immunodéprimés.

Le score TxGNN est très élevé, mais il reste une prédiction de modèle. Aucune donnée réelle ne le confirme à ce jour.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00002058](https://clinicaltrials.gov/study/NCT00002058) | Non applicable | Terminé | Non renseignée | Étude randomisée de prophylaxie par la clofazimine contre l'infection à *Mycobacterium avium* complex chez des patients infectés par le VIH. Elle ne concerne pas *Pneumocystis* (pertinence : faible, grade C). |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [8501340](https://pubmed.ncbi.nlm.nih.gov/8501340/) | 1993 | Essai randomisé ouvert (prophylaxie MAC) | J Infect Dis | 110 patients atteints du sida, dont certains avec un antécédent de pneumocystose. La clofazimine (50 mg) a été évaluée en prophylaxie de l'infection disséminée à MAC. |
| [11363899](https://pubmed.ncbi.nlm.nih.gov/11363899/) | 1996 | Revue | PI Perspective | Mise à jour générale sur les infections opportunistes. Pas de résumé disponible. |
| [2714863](https://pubmed.ncbi.nlm.nih.gov/2714863/) | 1989 | Rapport de cas | Infection | Patient atteint du sida avec infection à *M. kansasii*, traité par isoniazide, éthambutol, clofazimine et ciprofloxacine. La pneumocystose, survenue ensuite, a été traitée par triméthoprime-sulfaméthoxazole. |
| [6299154](https://pubmed.ncbi.nlm.nih.gov/6299154/) | 1983 | Rapport de cas | Ann Intern Med | Patient hémophile atteint du sida avec pneumocystose et bactériémie à *M. avium-intracellulare*. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 62768220 | LAMPRENE 50 mg | Capsule molle |
| 67132888 | LAMPRENE 100 mg | Capsule molle |

Les deux AMM sont détenues par Novartis Pharma, pour une voie orale uniquement.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucune preuve directe ne soutient l'efficacité de la clofazimine contre la pneumocystose. L'essai unique porte sur le MAC, et les autres documents sont des rapports de cas où la pneumocystose est une infection concomitante.
- Le dossier ne contient ni données de mécanisme ni données de sécurité issues de la notice ANSM. Ce déficit bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications, indication approuvée).
- Obtenir les données de mécanisme d'action via DrugBank.
- Rechercher des données précliniques d'activité de la clofazimine contre *Pneumocystis*.
- Documenter l'indication d'origine à partir du RCP.

**Autres prédictions du modèle** (paludisme, anomalie de sécrétion de gastrine) : elles ne sont pas évaluées ici. Le paludisme repose uniquement sur des données in vitro d'analogues de la clofazimine (hypothèse à explorer). Pour l'anomalie de sécrétion de gastrine, aucune preuve n'a été retrouvée.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

