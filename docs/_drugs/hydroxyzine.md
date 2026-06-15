---
layout: default
title: Hydroxyzine
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 5
---

# Hydroxyzine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Hydroxyzine : De l'Antihistaminique H1 à l'Urticaire Allergique

## Résumé en Une Phrase

Hydroxyzine est un antagoniste H1 de première génération, historiquement utilisé comme antiallergique, antiprurigineux et anxiolytique depuis les années 1950. Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Urticaire Allergique**, avec **1 essai clinique** et **20 publications** soutenant actuellement cette direction. Il convient de noter que cette indication correspond à l'usage historique établi de la molécule, ce qui confère à cette prédiction une valeur de confirmation clinique plutôt qu'un repositionnement à proprement parler.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Données AMM non disponibles (antihistaminique H1 / anxiolytique — usage historique) |
| Nouvelle Indication Prédite | Urticaire Allergique |
| Score de Prédiction TxGNN | 99,77 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✗ Non commercialisé (données insuffisantes — vérification ANSM recommandée) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Hydroxyzine est un antagoniste compétitif des récepteurs H1 de l'histamine de première génération. Il bloque directement les récepteurs H1 périphériques, inhibant l'augmentation de la perméabilité vasculaire induite par l'histamine, ainsi que les réactions de papule (*wheal*) et d'érythème (*flare*) qui caractérisent l'urticaire allergique. Son principal métabolite actif, la cétirizine, partage ce même mécanisme H1 et dispose lui-même de preuves cliniques de Phase 3 dans cette indication — ce qui constitue une validation indirecte du mécanisme parent.

Le mécanisme d'action est directement aligné sur la physiopathologie centrale de l'urticaire allergique : l'activation des mastocytes par des allergènes déclenche une libération massive d'histamine, dont les effets vasculaires et prurigineux sont précisément la cible de l'hydroxyzine. Cette congruence mécanistique explique que la molécule ait été considérée comme traitement de première ligne de l'urticaire depuis les années 1950.

