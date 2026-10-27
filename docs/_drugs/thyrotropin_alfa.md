---
layout: default
title: Thyrotropin Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 757
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Thyrotropin Alfa : nouvelle indication prédite, Migraine (migraine disorder) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM disponibles"
monitor_inn: "thyrotropin alfa"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "Raynaud disease", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "ulerythema ophryogenesis", "pulmonary hypertension", "kyphoscoliotic heart disease", "postural orthostatic tachycardia syndrome", "hyperthyroidism"]
---

# Thyrotropin Alfa
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

## Thyrotropine alfa : Du Diagnostic du Cancer Thyroïdien à la Migraine (prédiction non étayée)
{: .text-alpha }

## Résumé en Une Phrase

La thyrotropine alfa (THYROGEN) est une forme recombinante de la TSH (hormone thyréotrope). Les données compilées pour ce rapport ne précisent pas son indication d'origine dans l'AMM française.
Le modèle TxGNN la prédit comme potentiellement efficace pour la **migraine** (score de 99,98 %), mais **aucun essai clinique ni aucune publication** ne soutient cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM disponibles |
| Nouvelle Indication Prédite | Migraine (*migraine disorder*) |
| Score de Prédiction TxGNN | 99,98 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la thyrotropine alfa est une TSH recombinante qui agit sur le récepteur de la TSH (TSHR) du tissu thyroïdien. Elle est utilisée comme agent de stimulation en contexte de diagnostic et de suivi thyroïdien.

**En l'état, la prédiction n'est pas plausible sur le plan biologique.** Aucun lien mécanistique établi n'existe entre la stimulation du récepteur de la TSH et la migraine. Le score élevé reflète vraisemblablement une proximité dans le graphe de connaissances (voisins communs via des nœuds thyroïdiens, vasculaires ou neuroendocriniens) plutôt qu'une preuve biologique. L'indication d'origine et le mécanisme n'étant pas documentés, la prédiction ne peut pas être vérifiée mécanistiquement.

Les autres prédictions du modèle présentent le même problème :
- **Sous-types de migraine** (migraine avec aura du tronc cérébral, susceptibilité génétique à la migraine) : prédictions corrélées à l'entrée principale, sans valeur de preuve indépendante.
- **Maladie de Raynaud, hypertension pulmonaire, cardiopathie cyphoscoliotique** : pas de lien direct. Les associations avec les maladies thyroïdiennes sont épidémiologiques et n'impliquent pas d'effet thérapeutique.
- **Atrophodermie vermiculée, ulérythème ophryogène** : aucun mécanisme identifiable, probable artefact du graphe.
- **Syndrome de tachycardie orthostatique posturale** : la stimulation thyroïdienne pourrait aggraver la tachycardie.
- **Hyperthyroïdie** : biologiquement contradictoire, car la thyrotropine alfa augmente la production d'hormones thyroïdiennes et pourrait aggraver la maladie.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68937442 (annulée) | THYROGEN 0,9 mg, poudre pour solution injectable | Poudre pour solution injectable | Non renseignée |

Titulaire : SANOFI WINTHROP INDUSTRIE.

## Considérations de Sécurité

**Interactions médicamenteuses** : 45 interactions ont été identifiées, toutes de niveau modéré dans les données compilées. Les 20 premières concernent les médicaments antidiabétiques :
- **Biguanides** : metformine
- **Sulfamides hypoglycémiants** : chlorpropamide, acétohexamide, glimépiride, glipizide, glibenclamide
- **Inhibiteurs de l'α-glucosidase** : acarbose
- **Inhibiteurs de la DPP-4** : alogliptine, saxagliptine
- **Inhibiteurs du SGLT2** : canagliflozine, dapagliflozine, empagliflozine, ertugliflozine
- **Agonistes du GLP-1** : albiglutide, dulaglutide, sémaglutide, exénatide
- **Insulines** : insuline humaine, insuline asparte (et asparte protamine)

Les 25 autres interactions ne figurent pas dans les données détaillées disponibles.

**Point d'attention propre aux prédictions** : la stimulation thyroïdienne par la TSH pourrait être préjudiciable en cas d'hyperthyroïdie, de tachycardie ou de pathologie cardiopulmonaire.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Toutes les prédictions reposent uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et sans lien mécanistique plausible. Certaines (hyperthyroïdie, tachycardie orthostatique, hypertension pulmonaire) soulèvent des inquiétudes de sécurité. De plus, la seule AMM française est annulée et les données de sécurité de la notice manquent, ce qui bloque le criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications, indication approuvée)
- Obtenir les données sur le mécanisme d'action depuis DrugBank
- Établir une hypothèse biologique crédible reliant la signalisation TSH/TSHR à la migraine, avant toute étude
- Réaliser une revue de la littérature et des registres d'essais cliniques ciblée
- Évaluer la compatibilité de la voie d'administration (injectable) avec toute indication envisagée
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

