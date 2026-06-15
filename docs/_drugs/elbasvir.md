---
layout: default
title: Elbasvir
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 10
---

# Elbasvir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Elbasvir : De l'Hépatite C Chronique à l'Infection par le Virus de l'Hépatite B

## Résumé en Une Phrase

Elbasvir est un inhibiteur de la protéine NS5A du virus de l'hépatite C (VHC), utilisé en association fixe avec le grazoprévir (Zepatier®), pour le traitement de l'hépatite C chronique de génotypes 1 et 4 avec des taux de guérison supérieurs à 95%.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Infection par le Virus de l'Hépatite B (VHB)**,
avec **13 essais cliniques** et **18 publications** identifiés lors de la recherche de preuves — cependant, la quasi-totalité de ces données concerne le traitement du VHC, le VHB n'apparaissant que comme paramètre de surveillance de sécurité dans ces études.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hépatite C chronique (génotypes 1 et 4) |
| Nouvelle Indication Prédite | Infection par le Virus de l'Hépatite B |
| Score de Prédiction TxGNN | 99,71% |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Elbasvir (MK-8742) est un inhibiteur hautement sélectif de la protéine NS5A du VHC, une protéine multifonctionnelle non enzymatique indispensable à la réplication du génome viral, à l'assemblage des particules virales et aux interactions avec les facteurs cellulaires de l'hôte. Administré une fois par jour en combinaison avec le grazoprévir (inhibiteur NS3/4A), il forme la combinaison Zepatier® dont l'efficacité antivirale contre le VHC GT1 et GT4 est bien établie dans de nombreux essais de Phase 2 et 3. Les données pharmacocinétiques (profil d'élimination biliaire, demi-vie longue permettant une prise quotidienne unique) sont également bien documentées.

La pertinence mécanistique pour l'hépatite B est cependant très faible. Le VHB est un virus à ADN appartenant à la famille des Hepadnaviridae : son cycle de réplication repose sur une transcriptase inverse virale (HBV pol/RT), un ADN circulaire covalent fermé (cccDNA) servant de réservoir persistant, et des protéines spécifiques (HBx, HBsAg, HBcAg) sans aucune homologie avec la protéine NS5A du VHC. L'elbasvir n'a donc pas de cible moléculaire identifiée dans le VHB.

La prédiction TxGNN à score élevé (99,71%) est vraisemblablement un artefact du graphe de connaissances. Les essais cliniques traitant du VHC incluent systématiquement dans leurs critères d'éligibilité ou de surveillance la recherche d'une co-infection ou d'une réactivation du VHB (phénomène clinique bien décrit lors du traitement du VHC par agents à action directe), générant une co-occurrence bibliographique VHB–VHC que le modèle interprète à tort comme un signal thérapeutique.

---

## Preuves d'Essais Cliniques

