---
layout: default
title: Eptinezumab
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 1
---

# Eptinezumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Eptinezumab : De la Prévention de la Migraine à la Migraine avec Aura du Tronc Cérébral

## Résumé en Une Phrase

Eptinezumab est un anticorps monoclonal anti-CGRP développé à l'international pour la prévention de la migraine épisodique et chronique, sans autorisation de mise sur le marché en France à ce jour.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **migraine avec aura du tronc cérébral**,
avec **0 essai clinique dédié** et **8 publications** soutenant actuellement cette direction. Cette sous-forme rare de migraine partage les voies CGRP de la migraine commune, justifiant mécanistiquement cette prédiction.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Prévention de la migraine (usage international reconnu ; aucune AMM en France) |
| Nouvelle Indication Prédite | Migraine avec aura du tronc cérébral |
| Score de Prédiction TxGNN | 99,94 % |
| Niveau de Preuve | L3 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Eptinezumab est un anticorps monoclonal dirigé contre le CGRP (Calcitonin Gene-Related Peptide), agissant comme antagoniste direct du ligand circulant. Ce neuropeptide vasodilatatoire est au cœur de la cascade trigémino-vasculaire de la migraine : en le neutralisant, eptinezumab empêche sa liaison aux récepteurs sur les vaisseaux méningés et les neurones trigéminaux, interrompant ainsi la chaîne de la douleur migraineuse.

La migraine avec aura du tronc cérébral (anciennement « migraine de type basilaire ») implique des symptômes d'aura d'origine clairement tronculaire — dysarthrie, vertiges, acouphènes, diplopie, ataxie — reflétant une implication du *nucleus trigeminalis caudalis* et une dépolarisation corticale envahissante (CSD). Ces mécanismes partagent la même voie CGRP que la migraine commune, ce qui rend plausible l'extension thérapeutique d'un anti-CGRP à ce sous-type. L'analyse post-hoc des essais PROMISE-1/2 (PMID 35302389) confirme par ailleurs qu'eptinezumab conserve son efficacité chez les patients migraineux présentant une aura auto-déclarée.

Cependant, des données récentes nuancent ce tableau. Un ECR de 2025 (PMID 40229719) démontre que les attaques induites par le PACAP38 opèrent via des voies indépendantes du CGRP, suggérant que certaines formes de migraine avec aura du tronc cérébral pourraient échapper à une thérapie purement anti-CGRP. De plus, les migraines génétiques (ex. : migraine hémiplégique familiale) présentent une réponse variable aux antagonistes CGRP selon les individus (PMID 40341526). Ces éléments impliquent une sélection rigoureuse des patients avant utilisation.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [35302389](https://pubmed.ncbi.nlm.nih.gov/35302389/) | 2022 | Analyse post-hoc (Phase 3 RCT PROMISE-1/2) | *Cephalalgia* | Efficacité et sécurité d'eptinezumab pour la prévention de la migraine chez les patients avec aura auto-déclarée ; signal positif dans ce sous-groupe |
| [40229719](https://pubmed.ncbi.nlm.nih.gov/40229719/) | 2025 | ECR (mécanisme, non-eptinezumab) | *J Headache Pain* | Les attaques induites par le PACAP38 sont indépendantes de la signalisation CGRP — nuance critique pour l'efficacité attendue dans les sous-types à aura du tronc cérébral |
| [40341526](https://pubmed.ncbi.nlm.nih.gov/40341526/) | 2025 | Revue d'association génétique | *Headache* | Les migraines d'origine génétique (MELAS, FHM) répondent aux antagonistes CGRP avec une variabilité inter-individuelle notable |
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Série de cas + revue narrative | *J Clin Med* | Les anticorps anti-CGRP (dont eptinezumab) pourraient réduire la fréquence de l'aura via un effet sur la dépolarisation corticale envahissante |
| [40191903](https://pubmed.ncbi.nlm.nih.gov/40191903/) | 2025 | Rapport de cas | *Rev Neurol* | Gestion réussie de l'effet de « wearing-off » par eptinezumab chez une patiente en échec de deux anti-CGRP sous-cutanés, dont le tableau comprenait une migraine avec aura |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Revue narrative | *Handb Exp Pharmacol* | Rôle pivot du CGRP dans la physiopathologie migraineuse, incluant les mécanismes d'aura et les voies du tronc cérébral |
| [33550872](https://pubmed.ncbi.nlm.nih.gov/33550872/) | 2021 | Revue narrative | *Pain Manag* | Eptinezumab positionné parmi les quatre nouvelles options préventives approuvées ; mécanisme d'action, profil d'efficacité et de tolérance |
| [32699706](https://pubmed.ncbi.nlm.nih.gov/32699706/) | 2020 | Revue narrative | *Cureus* | Les antagonistes du CGRP sont efficaces dans la migraine épisodique et chronique avec ou sans aura ; synthèse des études disponibles |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
L'analyse post-hoc d'essais de Phase 3 (PROMISE-1/2) et un ensemble cohérent de revues et rapports de cas (niveau L3) soutiennent la plausibilité mécanistique d'eptinezumab dans la migraine avec aura du tronc cérébral. Toutefois, l'absence d'essai clinique dédié à ce sous-type, conjuguée aux données sur les voies CGRP-indépendantes (PACAP38) et à la variabilité de réponse dans les formes génétiques, exige des précautions dans la sélection des patients.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données complètes sur le mécanisme d'action (MOA) via DrugBank (lacune DG002)
- Informations de sécurité complètes : mises en garde, contre-indications et interactions médicamenteuses (lacune DG001)
- Lancement d'un essai clinique prospectif dédié à la migraine avec aura du tronc cérébral (aucun essai enregistré à ce jour)
- Identification biomarqueurs des sous-populations à composante CGRP-dépendante pour optimiser la sélection des patients
- Démarche réglementaire auprès de l'ANSM pour envisager une autorisation de mise sur le marché en France
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

