---
layout: default
title: Enzalutamide
parent: Prédiction du modèle uniquement (L5)
nav_order: 286
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "ENZALUTAMIDE"
predicted_indications: ["prostate leiomyoma", "Brenner tumor", "fibroma of prostate", "benign reproductive system neoplasm", "benign prostate phyllodes tumor"]
description: "Enzalutamide : nouvelle indication prédite, Prostate leiomyoma (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Enzalutamide
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

## Enzalutamide: Prostate leiomyoma
{: .text-alpha }

## Résumé en Une Phrase

Enzalutamide est un inhibiteur du récepteur des androgènes, initialement utilisé pour le traitement du **cancer de la prostate**.
Le modèle TxGNN prédit en premier rang une association avec la **susceptibilité génétique au cancer de la prostate et du cerveau**, mais cette catégorie n'est pas une maladie traitable. La seule prédiction accompagnée de données réelles est celle du **cancer des organes reproducteurs masculins** (36 essais cliniques et 20 publications identifiés), qui reflète en pratique l'indication d'origine (le cancer de la prostate) et non un véritable repositionnement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Prostate leiomyoma |
| Score de Prédiction TxGNN | 0.9957 |
| Niveau de Preuve | L5 (rang 1) ; L1 (rang 6, mais portant sur l'indication d'origine) |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances établies, l'enzalutamide est un inhibiteur du récepteur des androgènes (AR) : il bloque la liaison du ligand, la translocation nucléaire du récepteur et sa fixation à l'ADN. Son efficacité dans le cancer de la prostate est établie.

Le rang 1 correspond à une catégorie de susceptibilité génétique, et non à une maladie traitable ; aucun lien mécanistique avec le cancer du cerveau n'a été identifié. Les tumeurs bénignes de la prostate (léiomyome, fibrome, tumeur phyllode) ainsi que la tumeur de Brenner (néoplasme ovarien) ne présentent pas de dépendance connue à la signalisation AR qui justifierait un antagonisme systémique.

Pour la catégorie « cancer des organes reproducteurs masculins », les preuves sont dominées par le cancer de la prostate, déjà indication de l'enzalutamide. D'autres cancers de cette catégorie (testicule, pénis) ne sont pas étayés par les données fournies.

## Preuves d'Essais Cliniques

