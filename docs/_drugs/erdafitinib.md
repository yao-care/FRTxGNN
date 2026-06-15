---
layout: default
title: Erdafitinib
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 6
---

# Erdafitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Le skill txgnn-pipeline couvre le pipeline technique ; la génération de rapport suit les instructions du prompt v5. Je procède à la rédaction.

---

# Erdafitinib : Du Cancer Urothélial à l'Hypertension Pulmonaire

## Résumé en Une Phrase

Erdafitinib (BALVERSA®) est un inhibiteur pan-FGFR (FGFR1, 2, 3, 4) approuvé par la FDA pour le carcinome urothélial localement avancé ou métastatique portant des altérations des gènes FGFR2 ou FGFR3, actuellement non enregistré à Taïwan.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertension pulmonaire**,
avec **0 essai clinique** et **0 publication** soutenant directement cette direction — la prédiction repose exclusivement sur des liens computationnels dans le graphe de connaissances biologiques.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Carcinome urothélial avec altération FGFR2/FGFR3 (FDA, États-Unis ; non enregistré à Taïwan) |
| Nouvelle Indication Prédite (rang 1) | Hypertension pulmonaire |
| Score de Prédiction TxGNN | 99.38% |
| Niveau de Preuve | L5 |
| Statut de Marché à Taïwan | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce pack. Sur la base des informations pharmacologiques connues, Erdafitinib est un inhibiteur pan-FGFR (FGFR1/2/3/4) de petite molécule administré par voie orale, dont l'efficacité dans le carcinome urothélial présentant des altérations génomiques FGFR a été démontrée en contexte oncologique et ayant conduit à son approbation par la FDA.

FGFR1 est surexprimé dans les cellules musculaires lisses des artères pulmonaires (PASMC) dans l'hypertension artérielle pulmonaire (HAP), où il drive une prolifération anormale et un remodelage vasculaire pathologique. Des modèles précliniques in vitro et in vivo montrent que l'inhibition de FGFR peut réduire la résistance vasculaire pulmonaire, conférant une plausibilité mécanistique à cette prédiction.

Cependant, Erdafitinib ne dispose d'aucune donnée clinique dans la HAP. Les patients atteints de HAP présentent fréquemment une insuffisance cardiopulmonaire, imposant une vigilance particulière concernant le risque de cardiotoxicité potentielle. La direction mécanistique est biologiquement justifiable, mais le niveau de preuve reste strictement L5.

---

## Vue d'Ensemble des Six Indications Prédites

