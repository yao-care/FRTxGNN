---
layout: default
title: Bendroflumethiazide
parent: Prédiction du modèle uniquement (L5)
nav_order: 95
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Bendroflumethiazide : nouvelle indication prédite, Maladie rénale hypertensive maligne (niveau de preuve L5). Indication d'origine : Hypertension artérielle"
monitor_inn: "bendroflumethiazide"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia"]
---

# Bendroflumethiazide
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

# Bendrofluméthiazide : De l'hypertension à la maladie rénale hypertensive maligne

## Résumé en Une Phrase

La bendrofluméthiazide est un diurétique thiazidique, initialement utilisé pour le traitement de l'hypertension artérielle.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **maladie rénale hypertensive maligne**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction issue du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle (le texte d'indication de l'AMM n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Maladie rénale hypertensive maligne |
| Score de Prédiction TxGNN | 99,88 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées (non commercialisé) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la bendrofluméthiazide fait partie de la classe des diurétiques thiazidiques, son efficacité dans l'hypertension est reconnue, et elle agit sur la pression artérielle par le contrôle du volume.

Un lien avec la maladie rénale hypertensive est biologiquement plausible, car la pression artérielle et le volume intravasculaire jouent un rôle dans l'atteinte rénale. Cependant, l'hypertension maligne est une urgence hypertensive, habituellement prise en charge par des médicaments d'action rapide par voie parentérale. Les thiazidiques ne constituent pas un traitement standard dans ce cadre.

Le score élevé (0,9988) reflète très probablement la proximité dans le graphe avec l'indication approuvée d'hypertension plutôt qu'une preuve indépendante. Aucun soutien au niveau du mécanisme ne peut être confirmé.

**Autres prédictions du modèle (toutes de niveau L5, sans essai ni publication) :**

| Maladie prédite | Score TxGNN | Commentaire |
|------|------|------|
| Hypertension rénovasculaire maligne | 99,88 % | Probablement héritée de l'indication hypertension ; la prise en charge repose sur le blocage du SRAA et la revascularisation, et les thiazidiques peuvent activer davantage le SRAA |
| Hypertension pulmonaire d'origine multifactorielle peu claire | 99,87 % | Physiopathologie différente ; les diurétiques ne sont qu'un traitement de soutien de la surcharge volumique |
| Hypertension pulmonaire liée à une maladie pulmonaire et/ou à l'hypoxie | 99,87 % | Les diurétiques n'ont pas d'effet établi sur le processus vasculaire pulmonaire ; risque d'alcalose métabolique pouvant aggraver l'hypoventilation |
| Syndrome de Braddock | 99,83 % | Aucun lien mécanistique plausible identifié ; probable artefact du modèle |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61977014 | TENSIONORME, comprimé sécable (ETHYX PHARMACEUTICALS) | Comprimé sécable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : anuria, maladie rénale, maladie hépatique, coma et encéphalopathie hépatiques, maladie de la vésicule biliaire, pancréatite, pyourétère, goutte, hyperuricémie, diabète et acidocétose diabétique, carence en potassium, hypercalcémie, néphrocalcinose, hyperparathyroïdie, ostéite fibreuse, troubles du métabolisme du phosphore, lupus érythémateux systémique (y compris pédiatrique), myasthénie grave et maladies de la jonction neuromusculaire, bloc auriculo-ventriculaire, emphysème pulmonaire, maladie bronchique, ictère néonatal, troubles anxieux, troubles névrotiques et dysthymie.
- **Interactions médicamenteuses** : 168 interactions recensées. Parmi les principales, de niveau modéré : antidiabétiques (metformine, pioglitazone, alogliptine, albiglutide, acarbose), corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, béclométasone), amphotéricine B (y compris complexe lipidique), oméprazole, rabéprazole, cholécalciférol, bupropion et morphine. De niveau mineur : doxycycline, hyoscyamine et atropine.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication, et l'hypertension maligne n'est pas une situation où les thiazidiques sont un traitement de référence.
- La seule AMM française est annulée et les données de sécurité issues de la notice manquent, ce qui empêche de passer au criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle de l'ANSM (mises en garde et contre-indications).
- Obtenir les données sur le mécanisme d'action (DrugBank).
- Réaliser une recherche systématique d'essais cliniques et de publications sur l'usage des thiazidiques dans l'atteinte rénale hypertensive.
- Évaluer la compatibilité des voies d'administration et la pertinence clinique par rapport aux traitements de référence.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

