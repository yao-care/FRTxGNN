---
layout: default
title: Pentosan Polysulfate
parent: Prédiction du modèle uniquement (L5)
nav_order: 588
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
monitor_inn: "pentosan polysulfate"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease"]
description: "Pentosan Polysulfate : nouvelle indication prédite, Trouble primaire de la libération plaquettaire (primary release disorder of platelets) (niveau de preuve L5). Indication d'origine : Non renseignée…"
---

# Pentosan Polysulfate
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

## Pentosan Polysulfate: Trouble primaire de la libération plaquettaire (primary release disorder of platelets)
{: .text-alpha }

## Résumé en Une Phrase

Le pentosane polysulfate (ELMIRON 100 mg, gélule) était initialement utilisé pour le traitement de la **cystite interstitielle**.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble primaire de la libération plaquettaire** (« primary release disorder of platelets »).
Cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Trouble primaire de la libération plaquettaire (primary release disorder of platelets) |
| Score de Prédiction TxGNN | 0.9971 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le pentosane polysulfate est un polysaccharide sulfaté dont les propriétés ressemblent à celles de l'héparine : il possède une activité anticoagulante et un effet antiplaquettaire faible. Son efficacité dans la cystite interstitielle est l'indication d'origine.

**La plausibilité biologique de cette prédiction est faible.** Un composé à action anticoagulante et antiplaquettaire devrait plutôt aggraver un défaut de sécrétion plaquettaire qu'en améliorer l'évolution. L'association retrouvée par le modèle reflète probablement une proximité dans le réseau de connaissances (nœuds communs de coagulation et de fonction plaquettaire) plutôt qu'une véritable relation thérapeutique.

Le même constat s'applique aux deux autres prédictions les mieux classées, également sans aucune preuve clinique ni publication :
- **Thrombasthénie de Glanzmann** (score 0,9965) : liée à un déficit ou un dysfonctionnement de l'intégrine αIIbβ3 (GPIIb/IIIa). Un effet anticoagulant risquerait d'aggraver le phénotype hémorragique.
- **Pseudo-maladie de von Willebrand** (score 0,9962) : liée à un gain de fonction de la GPIbα plaquettaire. Une interaction du pentosane polysulfate avec le facteur von Willebrand ou les glycoprotéines plaquettaires est spéculative, et l'effet anticoagulant augmenterait le risque hémorragique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut | Indication Approuvée |
|---------|------|------|------|-----------|
| 60027685 | ELMIRON 100 mg, gélule | Gélule | Active | Non renseignée |

Le produit est fabriqué par BENE-ARZNEIMITTEL (Allemagne). Il est commercialisé, avec 1 AMM valide sur 1.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie, et non texte de la notice) : maladie du foie, maladie de la vésicule biliaire, thrombopénie, trouble de la coagulation sanguine, hémophilie, thrombopénie induite par l'héparine.
- **Interactions médicamenteuses** : 58 interactions recensées, toutes celles listées étant de niveau modéré. Elles concernent principalement des médicaments affectant l'hémostase, avec un risque hémorragique additif :
  - Antiagrégants plaquettaires : acide acétylsalicylique, clopidogrel, cilostazol, dipyridamole, abciximab, cangrelor
  - Anticoagulants : warfarine, apixaban, édoxaban, bétrixaban, daltéparine, bivalirudine, antithrombine III
  - Thrombolytiques et autres : altéplase, anistreplase, défibrotide, caplacizumab
  - Radio-immunothérapies : ibritumomab tiuxétan, tositumomab (I-131) et tositumomab

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication. Le mécanisme anticoagulant du médicament va à l'encontre d'un bénéfice dans des troubles plaquettaires hémorragiques, et les contre-indications du graphe incluent déjà les troubles de la coagulation et la thrombopénie. L'AMM française est en outre annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice officielle (mises en garde et contre-indications) auprès de l'ANSM : lacune bloquante pour tout examen de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (par ex. via l'API DrugBank)
- Rechercher d'éventuelles études précliniques ou publications sur le pentosane polysulfate et la fonction plaquettaire
- Réévaluer la pertinence biologique de la prédiction avant tout investissement, compte tenu du risque hémorragique attendu
- Clarifier la compatibilité des voies d'administration et la similarité avec l'indication d'origine (actuellement non évaluées)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

