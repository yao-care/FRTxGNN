---
layout: default
title: Heparin
parent: Prédiction du modèle uniquement (L5)
nav_order: 377
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Heparin : nouvelle indication prédite, Thrombophilie par déficit en protéine C, autosomique récessive (niveau de preuve L5). Indication d'origine : Embolie pulmonaire, coagulation intravasculaire dis…"
---

# Heparin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Héparine : De l'embolie pulmonaire au déficit en protéine C (thrombophilie autosomique récessive)

## Résumé en Une Phrase

L'héparine est un anticoagulant initialement utilisé pour traiter l'embolie pulmonaire, la coagulation intravasculaire disséminée et le purpura fulminans.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **thrombophilie par déficit en protéine C (forme autosomique récessive)**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : la prédiction repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Embolie pulmonaire, coagulation intravasculaire disséminée, purpura fulminans (texte d'indication des AMM non renseigné) |
| Nouvelle Indication Prédite | Thrombophilie par déficit en protéine C, autosomique récessive |
| Score de Prédiction TxGNN | 99,29 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 11 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances pharmacologiques générales, l'héparine potentialise l'antithrombine et inhibe la thrombine ainsi que le facteur Xa. Son efficacité a été reconnue dans des états thrombotiques comme l'embolie pulmonaire.

Le déficit en protéine C entraîne la perte d'une voie anticoagulante naturelle et un état d'hypercoagulabilité. Une anticoagulation par héparine pourrait, en principe, compenser ce déséquilibre. Le lien avec l'indication d'origine est notable : le purpura fulminans est une manifestation typique du déficit sévère en protéine C.

Ce raisonnement reste toutefois théorique. Le score élevé du modèle est une prédiction computationnelle et aucune preuve directe (essai ou publication) n'a été identifiée pour cette indication.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

*Remarque : une seconde indication prédite (trouble primaire de la libération plaquettaire, score de 99,06 %) est associée à 20 publications, mais celles-ci portent surtout sur la coagulation en général, la thrombopénie induite par l'héparine ou des sujets sans rapport. Aucune n'évalue l'héparine comme traitement de ce trouble. Le mécanisme est faible, voire contradictoire (l'héparine augmente le risque hémorragique), et cette piste n'est pas retenue.*

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65476933 | HEPARINE CHOAY 25 000 UI/5 mL | Solution injectable | Non renseignée (AMM annulée) |
| 63018531 | CALCIPARINE SOUS CUTANEE 25 000 UI/1 ml | Solution injectable | Non renseignée (AMM annulée) |
| 65822577 | HEPARINE CHOAY 5 000 UI/1 mL | Solution injectable | Non renseignée (AMM annulée) |
| 60852495 | CALCIPARINE SOUS CUTANEE 20 000 UI/0,8 ml | Solution injectable | Non renseignée (AMM annulée) |
| 64395923 | HEPARINE SODIQUE PANPHARMA 5 000 UI/ml (I.V.) | Solution injectable | Non renseignée (AMM annulée) |

Au total, 11 AMM figurent dans les données, toutes annulées ; aucune AMM valide n'est recensée.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (non issues de la notice)** : insuffisance hépatique, thrombopénie, thrombopénie induite par l'héparine, hémophilie, maladies de la coagulation, déficit en antithrombine III, hémorragie intracrânienne ou intracérébrale, ulcère gastroduodénal actif, endocardite infectieuse, rétinopathie diabétique ou hypertensive, ostéoporose, rectocolite hémorragique et maladies inflammatoires chroniques de l'intestin, décollement placentaire, thrombasthénie de Glanzmann, anomalies qualitatives des plaquettes, entre autres.
- **Interactions médicamenteuses** : 614 interactions recensées. Les principales de niveau modéré concernent l'acide acétylsalicylique et plusieurs antidiabétiques (glimépiride, glipizide, glibenclamide, répaglinide, natéglinide, tolbutamide, chlorpropamide, etc.), ainsi que la fenfluramine, la dexfenfluramine et la sibutramine.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être obtenues. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication pour l'indication principale.
- Toutes les AMM françaises sont annulées et les données de sécurité officielles sont absentes, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Mener une revue ciblée de la littérature sur l'héparine dans le déficit en protéine C (cas cliniques, séries, recommandations).
- Clarifier le statut réglementaire actuel de l'héparine en France, les AMM étant toutes annulées.
- Évaluer la compatibilité des voies d'administration et la similarité avec l'indication d'origine, aujourd'hui non évaluées.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

