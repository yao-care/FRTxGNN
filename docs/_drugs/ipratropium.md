---
layout: default
title: Ipratropium
parent: Preuves élevées (L1-L2)
nav_order: 158
evidence_level: L1
indication_count: 10
---

# Ipratropium
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
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

# Ipratropium : De l'Indication Originale (non renseignée) à la Maladie Pulmonaire Obstructive

## Résumé en Une Phrase

L'ipratropium est un bronchodilatateur anticholinergique inhalé, commercialisé en France, mais dont l'indication originale n'est pas renseignée dans les données ANSM fournies.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **maladie pulmonaire obstructive**, avec **50 essais cliniques** et **20 publications** associés.
Il s'agit plutôt de la confirmation d'un usage déjà établi (BPCO, asthme) que d'une véritable nouvelle piste : seule une partie de ces essais teste directement l'ipratropium.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM (texte d'indication vide pour les 4 AMM) |
| Nouvelle Indication Prédite | Maladie pulmonaire obstructive |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 4 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données DrugBank détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Les éléments de justification indiquent toutefois que l'ipratropium est un antagoniste muscarinique non sélectif. En bloquant les récepteurs M3 du muscle lisse bronchique, il réduit la bronchoconstriction d'origine cholinergique ainsi que la sécrétion de mucus. La littérature le décrit comme un dérivé quaternaire de l'atropine, mal absorbé par voie inhalée.

Ce mécanisme correspond directement à la physiopathologie de la BPCO et de l'asthme, où le tonus vagal contribue à l'obstruction bronchique. La prédiction est donc pharmacologiquement cohérente.

Il faut cependant être clair : l'obstruction bronchique est un usage établi de l'ipratropium, et non un repositionnement au sens strict. Le score élevé du modèle confirme surtout une indication déjà validée cliniquement.

---

## Preuves d'Essais Cliniques

Sur les 50 essais associés, seuls ceux qui testent réellement l'ipratropium ou ses associations sont présentés ci-dessous. Plusieurs autres essais concernent d'autres bronchodilatateurs (indacatérol, formotérol, tiotropium) et n'apportent pas de preuve directe.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT05890638](https://clinicaltrials.gov/study/NCT05890638) | Phase 3 | Inconnu | 74 | Non-infériorité de l'association fixe ipratropium/lévosalbutamol versus association libre en nébulisation dans la BPCO stable |
| [NCT02182479](https://clinicaltrials.gov/study/NCT02182479) | Phase 3 | Terminé | 631 | Berodual (fénotérol/ipratropium) via Respimat versus MDI dans l'asthme sur 12 semaines : réponse bronchodilatatrice non inférieure |
| [NCT00400153](https://clinicaltrials.gov/study/NCT00400153) | Phase 3 | Terminé | 1480 | Combivent Respimat versus Combivent MDI et ipratropium seul dans la BPCO (VEMS sur 12 semaines) |
| [NCT02177253](https://clinicaltrials.gov/study/NCT02177253) | Phase 3 | Terminé | 1118 | Ipratropium/salbutamol Respimat versus Combivent, ipratropium seul et placebo dans la BPCO (12 semaines) |
| [NCT02177344](https://clinicaltrials.gov/study/NCT02177344) | Phase 3 | Terminé | 646 | Ipratropium Respimat (20 et 40 µg) versus Atrovent aérosol-doseur et placebo dans la BPCO (6 mois) |
| [NCT02194205](https://clinicaltrials.gov/study/NCT02194205) | Phase 3 | Arrêté | 360 | Combivent HFA versus Combivent CFC et placebo dans la BPCO (1 an) |
| [NCT01019694](https://clinicaltrials.gov/study/NCT01019694) | Phase 3 | Terminé | 470 | Sécurité à long terme et acceptabilité de Combivent Respimat dans la BPCO |
| [NCT00274040](https://clinicaltrials.gov/study/NCT00274040) | Phase 3 | Terminé | 141 | Tiotropium versus Atrovent (ipratropium) aérosol-doseur dans la BPCO |
| [NCT01136421](https://clinicaltrials.gov/study/NCT01136421) | Phase 3 | Terminé | 124 | Sulfate de magnésium versus ipratropium, associés à un β2-agoniste, dans l'exacerbation aiguë de BPCO |
| [NCT01691482](https://clinicaltrials.gov/study/NCT01691482) | Phase 4 | Terminé | 56 | Variation quotidienne de la réponse bronchodilatatrice à l'albutérol et à l'ipratropium, seuls et associés, dans la BPCO |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | Comparaison du tiotropium et de l'ipratropium dans la BPCO stable |
| [20163324](https://pubmed.ncbi.nlm.nih.gov/20163324/) | 2010 | Revue systématique | Expert Opin Drug Metab Toxicol | Mécanisme, efficacité et sécurité de l'albutérol, de l'ipratropium et de leur association dans la BPCO |
| [8181328](https://pubmed.ncbi.nlm.nih.gov/8181328/) | 1994 | Essai comparatif | Chest | L'association ipratropium/albutérol est plus efficace que chaque agent seul (essai multicentrique de 85 jours) |
| [23170031](https://pubmed.ncbi.nlm.nih.gov/23170031/) | 2012 | Revue | Ann Pharmacother | Efficacité et sécurité de l'ipratropium associé au tiotropium dans la BPCO |
| [15257628](https://pubmed.ncbi.nlm.nih.gov/15257628/) | 2004 | Revue | Drugs | Berodual (ipratropium/fénotérol) via Respimat dans l'asthme et la BPCO |
| [9741369](https://pubmed.ncbi.nlm.nih.gov/9741369/) | 1998 | Étude clinique | Thorax | Effets de la théophylline et de l'ipratropium sur la performance à l'effort dans la BPCO stable |
| [28461224](https://pubmed.ncbi.nlm.nih.gov/28461224/) | 2017 | Étude clinique | EBioMedicine | Différences de réponse du VEMS à l'ipratropium selon le sexe dans la BPCO légère à modérée |
| [38457591](https://pubmed.ncbi.nlm.nih.gov/38457591/) | 2024 | Analyse rétrospective | Medicine | Probiotiques associés au budésonide et à l'ipratropium : fonction pulmonaire et microbiote (118 patients) |
| [2977109](https://pubmed.ncbi.nlm.nih.gov/2977109/) | 1988 | Revue | Clin Pharm | Chimie, pharmacologie, efficacité clinique et effets indésirables de l'ipratropium dans la maladie pulmonaire obstructive |
| [35616126](https://pubmed.ncbi.nlm.nih.gov/35616126/) | 2022 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | Sulfate de magnésium dans les exacerbations de BPCO (preuve indirecte, l'ipratropium n'est pas l'intervention étudiée) |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66698997 | ATROVENT 20 microgrammes/dose (Boehringer Ingelheim France) | Solution pour inhalation en flacon pressurisé | Non renseignée |
| 61260984 | IPRATROPIUM VIATRIS 0,25 mg/ml ENFANTS (Viatris Santé) | Solution pour inhalation par nébuliseur en récipient unidose | Non renseignée |
| 69293057 | IPRATROPIUM VIATRIS 0,5 mg/2 ml ADULTES (Viatris Santé) | Solution pour inhalation par nébuliseur en récipient unidose | Non renseignée |
| 60175716 | IPRATROPIUM AGUETTANT ADULTES 0,5 mg/2 ml (Aguettant) | Solution pour inhalation par nébuliseur en récipient unidose | Non renseignée |

---

## Considérations de Sécurité

Les mises en garde, contre-indications et interactions médicamenteuses ne sont pas disponibles dans les données fournies. Veuillez consulter la notice pour les informations de sécurité.

Le dossier signale néanmoins les points de vigilance suivants :
- **Effets anticholinergiques** : rétention urinaire, glaucome et mydriase sont à surveiller. Un cas de mydriase unilatérale après inhalation a été rapporté chez un nourrisson (PMID 40069469).
- **Hypersensibilité** : un cas d'anaphylaxie sévère après inhalation d'ipratropium a été publié (PMID 8449120).

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de Phase 3 terminés, de grande taille, ainsi que des revues systématiques Cochrane soutiennent l'efficacité de l'ipratropium dans la BPCO et l'asthme, ce qui correspond au niveau L1. Cette indication est toutefois déjà établie et ne constitue pas un repositionnement nouveau.
- Les autres indications prédites ont des preuves faibles ou nulles et restent en attente ou au stade de question de recherche : rhinite/cavité nasale (L4), maladie trachéale (L4), malformation respiratoire (L4), pharyngite (L5), anaphylaxie (L4, avec un signal de sécurité inverse) et les autres (L5).

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser les notices ANSM (mises en garde, contre-indications, texte des indications approuvées), qui constituent une lacune bloquante pour le criblage de sécurité
- Compléter les données sur le mécanisme d'action via DrugBank
- Vérifier le rôle de l'ipratropium (produit testé ou comparateur) dans l'essai NCT00393458, dont le titre est tronqué
- Surveiller les effets anticholinergiques (rétention urinaire, glaucome, mydriasis) et les réactions d'hypersensibilité

*Ces résultats sont fournis à titre de référence pour la recherche et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

