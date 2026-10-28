---
layout: default
title: Lisinopril
parent: Prédiction du modèle uniquement (L5)
nav_order: 455
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
monitor_inn: "LISINOPRIL"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "Braddock syndrome", "chronic pulmonary heart disease", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome"]
description: "Lisinopril : nouvelle indication prédite, Pulmonary hypertension with unclear multifactorial mechanism (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Lisinopril
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Lisinopril: Pulmonary hypertension with unclear multifactorial mechanism
{: .text-alpha }

## Résumé en Une Phrase

Lisinopril est un inhibiteur de l'enzyme de conversion de l'angiotensine (IEC), initialement utilisé pour le traitement de l'hypertension artérielle et de l'infarctus du myocarde.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infarctus du myocarde postéro-inférieur**. Il s'agit toutefois d'un sous-type anatomique d'une indication déjà reconnue, et **aucun essai clinique** ni **aucune publication** spécifique ne soutient actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Pulmonary hypertension with unclear multifactorial mechanism |
| Score de Prédiction TxGNN | 0.9989 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, lisinopril fait partie de la classe des IEC. Son efficacité dans l'hypertension et l'infarctus du myocarde est établie, et il agit par blocage du système rénine-angiotensine-aldostérone (SRAA), ce qui limite le remodelage ventriculaire après infarctus.

L'infarctus du myocarde postéro-inférieur est un sous-type anatomique de l'infarctus du myocarde, indication déjà reconnue pour ce médicament. Aucune donnée propre à ce sous-type n'a été fournie.

Les autres prédictions du modèle vont dans le même sens : infarctus postéro-latéral et septal (sous-types de l'infarctus), hypertension rénovasculaire maligne et néphropathie hypertensive maligne (sous-types de l'hypertension). La seule piste réellement nouvelle avec des données de soutien est le **cœur pulmonaire chronique** (voir les remarques plus bas).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'infarctus du myocarde postéro-inférieur.

À titre indicatif, la prédiction n°9 (cœur pulmonaire chronique, score 0,9968, niveau L3) dispose des publications suivantes les plus pertinentes :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [17047621](https://pubmed.ncbi.nlm.nih.gov/17047621/) | 2006 | Étude clinique (probablement de petite taille) | Kardiologiia | Lisinopril 10 mg/jour : atténuation de l'hypertension pulmonaire, amélioration de la fonction systolique du ventricule droit et du remplissage diastolique chez des patients insuffisants cardiaques avec cardiopathie ischémique et BPCO |
| [14524095](https://pubmed.ncbi.nlm.nih.gov/14524095/) | 2003 | Étude clinique (probablement de petite taille, non contrôlée) | Problemy tuberkuleza i boleznei legkikh | Lisinopril dans le traitement du cœur pulmonaire chronique (résumé non disponible) |
| [20852161](https://pubmed.ncbi.nlm.nih.gov/20852161/) | 2010 | Rapport de cas (sécurité/interaction) | Am J Health Syst Pharm | Hypotension et bradycardie sévères lors de l'association tizanidine et lisinopril |

Les autres publications retrouvées pour cette indication sont hors sujet (insuffisance cardiaque pédiatrique, nébivolol, dépression chez l'insuffisant rénal, modèle animal d'hypertension).

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62606357 | LISINOPRIL ZENTIVA 20 mg, comprimé sécable (ZENTIVA FRANCE) | Comprimé sécable | Non renseignée (AMM active) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité (mises en garde et contre-indications de la notice non disponibles dans les données compilées).

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : angiœdème (dont héréditaire, acquis et induit par les bloqueurs du SRAA), maladie rénale, maladie hépatique et encéphalopathie hépatique, pancréatite, maladie de la vésicule biliaire, lupus érythémateux systémique, diabète et acidocétose diabétique, carence en potassium, neutropénie et agranulocytose, sténose aortique, hypotension, hyperparathyroïdie, maladies du tissu conjonctif et maladies osseuses.
- **Interactions médicamenteuses** (100 interactions recensées, extrait des principales) :
  - **Majeures** : citrate de potassium, bicarbonate de potassium (risque d'hyperkaliémie).
  - **Modérées** : corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), antidiabétiques (metformine, alogliptine, saxagliptine, canagliflozine, dapagliflozine, empagliflozine, chlorpropamide), acide acétylsalicylique, morphine, bupropion, dronabinol, préparations de lavage colique (acide picosulfurique, polyéthylène glycol).
- Dans le contexte de l'hypertension pulmonaire et rénovasculaire : risque d'hypotension systémique et d'insuffisance rénale aiguë en cas de sténose bilatérale des artères rénales.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'infarctus du myocarde postéro-inférieur est un sous-type d'une indication déjà reconnue ; la prédiction ne constitue pas un repositionnement réel et aucune preuve spécifique n'existe (niveau L5). Les données de sécurité de la notice manquent et bloquent l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les mises en garde et contre-indications de la notice ANSM (téléchargement et analyse du PDF)
- Obtenir le mécanisme d'action détaillé (via DrugBank)
- Vérifier le statut réglementaire : l'unique AMM identifiée est annulée, et le texte d'indication n'est pas renseigné
- Réorienter l'évaluation vers les indications réellement nouvelles, en priorité le **cœur pulmonaire chronique** (niveau L3), en recherchant des essais contrôlés randomisés, les études disponibles étant petites et de faible rigueur méthodologique
- Prévoir un suivi de la fonction rénale, de la kaliémie et de la tension artérielle pour toute population ciblée
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

