---
layout: default
title: Dabigatran Etexilate
parent: Prédiction du modèle uniquement (L5)
nav_order: 207
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-31
description: "Dabigatran Etexilate : nouvelle indication prédite, Cholangite sclérosante (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM (texte d'indication vide)"
monitor_inn: "dabigatran etexilate"
predicted_indications: ["sclerosing cholangitis", "obsolete familial combined hyperlipidemia", "hypoalphalipoproteinemia", "homozygous familial hypercholesterolemia", "primary release disorder of platelets"]
---

# Dabigatran Etexilate
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

## Dabigatran etexilate : De l'anticoagulation à la cholangite sclérosante
{: .text-alpha }

## Résumé en une phrase

Le dabigatran etexilate (PRADAXA et génériques) est un anticoagulant oral. Les données compilées pour ce rapport ne précisent pas son indication d'origine dans les AMM françaises.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **cholangite sclérosante**, avec un score élevé. En pratique, **aucun essai clinique** et **une seule publication** (étude pharmacocinétique portant sur un autre médicament) sont associés à cette prédiction. Cette direction repose donc uniquement sur le modèle.

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Non renseignée dans les données d'AMM (texte d'indication vide) |
| Nouvelle indication prédite | Cholangite sclérosante |
| Score de prédiction TxGNN | 0,9982 |
| Niveau de preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | au moins 20 |
| Décision recommandée | Hold |

## Pourquoi cette prédiction est-elle raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les connaissances générales, le dabigatran etexilate est la prodrogue du dabigatran, un inhibiteur direct de la thrombine. Il est utilisé comme anticoagulant, mais son indication d'origine n'est pas documentée dans les données compilées.

Un lien mécanistique plausible, mais **non vérifié**, existe : la signalisation thrombine/PAR-1 contribuerait à la fibrose hépatique et biliaire. Une inhibition directe de la thrombine pourrait donc, en théorie, moduler la fibrogenèse. Aucune donnée fournie ne confirme cette hypothèse.

Le seul article associé (PMID 36906733) évalue les interactions médicamenteuses du cilofexor, un agoniste du récepteur FXR, dans le développement pour la stéatohépatite non alcoolique et la cholangite sclérosante primitive. Il s'agit d'une étude pharmacocinétique qui ne concerne pas le dabigatran et ne dit rien de son efficacité dans cette maladie.

## Preuves d'essais cliniques

Aucun essai clinique associé n'est enregistré actuellement pour la cholangite sclérosante.

## Preuves de la littérature

| PMID | Année | Type | Revue | Résultats principaux |
|------|-----|------|------|---------|
| [36906733](https://pubmed.ncbi.nlm.nih.gov/36906733/) | 2023 | Étude pharmacocinétique / interactions médicamenteuses | Clinical Pharmacokinetics | Évaluation du potentiel d'interactions (cytochrome P450 et transporteurs) du cilofexor, agoniste FXR en développement dans la cholangite sclérosante primitive. Ne concerne pas le dabigatran. |

## Informations de marché en France

20 AMM valides en France, médicament commercialisé. Le texte d'indication n'est pas renseigné dans les données.

| Numéro d'AMM | Nom du produit | Forme pharmaceutique | Indication approuvée |
|---------|------|------|-----------|
| 62186316 | PRADAXA 110 mg, granulés enrobés | Granulés enrobés | Non renseignée |
| 68370173 | DABIGATRAN ETEXILATE BIOGARAN 75 mg | Gélule | Non renseignée |
| 65570603 | PRADAXA 110 mg | Gélule | Non renseignée |
| 68185986 | DABIGATRAN ETEXILATE ZENTIVA K.S. 75 mg | Gélule | Non renseignée |
| 63793251 | DABIGATRAN ETEXILATE VIATRIS SANTE 110 mg | Gélule | Non renseignée |

*Cinq AMM sont présentées sur un total de 20.*

## Considérations de sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie du graphe PrimeKG, et non texte de notice) : troubles de la coagulation, anémie, anémie macrocytaire, hémorragie intracérébrale.

Pour les mises en garde, les contre-indications officielles et les interactions médicamenteuses, veuillez consulter la notice.

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé (0,9982), mais il n'est soutenu par aucun essai ni aucune publication pertinente (niveau L5). Le lien mécanistique reste hypothétique.
- Le médicament est commercialisé en France (20 AMM valides), mais les données de sécurité officielles sont absentes, ce qui bloque l'étape de sélection de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications).
- Obtenir les données sur le mécanisme d'action depuis DrugBank.
- Confirmer l'indication d'origine et clarifier la raison de l'annulation des AMM.
- Mener des études précliniques sur le rôle de la thrombine dans la fibrose biliaire, puis un éventuel essai exploratoire.
- Évaluer le risque hémorragique chez les patients atteints de cholangite sclérosante, notamment en cas d'hypertension portale ou de varices.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

