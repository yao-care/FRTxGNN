---
layout: default
title: Pentamidine
parent: Prédiction du modèle uniquement (L5)
nav_order: 587
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "PENTAMIDINE"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "neurotrophic keratopathy", "exposure keratitis", "non-human animal disease", "congenital analbuminemia"]
description: "Pentamidine : nouvelle indication prédite, Kératoconjonctivite ponctuée épithéliale (punctate epithelial keratoconjunctivitis) (niveau de preuve L5). Indication d'origine : Non renseignée dans les do…"
---

# Pentamidine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

## Pentamidine: Kératoconjonctivite ponctuée épithéliale (punctate epithelial keratoconjunctivitis)
{: .text-alpha }

## Résumé en Une Phrase

Pentamidine est un antimicrobien (antiprotozoaire et antifongique) initialement utilisé pour traiter la pneumocystose et la trypanosomiase humaine africaine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **kératoconjonctivite ponctuée épithéliale**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Kératoconjonctivite ponctuée épithéliale (punctate epithelial keratoconjunctivitis) |
| Score de Prédiction TxGNN | 0.9973 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la pentamidine est un agent antimicrobien dont l'efficacité a été établie dans la pneumocystose et les trypanosomiases. Sur le plan mécanistique, elle pourrait être applicable à une kératoconjonctivite d'origine infectieuse (par exemple adénovirale ou microsporidienne).

Ce lien reste toutefois spéculatif. Aucune donnée compilée pour ce rapport ne le démontre, et le score élevé du modèle (0,9973) provient du modèle TxGNN (apprentissage profond) : il peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique. La voie d'administration oculaire et la tolérance locale de la pentamidine ne sont pas établies, et la compatibilité des voies d'administration reste à évaluer (la seule forme connue est une poudre pour aérosol et usage parentéral).

Les autres prédictions du modèle sont encore moins soutenues : kératopathie neurotrophique (0,9967), kératite d'exposition (0,9936), « maladie animale non humaine » (0,9913, catégorie non spécifique, sans portée clinique) et analbuminémie congénitale (0,9909, sans mécanisme plausible). Ces scores proviennent du modèle TxGNN (apprentissage profond) et peuvent refléter des similarités apprises entre maladies apparentées, et non une preuve biologique ; ils ne justifient pas d'évaluation à ce stade.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61423246 | PENTACARINAT 300 mg, poudre pour aérosol et pour usage parentéral (statut : active) | Poudre pour aérosol et pour usage parentéral | Non renseignée |

## Considérations de Sécurité

- **Maladies associées à des contre-indications selon le graphe de connaissances** (et non selon la notice) : hypertension, hypotension, torsades de pointes, arrêt cardiaque soudain, trouble de la conduction cardiaque, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, pancréatite, thrombopénie, leucopénie, anémie (dont macrocytaire), hyperglycémie, hypoglycémie, diabète, acidocétose diabétique, asthme (dont intrinsèque et allergique), hypercalcémie, néphrocalcinose, troubles du métabolisme du phosphore et pyourétère.
- **Interactions médicamenteuses** : 100 interactions recensées, dont les exemples suivants de niveau modéré :
  - antidiabétiques : acarbose, metformine, pioglitazone, alogliptine, albiglutide, canagliflozine, dapagliflozine, chlorpropamide ;
  - amphotéricine B (y compris complexe lipidique) ;
  - clarithromycine ;
  - inhibiteurs de la pompe à protons et anti-H2 : oméprazole, rabéprazole, famotidine ;
  - laxatifs et gastro-intestinaux : bisacodyl, acide picosulfurique, polyéthylène glycol, lopéramide, mésalazine, balsalazide.

Les mises en garde et contre-indications issues de la notice n'ont pas pu être consultées. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Le mécanisme d'action est inconnu, la seule AMM française est annulée, et le profil de risque (cardiaque, rénal, glycémique, hématologique) est préoccupant.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice auprès de l'ANSM (lacune bloquante pour le criblage de sécurité).
- Obtenir les données sur le mécanisme d'action depuis DrugBank.
- Mener une revue de la littérature et des registres d'essais sur la pentamidine dans les kératites et kératoconjonctivites infectieuses.
- Évaluer la faisabilité d'une formulation et d'une voie d'administration oculaires, ainsi que la tolérance locale.
- Réévaluer les indications prédites secondaires, qui paraissent peu plausibles.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

