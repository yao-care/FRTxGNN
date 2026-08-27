---
layout: default
title: Tioconazole
parent: 僅模型預測 (L5)
nav_order: 308
evidence_level: L5
indication_count: 3
---

# Tioconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Tioconazole : De la Candidose Cutanéo-Vaginale à la Vulvovaginite

## Résumé en Une Phrase

Le tioconazole est un antifongique imidazolé topique, historiquement utilisé contre les mycoses superficielles de la peau et les candidoses vaginales.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Vulvovaginite**,
avec **2 essais cliniques** (indirects, sur molécules apparentées) et **20 publications** (dont plusieurs essais directs sur le tioconazole) soutenant cette direction.
Il faut noter que cette « nouvelle » indication recoupe en réalité largement le spectre antifongique déjà connu du produit — il ne s'agit pas d'un repositionnement mécanistique inédit.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Mycoses superficielles / candidose cutanéo-vaginale (usage antifongique topique — donnée issue de la littérature, aucune AMM française disponible) |
| Nouvelle Indication Prédite | Vulvovaginite |
| Score de Prédiction TxGNN | 99.23% |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le champ officiel de mécanisme d'action (DrugBank) n'est pas renseigné pour ce candidat (lacune de données signalée, sévérité élevée). Sur la base de la littérature disponible, le tioconazole est un antifongique imidazolé qui inhibe la lanostérol 14α-déméthylase fongique, bloquant ainsi la synthèse de l'ergostérol et compromettant l'intégrité de la membrane cellulaire fongique.

La vulvovaginite est très fréquemment causée par une infection à *Candida albicans*, c'est-à-dire exactement le spectre pour lequel le tioconazole a démontré son efficacité dans de nombreux essais historiques (candidose vulvo-vaginale, cf. littérature ci-dessous). Il ne s'agit donc pas d'une extrapolation mécanistique risquée : la cible pathogène de la « nouvelle » indication chevauche directement celle de l'usage antifongique originel du produit.