Seule la prédiction du rang 6 dispose d'essais cliniques (36 identifiés, dont 10 sont présentés ci-dessous, sélectionnés parmi les plus pertinents). Tous concernent le cancer de la prostate, soit l'indication d'origine.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02446405](https://clinicaltrials.gov/study/NCT02446405) | Phase 3 | Actif, ne recrute plus | 1125 | ENZAMET : enzalutamide vs antiandrogène non stéroïdien en traitement de première ligne du cancer de la prostate métastatique |
| [NCT06551324](https://clinicaltrials.gov/study/NCT06551324) | Phase 3 | Actif, ne recrute plus | 600 | MEVPRO-1 : mévrométostat + enzalutamide vs enzalutamide ou docétaxel dans le CPRCm après abiratérone |
| [NCT06496581](https://clinicaltrials.gov/study/NCT06496581) | Phase 3 | En recrutement | 500 | PEACE-6 : traitement standard ± 177Lu-PSMA-617 dans le cancer de la prostate hormonosensible métastatique d'emblée |
| [NCT03834493](https://clinicaltrials.gov/study/NCT03834493) | Phase 3 | Terminé (arrêté) | 1244 | KEYNOTE-641 : pembrolizumab + enzalutamide vs placebo + enzalutamide dans le CPRCm |
| [NCT06059118](https://clinicaltrials.gov/study/NCT06059118) | Phase 2 | En recrutement | 50 | Séquence DFMO + testostérone à haute dose puis enzalutamide dans le CPRCm asymptomatique |
| [NCT07512076](https://clinicaltrials.gov/study/NCT07512076) | Phase 2 | Pas encore en recrutement | 26 | Optimisation de la dose d'enzalutamide chez les patients âgés atteints d'un cancer de la prostate avancé |
| [NCT06582628](https://clinicaltrials.gov/study/NCT06582628) | Phase 2 | En recrutement | 78 | Talazoparib + enzalutamide en première ligne du CPRCm après progression sous inhibiteur de la voie AR |
| [NCT04332744](https://clinicaltrials.gov/study/NCT04332744) | Phase 2 | Terminé | 54 | Talazoparib + enzalutamide dans le cancer de la prostate hormonosensible métastatique |
| [NCT01547299](https://clinicaltrials.gov/study/NCT01547299) | Phase 2 | Terminé | 52 | Enzalutamide néoadjuvant avant prostatectomie dans le cancer de la prostate localisé |
| [NCT00510718](https://clinicaltrials.gov/study/NCT00510718) | Phase 1 | Terminé | 140 | Étude d'escalade de dose, sécurité et pharmacocinétique de MDV3100 (enzalutamide) dans le CPRC |

Les autres prédictions (rangs 1 à 5 et 7) ne disposent d'aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

La littérature pertinente concerne la catégorie du rang 6 (10 publications présentées sur 20 identifiées). Elle porte sur le cancer de la prostate, indication d'origine.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [42223064](https://pubmed.ncbi.nlm.nih.gov/42223064/) | 2026 | ECR | N Engl J Med | Inhibition de PARP et de la voie des androgènes + ADT dans le cancer de la prostate métastatique ; un essai antérieur avait montré un bénéfice de l'ajout du talazoparib à l'enzalutamide |
| [32534790](https://pubmed.ncbi.nlm.nih.gov/32534790/) | 2020 | Revue | Trends Cancer | Avancées thérapeutiques dans le cancer de la prostate avancé (enzalutamide, abiratérone, etc.) |
| [28655021](https://pubmed.ncbi.nlm.nih.gov/28655021/) | 2017 | Revue | JAMA | Diagnostic et traitement du cancer de la prostate |
| [37844613](https://pubmed.ncbi.nlm.nih.gov/37844613/) | 2023 | Étude préclinique | Nature | Cibler la chimiotaxie myéloïde pour lever la résistance thérapeutique dans le cancer de la prostate |
| [29460922](https://pubmed.ncbi.nlm.nih.gov/29460922/) | 2018 | Revue | Nat Rev Urol | Plasticité cellulaire et phénotype neuroendocrine, mécanisme de résistance aux inhibiteurs de la voie AR |
| [27725309](https://pubmed.ncbi.nlm.nih.gov/27725309/) | 2016 | Revue | Pharmacol Res | Variation du récepteur des androgènes, progression et résistance aux médicaments |
| [32673844](https://pubmed.ncbi.nlm.nih.gov/32673844/) | 2020 | Revue | Cancer Treat Res Commun | Traitements récents du cancer de la prostate résistant à la castration non métastatique (enzalutamide, apalutamide, darolutamide) |
| [33542074](https://pubmed.ncbi.nlm.nih.gov/33542074/) | 2021 | Étude préclinique | Clin Cancer Res | Résistance à l'enzalutamide associée à des dépendances à BCL-2 et IKKB |
| [25151012](https://pubmed.ncbi.nlm.nih.gov/25151012/) | 2015 | Étude préclinique | Eur Urol | AZD5363 + enzalutamide retarde la résistance dans des modèles précliniques |
| [34489465](https://pubmed.ncbi.nlm.nih.gov/34489465/) | 2021 | Étude préclinique | Nat Commun | Séquençage ATAC/ARN en cellule unique : cellules associées à la rechute et à la résistance à l'enzalutamide |

Pour la catégorie « tumeur bénigne de l'appareil reproducteur » (rang 5), cinq articles ont été retrouvés. Ils portent sur la biologie du cancer de la prostate (maladie maligne) et ne soutiennent pas cette indication. Les autres prédictions n'ont aucune littérature associée.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64093355 | XTANDI 40 mg, comprimé pelliculé (Astellas Pharma Europe, Pays-Bas) | Comprimé pelliculé | Non renseignée — AMM active |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (hormonothérapie : inhibiteur du récepteur des androgènes), non cytotoxique conventionnel |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 100 interactions ont été recensées ; les 20 premières sont de niveau modéré, à l'exception de trois interactions **majeures** : bupropion, dolasétron et éliglustat. Interactions modérées notamment avec : famotidine, rabéprazole, oméprazole, hydrocortisone, dexaméthasone, alosétron, alvimopan, lopéramide, aprépitant, clarithromycine, chlorpropamide, saxagliptine, empagliflozine, linagliptine, bisacodyl, acide picosulfurique et polyéthylène glycol.

Les mises en garde et contre-indications de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction de rang 1 correspond à une catégorie de susceptibilité génétique, non traitable, sans lien mécanistique avec le cancer du cerveau ; les autres prédictions (tumeurs bénignes de la prostate, tumeur de Brenner) n'ont aucune preuve (L5). Le niveau L1 du rang 6 provient des essais de phase 3 dans le cancer de la prostate, indication déjà établie : il ne démontre aucune nouvelle opportunité de repositionnement. De plus, la seule AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde, contre-indications), lacune bloquante pour le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Identifier une indication réellement nouvelle et traitable, avec une justification biologique de la dépendance à la voie AR (par exemple, cancers non prostatiques exprimant l'AR)
- Compléter l'analyse des 36 essais et 20 publications (seule une partie a été examinée)
- Clarifier le statut réglementaire en France (AMM annulée) et la compatibilité des voies d'administration
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

