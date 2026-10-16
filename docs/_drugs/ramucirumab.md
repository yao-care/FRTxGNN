---
layout: default
title: Ramucirumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 650
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ramucirumab : nouvelle indication prédite, Adénocarcinome du ligament utérin (niveau de preuve L5). Indication d'origine : Cancer gastrique (adénocarcinome gastrique)…"
monitor_inn: "RAMUCIRUMAB"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "cervical adenosquamous carcinoma, glassy cell variant", "uterine ligament endometrioid adenocarcinoma", "uterine ligament clear cell adenocarcinoma", "uterine ligament mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
---

# Ramucirumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Ramucirumab : Du Cancer Gastrique à l'Adénocarcinome du Ligament Utérin

## Résumé en Une Phrase

Le ramucirumab est un anticorps monoclonal initialement utilisé dans le traitement de cancers solides, notamment le cancer gastrique, le cancer bronchique non à petites cellules et le carcinome hépatocellulaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**adénocarcinome du ligament utérin**, ainsi que pour plusieurs cancers gynécologiques apparentés (col de l'utérus, ligament utérin).
Aucun essai clinique ni aucune publication ne soutient actuellement cette direction : il s'agit d'une **prédiction purement computationnelle**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer gastrique (adénocarcinome gastrique), cancer bronchique non à petites cellules, carcinome hépatocellulaire (d'après le graphe de connaissances ; le texte d'indication de l'AMM française n'est pas renseigné) |
| Nouvelle Indication Prédite | Adénocarcinome du ligament utérin |
| Score de Prédiction TxGNN | 99,95 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, le ramucirumab est un antagoniste du récepteur VEGFR-2 : il bloque l'angiogenèse induite par le VEGF. Son efficacité a été établie dans des tumeurs solides dépendantes de l'angiogenèse, comme l'adénocarcinome gastrique, le cancer bronchique non à petites cellules et le carcinome hépatocellulaire.

Les adénocarcinomes gynécologiques (ligament utérin, col de l'utérus) dépendent souvent aussi de l'angiogenèse. Le blocage de la voie VEGF/VEGFR-2 a d'ailleurs un rôle établi dans le cancer du col avancé, avec une autre molécule anti-angiogénique (le bévacizumab). Cela offre un raisonnement plausible, mais indirect, au niveau de la classe thérapeutique.

Le score élevé de TxGNN (99,95 %) reflète vraisemblablement la proximité dans le graphe de connaissances avec d'autres adénocarcinomes et noeuds cervicaux, et non une validation biologique ou clinique. Les autres candidats prédits (carcinome endocervical, carcinome adénoïde kystique du col, adénocarcinomes séreux, endométrioïdes, à cellules claires ou mucineux du ligament utérin, variantes à cellules en bague à chaton ou de type intestinal du col) reposent sur le même raisonnement générique. Certaines analogies histologiques avec l'adénocarcinome gastrique (cellules en bague à chaton, type intestinal) restent lâches et n'établissent pas l'efficacité.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63848228 | CYRAMZA 10 mg/ml (Eli Lilly, Pays-Bas), statut : annulée | Solution à diluer pour perfusion | Non renseignée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (anticorps monoclonal anti-VEGFR-2), non cytotoxique conventionnel |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 100 interactions ont été recensées dans les données compilées ; les principales sont de niveau majeur et concernent surtout des médicaments affectant l'hémostase (risque hémorragique potentiel) :
  - Anticoagulants et antithrombotiques : apixaban, bétrixaban, daltéparine, bivalirudine, antithrombine III humaine, défibrotide, caplacizumab
  - Antiagrégants plaquettaires : acide acétylsalicylique, clopidogrel, cilostazol, abciximab, cangrélor
  - Thrombolytique : alteplase
  - Autres : déférasirox, ibritumomab tiuxétan, tositumomab (dont I-131)
  - Niveau modéré : dexfenfluramine, fenfluramine, sibutramine

Les mises en garde et contre-indications de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Les données de sécurité de la notice et le mécanisme d'action sont manquants, et la seule AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), indispensable avant tout examen de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Réaliser une revue systématique de la littérature et des registres d'essais sur le ramucirumab dans les cancers gynécologiques
- Hiérarchiser les entités prédites (par exemple le carcinome endocervical, mieux étayé par le rationnel anti-angiogénique) et évaluer leur plausibilité biologique
- Clarifier le statut réglementaire en France (AMM annulée) et la disponibilité réelle du produit
- Évaluer le risque hémorragique avec les médicaments antithrombotiques dans une population cible précise
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

