---
layout: default
title: Clopidogrel
parent: 僅模型預測 (L5)
nav_order: 84
evidence_level: L5
indication_count: 8
---

# Clopidogrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Clopidogrel : De la Prévention Thromboembolique à la Migraine avec Aura du Tronc Cérébral

## Résumé en Une Phrase

Clopidogrel est un agent antiplaquettaire de la classe des thiénopyridines, largement utilisé en prévention cardiovasculaire (syndrome coronarien aigu, AVC ischémique) via le blocage irréversible du récepteur plaquettaire P2Y12.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Migraine avec Aura du Tronc Cérébral**,
avec **0 essai clinique spécifique** à ce sous-type et **16 publications** soutenant actuellement cette direction — la quasi-totalité issue de la littérature sur la migraine avec aura en contexte de foramen ovale perméable (FOP).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Prévention thromboembolique (syndrome coronarien aigu, AVC ischémique — indication internationale connue, non enregistrée dans les données fournies) |
| Nouvelle Indication Prédite | Migraine avec aura du tronc cérébral |
| Score de Prédiction TxGNN | 99,44 % |
| Niveau de Preuve | L3 |
| Statut de Marché | Non commercialisé (selon données réglementaires fournies) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Research Question |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier. Sur la base des informations connues dans la littérature internationale, clopidogrel est un inhibiteur irréversible du récepteur P2Y12 à l'ADP sur les plaquettes : il bloque l'activation plaquettaire dépendante de l'ADP, réduit l'agrégation plaquettaire et diminue la libération de sérotonine (5-HT) par les plaquettes activées. Ces propriétés, bien établies pour la prévention cardiovasculaire, constituent le point d'entrée mécanistique vers la migraine.

La migraine avec aura du tronc cérébral (anciennement « migraine de type basilaire ») implique des mécanismes ischémiques de la circulation postérieure (vertébro-basilaire). Un lien physiopathologique est établi entre le foramen ovale perméable (FOP) et la migration de micro-emboles veineux vers la circulation cérébrale, contournant le filtre pulmonaire. Ces micro-emboles peuvent déclencher une dépression corticale envahissante (CSD) — substrat neurologique de l'aura — dans le territoire du tronc cérébral, plus vulnérable à cette voie paradoxale. De plus, les études précliniques (PMID 34363208, PMID 31722730) montrent que le récepteur P2Y12 est exprimé sur les astrocytes et la microglie, et module directement le seuil de la CSD et l'activation microgliale dans le noyau caudal du trijumeau.

