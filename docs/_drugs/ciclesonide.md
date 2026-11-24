---
layout: default
title: Ciclesonide
parent: Prédiction du modèle uniquement (L5)
nav_order: 167
evidence_level: L5
indication_count: 5
monitor_inn: "ciclesonide"
predicted_indications: ["atopic eczema", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "bronchitis", "contact dermatitis"]
last_modified_at: 2026-11-24
description: "Ciclesonide : nouvelle indication prédite, Eczéma atopique (atopic eczema) (niveau de preuve L5). En France, AMM dans la BDPM : 2 (valides : 2)"
---

# Ciclesonide
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

## Ciclésonide : corticoïde inhalé (promédicament, agoniste du récepteur des glucocorticoïdes) → Eczéma atopique (atopic eczema)
{: .text-alpha }

## Résumé en Une Phrase

La ciclésonide est un corticoïde inhalé, administré sous forme de solution pour inhalation en flacon pressurisé.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**eczéma atopique (atopic eczema)**, avec un score de 0,9996.
Aucun essai clinique ni aucune publication ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Eczéma atopique (atopic eczema) |
| Score de Prédiction TxGNN | 0,9996 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Ciclesonide (traduction non officielle) : « Le ciclésonide est une prodrogue qui est hydrolysée par voie enzymatique en un métabolite pharmacologiquement actif, le C21-désisobutyryl-ciclésonide (des-ciclésonide ou RM1), après inhalation par voie orale. Le des-ciclésonide possède une activité anti-inflammatoire avec une affinité pour les récepteurs des glucocorticoïdes 120 fois supérieure à celle de la molécule mère et 12 fois supérieure à celle de la dexaméthasone. » Texte original en anglais : "Ciclesonide is a prodrug that is enzymatically hydrolyzed to a pharmacologically active metabolite, C21-desisobutyryl-ciclesonide (des-ciclesonide or RM1) following oral inhalation. Des-ciclesonide has anti-inflammatory activity with affinity for glucocorticoid receptors that is 120 times greater than the parent compound and 12 times greater than dexamethasone." ([DailyMed: Alvesco (ciclesonide) prescribing information, Covis Pharma US, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9f6112fb-78ef-43cf-8ae3-36370eb45468), version du 2025-02-28 ; consulté le 2026-11-19). D'après les informations connues, la ciclésonide est un promédicament : des estérases l'activent en desciclésonide, un agoniste du récepteur des glucocorticoïdes à activité anti-inflammatoire.

Les corticoïdes, topiques ou systémiques, sont un traitement établi de l'eczéma atopique. Le mécanisme anti-inflammatoire est donc plausible pour cette maladie.

Cette plausibilité reste théorique. Le score est très élevé (0,9996), mais aucune étude n'a été fournie pour ce médicament dans cette indication. La ciclésonide est formulée pour l'inhalation et non pour un usage dermatologique : une nouvelle formulation serait nécessaire. Par ailleurs, les prédictions « dermatitis, atopic » (score 0,9973) et « eczéma atopique » désignent le même concept de maladie.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 63599556 | ALVESCO 80 microgrammes/dose, solution pour inhalation en flacon pressurisé | Solution pour inhalation | COVIS PHARMA EUROPE (PAYS-BAS) | Active |
| 66052179 | ALVESCO 160 microgrammes/dose, solution pour inhalation en flacon pressurisé | Solution pour inhalation | COVIS PHARMA EUROPE (PAYS-BAS) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 63 interactions recensées. Parmi les principales :
  - Majeure : cladribine.
  - Modérées : clarithromycine, miconazole, cobicistat, atazanavir, fosamprénavir, amprénavir, cératinib, bocéprévir, conivaptan, fostamatinib, insuline humaine inhalée, abamétapir (topique).
  - Mineures : formotérol, salbutamol, arformotérol.
  - Niveau non précisé : oméprazole, lansoprazole, prednisolone, famotidine.

Veuillez consulter la notice pour les autres informations de sécurité (mises en garde, contre-indications).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle, sans essai clinique ni publication sur l'eczéma atopique (niveau L5). La ciclésonide n'existe que sous forme inhalée, ce qui est inadapté à cette indication.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action.
- Études précliniques ou cliniques évaluant la ciclésonide dans l'eczéma atopique.
- Évaluation d'une formulation adaptée à la voie cutanée.
- Fusion des entrées en doublon (eczéma atopique / dermatite atopique) lors de la revue.
- Récupération de la notice de l'ANSM pour examiner les mises en garde et contre-indications.

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Alvesco (ciclesonide) prescribing information, Covis Pharma US, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9f6112fb-78ef-43cf-8ae3-36370eb45468) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