> ⚠️ Aucun des essais ci-dessous n'évalue l'efficacité d'elbasvir contre le VHB. Le VHB n'apparaît que comme critère d'exclusion ou paramètre de surveillance de sécurité (réactivation VHB lors du traitement VHC).

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01532973](https://clinicaltrials.gov/study/NCT01532973) | Phase 1 | Terminé | 48 | Étude PK/PD de référence d'elbasvir (MK-8742) chez des patients VHC GT1 et GT3 ; établit le profil pharmacologique fondamental du médicament |
| [NCT03423641](https://clinicaltrials.gov/study/NCT03423641) | N/A | Terminé | 33 808 | Grande étude de sécurité réelle des AAD pour VHC (n=33 808) ; inclut la surveillance de la réactivation VHB comme signal de sécurité |
| [NCT02332720](https://clinicaltrials.gov/study/NCT02332720) | Phase 2 | Terminé | 413 | GZR + uprifosbuvir ± elbasvir ou ruzasvir dans VHC GT3-6 ; évaluation SVR12 multi-génotypes |
| [NCT02105688](https://clinicaltrials.gov/study/NCT02105688) | Phase 3 | Terminé | 301 | GZR/elbasvir dans VHC GT1, GT4, GT6 chez patients sous thérapie de substitution aux opiacés |
| [NCT01717326](https://clinicaltrials.gov/study/NCT01717326) | Phase 2 | Terminé | 573 | GZR + elbasvir ± RBV dans l'hépatite C chronique ; endpoint primaire SVR12 par bras de traitement |
| [NCT02600325](https://clinicaltrials.gov/study/NCT02600325) | Phase 3 | Terminé | 80 | GZR + elbasvir dans VHC aigu GT1/4 chez patients HIV (étude DAHHS-2, Pays-Bas) |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Terminé | 87 | Risques cardiovasculaires après éradication du VHC chez patients HIV/VHC co-infectés ; le VHB n'est pas un objectif de l'étude |
| [NCT02332707](https://clinicaltrials.gov/study/NCT02332707) | Phase 2 | Terminé | 443 | GZR + uprifosbuvir ± elbasvir dans VHC GT1 et GT2 (étude parallèle à NCT02332720) |
| [NCT01932762](https://clinicaltrials.gov/study/NCT01932762) | Phase 2 | Terminé | 98 | GZR ± elbasvir ± RBV dans VHC GT2, GT4, GT5 et GT6 non cirrhotiques naïfs |
| [NCT02115321](https://clinicaltrials.gov/study/NCT02115321) | Phase 2/3 | Terminé | 40 | GZR + elbasvir chez patients VHC GT1, 4, 6 avec cirrhose avancée Child-Pugh B |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [26904396](https://pubmed.ncbi.nlm.nih.gov/26904396/) | 2016 | Revue | Acta Pharm Sin B | Vue d'ensemble des AAD ciblant NS3/4A, NS5A et NS5B ; souligne la différence fondamentale entre VHC (guérissable) et VHB (non guérissable), sans lien direct avec elbasvir-VHB |
| [34902265](https://pubmed.ncbi.nlm.nih.gov/34902265/) | 2022 | Cohorte | Antimicrob Agents Chemother | GZR/EBR chez receveurs de transplantation hépatique ou rénale infectés par VHC GT1b : efficacité et sécurité hépatique et rénale dans un contexte immunosupprimé |
| [25529080](https://pubmed.ncbi.nlm.nih.gov/25529080/) | 2015 | Revue | Liver Int | Vers l'éradication du VHC et la guérison du VHB : analyse comparative des stratégies thérapeutiques, soulignant l'absence de traitement curatif pour le VHB à l'époque |
| [32039536](https://pubmed.ncbi.nlm.nih.gov/32039536/) | 2020 | Cohorte | J Viral Hepat | Expérience réelle d'elbasvir/grazoprévir à Taïwan chez patients VHC GT1 avec maladie hépatique compensée ; analyse détaillée des effets indésirables hépatiques et rénaux |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Revue | Clin Pharmacokinet | Mise à jour 2019 des paramètres PK/PD des AAD approuvés pour le VHC, incluant elbasvir/grazoprévir ; données de référence pharmacologiques |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Revue | Klin Mikrobiol Infekc Lek | Traitement antiviral des hépatites B et C chroniques chez l'enfant à Ostrava ; compare les approches thérapeutiques VHB vs VHC dans un contexte pédiatrique |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Analyse comparative | Ann Hepatol | Comparaison internationale des prix des antiviraux VHB et VHC ; contexte économique et d'accès aux traitements, sans lien mécanistique avec elbasvir-VHB |
| [32925725](https://pubmed.ncbi.nlm.nih.gov/32925725/) | 2020 | Cohorte | Medicine | Incidence et facteurs prédictifs des élévations anormales des transaminases pendant le traitement DAA dans le VHC chronique ; données de sécurité hépatique pertinentes pour une population co-infectée |
| [33208686](https://pubmed.ncbi.nlm.nih.gov/33208686/) | 2021 | Cohorte | Eur J Gastroenterol Hepatol | Efficacité et sécurité des AAD chez patients VHC atteints de maladies héréditaires du sang (thalassémie, hémophilie) ; population à risque de co-infection VHB |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | Étude expérimentale | Hepatology | Voies évolutives de la résistance aux inhibiteurs de protéase VHC ; étude des déterminants moléculaires de la résistance aux AAD, non applicable au VHB |

---

## Informations de Marché en France

Aucune autorisation de mise sur le marché n'a été identifiée dans la base de données réglementaire interrogée pour elbasvir en tant que substance active indépendante. Le médicament est **non commercialisé** sous ce statut réglementaire (0 AMM enregistrée). Elbasvir est disponible dans les pays où Zepatier® (elbasvir/grazoprévir) a été approuvé par l'EMA, mais cette approbation n'apparaît pas dans les données de la base consultée.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Elbasvir cible la protéine NS5A du VHC, une protéine absente chez le VHB qui est un virus à ADN à réplication fondamentalement différente ; il n'existe aucun rationnel mécanistique pour cette prédiction. L'ensemble des 13 essais cliniques et des 18 publications répertoriés concernent le traitement du VHC, le VHB n'apparaissant que comme paramètre de sécurité (risque de réactivation lors du traitement du VHC), et non comme cible thérapeutique — le score TxGNN élevé est vraisemblablement un artefact du graphe de connaissances lié à la co-occurrence fréquente VHB/VHC dans les métadonnées des essais.

**Pour avancer, les éléments suivants seraient nécessaires :**
- Données in vitro documentant une activité d'elbasvir contre le VHB (réplication, cccDNA, antigènes viraux) — actuellement inexistantes
- Identification d'une cible moléculaire VHB pouvant interagir avec elbasvir (aucune candidate identifiée à ce jour)
- Données de sécurité complètes (notices, mises en garde ANSM/EMA) pour évaluer les contre-indications dans une population VHB
- Réévaluation de la pertinence de cette indication au regard des traitements VHB disponibles (ténofovir, entécavir) qui disposent déjà d'un profil d'efficacité établi
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

