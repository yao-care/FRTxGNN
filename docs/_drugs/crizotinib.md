---
layout: default
title: Crizotinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib : Du cancer bronchique non à petites cellules ALK-positif à la fibromatose gingivale

## Résumé en Une Phrase

Le crizotinib est un inhibiteur de tyrosine kinase (ALK, ROS1, MET), initialement utilisé dans le cancer bronchique non à petites cellules (CBNPC) avec réarrangement ALK ou ROS1.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **fibromatose gingivale**, mais cette prédiction repose uniquement sur un graphe de connaissances : **0 essai clinique** et **0 publication** ne la soutiennent actuellement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | CBNPC ALK/ROS1-positif (d'après la littérature ; le texte d'indication des AMM n'est pas renseigné dans les données) |
| Nouvelle Indication Prédite | Fibromatose gingivale |
| Score de Prédiction TxGNN | 99,81 % (rang 1922) |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, le crizotinib est un inhibiteur compétitif de l'ATP des récepteurs à tyrosine kinase ALK, ROS1 et c-MET. Son efficacité est établie dans le CBNPC porteur d'un réarrangement ALK ou ROS1.

**À ce stade, il n'existe pas de lien mécanistique identifié** entre ces cibles et la fibromatose gingivale. Le score TxGNN élevé (0,998) est une prédiction issue du graphe et ne constitue pas une preuve biologique ou clinique. La similarité avec l'indication d'origine reste à évaluer.

Cette prédiction doit donc être considérée comme une hypothèse de travail, à documenter avant toute exploration : une voie ALK, ROS1 ou MET impliquée dans la fibromatose gingivale n'est étayée par aucune donnée fournie.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 66937155 | XALKORI 200 mg, gélule | Gélule |
| 61506083 | XALKORI 250 mg, gélule | Gélule |

Titulaire des deux AMM : PFIZER EUROPE MA EEIG (Belgique). Voie d'administration : orale (gélule).

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase ALK/ROS1/MET) |
| Éléments de Surveillance | Fonction hépatique et surveillance cardiaque (ECG), d'après les signaux de toxicité rapportés dans la littérature du dossier (voir ci-dessous) |

Pour le risque de myélosuppression, l'émétogénicité et la protection de manipulation, veuillez consulter les mises en garde et précautions de la notice.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Les mises en garde, contre-indications et interactions médicamenteuses ne sont pas disponibles dans le dossier.

À titre indicatif, la littérature associée aux autres prédictions du dossier signale, chez des patients traités par crizotinib : insuffisance hépatique fulminante (cas fatal), toxicités cardiaques (bradycardie, allongement du QT), pneumopathie médicamenteuse (pneumopathie organisée) et érythème polymorphe. Ces éléments ne remplacent pas la notice officielle.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction est de niveau L5 : aucun essai clinique, aucune publication, aucun lien mécanistique identifié pour la fibromatose gingivale.
- Le dossier de sécurité est incomplet (notice ANSM non exploitée), ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications, interactions).
- Obtenir les données de mécanisme d'action via DrugBank (DB08865).
- Rechercher une hypothèse mécanistique reliant ALK, ROS1 ou MET à la fibromatose gingivale, ainsi que toute étude préclinique ou rapport de cas.
- Évaluer la compatibilité de la voie d'administration (orale) avec la pathologie visée.
- À titre de comparaison, dans le même dossier, le carcinome du hile pulmonaire (rang 4) et la tumeur germinale pulmonaire (rang 7) atteignent le niveau L4 et l'étape S1 (« Research Question ») : ils sont plus mûrs que cette prédiction.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement doit faire l'objet d'une validation clinique.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

