---
layout: default
title: Rasburicase
parent: Prédiction du modèle uniquement (L5)
nav_order: 654
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "RASBURICASE"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "hepatic porphyria", "early-onset familial noncirrhotic portal hypertension", "hepatoportal sclerosis", "primitive portal vein thrombosis", "hepatopulmonary syndrome", "idiopathic copper-associated cirrhosis", "renal tubular acidosis", "disorder of phenylalanine metabolism"]
description: "Rasburicase : nouvelle indication prédite, Hypouricémie rénale (hypouricemia, renal) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Rasburicase
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

## Rasburicase: Hypouricémie rénale (hypouricemia, renal)
{: .text-alpha }

## Résumé en Une Phrase

Rasburicase est une enzyme recombinante (urate oxydase), initialement utilisée pour le traitement de l'hyperuricémie.
Le modèle TxGNN (apprentissage profond) la prédit comme potentiellement efficace pour l'**hypouricémie rénale**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction. Le score provient du modèle TxGNN et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique ; la prédiction pourrait même être une inversion de sens (contre-indication plutôt qu'indication).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Hypouricémie rénale (hypouricemia, renal) |
| Score de Prédiction TxGNN | 0.9999 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, la rasburicase est une urate oxydase recombinante qui convertit l'acide urique en allantoïne, ce qui abaisse l'uricémie. Son usage d'origine concerne donc les situations d'excès d'acide urique.

La prédiction du modèle pose problème. L'hypouricémie rénale est un état de **faible** taux d'acide urique (perte de fonction de URAT1/GLUT9). Réduire davantage l'urate n'a aucune justification thérapeutique et pourrait être nocif (par exemple, insuffisance rénale aiguë après effort). Le score élevé provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies liées au métabolisme de l'acide urique, et non une preuve biologique. La prédiction est vraisemblablement inversée : il s'agirait plutôt d'une contre-indication que d'une indication.

### Autres prédictions du modèle

Neuf autres indications prédites figurent dans les données compilées. Toutes sont au niveau L5, sans essai ni publication, et la décision est Hold pour chacune.

| Rang | Maladie prédite | Score TxGNN | Évaluation du lien mécanistique |
|---|---|---|---|
| 2 | Déficit partiel en hypoxanthine-guanine phosphoribosyltransférase | 0,9997 | Lien biologique faible avec l'hyperuricémie. Usage parentéral de courte durée, ne corrige pas le défaut de récupération des purines. Risques d'hémolyse (déficit en G6PD), de méthémoglobinémie et d'immunogénicité. |
| 3 | Porphyrie hépatique | 0,9997 | Aucun lien mécanistique identifié ; artefact de proximité dans le réseau. |
| 4 | Hypertension portale familiale non cirrhotique à début précoce | 0,9997 | Aucun lien ; scores identiques entre plusieurs entités voisines, ce qui suggère un chemin prédictif commun. |
| 5 | Sclérose hépatoportale | 0,9997 | Aucun lien direct ; le score provient du modèle TxGNN et peut refléter des similarités apprises entre maladies apparentées, non une preuve biologique. |
| 6 | Thrombose portale primitive | 0,9997 | Aucune activité anticoagulante ou thrombolytique. |
| 7 | Syndrome hépatopulmonaire | 0,9997 | Aucun rôle reconnu ; le risque de méthémoglobinémie l'emporte sur tout bénéfice spéculatif. |
| 8 | Cirrhose idiopathique associée au cuivre | 0,9997 | Aucun lien avec l'accumulation hépatique de cuivre. |
| 9 | Acidose tubulaire rénale | 0,9985 | Pas d'action sur le transport acido-basique ; lien spéculatif ; risques liés au peroxyde d'hydrogène et à l'hémolyse. |
| 10 | Trouble du métabolisme de la phénylalanine | 0,9983 | Aucun lien avec la voie de la phénylalanine hydroxylase ; artefact probable entre erreurs innées du métabolisme. |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69211156 | FASTURTEC 1,5 mg/ml, poudre et solvant pour solution à diluer pour perfusion (SANOFI WINTHROP INDUSTRIE) | Poudre et solvant pour solution à diluer pour perfusion | Non renseignée ; AMM active |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 13 interactions ont été identifiées, dont deux de niveau majeur :
  - **Majeures** : prilocaïne ; acide nitreux.
  - **Modérées** : anesthésiques locaux (tétracaïne ophtalmique et topique, lidocaïne topique et ophtalmique, benzocaïne topique, cocaïne topique et nasale, proparacaïne ophtalmique, oxybuprocaïne ophtalmique, cinchocaïne topique) et idélalisib.
- **Risques liés à la classe et au mécanisme** (issus de l'analyse des indications prédites) : hémolyse en cas de déficit en G6PD, méthémoglobinémie, immunogénicité en cas d'administrations répétées, production de peroxyde d'hydrogène.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction principale (hypouricémie rénale) est mécanistiquement contradictoire avec l'action de la rasburicase et pourrait être nocive. Aucune des dix prédictions n'est étayée par un essai ou une publication (niveau L5). La seule AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice de l'ANSM, indispensables pour le criblage de sécurité initial
- Les données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Une vérification du sens de la prédiction (indication ou contre-indication) pour l'hypouricémie rénale
- Pour les prédictions secondaires, notamment le déficit partiel en HPRT, une revue de la littérature et une évaluation de la faisabilité (voie parentérale, usage de courte durée, risque d'hémolyse)
- La compatibilité des voies d'administration et la similarité avec l'indication d'origine, actuellement non évaluées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

