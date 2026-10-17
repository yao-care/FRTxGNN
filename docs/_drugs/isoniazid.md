---
layout: default
title: Isoniazid
parent: Prédiction du modèle uniquement (L5)
nav_order: 416
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Isoniazid : nouvelle indication prédite, Conjonctivite (niveau de preuve L5). Indication d'origine : Tuberculose pulmonaire"
monitor_inn: "isoniazid"
predicted_indications: ["conjunctivitis"]
---

# Isoniazid
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

# Isoniazide : De la tuberculose pulmonaire à la conjonctivite

## Résumé en Une Phrase

L'isoniazide est un antituberculeux de référence, utilisé à l'origine pour le traitement de la tuberculose pulmonaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **conjonctivite**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : la prédiction repose uniquement sur le score du modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Tuberculose pulmonaire (selon le graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Conjonctivite |
| Score de Prédiction TxGNN | 99,36 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées (aucune AMM valide) |
| Nombre d'AMM | 5 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances pharmacologiques générales, l'isoniazide est une prodrogue activée par l'enzyme KatG des mycobactéries ; elle inhibe ensuite InhA et donc la synthèse des acides mycoliques de la paroi bactérienne. Cette action est spécifique des mycobactéries.

Ce mécanisme n'a pas de lien établi avec les causes usuelles de la conjonctivite (virales, bactériennes, allergiques). Un lien avec la tuberculose est concevable, par exemple la kératoconjonctivite phlycténulaire, une réaction d'hypersensibilité aux antigènes mycobactériens, mais il reste spéculatif et n'est étayé par aucune donnée disponible.

La prédiction repose donc uniquement sur le score élevé de TxGNN (99,36 %), dont le raisonnement n'est pas interprétable ici. Il n'existe à ce stade aucun mécanisme plausible et documenté pour un repositionnement, par voie topique ou systémique, de l'isoniazide dans la conjonctivite.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les cinq AMM recensées sont annulées. Le texte d'indication approuvée n'est pas renseigné dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 63644987 | RIMIFON 50 mg, comprimé | Comprimé | Annulée |
| 69515643 | RIMIFON 500 mg/5 ml | Solution injectable ou pour perfusion | Annulée |
| 69568222 | RIMIFON 150 mg, comprimé | Comprimé | Annulée |
| 63898512 | RIFINAH 300 mg/150 mg | Comprimé enrobé | Annulée |
| 64208131 | RIFATER | Comprimé enrobé | Annulée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : insuffisance hépatique (y compris aiguë), hépatite et maladies du foie, porphyries (y compris héréditaire et troubles du métabolisme des porphyrines), maladies de la vésicule biliaire, diabète et acidocétose diabétique, goutte, neuropathie périphérique et maladies du système nerveux périphérique, abus ou dépendance à des substances, et statut d'acétylateur lent.
- **Interactions médicamenteuses** : 242 interactions recensées. Parmi les principales, de niveau modéré : antidiabétiques (acarbose, metformine, pioglitazone, alogliptine, canagliflozine, dapagliflozine, chlorpropamide, albiglutide), métronidazole, budésonide, vitamine D et dérivés (cholécalciférol, calcifédiol, calcitriol), alosétron et acide picosulfurique. De niveau mineur : corticoïdes (hydrocortisone, triamcinolone, dexaméthasone, bétaméthasone).

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être intégrées. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication et sans mécanisme plausible. De plus, toutes les AMM françaises sont annulées et les données de sécurité officielles manquent, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser les mises en garde et contre-indications de la notice officielle (site de l'ANSM), car il s'agit d'un point bloquant.
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank).
- Mener une revue de la littérature pour rechercher un lien entre l'isoniazide et les atteintes oculaires (par exemple la kératoconjonctivite phlycténulaire).
- Évaluer la compatibilité des voies d'administration (une voie topique oculaire n'existe pas dans les formes recensées).
- Examiner le profil de sécurité, notamment hépatique et neurologique, au regard d'une éventuelle nouvelle population cible.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

