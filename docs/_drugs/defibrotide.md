---
layout: default
title: Defibrotide
parent: Prédiction du modèle uniquement (L5)
nav_order: 221
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Defibrotide : nouvelle indication prédite, Pseudo-maladie de von Willebrand (rang 1) (niveau de preuve L5). Indication d'origine : Maladie veino-occlusive hépatique"
monitor_inn: "defibrotide"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "thrombotic thrombocytopenic purpura", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "congenital factor V deficiency", "fetal and neonatal alloimmune thrombocytopenia", "thrombocytopenic purpura"]
---

# Defibrotide
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

## Défibrotide : De la maladie veino-occlusive hépatique au purpura thrombotique thrombocytopénique
{: .text-alpha }

## Résumé en Une Phrase

Le défibrotide est un oligonucléotide à effet antithrombotique et profibrinolytique, initialement utilisé pour traiter la **maladie veino-occlusive hépatique** (y compris le syndrome de maladie veino-occlusive avec déficit immunitaire).
Le modèle TxGNN prédit en premier rang la **pseudo-maladie de von Willebrand** (score de 99,91 %), mais cette prédiction ne repose sur aucune preuve. La piste la mieux étayée parmi les prédictions est le **purpura thrombotique thrombocytopénique (PTT)**, avec **8 publications** (aucun essai clinique), essentiellement des cas cliniques, des revues et une étude in vitro.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie veino-occlusive hépatique (selon le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Pseudo-maladie de von Willebrand (rang 1) ; piste la mieux documentée : purpura thrombotique thrombocytopénique (rang 4) |
| Score de Prédiction TxGNN | 99,91 % (rang 1) ; 99,71 % pour le PTT (rang 4) |
| Niveau de Preuve | L5 pour le rang 1 ; L4 pour le PTT |
| Statut de Marché en France | ✗ Annulée uniquement |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold (rang 1) ; question de recherche pour le PTT / la microangiopathie thrombotique associée à la greffe |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, le défibrotide protège les cellules endothéliales, réduit leur activation pro-inflammatoire et prothrombotique, et augmente l'activité fibrinolytique (hausse du tPA, baisse du PAI-1).

**Prédiction de rang 1 (pseudo-maladie de von Willebrand) :** aucun essai ni publication n'a été trouvé. Le lien avec l'hyperadhésion plaquettaire GPIb-VWF est spéculatif. Il s'agit en outre d'un trouble hémorragique plaquettaire, peu compatible avec un agent susceptible d'augmenter le risque hémorragique. Les autres prédictions de score élevé (défaut de sécrétion plaquettaire, thrombasthénie de Glanzmann, syndrome de Scott, déficit en récepteur du collagène, thrombopénie constitutionnelle, déficit congénital en facteur V, thrombopénie alloimmune fœto-néonatale) présentent le même profil : prédiction seule, sans preuve, avec une incohérence mécanistique et un risque hémorragique.

**Piste du PTT et de la microangiopathie thrombotique (MAT) :** la maladie veino-occlusive et les MAT partagent une lésion endothéliale comme élément central. Cela rend plausible un effet protecteur du défibrotide, notamment dans la MAT associée à la greffe. Une étude in vitro montre une atténuation de la lésion endothéliale induite par des plasmas de patients atteints de COVID-19 et de vasculopathies apparentées. Le traitement standard du PTT classique (échange plasmatique, immunosuppression, caplacizumab) étant bien établi, l'intérêt du repositionnement semble plus plausible pour la MAT associée à la greffe que pour le PTT classique. Pour le « purpura thrombocytopénique » (rang 10), la littérature est identique à celle du PTT et ne concerne pas le purpura thrombopénique immunologique ; son applicabilité n'est pas démontrée.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Publications relatives au PTT (rang 4), classées par type :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [11960280](https://pubmed.ncbi.nlm.nih.gov/11960280/) | 2002 | Série de cas / cohorte | Bone Marrow Transplant | Défibrotide présenté comme traitement prometteur du PTT chez des patients greffés de moelle osseuse (résumé non disponible) |
| [10775024](https://pubmed.ncbi.nlm.nih.gov/10775024/) | 2000 | Cas clinique | Clin Appl Thromb Hemost | Défibrotide dans le PTT récidivant, forme dont la prise en charge reste difficile |
| [3754836](https://pubmed.ncbi.nlm.nih.gov/3754836/) | 1986 | Cas clinique | Haemostasis | Effets du défibrotide dans l'insuffisance rénale aiguë due à une microangiopathie thrombotique |
| [7896218](https://pubmed.ncbi.nlm.nih.gov/7896218/) | 1994 | Cas clinique (événement indésirable) | Haematologica | PTT survenu après un traitement par défibrotide : signal de sécurité |
| [37001283](https://pubmed.ncbi.nlm.nih.gov/37001283/) | 2023 | Étude in vitro | Thromb Res | Le défibrotide atténue la lésion des cellules endothéliales induite par des plasmas de patients COVID-19 et de vasculopathies apparentées |
| [30305540](https://pubmed.ncbi.nlm.nih.gov/30305540/) | 2018 | Revue | Rinsho Ketsueki | Prise en charge de la microangiopathie thrombotique associée à la greffe (lésion endothéliale, conditionnement, inhibiteurs de la calcineurine, complément) |
| [17603513](https://pubmed.ncbi.nlm.nih.gov/17603513/) | 2007 | Revue | Bone Marrow Transplant | Diagnostic et traitement de la MAT associée à la greffe ; absence de définition consensuelle |
| [19228075](https://pubmed.ncbi.nlm.nih.gov/19228075/) | 2009 | Revue | Drugs | MAT après greffe de cellules souches : incidence de 0,5 à 76 %, mortalité de 60 à 90 % malgré le traitement |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69439245 | DEFITELIO 80 mg/mL solution à diluer pour perfusion (GENTIUM, Italie) | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Interactions médicamenteuses** : 130 interactions ont été recensées. Parmi les principales, de niveau **majeur** : acide acétylsalicylique, abciximab, acalabrutinib, alteplase, fondaparinux, anagrélide, déférasirox, ibritumomab tiuxétan et tositumomab (y compris marqué à l'iode 131). De niveau **modéré** : AINS (ibuprofène, kétorolac, célécoxib, diclofénac topique), fluvoxamine, oméga-3, ainsi que fenfluramine, dexfenfluramine et sibutramine. La plupart de ces associations concernent des agents antiagrégants, anticoagulants ou thrombolytiques et majorent le risque hémorragique.
- **Signal de sécurité** : un cas de PTT survenu après un traitement par défibrotide a été rapporté (PMID 7896218).
- **Risque hémorragique** : le profil antithrombotique et profibrinolytique du médicament est un enjeu pour toutes les prédictions concernant des troubles hémorragiques.

Veuillez consulter la notice pour les mises en garde et contre-indications détaillées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold** (pour la prédiction de rang 1 et les troubles hémorragiques plaquettaires ou de la coagulation) ; **question de recherche** pour le PTT / la MAT associée à la greffe (niveau L4).

**Justification :**
- Le rang 1 et la majorité des prédictions n'ont aucune preuve (L5) et présentent une incohérence mécanistique avec un risque hémorragique. La piste PTT/MAT ne repose que sur de petits cas cliniques anciens, des revues et une étude in vitro, avec un signal de sécurité et sans essai enregistré.
- L'AMM française est annulée et les données de sécurité de la notice sont absentes, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice auprès de l'ANSM (lacune bloquante)
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Cibler la MAT associée à la greffe plutôt que le PTT classique, avec une revue systématique de la littérature
- Concevoir une étude prospective ou un essai exploratoire, avec évaluation du risque hémorragique
- Clarifier le statut réglementaire en France (AMM annulée)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

