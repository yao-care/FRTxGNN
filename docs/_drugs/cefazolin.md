---
layout: default
title: Cefazolin
parent: Preuves modérées (L3-L4)
nav_order: 146
evidence_level: L4
indication_count: 8
last_modified_at: 2026-10-14
description: "Cefazolin : nouvelle indication prédite, Otite moyenne infectieuse (niveau de preuve L4). Indication d'origine : Pneumonie bactérienne, cholangite, endocardite, arthrite bactérienne"
monitor_inn: "cefazolin"
predicted_indications: ["infectious otitis media", "bronchitis", "middle ear disease", "chronic otitis media", "suppurative otitis media", "otosalpingitis", "non-suppurative otitis media", "allergic otitis media"]
---

# Cefazolin
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

# Céfazoline : Des infections bactériennes (pneumonie, endocardite, cholangite) à l'otite moyenne infectieuse

## Résumé en Une Phrase

La céfazoline est une céphalosporine de première génération administrée par voie injectable, initialement utilisée contre des infections bactériennes comme les pneumonies (à streptocoques et à staphylocoques), les endocardites, les cholangites et les arthrites bactériennes.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**otite moyenne infectieuse**, mais **aucun essai clinique** n'est enregistré pour cette indication et seules **2 publications** (peu pertinentes) y sont rattachées.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Pneumonie bactérienne, cholangite, endocardite, arthrite bactérienne (d'après le graphe de connaissances ; aucun texte d'indication d'AMM disponible) |
| Nouvelle Indication Prédite | Otite moyenne infectieuse |
| Score de Prédiction TxGNN | 99,44 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 8 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, la céfazoline est une céphalosporine de première génération qui inhibe la synthèse de la paroi bactérienne. Elle est active sur les cocci à Gram positif, notamment les streptocoques et les staphylocoques sensibles à la méticilline.

Ces germes figurent parmi les pathogènes plausibles de l'otite moyenne, ce qui rend le lien biologiquement raisonnable. Les indications d'origine (pneumonies à streptocoques et staphylocoques, endocardite, arthrite bactérienne) reposent sur la même activité antibactérienne.

Plusieurs limites sont toutefois à souligner : la céfazoline n'existe que sous forme injectable, et son activité est limitée contre *H. influenzae* et *M. catarrhalis*, deux agents majeurs de l'otite moyenne. La prédiction reste donc une hypothèse de recherche.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Rapport de cas | Ann Otol Rhinol Laryngol | Syndrome de Gradenigo pédiatrique (complication d'otite moyenne aiguë) traité par une association empirique ceftazidime-céfazoline ; la contribution propre de la céfazoline ne peut être isolée |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Revue | Clin Pharm | Prise en charge du syndrome de Stevens-Johnson ; hors sujet pour cette indication |

Les deux références sont de faible pertinence : l'une est un cas isolé en association, l'autre ne concerne pas l'efficacité de la céfazoline dans l'otite moyenne.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67948546 | CEFAZOLINE VIATRIS 2 g | Poudre pour solution injectable | Non renseignée (AMM annulée) |
| 67504598 | CEFAZOLINE QILU 1 g | Poudre pour solution injectable ou pour perfusion | Non renseignée (AMM annulée) |
| 61876894 | CEFAZOLINE PANPHARMA 1 g | Poudre pour solution injectable ou pour perfusion | Non renseignée (AMM annulée) |
| 69312237 | CEFAZOLINE QILU 2 g | Poudre pour solution injectable ou pour perfusion | Non renseignée (AMM annulée) |
| 60461151 | CEFAZOLINE PANPHARMA 2 g | Poudre pour solution injectable ou pour perfusion | Non renseignée (AMM annulée) |

Au total, 8 AMM sont recensées, toutes annulées ; seules les 5 premières sont listées ici.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : troubles de la coagulation, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, déficit congénital en prothrombine.
- **Interactions médicamenteuses** : 112 interactions recensées. Les interactions de niveau modéré concernent les aminosides (kanamycine, néomycine, streptomycine) et l'acide picosulfurique. D'autres interactions, de niveau non classifié, concernent notamment l'amphotéricine B, l'acide acétylsalicylique, l'amoxicilline, la metformine et l'oméprazole.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose essentiellement sur le score du modèle : aucun essai clinique, et une littérature limitée à un cas en association et à un article hors sujet. Les AMM françaises sont toutes annulées et les données de sécurité officielles manquent.
- Parmi les autres indications prédites, l'otite moyenne suppurée est le signal le plus solide (niveau L3, étude comparative de 1982 cefmétazole vs céfazoline), mais il reste faible et ancien.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice officielle de l'ANSM (mises en garde et contre-indications), actuellement bloquant pour le criblage de sécurité
- Données détaillées sur le mécanisme d'action (DrugBank)
- Études cliniques récentes sur la céfazoline dans l'otite moyenne, avec prise en compte des résistances actuelles et de la couverture d'*H. influenzae*
- Évaluation de la compatibilité de la voie d'administration (injectable uniquement) avec cette indication
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

