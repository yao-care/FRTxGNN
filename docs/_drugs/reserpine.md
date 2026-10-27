---
layout: default
title: Reserpine
parent: Prédiction du modèle uniquement (L5)
nav_order: 661
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Reserpine : nouvelle indication prédite, Schizophrénie résistante au traitement (niveau de preuve L5). Indication d'origine : Hypertension artérielle et troubles psychotiques"
---

# Reserpine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Réserpine : De l'Hypertension et des Troubles Psychotiques à la Schizophrénie Résistante au Traitement
{: .text-alpha }

## Résumé en Une Phrase

La réserpine est un médicament historiquement utilisé pour traiter l'hypertension artérielle et les troubles psychotiques (dont la schizophrénie et les troubles apparentés).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **schizophrénie résistante au traitement**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle et troubles psychotiques (selon le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Schizophrénie résistante au traitement |
| Score de Prédiction TxGNN | 99,04 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Autorisation annulée uniquement (non commercialisé) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances pharmacologiques générales, la réserpine inhibe de façon irréversible le transporteur vésiculaire des monoamines de type 2 (VMAT2). Cela appauvrit les réserves présynaptiques de dopamine, de noradrénaline et de sérotonine.

La déplétion en dopamine est cohérente avec une activité antipsychotique. La réserpine a d'ailleurs été utilisée autrefois comme l'un des premiers antipsychotiques dans la schizophrénie et d'autres troubles psychotiques, ce qui correspond à ses indications d'origine. La nouvelle indication prédite s'inscrit donc dans la continuité de cet usage historique.

Il faut toutefois interpréter le score élevé (99,04 %) avec prudence. Il reflète probablement l'association déjà connue du médicament avec la schizophrénie et les troubles psychotiques dans le graphe de connaissances, et non une efficacité démontrée dans la forme résistante au traitement. De plus, la réserpine a été largement remplacée par des antipsychotiques plus récents en raison d'effets indésirables tels que dépression, sédation, hypotension et syndrome parkinsonien.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61977014 | TENSIONORME, comprimé sécable (ETHYX PHARMACEUTICALS) | Comprimé sécable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : insuffisance hépatique, maladie hépatique, cirrhose, encéphalopathie hépatique et coma hépatique ; maladie rénale et anurie ; épilepsie ; troubles anxieux, névrotiques et dysthymiques ; ulcère gastroduodénal ; pancréatite ; maladie de la vésicule biliaire ; lupus érythémateux systémique (y compris pédiatrique) ; diabète et acidocétose diabétique ; goutte et hyperuricémie ; hypotension ; hyperparathyroïdie, ostéite fibrokystique, hypercalcémie et néphrocalcinose ; troubles du métabolisme du phosphore ; carence en potassium ; pyo-uretère ; ictère néonatal ; acétylation lente.
- **Interactions médicamenteuses** : 103 interactions recensées. Les 20 premières sont de niveau modéré et concernent notamment :
  - l'épinéphrine ;
  - les corticoïdes (hydrocortisone, triamcinolone, dexaméthasone, bétaméthasone, budésonide) ;
  - le bupropion ;
  - les antidiabétiques (canagliflozine, dapagliflozine, empagliflozine, chlorpropamide, glimépiride, répaglinide, insulines asparte, dégludec, détémir et glargine) ;
  - les anorexigènes et stimulants (diéthylpropion, phentermine, dronabinol).

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. La réserpine n'a plus d'autorisation valide en France, et son profil d'effets indésirables ainsi que ses nombreuses interactions et contre-indications limitent l'intérêt d'un repositionnement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications) auprès de l'ANSM, une étape bloquante pour le criblage de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank).
- Rechercher des études cliniques ou observationnelles spécifiques à la schizophrénie résistante au traitement.
- Évaluer le rapport bénéfice/risque par rapport aux traitements actuels de cette indication (dont la clozapine), compte tenu de l'absence d'AMM valide.
- Vérifier la compatibilité des voies d'administration et la similarité avec l'indication d'origine, actuellement non évaluées.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

