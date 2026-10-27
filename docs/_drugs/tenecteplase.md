---
layout: default
title: Tenecteplase
parent: Prédiction du modèle uniquement (L5)
nav_order: 737
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tenecteplase : nouvelle indication prédite, Infarctus du myocarde postéro-inférieur (niveau de preuve L5). Indication d'origine : Infarctus du myocarde"
monitor_inn: "tenecteplase"
predicted_indications: ["congenital coronary artery anomaly", "coronary stenosis", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyropoikilocytosis, hereditary", "pyruvate kinase deficiency of red cells"]
---

# Tenecteplase
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

## Ténectéplase : De l'infarctus du myocarde à l'infarctus postéro-inférieur
{: .text-alpha }

## Résumé en Une Phrase

La ténectéplase est un activateur tissulaire du plasminogène, spécifique de la fibrine, initialement utilisé pour le traitement de l'infarctus du myocarde.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**infarctus du myocarde postéro-inférieur**, mais **aucun essai clinique** ni **aucune publication** spécifique à ce sous-type ne soutient actuellement cette prédiction.
Cette prédiction correspond surtout à un sous-type anatomique de l'indication d'origine, et non à un véritable nouveau signal de repositionnement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infarctus du myocarde (le texte d'indication des AMM n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Infarctus du myocarde postéro-inférieur |
| Score de Prédiction TxGNN | 99,87 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Retiré (AMM annulées uniquement) |
| Nombre d'AMM | 2 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la ténectéplase est un activateur tissulaire du plasminogène spécifique de la fibrine, qui dissout les thrombus dans l'artère coronaire occluse. Son efficacité dans l'infarctus du myocarde est établie.

L'infarctus postéro-inférieur est un sous-type anatomique de l'infarctus du myocarde. Le score TxGNN élevé reflète donc probablement ce chevauchement avec l'indication d'origine, plutôt qu'une découverte nouvelle. Mécanistiquement, la thrombolyse s'applique de la même façon quelle que soit la paroi touchée.

Il convient de noter que les autres prédictions du modèle (anomalie coronaire congénitale, délétion du bras court du chromosome 16, thalassémie bêta, déficits enzymatiques des globules rouges, pyropoïkilocytose héréditaire) ne reposent sur aucun lien mécanistique plausible et semblent être des artefacts du graphe. La mention « hémoglobinopathie » parmi les indications d'origine est elle-même discutable.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'infarctus postéro-inférieur.

À titre indicatif, pour des prédictions voisines de rang inférieur, des publications indirectes existent (par exemple, l'étude de faisabilité de la ténectéplase intracoronaire lors d'une angioplastie primaire, [PMID 31870492](https://pubmed.ncbi.nlm.nih.gov/31870492/), 2020, pour la sténose coronaire). Aucune ne teste la ténectéplase dans l'infarctus postéro-inférieur en tant qu'indication distincte.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65088998 | METALYSE 10 000 unités (50 mg) | Poudre et solvant pour solution injectable | Non renseignée (AMM annulée) |
| 62750941 | METALYSE 5000 unités (25 mg) | Poudre pour solution injectable | Non renseignée (AMM annulée) |

Les deux AMM, détenues par Boehringer Ingelheim International, sont annulées.

---

## Considérations de Sécurité

**Interactions Médicamenteuses** : 137 interactions sont répertoriées. Parmi les principales :
- **Majeures** : abciximab, apixaban, bétrixaban, déférasirox, acalabrutinib, avapritinib, ibritumomab tiuxétan, tositumomab (y compris la forme I-131)
- **Modérées** : acide acétylsalicylique, kétorolac, ibuprofène, célécoxib, acide aminocaproïque, oméga-3, dexfenfluramine, fenfluramine, sibutramine

Ces interactions concernent surtout un risque hémorragique accru lors de l'association avec des anticoagulants, antiagrégants et anti-inflammatoires.

Veuillez consulter la notice pour les mises en garde et contre-indications.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction ne repose sur aucune preuve spécifique (L5) et reprend l'indication de l'infarctus du myocarde, déjà connue. De plus, les deux AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications issues de la notice ANSM (données bloquantes pour l'évaluation de sécurité)
- Les données sur le mécanisme d'action, à compléter via DrugBank
- Une clarification du statut réglementaire actuel du produit en France
- Des données cliniques spécifiques au sous-type postéro-inférieur, si une exploration est jugée pertinente
- Parmi les autres prédictions, seule la sténose coronaire (niveau L3, question de recherche) présente une littérature indirecte à approfondir ; les autres prédictions sont à écarter faute de plausibilité mécanistique
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