Les deux essais cliniques identifiés dans le pack de preuves ne testent toutefois pas le tioconazole lui-même, mais des associations apparentées (fenticonazole + tinidazole + lidocaïne, ovule Gynomax® XL) — ils apportent un soutien de classe indirect plutôt qu'une preuve directe. La force de la preuve provient donc principalement de la littérature historique directement centrée sur le tioconazole.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT06056947](https://clinicaltrials.gov/study/NCT06056947) | Phase 3 | Terminé | 577 | Comparaison de nouvelles formulations fenticonazole + tinidazole + lidocaïne vs Gynomax® XL dans la vaginose bactérienne, la candidose vulvovaginale, la trichomonase et les infections mixtes. **Molécule testée ≠ tioconazole** — preuve de classe indirecte (grade B). |
| [NCT03839875](https://clinicaltrials.gov/study/NCT03839875) | Phase 4 | Terminé | 116 | Étude ouverte à bras unique évaluant Gynomax® XL ovule dans le même spectre d'infections vaginales. Identité exacte du principe actif non confirmée dans le titre — preuve de classe indirecte (grade B). |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [6347833](https://pubmed.ncbi.nlm.nih.gov/6347833/) | 1983 | ECR (double aveugle) | Gynäkologische Rundschau | Comparaison tioconazole vs placebo dans la candidose vaginale, avec évaluation de l'absorption systémique (résumé détaillé non indexé). |
| [3524439](https://pubmed.ncbi.nlm.nih.gov/3524439/) | 1986 | ECR | Antimicrob Agents Chemother | Dose unique de tioconazole 6,5 % vs clotrimazole 3 jours : 84 % vs 85 % de patientes asymptomatiques à 4 semaines. |
| [6873744](https://pubmed.ncbi.nlm.nih.gov/6873744/) | 1983 | ECR ouvert | Gynäkologische Rundschau | Comparaison ouverte tioconazole crème vs econazole ovules, traitement de 3 jours de la candidose vaginale. |
| [6347834](https://pubmed.ncbi.nlm.nih.gov/6347834/) | 1983 | ECR ouvert | Gynäkologische Rundschau | Comparaison ouverte tioconazole vs econazole, traitement de 3 jours de la candidose vaginale. |
| [4025721](https://pubmed.ncbi.nlm.nih.gov/4025721/) | 1985 | Cohorte / évaluation clinique ouverte | Alabama J Med Sci | Évaluation clinique et cytologique du tioconazole dans la candidose vulvo-vaginale. |
| [6094282](https://pubmed.ncbi.nlm.nih.gov/6094282/) | 1984 | Étude ouverte randomisée | J Int Med Res | Dose unique topique de tioconazole 6 % vs kétoconazole systémique 400 mg/j x 5 j : éradication efficace dans les deux groupes à 5 semaines, réponse symptomatique plus rapide sous traitement topique. |
| [3485546](https://pubmed.ncbi.nlm.nih.gov/3485546/) | 1986 | Étude ouverte non comparative | J Int Med Res | Crème de tioconazole 2 % pendant 3 jours dans *Trichomonas vaginalis* et infections mixtes : taux de guérison de 95 % à J7. |
| [3510114](https://pubmed.ncbi.nlm.nih.gov/3510114/) | 1986 | Revue | Drugs | Large spectre d'activité antimicrobienne (dermatophytes, levures, chlamydia, trichomonas, bactéries Gram+) ; essais ouverts et contrôlés confirmant l'efficacité et la sécurité des préparations topiques dans les mycoses cutanées et la candidose vaginale. |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Revue | Expert Rev Anti Infect Ther | Revue des options antifongiques azolées non invasives pour la candidose vulvovaginale, y compris les formes compliquées/récurrentes. |
| [10470518](https://pubmed.ncbi.nlm.nih.gov/10470518/) | 1999 | Revue | Comprehensive Therapy | Épidémiologie, diagnostic et traitement des vulvovaginites — motif fréquent de consultation. |

---

## Informations de Marché en France

Aucune AMM n'est enregistrée en France : le tioconazole est classé **non commercialisé** dans le référentiel réglementaire consulté (0 licence trouvée).

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. *(Aucune donnée de mise en garde, contre-indication ou interaction médicamenteuse n'a pu être récupérée — recherche TFDA/DDI infructueuse ; il s'agit d'une lacune bloquante pour l'évaluation de sécurité S1.)*

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
La plausibilité mécanistique est forte — la vulvovaginite candidosique relève déjà du spectre antifongique historique du tioconazole, corroboré par plusieurs essais contrôlés directs (niveau de preuve L1). Cependant, les seuls essais cliniques référencés dans ce pack testent des molécules apparentées et non le tioconazole lui-même, et le produit n'est ni commercialisé en France ni documenté sur le plan réglementaire (仿單/警語 manquants — lacune bloquante DG001).

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir le résumé des caractéristiques du produit / notice TFDA (mises en garde, contre-indications) pour lever la lacune bloquante S1
- Confirmer l'identité exacte du principe actif testé dans NCT06056947 et NCT03839875
- Compléter les données de mécanisme d'action (DrugBank) pour formaliser l'analyse de similarité mécanistique
- Évaluer la voie réglementaire pour une éventuelle mise sur le marché français, le produit étant actuellement absent

---

**Note — autres indications candidates identifiées pour ce médicament (hors périmètre du présent rapport détaillé) :**
- *Vulvite* (score TxGNN 99.20%, niveau L2, recommandation « Research Question ») — plausibilité mécanistique par extrapolation, aucun essai ni publication centrés spécifiquement sur ce diagnostic isolé.
- *Vaginite atrophique post-ménopausique* (score TxGNN 99.19%, niveau L5, recommandation « Hold ») — aucune preuve clinique ni littérature ; l'étiologie (carence œstrogénique, non infectieuse) est incompatible avec le mécanisme antifongique du tioconazole, ce qui suggère un faux positif du modèle lié à la proximité sémantique du terme « vaginite ».
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

