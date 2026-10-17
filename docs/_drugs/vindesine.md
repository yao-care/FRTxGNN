---
layout: default
title: Vindesine
parent: Prédiction du modèle uniquement (L5)
nav_order: 815
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Vindesine : nouvelle indication prédite, Ganglioneuroblastome (niveau de preuve L5). Indication d'origine : Leucémie lymphoblastique aiguë"
monitor_inn: "vindesine"
predicted_indications: ["ganglioneuroblastoma (disease)", "vertebral anomalies and variable endocrine and T-cell dysfunction", "neuroblastoma", "retroperitoneal neoplasm"]
---

# Vindesine
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

# Vindésine : De la leucémie lymphoblastique aiguë au ganglioneuroblastome

## Résumé en Une Phrase

La vindésine est un alcaloïde de la pervenche (vinca) antimitotique, initialement utilisé dans le traitement de la leucémie lymphoblastique aiguë, du mélanome et du cancer du poumon.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **ganglioneuroblastome**, mais aucun essai clinique ni aucune publication ne soutient actuellement cette prédiction précise (preuve de niveau **L5**).
Pour la pathologie voisine, le **neuroblastome**, 6 essais cliniques de protocoles multi-agents sont enregistrés, sans confirmation de l'usage de la vindésine. Pour la **leucémie myéloïde**, 20 publications sont disponibles, dont plusieurs études cliniques anciennes.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Leucémie lymphoblastique aiguë (indication issue du graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Ganglioneuroblastome |
| Score de Prédiction TxGNN | 99,89 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, la vindésine appartient à la classe des alcaloïdes de la pervenche, qui inhibent la polymérisation de la tubuline et bloquent la formation du fuseau mitotique. Son efficacité a été décrite dans les leucémies aiguës, et mécanistiquement elle pourrait s'appliquer à des tumeurs à prolifération rapide.

Le ganglioneuroblastome appartient au spectre des tumeurs neuroblastiques, biologiquement apparenté au neuroblastome. La vincristine, proche de la vindésine, fait partie des schémas de chimiothérapie établis du neuroblastome. Le lien repose toutefois uniquement sur le score élevé du modèle et sur ce contexte : aucune donnée directe n'a été fournie pour le ganglioneuroblastome.

Les autres prédictions classées par le modèle sont de moindre intérêt. Le syndrome malformatif avec anomalies vertébrales et dysfonction endocrinienne et T (rang 2) n'a aucun lien mécanistique plausible : il s'agit d'un syndrome congénital rare et non d'une tumeur proliférative, et son score semble être un artefact du graphe de connaissances. La **leucémie myéloïde** (rang 5) est la prédiction la mieux documentée (niveau L3), avec des études cliniques anciennes ; elle est présentée dans les sections suivantes à titre complémentaire.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré pour le ganglioneuroblastome.

