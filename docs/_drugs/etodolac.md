---
layout: default
title: Etodolac
parent: Prédiction du modèle uniquement (L5)
nav_order: 306
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Etodolac : nouvelle indication prédite, Spondylarthrite ankylosante (candidate n° 6 du classement (niveau de preuve L5). Indication d'origine : Polyarthrite rhumatoïde, arthrose, arthropathies…"
monitor_inn: "etodolac"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "inflammatory spondylopathy"]
---

# Etodolac
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

# Étodolac : De la polyarthrite rhumatoïde à la spondylarthrite ankylosante

## Résumé en Une Phrase

L'étodolac est un anti-inflammatoire non stéroïdien (AINS) utilisé à l'origine dans les maladies rhumatismales : polyarthrite rhumatoïde, arthrose et arthropathies.
Le modèle TxGNN prédit qu'il pourrait être utile pour la **spondylarthrite ankylosante** (prédiction la plus pertinente cliniquement parmi les candidats), mais cette indication est très proche de ses usages déjà connus.
Les données compilées font état de **0 essai clinique** enregistré et de **8 publications** (revues narratives, études ouvertes, surveillance post-commercialisation et une recommandation méthodologique) : le niveau de preuve reste faible.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Polyarthrite rhumatoïde, arthrose, arthropathies, arthrite juvénile idiopathique, spondylarthropathie (texte d'indication de l'AMM non disponible) |
| Nouvelle Indication Prédite | Spondylarthrite ankylosante (candidate n° 6 du classement ; la candidate n° 1 du modèle est la dysplasie acromésomélique de type Hunter-Thompson) |
| Score de Prédiction TxGNN | 99,93 % (spondylarthrite ankylosante) ; 99,97 % pour la dysplasie acromésomélique, jugée sans lien mécanistique plausible |
| Niveau de Preuve | L4 (spondylarthrite ankylosante) ; L5 pour la plupart des autres candidates |
| Statut de Marché en France | Uniquement AMM annulée |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold (maintien en attente) ; question de recherche pour la spondylarthrite ankylosante |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les informations connues et la littérature, l'étodolac est un AINS à sélectivité préférentielle pour la cyclo-oxygénase-2 (COX-2). Il réduit la production de prostaglandines, médiateurs de l'inflammation et de la douleur.

Les AINS constituent le traitement de première intention de la spondylarthrite ankylosante : l'inhibition de la COX diminue la douleur lombaire inflammatoire et la raideur. L'étodolac est déjà associé à la spondylarthropathie parmi ses indications d'origine. Cette prédiction relève donc davantage d'une extension d'un usage de classe ou quasi-AMM que d'un véritable repositionnement.