Les lignes directrices actuelles (CSACI 2019) indiquent que les antihistaminiques H1 de deuxième génération sont désormais préférés en raison d'un meilleur profil de sécurité (moindre sédation, risque cardiovasculaire réduit). L'hydroxyzine conserve cependant un rôle documenté dans certaines situations cliniques spécifiques, notamment les urticaires réfractaires, les formes nécessitant un effet sédatif concomitant, ou en milieu hospitalier de courte durée.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---|---|---|---|---|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 (Pilote) | Terminé | 36 | Étude pilote multicentrique randomisée en double aveugle comparant la cétirizine IV (10 mg) — métabolite actif de l'hydroxyzine — à la diphenhydramine IV (50 mg) pour le traitement de l'urticaire aiguë en services d'urgences, d'urgences rapides et de cliniques d'allergie. Valide indirectement le mécanisme H1 dans l'urticaire allergique ; non extrapolable directement à la posologie orale de l'hydroxyzine. |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [31582993](https://pubmed.ncbi.nlm.nih.gov/31582993/) | 2019 | Guideline / Position officielle | *Allergy, Asthma & Clinical Immunology* | Déclaration de position CSACI : les AH de 2e génération sont plus sûrs que la 1re génération (incl. hydroxyzine, diphenhydramine) et doivent être la 1re ligne dans rhinite allergique et urticaire ; cite hydroxyzine explicitement comme référence historique avec risques sédatifs et cardiaques documentés |
| [28913986](https://pubmed.ncbi.nlm.nih.gov/28913986/) | 2017 | Revue | *Allergy, Asthma & Immunology Research* | Revue du traitement de l'urticaire spontanée chronique : les antihistaminiques H1 de 1re génération (hydroxyzine, diphenhydramine) étaient la norme passée ; doublage de dose jusqu'à 4×/jour si nécessaire ; en cas d'échec des AH à haute dose, passage à l'omalizumab 300 mg/mois |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Revue | *Annals of Pharmacotherapy* | Revue comparative de l'efficacité et de la sécurité des antihistaminiques de 1re et nouvelle génération dans la rhinite allergique et l'urticaire chronique idiopathique ; recommandations pratiques pour la pharmacie clinique |
| [22994340](https://pubmed.ncbi.nlm.nih.gov/22994340/) | 2012 | Revue | *Clinical and Experimental Allergy* | Analyse comparative des AH H1 dans l'urticaire spontanée chronique : comment prédire le meilleur médicament pour le patient individuel ; discussion des études en tête-à-tête et des biomarqueurs de réponse |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Revue pharmacologique | *Drugs* | La cétirizine, dérivé pipérazine et métabolite carboxylé de l'hydroxyzine, est un puissant antagoniste H1 avec propriétés antiallergiques ; essais contrôlés confirmant l'efficacité dans l'urticaire chronique avec profil de sécurité amélioré vs hydroxyzine parent |
| [12113226](https://pubmed.ncbi.nlm.nih.gov/12113226/) | 2002 | Revue | *Clinical Allergy and Immunology* | Revue des antagonistes H1 chez l'enfant : preuves de niveau 1 pour l'efficacité dans l'urticaire et la rhinoconjonctivite allergique ; données pédiatriques étayées par de nombreuses études bien conçues |
| [18336052](https://pubmed.ncbi.nlm.nih.gov/18336052/) | 2008 | Revue comparative PK/PD | *Clinical Pharmacokinetics* | Comparaison des profils pharmacocinétiques et pharmacodynamiques des AH de 2e génération (desloratadine, fexofénadine, levocetirizine) dans la rhinite allergique et l'urticaire chronique idiopathique |
| [22686617](https://pubmed.ncbi.nlm.nih.gov/22686617/) | 2012 | ECR Phase 3 | *Drugs* | Bilastine (AH 2e génération) : deux essais de Phase 3 bien conçus démontrant une réduction significative du score total de symptômes vs placebo dans la rhinite allergique saisonnière et l'urticaire |
| [12806876](https://pubmed.ncbi.nlm.nih.gov/12806876/) | 2003 | Revue | *Revue Médicale de Bruxelles* | Les antagonistes H1 sont les médicaments les plus prescrits pour les maladies atopiques ; leurs indications principales incluent urticaire et rhinite allergique ; comparaison 1re vs 2e génération sur effets indésirables et profil d'utilisation |
| [39532327](https://pubmed.ncbi.nlm.nih.gov/39532327/) | 2024 | Rapport de cas | *BMJ Case Reports* | Urticaire aquagénique (sous-type d'urticaire physique) chez une adolescente : diagnostic et prise en charge documentés ; rappelle la complexité des urticaires induites et le rôle des AH dont l'hydroxyzine dans les formes réfractaires |

---

## Informations de Marché en France

Aucune autorisation de mise sur le marché (AMM) n'est répertoriée pour HYDROXYZINE dans les données interrogées.

> ⚠️ **Attention — Gap de données probable** : L'absence de données AMM reflète vraisemblablement une limite de la source interrogée plutôt que l'absence réelle du médicament sur le marché français. Hydroxyzine (Atarax®) est une molécule ancienne et largement connue. Une vérification directe sur la base de données de l'ANSM est indispensable avant toute décision réglementaire ou commerciale.

---

## Considérations de Sécurité

Les données de sécurité formelles (mises en garde ANSM, contre-indications réglementaires, interactions médicamenteuses) ne sont pas disponibles dans cet Evidence Pack.

**Points de vigilance identifiés dans la littérature scientifique :**

- **Effets sédatifs prononcés** : somnolence, altération des fonctions cognitives, mauvaise qualité du sommeil — caractéristiques des AH de 1re génération, distinguant l'hydroxyzine des alternatives modernes
- **Effets anticholinergiques** : bouche sèche, vertiges, hypotension orthostatique
- **Risque cardiovasculaire** : des cas de mort subite cardiaque ont été associés aux AH de 1re génération à forte dose (PMID 31582993)
- **Risque en cas de surdosage** : décès par accidents (conduite), surdosages intentionnels ou non intentionnels rapportés
- **Population pédiatrique** : précaution pour le dosage (études disponibles, mais risque de sédation à surveiller)
- **Interactions médicamenteuses** : potentialisation attendue avec autres dépresseurs du SNC, alcool, anesthésiants — données formelles non disponibles dans cet Evidence Pack

> Veuillez consulter la notice officielle et les données ANSM pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
L'indication d'urticaire allergique est mécanistiquement directe (antagonisme H1 → inhibition histaminique) et correspond à l'usage historique documenté de l'hydroxyzine depuis les années 1950. La prédiction TxGNN est confortée par 1 essai clinique de Phase 3 (pilote, portant sur la cétirizine — métabolite direct) et 20 publications incluant des guidelines officielles de sociétés savantes. Le principal frein n'est pas l'efficacité, mais la balance bénéfice-risque défavorable face aux AH de 2e génération dans les indications standard ; la molécule conserve cependant un espace clinique dans des niches spécifiques.

**Pour avancer, les éléments suivants sont nécessaires :**
- Vérification du statut AMM réel auprès de l'ANSM (les données actuelles de cet Evidence Pack sont incomplètes — gap de données DG001/DG002)
- Récupération des mises en garde et contre-indications depuis la notice officielle ANSM (DG001 — sévérité Bloquante)
- Récupération des données complètes de mécanisme d'action depuis DrugBank (DG002 — sévérité Haute)
- Définition précise des sous-populations cibles pour lesquelles l'hydroxyzine conserve un avantage différentiel (urticaires réfractaires aux AH de 2e génération, contexte hospitalier avec besoin de sédation concomitante)
- Plan de surveillance de sécurité spécifique, notamment pour les sujets âgés, les conducteurs, et les patients sous co-médications sédatives
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

