---
layout: default
title: Salbutamol
parent: Prédiction du modèle uniquement (L5)
nav_order: 690
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Salbutamol : nouvelle indication prédite, Conjonctivite papillaire (niveau de preuve L5). Indication d'origine : Asthme, maladie bronchique"
monitor_inn: "SALBUTAMOL"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture", "obstructive lung disease"]
---

# Salbutamol
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

# Salbutamol : De l'asthme à la conjonctivite papillaire

## Résumé en une phrase

Le salbutamol est un bêta-2 agoniste, utilisé à l'origine pour traiter l'asthme et les maladies bronchiques.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **conjonctivite papillaire**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

---

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Asthme, maladie bronchique (d'après le graphe de connaissances, faute d'AMM française) |
| Nouvelle indication prédite | Conjonctivite papillaire |
| Score de prédiction TxGNN | 99,996 % (rang 141) |
| Niveau de preuve | L5 |
| Statut de marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision recommandée | Hold |

---

## Pourquoi cette prédiction est-elle raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le salbutamol appartient à la classe des bêta-2 agonistes. Son efficacité dans l'asthme et les maladies bronchiques est établie, et il pourrait être mécanistiquement applicable à la conjonctivite papillaire.

Les données compilées indiquent que les bêta-2 agonistes ont montré, dans des modèles précliniques, des effets anti-inflammatoires et de stabilisation des mastocytes dans le tissu conjonctival. Une inflammation conjonctivale de nature allergique pourrait donc, en théorie, y être sensible.

Cette plausibilité reste toutefois théorique. L'asthme (voie respiratoire) et la conjonctivite papillaire (surface oculaire) sont des maladies très différentes. Aucune étude clinique ou publication propre à cette indication n'a été retrouvée pour le salbutamol. La similarité avec l'indication originale n'a pas encore été évaluée.

---

## Preuves d'essais cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la littérature

Aucune littérature associée disponible actuellement.

---

## Considérations de sécurité

Les notices de l'ANSM n'ont pas pu être exploitées : les mises en garde et contre-indications officielles ne sont donc pas disponibles. Veuillez consulter la notice pour ces informations.

- **Contre-indications issues du graphe de connaissances** (elles ne proviennent pas du texte de la notice) : hypertension artérielle, syndrome du QT long (y compris familial), épilepsie, hypokaliémie (déficit en potassium), diabète sucré, acidocétose diabétique, acidose (dont l'acidose métabolique), hypertrophie bénigne de la prostate, obstruction du col vésical, hypertension oculaire, glaucome à angle fermé, hyperthyroïdie (maladie de Basedow, thyrotoxicose), arrêt cardiaque soudain, maladie de la conduction cardiaque, ischémie myocardique, maladie coronarienne.
- **Interactions médicamenteuses** : 100 interactions sont recensées. Parmi les premières de la liste :
  - de niveau modéré : acarbose, isométheptène, famotidine, épinéphrine, albiglutide, acétohexamide, alogliptine, bisacodyl, canagliflozine, huile de ricin, chlorpropamide, cisapride, clarithromycine, dapagliflozine, diéthylpropion ;
  - de niveau mineur : hydrocortisone, béclométasone, bétaméthasone, budésonide, dexaméthasone.
- Certaines contre-indications (glaucome à angle fermé, hypertension oculaire) sont particulièrement pertinentes pour une application oculaire et demanderaient une évaluation spécifique.

---

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai clinique ni publication ne la soutient, et le produit n'est pas commercialisé en France.
- Les données de sécurité officielles et le mécanisme d'action manquent, ce qui empêche toute évaluation de sécurité approfondie.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), point bloquant à ce stade.
- Compléter les données sur le mécanisme d'action (DrugBank).
- Générer des preuves propres à l'indication : études précliniques oculaires puis essais cliniques chez l'humain.
- Évaluer la compatibilité des voies d'administration, car aucune forme oculaire n'est identifiée dans les données compilées.

**Remarque :** d'autres indications prédites disposent de preuves plus solides que la conjonctivite papillaire :
- la **bronchite** (niveau L2, essais de phase 2 mais bénéfice limité selon les revues Cochrane) ;
- l'**anaphylaxie** et le **rhume** (niveau L3) ;
- les **maladies pulmonaires obstructives** (niveau L1, mais cette indication recoupe l'indication originale et n'est pas un véritable repositionnement).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

