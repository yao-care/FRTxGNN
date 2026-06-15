---
layout: default
title: Darolutamide
parent: 僅模型預測 (L5)
nav_order: 97
evidence_level: L5
indication_count: 3
---

# Darolutamide
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

# Darolutamide : Du Cancer de la Prostate à l'Hypercholestérolémie Familiale Homozygote

## Résumé en Une Phrase

Darolutamide est un antagoniste sélectif du récepteur aux androgènes (AR) de nouvelle génération, initialement développé pour le traitement du cancer de la prostate résistant à la castration.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Hypercholestérolémie Familiale Homozygote (HoFH)**,
avec **0 essai clinique** et **0 publication** soutenant actuellement cette direction — cette prédiction repose exclusivement sur le graphe de connaissances biologiques du modèle.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Cancer de la prostate résistant à la castration |
| Nouvelle Indication Prédite | Hypercholestérolémie Familiale Homozygote (HoFH) |
| Score de Prédiction TxGNN | 99,11 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier. Sur la base des informations connues, Darolutamide est un antagoniste sélectif du récepteur aux androgènes (AR) de nouvelle génération (classe des anti-androgènes non stéroïdiens), dont la particularité est une très faible pénétration de la barrière hémato-encéphalique, lui conférant un meilleur profil de tolérance neurologique que les agents similaires.

L'HoFH est une maladie génétique sévère causée par des mutations homozygotes du récepteur LDL (LDLR), entraînant une accumulation critique de cholestérol LDL dès l'enfance. Le lien mécanistique avec l'AR est indirect : des données expérimentales suggèrent que la signalisation androgénique peut moduler l'expression hépatique du LDLR et le métabolisme du cholestérol — l'inhibition de l'AR pourrait théoriquement exercer un très faible effet compensatoire sur cette voie.

Ce mécanisme est cependant extrêmement indirect et hautement spéculatif. Aucune donnée préclinique ni clinique ne vient étayer cette hypothèse pour l'HoFH. Le signal TxGNN reflète une connexion distante au niveau du graphe biologique, sans validation expérimentale.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Darolutamide ne dispose d'aucune AMM enregistrée en France dans ce dossier. À titre informatif, Darolutamide (Nubeqa®) est approuvé par l'EMA et la FDA pour le cancer de la prostate, mais ces données réglementaires ne sont pas reflétées dans la présente base.

---

## Cytotoxicité

Darolutamide est un médicament antinéoplasique (antagoniste du récepteur aux androgènes, utilisé en oncologie urologique).

| Élément | Contenu |
|---|---|
| Classification de Cytotoxicité | Thérapie ciblée — Antagoniste du récepteur aux androgènes (AR antagoniste de 2ᵉ génération) |
| Risque de Myélosuppression | Faible (mécanisme non cytotoxique direct ; aucune myélosuppression significative rapportée dans les essais pivots) |
| Classification d'Émétogénicité | Faible |
| Éléments de Surveillance | Bilan hépatique, fonction rénale, pression artérielle (hypertension signalée), PSA, bilan cardiovasculaire |
| Protection de Manipulation | Précautions standard applicables aux médicaments antinéoplasiques oraux |

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le lien mécanistique entre Darolutamide et l'HoFH est extrêmement indirect — aucune donnée préclinique ou clinique ne soutient cette indication, et la prédiction est de niveau L5 (modèle uniquement). Une poursuite de l'évaluation n'est pas justifiée à ce stade.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données complètes sur le mécanisme d'action (MOA) de Darolutamide (source : DrugBank API)
- Notice ANSM/EMA complète pour mises en garde, contre-indications et interactions médicamenteuses
- Études précliniques évaluant l'effet de l'inhibition de l'AR sur l'expression du LDLR dans des modèles HoFH
- Revue de littérature ciblée sur androgènes et métabolisme du cholestérol hépatique

---

## Annexe — Autres Indications Prédites (Dossier Multi-Indications)

Ce dossier couvre 3 indications prédites. Les résumés des indications #2 et #3 sont présentés ci-dessous.

### Indication #2 : Néoplasie Endocrinienne Multiple (MEN)

| Élément | Contenu |
|---|---|
| Score de Prédiction TxGNN | 99,06 % |
| Niveau de Preuve | L4 |
| Décision Recommandée | Research Question |

**Rationnel mécanistique :** L'expression de l'AR a été rapportée dans certaines tumeurs associées à MEN2 (carcinome médullaire thyroïdien, phéochromocytome). La signalisation AR pourrait participer aux voies de prolifération dans ces tumeurs. L'inhibition par Darolutamide est biologiquement plausible pour les tumeurs MEN AR-positives, mais aucune donnée directe n'est disponible.

**Essai clinique identifié :**

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---|---|---|---|---|
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | Terminé | 2 | Essai panier multi-tumeurs (SMMART PRIME) évaluant des combinaisons moléculaires selon profil tumoral ; Darolutamide est l'un des agents testés, sans ciblage spécifique de la MEN. Essai terminé prématurément avec seulement 2 patients — aucune conclusion possible. Pertinence indirecte (grade C). |

---

### Indication #3 : Maladie Infectieuse à VIH

| Élément | Contenu |
|---|---|
| Score de Prédiction TxGNN | 99,04 % |
| Niveau de Preuve | L5 |
| Décision Recommandée | Research Question |

**Rationnel mécanistique :** La signalisation androgénique influence la fonction des lymphocytes T CD4+, l'activation immunitaire et la dynamique de réplication du VIH. Les androgènes favoriseraient le maintien du réservoir viral et inhiberaient certains mécanismes d'élimination immunitaire. Des études parallèles sur les antagonistes de l'AR dans le contexte SARS-CoV-2 apportent un soutien indirect à l'hypothèse immunomodératrice. L'hypothèse est biologiquement cohérente mais non vérifiée spécifiquement pour le VIH.

Aucun essai clinique ni littérature associés disponibles actuellement pour cette indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