Cependant, ce sous-type spécifique « aura du tronc cérébral » ne dispose d'aucun essai clinique indépendant dédié. Les preuves disponibles proviennent de la population générale « migraine avec aura » en contexte de FOP, et leur extrapolation au sous-type tronc cérébral, bien que mécanistiquement plausible (circulation postérieure plus exposée aux micro-emboles paradoxaux), reste non validée cliniquement. À noter : la deuxième indication prédite, **migraine disorder** (Rang 2, TxGNN 99,43 %), dispose d'un niveau de preuve nettement supérieur (L2 — essai CANOA, Phase 4, n=220, complété, publié dans *JAMA* et *JAMA Cardiology*), ce qui renforce la crédibilité biologique globale de la prédiction.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé à la migraine avec aura du tronc cérébral enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Revue Systématique | *Headache* | Revue systématique sur le rôle des antithrombotiques dans la prévention de la migraine, incluant les sous-types avec aura ; clopidogrel identifié comme candidat d'intérêt |
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | ECR | *European Heart Journal* | Essai PRIMA : fermeture percutanée du FOP chez migraineurs avec aura réfractaires au traitement médicamenteux ; clopidogrel intégré au protocole post-procédure |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | Pilot ECR | *Cephalalgia* | Essai pilote randomisé contrôlé : clopidogrel évalué en prophylaxie de la migraine avec sous-groupe avec aura — signal positif préliminaire |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Cohorte Rétrospective | *J Investig Med* | Clopidogrel 75 mg/j ajouté au régime prophylactique chez migraineurs avec FOP réfractaires à ≥2 traitements préventifs ; 56,8 % présentaient un FOP confirmé ; réduction significative des crises |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Cohorte Observationnelle | *Heart* | Clopidogrel réduit la migraine avec aura après fermeture transcathéter de shunts auriculaires (FOP et CIA) ; observation clinique ayant initié le champ de recherche |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Pilote Open-Label | *Neurology* | Essai TRACTOR — ticagrélor pour migraine réfractaire/FOP ; étude initiée suite aux résultats positifs des thiénopyridines (clopidogrel, prasugrel), fournissant une validation indirecte de la classe |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Revue Rétrospective | *Neurology* | Revue rétrospective des thiénopyridines (incluant clopidogrel et prasugrel) chez migraineurs avec FOP ; réduction de fréquence des crises documentée en pratique clinique réelle |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Revue Rétrospective | *Cephalalgia* | Clopidogrel en thérapie primaire chez migraineurs avec shunt droit→gauche ; lien mécanistique avec activation plaquettaire et embolisation paradoxale décrit |
| [33815258](https://pubmed.ncbi.nlm.nih.gov/33815258/) | 2021 | Rapport de Cas | *Front. Neurology* | Migraine avec aura visuelle déclenchée par coiling endovasculaire d'un anévrisme de l'artère cérébrale postérieure — pertinence anatomique directe pour l'aura du territoire du tronc cérébral |
| [36588875](https://pubmed.ncbi.nlm.nih.gov/36588875/) | 2022 | Rapport de Cas | *Front. Neurology* | Fistule artério-veineuse pulmonaire (PAVF) associée à la migraine avec aura : mécanisme de shunt droit→gauche analogue au FOP, soutenant la généralisation du concept micro-embolique |

---

## Informations de Marché

Aucune AMM disponible dans les données réglementaires fournies (statut : non commercialisé, 0 licence enregistrée).

> **Contexte :** Clopidogrel (ex. Plavix®, Générique) est un médicament établi sur les marchés internationaux pour la prévention cardiovasculaire, disposant de larges programmes d'AMM en Europe, Amérique du Nord et Asie. L'absence de données dans ce dossier reflète le périmètre de la requête réglementaire effectuée et non l'inexistence du produit.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

> **Note de vigilance spécifique à cette indication :** Le PMID 38107217 (2023, *Cureus*) rapporte un cas d'arthrite inflammatoire induite par clopidogrel — bien que non directement lié à la migraine, ce signal suggère des effets immunomodulateurs inattendus à surveiller. Par ailleurs, le profil de résistance pharmacogénomique CYP2C19 (polymorphismes fréquents en population asiatique) est susceptible de modifier significativement l'efficacité antiplaquettaire et devra être considéré dans la conception d'un futur essai.

---

## Conclusion et Prochaines Étapes

**Décision : Research Question**

**Justification :**
La migraine avec aura du tronc cérébral est un sous-type rare et anatomiquement spécifique pour lequel aucun essai clinique dédié n'a été mené avec clopidogrel. Bien que la plausibilité mécanistique soit robuste (micro-embolisation paradoxale via FOP → circulation postérieure → CSD de type tronc cérébral ; inhibition P2Y12 réductrice de 5-HT plaquettaire et modulatrice de la CSD), les preuves cliniques disponibles (niveau L3) sont indirectes et extrapolées depuis la population générale « migraine avec aura/FOP ». La puissance de l'indication secondaire connexe (migraine disorder, L2, CANOA *JAMA* 2015/2021) constitue un signal d'encouragement, mais ne suffit pas à valider ce sous-type précis sans données spécifiques.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les données complètes sur le mécanisme d'action (DrugBank MOA — remédiation DG002)
- Récupérer les avertissements, contre-indications et interactions médicamenteuses officiels (remédiation DG001)
- Concevoir un sous-groupe pré-spécifié « aura du tronc cérébral » dans un futur essai sur la migraine/FOP (exploiter les cohortes CANOA, COMPETE ou SPRING en cours)
- Intégrer un dépistage systématique du FOP (ETO ou TCD avec injection de microbulles) dans le protocole de recrutement
- Réaliser un génotypage CYP2C19 des participants pour stratifier les non-répondeurs potentiels au clopidogrel
- Évaluer les résultats de l'essai NCT00799045 (CANOA, complété) pour analyse en sous-groupe aura du tronc cérébral si données individuelles disponibles
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

