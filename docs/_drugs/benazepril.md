---
layout: default
title: Benazepril
parent: Prédiction du modèle uniquement (L5)
nav_order: 93
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Benazepril : nouvelle indication prédite, Maladie rénale hypertensive maligne (niveau de preuve L5). Indication d'origine : Hypertension artérielle"
monitor_inn: "benazepril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Benazepril
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

## Bénazépril : De l'Hypertension à la Maladie Rénale Hypertensive Maligne
{: .text-alpha }

## Resume en Une Phrase

Le bénazépril est un inhibiteur de l'enzyme de conversion de l'angiotensine (IEC), initialement utilisé pour traiter l'hypertension artérielle.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **maladie rénale hypertensive maligne**, avec un score très élevé.
Cependant, **aucun essai clinique** et **aucune publication pertinente** ne soutiennent actuellement cette prédiction : elle repose uniquement sur le modèle.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle (selon le graphe de connaissances ; aucune AMM française disponible) |
| Nouvelle Indication Predite | Maladie rénale hypertensive maligne |
| Score de Prediction TxGNN | 99,65 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, le bénazépril appartient à la classe des IEC : en bloquant la formation d'angiotensine II, il réduit la pression artérielle systémique ainsi que la pression intraglomérulaire. Son efficacité dans l'hypertension et la protection rénale est établie.

La néphropathie hypertensive maligne est une conséquence directe d'une hypertension sévère. Un bénéfice du bénazépril est donc plausible sur le plan mécanistique, mais il s'agit essentiellement d'une extension de l'indication d'origine, et non d'une indication réellement nouvelle.

Il faut rester prudent : l'hypertension maligne est une urgence, généralement prise en charge par des antihypertenseurs intraveineux. Les IEC comportent des risques en cas d'atteinte rénale (hyperkaliémie, insuffisance rénale aiguë, notamment en cas de sténose des artères rénales).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Litterature

Aucune littérature associée disponible actuellement pour cette indication.

## Informations de Marche en France

Aucune AMM n'est enregistrée en France pour le bénazépril dans les données compilées : le médicament apparaît comme non commercialisé.

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : insuffisance hépatique, encéphalopathie hépatique, maladie rénale, anurie, pancréatite, maladie de la vésicule biliaire, angio-œdème (acquis, héréditaire, induit par les bloqueurs du système rénine-angiotensine-aldostérone), lupus érythémateux systémique, carence en potassium, diabète et acidocétose diabétique, neutropénie, agranulocytose, hypotension, hyperparathyroïdie, connectivites, ictère néonatal, entre autres.
- **Interactions médicamenteuses** : 169 interactions recensées. Les principales (niveau modéré) concernent :
  - les antidiabétiques oraux et injectables (acétohexamide, chlorpropamide, glimépiride, glipizide, glibenclamide, alogliptine, dapagliflozine, exénatide) ;
  - de nombreuses insulines (humaine, asparte, dégludec, détémir, glargine, glulisine, lispro, etc.) ;
  - l'hydrocortisone et la glycérine.
- **Points d'attention propres aux indications prédites** : risque d'insuffisance rénale aiguë en cas de sténose bilatérale des artères rénales ou de rein unique sténosé ; hyperkaliémie ; hypotension.

Veuillez consulter la notice pour les mises en garde officielles : elles ne sont pas disponibles dans les données compilées.

## Autres Indications Predites (pour information)

| Rang | Indication | Score TxGNN | Niveau de Preuve | Recommandation |
|---|---|---|---|---|
| 2 | Hypertension rénovasculaire maligne | 99,65 % | L5 | Hold |
| 3 | Hypertension pulmonaire à mécanisme multifactoriel mal défini | 99,60 % | L5 | Hold |
| 4 | Hypertension pulmonaire liée à une maladie pulmonaire et/ou à l'hypoxie | 99,60 % | L5 | Hold |
| 5 | Syndrome de Braddock | 99,44 % | L5 | Hold |

Remarques : les scores identiques des rangs 1 et 2 (et 3 et 4) suggèrent un voisinage commun dans le graphe plutôt que des preuves indépendantes. Les IEC ne sont pas recommandés dans l'hypertension artérielle pulmonaire. Pour le rang 4, les trois publications retrouvées (médecine traditionnelle chinoise dans des modèles de fibrose rénale et myocardique) ne concernent ni le bénazépril ni l'hypertension pulmonaire et n'apportent aucune preuve utile. Pour le syndrome de Braddock, aucun lien mécanistique n'a pu être établi.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication pertinente, et prolonge surtout l'indication d'origine. Le médicament n'est pas commercialisé en France, et les données de sécurité officielles sont absentes, ce qui bloque la phase de revue de sécurité.

**Pour avancer, les elements suivants sont necessaires :**
- Récupérer la notice officielle de l'ANSM (mises en garde et contre-indications) ;
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank) ;
- Effectuer une recherche ciblée d'essais cliniques et de publications sur le bénazépril dans la néphropathie hypertensive maligne ;
- Définir un plan de surveillance de la fonction rénale et de la kaliémie ;
- Clarifier la situation réglementaire en France (absence d'AMM).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

