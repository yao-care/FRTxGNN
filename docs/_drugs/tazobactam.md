---
layout: default
title: Tazobactam
parent: Preuves élevées (L1-L2)
nav_order: 733
evidence_level: L1
indication_count: 2
last_modified_at: 2026-10-14
description: "Tazobactam : nouvelle indication prédite, Pneumonie (niveau de preuve L1). Indication d'origine : Pneumonie bactérienne"
monitor_inn: "tazobactam"
predicted_indications: ["pneumonia", "urinary tract infection (disease)"]
---

# Tazobactam
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **2** 
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

# Tazobactam : De la pneumonie bactérienne à la pneumonie (extension au sein du même domaine thérapeutique)

## Résumé en Une Phrase

Le tazobactam est un inhibiteur de bêta-lactamases, utilisé à l'origine en association avec la pipéracilline pour traiter des infections bactériennes (pneumonie bactérienne, péritonite, appendicite, infections à staphylocoque doré).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **pneumonie**, avec **20 essais cliniques** et **20 publications** compilés pour cette direction. Il s'agit toutefois d'une extension au sein du même domaine thérapeutique plutôt que d'un véritable repositionnement, et les preuves concernent le tazobactam en association fixe, jamais en monothérapie.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Pneumonie bactérienne (texte d'indication des AMM non renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Pneumonie |
| Score de Prédiction TxGNN | 99,46 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 (0 valide, 20 annulées) |
| Décision Recommandée | Proceed with Guardrails |

**Seconde indication prédite (pour information) :** infection urinaire, score TxGNN de 99,12 %, niveau de preuve L1, mêmes réserves (voir plus bas).

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les informations connues, le tazobactam inhibe les bêta-lactamases de classe A (et certaines de classe C), protégeant le partenaire bêta-lactamine (pipéracilline, ceftolozane) de l'hydrolyse par des bactéries à Gram négatif productrices de ces enzymes.

La pneumonie est très proche de l'indication d'origine (pneumonie bactérienne) : il s'agit d'une extension au sein de la même aire thérapeutique. Le tazobactam n'a pas d'activité antibactérienne propre suffisante pour une utilisation seul ; les preuves portent donc sur des associations fixes (pipéracilline/tazobactam, ceftolozane/tazobactam).

Pour l'infection urinaire, le raisonnement est analogue : les entérobactéries et *Pseudomonas* responsables d'infections urinaires compliquées produisent fréquemment des bêta-lactamases. L'efficacité face aux germes producteurs de BLSE reste cependant incertaine, comme le montre la question en cours de la pipéracilline/tazobactam face aux carbapénèmes.

## Preuves d'Essais Cliniques

Pneumonie (les 10 essais les plus pertinents ; les 10 autres essais compilés, dont plusieurs sans évaluation de pertinence, ne sont pas détaillés) :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Phase 3 | Terminé | 537 | Imipénème/relébactam vs pipéracilline/tazobactam dans la pneumonie nosocomiale (HABP/VABP) ; critère principal : mortalité toutes causes |
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Phase 3 | Terminé | 726 | Ceftolozane/tazobactam vs méropénème dans la pneumonie nosocomiale ventilée (ASPECT-NP) ; non-infériorité |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Phase 3 | Terminé | 460 | Lévofloxacine vs pipéracilline/tazobactam dans la pneumonie nosocomiale légère à modérée ; non-infériorité |
| [NCT04223752](https://clinicaltrials.gov/study/NCT04223752) | Phase 1 | Terminé | 41 | Sécurité et pharmacocinétique du ceftolozane/tazobactam chez l'enfant avec pneumonie nosocomiale |
| [NCT00438269](https://clinicaltrials.gov/study/NCT00438269) | Phase 2 | Terminé | 80 | Essai pilote randomisé sur le traitement antimicrobien approprié en réanimation ; soutien indirect |
| [NCT06972537](https://clinicaltrials.gov/study/NCT06972537) | N/A | En recrutement | 42 | Dosage guidé par modèle vs empirique de la pipéracilline/tazobactam chez le sujet âgé ; pas de résultats |
| [NCT06977347](https://clinicaltrials.gov/study/NCT06977347) | N/A | Pas encore en recrutement | 100 | Pipéracilline/tazobactam seule vs associée à une fluoroquinolone dans la pneumonie communautaire grave |
| [NCT01853982](https://clinicaltrials.gov/study/NCT01853982) | Phase 3 | Arrêté | 4 | Ceftolozane/tazobactam vs pipéracilline/tazobactam dans la pneumonie sous ventilation ; arrêté, aucune donnée exploitable |
| [NCT03006679](https://clinicaltrials.gov/study/NCT03006679) | Phase 3 | Retiré | 0 | Méropénème-vaborbactam vs pipéracilline/tazobactam ; aucun participant inclus |
| [NCT04673175](https://clinicaltrials.gov/study/NCT04673175) | Phase 4 | Arrêté | 17 | Ceftolozane/tazobactam chez des patients d'hématologie ; arrêté précocement, preuves limitées |

Infection urinaire (évoquée à titre complémentaire) :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03687255](https://clinicaltrials.gov/study/NCT03687255) | Phase 3 | Terminé | 1043 | Céfépime-AAI101 vs pipéracilline/tazobactam (comparateur) dans l'infection urinaire compliquée |
| [NCT02728089](https://clinicaltrials.gov/study/NCT02728089) | Phase 3 | Terminé | 115 | Ceftolozane/tazobactam, étude japonaise non comparative dans la pyélonéphrite et l'infection urinaire compliquée |
| [NCT03230838](https://clinicaltrials.gov/study/NCT03230838) | Phase 2 | Terminé | 134 | Ceftolozane/tazobactam vs méropénème chez l'enfant avec infection urinaire compliquée |
| [NCT03891433](https://clinicaltrials.gov/study/NCT03891433) | Phase 4 | Suspendu | 198 | Pipéracilline/tazobactam vs carbapénèmes dans l'infection urinaire à germes producteurs de BLSE |

## Preuves de la Littérature

Pneumonie :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | ECR | Lancet Infect Dis | Ceftolozane-tazobactam vs méropénème dans la pneumonie nosocomiale (ASPECT-NP), phase 3 de non-infériorité |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | ECR | Clin Infect Dis | Imipénème/cilastatine/relébactam vs pipéracilline/tazobactam dans la HABP/VABP (RESTORE-IMI 2) |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | ECR | Int J Infect Dis | Essai de phase III de non-infériorité IMI/REL vs PIP/TAZ dans la HABP/VABP |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Revue systématique / méta-analyse en réseau | Clin Microbiol Infect | Schémas antibiotiques empiriques dans la pneumonie nosocomiale non ventilée |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Revue systématique | Int J Antimicrob Agents | Pharmacocinétique/pharmacodynamie des nouvelles associations bêta-lactamine/inhibiteur dans la pneumonie à bactéries résistantes aux carbapénèmes |
| [36543346](https://pubmed.ncbi.nlm.nih.gov/36543346/) | 2022 | Revue | Eur Respir Rev | Nouveaux antibiotiques pour la pneumonie à Gram négatif |
| [35088403](https://pubmed.ncbi.nlm.nih.gov/35088403/) | 2022 | Revue | Semin Respir Crit Care Med | Nouveaux antibiotiques pour les pneumonies nosocomiales et sous ventilation |
| [32600375](https://pubmed.ncbi.nlm.nih.gov/32600375/) | 2020 | Revue | Crit Care | Mise à jour du traitement de la pneumonie nosocomiale en réanimation |
| [38862579](https://pubmed.ncbi.nlm.nih.gov/38862579/) | 2024 | Étude observationnelle | Sci Rep | Céfépime vs pipéracilline/tazobactam dans la pneumonie communautaire en réanimation (2026 patients) |
| [38688353](https://pubmed.ncbi.nlm.nih.gov/38688353/) | 2024 | Recommandations / revue | Int J Antimicrob Agents | Prise en charge des infections à bacilles à Gram négatif multirésistants (sociétés italienne et française) |

Infection urinaire (principales références) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [36194218](https://pubmed.ncbi.nlm.nih.gov/36194218/) | 2022 | ECR | JAMA | Céfépime/enmétazobactam vs pipéracilline/tazobactam dans l'infection urinaire compliquée ou la pyélonéphrite aiguë |
| [29486041](https://pubmed.ncbi.nlm.nih.gov/29486041/) | 2018 | ECR | JAMA | Méropénème-vaborbactam vs pipéracilline-tazobactam (TANGO I) |
| [30861061](https://pubmed.ncbi.nlm.nih.gov/30861061/) | 2019 | ECR | Clin Infect Dis | Fosfomycine IV (ZTI-01) vs pipéracilline-tazobactam (ZEUS, phase 2/3) |
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | Revue systématique / méta-analyse en réseau | J Comp Eff Res | Options thérapeutiques dans les infections urinaires compliquées |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66252571 | PIPERACILLINE TAZOBACTAM VIATRIS 2 g/0,25 g | Poudre pour solution pour perfusion | Non renseignée (AMM annulée) |
| 67909536 | PIPERACILLINE/TAZOBACTAM SANDOZ 4 g/0,5 g | Poudre pour solution pour perfusion | Non renseignée (AMM annulée) |
| 60445784 | TAZOCILLINE 4 g/0,5 g | Poudre pour solution pour perfusion | Non renseignée (AMM annulée) |
| 67873780 | TAZOCILLINE 2 g/0,25 g | Poudre pour solution pour perfusion | Non renseignée (AMM annulée) |
| 65166404 | ZERBAXA 1 g/0,5 g | Poudre pour solution à diluer pour perfusion | Non renseignée (AMM annulée) |

Les 20 AMM compilées sont toutes au statut « annulée » ; aucune AMM valide n'est donc recensée dans les données.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (et non du texte de la notice)** : maladie rénale, pyo-uretère, neutropénie, agranulocytose, troubles de la coagulation, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, mononucléose infectieuse, syndrome d'infection chronique par le virus d'Epstein-Barr.
- **Interactions médicamenteuses** : aucune interaction retrouvée dans les données compilées.

Les mises en garde et contre-indications officielles issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de phase 3 et ECR concernent des associations contenant du tazobactam dans la pneumonie nosocomiale (niveau L1), mais le tazobactam n'y est souvent que le comparateur ou un composant d'association, et jamais évalué seul. L'indication est de plus très proche de l'indication d'origine, et toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité).
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Clarifier la situation réglementaire en France (AMM annulées, indications non renseignées) et la disponibilité réelle des produits.
- Préciser que toute utilisation concerne des associations fixes (pipéracilline/tazobactam, ceftolozane/tazobactam), et non le tazobactam seul.
- Pour l'infection urinaire, trancher la question de l'efficacité face aux germes producteurs de BLSE (essai CAPITIS suspendu).
- Prévoir une surveillance rénale et hématologique (NFS, fonction rénale) compte tenu des contre-indications du graphe de connaissances.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

