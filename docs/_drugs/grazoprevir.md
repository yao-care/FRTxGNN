---
layout: default
title: Grazoprevir
parent: Prédiction du modèle uniquement (L5)
nav_order: 372
evidence_level: L5
indication_count: 10
---

# Grazoprevir
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Grazoprevir : De l'hépatite C chronique à l'infection par le VIH

## Résumé en Une Phrase

Grazoprevir (commercialisé en association avec l'elbasvir sous le nom ZEPATIER) est un inhibiteur de la protéase NS3/4A du virus de l'hépatite C, initialement utilisé pour le traitement de l'**infection chronique par le virus de l'hépatite C**.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infection par le VIH**, mais les données compilées montrent que les **10 essais cliniques** rattachés à cette prédiction portent sur le traitement de l'hépatite C chez des patients co-infectés par le VIH, et non sur le VIH lui-même. La prédiction relève donc d'une extension de population plutôt que d'un véritable repositionnement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection chronique par le virus de l'hépatite C (source : graphe de connaissances, le texte d'indication de l'AMM n'étant pas renseigné) |
| Nouvelle Indication Prédite | Infection par le VIH |
| Score de Prédiction TxGNN | 99,73 % |
| Niveau de Preuve | L3 (au mieux ; aucune preuve directe d'activité anti-VIH) |
| Statut de Marché en France | Annulée uniquement (AMM annulée) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier compilé. Selon les informations connues, le grazoprevir est un inhibiteur de la protéase NS3/4A du VHC, utilisé en association à dose fixe avec l'elbasvir (inhibiteur de NS5A). Son efficacité dans l'hépatite C chronique de génotypes 1 et 4 est établie.

Le grazoprevir n'a aucune activité directe connue contre la protéase du VIH ni contre d'autres cibles du VIH. Le score élevé du modèle reflète vraisemblablement la proximité, dans le graphe de connaissances, entre les antiviraux et les nœuds liés au VIH. Les données cliniques disponibles concernent la guérison de l'hépatite C et les interactions médicamenteuses avec les antirétroviraux chez les patients co-infectés VIH/VHC. Il s'agit d'une extension de population de l'indication d'origine, non d'un repositionnement au sens strict.

Parmi les autres prédictions, seules la fièvre hémorragique d'Omsk et la maladie de la forêt de Kyasanur (flavivirus possédant une protéase NS3) ont une justification structurale plausible au niveau de la classe virale. Elles ne reposent toutefois que sur une prédiction informatique et une étude in silico.

---

## Preuves d'Essais Cliniques

Tous les essais ci-dessous évaluent le traitement de l'hépatite C ; aucun n'a de critère d'efficacité anti-VIH.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02897596](https://clinicaltrials.gov/study/NCT02897596) | Phase 3 | Inconnu | 62 | Grazoprevir/elbasvir pendant 8 ou 12 semaines dans l'hépatite C chronique précoce chez des patients co-infectés VIH/VHC |
| [NCT02105662](https://clinicaltrials.gov/study/NCT02105662) | Phase 3 | Terminé | 218 | Grazoprevir + elbasvir chez des patients naïfs de traitement co-infectés par le VIH ; critère : RVS12 |
| [NCT02252016](https://clinicaltrials.gov/study/NCT02252016) | Phase 3 | Terminé | 159 | Grazoprevir + elbasvir versus placebo dans l'hépatite C avec maladies hématologiques héréditaires, avec ou sans co-infection VIH |
| [NCT02600325](https://clinicaltrials.gov/study/NCT02600325) | Phase 3 | Terminé | 80 | Grazoprevir + elbasvir dans l'hépatite C aiguë de génotype 1/4 chez des patients infectés par le VIH (étude DAHHS-2) |
| [NCT02785666](https://clinicaltrials.gov/study/NCT02785666) | Phase 3 | Terminé | 150 | Stratégie « traiter, conseiller, guérir » chez des hommes ayant des rapports sexuels avec des hommes, co-infectés (Swiss HCVree) |
| [NCT03098121](https://clinicaltrials.gov/study/NCT03098121) | Phase 4 | Terminé | 40 | Efficacité et tolérance chez des patients co-infectés VIH/VHC de génotype 1 déjà traités par peginterféron/ribavirine |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Terminé | 87 | Risque cardiovasculaire après éradication du VHC chez des patients VIH/VHC |
| [NCT04048850](https://clinicaltrials.gov/study/NCT04048850) | N/A | Terminé | 25 | Cohorte de traitement par Zepatier chez des patients mono-infectés ou co-infectés avec usage de substances |
| [NCT03407703](https://clinicaltrials.gov/study/NCT03407703) | N/A | Inconnu | 50 | Effet du traitement par elbasvir/grazoprevir sur la fonction rénale, avec ou sans VIH |
| [NCT02057003](https://clinicaltrials.gov/study/NCT02057003) | N/A | Inconnu | 1000 | Cohorte HEPAVIR : antiviraux à action directe en conditions réelles chez des patients co-infectés |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [26423374](https://pubmed.ncbi.nlm.nih.gov/26423374/) | 2015 | Essai non randomisé, ouvert | Lancet HIV | Étude C-EDGE CO-INFECTION : efficacité et tolérance du grazoprevir + elbasvir chez des patients co-infectés VHC/VIH |
| [32246857](https://pubmed.ncbi.nlm.nih.gov/32246857/) | 2020 | Revue systématique et méta-analyse en réseau | J Gastroenterol Hepatol | Efficacité et sécurité des schémas d'antiviraux à action directe dans la co-infection VHC/VIH |
| [28689442](https://pubmed.ncbi.nlm.nih.gov/28689442/) | 2017 | Revue | Expert Opin Drug Metab Toxicol | Interactions médicamenteuses entre antiviraux anti-VHC et antirétroviraux |
| [30745392](https://pubmed.ncbi.nlm.nih.gov/30745392/) | 2019 | Étude de phase 1 | Antimicrob Agents Chemother | Interactions pharmacocinétiques avec le ritonavir, l'atazanavir, le lopinavir et le darunavir chez des volontaires sains |
| [30541077](https://pubmed.ncbi.nlm.nih.gov/30541077/) | 2019 | Étude d'interaction | J Antimicrob Chemother | Interactions avec les inhibiteurs d'intégrase raltégravir et dolutégravir |
| [32910788](https://pubmed.ncbi.nlm.nih.gov/32910788/) | 2020 | Étude clinique | Antivir Ther | Efficacité d'elbasvir/grazoprevir dans l'hépatite C de génotype 1 avec ou sans VIH, en Thaïlande |
| [28417245](https://pubmed.ncbi.nlm.nih.gov/28417245/) | 2017 | Revue | Drugs | Elbasvir/grazoprevir dans l'hépatite C chronique de génotypes 1 et 4 |
| [30233138](https://pubmed.ncbi.nlm.nih.gov/30233138/) | 2018 | Revue | Drug Des Devel Ther | Données actuelles sur la sécurité et l'efficacité d'elbasvir/grazoprevir |
| [27603877](https://pubmed.ncbi.nlm.nih.gov/27603877/) | 2016 | Revue | Expert Rev Clin Pharmacol | Mécanisme d'action, pharmacocinétique, efficacité et sécurité d'elbasvir/grazoprevir |
| [29427481](https://pubmed.ncbi.nlm.nih.gov/29427481/) | 2018 | Revue | Liver Int | Résultats en vie réelle des antiviraux à action directe, y compris en co-infection |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66198173 | ZEPATIER 50 mg/100 mg, comprimé pelliculé (MERCK SHARP & DOHME, Pays-Bas) | Comprimé pelliculé | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 53 interactions sont recensées. Parmi les principales, de gravité majeure : clarithromycine, dexaméthasone, éluxadoline, acide obéticholique, rosuvastatine, simvastatine, cobicistat, eltrombopag, artésunate. De gravité modérée : aprépitant, cimétidine, clotrimazole, miconazole, troglitazone, déférasirox, ticagrelor, ivacaftor, zafirlukast, chloramphénicol, érythromycine.
- La littérature signale en outre des interactions pharmacocinétiques à vérifier avec les antirétroviraux (inhibiteurs de protéase boostés, inhibiteurs d'intégrase), point central en cas de co-infection VIH/VHC.

Veuillez consulter la notice pour les mises en garde et contre-indications.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucune donnée ne montre d'activité du grazoprevir contre le VIH : les essais et publications concernent l'hépatite C chez des patients co-infectés. Le score TxGNN élevé reflète probablement un artefact du graphe. L'AMM française est de plus annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de mécanisme d'action détaillées (cibles du grazoprevir, éventuelle activité antivirale hors VHC)
- Études précliniques in vitro de l'activité anti-VIH, aucune n'étant disponible à ce jour
- Texte de la notice (mises en garde et contre-indications) auprès de l'ANSM, absent du dossier et bloquant pour tout examen de sécurité
- Pour une valorisation clinique réaliste, considérer l'indication comme un usage dans la population co-infectée VIH/VHC (déjà couvert par les données de C-EDGE CO-INFECTION), et non comme un traitement du VIH
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