| Rang | Maladie | Score TxGNN | Preuve | Recommandation | Justification Clé |
|------|---------|------------|--------|----------------|-------------------|
| 1 | Hypertension pulmonaire | 99.38% | L5 | Research Question | FGFR1 surexprimé dans les PASMC ; plausibilité biologique, aucune donnée clinique |
| 2 | Cardiopathie cyphoscoliotique | 99.27% | L5 | Hold | Mécanisme purement mécanique (compression), non FGFR-dépendant |
| 3 | Aménorrhée | 99.26% | L5 | Hold | Erdafitinib **induit** l'aménorrhée en tant qu'EI — contradiction mécanistique directe |
| 4 | Polyarthrite rhumatoïde | 99.25% | L5 | Research Question | FGF2 élevé dans le liquide synovial ; hypothèse à valider en modèle cellulaire/animal |
| 5 | Sclérose latérale amyotrophique | 99.06% | L5 | Hold | FGF-2 est neuroprotecteur ; inhiber FGFR risque de compromettre la survie des motoneurones |
| 6 | Syndrome brachydactylie-syndactylie | 99.03% | L5 | Research Question | Sous-types FGFR2 GOF (ex. syndrome d'Apert) — potentiel de médecine de précision |

### Notes d'analyse par indication

**Hold — Cardiopathie cyphoscoliotique (Rang 2)**
La pathologie résulte d'une compression mécanique par déformation vertébrale rachidienne. Le mécanisme FGFR n'est pas impliqué dans la physiopathologie cardiaque secondaire. La prédiction semble issue d'associations indirectes squelette–cœur dans le graphe de connaissances. Pas de justification mécanistique valable.

**Hold — Aménorrhée (Rang 3)**
FGFR2 participe au développement folliculaire ovarien et à la prolifération endométriale, mais les inhibiteurs de FGFR — dont Erdafitinib — sont précisément documentés comme inducteurs d'irrégularités menstruelles et d'aménorrhée (effets indésirables connus dans l'indication approuvée). L'inhibiteur lui-même constitue une cause potentielle d'aménorrhée ; le recommander pour la traiter est mécanistiquement contradictoire.

**Hold — Sclérose latérale amyotrophique (Rang 5)**
Les ligands FGF (notamment FGF-2) exercent des propriétés neuroprotectrices sur les motoneurones. L'inhibition de la voie FGFR risque de compromettre la survie neuronale plutôt que de la soutenir — le mécanisme est opposé à l'objectif thérapeutique. De plus, la SLA implique de multiples voies pathologiques (agrégats TDP-43, stress oxydatif, neuroinflammation) bien au-delà de la seule voie FGFR.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé à Erdafitinib n'a été identifié pour les six indications prédites (requêtes ClinicalTrials.gov et ICTRP effectuées le 2026-04-20).

---

## Preuves de la Littérature

Aucune publication directement pertinente pour l'indication de rang 1 (hypertension pulmonaire). Une seule référence a été identifiée, pour la polyarthrite rhumatoïde (rang 4) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-------|------|-------|----------------------|
| [31862477](https://pubmed.ncbi.nlm.nih.gov/31862477/) | 2020 | Revue | Pharmacological Research | Revue des inhibiteurs de kinases approuvés par la FDA ; Erdafitinib figure parmi les 4 nouvelles approbations 2019, ciblant FGFR pour le carcinome urothélial. Aucune donnée spécifique à la polyarthrite rhumatoïde. |

---

## Informations de Marché (Taïwan)

Erdafitinib n'est actuellement pas enregistré à Taïwan (0 licence de mise sur le marché). Aucune donnée TFDA disponible.

À titre d'information comparative, le médicament est approuvé sous les noms commerciaux suivants hors Taïwan :

| Pays / Agence | Nom Commercial | Indication Approuvée |
|---------------|---------------|----------------------|
| États-Unis (FDA) | BALVERSA® | Carcinome urothélial localement avancé ou métastatique avec altérations FGFR2/FGFR3 |

---

## Cytotoxicité

Erdafitinib est un agent antinéoplasique (inhibiteur de tyrosine kinase ciblé sur FGFR) ; la section suivante s'applique.

| Élément | Contenu |
|---|---|
| Classification de Cytotoxicité | Thérapie ciblée — Inhibiteur pan-FGFR (FGFR1/2/3/4) ; non cytotoxique conventionnel |
| Risque de Myélosuppression | Faible à modéré (profil hématologique moins sévère que la chimiothérapie cytotoxique conventionnelle) |
| Classification d'Émétogénicité | Faible (voie orale, inhibiteur de kinase) |
| Éléments de Surveillance | NFS avec différentielle, bilan hépatique, fonction rénale, phosphatémie (hyperphosphatémie — effet de classe FGFR, requiert titration de dose), surveillance ophtalmologique (rétinopathie séreuse centrale et décollement de rétine — effets de classe documentés) |
| Protection de Manipulation | Doit respecter les recommandations standard de manipulation des médicaments anticancéreux oraux |

---

## Considérations de Sécurité

Veuillez consulter la notice officielle pour les informations de sécurité complètes. Les données de sécurité spécifiques (avertissements TFDA, contre-indications, interactions médicamenteuses) ne sont pas disponibles dans ce pack de données.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
L'ensemble des six indications prédites se situe au niveau de preuve L5 (prédiction computationnelle uniquement), sans aucun essai clinique ni publication directement pertinente pour Erdafitinib dans ces nouvelles indications. Trois pistes présentent une plausibilité mécanistique intéressante (hypertension pulmonaire, polyarthrite rhumatoïde, syndrome brachydactylie-syndactylie FGFR2 GOF) et méritent d'être documentées comme questions de recherche, mais les données probantes sont insuffisantes pour franchir l'étape S1.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mécanisme d'action complet (MOA) via DrugBank API
- Avertissements de sécurité et contre-indications (notice TFDA / FDA / EMA)
- Données précliniques (cellulaire/animale) pour l'hypertension pulmonaire : modèles PAH et inhibition FGFR1 dans les PASMC
- Données précliniques pour les sous-types FGFR2 GOF du syndrome brachydactylie-syndactylie (ex. modèles Apert)
- Évaluation du risque de cardiotoxicité chez des populations à fragilité cardiopulmonaire (HAP)
- Avis d'experts en médecine vasculaire pulmonaire et en maladies rares osseuses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

