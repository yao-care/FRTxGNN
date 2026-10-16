---
layout: default
title: Ceritinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 154
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ceritinib : nouvelle indication prédite, Fibromatose gingivale (niveau de preuve L5). Indication d'origine : Cancer bronchique non à petites cellules"
---

# Ceritinib
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

# Ceritinib : Du Cancer Bronchique Non à Petites Cellules à la Fibromatose Gingivale

## Résumé en Une Phrase

Ceritinib est un inhibiteur de la kinase ALK, initialement utilisé pour le traitement du cancer bronchique non à petites cellules (CBNPC) ALK-positif.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **fibromatose gingivale**, mais cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer bronchique non à petites cellules ; cancer du poumon (le texte d'indication de l'AMM n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Fibromatose gingivale |
| Score de Prédiction TxGNN | 99,86 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Retiré (AMM annulée uniquement) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, ceritinib est un inhibiteur de tyrosine kinase ciblant ALK (et, selon la littérature, également IGF-1R, FAK et ROS1). Son efficacité a été démontrée dans le CBNPC avec réarrangement ALK, notamment dans l'essai de phase 3 ASCEND-4.

Pour la fibromatose gingivale, **aucun lien mécanistique n'est étayé par les données compilées**. Le score élevé du modèle (99,86 %) est une prédiction seule. La voie ALK n'a pas de rôle documenté dans cette maladie, qui est une affection gingivale héréditaire. La similarité avec l'indication d'origine n'a pas été évaluée.

À titre de comparaison, parmi les dix prédictions les mieux classées, plusieurs concernent des tumeurs pulmonaires (carcinome du hile pulmonaire, tumeur du sillon pulmonaire). Elles recoupent l'indication existante du CBNPC et ne constituent pas de véritables signaux de repositionnement. Une seule piste présente un soutien indirect : la tumeur germinale pulmonaire (niveau L4, « question de recherche »), pour laquelle la littérature montre l'activité de ceritinib sur des tumeurs ALK-altérées hors CBNPC (glioblastome, neuroblastome). Ce soutien ne concerne pas les tumeurs germinales elles-mêmes.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la fibromatose gingivale.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66958808 | ZYKADIA 150 mg, gélule (NOVARTIS EUROPHARM, Irlande) | Gélule | Non renseignée (AMM annulée) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase ALK) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Fonction hépatique et ECG (intervalle QT), d'après la littérature récupérée ; autres paramètres : voir la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 629 interactions sont recensées. Parmi celles listées dans les données compilées, deux sont de niveau **majeur** : la **triamcinolone** et le **budésonide**. Les autres sont de niveau modéré, notamment les antiacides et inhibiteurs de la sécrétion gastrique (famotidine, ranitidine, oméprazole, rabéprazole), des corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone), des antidiabétiques (metformine, pioglitazone, alogliptine, acarbose, canagliflozine, albiglutide), le lopéramide, l'aprépitant et le bisacodyl.
- **Signaux de sécurité issus de la littérature** : allongement de l'intervalle QT, hypersensibilité (cas rapporté de pneumopathie infiltrante diffuse avec péricardite et épanchement pleural) et toxicités cardiaques des inhibiteurs de tyrosine kinase.

Les mises en garde et contre-indications officielles n'ont pas pu être récupérées. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la fibromatose gingivale repose uniquement sur le modèle (L5), sans essai clinique, sans littérature et sans lien mécanistique documenté. De plus, l'AMM française est annulée et le profil d'interactions est lourd, ce qui rend difficile de justifier un traitement systémique par inhibiteur de kinase sans données à l'appui.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action de ceritinib (DrugBank) et analyse du lien éventuel entre la voie ALK et la fibromatose gingivale
- Mises en garde et contre-indications officielles (notice de l'ANSM), indispensables avant tout examen de sécurité
- Recherche ciblée d'études précliniques ou de cas cliniques dans cette indication
- Évaluation de la faisabilité de la voie d'administration et de la situation réglementaire (AMM annulée)
- Piste alternative à explorer en priorité : vérifier si certaines tumeurs germinales pulmonaires portent des altérations d'ALK
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

