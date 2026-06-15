---
layout: default
title: Danazol
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 10
---

# Danazol
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

# Danazol : De l'Endométriose à l'Aménorrhée

## Résumé en Une Phrase

Danazol est un stéroïde synthétique dérivé de la 17α-éthinyltestostérone, reconnu dans la littérature internationale pour le traitement de l'endométriose, de la maladie fibrokystique du sein et de l'angiœdème héréditaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Aménorrhée**,
avec **0 essai clinique enregistré** et **20 publications** soutenant actuellement cette direction — dont un essai randomisé contrôlé et une cohorte rétrospective multi-sites récente (2024) sur la suppression menstruelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Endométriose, maladie fibrokystique du sein, angiœdème héréditaire *(source : littérature ; médicament non enregistré en France)* |
| Nouvelle Indication Prédite | Aménorrhée *(amenorrhea)* |
| Score de Prédiction TxGNN | 99,99% |
| Niveau de Preuve | L3 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données officielles sur le mécanisme d'action (MOA) ne sont pas disponibles dans les sources réglementaires françaises (Danazol n'est pas commercialisé en France). Sur la base des informations connues issues de la littérature, Danazol est un stéroïde synthétique à effets antigonadotropes multiples : il inhibe la sécrétion pulsatile de GnRH, supprimant ainsi la libération de FSH et LH par l'hypophyse. Cette suppression entraîne une mise en repos de la fonction ovarienne, une atrophie endométriale progressive, et finalement une aménorrhée médicalement induite — mécanisme central de son efficacité dans l'endométriose.

Le lien entre l'indication originale (endométriose) et la nouvelle indication prédite (aménorrhée) est direct et biologiquement cohérent : l'induction de l'aménorrhée est précisément le mécanisme thérapeutique par lequel Danazol agit sur l'endométriose. Le modèle TxGNN identifie ici une relation de causalité pharmacologique bien établie. Plus récemment, cette propriété est exploitée de façon délibérée chez les personnes transgenres et non binaires pour la suppression menstruelle (PMID 39051650, 2024), représentant une application émergente à part entière.

