---
layout: default
title: Oxitriptan
parent: Preuves modérées (L3-L4)
nav_order: 226
evidence_level: L4
indication_count: 1
---

# Oxitriptan
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **1** 
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

# Oxitriptan : De l'Indication Non Renseignée à l'Insomnie

## Résumé en Une Phrase

L'oxitriptan (5-hydroxytryptophane, 5-HTP) est commercialisé en France sous le nom LEVOTONINE (gélule), mais aucune indication d'origine n'est renseignée dans les données disponibles.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**insomnie**.
Cette piste s'appuie sur **6 essais cliniques** et **13 publications**, mais aucune de ces sources ne démontre directement l'efficacité de l'oxitriptan dans l'insomnie.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Insomnie |
| Score de Prédiction TxGNN | 99,89 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans DrugBank. On sait toutefois que l'oxitriptan est le précurseur biosynthétique direct de la sérotonine et, en aval, de la mélatonine. Ces deux molécules interviennent dans la régulation du sommeil, ce qui donne un lien plausible avec l'insomnie.

Aucune indication d'origine n'est renseignée, donc la prédiction ne peut pas être comparée à une indication officielle. La plupart des publications retrouvées utilisent le modèle de rongeur PCPA (para-chlorophénylalanine). Dans ce modèle, l'inhibition de la tryptophane hydroxylase épuise la sérotonine et provoque un comportement de type insomnie. Il montre que restaurer le tonus sérotoninergique améliore le sommeil, ce qui est cohérent avec la logique du 5-HTP.

