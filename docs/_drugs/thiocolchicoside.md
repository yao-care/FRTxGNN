---
layout: default
title: Thiocolchicoside
parent: Prédiction du modèle uniquement (L5)
nav_order: 753
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Thiocolchicoside : nouvelle indication prédite, Insomnie (niveau de preuve L5). Indication d'origine : Non précisée dans les données compilées"
monitor_inn: "THIOCOLCHICOSIDE"
predicted_indications: ["insomnia (disease)", "alcohol withdrawal delirium"]
drugbank_id: DB11582
---

# Thiocolchicoside
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Thiocolchicoside : D'un myorelaxant à l'insomnie, une prédiction non étayée
{: .text-alpha }

## Résumé en Une Phrase

Le thiocolchicoside est un dérivé semi-synthétique de la colchicoside, commercialisé en France sous forme de comprimés, gélules et solution injectable. Les données compilées pour ce rapport ne précisent pas son indication d'origine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**insomnie**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données compilées |
| Nouvelle Indication Prédite | Insomnie |
| Score de Prédiction TxGNN | 0,9989 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 9 sur 10) |
| Nombre d'AMM | 10 (valides : 9) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances pharmacologiques disponibles, le thiocolchicoside agirait comme antagoniste compétitif des récepteurs GABA-A et, selon certains rapports, des récepteurs de la glycine.

Cette pharmacologie va **à l'opposé** de l'effet sédatif-hypnotique des modulateurs positifs du GABA-A. L'antagonisme GABA-A est associé à des effets convulsivants et pro-excitateurs. Le score élevé du modèle (0,9989) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies voisines, et non une preuve biologique ; aucun mécanisme plausible n'est établi et la direction mécanistique est contradictoire.

Un éventuel bénéfice ne pourrait être qu'indirect, par exemple par le soulagement des spasmes musculaires et de la douleur qui perturbent le sommeil. Cette hypothèse reste spéculative.

**Autre prédiction du modèle : le delirium de sevrage alcoolique** (score de 0,9921). Le traitement standard repose sur des agonistes GABA-A (benzodiazépines). L'antagonisme GABA-A du thiocolchicoside risquerait d'aggraver l'hyperexcitabilité du système nerveux central et le risque de convulsions, déjà majeur lors du sevrage alcoolique. Cette piste est sans aucun appui clinique ni bibliographique, et le raisonnement mécanistique laisse craindre un préjudice potentiel.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement.

---

## Informations de Marché en France

Le texte des indications approuvées n'est pas renseigné dans les données compilées.

<!-- review:begin fr-lic-20261106-thiocolchicoside-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les 9 AMM recensées sont toutes annulées. Le texte des indications approuvées n'est pas renseigné dans les données compilées. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 9 AMM pour ce médicament, dont 9 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-thiocolchicoside-1 -->

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 69999429 | THIOCOLCHICOSIDE EG 4 mg, comprimé sécable | Comprimé sécable | EG LABO - LABORATOIRES EUROGENERICS | Active |
| 63646098 | THIOCOLCHICOSIDE ZENTIVA 4 mg, comprimé | Comprimé | ZENTIVA FRANCE | Active |
| 68086109 | THIOCOLCHICOSIDE CRISTERS 4 mg, comprimé | Comprimé | CRISTERS | Active |
| 65617572 | MIOREL 4 mg, gélule | Gélule | FARMACEUTICO SIT | Active |
| 67136662 | THIOCOLCHICOSIDE BIOGARAN 4 mg, comprimé | Comprimé | BIOGARAN | Active |
| 66305209 | MIOREL 4 mg/2 ml, solution injectable (IM) en ampoule | Solution injectable | FARMACEUTICO SIT | Active |
| 64045168 | THIOCOLCHICOSIDE ARROW 4 mg, comprimé | Comprimé | ARROW GENERIQUES | Active |
| 68268147 | THIOCOLCHICOSIDE VIATRIS 4 mg, comprimé | Comprimé | VIATRIS SANTE | Active |
| 67730031 | THIOCOLCHICOSIDE ALMUS 4 mg, comprimé | Comprimé | BIOGARAN | Active |
| 60855840 | THIOCOLCHICOSIDE ALTER 4 mg, comprimé | Comprimé | LABORATOIRES ALTER | Abrogée |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

À titre d'alerte, les données précliniques et de pharmacovigilance indiquent un potentiel pro-convulsivant du thiocolchicoside, ce qui plaide contre son utilisation dans les contextes à risque d'hyperexcitabilité du système nerveux central, comme le sevrage alcoolique.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les deux prédictions reposent uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Le mécanisme connu (antagonisme GABA-A) contredit l'effet recherché dans l'insomnie et suggère un risque dans le delirium de sevrage alcoolique.
- 9 AMM françaises sur 10 sont valides, et les données de sécurité issues de la notice font défaut.

<!-- review:begin fr-lic-20261124-thiocolchicoside-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Les 9 AMM françaises sur 9 sont valides » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans le Résumé rapide. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-thiocolchicoside-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse des notices ANSM (mises en garde et contre-indications), étape bloquante pour tout criblage de sécurité
- Données détaillées sur le mécanisme d'action (via DrugBank)
- Études précliniques ou cliniques justifiant un bénéfice réel dans l'insomnie, avec évaluation du risque convulsivant
- Aucune poursuite n'est recommandée pour le delirium de sevrage alcoolique en l'état, compte tenu du risque mécanistique

<!-- review:begin fr-lic-20261106-thiocolchicoside-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Données détaillées sur le mécanisme d'action (via DrugBank) / Clarification de l'indication d'origine et des raisons de l'annulation des AMM » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 9 AMM pour ce médicament, dont 9 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-thiocolchicoside-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Les 9 AMM recensées sont toutes annulées » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « Clarification de l'indication d'origine et des raisons de l'annulation des AMM » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

