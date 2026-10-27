---
layout: default
title: Caplacizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 136
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Caplacizumab : nouvelle indication prédite, Purpura thrombotique thrombocytopénique (PTT)… (niveau de preuve L5). Indication d'origine : Purpura thrombopénique"
monitor_inn: "CAPLACIZUMAB"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "fetal and neonatal alloimmune thrombocytopenia", "hemophilia", "platelet-type bleeding disorder"]
---

# Caplacizumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

## Caplacizumab : Du Purpura Thrombopénique à la Purpura Thrombotique Thrombocytopénique
{: .text-alpha }

## Resume en Une Phrase

Caplacizumab est un nanocorps anti-facteur von Willebrand (vWF), initialement utilisé pour le traitement du purpura thrombopénique.
Le modèle TxGNN prédit en premier lieu des indications hémorragiques (troubles plaquettaires), mais la seule prédiction étayée par des preuves est le **purpura thrombotique thrombocytopénique (PTT)**, qui correspond en réalité à l'indication d'origine du médicament, avec **8 essais cliniques** et **19 publications** recensés.
Les autres prédictions n'ont aucune preuve réelle et sont mécanistiquement peu plausibles.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Purpura thrombopénique (selon le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Predite | Purpura thrombotique thrombocytopénique (PTT), rang 5 des prédictions. Le rang 1 du modèle est le « trouble primaire de la libération plaquettaire » (L5, Hold) |
| Score de Prediction TxGNN | 99,996 % (PTT) ; 99,9998 % (rang 1) |
| Niveau de Preuve | L1 (PTT) |
| Statut de Marche en France | Annulée uniquement (AMM annulée) |
| Nombre d'AMM | 1 (0 valide, 1 annulée) |
| Decision Recommandee | Proceed with Guardrails (PTT, indication déjà existante) ; Hold pour les 9 autres prédictions |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les sources compilées. D'après la littérature, caplacizumab est un nanocorps humanisé dirigé contre le domaine A1 du facteur von Willebrand. Il bloque l'interaction entre les multimères ultra-larges de vWF et le récepteur plaquettaire GPIb-IX-V, ce qui empêche l'agrégation plaquettaire dans la microcirculation.

Dans le PTT immun, le déficit en ADAMTS13 laisse ces multimères de vWF s'accumuler, d'où une microthrombose, une thrombopénie et une anémie hémolytique. Le PTT est donc cohérent avec l'indication d'origine : il ne s'agit pas d'un véritable repositionnement, mais d'une confirmation de l'usage actuel.

Pour les autres prédictions (maladie de Glanzmann, pseudo-maladie de von Willebrand, syndrome de Scott, hémophilie, etc.), le mécanisme va à l'inverse : ce sont des troubles hémorragiques, et inhiber l'adhésion plaquettaire médiée par le vWF risquerait d'aggraver le saignement. Ces scores élevés reflètent vraisemblablement la proximité dans le graphe avec les termes « plaquettes » ou « thrombopénie », et non une plausibilité thérapeutique. Pour l'hémophilie, les 19 publications associées portent en réalité sur le PTT et ne constituent pas une preuve.

---

## Preuves d'Essais Cliniques

