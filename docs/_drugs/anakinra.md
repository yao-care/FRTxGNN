---
layout: default
title: Anakinra
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 10
---

# Anakinra
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Anakinra : De la Polyarthrite Rhumatoïde à la Fièvre Méditerranéenne Familiale Résistante à la Colchicine

*Rapport Multi-Indications — 10 indications prédites par TxGNN*

---

## Résumé en Une Phrase

Anakinra est un antagoniste recombinant du récepteur de l'interleukine-1 (IL-1Ra), reconnu internationalement pour le traitement de la polyarthrite rhumatoïde et de certains syndromes auto-inflammatoires rares, mais non encore commercialisé en France.
Le modèle TxGNN identifie **10 nouvelles indications potentielles**, parmi lesquelles la **Fièvre Méditerranéenne Familiale à transmission autosomique récessive (AR-FMF)** et le **Syndrome Auto-Inflammatoire Pyogénique (PAPA/PAPASH)** présentent le meilleur niveau de preuve clinique.
Ces deux indications prioritaires sont soutenues respectivement par **20 publications** et **19 publications**, incluant des preuves directes d'efficacité d'anakinra chez des patients résistants à la colchicine ou aux traitements conventionnels.

---

## Aperçu Rapide

### Indication Prioritaire : Fièvre Méditerranéenne Familiale Autosomique Récessive

| Élément | Contenu |
|---------|---------|
| Indication Originale | Polyarthrite rhumatoïde (indication internationale — médicament non commercialisé en France) |
| Nouvelle Indication Prédite | Fièvre Méditerranéenne Familiale autosomique récessive (AR-FMF) |
| Score de Prédiction TxGNN | 99.89% |
| Niveau de Preuve | L3 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

### Vue d'Ensemble des 10 Indications Prédites

| Rang | Indication | Score TxGNN | Niveau de Preuve | Recommandation |
|------|-----------|-------------|-----------------|----------------|
| 1 | Mastocytome extracutané | 99.93% | L5 | Hold |
| 2 | Infarctus hépatique | 99.89% | L5 | Hold |
| **3** | **Fièvre Méditerranéenne Familiale AR** | **99.89%** | **L3** | **✓ Proceed with Guardrails** |
| 4 | Mastocytose systémique agressive | 99.88% | L4 | Research Question |
| 5 | Maladie veino-occlusive hépatique | 99.88% | L5 | Hold |
| 6 | Péliose hépatique | 99.85% | L5 | Hold |
| 7 | JIA oligoarticulaire ANA+ | 99.85% | L4 | Research Question |
| 8 | JIA oligoarticulaire ANA- | 99.85% | L4 | Research Question |
| **9** | **Syndrome auto-inflammatoire pyogénique (PAPA/PAPASH)** | **99.83%** | **L3** | **✓ Proceed with Guardrails** |
| 10 | Syndrome auto-inflammatoire non classifié | 99.81% | L3 | Research Question |

---

## Pourquoi Ces Prédictions sont-elles Raisonnables ?

### Mécanisme d'action d'Anakinra

Anakinra est une forme recombinante de l'antagoniste naturel du récepteur de l'interleukine-1 humain (IL-1Ra). Il bloque compétitivement la liaison de l'IL-1α et de l'IL-1β au récepteur IL-1 de type I (IL-1R1), empêchant la transduction du signal inflammatoire en aval. Cette inhibition ciblée de la voie IL-1 en fait un candidat thérapeutique idéal pour les pathologies dans lesquelles la dérégulation de l'inflammasome et la surproduction d'IL-1β jouent un rôle central dans la physiopathologie.

### Fièvre Méditerranéenne Familiale (AR-FMF)

