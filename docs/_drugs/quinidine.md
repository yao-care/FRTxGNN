---
layout: default
title: Quinidine
parent: Prédiction du modèle uniquement (L5)
nav_order: 644
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Quinidine : nouvelle indication prédite, Syndrome néphrogénique d'antidiurèse inappropriée (niveau de preuve L5). Indication d'origine : Fibrillation auriculaire"
monitor_inn: "quinidine"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Quinidine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Quinidine : De la fibrillation auriculaire et du paludisme au syndrome néphrogénique d'antidiurèse inappropriée

## Résumé en Une Phrase

La quinidine est un antiarythmique de classe Ia, initialement utilisé pour la fibrillation auriculaire et le paludisme.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome néphrogénique d'antidiurèse inappropriée (SNAI)**,
mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Fibrillation auriculaire ; paludisme (selon le graphe de connaissances TxGNN, le texte d'indication de l'AMM n'étant pas renseigné) |
| Nouvelle Indication Prédite | Syndrome néphrogénique d'antidiurèse inappropriée |
| Score de Prédiction TxGNN | 99,27 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les connaissances générales, la quinidine est un antiarythmique de classe Ia qui bloque les canaux sodiques et potassiques, avec une activité anticholinergique et alpha-adrénergique bloquante. Son efficacité dans la fibrillation auriculaire et le paludisme est connue.

Le SNAI est causé par des mutations gain de fonction du récepteur V2 de la vasopressine (AVPR2), entraînant une rétention d'eau et une hyponatrémie indépendamment de la vasopressine. Aucune voie établie ne relie les actions pharmacologiques de la quinidine à la signalisation d'AVPR2 ou à la gestion rénale de l'eau. Le lien mécanistique reste donc purement spéculatif.

Le score élevé (0,993) provient uniquement du graphe de connaissances. Il doit être considéré comme un signal générateur d'hypothèses et non comme une preuve d'efficacité.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66182379 | QUINIMAX 500 mg/4 ml, solution injectable (SANOFI WINTHROP INDUSTRIE), statut : annulée | Solution injectable | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie du graphe, et non texte de la notice) : syndrome du QT long (y compris familial), torsades de pointes, insuffisance rénale, maladie hépatique, maladie de la vésicule biliaire, thrombocytopénie, carence en potassium, psoriasis et parapsoriasis, hypotension, myasthénie grave (y compris de l'adulte) et maladies de la jonction neuromusculaire, bloc auriculo-ventriculaire, bloc de branche gauche, bloc cardiaque familial progressif, insuffisance cardiaque, intoxication digitalique, emphysème pulmonaire, dyskinésie de l'œsophage, pyourètre.
- **Interactions médicamenteuses** : 345 interactions recensées. Parmi celles affichées, les interactions **majeures** concernent : clarithromycine, lopéramide, dolasétron, palonosétron, éliglustat, acide picosulfurique et polyéthylène glycol (3350 avec électrolytes). Des interactions **modérées** concernent notamment : famotidine, ranitidine, cimétidine, metformine, aprépitant, acide acétylsalicylique, bisacodyl, glycopyrronium, chlorpropamide, citrate de potassium, éluxadoline, glimépiride et trospium.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être consultées : veuillez vous référer à la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et sans lien mécanistique plausible avec la physiopathologie du SNAI. De plus, la seule AMM française est annulée et le profil de sécurité (risque de QT long, nombreuses interactions majeures) est préoccupant.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (par ex. via DrugBank)
- Mises en garde et contre-indications officielles issues de la notice de l'ANSM (bloquant pour le criblage de sécurité)
- Études précliniques ou de mécanisme évaluant un effet sur le récepteur V2 ou la gestion rénale de l'eau
- Revue de la littérature pour identifier d'éventuels rapports de cas ou données in vitro
- Évaluation de la compatibilité des voies d'administration et de la similarité avec les indications d'origine
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

