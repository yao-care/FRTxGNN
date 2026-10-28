---
layout: default
title: Rasagiline
parent: Prédiction du modèle uniquement (L5)
nav_order: 653
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
monitor_inn: "rasagiline"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "paralysis agitans, juvenile, of Hunt", "transaldolase deficiency", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis"]
description: "Rasagiline : nouvelle indication prédite, Neurodégénérescence associée à PLA2G6 (PLA2G6-associated neurodegeneration) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données loc…"
---

# Rasagiline
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Rasagiline: Neurodégénérescence associée à PLA2G6 (PLA2G6-associated neurodegeneration)
{: .text-alpha }

## Résumé en Une Phrase

La rasagiline est un inhibiteur irréversible de la monoamine oxydase de type B (MAO-B), initialement utilisé dans le traitement de la **maladie de Parkinson** et des syndromes parkinsoniens apparentés.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **neurodégénérescence associée à PLA2G6**.
Aucun essai clinique ni aucune publication ne soutient actuellement cette prédiction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Neurodégénérescence associée à PLA2G6 (PLA2G6-associated neurodegeneration) |
| Score de Prédiction TxGNN | 0.9971 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 14 sur 14) |
| Nombre d'AMM | 14 (valides : 14) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, la rasagiline est un inhibiteur irréversible de la MAO-B : elle augmente la disponibilité de la dopamine dans le striatum et pourrait exercer des effets neuroprotecteurs ou anti-apoptotiques. Son efficacité dans la maladie de Parkinson est établie.

La neurodégénérescence associée à PLA2G6 (dont la dystrophie neuroaxonale infantile et la dystonie-parkinsonisme liée à PLA2G6) partage des traits parkinsoniens avec les indications d'origine. Un bénéfice symptomatique sur le syndrome parkinsonien est donc plausible.

Cependant, cette maladie résulte surtout de défauts du métabolisme lipidique et du remodelage membranaire, d'une accumulation de fer et d'une pathologie de l'alpha-synucléine. L'inhibition de la MAO-B n'agit pas sur ces mécanismes : un effet modificateur de la maladie reste spéculatif. Le score élevé (0,9971) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, pas une preuve biologique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 14 AMM recensées sont toutes annulées. Les 5 premières sont listées ci-dessous (le texte d'indication approuvée n'est pas renseigné).

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 65462218 | RASAGILINE BIOGARAN 1 mg | Comprimé | Active |
| 64201902 | RASAGILINE EG 1 mg | Comprimé | Active |
| 63729327 | RASAGILINE SANDOZ 1 mg | Comprimé | Active |
| 68885764 | RASAGILINE CRISTERS 1 mg | Comprimé | Active |
| 62725468 | RASAGILINE ZYDUS 1 mg | Comprimé | Active |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : hypertension, atrophie multisystématisée, syndrome de tachycardie orthostatique posturale, hypotension orthostatique, dyskinésie d'origine médicamenteuse, épilepsie, trouble bipolaire, trouble affectif majeur, maladie hépatique, maladie de la vésicule biliaire, mélanome, phéochromocytome, cancers du duodénum, de l'intestin grêle, du cœur et de la surrénale, paragangliome sympathique.
- **Interactions médicamenteuses** : 137 interactions recensées. Parmi les principales :
  - **Majeures** : bupropion, morphine.
  - **Modérées** : épinéphrine, chlorpropamide, cimétidine, diéthylpropion, difénoxine, diphénoxylate, dronabinol, acide obéticholique, phentermine, glimépiride et plusieurs insulines (asparte, dégludec, détémir, glargine, glulisine, humaine).

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Le mécanisme de la MAO-B ne cible pas les causes de la maladie. Le médicament est commercialisé en France (14 AMM valides sur 14).
- Les données de sécurité officielles manquent, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle de l'ANSM (mises en garde et contre-indications).
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Rechercher des études précliniques ou des séries de cas sur la rasagiline dans la neurodégénérescence associée à PLA2G6.
- Évaluer l'indication voisine du parkinsonisme juvénile de Hunt, dont le lien mécanistique est le plus fort (niveau L4, « question de recherche »), avec des données pédiatriques et de sécurité spécifiques.
- Clarifier la disponibilité réelle du produit en France, compte tenu des AMM annulées.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