La FMF est causée par des mutations du gène **MEFV** codant la protéine pyrine, un régulateur naturel de l'inflammasome. Ces mutations entraînent une activation incontrôlée de l'inflammasome à pyrine → hypersécrétion d'IL-1β → crises fébriles récurrentes avec sérosite, arthrite et myalgie. Anakinra, en bloquant directement IL-1R1, interrompt ce cycle inflammatoire de manière hautement spécifique. La littérature documente son efficacité chez les 5 à 10 % de patients résistants à la colchicine, avec des données publiées depuis 2009 (PMID 19033248). Les polymorphismes du gène IL-1Ra lui-même ont été étudiés dans la FMF (PMID 26861613), renforçant la cohérence mécanistique du ciblage de cette voie.

### Syndrome Auto-Inflammatoire Pyogénique (PAPA/PAPASH)

Les mutations du gène **PSTPIP1** provoquent une hyper-phosphorylation de la protéine PSTPIP1, entraînant l'oligomérisation de l'ASC et l'activation continue des inflammasomes NLRP3 et pyrine → surproduction massive d'IL-1β → arthrite pyogénique, pyoderma gangrenosum et acné sévère. Ce mécanisme est directement ciblé par anakinra. Une revue de cadrage multicentrique récente (PMID 38259483, 2023) a spécifiquement évalué l'efficacité et la sécurité d'anakinra dans les maladies associées à PSTPIP1, constituant la preuve directe la plus robuste disponible dans ce domaine.

### Cohérence Transversale

L'ensemble des indications aux niveaux L3-L4 partagent un dénominateur commun : **dérégulation de l'immunité innée et activation excessive de l'inflammasome avec surproduction d'IL-1**. Cette convergence mécanistique explique les scores TxGNN uniformément élevés pour ces pathologies auto-inflammatoires et valide la logique de repositionnement d'anakinra en tant qu'agent anti-IL-1 à large spectre dans les maladies rares de l'inflammasome.

---

## Preuves de la Littérature — Fièvre Méditerranéenne Familiale (AR-FMF)

