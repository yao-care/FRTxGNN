---
layout: default
title: Fosfomycin
parent: Prédiction du modèle uniquement (L5)
nav_order: 348
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fosfomycin : nouvelle indication prédite, Urétrite gonococcique (niveau de preuve L5). Indication d'origine : Infection des voies urinaires"
monitor_inn: "fosfomycin"
predicted_indications: ["uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "epiglottitis", "urogenital tuberculosis", "laryngitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia"]
---

# Fosfomycin
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

# Fosfomycine : De l'infection urinaire à l'urétrite gonococcique

## Résumé en Une Phrase

La fosfomycine est un antibiotique initialement utilisé pour traiter les infections urinaires.
Le modèle TxGNN prédit qu'elle pourrait être efficace contre l'**urétrite gonococcique**.
Les données compilées pour ce rapport ne contiennent **aucun essai clinique enregistré**. Elles comportent **6 publications**, dont 1 essai randomisé (2016) et une série clinique ancienne (1977).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection des voies urinaires (le texte d'indication des AMM françaises n'est pas renseigné ; indication tirée du graphe de connaissances) |
| Nouvelle Indication Prédite | Urétrite gonococcique |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L3 (un essai randomisé ouvert dont la phase n'est pas confirmée, plus des séries cliniques ; critères L2 non démontrés) |
| Statut de Marché en France | Uniquement des AMM abrogées (aucune commercialisée) |
| Nombre d'AMM | 19 (toutes abrogées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données de mécanisme d'action issues de la base pharmacologique ne sont pas disponibles. D'après les connaissances générales, la fosfomycine inhibe l'enzyme MurA (UDP-N-acétylglucosamine énolpyruvyl transférase). Elle bloque ainsi la première étape de la synthèse du peptidoglycane de la paroi bactérienne et agit de façon bactéricide. *Neisseria gonorrhoeae* possède une paroi bactérienne, ce qui rend cette cible plausible.

L'urétrite gonococcique et l'infection urinaire sont toutes deux des infections bactériennes des voies génito-urinaires. La fosfomycine atteint de fortes concentrations urinaires, ce qui rapproche les deux indications. Cela explique en partie le score élevé du modèle.

Deux travaux cliniques publiés vont dans le sens d'une activité. Une série de 1977 rapporte environ 86 à 92 % de guérisons, selon le schéma. Un essai randomisé de 2016 a évalué la fosfomycine trométamol par voie orale. Le contexte actuel limite toutefois l'intérêt de cette piste : les résistances et les schémas de référence à base de ceftriaxone réduisent le besoin non couvert.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [27064136](https://pubmed.ncbi.nlm.nih.gov/27064136/) | 2016 | ECR (ouvert) | Clin Microbiol Infect | 152 hommes inclus avec une urétrite gonococcique non compliquée, 126 ayant terminé l'étude ; fosfomycine trométamol 3 g par voie orale aux jours 1, 3 et 5 dans le groupe intervention (60 patients) |
| [832528](https://pubmed.ncbi.nlm.nih.gov/832528/) | 1977 | Série clinique | Chemotherapy | 70 patients traités par fosfomycine intramusculaire ; 11 guérisons sur 12 (92 %) avec 4 g en doses fractionnées, 37 guérisons sur 43 (86 %) avec 4 g en dose unique |
| [832523](https://pubmed.ncbi.nlm.nih.gov/832523/) | 1977 | Évaluation clinique/bactériologique | Chemotherapy | Évaluation de 959 patients dans des hôpitaux espagnols, dont des urétrites gonococciques ; large spectre in vitro |
| [19593988](https://pubmed.ncbi.nlm.nih.gov/19593988/) | 2009 | Revue/clinique | Zhonghua Nan Ke Xue | Infections génito-urinaires masculines à *Neisseria* non gonococciques ; lien indirect |
| [35820778](https://pubmed.ncbi.nlm.nih.gov/35820778/) | 2023 | Analyse secondaire | Sex Transm Infect | Clairance spontanée de *N. gonorrhoeae* asymptomatique (essai NABOGO) ; non spécifique à la fosfomycine |
| [17878816](https://pubmed.ncbi.nlm.nih.gov/17878816/) | 2007 | Rapport de cas | J Fr Ophtalmol | Conjonctivite gonococcique compliquée chez un adulte, souche résistante aux pénicillines, tétracyclines et fluoroquinolones ; peu pertinent pour la fosfomycine |

## Informations de Marché en France

Les 19 AMM recensées sont abrogées. Les 5 premières sont listées ci-dessous (le texte d'indication approuvée n'est pas renseigné).

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 61935264 | Fosfomycine Viatris Adultes 3 g | Granulés pour solution buvable en sachet | Viatris Santé |
| 66430643 | Fosfomycine Arrow 3 g | Granulés pour solution buvable en sachet | Arrow Génériques |
| 65164104 | Fomicyt 4 g I.V. | Poudre pour solution à diluer pour perfusion | Infectopharm |
| 62884890 | Fosfomycine Cristers Pharma Adultes 3 g | Granulés pour solution buvable en sachet | Cristers |
| 61334559 | Fosfomycine Teva Santé Adultes 3 g | Granulés pour solution buvable en sachet | Teva Santé |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations du graphe, et non texte de notice) : maladie rénale, pyo-uretère, colite à *Clostridium difficile*, entérocolite nécrosante périnatale.
- **Interactions médicamenteuses** (3 identifiées) :
  - Balsalazide : modérée
  - Acide picosulfurique : modérée
  - Métoclopramide : mineure

Les mises en garde et contre-indications officielles de la notice ne figurent pas dans les données compilées. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les preuves se limitent à un essai randomisé ouvert de 2016, dont la phase n'est pas confirmée, et à des séries anciennes ; aucun essai n'est enregistré.
- Les résistances, les schémas de référence à base de ceftriaxone et l'absence d'AMM en cours de validité limitent l'intérêt d'un développement.

À titre de comparaison, la prédiction **pyélite** (infection urinaire haute) repose sur un signal bien plus solide. Elle s'appuie sur l'essai de phase 2/3 ZEUS (fosfomycine IV contre pipéracilline-tazobactam dans l'infection urinaire compliquée) et sur des revues récentes. Elle représente surtout une extension de l'indication d'origine vers la forme intraveineuse. Elle mérite une évaluation distincte, avec des garde-fous : forme IV nécessaire, charge sodée, surveillance de l'hypokaliémie, sensibilité locale.

**Pour avancer, les éléments suivants sont nécessaires :**
- Confirmer la phase, la méthodologie et les critères de jugement de l'essai randomisé de 2016, et analyser ses résultats complets.
- Disposer de données récentes de sensibilité de *N. gonorrhoeae* à la fosfomycine et les comparer aux recommandations en vigueur.
- Obtenir les mises en garde et contre-indications officielles de la notice et les données détaillées sur le mécanisme d'action.
- Clarifier la disponibilité réelle d'un produit en France, toutes les AMM étant abrogées.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

