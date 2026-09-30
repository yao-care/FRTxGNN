---
layout: default
title: Flavoxate
parent: Prédiction du modèle uniquement (L5)
nav_order: 130
evidence_level: L5
indication_count: 8
---

# Flavoxate
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

# Flavoxate : D'un Antispasmodique Urinaire au Trouble du Déficit de l'Attention avec Hyperactivité (type inattentif)

## Résumé en Une Phrase

Le flavoxate est un relaxant des muscles lisses (effets antimuscarinique, inhibiteur des phosphodiestérases et modulateur du calcium), commercialisé en France sous le nom Urispas. Le texte d'indication ANSM n'est pas renseigné dans les données reçues.
Le modèle TxGNN prédit en premier rang qu'il pourrait être efficace pour le **trouble du déficit de l'attention avec hyperactivité, type inattentif**, avec un score élevé (99,75 %).
**Aucun essai clinique et aucune publication** ne soutiennent cette prédiction, et l'analyse mécanistique la juge peu plausible.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM (texte d'indication vide) |
| Nouvelle Indication Prédite | Trouble du déficit de l'attention avec hyperactivité, type inattentif |
| Score de Prédiction TxGNN | 99,75 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le pack. D'après les informations pharmacologiques connues, le flavoxate est un relaxant des muscles lisses aux propriétés antimuscariniques, inhibitrices des phosphodiestérases et modulatrices du calcium.

**Pour le TDAH, aucun lien mécanistique plausible n'est identifié.** Le flavoxate n'a pas d'activité connue sur les voies dopaminergiques ou noradrénergiques, qui sont au cœur de ce trouble. Le score élevé est très probablement un artefact du graphe de connaissances. Le même constat vaut pour le « trouble du déficit de l'attention avec hyperactivité » (rang 4, doublon) et pour le « trouble spécifique du développement » (rang 3, proximité dans le graphe avec les prédictions TDAH).

Les autres prédictions sont plus cohérentes sur le plan biologique, mais restent des inférences sans preuve :

| Rang | Indication prédite | Score TxGNN | Lien mécanistique | Recommandation |
|------|------|------|------|------|
| 2 | Syndrome de l'intestin irritable | 99,74 % | Plausible (effet antispasmodique de classe) | Hold |
| 3 | Trouble spécifique du développement | 99,56 % | Aucun | Hold |
| 4 | TDAH | 99,39 % | Aucun (doublon du rang 1) | Hold |
| 5 | Syndrome de la queue de cheval | 99,27 % | Indirect : soulagement possible de symptômes vésicaux, sans traitement de la cause. Risque en cas de rétention urinaire | Hold |
| 6 | Vessie neurogène (terme obsolète) | 99,13 % | Le plus cohérent : relaxation du détrusor. Nécessite un remappage vers un concept actuel (hyperactivité neurogène du détrusor) | Question de recherche |
| 7 | Gastroduodénite | 99,12 % | Faible | Hold |
| 8 | Ulcère gastroduodénal | 99,10 % | Faible, les traitements actuels (IPP, éradication d'*H. pylori*) rendent l'intérêt improbable | Hold |

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63383409 | URISPAS 200 mg, comprimé pelliculé (BOUCHARA-RECORDATI) | Comprimé pelliculé | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été trouvée dans les données consultées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction principale (TDAH) repose uniquement sur le modèle (niveau L5, stade S0), sans essai ni publication, et sans lien mécanistique plausible : il s'agit probablement d'un artefact du graphe.
- Parmi les prédictions, seules la vessie neurogène (rang 6) et, plus faiblement, le syndrome de l'intestin irritable (rang 2) ont une cohérence pharmacologique. Elles restent à l'état d'hypothèses.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications, indication autorisée), ce qui bloque actuellement le criblage de sécurité S1.
- Compléter les données de mécanisme d'action via DrugBank.
- Remapper le terme obsolète « vessie neurogène » vers un concept actuel, puis lancer une recherche systématique d'essais et de littérature pour cette indication et pour le syndrome de l'intestin irritable.
- Écarter ou déprioriser les prédictions TDAH et trouble du développement, sauf si de nouvelles données les soutiennent.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

