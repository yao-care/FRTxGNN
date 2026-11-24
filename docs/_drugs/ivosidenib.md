---
layout: default
title: Ivosidenib
parent: Prédiction du modèle uniquement (L5)
nav_order: 421
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "ivosidenib"
predicted_indications: ["bulbar polio"]
description: "Ivosidenib : nouvelle indication prédite, Poliomyélite bulbaire (bulbar polio) (niveau de preuve L5). En France, AMM dans la BDPM : 1 (valides : 1)"
---

# Ivosidenib
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

## Ivosidenib: Poliomyélite bulbaire (bulbar polio)
{: .text-alpha }

## Résumé en Une Phrase

Ivosidénib est un inhibiteur de l'enzyme IDH1 mutée, initialement utilisé dans le traitement de la leucémie myéloïde aiguë (LAM).
Le modèle TxGNN (apprentissage profond) prédit qu'il pourrait être efficace pour la **poliomyélite bulbaire**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction. L'analyse mécanistique ne retient aucun lien biologique plausible : le score élevé provient du modèle TxGNN et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Poliomyélite bulbaire (bulbar polio) |
| Score de Prédiction TxGNN | 0.9931 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Ivosidenib (traduction non officielle) : « L'ivosidénib est un inhibiteur de petite molécule qui cible l'enzyme isocitrate déshydrogénase 1 (IDH1) mutante. Chez les patients atteints de LAM, les mutations sensibles d'IDH1 sont définies comme celles entraînant des taux accrus de 2-hydroxyglutarate (2-HG) dans les cellules leucémiques et pour lesquelles l'efficacité est prédite par 1) des rémissions cliniquement significatives à la dose recommandée d'ivosidénib et/ou 2) une inhibition de l'activité enzymatique d'IDH1 mutante à des concentrations d'ivosidénib pouvant être maintenues à la posologie recommandée selon des méthodes validées. » Texte original en anglais : "Ivosidenib is a small molecule inhibitor that targets the mutant isocitrate dehydrogenase 1 (IDH1) enzyme. In patients with AML, susceptible IDH1 mutations are defined as those leading to increased levels of 2-hydroxyglutarate (2-HG) in the leukemia cells and where efficacy is predicted by 1) clinically meaningful remissions with the recommended dose of ivosidenib and/or 2) inhibition of mutant IDH1 enzymatic activity at concentrations of ivosidenib sustainable at the recommended dosage according to validated methods." ([DailyMed: Tibsovo (ivosidenib) prescribing information, Servier Pharmaceutical LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=65d254c0-67ad-42c4-b972-ad463b755b2d), version du 2025-12-22 ; consulté le 2026-11-19). Sur la base des connaissances générales, l'ivosidénib inhibe l'isocitrate déshydrogénase 1 (IDH1) mutée. Il réduit l'oncométabolite 2-hydroxyglutarate (2-HG) et lève le blocage de différenciation observé dans les hémopathies myéloïdes porteuses d'une mutation IDH1.

La poliomyélite bulbaire est une infection virale des motoneurones causée par le poliovirus. Elle ne dépend ni d'une mutation d'IDH1 ni de la signalisation par le 2-HG. **Aucun lien mécanistique plausible n'a été identifié** entre l'indication d'origine et cette nouvelle indication. Le score TxGNN très élevé (0,9931) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une justification biologique.

### Autres prédictions du modèle

Deux autres prédictions de score très proche (0,9931) sont biologiquement plus plausibles :

- **LAM et syndromes myélodysplasiques liés à la radiothérapie**
- **LAM et syndromes myélodysplasiques liés aux agents alkylants**

Ces entités sont des néoplasmes myéloïdes secondaires à un traitement, qui peuvent porter une mutation IDH1 dans une partie des cas. Un bénéfice éventuel serait limité aux patients porteurs de la mutation, quelle que soit l'étiologie. Elles recoupent largement les indications déjà listées (LAM et SMD liés au traitement, LAM liée aux inhibiteurs de la topoisomérase II). Il vaut mieux les traiter comme une question de sous-groupe défini par biomarqueur ou d'extension d'indication existante que comme un vrai repositionnement. Aucun essai ni publication spécifique n'a été fourni pour ces sous-types.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 63239234 | TIBSOVO 250 mg, comprimé pelliculé | Comprimé pelliculé | LES LABORATOIRES SERVIER | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur d'IDH1 mutée) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

Les mises en garde et contre-indications de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

- **Interactions Médicamenteuses** : 413 interactions sont recensées. Parmi les principales, de niveau **majeur** :
  - Aprépitant
  - Clarithromycine
  - Dolasétron
  - Palonosétron
  - Cisapride
  - Granisétron
  - Lévofloxacine

  Des interactions de niveau **modéré** sont aussi rapportées, notamment avec :
  - Famotidine
  - Lopéramide
  - Bisacodyl
  - Saxagliptine
  - Éliglustat
  - Linagliptine
  - Plusieurs laxatifs et préparations de lavage intestinal (picosulfate, polyéthylène glycol, sulfate de sodium, huile de ricin, glycérine, lactitol, lactulose)

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la poliomyélite bulbaire repose uniquement sur le modèle (niveau L5). Elle n'a aucun essai ni publication à l'appui et aucun lien mécanistique plausible.

<!-- review:begin fr-lic-20261106-ivosidenib-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Elle n'a aucun essai ni publication à l'appui et aucun lien mécanistique plausible. L'AMM française est de plus annulée. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-ivosidenib-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour l'évaluation de sécurité)
- Compléter les données sur le mécanisme d'action (via DrugBank)
- Pour la poliomyélite bulbaire : une justification biologique indépendante, faute de quoi la piste devrait être abandonnée
- Pour les LAM/SMD liés à la radiothérapie ou aux agents alkylants : évaluer la piste comme sous-groupe défini par le statut mutationnel IDH1, avec recherche d'études spécifiques

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « L'AMM française est de plus annulée » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-12 | Tableau : l’AMM 63239234 (TIBSOVO 250 mg) est active, non annulée | Remplacé par le tableau d'AMM généré par programme (auparavant : Corrigé) | [Base de données publique des médicaments (BDPM)](https://base-donnees-publique.medicaments.gouv.fr/) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Tibsovo (ivosidenib) prescribing information, Servier Pharmaceutical LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=65d254c0-67ad-42c4-b972-ad463b755b2d) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