**Une mise en garde importante :** les scores TxGNN les plus élevés (dysplasie acromésomélique, syndrome brachyolmie-amélogenèse imparfaite, myosclérose, brachyolmie, pseudoachondroplasie) concernent des maladies génétiques rares du squelette ou du tissu conjonctif. Aucun lien mécanistique crédible n'a été identifié : l'inhibition de la COX ne corrige pas un défaut de signalisation de facteurs de croissance. Ces scores reflètent vraisemblablement la proximité dans le graphe de connaissances avec des phénotypes articulaires ou squelettiques, et non une relation pharmacologique réelle. La « spondylarthropathie, susceptibilité à » est un doublon ontologique de l'indication d'origine. La vascularite rhumatoïde et l'hypermobilité du coccyx n'offrent, au mieux, qu'un soulagement symptomatique générique, sans preuve spécifique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Ces publications portent sur la spondylarthrite ankylosante et la spondylopathie inflammatoire (jeu de références identique).

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [1717225](https://pubmed.ncbi.nlm.nih.gov/1717225/) | 1991 | Revue | Drugs | Étodolac efficace dans la polyarthrite rhumatoïde, l'arthrose et la spondylarthrite ankylosante ; au moins aussi efficace que les autres AINS ; effets indésirables dominés par douleurs abdominales et dyspepsie |
| [22071858](https://pubmed.ncbi.nlm.nih.gov/22071858/) | 2011 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | Sécurité des AINS, aspirine et paracétamol chez les patients sous méthotrexate pour arthrite inflammatoire (étude non spécifique à l'étodolac) |
| [2146130](https://pubmed.ncbi.nlm.nih.gov/2146130/) | 1990 | Revue (synthèse d'études randomisées en double aveugle) | Eur J Rheumatol Inflamm | Étodolac comparable au naproxène et au piroxicam dans la polyarthrite rhumatoïde et l'arthrose ; la spondylarthrite ankylosante est également étudiée |
| [17694363](https://pubmed.ncbi.nlm.nih.gov/17694363/) | 1997 | Revue | Inflammopharmacology | Analgésique polyvalent à effet sélectif sur la COX-2, utilisé dans les arthrites inflammatoires dont la spondylarthrite ankylosante |
| [2525800](https://pubmed.ncbi.nlm.nih.gov/2525800/) | 1989 | Étude ouverte | Rev Med Interne | 4 947 patients (polyarthrite rhumatoïde, spondylarthrite ankylosante, arthrose) suivis par 974 rhumatologues : évaluation de l'efficacité et de la tolérance de Lodine 200 |
| [2150569](https://pubmed.ncbi.nlm.nih.gov/2150569/) | 1990 | Essai ouvert (sécurité) | Rheumatol Int | Deux grandes études françaises, dont une de sécurité post-commercialisation (51 355 patients) |
| [2150568](https://pubmed.ncbi.nlm.nih.gov/2150568/) | 1990 | Surveillance post-commercialisation | Rheumatol Int | 4 études de surveillance (Italie, Suisse, Royaume-Uni, France), 8 334 patients, profil de sécurité favorable |
| [20829199](https://pubmed.ncbi.nlm.nih.gov/20829199/) | 2011 | Recommandation | Ann Rheum Dis | Recommandations ASAS pour recueillir et analyser la prise d'AINS dans les essais sur la spondylarthrite axiale (méthodologique) |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68645185 | LODINE 200 mg, comprimé pelliculé (Laboratoires Ethypharm) | Comprimé pelliculé | Non disponible (AMM annulée) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité (les mises en garde et contre-indications du résumé des caractéristiques du produit ne sont pas disponibles dans les données compilées).

- **Contre-indications issues du graphe de connaissances** (hors texte de notice) : hypertension, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, ulcère gastroduodénal (dont ulcère actif), troubles de la coagulation, infarctus du myocarde et thrombose coronarienne, maladies cardiovasculaires et cardiaques, hémoglobinopathie, pyo-uretère. Ce profil est cohérent avec les risques connus des AINS (digestifs, rénaux, cardiovasculaires).
- **Interactions médicamenteuses** : 221 interactions recensées. Parmi les principales :
  - Modérées : corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), acide acétylsalicylique, mésalazine, balsalazide, metformine, sulfamides hypoglycémiants (glimépiride, chlorpropamide), répaglinide, sels de potassium (citrate, bicarbonate), picosulfate, polyéthylène glycol.
  - Mineures : famotidine, ranitidine, cimétidine, linaclotide.
- Chez les patients sous méthotrexate, l'usage concomitant d'AINS nécessite une évaluation spécifique de la sécurité (revue Cochrane citée ci-dessus).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucune des candidates ne dispose d'essai clinique enregistré. Les scores les plus élevés correspondent à des maladies génétiques rares sans lien mécanistique crédible (artefacts probables du graphe). La spondylarthrite ankylosante et la spondylopathie inflammatoire (niveau L4) restent des questions de recherche : elles s'inscrivent dans l'usage connu des AINS, avec des preuves indirectes ou de faible niveau. L'AMM française est annulée, ce qui limite la portée pratique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer le résumé des caractéristiques du produit (mises en garde, contre-indications) auprès de l'ANSM : donnée bloquante pour le dépistage de sécurité.
- Obtenir les données sur le mécanisme d'action depuis DrugBank.
- Vérifier la disponibilité actuelle de l'étodolac en France (AMM annulée) ou dans d'autres juridictions.
- Rechercher des essais contrôlés randomisés spécifiques à l'étodolac dans la spondylarthrite ankylosante, ou comparer à d'autres AINS déjà recommandés.
- Écarter formellement les candidates génétiques rares sans fondement mécanistique, sauf nouvelle preuve indépendante.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