Essais relatifs au PTT (prédiction de rang 5). Aucun essai n'est enregistré pour les neuf autres indications prédites.

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT02553317](https://clinicaltrials.gov/study/NCT02553317) | Phase 3 | Terminé | 145 | HERCULES : essai randomisé en double aveugle contre placebo dans le PTT acquis ; essai pivot visant une normalisation plus rapide du taux de plaquettes |
| [NCT02878603](https://clinicaltrials.gov/study/NCT02878603) | Phase 3 | Terminé | 104 | Post-HERCULES : suivi à long terme de la sécurité et de l'efficacité, y compris la réutilisation |
| [NCT05468320](https://clinicaltrials.gov/study/NCT05468320) | Phase 3 | Terminé | 51 | Étude ouverte à un bras : caplacizumab + immunosuppresseurs sans échange plasmatique en première ligne dans le PTT immun |
| [NCT04074187](https://clinicaltrials.gov/study/NCT04074187) | Phase 2/3 | Terminé | 21 | Étude ouverte chez des patients japonais atteints de PTT acquis ; prévention des récidives |
| [NCT01151423](https://clinicaltrials.gov/study/NCT01151423) | Phase 2 | Terminé | 75 | TITAN : essai randomisé en simple aveugle contre placebo, nanocorps anti-vWF en complément des échanges plasmatiques |
| [NCT04720261](https://clinicaltrials.gov/study/NCT04720261) | Phase 2 | Interrompu | 58 | Schéma de caplacizumab personnalisé selon l'activité d'ADAMTS13 ; étude de non-infériorité à un bras |
| [NCT05263193](https://clinicaltrials.gov/study/NCT05263193) | N/A | Terminé | 4 | Collecte rétrospective de données chez des enfants atteints de PTT immun |
| [NCT05785468](https://clinicaltrials.gov/study/NCT05785468) | N/A | Inconnu | 1 | ROSCAPLI : étude rétrospective observationnelle italienne dans le PTT acquis |

---

## Preuves de la Litterature

Publications sélectionnées parmi celles liées au PTT (prédiction de rang 5). Les 19 publications de l'hémophilie portent sur le PTT et ne sont pas retenues comme preuve.

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [30625070](https://pubmed.ncbi.nlm.nih.gov/30625070/) | 2019 | Essai clinique (HERCULES) | N Engl J Med | Caplacizumab inhibite l'interaction entre les multimères de vWF et les plaquettes dans le PTT acquis |
| [26863353](https://pubmed.ncbi.nlm.nih.gov/26863353/) | 2016 | ECR (TITAN) | N Engl J Med | Caplacizumab dans le PTT acquis, en complément des échanges plasmatiques et de l'immunosuppression |
| [33881463](https://pubmed.ncbi.nlm.nih.gov/33881463/) | 2021 | Analyse intégrée | Blood Adv | Analyse combinée TITAN/HERCULES : moins de décès et moins de PTT réfractaire sous caplacizumab |
| [36138517](https://pubmed.ncbi.nlm.nih.gov/36138517/) | 2022 | Suivi long terme | J Thromb Haemost | Post-HERCULES : sécurité et efficacité à long terme, y compris la réutilisation |
| [32914526](https://pubmed.ncbi.nlm.nih.gov/32914526/) | 2020 | Recommandations | J Thromb Haemost | Recommandations ISTH pour le traitement du PTT |
| [40533296](https://pubmed.ncbi.nlm.nih.gov/40533296/) | 2025 | Recommandations | J Thromb Haemost | Mise à jour ciblée 2025 des recommandations ISTH, PTT immun et congénital |
| [40235949](https://pubmed.ncbi.nlm.nih.gov/40235949/) | 2025 | Cohorte rétrospective | EClinicalMedicine | Projet Capla 1000+ : utilisation du caplacizumab dans le PTT immun, impact sur la mortalité et délai d'initiation |
| [38838300](https://pubmed.ncbi.nlm.nih.gov/38838300/) | 2024 | Étude rétrospective | Blood | Prise en charge du PTT immun sans échange plasmatique (42 épisodes, Autriche et Allemagne) |
| [32634236](https://pubmed.ncbi.nlm.nih.gov/32634236/) | 2020 | Données en vie réelle | Blood Adv | 60 patients en Allemagne : efficacité confirmée du caplacizumab |
| [40388146](https://pubmed.ncbi.nlm.nih.gov/40388146/) | 2025 | Revue | JAMA | Revue sur le PTT immun |

---

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 64183564 | CABLIVI 10 mg, poudre et solvant pour solution injectable (statut : annulée) | Poudre et solvant pour solution injectable | Non renseignée |

---

## Considerations de Securite

- **Interactions Medicamenteuses** : 100 interactions recensées, dont plusieurs de niveau majeur, principalement liées à un risque hémorragique accru :
  - Majeures : acide acétylsalicylique, abciximab, alteplase, fondaparinux, anagrélide, acalabrutinib, déférasirox, trastuzumab emtansine, ibritumomab tiuxétan, tositumomab
  - Modérées : ibuprofène, kétorolac, célécoxib, diclofénac (topique), fluvoxamine, fenfluramine, dexfenfluramine, sibutramine
- **Risque hémorragique** : le mécanisme d'action (inhibition de l'adhésion plaquettaire médiée par le vWF) rend le saignement préoccupant, surtout dans les troubles hémorragiques prédits par le modèle.

Les mises en garde et contre-indications officielles ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Etapes

**Decision : Proceed with Guardrails (PTT) / Hold (neuf autres prédictions)**

**Justification :**
- Pour le PTT, les preuves sont de niveau L1 (essais de phase 3, dont HERCULES, et suivis à long terme), mais il s'agit de l'indication d'origine et non d'un nouveau repositionnement. Le statut « annulée uniquement » de l'AMM française impose de vérifier la disponibilité réelle du produit.
- Les autres prédictions (troubles plaquettaires, hémophilie, etc.) sont de niveau L5, sans essai ni publication pertinente, et le mécanisme suggère un risque d'aggravation des saignements ; il ne faut pas les poursuivre.

**Pour avancer, les elements suivants sont necessaires :**
- Obtenir la notice ANSM (mises en garde et contre-indications), lacune bloquante pour le dépistage de sécurité
- Compléter les données sur le mécanisme d'action via DrugBank
- Vérifier la disponibilité actuelle du produit en France (AMM annulée) et le texte de l'indication approuvée
- Garde-fous cliniques : association aux échanges plasmatiques et à l'immunosuppression, surveillance du risque hémorragique, durée guidée par l'activité d'ADAMTS13
- Rejeter ou réévaluer les prédictions de troubles hémorragiques, probables faux positifs liés à la proximité dans le graphe
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