*20 publications identifiées. Les 10 plus pertinentes sont présentées ci-dessous, par ordre de pertinence directe.*

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-------|------|-------|---------------------|
| [23322405](https://pubmed.ncbi.nlm.nih.gov/23322405/) | 2013 | Série de cas / Revue narrative | Clin Rev Allergy Immunol | Documente l'efficacité des biologiques anti-IL-1β (dont anakinra) dans la FMF résistante à la colchicine ; rationnel mécanistique détaillé |
| [26572612](https://pubmed.ncbi.nlm.nih.gov/26572612/) | 2016 | Revue | Curr Med Chem | Revue complète incluant anakinra comme traitement de la FMF résistante à la colchicine ; place dans l'arsenal thérapeutique définie |
| [21277619](https://pubmed.ncbi.nlm.nih.gov/21277619/) | 2011 | Série de cas / Revue | Semin Arthritis Rheum | Évaluation des médicaments ciblant IL-1 (dont anakinra) dans la FMF — confirmation de l'efficacité clinique |
| [19033248](https://pubmed.ncbi.nlm.nih.gov/19033248/) | 2009 | Rapport de cas | Nephrol Dial Transplant | Premier rapport de traitement réussi de FMF avec anakinra, avec suivi post-transplantation rénale ; données pionnières |
| [21931121](https://pubmed.ncbi.nlm.nih.gov/21931121/) | 2012 | Série de cas | Nephrol Dial Transplant | Effet bénéfique des inhibiteurs d'IL-1 (dont anakinra) dans FMF compliquée d'amylose AA et d'insuffisance rénale |
| [23928237](https://pubmed.ncbi.nlm.nih.gov/23928237/) | 2013 | Rapport de cas | Joint Bone Spine | Myosite associée à FMF + spondylarthrite traitée avec succès par anakinra après échec de la colchicine |
| [28585601](https://pubmed.ncbi.nlm.nih.gov/28585601/) | 2017 | Rapport de cas | JPMA J Pak Med Assoc | Anakinra puis canakinumab chez 4 enfants atteints de FMF résistante à la colchicine — réponse favorable documentée |
| [31205631](https://pubmed.ncbi.nlm.nih.gov/31205631/) | 2019 | Revue | Mediterr J Hematol Infect Dis | Évaluation globale de la FMF et plans de traitement incluant les agents biologiques anti-IL-1 ; algorithme décisionnel |
| [34873893](https://pubmed.ncbi.nlm.nih.gov/34873893/) | 2022 | Revue | Allergol Immunopathol | FMF en population pédiatrique — mécanismes, génétique et options thérapeutiques dont biologiques |
| [26861613](https://pubmed.ncbi.nlm.nih.gov/26861613/) | 2016 | Étude d'association génétique | Gene | Polymorphismes du gène IL-1Ra (rs2234663) dans la FMF turque — pertinence mécanistique directe du ciblage IL-1Ra |

---

## Preuves de la Littérature — Syndrome Auto-Inflammatoire Pyogénique (PAPA/PAPASH)

*19 publications identifiées. Les 10 plus pertinentes sont présentées ci-dessous, par ordre de pertinence directe.*

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-------|------|-------|---------------------|
| [38259483](https://pubmed.ncbi.nlm.nih.gov/38259483/) | 2023 | Revue de cadrage / Cohorte rétrospective | Front Immunol | Efficacité ET sécurité d'anakinra dans les maladies associées à PSTPIP1 — preuve directe la plus solide disponible ; analyse multicentrique |
| [39006661](https://pubmed.ncbi.nlm.nih.gov/39006661/) | 2024 | Série de cas | Cureus | Anakinra dans le syndrome PAPASH (PSTPIP1) — efficacité documentée avec revue de littérature ; données les plus récentes |
| [24275598](https://pubmed.ncbi.nlm.nih.gov/24275598/) | 2013 | Revue | Semin Immunol | Traitement de l'inflammation par le blocage de l'IL-1 chez l'humain — rationnel pharmacologique global pour anakinra |
| [27448064](https://pubmed.ncbi.nlm.nih.gov/27448064/) | 2016 | Revue | Hautarzt | Acné sévère dans les maladies auto-inflammatoires (PASH/PAPASH) — anakinra explicitement mentionné comme traitement via IL-1β |
| [21532836](https://pubmed.ncbi.nlm.nih.gov/21532836/) | 2010 | Revue | Curr Genomics | Syndrome PAPA : caractéristiques cliniques, moléculaires et génétiques — surproduction d'IL-1β comme cible thérapeutique principale |
| [22161697](https://pubmed.ncbi.nlm.nih.gov/22161697/) | 2012 | Série de cas | Arthritis Rheum | Génotype, phénotype, immunophénotype et traitements dans 5 patients atteints de syndrome PAPA |
| [28251506](https://pubmed.ncbi.nlm.nih.gov/28251506/) | 2017 | Rapport de cas / Revue | Infection | Syndrome PAPA diagnostiqué par comptages cellulaires synoviaux anormaux — défis diagnostiques et thérapeutiques |
| [18347298](https://pubmed.ncbi.nlm.nih.gov/18347298/) | 2008 | Revue | Arch Dermatol | Avancées cliniques et génétiques dans 7 maladies auto-inflammatoires dont PAPA — vue d'ensemble historique |
| [29742056](https://pubmed.ncbi.nlm.nih.gov/29742056/) | 2018 | Revue | Clin Exp Rheumatol | Perspective dermatologique sur les maladies auto-inflammatoires — rôle des mutations PSTPIP1 et traitement anti-IL-1 |
| [27464597](https://pubmed.ncbi.nlm.nih.gov/27464597/) | 2016 | Revue | Curr Opin Rheumatol | Spectre expansif des maladies liées à PSTPIP1 — nouveaux aspects pathogéniques pertinents pour le ciblage thérapeutique |

---

## Informations de Marché en France

Anakinra ne dispose d'aucune Autorisation de Mise sur le Marché (AMM) en France à ce jour. Le médicament est commercialisé dans d'autres pays sous le nom de marque **Kineret®** (Swedish Orphan Biovitrum) pour la polyarthrite rhumatoïde, la maladie de Still et d'autres syndromes auto-inflammatoires rares, mais n'a pas reçu d'AMM en France. Une demande d'accès compassionnel ou d'autorisation temporaire d'utilisation (ATU) pourrait constituer une voie réglementaire pertinente pour les indications prioritaires identifiées.

---

## Considérations de Sécurité

Veuillez consulter la notice officielle du médicament (Kineret®) pour les informations complètes de sécurité, incluant les mises en garde, contre-indications et interactions médicamenteuses.

---

## Conclusion et Prochaines Étapes

### Indication Prioritaire 1 : Fièvre Méditerranéenne Familiale AR (Rang 3)

**Décision : Proceed with Guardrails**

**Justification :**
Le mécanisme d'action d'anakinra (blocage direct de IL-1R1) est directement ciblé sur la physiopathologie de la FMF (surproduction d'IL-1β par l'inflammasome à pyrine mutante). Plusieurs rapports de cas et séries publiés entre 2009 et 2017 documentent l'efficacité clinique chez des patients résistants à la colchicine, et les publications de revue récentes positionnent anakinra comme traitement de deuxième ligne reconnu. Le niveau de preuve L3 justifie une progression encadrée vers un essai clinique formel.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les données complètes de mécanisme d'action (MOA) via DrugBank API
- Télécharger et analyser la notice ANSM/EMA pour les mises en garde et contre-indications
- Concevoir une étude observationnelle prospective ou un essai initié par l'investigateur (IIT) dans la population FMF résistante à la colchicine
- Évaluer la compatibilité des voies d'administration disponibles avec les besoins cliniques
- Explorer les voies d'accès réglementaire en France (autorisation temporaire d'utilisation, usage compassionnel)

---

### Indication Prioritaire 2 : Syndrome Auto-Inflammatoire Pyogénique — PAPA/PAPASH (Rang 9)

**Décision : Proceed with Guardrails**

**Justification :**
Le lien mécanistique PSTPIP1 → inflammasome NLRP3/pyrine → surproduction d'IL-1β → phénotype PAPA est hautement pertinent pour anakinra. La revue de cadrage multicentrique 2023 (PMID 38259483) et la série de cas 2024 (PMID 39006661) constituent des preuves directes et récentes d'efficacité. La rareté extrême de la maladie (maladie orpheline) suggère une stratégie IIT ou compassionnelle, idéalement dans un réseau de centres experts.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les données de sécurité complètes (notice officielle Kineret®)
- Identifier les centres experts nationaux en maladies auto-inflammatoires rares (réseau FAI²R en France)
- Envisager un registre prospectif multicentrique pour les syndromes liés à PSTPIP1
- Évaluer l'éligibilité à la désignation de médicament orphelin pour cette indication

---

### Indications à Surveiller (Research Question)

| Indication | Rang | Raison |
|-----------|------|--------|
| Mastocytose systémique agressive | 4 | Mécanisme indirect (IL-1 secondaire à l'activation des mastocytes) ; surveiller la littérature émergente |
| JIA oligoarticulaire ANA± | 7-8 | IL-1 non dominant dans ce sous-type ; anakinra en option exploratoire de dernier recours |
| Syndrome auto-inflammatoire non classifié | 10 | Valeur diagnostique ex juvantibus possible ; données de registre disponibles (PMID 37747561, PMID 36589607) |

---

### Indications à Ne Pas Poursuivre (Hold)

Les indications aux rangs **1** (mastocytome extracutané), **2** (infarctus hépatique), **5** (maladie veino-occlusive hépatique) et **6** (péliose hépatique) ne sont soutenues par aucune preuve clinique ou préclinique directe. Les scores TxGNN élevés reflètent des biais structurels du graphe de connaissances (nœuds d'inflammation partagés) plutôt qu'un lien mécanistique spécifique et actionnable. Aucune ressource ne devrait être investie dans ces directions sans émergence de nouvelles données fondamentales.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

