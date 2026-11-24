---
layout: default
title: Sulfamethoxazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 720
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "sulfamethoxazole"
predicted_indications: ["acute contagious conjunctivitis"]
description: "Sulfamethoxazole : nouvelle indication prédite, Conjonctivite aiguë contagieuse (acute contagious conjunctivitis) (niveau de preuve L5). En France, AMM dans la BDPM : 6 (valides : 6)"
---

# Sulfamethoxazole
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Sulfamethoxazole: Conjonctivite aiguë contagieuse (acute contagious conjunctivitis)
{: .text-alpha }

## Résumé en Une Phrase

Le sulfaméthoxazole est un antibiotique de la famille des sulfamides, initialement utilisé pour traiter diverses infections (otite moyenne infectieuse, nocardiose, toxoplasmose, pneumocystose, shigellose, conjonctivite, maladie des griffes du chat, entre autres).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **conjonctivite aiguë contagieuse**. Cette indication figure toutefois déjà parmi ses indications d'origine : il ne s'agit donc pas d'un véritable repositionnement.
Les preuves actuelles se limitent à **1 publication** (étude de cohorte) et **aucun essai clinique**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Conjonctivite aiguë contagieuse (acute contagious conjunctivitis) |
| Score de Prédiction TxGNN | 0.9963 |
| Niveau de Preuve | L5 (niveau attribué dans les données compilées ; une seule étude de cohorte observationnelle, aucun essai clinique) |
| Statut de Marché en France | Commercialisé (autorisations valides : 6 sur 6) |
| Nombre d'AMM | 6 (valides : 6) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon ChEMBL (EMBL-EBI), le mécanisme d'action enregistré pour Sulfamethoxazole est (traduction non officielle) : « Inhibiteur de la dihydroptéroate synthase bactérienne ». Texte original en anglais : "Bacterial dihydropteroate synthase inhibitor" ([ChEMBL CHEMBL443 (sulfamethoxazole): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL443), CC BY-SA 3.0 ; consulté le 2026-11-19). Sur la base des connaissances pharmacologiques générales, le sulfaméthoxazole inhibe la dihydroptéroate synthase bactérienne et bloque ainsi la synthèse des folates, ce qui freine la croissance des bactéries. Cette inférence ne provient pas des données fournies.

Ce mécanisme antibactérien est cohérent avec une conjonctivite d'origine bactérienne. Cependant, la conjonctivite figure déjà parmi les indications d'origine du médicament dans le graphe de connaissances. Le score élevé du modèle (0,9963) reflète probablement cette association existante plutôt qu'une découverte nouvelle, et il reste une simple prédiction.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31788487](https://pubmed.ncbi.nlm.nih.gov/31788487/) | 2019 | Cohorte (rétrospective) | Medical Hypothesis, Discovery & Innovation Ophthalmology Journal | Analyse de la bactériologie et de la sensibilité aux antibiotiques dans les conjonctivites bactériennes aiguës de l'enfant, dans l'ouest de la Grèce (hôpital pédiatrique de Patras, 2013 et après) |

Cette étude décrit les profils de sensibilité aux antibiotiques ; le résumé disponible ne permet pas de confirmer qu'elle évalue directement le sulfaméthoxazole.

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 69464049 | BACTRIM 40 mg/mL + 8 mg/mL, suspension buvable | Suspension buvable | EUMEDICA PHARMACEUTICALS (ALLEMAGNE) | Active |
| 67891013 | COTRIMOXAZOLE TEVA 800 mg/160 mg, comprimé | Comprimé | TEVA SANTE | Active |
| 69233327 | BACTRIM, solution injectable pour perfusion | Solution injectable pour perfusion | EUMEDICA PHARMACEUTICALS (ALLEMAGNE) | Active |
| 64121235 | BACTRIM FORTE, comprimé sécable | Comprimé sécable | EUMEDICA PHARMACEUTICALS (ALLEMAGNE) | Active |
| 65880598 | BACTRIM, suspension buvable | Suspension buvable | EUMEDICA PHARMACEUTICALS (ALLEMAGNE) | Active |
| 65181349 | BACTRIM, comprimé sécable | Comprimé sécable | EUMEDICA PHARMACEUTICALS (ALLEMAGNE) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie, et non texte de la notice) : porphyries (héréditaire et autres troubles du métabolisme des porphyrines), maladie rénale, insuffisance rénale, urémie, glomérulonéphrite, maladie hépatique, maladie de la vésicule biliaire, thrombopénie, neutropénie, agranulocytose, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, déficit en G6PD, anémie par carence en acide folique, glycogénose, cystinurie, galactosémie.
- **Interactions médicamenteuses** : 151 interactions recensées. Parmi celles listées :
  - Niveau modéré : sulfamides hypoglycémiants (chlorpropamide, glimépiride, acétohexamide, glipizide, glibenclamide), insulines (humaine, asparte, dégludec, détémir, glargine, glulisine), balsalazide, acide picosulfurique.
  - Niveau mineur : famotidine, clarithromycine, dolasétron, palonosétron, cisapride, granisétron.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La conjonctivite figure déjà parmi les indications d'origine du médicament : il ne s'agit pas d'un vrai repositionnement. Les preuves se limitent à une étude de cohorte, sans essai clinique ; le médicament est commercialisé en France, avec 6 AMM valides sur 6. Les données de sécurité de la notice manquent, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications)
- Obtenir les données sur le mécanisme d'action via DrugBank
- Vérifier si la formulation (notamment ophtalmique) est compatible avec l'indication, aucune donnée de voie d'administration n'étant disponible

<!-- review:begin fr-lic-20261106-sulfamethoxazole-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Obtenir les données sur le mécanisme d'action via DrugBank / Clarifier la pertinence d'une évaluation, compte tenu de l'indication déjà existante et du statut annulé des AMM » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-sulfamethoxazole-1 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Clarifier la pertinence d'une évaluation, compte tenu de l'indication déjà existante et du statut annulé des AMM » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé (révisé le 2026-11-20 ; version antérieure conservée dans le journal) | [ChEMBL CHEMBL443 (sulfamethoxazole): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL443) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

