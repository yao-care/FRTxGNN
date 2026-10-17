---
layout: default
title: Fluconazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 331
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Fluconazole : nouvelle indication prédite, Kératoconjonctivite épithéliale ponctuée (niveau de preuve L5). Indication d'origine : Candidoses (candidose buccale, vulvovaginale, œsophagienne…"
monitor_inn: "FLUCONAZOLE"
predicted_indications: ["punctate epithelial keratoconjunctivitis"]
---

# Fluconazole
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

# Fluconazole : Des Candidoses à la Kératoconjonctivite Épithéliale Ponctuée

## Résumé en Une Phrase

Le fluconazole est un antifongique azolé, initialement utilisé pour traiter les candidoses (buccale, vulvovaginale, œsophagienne, candidémie, candidose disséminée) et la méningite à cryptocoque.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **kératoconjonctivite épithéliale ponctuée**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Candidoses (candidose buccale, vulvovaginale, œsophagienne, candidémie, candidose disséminée) et méningite à cryptocoque (d'après le graphe de connaissances ; le texte des AMM ne précise pas d'indication) |
| Nouvelle Indication Prédite | Kératoconjonctivite épithéliale ponctuée |
| Score de Prédiction TxGNN | 99,24 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 20 (dont 0 valide, 20 annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, le fluconazole est un antifongique azolé qui inhibe la lanostérol 14-alpha-déméthylase fongique (CYP51), ce qui perturbe la synthèse de l'ergostérol, composant essentiel de la membrane des champignons. Son efficacité dans les infections à *Candida* et à *Cryptococcus* est établie.

Le seul soutien à la prédiction est le score élevé du modèle (0,992). Un lien plausible, mais non vérifié, serait que le modèle associe les kératoconjonctivites d'origine fongique ou infectieuse à l'activité antifongique. Or la kératoconjonctivite épithéliale ponctuée est souvent d'origine virale (par exemple adénovirus) ou liée à une atteinte de la surface oculaire ; dans ces situations, un antifongique n'agirait pas sur la cause.

La prédiction ne peut donc pas être considérée comme soutenue sur le plan mécanistique sans preuves supplémentaires. La similarité avec l'indication d'origine reste à évaluer, et la compatibilité des voies d'administration (les formes disponibles sont orales et perfusion, aucune forme ophtalmique) n'a pas été établie.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les 20 AMM recensées sont toutes annulées. Les 5 premières sont listées ci-dessous (le texte d'indication n'est pas renseigné dans les données).

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 60560861 | FLUCONAZOLE EVOLUGEN 50 mg | Gélule | Annulée |
| 62033904 | FLUCONAZOLE SANDOZ 200 mg | Gélule | Annulée |
| 63909389 | FLUCONAZOLE VIATRIS 50 mg | Gélule | Annulée |
| 63206323 | FLUCONAZOLE PFIZER 150 mg | Gélule | Annulée |
| 64080646 | TRIFLUCAN 50 mg | Gélule | Annulée |

Les autres formes concernées par des AMM annulées : poudre pour suspension buvable et solution pour perfusion.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : syndrome du QT long (y compris familial), maladie rénale, pyo-uretère, maladie hépatique, maladie de la vésicule biliaire.
- **Interactions médicamenteuses** (100 interactions recensées ; principales) :
  - **Majeure** : chlorpropamide.
  - **Modérée** : famotidine, rabéprazole, oméprazole, dexlansoprazole, hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, budésonide, lopéramide, aprépitant, bisacodyl, acide picosulfurique, polyéthylène glycol (3350 avec électrolytes), saxagliptine.
  - **Mineure** : amphotéricine B (y compris complexe lipidique), clarithromycine.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication, et le lien mécanistique est peu plausible pour une kératoconjonctivite souvent virale. Aucune AMM n'est actuellement valide en France, et les données de sécurité de la notice manquent.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice (ANSM) pour permettre l'évaluation de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Rechercher des études cliniques ou précliniques du fluconazole dans la kératoconjonctivite épithéliale ponctuée et préciser l'étiologie ciblée (fongique ou autre).
- Évaluer la voie d'administration adaptée (aucune forme ophtalmique disponible) et la compatibilité avec la pathologie.
- Clarifier le statut réglementaire, toutes les AMM étant annulées.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

