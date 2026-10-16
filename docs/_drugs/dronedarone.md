---
layout: default
title: Dronedarone
parent: Preuves modérées (L3-L4)
nav_order: 261
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Dronedarone : nouvelle indication prédite, Accident vasculaire cérébral (« stroke disorder ») (niveau de preuve L4). Indication d'origine : Fibrillation atriale"
monitor_inn: "dronedarone"
predicted_indications: ["stroke disorder", "obsolete susceptibility to ischemic stroke", "ABri amyloidosis", "cerebrovascular disorder", "brain stem infarction", "sick sinus syndrome 2, autosomal dominant", "duodenal obstruction", "cerebral artery occlusion", "sarcoglycanopathy", "Wildervanck syndrome"]
---

# Dronedarone
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **10** 
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

# Dronédarone : De la Fibrillation Atriale à l'Accident Vasculaire Cérébral

## Résumé en Une Phrase

La dronédarone est un antiarythmique initialement utilisé pour le traitement de la fibrillation atriale.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**accident vasculaire cérébral (AVC)**,
mais **aucun essai clinique** n'est enregistré et les **20 publications** retrouvées sont surtout des revues sur la fibrillation atriale, dont seules quelques analyses post hoc évoquent une réduction du risque d'AVC.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Fibrillation atriale (d'après le graphe de connaissances ; le texte de l'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Accident vasculaire cérébral (« stroke disorder ») |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | AMM annulée uniquement |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, la dronédarone est un antiarythmique multicanal (blocage des courants Na⁺, K⁺ et Ca²⁺), structurellement proche de l'amiodarone mais non iodé. Son efficacité dans la fibrillation atriale est établie.

Le lien avec l'AVC est surtout indirect. La fibrillation atriale est une cause majeure d'AVC cardio-embolique, et le maintien du rythme sinusal pourrait en théorie réduire ce risque. Une analyse post hoc de l'essai ATHENA a suggéré une baisse de l'incidence des AVC sous dronédarone. Des données précliniques évoquent aussi des effets protecteurs contre les lésions d'ischémie-reperfusion cardiaques et cérébrales, ainsi que des effets anticoagulants et antiplaquettaires indépendants de l'action antiarythmique.

Ces éléments restent toutefois limités : l'AVC y est un critère secondaire ou post hoc, chez des patients atteints de fibrillation atriale. Dans l'essai PALLAS (fibrillation atriale permanente à haut risque), la dronédarone a été associée à une augmentation des événements vasculaires majeurs, dont les AVC. Le score TxGNN très élevé est une prédiction issue d'un graphe, et non une preuve clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Les publications les plus pertinentes pour l'AVC (parmi celles retrouvées pour les indications « AVC » et « trouble cérébrovasculaire ») :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [22149318](https://pubmed.ncbi.nlm.nih.gov/22149318/) | 2011 | Méta-analyse (post hoc ATHENA) | Am J Cardiovasc Drugs | Réduction possible du risque d'AVC sous dronédarone en cas de fibrillation atriale paroxystique ou persistante |
| [25820938](https://pubmed.ncbi.nlm.nih.gov/25820938/) | 2015 | Revue systématique | Cochrane Database Syst Rev | Antiarythmiques pour le maintien du rythme sinusal après cardioversion ; effet sur la mortalité et les autres critères peu clair |
| [22082198](https://pubmed.ncbi.nlm.nih.gov/22082198/) | 2011 | Essai randomisé (PALLAS) | N Engl J Med | Dronédarone dans la fibrillation atriale permanente à haut risque ; critère de prévention des événements vasculaires majeurs |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | Étude expérimentale | Atherosclerosis | Effets anticoagulants et antiplaquettaires indépendants de l'action antiarythmique |
| [22366819](https://pubmed.ncbi.nlm.nih.gov/22366819/) | 2012 | Préclinique | Cardiovasc Drugs Ther | Effets pléiotropes sur les lésions d'ischémie-reperfusion du cœur et du cerveau |
| [20396635](https://pubmed.ncbi.nlm.nih.gov/20396635/) | 2010 | Revue | Clin Interv Aging | Impact de la dronédarone sur la réduction des AVC dans la fibrillation atriale et le flutter |
| [41152878](https://pubmed.ncbi.nlm.nih.gov/41152878/) | 2025 | Cohorte | BMC Med | Association anticoagulants oraux directs et antiarythmiques interagissant, et risque d'AVC et d'hémorragie |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Cohorte | Circ Arrhythm Electrophysiol | Dronédarone versus sotalol chez des vétérans atteints de fibrillation atriale |
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | Analyse secondaire d'ECR | Clin Res Cardiol | Sécurité et efficacité de l'amiodarone et de la dronédarone pour le contrôle précoce du rythme (EAST-AFNET 4) |
| [22166900](https://pubmed.ncbi.nlm.nih.gov/22166900/) | 2012 | Revue | Lancet | Prise en charge de la fibrillation atriale et stratification du risque d'AVC |

Aucune de ces publications n'est un essai dédié à la prévention de l'AVC par la dronédarone.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69213011 | MULTAQ 400 mg, comprimé pelliculé (statut : annulée) | Comprimé pelliculé | Non renseignée |

## Cytotoxicité

Section non applicable : la dronédarone n'est pas un médicament antinéoplasique.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (à confirmer avec la notice) : syndrome du QT long (y compris familial), torsades de pointes, insuffisance hépatique, carence en potassium, bloc auriculo-ventriculaire, maladie du sinus (y compris forme familiale).
- **Interactions médicamenteuses** : 253 interactions recensées. Parmi les interactions de niveau majeur figurent l'hydrocortisone, l'amphotéricine B (et ses formulations lipidiques, liposomales et au sulfate de cholestéryle), le lopéramide, la clarithromycine, l'acide picosulfurique, le polyéthylène glycol (3350 avec électrolytes) et la dolasétron. Parmi les interactions de niveau modéré : famotidine, alvimopan, aprépitant, dexaméthasone, bisacodyl, budésonide, cimétidine, saxagliptine et huile de ricin.
- **Points d'attention issus de la littérature** : risque accru d'AVC et d'événements cardiovasculaires dans la fibrillation atriale permanente (PALLAS), précautions en cas d'insuffisance cardiaque décompensée ou récente, et interaction avec les anticoagulants oraux directs.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
L'association avec l'AVC repose essentiellement sur une prédiction de graphe et sur des analyses post hoc chez des patients atteints de fibrillation atriale, sans essai dédié. Le profil de sécurité (insuffisance cardiaque, fibrillation atriale permanente, interactions) et l'AMM française annulée limitent encore la portée de ces signaux. À ce stade, il s'agit d'une question de recherche et non d'une recommandation de repositionnement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications), ce qui bloque l'étape de criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Évaluer, dans des cohortes de fibrillation atriale paroxystique ou persistante, l'effet de la dronédarone sur l'AVC comme critère principal
- Définir les populations exclues (fibrillation atriale permanente, insuffisance cardiaque) et un plan de gestion des interactions, notamment avec les anticoagulants oraux directs
- Clarifier la situation réglementaire en France, l'AMM étant annulée

Les autres indications prédites (par exemple les amyloses, la sarcoglycanopathie, le syndrome de Wildervanck, l'obstruction duodénale) n'ont ni essai ni publication ni lien mécanistique plausible : elles restent en Hold. Le syndrome du sinus malade de type 2 soulève de plus un risque d'aggravation de la bradycardie.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

