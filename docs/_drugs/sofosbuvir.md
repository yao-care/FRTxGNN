---
layout: default
title: Sofosbuvir
parent: Preuves modérées (L3-L4)
nav_order: 285
evidence_level: L4
indication_count: 8
---

# Sofosbuvir
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **8** 
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

# Sofosbuvir : De l'Hépatite C à l'Infection par le Virus de l'Hépatite B

## Résumé en Une Phrase

Le sofosbuvir est un analogue nucléotidique inhibiteur de la polymérase NS5B du virus de l'hépatite C (VHC). Il est commercialisé en France seul (Sovaldi) ou en association (Epclusa, Harvoni) pour traiter l'hépatite C.
Le modèle TxGNN prédit qu'il pourrait être utile dans l'**infection par le virus de l'hépatite B (VHB)**. Cependant, seuls **quelques essais** sur les 50 listés ciblent réellement le VHB (un essai de phase 2 en monoinfection et des essais chez des patients coinfectés VHC/VHB), et le principal signal clinique concerne la **sécurité** (réactivation du VHB) et non l'efficacité.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hépatite C chronique (déduite des produits autorisés et des essais ; le texte d'indication de l'AMM n'est pas renseigné dans les données) |
| Nouvelle Indication Prédite | Infection par le virus de l'hépatite B |
| Score de Prédiction TxGNN | 99,77 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 7 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le champ DrugBank. Le sofosbuvir est un analogue nucléotidique dont le métabolite triphosphate inhibe l'ARN polymérase ARN-dépendante NS5B du VHC. Cela explique son efficacité dans l'hépatite C. Comme d'autres antiviraux nucléos(t)idiques, il est administré sous forme de promédicament activé dans le foie.

Le lien avec l'hépatite B est **faible sur le plan mécanistique**. Le VHB est un virus à ADN qui se réplique par une ADN polymérase à activité de transcription inverse, et non par une polymérase de type NS5B. Aucune activité antivirale directe contre le VHB n'est établie. Le score TxGNN très élevé reflète très probablement la **cooccurrence** des deux virus dans le graphe de connaissances (coinfections VHC/VHB, mêmes patients, mêmes essais), et non une activité anti-VHB réelle.

Un point mérite l'attention. Un essai de phase 2 (NCT03312023) est parti d'une observation rétrospective : chez des patients coinfectés traités par lédipasvir/sofosbuvir, l'antigène HBs (HBsAg) a modestement diminué. Cet essai teste si l'on observe la même baisse chez des patients porteurs du VHB seul. C'est une hypothèse exploratoire, sans résultat confirmé dans les données fournies.

---

## Preuves d'Essais Cliniques

Sur les 50 essais remontés pour cette indication, la grande majorité concerne l'hépatite C et non le VHB. Voici les plus pertinents pour le VHB :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Terminé | 21 | Lédipasvir/sofosbuvir 12 semaines chez des patients avec infection par le VHB. Objectif : baisse du HBsAg. Résultats non fournis dans les données. |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3b | Terminé | 111 | Lédipasvir/sofosbuvir 12 semaines chez des adultes coinfectés VHC (génotype 1 ou 2)/VHB à Taïwan. Objectif : efficacité antivirale, sécurité et tolérance (critère centré sur le VHC). |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Terminé | 23 | Antiviraux à action directe chez des patients coinfectés VHC/VHB. Objectif : incidence et facteurs prédisposants de la réactivation du VHB. |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Inconnu | 120 | Sofosbuvir/velpatasvir 12 semaines avec ténofovir alafénamide (TAF) prophylactique, chez des patients coinfectés VHC/VHB en Chine, avec ou sans cirrhose compensée. |
| [NCT02768961](https://clinicaltrials.gov/study/NCT02768961) | Phase 4 | Terminé | 64 | Dépistage du VHC, du VHB et du VIH en milieu pénitentiaire et traitement du VHC sans interféron (le VHB n'est pas la cible du traitement). |

---

## Preuves de la Littérature

Sur les 19 publications remontées, aucun essai randomisé ni revue systématique ne démontre une efficacité contre le VHB. Les résultats ci-dessous sont limités à ce que les résumés disponibles indiquent.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Essai de phase 2 ouvert | J Med Virol | Lédipasvir/sofosbuvir chez des patients avec VHB seul. Critères : baisse du HBsAg (principal) et de l'ADN du VHB (secondaire) à la semaine 12. |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Étude observationnelle | J Clin Gastroenterol | Risque de réactivation du VHB pendant ou après un traitement du VHC par lédipasvir/sofosbuvir. |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Étude observationnelle prospective | J Viral Hepat | Réactivation du VHB chez des patients cancéreux coinfectés VHC/VHB recevant des antiviraux à action directe. |
| [35268497](https://pubmed.ncbi.nlm.nih.gov/35268497/) | 2022 | Étude observationnelle | J Clin Med | Cinétique de l'ADN du VHB et du HBsAg chez des patients coinfectés VHC/VHB sous antiviraux à action directe, avec ou sans sofosbuvir. |
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | Cohorte | Trans R Soc Trop Med Hyg | Traitement par sofosbuvir/daclatasvir chez des patients VHC et coinfectés VHC/VHB en Égypte. |
| [26967675](https://pubmed.ncbi.nlm.nih.gov/26967675/) | 2016 | Revue | J Clin Virol | Réactivation du VHB chez les adultes coinfectés traités par antiviraux à action directe contre le VHC. |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Rapport de cas et revue | Medicine | Cas de réactivation du VHB après traitement du VHC par sofosbuvir et ribavirine. |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Rapport de cas | J Med Case Rep | Réactivation du VHB avec un mutant d'échappement de l'HBsAg pendant un traitement par sofosbuvir/velpatasvir. |

---

## Informations de Marché en France

Cinq des 7 AMM sont présentées ci-dessous. Le texte d'indication n'est pas renseigné dans les données.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61206641 | SOVALDI 400 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 60348342 | EPCLUSA 200 mg/50 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 60704272 | EPCLUSA 150 mg/37,5 mg, granulés enrobés en sachet | Granulés enrobés | Non renseignée |
| 68425495 | EPCLUSA 200 mg/50 mg, granulés enrobés en sachet | Granulés enrobés | Non renseignée |
| 64426906 | HARVONI 90 mg/400 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |

---

## Considérations de Sécurité

Les données de sécurité issues de la notice (mises en garde, contre-indications) ne sont pas disponibles et aucune interaction médicamenteuse n'a été retrouvée dans la base. Veuillez consulter la notice pour les informations de sécurité.

Un signal ressort de la littérature : la **réactivation du VHB** chez les patients coinfectés (ou ayant déjà été exposés au VHB) lorsque le VHC est éliminé par des antiviraux à action directe, dont le sofosbuvir, sans suppression concomitante du VHB (PMID 33031326, 29334502, 31542053, 33523503). Ce risque est important à considérer avant toute utilisation dans un contexte d'hépatite B.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le sofosbuvir n'a pas de mécanisme antiviral établi contre le VHB, et les données cliniques disponibles portent surtout sur le VHC chez des patients coinfectés. Le signal principal lié au VHB est un risque de réactivation, pas un bénéfice thérapeutique.
- Le score TxGNN élevé s'explique vraisemblablement par la cooccurrence des infections, et non par une activité anti-VHB. L'étape de sécurité (S1) ne peut pas être franchie tant que la notice n'est pas analysée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde et contre-indications), élément bloquant.
- Compléter les données sur le mécanisme d'action via l'API DrugBank.
- Obtenir les résultats publiés de l'essai NCT03312023 et de l'étude PMID 36045503 (baisse du HBsAg et de l'ADN du VHB en monoinfection).
- Définir un plan de dépistage et de surveillance du VHB avant tout traitement du VHC.
- À titre indicatif, l'infection par le virus de l'hépatite E (2e prédiction, niveau L3) dispose de données précliniques et de petites séries de cas. Elle pourrait constituer une piste de recherche plus étayée.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

