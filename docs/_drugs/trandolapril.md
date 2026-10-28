---
layout: default
title: Trandolapril
parent: Prédiction du modèle uniquement (L5)
nav_order: 778
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "TRANDOLAPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
description: "Trandolapril : nouvelle indication prédite, Malignant hypertensive renal disease (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Trandolapril
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

## Trandolapril: Malignant hypertensive renal disease
{: .text-alpha }

## Résumé en Une Phrase

Trandolapril est un inhibiteur de l'enzyme de conversion de l'angiotensine (IEC), initialement utilisé pour le traitement de l'hypertension artérielle.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertension rénovasculaire maligne**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette indication précise : il s'agit d'une prédiction du modèle uniquement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Malignant hypertensive renal disease |
| Score de Prédiction TxGNN | 0.9992 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 11 sur 11) |
| Nombre d'AMM | 11 (valides : 11) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, trandolapril fait partie de la classe des inhibiteurs de l'enzyme de conversion de l'angiotensine, dont l'efficacité dans l'hypertension est établie.

L'hypertension rénovasculaire est fortement dépendante de la rénine et de l'angiotensine II. Un blocage de ce système est donc mécanistiquement cohérent. Toutefois, il s'agit essentiellement d'un sous-type de l'indication d'origine, et non d'un repositionnement au sens strict.

Une précaution importante : les IEC peuvent provoquer une insuffisance rénale aiguë en cas de sténose bilatérale des artères rénales. Cela exige une vigilance particulière de sécurité pour cette indication.

Les autres prédictions du modèle sont du même ordre : hypertension rénale maligne (score identique, 0,9992, raisonnement par analogie de classe), hypertension pulmonaire d'origine pulmonaire ou hypoxique (0,9992), hypertension pulmonaire à mécanisme multifactoriel (0,9992), syndrome de Braddock (0,9988) et cœur pulmonaire chronique (0,9919). Pour les formes pulmonaires, le score élevé reflète probablement la proximité des termes dans l'ontologie plutôt qu'une biologie spécifique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature directement associée à l'hypertension rénovasculaire maligne n'est disponible actuellement.

À titre indicatif, des publications indirectes ont été retrouvées pour l'hypertension pulmonaire d'origine pulmonaire/hypoxique (prédiction de rang 3) ; aucune n'étudie l'hypertension pulmonaire chez l'humain :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [7511729](https://pubmed.ncbi.nlm.nih.gov/7511729/) | 1994 | Étude animale | J Cardiovasc Pharmacol | Trandolapril chez le rat spontanément hypertendu : régression de l'hypertrophie ventriculaire gauche, effets sur la résistance coronaire et la compliance ventriculaire |
| [8909991](https://pubmed.ncbi.nlm.nih.gov/8909991/) | 1996 | Étude animale | Gen Pharmacol | Trandolapril + vérapamil inhibent le vasospasme coronaire induit par l'hypoxie après ischémie-reperfusion chez le chien |
| [9218195](https://pubmed.ncbi.nlm.nih.gov/9218195/) | 1997 | Étude préclinique | J Hypertens Suppl | Association vérapamil-trandolapril : réduction de la pression artérielle et effets au-delà |
| [8166049](https://pubmed.ncbi.nlm.nih.gov/8166049/) | 1994 | Revue | Am J Cardiol | Bases moléculaires de la régression de l'hypertrophie cardiaque |
| [17393952](https://pubmed.ncbi.nlm.nih.gov/17393952/) | 2007 | Rapport de cas | J Natl Med Assoc | Disparition de la douleur drépanocytaire sous IEC chez une patiente |
| [8989645](https://pubmed.ncbi.nlm.nih.gov/8989645/) | 1996 | Étude animale | J Card Fail | Traitement prolongé par trandolapril et vasoconstriction accrue chez le rat en insuffisance cardiaque chronique (lié au cœur pulmonaire chronique, rang 6) |

---

## Informations de Marché en France

Les textes d'indication ne sont pas renseignés.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 67937514 | TRANDOLAPRIL BIOGARAN 0,5 mg | Gélule | Active |
| 62481448 | ODRIK 4 mg | Gélule | Active |
| 66972380 | TRANDOLAPRIL BIOGARAN 2 mg | Gélule | Active |
| 64337254 | TRANDOLAPRIL VIATRIS 2 mg | Gélule | Active |
| 68510337 | ODRIK 2 mg | Gélule | Active |

(5 AMM affichées sur 11 ; les autres concernent d'autres dosages de Trandolapril Biogaran/Viatrix et les associations Tarka LP à libération prolongée.)

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie rénale, maladie hépatique, angioedème (dont angioedème héréditaire et induit par les bloqueurs du système rénine-angiotensine-aldostérone), neutropénie, agranulocytose, sténose aortique, cardiomyopathie hypertrophique, hypotension, obstruction de l'artère rénale, myasthénie, tachycardie ventriculaire, bloc auriculo-ventriculaire, insuffisance cardiaque, entre autres.
- **Interactions médicamenteuses** (100 interactions recensées) :
  - Majeures : citrate de potassium, bicarbonate de potassium (risque d'hyperkaliémie).
  - Modérées (exemples) : corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), antidiabétiques (metformine, alogliptine, canagliflozine, dapagliflozine, empagliflozine, glimépiride, chlorpropamide), acide acétylsalicylique, morphine, bupropion, dronabinol, acide picosulfurique, polyéthylène glycol avec électrolytes.
- **Point d'attention** : le risque d'insuffisance rénale aiguë en cas de sténose bilatérale des artères rénales est directement pertinent pour l'indication prédite.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle et un raisonnement de classe, sans essai ni publication pour cette indication. Les données de sécurité de la notice, étape bloquante, manquent.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications) : lacune bloquante.
- Compléter les données sur le mécanisme d'action (DrugBank).
- Rechercher des études cliniques ou observationnelles chez l'humain sur l'hypertension rénovasculaire et rénale maligne.
- Clarifier la pertinence du repositionnement, vu le chevauchement avec l'indication d'origine, ainsi que la situation réglementaire (AMM annulées).
- Évaluer le risque rénal (sténose bilatérale des artères rénales) et l'hyperkaliémie avant toute progression.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

