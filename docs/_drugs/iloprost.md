---
layout: default
title: Iloprost
parent: Prédiction du modèle uniquement (L5)
nav_order: 390
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Iloprost : nouvelle indication prédite, Hypotrichose simplex du cuir chevelu (niveau de preuve L5). Indication d'origine : Hypertension artérielle pulmonaire"
monitor_inn: "ILOPROST"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "pulmonary arteriovenous malformation (disease)", "diffuse alopecia areata"]
---

# Iloprost
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

## Iloprost : De l'hypertension artérielle pulmonaire à l'hypotrichose simplex du cuir chevelu
{: .text-alpha }

## Résumé en Une Phrase

Iloprost est un analogue de la prostacycline, initialement utilisé pour le traitement de l'hypertension artérielle pulmonaire (HTAP).
Le modèle TxGNN prédit en première position qu'il pourrait être efficace pour l'**hypotrichose simplex du cuir chevelu**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette prédiction.
En revanche, des sous-groupes de l'HTAP (notamment l'HTAP associée aux cardiopathies congénitales et aux connectivites) disposent de publications, ce qui en fait des pistes plus crédibles.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle pulmonaire (selon le graphe de connaissances TxGNN ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Hypotrichose simplex du cuir chevelu |
| Score de Prédiction TxGNN | 99,45 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, l'iloprost est un analogue stable de la prostacycline : il active les récepteurs IP, augmente l'AMPc, provoque une vasodilatation, inhibe l'agrégation plaquettaire et exerce des effets antiprolifératifs. C'est la base de son usage dans l'HTAP.

Pour l'hypotrichose simplex du cuir chevelu, **aucun lien mécanistique direct n'est établi**. Il s'agit d'un trouble génétique du follicule pileux (variants de CDSN, APCDD1, RPL21). Une amélioration théorique de la perfusion du cuir chevelu ne suffit pas à justifier un effet sur une maladie d'origine génétique. Le score élevé du modèle reflète une proximité dans le graphe de connaissances, non une preuve biologique ou clinique.

Les autres prédictions à score élevé se répartissent en deux groupes :
- **Sous-groupes de l'HTAP** (cardiopathies congénitales, connectivites, schistosomiase, VIH, anémie hémolytique chronique) : mécanisme plausible, mais il s'agit davantage d'une extension de sous-population que d'un véritable repositionnement.
- **Affections non vasculaires** (hypotrichose congénitale avec milia, alopécie areata diffuse, malformation artérioveineuse pulmonaire) : aucun mécanisme soutenu. Pour la malformation artérioveineuse pulmonaire, un vasodilatateur pourrait même aggraver le shunt ou l'hypoxémie.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour l'hypotrichose simplex du cuir chevelu.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'hypotrichose simplex du cuir chevelu.

À titre de comparaison, les prédictions en HTAP disposent de publications (indirectes pour la prédiction principale) :

| Indication prédite | Niveau de preuve | Publications notables |
|------|------|------|
| HTAP associée aux cardiopathies congénitales (rang 3) | L3 | Étude croisée en double aveugle contre placebo sur l'iloprost nébulisé dans le syndrome d'Eisenmenger ([31371115](https://pubmed.ncbi.nlm.nih.gov/31371115/), 2020, pilote) ; cohortes sur l'iloprost inhalé chez l'enfant ([29426959](https://pubmed.ncbi.nlm.nih.gov/29426959/), [24729548](https://pubmed.ncbi.nlm.nih.gov/24729548/)) ; effet sur la fonction ventriculaire droite ([27492657](https://pubmed.ncbi.nlm.nih.gov/27492657/)) |
| HTAP associée aux connectivites (rang 5) | L3 | Résultats à long terme de l'iloprost intraveineux à domicile ([27651181](https://pubmed.ncbi.nlm.nih.gov/27651181/), 2017, cohorte) ; revues ([37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/), [18035518](https://pubmed.ncbi.nlm.nih.gov/18035518/)) ; étude préclinique sur la fibrose ventriculaire droite ([25261325](https://pubmed.ncbi.nlm.nih.gov/25261325/)) |
| HTAP associée à la schistosomiase (rang 6) | L4 | Une seule étude pédiatrique générale, non spécifique ([24729548](https://pubmed.ncbi.nlm.nih.gov/24729548/)) |
| HTAP associée au VIH (rang 7) | L4 | Revues générales sans données spécifiques à l'iloprost ([17195895](https://pubmed.ncbi.nlm.nih.gov/17195895/), [14720012](https://pubmed.ncbi.nlm.nih.gov/14720012/)) |

Aucun essai de phase 3 n'est identifié dans les données compilées pour ces sous-groupes.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69133241 | ILOPROST TEVA 100 microgrammes/mL | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |
| 64341103 | ILOPROST ZENTIVA 100 microgrammes/mL | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |
| 62386427 | ILOMEDINE 0,1 mg/1 ml | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |

Aucune AMM n'est actuellement valide pour une spécialité à base d'iloprost seul dans les données compilées.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique, bronchopneumopathie chronique obstructive (dont forme sévère à début précoce), troubles hypotenseurs, œdème pulmonaire, maladie bronchique.
- **Interactions médicamenteuses** : 100 interactions recensées. Les principales, de niveau modéré, concernent l'épinéphrine, l'acide acétylsalicylique, les inhibiteurs du SGLT2 (canagliflozine, dapagliflozine, empagliflozine, ertugliflozine), l'insuline humaine inhalée, le mannitol, l'éphédrine, la fenfluramine, la dexfenfluramine, la glycérine, la papavérine et la sibutramine. Quelques interactions de niveau inconnu concernent le calcitriol, le pantoprazole, la morphine, la metformine et l'oméprazole.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui n'ont pas pu être obtenues.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction principale (hypotrichose simplex du cuir chevelu) repose uniquement sur le modèle (L5), sans essai, sans publication ni lien mécanistique plausible pour une maladie génétique du follicule pileux.
- Les pistes les plus défendables sont des sous-groupes de l'HTAP (cardiopathies congénitales et connectivites, niveau L3, recommandation « question de recherche »), qui relèvent d'une extension de l'indication d'origine plutôt que d'un repositionnement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice officielle de l'ANSM (mises en garde, contre-indications), un manque bloquant pour toute évaluation de sécurité.
- Obtenir les données sur le mécanisme d'action (DrugBank).
- Vérifier le statut réglementaire, car les 3 AMM françaises sont annulées.
- Pour l'HTAP associée aux cardiopathies congénitales ou aux connectivites : examiner la littérature en texte intégral et définir un protocole d'essai de phase 2/3.
- Évaluer la compatibilité des voies d'administration (perfusion disponible en France ; voie inhalée ou topique non documentée).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

