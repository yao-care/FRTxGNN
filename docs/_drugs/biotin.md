---
layout: default
title: Biotin
parent: Prédiction du modèle uniquement (L5)
nav_order: 109
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Biotin : nouvelle indication prédite, Dyspepsie (niveau de preuve L5). Indication d'origine : Carence nutritionnelle en biotine"
monitor_inn: "biotin"
predicted_indications: ["dyspepsia", "gastroparesis (disease)"]
---

# Biotin
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

# Biotine : De la carence nutritionnelle en biotine à la dyspepsie

## Résumé en Une Phrase

La biotine (vitamine B8) était utilisée à l'origine pour traiter la carence nutritionnelle en biotine.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **dyspepsie**, mais cette prédiction repose uniquement sur le modèle : **aucun essai clinique** n'est enregistré et les **6 publications** identifiées ne soutiennent pas directement cette indication.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carence nutritionnelle en biotine |
| Nouvelle Indication Prédite | Dyspepsie |
| Score de Prédiction TxGNN | 99,43 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 4 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la biotine est un cofacteur de carboxylases impliquées dans le métabolisme des acides gras, du glucose et des acides aminés. Son efficacité dans la carence en biotine est établie.

Aucun lien mécanistique direct avec la dyspepsie n'est démontré. Une carence en biotine peut provoquer des symptômes digestifs (anorexie, nausées), ce qui permet d'imaginer un lien, mais uniquement dans un contexte de carence. Le score élevé de TxGNN (99,43 %) est une prédiction du modèle, sans confirmation clinique.

La seconde prédiction, la gastroparésie (score de 99,42 %), n'est étayée par aucun essai ni aucune publication. Aucun mécanisme plausible reliant la biotine à la motilité gastrique n'est documenté.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Rapport de cas | The Journal of Dermatology | Carence en biotine chez un nourrisson de 5 mois, diagnostiqué dyspeptique à la naissance et nourri exclusivement avec une formule d'acides aminés ; biotine sérique et urinaire basses |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Étude observationnelle | International Journal of Molecular Medicine | Cellules endocrines de l'antre gastrique chez 76 patients atteints du syndrome de l'intestin irritable ; pas de lien avec la biotine |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Étude observationnelle | World Journal of Gastrointestinal Endoscopy | Cellules endocrines de la muqueuse oxyntique dans le syndrome de l'intestin irritable ; pas de lien avec la biotine |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Article clinique/revue | Eksperimental'naia i Klinicheskaia Gastroenterologiia | Complément contenant des prébiotiques et plusieurs vitamines (dont la biotine) pour la microbiocénose intestinale après antibiothérapie ; effet de la biotine seule non évaluable |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Étude observationnelle | Journal of Clinical Pathology | Localisation de l'interleukine 10 dans la gastrite à *H. pylori* ; pas de lien direct avec la biotine |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Étude observationnelle | Kidney International | Lymphocytes T de l'intestin grêle dans la néphropathie à IgA ; pas de lien direct avec la biotine |

Ces publications sont indirectes : aucune n'évalue la biotine comme traitement de la dyspepsie.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61890004 | BIOTINE BAYER 0,5 %, solution injectable I.M. | Solution injectable | Non renseignée (AMM annulée) |
| 66001124 | BIOTINE BAYER 5 mg, comprimé | Comprimé | Non renseignée (AMM annulée) |
| 67312509 | SOLUVIT, lyophilisat pour usage parentéral | Lyophilisat pour usage parentéral | Non renseignée (AMM annulée) |
| 61001031 | CERNEVIT, poudre pour solution injectable ou pour perfusion | Poudre pour solution injectable ou pour perfusion | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (et non du texte de la notice)** : maladie rénale, pyo-uretère, sarcoïdose, hyperparathyroïdie, ostéite fibreuse, hypercalcémie, néphrocalcinose, trouble du métabolisme du phosphore, néphrolithiase (y compris la susceptibilité liée à SLC26A1), néphropathie urique aiguë, constipation, lésions osseuses métastatiques lytiques.
- **Interactions médicamenteuses** : aucune interaction retrouvée dans les données compilées.

Les mises en garde et contre-indications issues de la notice ANSM n'ont pas pu être consultées. Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication directe pour la dyspepsie. Toutes les AMM françaises sont annulées, et les données de sécurité de la notice sont manquantes, ce qui empêche le passage à l'étape d'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications).
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank).
- Mener une recherche bibliographique ciblée sur la biotine dans la dyspepsie et la gastroparésie.
- Clarifier la pertinence de la prédiction : l'effet n'est plausible que dans un contexte de carence en biotine.
- Examiner les contre-indications rénales et calciques/phosphorées issues du graphe de connaissances.
- Vérifier la compatibilité des voies d'administration, qui est encore à évaluer.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

