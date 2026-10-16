---
layout: default
title: Dihydralazine
parent: Prédiction du modèle uniquement (L5)
nav_order: 242
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dihydralazine : nouvelle indication prédite, Maladie cardiaque (heart disease) (niveau de preuve L5). Indication d'origine : Non renseignée dans la licence (texte d'indication vide)"
monitor_inn: "dihydralazine"
predicted_indications: ["heart disease", "Pierre Robin syndrome associated with a chromosomal anomaly", "genetic syndromic Pierre Robin syndrome", "Laubry-Pezzi syndrome", "partial deletion of the long arm of chromosome 7", "orofacial clefting syndrome", "Jeune syndrome situs inversus", "disorder of fucoglycosan synthesis", "pulmonary valve disease", "partial deletion of the long arm of chromosome 22"]
---

# Dihydralazine
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

# Dihydralazine : De l'hypertension artérielle à la maladie cardiaque

## Résumé en Une Phrase

Dihydralazine est un vasodilatateur artériolaire à action directe, utilisé sous forme injectable (Nepressol) dans la prise en charge de l'hypertension. L'indication originale n'est pas renseignée dans la licence française compilée ; elle est déduite de la littérature et de la classe pharmacologique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **maladie cardiaque**, mais **aucun essai clinique ne confirme directement** cette direction (un seul essai de phase 3 est mentionné, sans que le rôle de la dihydralazine soit vérifié) et la littérature disponible est ancienne et indirecte (**19 publications**, principalement sur l'hypertension, l'insuffisance cardiaque et des études animales).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans la licence (texte d'indication vide) |
| Nouvelle Indication Prédite | Maladie cardiaque (heart disease) |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L5 (prédiction du modèle, essai associé non confirmé ; le dossier source indique L4) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, la dihydralazine appartient à la classe des hydrazinophtalazines, des vasodilatateurs artériels directs qui réduisent la résistance vasculaire systémique et donc la post-charge cardiaque.

Cette réduction de la post-charge explique un lien plausible avec des affections cardiaques comme le cœur hypertensif, l'insuffisance cardiaque ou l'hypertrophie ventriculaire. Plusieurs publications anciennes (1980-1985) ont d'ailleurs étudié son usage dans l'insuffisance cardiaque sévère, en France notamment sous le nom de Nepressol.

Il faut toutefois rester prudent : la littérature concerne surtout l'usage antihypertenseur déjà connu, et non une véritable nouvelle indication. Le score TxGNN très élevé est une prédiction computationnelle, pas une preuve clinique. Les autres prédictions (syndrome de Pierre Robin, délétions chromosomiques, maladie valvulaire pulmonaire, etc.) n'ont aucune justification mécanistique plausible et relèvent probablement d'artefacts du graphe de connaissances.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT05230901](https://clinicaltrials.gov/study/NCT05230901) | Phase 3 | Inconnu | 300 | Traitement antifibrotique (spironolactone, avec ou sans dihydralazine selon la description) pour la régression de la fibrose myocardique après TAVI dans la sténose aortique. Le rôle exact de la dihydralazine n'est pas confirmé ; pertinence jugée faible (grade C). |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [3075406](https://pubmed.ncbi.nlm.nih.gov/3075406/) | 1988 | Étude clinique comparative | Acta Physiol Hung | Comparaison à court terme de deux préparations de captopril et de la dihydralazine dans l'insuffisance cardiaque chronique sévère |
| [3159248](https://pubmed.ncbi.nlm.nih.gov/3159248/) | 1985 | Cohorte/Observationnelle | Am Heart J | Hypertrophie cardiaque et distensibilité artérielle dans l'hypertension essentielle |
| [6479183](https://pubmed.ncbi.nlm.nih.gov/6479183/) | 1984 | Étude clinique | Eur Heart J | Perte d'efficacité de la dihydralazine au long cours dans l'insuffisance cardiaque chronique (14 patients, versus placebo) |
| [7307999](https://pubmed.ncbi.nlm.nih.gov/7307999/) | 1981 | Étude clinique | Dtsch Med Wochenschr | Développement d'une tolérance aux vasodilatateurs dans l'insuffisance cardiaque congestive ; seule la dihydralazine réduit nettement la résistance systémique |
| [7449633](https://pubmed.ncbi.nlm.nih.gov/7449633/) | 1980 | Étude clinique | Dtsch Med Wochenschr | Effets hémodynamiques aigus comparés de l'isosorbide dinitrate, du prazosine et de la dihydralazine dans l'insuffisance cardiaque réfractaire |
| [4026112](https://pubmed.ncbi.nlm.nih.gov/4026112/) | 1985 | Article de synthèse | Ann Med Interne | Rôle de la dihydralazine (Nepressol) dans l'insuffisance cardiaque chronique |
| [6127295](https://pubmed.ncbi.nlm.nih.gov/6127295/) | 1982 | Revue | Fortschr Med | Traitement des cardiomyopathies, avec les vasodilatateurs dont la dihydralazine |
| [29974489](https://pubmed.ncbi.nlm.nih.gov/29974489/) | 2018 | Méta-analyse en réseau | Br J Clin Pharmacol | Médicaments de l'hypertension sévère de la grossesse |
| [8497771](https://pubmed.ncbi.nlm.nih.gov/8497771/) | 1993 | Revue | Schweiz Med Wochenschr | Crise hypertensive |
| [42117551](https://pubmed.ncbi.nlm.nih.gov/42117551/) | 2026 | Protocole d'essai | ESC Heart Fail | Conception de l'essai Reduce-MFA DZHK25 sur le traitement antifibrotique après TAVI |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67455336 (annulée) | NEPRESSOL 25 mg/2 ml, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | Non renseignée |

## Considérations de Sécurité

Les données de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité.

À noter, la littérature compilée signale des cas d'hépatite auto-immune induite par la dihydralazine (autoanticorps anti-CYP1A2), un signal de sécurité à prendre en compte avant tout repositionnement. Aucune interaction médicamenteuse n'a été identifiée dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose essentiellement sur le modèle : aucun essai ne confirme le rôle de la dihydralazine, la littérature est ancienne et indirecte, et la seule AMM française est annulée. Le signal d'hépatotoxicité auto-immune plaide aussi pour la prudence.

**Pour avancer, les éléments suivants sont nécessaires :**
- Vérifier si la dihydralazine est réellement un bras d'intervention de l'essai NCT05230901
- Récupérer la notice ANSM (mises en garde et contre-indications), donnée bloquante pour l'évaluation de sécurité
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Préciser l'indication originale et la précision de la formulation disponible
- Rechercher des essais contrôlés récents dans l'insuffisance cardiaque ou le cœur hypertensif
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

