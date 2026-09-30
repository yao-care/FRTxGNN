---
layout: default
title: Fluvoxamine
parent: Preuves modérées (L3-L4)
nav_order: 136
evidence_level: L4
indication_count: 10
---

# Fluvoxamine
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

# Fluvoxamine : D'un ISRS (indication d'origine non renseignée) au Trouble de la Personnalité Schizotypique

## Résumé en Une Phrase

La fluvoxamine est un inhibiteur sélectif de la recapture de la sérotonine (ISRS) qui agit aussi comme agoniste du récepteur sigma-1. Elle est commercialisée en France sous le nom Floxyfral 50 mg.
Le modèle TxGNN prédit qu'elle pourrait être efficace dans le **trouble de la personnalité schizotypique**, avec un score très élevé (99,997 %).
Cette prédiction repose toutefois sur **aucun essai clinique** et **6 publications indirectes**, qui portent surtout sur le trouble obsessionnel compulsif (TOC) associé. Aucune n'a testé la fluvoxamine directement dans cette pathologie.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données AMM disponibles |
| Nouvelle Indication Prédite | Trouble de la personnalité schizotypique |
| Score de Prédiction TxGNN | 99,997 % (rang 117) |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les connaissances de base, la fluvoxamine est un ISRS et un agoniste du récepteur sigma-1. Ce mécanisme est bien établi dans les troubles anxieux, le TOC et la dépression.

Le lien avec le trouble de la personnalité schizotypique est **indirect**. Les publications retrouvées décrivent des patients atteints de TOC résistant à la fluvoxamine, chez qui l'ajout d'un neuroleptique a donné une réponse. Cette réponse était associée à la présence de tics ou d'un trouble schizotypique comorbide. Elles suggèrent une implication de la dopamine et de la sérotonine dans ces formes de TOC. Elles ne montrent pas que la fluvoxamine traite le trouble schizotypique lui-même.

Le score très élevé du modèle n'est donc pas soutenu par des données cliniques. Il reflète probablement la proximité de cette pathologie avec le TOC et les troubles anxieux dans le graphe de connaissances.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [11063782](https://pubmed.ncbi.nlm.nih.gov/11063782/) | 2000 | Essai ouvert | Psychiatry Research | Ajout d'olanzapine chez 23 patients avec TOC résistant à la fluvoxamine. L'étude cherchait si un tic chronique ou un trouble schizotypique associé influençait la réponse. |
| [20414175](https://pubmed.ncbi.nlm.nih.gov/20414175/) | 2010 | Cohorte | CNS Spectrums | Caractéristiques cliniques et traitement de l'accumulation compulsive chez des patients japonais avec TOC. |
| [1970224](https://pubmed.ncbi.nlm.nih.gov/1970224/) | 1990 | Série de cas | Am J Psychiatry | Chez 9 patients sur 17 avec TOC résistant à la fluvoxamine, l'ajout d'un neuroleptique a été suivi d'une réponse. La réponse était associée à des tics ou à un trouble schizotypique. |
| [14999178](https://pubmed.ncbi.nlm.nih.gov/14999178/) | 2004 | Cas clinique | CNS Spectrums | Accumulation compulsive avec TDAH et trouble schizotypique, traitée par fluvoxamine, sels d'amphétamine, rispéridone et thérapie comportementale. |
| [16146185](https://pubmed.ncbi.nlm.nih.gov/16146185/) | 2005 | Cas clinique | Seishin Shinkeigaku Zasshi | TOC avec syndrome déficitaire induit par les neuroleptiques, chez un patient à personnalité schizotypique. Amélioration après arrêt des neuroleptiques puis introduction de la fluvoxamine. |
| [8473723](https://pubmed.ncbi.nlm.nih.gov/8473723/) | 1993 | Cas clinique | Int Clin Psychopharmacol | Convulsions lors de l'association lévomépromazine-fluvoxamine. Signal de sécurité, sans lien avec l'efficacité. |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 65470567 | FLOXYFRAL 50 mg, comprimé pelliculé sécable (VIATRIS MEDICAL) | Comprimé pelliculé |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

La littérature retrouvée signale un cas de convulsions lors de l'association de la fluvoxamine avec une phénothiazine (lévomépromazine). Cette association est pertinente si un neuroleptique est ajouté, comme dans les publications sur le TOC résistant. La fluvoxamine est par ailleurs connue pour inhiber fortement les CYP1A2 et CYP2C19. L'absence d'interactions dans le dossier (0 trouvée) est probablement une lacune de données et non une absence d'interactions.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé, mais aucun essai ni étude n'a évalué la fluvoxamine directement dans le trouble de la personnalité schizotypique. Les publications retrouvées concernent le TOC comorbide.
- Les données de sécurité de la notice ANSM ne sont pas disponibles, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice ANSM : mises en garde et contre-indications de Floxyfral (téléchargement et analyse du PDF)
- Données détaillées sur le mécanisme d'action (DrugBank) et indication d'origine de l'AMM
- Études ciblant spécifiquement le trouble schizotypique (essai contrôlé, ou au minimum une série de cas dédiée)
- Profil complet des interactions médicamenteuses, à vérifier manuellement

**Remarque :** dans le même dossier, trois autres indications prédites ont un meilleur niveau de preuve (L1, « Proceed with Guardrails »). Ce sont le **trouble anxieux**, l'**agoraphobie** (surtout le trouble panique avec agoraphobie) et la **dépression endogène**, cette dernière avec un essai de phase 2, NCT04160377, de statut inconnu. Ces trois pistes sont mieux étayées que celle du trouble schizotypique. Ces preuves reposent sur des essais contrôlés randomisés publiés et des méta-analyses, sans essai de phase 3 enregistré dans le dossier.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

