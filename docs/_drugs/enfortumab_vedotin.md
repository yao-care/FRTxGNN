---
layout: default
title: Enfortumab Vedotin
parent: Prédiction du modèle uniquement (L5)
nav_order: 282
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Enfortumab Vedotin : nouvelle indication prédite, Lèpre (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM"
monitor_inn: "enfortumab vedotin"
predicted_indications: ["leprosy", "multiple endocrine neoplasia", "cytomegalovirus infection", "candidiasis", "cerebral infarction", "HIV infectious disease", "homozygous familial hypercholesterolemia", "malignant catarrh", "infectious bovine rhinotracheitis"]
---

# Enfortumab Vedotin
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

# Enfortumab vedotin : D'un médicament antinéoplasique à la lèpre (prédiction non étayée)

## Résumé en Une Phrase

L'enfortumab vedotin est un conjugué anticorps-médicament ciblant la Nectine-4 et délivrant la MMAE (un agent perturbateur des microtubules). Les données compilées pour ce rapport ne précisent pas d'indication originale (aucun texte d'indication n'est renseigné dans les AMM françaises).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **lèpre**, mais **aucun essai clinique** et **aucune publication** ne soutiennent cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Lèpre |
| Score de Prédiction TxGNN | 99,53 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les informations connues, l'enfortumab vedotin est un conjugué anticorps-médicament dirigé contre la Nectine-4, qui libère la MMAE, un agent cytotoxique perturbant les microtubules, dans les cellules tumorales exprimant cette cible.

Aucun lien mécanistique n'est établi entre ce mode d'action et l'infection par *Mycobacterium leprae*. Rien dans les données ne relie le ciblage de la Nectine-4 ou la délivrance d'une charge cytotoxique à la lèpre. Le score TxGNN élevé (0,995) reflète vraisemblablement des artefacts liés à la structure du réseau de connaissances plutôt qu'une plausibilité biologique.

Les autres prédictions du modèle (néoplasie endocrinienne multiple, infection à cytomégalovirus, candidose, infarctus cérébral, infection par le VIH, hypercholestérolémie familiale homozygote, etc.) présentent le même constat : aucun essai clinique, aucun rationnel mécanistique, et le niveau de preuve reste L5 pour toutes.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la lèpre.

À titre d'information, deux publications liées à d'autres indications prédites sont des signaux de sécurité et non des preuves thérapeutiques :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [42647281](https://pubmed.ncbi.nlm.nih.gov/42647281/) | 2026 | Rapport de cas | Reports (MDPI) | Œsophagite ulcérative diffuse sévère sous enfortumab vedotin et pembrolizumab dans le carcinome urothélial métastatique (événement indésirable) |
| [41341429](https://pubmed.ncbi.nlm.nih.gov/41341429/) | 2025 | Pharmacovigilance (FAERS) | Clinical Epidemiology | Signaux de risque des conjugués anticorps-médicament dans le cancer de la vessie en vie réelle |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67032044 | PADCEV 20 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | Non renseignée (AMM annulée) |
| 67688034 | PADCEV 30 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | Non renseignée (AMM annulée) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Conjugué anticorps-médicament (thérapie ciblée) avec charge cytotoxique (MMAE) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter la notice (NFS, fonction hépatique et rénale, glycémie à envisager) |
| Protection de Manipulation | Manipulation selon les réglementations applicables aux médicaments cytotoxiques |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 147 interactions recensées. Parmi celles listées, une est de niveau **majeur** (clarithromycine) ; les autres sont de niveau **modéré**, notamment les antidiabétiques (acarbose, metformine, pioglitazone, glimépiride, glipizide, glibenclamide, inhibiteurs de la DPP-4, inhibiteurs du SGLT2, analogues du GLP-1) et l'aprépitant.

Les mises en garde et contre-indications de la notice ne sont pas disponibles dans les données compilées ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la lèpre repose uniquement sur le score du modèle, sans essai, sans publication ni lien mécanistique. Le niveau de preuve est L5, et les AMM françaises sont toutes annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (DrugBank) et analyse d'un éventuel lien Nectine-4 / infection mycobactérienne
- Mises en garde et contre-indications issues de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Indications originales approuvées et clarification du statut des AMM annulées
- Données précliniques ou études de mécanisme justifiant la plausibilité biologique avant tout essai clinique
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

