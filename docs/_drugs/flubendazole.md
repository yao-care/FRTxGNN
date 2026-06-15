---
layout: default
title: Flubendazole
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 10
---

# Flubendazole
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

# Flubendazole : De l'Antiparasitaire au Carcinome de la Vessie Urinaire

## Résumé en Une Phrase

Flubendazole est un agent benzimidazolé dont l'indication originale documentée en France est absente (médicament non commercialisé), mais qui appartient à une classe pharmacologique — les benzimidazoles — reconnue pour inhiber la polymérisation des tubulines et perturber la mitose cellulaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Carcinome de la Vessie Urinaire**, avec un score de confiance de **99,99%**.
Cependant, les preuves directes sont **quasi inexistantes** : aucun essai clinique ni publication portant spécifiquement sur Flubendazole dans cette indication n'a été identifié — seule une étude préclinique sur un analogue structurel (fenbendazole) apporte un soutien indirect pour la sous-indication adjacente.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non documentée (aucune AMM disponible) |
| Nouvelle Indication Prédite | Carcinome de la Vessie Urinaire |
| Score de Prédiction TxGNN | 99,99% |
| Niveau de Preuve | L5 (prédiction modèle uniquement — aucune étude directe) |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold — Question de Recherche |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Flubendazole appartient à la classe des **benzimidazoles**, dont le mécanisme d'action principal est l'**inhibition de la polymérisation des β-tubulines** (tubulin polymerization inhibition). En bloquant l'assemblage du fuseau mitotique, ces agents perturbent la division cellulaire et exercent un effet antiprolifératif potentiel sur les cellules à forte cinétique — dont les cellules cancéreuses. Ce mécanisme est pharmacologiquement distinct des chimiothérapies classiques et présente l'avantage théorique d'une résistance croisée limitée.

La prédiction TxGNN tire sa crédibilité de données établies sur des **analogues structurels de la même classe** : mebendazole et fenbendazole ont tous deux démontré une activité antitumorale dans des modèles précliniques de cancer vésical. En particulier, une étude de 2024 (PMID [39128990](https://pubmed.ncbi.nlm.nih.gov/39128990/)) montre que le fenbendazole, administré par **instillation intravésicale**, présente un effet synergique avec une thérapie CRISPR-Cas13a dans un modèle de cancer de la vessie — suggérant non seulement une activité anticancéreuse de classe, mais également une **voie d'administration** potentiellement adaptée à la pathologie visée.

Il convient cependant de souligner clairement les limites : **aucune donnée clinique ou préclinique directe ne concerne Flubendazole lui-même** dans le cancer de la vessie. Le score TxGNN élevé (0,9999) reflète vraisemblablement la densité des connexions entre les nœuds « benzimidazoles » et « cancers vésicaux » dans le graphe de connaissances biomédical, et non une prédiction fondée sur des données expérimentales spécifiques à cette molécule. La prudence s'impose avant toute extrapolation clinique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé à Flubendazole dans le carcinome de la vessie urinaire n'est enregistré actuellement.

---

## Preuves de la Littérature

Les données ci-dessous concernent la sous-indication adjacente (urinary bladder neoplasm, rang 2) et portent sur un analogue structurel — non sur Flubendazole directement.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39128990](https://pubmed.ncbi.nlm.nih.gov/39128990/) | 2024 | Préclinique (in vitro/in vivo) | J Exp Clin Cancer Res | Fenbendazole en instillation intravésicale combiné à CRISPR-Cas13a montre un effet synergique contre le cancer de la vessie ; valide la voie d'administration intravésicale pour les benzimidazoles et l'activité anticancéreuse de classe, mais non transposable directement à Flubendazole |

> **Note** : Cette publication concerne le **fenbendazole**, non Flubendazole. Elle constitue une preuve de classe (class evidence) et non une preuve directe. Le niveau L4 (données précliniques indirectes) s'applique uniquement à la sous-indication rang 2 ; la prédiction principale (rang 1) reste en L5.

---

## Informations de Marché en France

Flubendazole ne dispose d'**aucune AMM** en France. Aucune donnée de commercialisation n'est disponible.

---

## Cytotoxicité

Flubendazole est évalué ici dans un contexte antinéoplasique (inhibition de la polymérisation des tubulines, mécanisme antiprolifératif), ce qui justifie l'inclusion de cette section.

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique potentiel de classe benzimidazolée — inhibiteur de microtubules (analogue structural des agents antimitotiques) |
| Risque de Myélosuppression | Non documenté pour Flubendazole dans ce contexte — les benzimidazoles à usage antiparasitaire présentent un profil de myélosuppression généralement faible aux doses thérapeutiques habituelles, mais les données aux doses antitumorales sont absentes |
| Classification d'Émétogénicité | Non documentée — probablement faible à modérée par extrapolation de classe, à confirmer |
| Éléments de Surveillance | NFS (avec différentielle), fonction hépatique et rénale à prévoir dans tout protocole d'étude |
| Protection de Manipulation | Statut à définir — en l'absence de données de génotoxicité spécifiques à usage oncologique, appliquer par précaution les mesures standards de manipulation des agents cytotoxiques potentiels |

---

## Considérations de Sécurité

Les données de sécurité spécifiques à Flubendazole (mises en garde, contre-indications, interactions médicamenteuses) sont **absentes du pack de données disponible** (médicament non commercialisé en France, aucune fiche ANSM accessible). Les interactions médicamenteuses n'ont pas été identifiées dans la base de données DDI consultée.

> Veuillez consulter les références primaires (DrugBank DB08974, EMA ou littérature de pharmacovigilance internationale) pour toute information de sécurité avant d'envisager un usage expérimental.

---

## Conclusion et Prochaines Étapes

**Décision : Hold — Question de Recherche**

**Justification :**
Le score TxGNN est extrêmement élevé (99,99%), mais repose sur une prédiction par structure de graphe sans aucune validation expérimentale directe pour Flubendazole dans le cancer vésical. Les données de sécurité sont totalement absentes (médicament non commercialisé, aucune fiche d'AMM disponible), rendant impossible toute évaluation bénéfice-risque préliminaire. La prédiction reste une hypothèse de recherche légitime, soutenue par l'analogie de classe avec fenbendazole et mebendazole, mais ne peut pas progresser vers une phase clinique en l'état.

**Pour avancer, les éléments suivants sont nécessaires :**
- **Données de sécurité fondamentales** : récupérer la fiche DrugBank complète (MOA, toxicologie, profil ADMEt) et consulter les données réglementaires européennes disponibles
- **Validation préclinique directe** : études in vitro et in vivo de Flubendazole sur lignées cellulaires de carcinome vésical (T24, RT4, J82), en particulier comparaison avec fenbendazole/mebendazole
- **Évaluation de la voie d'administration** : faisabilité d'une formulation intravésicale de Flubendazole (solubilité, stabilité, tolérance locale)
- **Revue de littérature étendue** : recherche sur les analogues benzimidazolés dans le cancer vésical pour constituer un dossier de preuve de classe complet avant tout design d'étude clinique
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

