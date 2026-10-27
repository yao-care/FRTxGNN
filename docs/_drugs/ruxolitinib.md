---
layout: default
title: Ruxolitinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 687
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ruxolitinib : nouvelle indication prédite, PEComa périvasculaire du corps utérin (niveau de preuve L5). Indication d'origine : Myélofibrose primitive, polyglobulie de Vaquez…"
monitor_inn: "ruxolitinib"
predicted_indications: ["uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lymphangiomyoma", "lymphangioleiomyomatosis", "liposarcoma", "familial rhabdoid tumor", "lung PEComa", "ovarian myxoid liposarcoma", "acquired hemophagocytic lymphohistiocytosis associated with malignant disease", "hemophagocytic syndrome associated with an infection"]
---

# Ruxolitinib
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

## Ruxolitinib : De la myélofibrose primitive au PEComa périvasculaire du corps utérin
{: .text-alpha }

## Résumé en Une Phrase

Le ruxolitinib (JAKAVI) est un inhibiteur de kinases utilisé à l'origine dans les néoplasmes myéloprolifératifs (myélofibrose, polyglobulie de Vaquez).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **tumeur à cellules épithélioïdes périvasculaires (PEComa) du corps utérin**.
**Aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction précise.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Myélofibrose primitive, polyglobulie de Vaquez, néoplasme myéloprolifératif (selon le graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | PEComa périvasculaire du corps utérin |
| Score de Prédiction TxGNN | 99,73 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Toutes les AMM sont annulées |
| Nombre d'AMM | 6 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, le ruxolitinib est un inhibiteur de JAK1/JAK2. Son efficacité dans les néoplasmes myéloprolifératifs est établie, et il pourrait mécanistiquement être applicable à d'autres tumeurs dépendantes de la signalisation JAK-STAT.

Pour le PEComa utérin, seule la prédiction du modèle soutient cette indication. Un lien possible passe par les interactions entre les voies mTOR et JAK-STAT dans les PEComas. Cette hypothèse reste spéculative, car aucune donnée fournie ne l'étaye. La physiopathologie classique des PEComas repose surtout sur l'hyperactivation de mTOR, et la ressemblance avec l'indication d'origine (néoplasmes hématologiques) n'a pas été évaluée.

Le score élevé reflète probablement la proximité dans le graphe avec d'autres entités de la famille des PEComas (PEComa bénin, PEComa pulmonaire, lymphangiomyome, lymphangioléiomyomatose). Il ne constitue donc pas une preuve indépendante.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les 6 AMM recensées sont annulées. Aucune n'est actuellement valide. Le texte d'indication approuvée n'est pas renseigné pour ces AMM.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 65291824 | JAKAVI 5 mg, comprimé | Comprimé | Novartis Europharm (Irlande) |
| 66180136 | JAKAVI 20 mg, comprimé | Comprimé | Novartis Europharm (Irlande) |
| 60672974 | JAKAVI 15 mg, comprimé | Comprimé | Novartis Europharm (Irlande) |
| 68379069 | JAKAVI 5 mg/mL, solution buvable | Solution buvable | Novartis Europharm (Irlande) |
| 68279528 | OPZELURA 15 mg/g, crème | Crème | Incyte Biosciences Distribution (Pays-Bas) |

Une sixième AMM (JAKAVI 10 mg, comprimé, n° 65584250) est également annulée.

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de JAK1/JAK2), indiquée dans des néoplasmes myéloprolifératifs |
| Risque de Myélosuppression | Moyen à élevé d'après les connaissances générales sur la classe (anémie, thrombocytopénie, neutropénie) ; à confirmer avec la notice |
| Classification d'Émétogénicité | Faible |
| Éléments de Surveillance | NFS avec formule, fonction hépatique et rénale, bilan lipidique |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

Les mises en garde et contre-indications de la notice n'ont pas pu être intégrées à ce rapport. Veuillez consulter la notice pour ces informations.

- **Interactions Médicamenteuses** : 338 interactions sont recensées. Les principales sont :
  - **Majeures** : clarithromycine, cobicistat, déférasirox, défériprone, ibritumomab tiuxétan, tositumomab, tositumomab (I-131), samarium (153Sm) lexidronam.
  - **Modérées** (exemples) : dexaméthasone, rosuvastatine, palifermine, fenfluramine, dexfenfluramine, sibutramine, troglitazone, chlorure de strontium Sr-89.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'indication prédite (PEComa utérin) repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication.
- Toutes les AMM françaises du ruxolitinib sont annulées.
- Les données de sécurité de la notice ne sont pas disponibles.

À titre de comparaison, parmi les autres candidats prédits :
- **Syndrome hémophagocytaire associé à une infection** : le mieux documenté. Il s'appuie sur des modèles murins, des séries de cas et une étude de traitement stratifié pédiatrique. Il est classé L3, avec la recommandation « Research Question ».
- **Liposarcome** : classé L4, avec deux études précliniques sur la voie JAK-STAT dans le liposarcome myxoïde.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de mécanisme d'action (DrugBank) et analyse du lien mécanistique entre JAK-STAT et mTOR dans les PEComas.
- Revue de la littérature ciblée sur le ruxolitinib dans les PEComas et les tumeurs apparentées, avec des données précliniques ou cliniques.
- Mises en garde et contre-indications de la notice ANSM, obtenues en téléchargeant et analysant le PDF de la notice.
- Clarification du statut réglementaire en France (AMM annulées) et de la voie d'administration requise.
- Comparaison avec le traitement de référence (inhibiteurs de mTOR) avant toute décision de développement.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

