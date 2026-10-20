---
layout: default
title: Artemether
parent: Preuves élevées (L1-L2)
nav_order: 72
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Artemether : nouvelle indication prédite, Paludisme à Plasmodium falciparum (niveau de preuve L1). Indication d'origine : Non renseignée dans les données d'AMM compilées"
monitor_inn: "artemether"
predicted_indications: ["acquired angioedema", "Plasmodium falciparum malaria", "angioedema", "hereditary angioedema", "nephrogenic syndrome of inappropriate antidiuresis", "acute contagious conjunctivitis", "scleroderma (disease)", "conjunctivitis", "renin-angiotensin-aldosterone system-blocker-induced angioedema"]
---

# Artemether
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
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

# Artéméther : De l'indication antipaludique d'origine au paludisme à Plasmodium falciparum

## Résumé en Une Phrase

L'artéméther est un dérivé de l'artémisinine, utilisé en association avec la luméfantrine (spécialité RIAMET) pour traiter le paludisme.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **paludisme à Plasmodium falciparum**, avec **30 essais cliniques** et **20 publications** compilés pour cette direction. Il s'agit toutefois d'une indication déjà établie (validation du modèle) et non d'un repositionnement au sens strict.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées |
| Nouvelle Indication Prédite | Paludisme à Plasmodium falciparum |
| Score de Prédiction TxGNN | 99,77 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Proceed with Guardrails |

**Remarque :** les prédictions classées en premier rang (angioedème acquis, score 99,90 %) ne reposent sur aucun essai ni publication (niveau L5, décision Hold). Le paludisme à P. falciparum, classé au rang 2, est retenu ici car c'est la seule prédiction réellement documentée.

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base compilée. D'après les connaissances pharmacologiques établies, l'artéméther est un dérivé de l'artémisinine. Son pont endoperoxyde est activé par le fer de l'hème dans la vacuole digestive du parasite, ce qui génère des radicaux libres qui endommagent les protéines parasitaires et provoquent une clairance parasitaire rapide.

L'indication prédite correspond à l'usage antipaludique établi de l'association artéméther-luméfantrine, un traitement combiné à base d'artémisinine (ACT) largement recommandé. La prédiction valide donc le modèle plus qu'elle ne propose un véritable repositionnement. L'entrée « paludisme » (rang 3) est une catégorie plus large qui partage l'essentiel de ses essais avec celle-ci : les deux ne constituent pas des preuves indépendantes.

