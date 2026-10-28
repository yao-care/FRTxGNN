---
layout: default
title: Dalteparin
parent: Prédiction du modèle uniquement (L5)
nav_order: 210
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
monitor_inn: "dalteparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive", "primary release disorder of platelets", "pseudo-von Willebrand disease", "atypical hemolytic-uremic syndrome with thrombomodulin anomaly", "neuropathy, painful"]
description: "Dalteparin : nouvelle indication prédite, Thrombophilie par déficit en protéine C, autosomique récessif (thrombophilia due to protein C deficiency… (niveau de preuve L5). Indication d'origine : Non r…"
---

# Dalteparin
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

## Dalteparin: Thrombophilie par déficit en protéine C, autosomique récessif (thrombophilia due to protein C deficiency, autosomal recessive)
{: .text-alpha }

## Résumé en Une Phrase

La daltéparine est une héparine de bas poids moléculaire, initialement utilisée dans la prise en charge de l'embolie pulmonaire, de la coagulation intravasculaire disséminée et du purpura fulminans.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **thrombophilie par déficit en protéine C (autosomique récessif)**,
mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Thrombophilie par déficit en protéine C, autosomique récessif (thrombophilia due to protein C deficiency, autosomal recessive) |
| Score de Prédiction TxGNN | 0.9988 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 9 sur 9) |
| Nombre d'AMM | 9 (valides : 9) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, la daltéparine est une héparine de bas poids moléculaire : elle potentialise l'antithrombine et inhibe le facteur Xa.

Le déficit homozygote en protéine C supprime une voie anticoagulante naturelle et crée un état prothrombotique. Le purpura fulminans, déjà parmi les indications d'origine, en est la présentation sévère classique. Le lien biologique est donc cohérent : une anticoagulation pourrait contrebalancer l'excès de thrombose.

Cette plausibilité reste théorique. La prise en charge de référence associe le remplacement de la protéine C et l'anticoagulation ; la daltéparine ne jouerait donc, au mieux, qu'un rôle complémentaire. Le score très élevé (0,9988) est une prédiction informatique, non une preuve clinique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour cette indication.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61540502 | FRAGMINE 10 000 U.I. anti Xa/1 mL | Solution injectable (seringue préremplie) | Non renseignée |
| 60521926 | FRAGMINE 18 000 U.I. anti-Xa/0,72 mL | Solution injectable (seringue préremplie) | Non renseignée |
| 66032251 | FRAGMINE 5 000 U.I. anti Xa/0,2 mL | Solution injectable (seringue préremplie) | Non renseignée |
| 67591667 | FRAGMINE 10 000 U.I. anti-Xa/0,4 mL | Solution injectable (seringue préremplie) | Non renseignée |
| 62114270 | FRAGMINE 12 500 U.I. anti-Xa/0,5 mL | Solution injectable (seringue préremplie) | Non renseignée |


---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique, thrombopénie, thrombopénie induite par l'héparine, hémophilie et autres troubles de la coagulation, déficit en antithrombine III, hémorragie intracrânienne ou intracérébrale, ulcère gastroduodénal actif, maladies inflammatoires chroniques de l'intestin, endocardite infectieuse, rétinopathies (diabétique, hypertensive), décollement placentaire, thrombasthénie de Glanzmann et déficits qualitatifs des plaquettes, ostéoporose.
- **Interactions médicamenteuses** : 174 interactions recensées. Parmi les principales, de niveau majeur : acide acétylsalicylique, ibuprofène, kétorolac, fondaparinux, abciximab, acalabrutinib, déférasirox, trastuzumab emtansine, ibritumomab tiuxétan et tositumomab. Plusieurs interactions de niveau modéré existent également (fluvoxamine, fosinopril, sugammadex, fenfluramine, sibutramine, iodures radioactifs).
- **Alerte spécifique** : pour trois autres indications prédites (trouble de la libération plaquettaire, pseudo-maladie de von Willebrand, neuropathie douloureuse), l'effet anticoagulant pourrait aggraver le risque hémorragique et aucun lien mécanistique crédible n'existe ; elles ne sont pas recommandées.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être consultées : veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle TxGNN (apprentissage profond, niveau L5), sans essai ni publication. Le score peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique. Le médicament est commercialisé en France (9 AMM valides sur 9) ; les données de sécurité officielles sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), préalable indispensable au criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Réaliser une revue de la littérature sur l'héparine de bas poids moléculaire dans le déficit en protéine C et le purpura fulminans
- Clarifier le statut réglementaire (AMM annulées) et la disponibilité réelle du produit en France
- Évaluer la compatibilité des voies d'administration et la place éventuelle en traitement complémentaire du remplacement de la protéine C
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