Ces études testent cependant d'autres agents (extraits de plantes, ginsénoside Rg1, nuciférine, acide cinnamique) et non le 5-HTP lui-même. Le soutien reste donc indirect. Le score TxGNN est très élevé (0,999), mais il s'agit d'une prédiction computationnelle et non d'une preuve clinique.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT06893822](https://clinicaltrials.gov/study/NCT06893822) | N/A | En recrutement | 20 | Griffonia simplicifolia (source naturelle de 5-HTP) sur la douleur et la sensibilisation chez des volontaires sains, en croisé contre placebo. Pertinent pour la dose et la tolérance, pas pour le sommeil. |
| [NCT00001918](https://clinicaltrials.gov/study/NCT00001918) | N/A | Terminé | 20 | Évaluation clinique du syndrome éosinophilie-myalgie lié au L-5-hydroxytryptophane. Ce n'est pas un essai d'efficacité, mais un contexte de sécurité important. |
| [NCT04078724](https://clinicaltrials.gov/study/NCT04078724) | N/A | Terminé | 33 | Effet d'une supplémentation en 5-HTP sur la qualité du sommeil et le microbiote intestinal chez des personnes âgées, avec ou sans troubles cognitifs légers. Le sommeil est au mieux un critère périphérique. |
| [NCT03364101](https://clinicaltrials.gov/study/NCT03364101) | N/A | Terminé | 60 | Étude « Poweroff » sur la qualité du sommeil (placebo vs PowerOff, actigraphie). Aucun lien démontré avec l'oxitriptan ; probable correspondance fortuite de mots-clés. |
| [NCT06365801](https://clinicaltrials.gov/study/NCT06365801) | N/A | Pas encore en recrutement | 100 | Étude de cohorte sur les points d'acupuncture dans le syndrome de l'intestin irritable. Sans pertinence directe. |
| [NCT06718452](https://clinicaltrials.gov/study/NCT06718452) | N/A | Pas encore en recrutement | 100 | Acouphènes et neuroinflammation, avec l'association umPEALUT (palmitoyléthanolamide/lutéoline). Sans pertinence directe. |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [4128428](https://pubmed.ncbi.nlm.nih.gov/4128428/) | 1974 | Rapport de cas | Electroencephalogr Clin Neurophysiol | Cas d'agrypnie (4 mois sans sommeil) dans la maladie de Morvan, avec action favorable du 5-hydroxytryptophane (d'après le titre ; résumé absent). |
| [4548556](https://pubmed.ncbi.nlm.nih.gov/4548556/) | 1974 | Étude de cas | Rev Neurol | Études polygraphiques et métaboliques d'une insomnie persistante avec hallucinations (chorée fibrillaire de Morvan). |
| [2962265](https://pubmed.ncbi.nlm.nih.gov/2962265/) | 1987 | Revue | Rev Med Suisse Romande | Indications neurologiques du L-5-hydroxytryptophane (résumé absent). |
| [33634088](https://pubmed.ncbi.nlm.nih.gov/33634088/) | 2021 | Revue | Front Bioeng Biotechnol | Synthèse microbienne du 5-HTP, cité comme utilisé dans la dépression, l'insomnie et la migraine. Non clinique. |
| [32006050](https://pubmed.ncbi.nlm.nih.gov/32006050/) | 2020 | Bioprocédé | Appl Microbiol Biotechnol | Production accrue de 5-HTP par ingénierie métabolique. Non clinique. |
| [40350945](https://pubmed.ncbi.nlm.nih.gov/40350945/) | 2025 | Préclinique | Zhongguo Zhong Yao Za Zhi | Effet de la décoction Fushen sur le système 5-HT et le GABA dans un modèle murin d'insomnie induite par PCPA. |
| [40493075](https://pubmed.ncbi.nlm.nih.gov/40493075/) | 2025 | Préclinique | Psychopharmacology | Le ginsénoside Rg1 atténue l'insomnie induite par PCPA chez la souris (voie Nrf2/HO-1, inflammasome NLRP3). |
| [40160035](https://pubmed.ncbi.nlm.nih.gov/40160035/) | 2025 | Préclinique | Int J Neuropsychopharmacol | Effets sédatifs et hypnotiques de la nuciférine chez le rongeur, via la modulation du système sérotoninergique. |
| [40367689](https://pubmed.ncbi.nlm.nih.gov/40367689/) | 2025 | Préclinique | Int Immunopharmacol | L'acide cinnamique favorise le sommeil dans l'insomnie induite par PCPA chez le rat. |
| [24785966](https://pubmed.ncbi.nlm.nih.gov/24785966/) | 2014 | Préclinique | Fitoterapia | La gomisine N potentialise le sommeil induit par le pentobarbital chez la souris, via les systèmes sérotoninergique et GABAergique. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 62469022 | LEVOTONINE | Gélule | PANPHARMA |

## Considérations de Sécurité

- **Contexte de sécurité issu des essais** : le syndrome éosinophilie-myalgie a touché plus de 1 500 personnes en 1989 après la prise de L-tryptophane, avec jusqu'à 40 décès. Des impuretés dans les compléments sont suspectées. Des impuretés similaires ont été signalées dans des produits à base de 5-HTP (essai NCT00001918). La qualité et la pureté du produit sont donc à vérifier pour toute décision de repositionnement.

Veuillez consulter la notice pour les autres informations de sécurité (mises en garde, contre-indications, interactions médicamenteuses).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le niveau de preuve est L4 : aucun essai clinique ne teste l'oxitriptan dans l'insomnie, et le soutien repose sur un rationnel sérotoninergique et des études précliniques d'autres agents.
- Les données de sécurité issues de la notice de l'ANSM manquent, ce qui bloque le passage à l'étape de sélection de sécurité. Le risque historique lié aux impuretés (syndrome éosinophilie-myalgie) renforce cette prudence.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice de l'ANSM (mises en garde, contre-indications, interactions).
- Compléter les données de mécanisme d'action (MOA) via DrugBank.
- Identifier ou conduire des essais contrôlés randomisés du 5-HTP dans l'insomnie.
- Vérifier le contrôle de qualité et de pureté du produit commercialisé.
- Clarifier l'indication approuvée de LEVOTONINE pour comparer la prédiction à l'indication réelle.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Un candidat de repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

