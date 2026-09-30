---
layout: default
title: Imipramine
parent: Preuves modérées (L3-L4)
nav_order: 150
evidence_level: L4
indication_count: 7
---

# Imipramine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **7** 
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

# Imipramine : D'un antidépresseur tricyclique au Trouble Déficitaire de l'Attention avec Hyperactivité (TDAH)

## Résumé en Une Phrase

L'imipramine est un antidépresseur tricyclique, commercialisé en France sous le nom TOFRANIL. Le texte d'indication de ses AMM n'est pas renseigné dans les données fournies.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **TDAH (trouble déficitaire de l'attention avec hyperactivité)**.
Cette direction s'appuie sur **1 essai clinique** (sans lien avec l'imipramine) et **20 publications**, dont seule une minorité porte réellement sur l'imipramine, généralement des études anciennes et de petite taille.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM fournies (antidépresseur tricyclique) |
| Nouvelle Indication Prédite | Trouble déficitaire de l'attention avec hyperactivité (TDAH) |
| Score de Prédiction TxGNN | 99.90% |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les éléments d'analyse, l'imipramine inhibe la recapture de la noradrénaline et de la sérotonine. Comme antidépresseur tricyclique, son efficacité dans la dépression est connue, et mécanistiquement elle pourrait être applicable au TDAH.

Le lien avec le TDAH passe surtout par la modulation noradrénergique. Les stimulants (méthylphénidate, amphétamines) restent le traitement de première intention. La littérature fournie place les tricycliques (désipramine, imipramine) parmi les options non stimulantes de deuxième intention, avec l'atomoxétine et les agonistes alpha-2.

La prédiction est donc plausible sur le plan pharmacologique, mais aucun essai portant spécifiquement sur l'imipramine n'est fourni. Les autres prédictions du modèle sont beaucoup plus faibles :
- **Trouble obsessionnel-compulsif (TOC)** : preuve indirecte seulement. La clomipramine, tricyclique voisin, est un traitement établi, mais l'imipramine est moins sélective pour la sérotonine.
- **Sous-type inattentif du TDAH** : score probablement gonflé par la proximité avec le nœud TDAH dans le graphe de connaissances.
- **Autres prédictions** (syndrome facio-digito-génital, fibrome chondromyxoïde, torticolis paroxystique bénin du nourrisson, trouble spécifique du développement) : aucun lien mécanistique ni aucune preuve.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03220308](https://clinicaltrials.gov/study/NCT03220308) | Non applicable | Terminé | 103 | Entraînement à la pleine conscience (8 semaines) pour des enfants de 8 à 16 ans atteints de TDAH et pour leurs parents, comparé aux soins habituels seuls. L'essai ne teste pas l'imipramine et n'apporte donc aucune preuve pharmacologique. |

## Preuves de la Littérature

Aucun essai contrôlé randomisé n'est présent. Les publications ci-dessous sont classées par pertinence pour l'imipramine.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [6849467](https://pubmed.ncbi.nlm.nih.gov/6849467/) | 1983 | Non classé | Am J Psychiatry | « Imipramine for attention deficit disorder » : publication directement consacrée à l'imipramine dans le TDAH (résumé non disponible). |
| [9465283](https://pubmed.ncbi.nlm.nih.gov/9465283/) | 1996 | Non classé | Clin EEG | Une latence P300 prolongée prédit une mauvaise réponse à l'imipramine. 17 enfants TDAH, non répondeurs au pémoline, ont suivi un protocole imipramine. |
| [18304665](https://pubmed.ncbi.nlm.nih.gov/18304665/) | 2008 | Non classé | Int J Psychophysiol | Effets de l'imipramine sur l'EEG d'enfants TDAH non répondeurs aux stimulants. |
| [2258453](https://pubmed.ncbi.nlm.nih.gov/2258453/) | 1990 | Étude rétrospective | J Clin Psychopharmacol | Influence possible de la carbamazépine sur les concentrations plasmatiques d'imipramine et de désipramine chez 36 enfants TDAH. |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Méta-revue | Front Psychiatry | Efficacité, tolérance et risque suicidaire des antidépresseurs chez l'enfant et l'adolescent, TDAH inclus. |
| [17078784](https://pubmed.ncbi.nlm.nih.gov/17078784/) | 2006 | Étude clinique | Expert Rev Neurother | Choix du traitement guidé par la topographie P300. Les inhibiteurs de la recapture de la noradrénaline (désipramine, imipramine, atomoxétine) peuvent être efficaces. |
| [16890481](https://pubmed.ncbi.nlm.nih.gov/16890481/) | 2006 | Non classé | Clin Neurophysiol | Utilisation du potentiel évoqué cognitif P300 pour prédire la réponse au traitement dans le TDAH. |
| [15794722](https://pubmed.ncbi.nlm.nih.gov/15794722/) | 2005 | Non classé | Expert Opin Drug Saf | Sécurité des traitements non stimulants du TDAH. Les stimulants restent le premier choix, et des tricycliques comme l'imipramine peuvent être des alternatives. |
| [31776871](https://pubmed.ncbi.nlm.nih.gov/31776871/) | 2019 | Revue | CNS Drugs | Interactions médicamenteuses pharmacocinétiques des traitements du TDAH. |
| [11316683](https://pubmed.ncbi.nlm.nih.gov/11316683/) | 2001 | Non classé | Arch Dis Child | Protocole auditable de prise en charge du TDAH. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 68574699 | TOFRANIL 10 mg, comprimé enrobé | Comprimé enrobé | AMDIPHARM |
| 67117128 | TOFRANIL 25 mg, comprimé enrobé | Comprimé enrobé | AMDIPHARM |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité (mises en garde et contre-indications de l'ANSM non disponibles dans le dossier).

Les éléments d'analyse signalent toutefois, pour l'usage pédiatrique des tricycliques, des risques cardiaques et anticholinergiques ainsi qu'un risque suicidaire. Une publication fournie rapporte en outre une possible interaction avec la carbamazépine, qui modifie les concentrations plasmatiques d'imipramine.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucune donnée fournie ne montre l'efficacité de l'imipramine dans le TDAH : le seul essai clinique n'étudie pas ce médicament et la littérature est ancienne, surtout descriptive. La plausibilité repose sur le mécanisme et sur le score du modèle (niveau de preuve L4).
- Les données de sécurité de la notice ANSM manquent, ce qui bloque le passage à l'étape de criblage de sécurité. La population visée, principalement pédiatrique, est aussi celle où le profil de risque des tricycliques est le plus préoccupant.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications, interactions).
- Compléter les données sur le mécanisme d'action (DrugBank).
- Lire en texte intégral les études imipramine-TDAH (notamment PMID 6849467, 9465283, 18304665) pour établir leur conception et leurs résultats.
- Rechercher des essais contrôlés randomisés, ou des méta-analyses des tricycliques dans le TDAH.
- Évaluer le rapport bénéfice/risque cardiaque et suicidaire en population pédiatrique.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

