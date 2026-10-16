---
layout: default
title: Quinapril
parent: Prédiction du modèle uniquement (L5)
nav_order: 643
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Quinapril : nouvelle indication prédite, Hypertension rénovasculaire maligne (niveau de preuve L5). Indication d'origine : Hypertension artérielle"
monitor_inn: "QUINAPRIL"
predicted_indications: ["malignant renovascular hypertension", "malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Quinapril
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

# Quinapril : De l'Hypertension Artérielle à l'Hypertension Rénovasculaire Maligne

## Résumé en Une Phrase

Quinapril est un inhibiteur de l'enzyme de conversion de l'angiotensine (IEC), initialement utilisé pour le traitement de l'hypertension artérielle.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertension rénovasculaire maligne**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette indication précise : la prédiction repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle (les AMM françaises ne mentionnent aucun texte d'indication ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Hypertension rénovasculaire maligne |
| Score de Prédiction TxGNN | 99,86 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées (non commercialisé) |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, le quinapril appartient à la classe des IEC : il bloque la transformation de l'angiotensine I en angiotensine II, un puissant vasoconstricteur, et réduit ainsi la pression artérielle.

L'hypertension rénovasculaire est en grande partie entretenue par l'activation du système rénine-angiotensine. Le blocage de ce système est donc biologiquement plausible. Il faut toutefois souligner que cette prédiction est essentiellement une extension de l'indication déjà connue (l'hypertension), et non une indication réellement nouvelle sur le plan mécanistique.

Une réserve importante s'impose : les IEC peuvent provoquer une dégradation aiguë de la fonction rénale en cas de sténose bilatérale des artères rénales. Cette population exigerait donc une grande prudence. Le score élevé du modèle (0,9986) reste une simple prédiction.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'hypertension rénovasculaire maligne.

## Autres Indications Prédites (pour information)

| Rang | Maladie Prédite | Score TxGNN | Niveau de Preuve | Recommandation |
|------|------|------|------|------|
| 2 | Néphropathie hypertensive maligne | 99,86 % | L5 | Hold |
| 3 | Hypertension pulmonaire liée à une maladie pulmonaire et/ou à l'hypoxie | 99,85 % | L4 | Question de recherche |
| 4 | Hypertension pulmonaire à mécanisme multifactoriel mal défini | 99,85 % | L5 | Hold |
| 5 | Syndrome de Braddock | 99,79 % | L5 | Hold |

Seule l'hypertension pulmonaire liée à une maladie pulmonaire ou à l'hypoxie dispose de données de littérature, exclusivement précliniques :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [8873672](https://pubmed.ncbi.nlm.nih.gov/8873672/) | 1996 | Étude animale | Circulation | L'inhibition de l'ECA tissulaire par le quinapril réduit l'hypertension pulmonaire hypoxique et le remodelage vasculaire pulmonaire |
| [8720418](https://pubmed.ncbi.nlm.nih.gov/8720418/) | 1996 | Étude animale | J Cardiovasc Pharmacol | Préservation de la fonction mécanique et du métabolisme énergétique du ventricule gauche chez le rat après infarctus du myocarde (pertinence indirecte) |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62206135 | ACUITEL 5 mg, comprimé enrobé sécable (annulée) | Comprimé enrobé sécable | Non précisée |
| 62927128 | ACUITEL 20 mg, comprimé enrobé sécable (annulée) | Comprimé enrobé sécable | Non précisée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : angiœdème (y compris héréditaire, acquis et induit par les bloqueurs du système rénine-angiotensine-aldostérone), insuffisance rénale, anurie, maladie hépatique, encéphalopathie hépatique, pancréatite, maladie de la vésicule biliaire, lupus érythémateux systémique, maladies du tissu conjonctif, diabète et acidocétose diabétique, carence en potassium, goutte, neutropénie, agranulocytose, hypotension, hyperparathyroïdie, ainsi que l'ictère néonatal.
- **Interactions médicamenteuses** : 100 interactions ont été recensées. Parmi les principales :
  - **Majeure** : citrate de potassium (risque d'hyperkaliémie).
  - **Modérées** : metformine, canagliflozine, dapagliflozine, chlorpropamide, acide acétylsalicylique, corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, budésonide), doxycycline, tétracycline, bupropion, morphine, atropine, ainsi que plusieurs laxatifs et préparations de lavage intestinal.
- **Point d'attention propre à l'indication** : risque de dégradation aiguë de la fonction rénale en cas de sténose bilatérale des artères rénales.

Les mises en garde et contre-indications issues de la notice française n'ont pas pu être obtenues ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction est plausible mais prolonge largement l'indication hypertensive déjà connue, sans aucun essai ni publication spécifique. Le niveau de preuve est L5.
- Les AMM françaises sont toutes annulées et les données de sécurité de la notice sont absentes, ce qui bloque une évaluation de sécurité complète.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Rechercher des études cliniques ou observationnelles sur l'hypertension rénovasculaire maligne.
- Évaluer le risque rénal chez les patients atteints de sténose bilatérale des artères rénales.
- Clarifier la disponibilité du produit en France, puisque seules des AMM annulées sont recensées.
- Si une piste alternative est envisagée, l'hypertension pulmonaire liée à l'hypoxie (L4) pourrait constituer une question de recherche, à valider d'abord par des études chez l'humain.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