Les autres prédictions à score élevé (angioedème, angioedème héréditaire, conjonctivite, syndrome néphrogénique d'antidiurèse inappropriée, etc.) n'ont aucun support clinique ni plausibilité mécanistique établie. Seule la sclérodermie présente une hypothèse préclinique spéculative (effets antifibrotiques des dérivés de l'artémisinine, via la voie TGF-β/Smad), non validée.

---

## Preuves d'Essais Cliniques

Les essais ci-dessous portent sur l'association artéméther-luméfantrine. Sont listés les 10 plus pertinents (sur 30 essais compilés).

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00422084](https://clinicaltrials.gov/study/NCT00422084) | Phase 3 | Terminé | 1272 | Pyronaridine-artésunate vs Coartem (artéméther-luméfantrine) chez enfants et adultes, double aveugle |
| [NCT01082705](https://clinicaltrials.gov/study/NCT01082705) | Phase 3 | Terminé | 323 | Efficacité des ACT chez les enfants de 6 à 59 mois en Tanzanie |
| [NCT00677833](https://clinicaltrials.gov/study/NCT00677833) | Phase 2/3 | Terminé | 361 | Azithromycine + chloroquine vs artéméther-luméfantrine chez l'enfant en Afrique |
| [NCT02637128](https://clinicaltrials.gov/study/NCT02637128) | Phase 4 | Terminé | 452 | Efficacité in vivo de l'artéméther-luméfantrine et de l'artésunate-amodiaquine au Malawi |
| [NCT01017770](https://clinicaltrials.gov/study/NCT01017770) | Phase 4 | Terminé | 340 | Artéméther-luméfantrine vs artésunate-amodiaquine au Burkina Faso |
| [NCT00529867](https://clinicaltrials.gov/study/NCT00529867) | Phase 4 | Terminé | 267 | Suspension vs comprimés d'artéméther-luméfantrine chez l'enfant au Kenya |
| [NCT03453840](https://clinicaltrials.gov/study/NCT03453840) | Phase 4 | Terminé | 305 | Schéma prolongé chez des enfants infectés ou non par le VIH |
| [NCT01998295](https://clinicaltrials.gov/study/NCT01998295) | Phase 4 | Terminé | 45 | Temps de clairance parasitaire après artéméther-luméfantrine en Tanzanie (petite étude) |
| [NCT05951595](https://clinicaltrials.gov/study/NCT05951595) | Phase 3 | En recrutement | 1680 | Triple ACT artéméther-luméfantrine-amodiaquine vs ACT de première ligne |
| [NCT01103830](https://clinicaltrials.gov/study/NCT01103830) | Phase 1 | Terminé | 287 | Effet sur l'intervalle QT/QTc d'Eurartesim comparé à Riamet, placebo et moxifloxacine (sécurité) |

---

## Preuves de la Littérature

Sont listées les publications les plus pertinentes (sur 20 compilées), en priorité les synthèses systématiques.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35271592](https://pubmed.ncbi.nlm.nih.gov/35271592/) | 2022 | Revue systématique et méta-analyse | PLoS One | Efficacité thérapeutique des ACT (dont artéméther-luméfantrine) en Afrique subsaharienne |
| [34983552](https://pubmed.ncbi.nlm.nih.gov/34983552/) | 2022 | Revue systématique et méta-analyse d'ECR | Malaria Journal | Sécurité dihydroartémisinine-pipéraquine vs artéméther-luméfantrine chez l'enfant en Afrique |
| [22548983](https://pubmed.ncbi.nlm.nih.gov/22548983/) | 2012 | Revue systématique | Malaria Journal | Sécurité et efficacité de l'artéméther-luméfantrine pendant la grossesse |
| [33957925](https://pubmed.ncbi.nlm.nih.gov/33957925/) | 2021 | Revue systématique et méta-analyse | Malaria Journal | Efficacité et sécurité en Éthiopie |
| [29137664](https://pubmed.ncbi.nlm.nih.gov/29137664/) | 2017 | Revue systématique et méta-analyse | Infect Dis Poverty | Efficacité thérapeutique en Éthiopie |
| [26381375](https://pubmed.ncbi.nlm.nih.gov/26381375/) | 2015 | Revue systématique et méta-analyse | BMC Medicine | Concentrations de luméfantrine au jour 7 et réponse thérapeutique |
| [38741101](https://pubmed.ncbi.nlm.nih.gov/38741101/) | 2024 | Étude d'efficacité thérapeutique | Malaria Journal | Efficacité et tolérance au Niger, 2020 |
| [40660279](https://pubmed.ncbi.nlm.nih.gov/40660279/) | 2025 | Étude d'efficacité thérapeutique | Malaria Journal | Efficacité de plusieurs ACT au Mozambique, 2022 |
| [40138574](https://pubmed.ncbi.nlm.nih.gov/40138574/) | 2025 | Étude moléculaire | J Infect Dis | Sélection d'un nombre accru de copies de pfmdr1 sous traitement ; baisse d'efficacité récemment émergée en Afrique |
| [31210357](https://pubmed.ncbi.nlm.nih.gov/31210357/) | 2019 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | Artéméther dans le paludisme grave (entrée « paludisme ») |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65574434 | RIAMET 20 mg/120 mg, comprimé (NOVARTIS PHARMA) | Comprimé | Texte d'indication non disponible (AMM annulée) |

---

## Cytotoxicité

Section non applicable : l'artéméther est un antipaludique et non un antinéoplasique.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie du graphe de connaissances, et non texte de la notice) : syndrome du QT long, syndrome du QT long familial, torsades de pointes, carence en potassium.
- **Interactions Médicamenteuses** : 95 interactions recensées. Parmi les interactions **majeures** figurent : clarithromycine, cobicistat, amprénavir, aprépitant non listé, **apalutamide**, atazanavir et bocéprévir. Parmi les interactions **modérées** : dexaméthasone, miconazole, troglitazone, défératirox, fostamatinib, bosentan, brigatinib, armodafinil, bexarotène, aminoglutéthimide et amobarbital.
- **Surveillance cardiaque** : une étude de phase 1 (NCT01103830) et une étude ECG sur un schéma prolongé (PMID 32664948) ont examiné l'effet sur le QTc. Une étude plus ancienne (PMID 10674679) n'a pas retrouvé de cardiotoxicité cliniquement significative.

Les mises en garde et contre-indications issues de la notice française ne sont pas disponibles. Veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails** (pour le paludisme à P. falciparum uniquement)

**Justification :**
- Les preuves sont abondantes (plusieurs essais de phase 3 et 4, ainsi que des méta-analyses), mais l'indication est déjà établie : il ne s'agit pas d'un repositionnement nouveau. Les autres prédictions (angioedème, conjonctivite, sclérodermie, etc.) restent au niveau L5 sans aucun support et relèvent de Hold ou de simple question de recherche.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer le texte de la notice ANSM (mises en garde, contre-indications). Cette lacune est bloquante pour le dépistage de sécurité.
- Compléter les données sur le mécanisme d'action dans DrugBank et l'indication d'origine, absente des données d'AMM.
- Clarifier le statut réglementaire : seule une AMM annulée est enregistrée pour RIAMET, ce qui reflète probablement le produit en association et non l'accès réel au marché.
- Mettre en place une surveillance de l'ECG (QTc) et de la kaliémie, et un contrôle des co-médications à risque (inhibiteurs ou inducteurs du CYP3A4, macrolides).
- Suivre l'émergence de résistances à l'artémisinine et de baisse d'efficacité en Afrique.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