Il convient cependant de distinguer soigneusement deux cadres cliniques distincts : l'aménorrhée **thérapeutique** (effet intentionnel lors du traitement de l'endométriose ou de la suppression menstruelle) et l'aménorrhée **pathologique** (trouble gynécologique à traiter, par exemple par anovulation ou insuffisance ovarienne), pour laquelle Danazol n'a pas de données d'efficacité directes et peut même être contre-indiqué.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [2140996](https://pubmed.ncbi.nlm.nih.gov/2140996/) | 1990 | ECR | *Fertility and Sterility* | Nafarelin 400 µg/j vs Danazol 600 mg/j dans l'endométriose (82 patients, 6 mois) : les deux traitements induisent une régression significative de la maladie active et une aménorrhée thérapeutique |
| [39051650](https://pubmed.ncbi.nlm.nih.gov/39051650/) | 2024 | Cohorte rétrospective multi-sites | *Women's Health* | Danazol utilisé spécifiquement pour la suppression menstruelle chez des personnes transgenres et non binaires ; potentiel confirmé d'induction de l'aménorrhée avec effets androgènes réversibles |
| [36434439](https://pubmed.ncbi.nlm.nih.gov/36434439/) | 2023 | Revue systématique et méta-analyse | *Arch Gynecol Obstet* | Gestrinone (analogue structural de Danazol) induit l'atrophie endométriale et l'aménorrhée dans l'endométriose ; base de comparaison avec Danazol |
| [6210867](https://pubmed.ncbi.nlm.nih.gov/6210867/) | 1982 | Double aveugle randomisé | *Obstetrics and Gynecology* | Danazol à 4 niveaux de dose (100–600 mg/j, 27 patientes) : efficacité dose-dépendante sur la régression de l'endométriose et l'induction de l'aménorrhée |
| [6819580](https://pubmed.ncbi.nlm.nih.gov/6819580/) | 1982 | Étude clinique | *Prog Clin Biol Res* | Danazol supprime la fonction ovarienne et la stéroïdogenèse ; aménorrhée induite comme mécanisme d'action dans l'endométriose et l'infertilité associée |
| [16280355](https://pubmed.ncbi.nlm.nih.gov/16280355/) | 2006 | Revue | *Human Reproduction Update* | L'endométriose (maladie estrogène-dépendante) régresse lors des états d'aménorrhée ou de ménopause ; Danazol comme inducteur d'aménorrhée thérapeutique |
| [2404115](https://pubmed.ncbi.nlm.nih.gov/2404115/) | 1990 | Revue | *J Reproductive Medicine* | Danazol : effets biologiques multiples — inhibition des gonadotrophines, suppression de la stéroïdogenèse gonadique et surrénalienne, effets immunorégulateurs |
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Revue basée sur les preuves | *Menopause* | Approche thérapeutique des saignements utérins anormaux : Danazol parmi les agents hormonaux réduisant l'hyperplasie endométriale et induisant l'aménorrhée |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Revue | *J R Army Medical Corps* | Induction thérapeutique de l'aménorrhée : comparaison Danazol vs analogues GnRH (goséréline) vs contraceptifs oraux continus — Danazol efficace mais moins bien toléré |
| [2013670](https://pubmed.ncbi.nlm.nih.gov/2013670/) | 1991 | Suivi longitudinal (56 patients, >5 ans) | *J Allergy Clin Immunol* | Prophylaxie HAE à long terme : la dose minimale efficace de Danazol (200 mg/j) entraîne des irrégularités menstruelles et aménorrhée chez certaines patientes |

---

## Informations de Marché en France

Danazol n'est actuellement **pas commercialisé en France** — aucune AMM n'est enregistrée (0 licence ANSM). Le médicament est approuvé par la FDA (États-Unis) sous le nom de marque Danocrine® pour trois indications : endométriose, maladie fibrokystique du sein et angiœdème héréditaire. Une évaluation réglementaire complète auprès de l'ANSM serait nécessaire avant tout usage en France.

---

## Considérations de Sécurité

Les données réglementaires françaises (contre-indications, mises en garde de la notice ANSM) ne sont pas disponibles pour ce médicament non commercialisé.

> **Données issues de la littérature** :
> - **Effets androgènes** : acné, hirsutisme, prise de poids, modification de la voix (potentiellement irréversible à doses élevées)
> - **Hépatotoxicité** : surveillance de la fonction hépatique recommandée lors des traitements prolongés
> - **Contre-indication en grossesse** (catégorie X FDA) : risque de virilisation du fœtus féminin
> - **Contre-indication pendant l'allaitement** : passage dans le lait maternel
> - **Interaction médicamenteuse notable** : association Danazol + statines (ex. lovastatine) → risque de rhabdomyolyse et pancréatite (PMID 18691993)

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Le lien mécanistique entre Danazol et l'aménorrhée est biologiquement solide et bien documenté (20 publications dont 1 ECR et 1 cohorte rétrospective multi-sites). L'application émergente en suppression menstruelle chez les personnes transgenres constitue un angle de repositionnement cliniquement pertinent. Cependant, l'absence d'essais prospectifs ciblant explicitement l'aménorrhée comme indication primaire, combinée à l'absence de commercialisation en France et aux lacunes sur les données de sécurité réglementaires françaises, impose une progression encadrée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les données complètes de MOA depuis DrugBank (DG002 identifié comme lacune prioritaire)
- Télécharger et analyser la notice FDA (Danocrine®) pour les contre-indications et mises en garde complètes (DG001)
- Définir précisément la population cible : suppression menstruelle (personnes transgenres/non binaires) vs aménorrhée pathologique — les deux indications requièrent des stratégies cliniques différentes
- Évaluer la faisabilité d'une demande d'AMM en France auprès de l'ANSM
- Identifier des essais cliniques prospectifs actifs sur la suppression menstruelle comme indication primaire (ClinicalTrials.gov)
- Mettre en place un plan de surveillance hépatique et hormonale pour les traitements prolongés
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

