---
layout: default
title: Probenecid
parent: Prédiction du modèle uniquement (L5)
nav_order: 633
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Probenecid : nouvelle indication prédite, Hypouricémie rénale (niveau de preuve L5). Indication d'origine : Goutte, hyperuricémie"
monitor_inn: "probenecid"
predicted_indications: ["hypouricemia, renal", "Lesch-Nyhan syndrome", "hypoxanthine guanine phosphoribosyltransferase partial deficiency"]
---

# Probenecid
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

# Probénécide : De la goutte à l'hypouricémie rénale

## Résumé en Une Phrase

Le probénécide est un uricosurique initialement utilisé pour traiter la goutte et l'hyperuricémie.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypouricémie rénale**, mais cette prédiction est très probablement un faux positif : le mécanisme du médicament va dans le sens contraire de la physiopathologie de la maladie.
Aucun essai clinique n'est enregistré, et **20 publications** ont été retrouvées, dont aucune ne démontre un bénéfice du probénécide dans cette maladie.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Goutte, hyperuricémie (source : graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Hypouricémie rénale |
| Score de Prédiction TxGNN | 99,73 % |
| Niveau de Preuve | L5 (prédiction du modèle sans étude clinique ; le niveau L4 attribué dans les données compilées reflète des études mécanistiques et physiologiques) |
| Statut de Marché en France | Uniquement annulée (AMM annulée) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les sources compilées. D'après les connaissances pharmacologiques établies, le probénécide inhibe le transporteur URAT1 (SLC22A12) ainsi que OAT1 et OAT3. Il réduit ainsi la réabsorption tubulaire rénale de l'urate et augmente son excrétion urinaire, ce qui explique son usage dans la goutte.

Le lien avec l'hypouricémie rénale est donc évident sur le plan du réseau de connaissances : la maladie résulte d'une perte de fonction d'URAT1 (ou de GLUT9), avec une excrétion excessive d'urate et une uricémie basse. Le score élevé reflète probablement cette proximité (métabolisme de l'acide urique, transporteur URAT1) et non un bénéfice thérapeutique.

Le mécanisme du probénécide reproduit la physiopathologie de la maladie au lieu de la corriger. Une action uricosurique supplémentaire aggraverait le phénotype et pourrait augmenter le risque d'insuffisance rénale aiguë d'effort et de lithiase urinaire. Le lien est pertinent mécanistiquement, mais **directionnellement contre-indiqué**.

Les deux autres prédictions (syndrome de Lesch-Nyhan, déficit partiel en HPRT) reposent aussi uniquement sur la proximité avec la goutte et l'hyperuricémie. Elles ne sont soutenues par aucun essai clinique. Dans ces maladies, les inhibiteurs de la xanthine oxydase (allopurinol) sont préférés, car les uricosuriques augmentent la charge urinaire en acide urique et le risque de néphrolithiase.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Les publications ci-dessous sont les plus pertinentes parmi les 20 retrouvées. Il s'agit de revues, d'une analyse génétique de cohorte et de rapports de cas ; aucun essai randomisé. Le probénécide y apparaît surtout comme outil diagnostique (test de réponse uricosurique), non comme traitement.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cohorte (analyse génétique) | J Am Soc Nephrol | Analyse de SLC22A12 chez 32 patients japonais : les mutations d'URAT1 causent l'hypouricémie rénale |
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Revue | Mol Genet Metab | L'hypouricémie rénale héréditaire est due le plus souvent à une perte de fonction d'URAT1 |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Revue narrative | Clin Rheumatol | Mise à jour pour le rhumatologue sur les causes de l'hypouricémie |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Revue / cas | Am J Kidney Dis | Prévention de l'insuffisance rénale aiguë d'effort chez un patient avec hypouricémie rénale |
| [854144](https://pubmed.ncbi.nlm.nih.gov/854144/) | 1977 | Série de cas | Nephron | Réponse atténuée de la clairance de l'acide urique au probénécide et au pyrazinamide : défaut tubulaire de réabsorption |
| [8533596](https://pubmed.ncbi.nlm.nih.gov/8533596/) | 1995 | Cas | Acta Paediatr Jpn | Insuffisance rénale aiguë après effort chez un adolescent ; les tests probénécide/pyrazinamide montrent un défaut total |
| [2709741](https://pubmed.ncbi.nlm.nih.gov/2709741/) | 1989 | Cas | Klin Wochenschr | Insuffisance rénale aiguë par néphropathie uratique ; excrétion augmentée par le probénécide |
| [8302413](https://pubmed.ncbi.nlm.nih.gov/8302413/) | 1993 | Cas | Nephron | Hypouricémie avec lithiase ; le probénécide augmente la clairance de l'urate ; traitement par alcalinisation des urines |
| [3808147](https://pubmed.ncbi.nlm.nih.gov/3808147/) | 1987 | Cas familial | Nephron | Hypouricémie familiale avec réabsorption préservée ; réponse nette au probénécide |
| [14747372](https://pubmed.ncbi.nlm.nih.gov/14747372/) | 2004 | Étude préclinique | J Am Soc Nephrol | Fonction et localisation d'URAT1 dans le rein de souris |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68335966 | SANTURIL 500 mg, comprimé sécable (LIPOMED, Allemagne) | Comprimé sécable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) :
  - Insuffisance hépatique, maladie rénale et insuffisance de la fonction rénale, pyo-uretère
  - Maladies hématologiques : thrombocytopénie, leucopénie, agranulocytose, neutropénie (dont formes congénitales et cycliques)
  - Ulcère gastroduodénal
  - Atteintes musculaires : myopathie, rhabdomyolyse, paralysie périodique familiale
  - Affections digestives : diarrhée, colite à *Clostridium difficile*, entérocolite nécrosante périnatale
- **Interactions médicamenteuses** (71 interactions recensées ; principales) :
  - **Majeures** : phénylbutyrate, phénylbutyrate de glycérol
  - **Modérées** : acide acétylsalicylique, sulfamides hypoglycémiants (chlorpropamide, glimépiride, glipizide, glibenclamide, tolazamide, tolbutamide, acétohexamide), glinides (répaglinide, natéglinide)
  - **Mineures** : famotidine, amoxicilline, lévofloxacine, éluxadoline

Pour la contre-indication rénale, le risque est particulièrement pertinent ici : une uricosurie accrue peut favoriser l'insuffisance rénale aiguë d'effort et la lithiase chez les patients atteints d'hypouricémie rénale.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le mécanisme uricosurique du probénécide aggraverait l'hypouricémie rénale au lieu de la corriger. La prédiction est probablement un faux positif, sans essai clinique, et l'AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les avertissements et contre-indications de la notice officielle de l'ANSM (données bloquantes pour le criblage de sécurité)
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Une revue de la pertinence des publications retrouvées, dont la pertinence reste à évaluer
- Une réévaluation des prédictions alternatives (Lesch-Nyhan, déficit partiel en HPRT) uniquement si des preuves cliniques apparaissent, sachant que l'allopurinol reste le traitement de référence
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

