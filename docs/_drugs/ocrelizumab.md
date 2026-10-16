---
layout: default
title: Ocrelizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 551
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Ocrelizumab : nouvelle indication prédite, Carcinome mammaire HER2 positif (niveau de preuve L5). Indication d'origine : Sclérose en plaques progressive"
---

# Ocrelizumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

# Ocrelizumab : De la sclérose en plaques progressive au carcinome mammaire HER2 positif

## Résumé en Une Phrase

Ocrelizumab est un anticorps monoclonal anti-CD20 initialement utilisé pour le traitement de la sclérose en plaques progressive.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **carcinome mammaire HER2 positif**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette indication : la prédiction repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Sclérose en plaques progressive (indication issue du graphe de connaissances, le texte d'indication des AMM n'étant pas renseigné) |
| Nouvelle Indication Prédite | Carcinome mammaire HER2 positif |
| Score de Prédiction TxGNN | 99,89 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Annulé uniquement (aucune AMM valide) |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, l'ocrelizumab est un anticorps monoclonal humanisé anti-CD20 qui déplète les lymphocytes B. Son efficacité a été démontrée dans la sclérose en plaques, notamment dans sa forme primaire progressive.

Aucun lien mécanistique direct n'est établi entre la déplétion des lymphocytes B par ciblage du CD20 et la biologie tumorale dépendante de HER2. Le score élevé du modèle (0,999) est une prédiction issue du graphe de connaissances, sans soutien clinique ou bibliographique. Cette prédiction doit donc être considérée comme une simple hypothèse à explorer, et non comme un résultat étayé.

D'autres sous-types de cancer du sein figurent parmi les prédictions (récepteurs de la progestérone positifs ou négatifs, sous-type de type « normal breast-like », tumeurs luminales A ou B), avec des scores similaires (environ 0,998) et la même absence de preuves. Des scores identiques pour plusieurs sous-types suggèrent que le modèle reflète un voisinage commun dans le graphe plutôt qu'une biologie propre à chaque sous-type.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée à l'indication principale (carcinome mammaire HER2 positif) n'est disponible actuellement.

À titre d'information, 18 publications ont été rattachées à une autre prédiction (tumeurs mammaires luminales A ou B). Elles portent sur l'ocrelizumab dans la sclérose en plaques (essais OPERA et ORATORIO, OCARINA II, revues), les thérapies anti-CD20 et d'autres sujets d'immunologie. **Aucune n'évalue l'ocrelizumab dans le cancer du sein**. Il s'agit vraisemblablement d'un artefact de recherche et non d'une preuve en faveur de cette indication.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66127361 | OCREVUS 300 mg, solution à diluer pour perfusion (annulée) | Solution à diluer pour perfusion | Non renseignée |
| 62251899 | OCREVUS 920 mg, solution injectable (annulée) | Solution injectable | Non renseignée |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 280 interactions ont été recensées. Parmi celles listées :
  - Niveau modéré : corticoïdes (hydrocortisone, prednisolone, prednisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), radiopharmaceutiques (iobenguane I-131, ibritumomab tiuxétan, tositumomab, samarium-153 lexidronam), albendazole, pentamidine, lévamisole.
  - Niveau mineur : sels de zinc (sulfate, acétate, gluconate, chlorure).
- **Hypogammaglobulinémie secondaire** : la littérature rattachée la signale comme un enjeu de sécurité, qui serait particulièrement pertinent chez des patients en oncologie déjà immunodéprimés par leurs traitements.

Veuillez consulter la notice pour les mises en garde et contre-indications, qui ne sont pas disponibles dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique, sans publication pertinente et sans lien mécanistique plausible entre l'anti-CD20 et le cancer du sein HER2 positif. De plus, aucune AMM n'est actuellement valide en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications issues de la notice de l'ANSM (lacune bloquante pour le dépistage de sécurité).
- Les données sur le mécanisme d'action, à obtenir via DrugBank.
- Une justification biologique d'un rôle du CD20 ou des lymphocytes B dans le cancer du sein HER2 positif.
- Des données précliniques ou cliniques spécifiques à cette indication.
- Le statut réglementaire actuel du produit en France (AMM annulées).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

