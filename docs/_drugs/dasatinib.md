---
layout: default
title: Dasatinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 101
evidence_level: L5
indication_count: 10
---

# Dasatinib
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

# Dasatinib : De la leucémie myéloïde chronique (LMC) au sarcome d'Ewing

## Résumé en Une Phrase

Dasatinib est un inhibiteur de tyrosine kinase multi-cibles, utilisé à l'origine dans la leucémie myéloïde chronique (LMC) et la leucémie aiguë lymphoblastique à chromosome Philadelphie (LAL Ph+).
Le modèle TxGNN prédit qu'il pourrait être efficace dans le **sarcome d'Ewing**.
Cette piste repose sur **3 essais cliniques** (dont 2 testant réellement le dasatinib) et **9 publications** (dont 7 pertinentes, surtout précliniques). Aucun essai randomisé n'existe dans cette indication.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | LMC et LAL Ph+ (d'après la littérature du dossier ; le texte d'indication de l'ANSM n'est pas renseigné) |
| Nouvelle Indication Prédite | Sarcome d'Ewing |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L4 (le dossier indique L2, mais aucun ECR de phase 2/3 terminé n'existe dans cette indication ; voir ci-dessous) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans DrugBank. Le dossier indique toutefois que le dasatinib inhibe fortement BCR-ABL et les kinases de la famille SRC, y compris dans des clones résistants à l'imatinib.

Dans le sarcome d'Ewing, la signalisation SRC/FAK favorise la formation d'invadopodes, la migration et l'invasion des cellules tumorales. Le dasatinib montre in vitro une activité antiproliférative et antimigratoire sur des lignées de sarcome d'Ewing. Le lien mécanistique est donc plausible, mais il concerne surtout l'invasion et la métastase, plutôt qu'un effet cytotoxique direct.

Cette plausibilité biologique n'a pas été confirmée cliniquement. Une revue de 2022 rapporte qu'un essai de phase 2 dans les sarcomes avancés a échoué en monothérapie dans les sous-types Ewing et rhabdomyosarcome. L'activité attendue en monothérapie est modeste, et la logique biologique soutient plutôt des stratégies anti-invasion ou en association.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminé prématurément | 7 | Dasatinib + ifosfamide, carboplatine, étoposide en pédiatrie. Trop peu de patients pour conclure sur l'efficacité |
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Terminé | 366 | Dasatinib dans les sarcomes avancés (taux de réponse, survie sans progression à 6 mois). Les données de la cohorte Ewing ne sont pas visibles dans le dossier |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Phase 1 | En recrutement | 41 | CAR-T anti-B7-H3 chez l'enfant et le jeune adulte (tumeurs solides). Le dasatinib n'est pas l'intervention ; contexte uniquement |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Préclinique / revue | Sarcoma | Ciblage du complexe FAK-Src dans les sarcomes ; le dasatinib seul a échoué dans un essai de phase 2 (Ewing, rhabdomyosarcome) |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Revue | Oncol Lett | Importance de la signalisation Src dans les sarcomes ; Src considérée comme cible thérapeutique potentielle |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Préclinique | Neoplasia | Ténascine C et Src coopèrent pour la formation d'invadopodes dans le sarcome d'Ewing |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Préclinique | Neoplasia | Le stress microenvironnemental active l'invasion et la migration via Src dans le sarcome d'Ewing |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Préclinique | Oncol Rep | Activité antiproliférative et antimigratoire du dasatinib sur des lignées de neuroblastome et de sarcome d'Ewing |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Préclinique | Cancer Res | Le dasatinib inhibe la migration et l'invasion de lignées de sarcome et induit l'apoptose dans les sarcomes osseux dépendants de SRC |
| [29776413](https://pubmed.ncbi.nlm.nih.gov/29776413/) | 2018 | Préclinique | Cell Commun Signal | Le plérixafor (et non le dasatinib) favorise la prolifération de lignées d'Ewing ; contexte uniquement |

Deux autres références récupérées (chondrosarcome, cas de LMC en crise blastique) ne concernent pas directement cette indication et ne sont pas listées.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Fabricant |
|---------|------|------|-----------|
| 60926629 | DASATINIB SANDOZ 100 mg | Comprimé pelliculé | SANDOZ |
| 64498745 | DASATINIB KRKA 100 mg | Comprimé pelliculé | KRKA (Slovénie) |
| 61237544 | DASATINIB BIOGARAN 50 mg | Comprimé pelliculé | BIOGARAN |
| 66031135 | DASATINIB VIATRIS 20 mg | Comprimé pelliculé | VIATRIS SANTE |
| 63719525 | DASATINIB ZENTIVA 100 mg | Comprimé pelliculé | ZENTIVA FRANCE |

Ce tableau présente 5 des 20 AMM. Les textes d'indication approuvée ne sont pas renseignés dans les données reçues.

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase BCR-ABL/SRC) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Les mises en garde et contre-indications de l'ANSM ne figurent pas dans les données reçues, et aucune interaction médicamenteuse n'a été trouvée.

La littérature du dossier signale néanmoins, chez des patients atteints de LMC traités par dasatinib :
- **Atteintes pleurales et pulmonaires** : épanchement pleural, chylothorax et pneumopathie interstitielle (PMID 36448074, 36346055).
- **Grossesse** : risque à prendre en compte (PMID 36763239).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les preuves dans le sarcome d'Ewing sont essentiellement précliniques. Le seul essai avec dasatinib dans cette indication précise a été arrêté avec 7 patients. L'essai de phase 2 multi-histologies (n=366) n'a pas d'efficacité démontrée en monothérapie pour Ewing, et il s'agit d'un essai à un seul bras, non d'un ECR : le niveau L4 est donc retenu.
- Le dossier signale aussi un point bloquant : les mises en garde et contre-indications de l'ANSM sont manquantes, ce qui empêche le passage au criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde, contre-indications, interactions).
- Obtenir le mécanisme d'action détaillé via l'API DrugBank.
- Vérifier les résultats de la cohorte sarcome d'Ewing de NCT00464620 avant toute progression.
- Explorer des stratégies d'association (anti-invasion/anti-métastase) plutôt que la monothérapie.
- Prévoir un plan de surveillance pleuro-pulmonaire si le projet progresse.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

