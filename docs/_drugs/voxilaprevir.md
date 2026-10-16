---
layout: default
title: Voxilaprevir
parent: Prédiction du modèle uniquement (L5)
nav_order: 823
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Voxilaprevir : nouvelle indication prédite, Infection par le virus de l'hépatite B (niveau de preuve L5). Indication d'origine : Infection chronique par le virus de l'hépatite C"
monitor_inn: "voxilaprevir"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis, viral, animal", "hepatitis A virus infection", "Omsk hemorrhagic fever", "Kyasanur forest disease", "HIV infectious disease", "chronic hepatitis B virus infection", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome"]
---

# Voxilaprevir
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

# Voxilaprevir : De l'hépatite C chronique à l'infection par le virus de l'hépatite B

## Résumé en Une Phrase

Voxilaprevir est un inhibiteur de la protéase NS3/4A du virus de l'hépatite C (VHC). Il est commercialisé en association avec le sofosbuvir et le velpatasvir (VOSEVI) et était initialement utilisé pour traiter l'infection chronique par le VHC.
Le modèle TxGNN prédit qu'il pourrait être efficace contre l'**infection par le virus de l'hépatite B**, mais **aucun essai clinique** n'est associé à cette indication. Les **9 publications** retrouvées portent toutes sur l'hépatite C (retraitement, résistance, prix, épidémiologie) et ne testent pas le voxilaprevir contre le VHB.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection chronique par le virus de l'hépatite C (source : graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Infection par le virus de l'hépatite B |
| Score de Prédiction TxGNN | 99,84 % |
| Niveau de Preuve | L4 (selon l'évaluation compilée ; aucune étude ne teste le voxilaprevir contre le VHB, ce qui correspond en pratique à une prédiction seule) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances générales, le voxilaprevir est un inhibiteur de la protéase NS3/4A du VHC. Son efficacité dans l'hépatite C chronique est établie, notamment en retraitement après échec d'autres antiviraux à action directe.

Le lien mécanistique avec l'hépatite B est faible. Le VHB est un virus à ADN qui se réplique par transcription inverse et ne possède aucune protéase de type NS3/4A. Il n'existe donc pas de cible commune évidente.

Le score très élevé de TxGNN reflète probablement la proximité, dans le réseau de connaissances, entre les antiviraux et les maladies hépatiques virales, plutôt qu'une plausibilité pharmacologique. Cette prédiction doit être considérée comme une hypothèse de recherche et non comme une piste thérapeutique étayée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Les neuf publications retrouvées concernent l'hépatite C. Aucune ne teste le voxilaprevir contre le VHB ; ce dernier n'apparaît que comme sujet associé (prix, enquêtes sur les infections hématogènes).

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | Étude de cohorte (essai à bras unique) | Lancet Gastroenterol Hepatol | Retraitement par sofosbuvir-velpatasvir-voxilaprevir de l'hépatite C après échec d'un antiviral à action directe au Rwanda (SHARED-3) |
| [36535062](https://pubmed.ncbi.nlm.nih.gov/36535062/) | 2022 | Étude de cohorte | J Gastrointestin Liver Dis | Efficacité et sécurité en vie réelle chez des patients roumains de génotype 1b non répondeurs aux antiviraux |
| [40611935](https://pubmed.ncbi.nlm.nih.gov/40611935/) | 2025 | Étude de cohorte | J Clin Exp Hepatol | Substitutions associées à la résistance et facteurs prédictifs d'échec dans une cohorte d'élimination du VHC |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Revue | Semin Liver Dis | Retraitement des patients en échec des antiviraux à action directe |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Revue | Clin Pharmacokinet | Considérations pharmacocinétiques et pharmacodynamiques du traitement de l'hépatite C (mise à jour 2019) |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Revue (compte rendu de congrès) | AIDS Rev | Compte rendu de la conférence internationale sur les hépatites virales 2017 |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | Étude de mécanisme | Hepatology | Voies évolutives de persistance des variants du VHC résistants aux inhibiteurs de protéase |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Étude transversale | Ann Hepatol | Comparaison mondiale des prix des traitements des hépatites B et C |
| [41570233](https://pubmed.ncbi.nlm.nih.gov/41570233/) | 2025 | Étude de cohorte | Vopr Virusol | Prévalence des marqueurs du VIH, du VHB et du VHC chez des patients en cabinet dentaire |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61932485 | VOSEVI 400 mg/100 mg/100 mg, comprimé pelliculé (GILEAD SCIENCES IRELAND UC, Irlande) | Comprimé pelliculé | Non renseignée (AMM annulée) |

## Considérations de Sécurité

**Interactions médicamenteuses** : 19 interactions ont été identifiées, dont 3 de niveau majeur et 16 de niveau modéré.

- **Majeures** : rosuvastatine, edoxaban, ciclosporine.
- **Modérées** : éluxadoline, acide obéticholique, cobicistat, apixaban, eltrombopag, artésunate, afatinib, bosutinib, cobimétinib, éthinylestradiol, idélalisib, lapatinib, lenvatinib, olaparib, pazopanib, tériflunomide.

Pour les mises en garde et les contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucune cible commune plausible n'existe entre la protéase NS3/4A du VHC et le VHB, et aucun essai ni aucune publication ne teste le voxilaprevir contre l'hépatite B. Le score élevé de TxGNN reflète vraisemblablement une proximité dans le réseau de connaissances.
- La seule AMM française est annulée, ce qui limite aussi la faisabilité d'un repositionnement en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action du voxilaprevir
- Données de sécurité issues de la notice (mises en garde et contre-indications)
- Données précliniques (activité in vitro contre le VHB) avant tout essai clinique
- Vérification du statut réglementaire actuel du produit en France

**Autres pistes prédites (pour information) :** les autres indications prédites (hépatite E, hépatite A, fièvre hémorragique d'Omsk, maladie de la forêt de Kyasanur, VIH, hépatite B chronique, VIS, SIDA félin) reposent sur la prédiction seule ou sur une littérature qui ne démontre aucune activité contre la maladie ciblée. Elles ne justifient pas, en l'état, de recommandation autre que « Hold ». Pour le VIH, la littérature concerne le traitement du VHC chez des patients co-infectés, et non une activité anti-VIH.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