À titre de contexte, voici les essais enregistrés pour le **neuroblastome**, pathologie apparentée (rang 3). Il s'agit de protocoles multi-agents ; l'usage de la vindésine n'y est pas confirmé par les données compilées.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04221035](https://clinicaltrials.gov/study/NCT04221035) | Phase 3 | En recrutement | 800 | HR-NBL2 (SIOPEN) : trois randomisations évaluant les chimiothérapies d'induction et de consolidation et la radiothérapie dans le neuroblastome à haut risque |
| [NCT03042429](https://clinicaltrials.gov/study/NCT03042429) | Phase 3 | Terminé | 360 | Ajout de deux cycles de chimiothérapie à base de topotécan, suivi d'une greffe de cellules souches et d'isotrétinoïne, dans le neuroblastome à haut risque |
| [NCT00410631](https://clinicaltrials.gov/study/NCT00410631) | Phase 3 | Inconnu | 642 | NB2004 : traitement adapté au risque chez l'enfant atteint de neuroblastome |
| [NCT00002802](https://clinicaltrials.gov/study/NCT00002802) | Phase 3 | Terminé | 500 | Essai multicentrique ancien comparant des schémas de traitement chez l'enfant et l'adolescent |
| [NCT00526318](https://clinicaltrials.gov/study/NCT00526318) | Non applicable | Inconnu | 360 | NB2004-HR : chimiothérapie avant autogreffe puis isotrétinoïne dans le neuroblastome à haut risque |
| [NCT00017225](https://clinicaltrials.gov/study/NCT00017225) | Phase 2 | Terminé | Non renseigné | Étude de différentes thérapies combinant chimiothérapie, radiothérapie et greffe de cellules souches périphériques |

## Preuves de la Littérature

Aucune publication n'est disponible pour le ganglioneuroblastome.

Pour la **leucémie myéloïde** (rang 5), les principales publications portant sur la vindésine sont les suivantes :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [6957273](https://pubmed.ncbi.nlm.nih.gov/6957273/) | 1982 | Étude clinique | Cancer Chemother Pharmacol | Vindésine en monothérapie chez 36 patients (LMC, LMC en phase blastique, leucémie aiguë non lymphoïde) : diminution rapide des cellules leucémiques chez 31 patients |
| [6580840](https://pubmed.ncbi.nlm.nih.gov/6580840/) | 1983 | Étude randomisée | Gan To Kagaku Ryoho | Vindésine ou vincristine associée à la prednisolone dans la LAL de l'adulte et la crise blastique de LMC |
| [3857971](https://pubmed.ncbi.nlm.nih.gov/3857971/) | 1985 | Étude clinique de phase II | Cancer Treat Rep | Vindésine et prednisone dans la crise blastique de LMC chez 16 patients |
| [3855698](https://pubmed.ncbi.nlm.nih.gov/3855698/) | 1985 | Étude clinique | Cancer Treat Rep | Vindésine-prednisone dans la crise blastique de LMC : 3 rémissions complètes et 3 partielles sur 8 patients |
| [3865760](https://pubmed.ncbi.nlm.nih.gov/3865760/) | 1985 | Étude clinique | Dtsch Med Wochenschr | Vindésine et prednisolone chez 9 patients en crise blastique : 4 rémissions complètes, 1 partielle |
| [6573959](https://pubmed.ncbi.nlm.nih.gov/6573959/) | 1983 | Étude clinique | Cancer Treat Rep | Vindésine et prednisone dans les lymphomes et leucémies aiguës, dont la crise blastique de LMC |
| [274996](https://pubmed.ncbi.nlm.nih.gov/274996/) | 1978 | Essai de phase II | Cancer Treat Rep | Fort taux de rémission dans la leucémie lymphoïde aiguë et la crise blastique de LMC, sans résistance croisée avec la vincristine |
| [9389357](https://pubmed.ncbi.nlm.nih.gov/9389357/) | 1997 | Revue | Leuk Lymphoma | Vindésine dans les leucémies : potentiel limité mais intéressant dans la LAL résistante à la vincristine ou en rechute |
| [6359081](https://pubmed.ncbi.nlm.nih.gov/6359081/) | 1983 | Revue | Pharmacotherapy | Pharmacologie, efficacité clinique et effets indésirables de la vindésine |
| [8124212](https://pubmed.ncbi.nlm.nih.gov/8124212/) | 1993 | Étude clinique | Leuk Lymphoma | Protocole de rattrapage incluant la vindésine : rémission complète chez 59 % des LAM et 67 % des LAL réfractaires ou en rechute |

Pour la **tumeur rétropéritonéale** (rang 4), seules deux observations de cas ont été fournies, sans lien confirmé avec la vindésine (dont un liposarcome rétropéritonéal traité par CYVADIC, schéma incluant la vincristine).

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61886269 | ELDISINE 5 mg, poudre pour solution injectable (EG LABO - Laboratoires Eurogenerics) | Poudre pour solution injectable | Non renseignée (AMM annulée) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (alcaloïde de la pervenche, antimitotique) |
| Risque de Myélosuppression | Élevé : la myélosuppression est la toxicité dose-limitante (nadir vers J7-J8, récupération vers J11-J13, dose maximale tolérée de 4-5 mg/m²/semaine d'après la littérature) |
| Classification d'Émétogénicité | Faible (selon la classe) |
| Éléments de Surveillance | NFS avec formule, fonction hépatique et rénale, surveillance neurologique (neuropathie périphérique et atteinte neurovégétative décrites dans la littérature) |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques ; produit vésicant, éviter tout extravasation |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées, et aucune contre-indication n'est issue du graphe de connaissances.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Pour le ganglioneuroblastome, la prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication. La seule AMM française est annulée, et les données de sécurité de la notice sont absentes, ce qui empêche le passage au criblage de sécurité.
- Les pistes les plus étayées sont le neuroblastome (L4, essais de protocoles non spécifiques à la vindésine) et la leucémie myéloïde (L3, études anciennes et de petite taille, largement supplantées par les inhibiteurs de tyrosine kinase). Elles relèvent au mieux de questions de recherche.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde et contre-indications), donnée bloquante
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Vérifier, dans les protocoles de neuroblastome, si la vindésine figure réellement dans un bras de traitement
- Rechercher des données précliniques ou cliniques spécifiques au ganglioneuroblastome
- Évaluer la faisabilité d'une voie d'administration et d'un approvisionnement, la compatibilité de voie n'étant pas évaluée et le produit n'étant plus commercialisé en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

