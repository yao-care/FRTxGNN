---
layout: default
title: Lamotrigine
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 9
---

# Lamotrigine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Lamotrigine : De l'Épilepsie au Neoplasme du Nerf Trijumeau

## Résumé en Une Phrase

Lamotrigine est un antiépileptique à large spectre (bloqueur des canaux sodiques voltage-dépendants), utilisé notamment dans l'épilepsie et le trouble bipolaire. Le modèle TxGNN prédit un signal pour le **Néoplasme du Nerf Trijumeau**, mais ce signal n'est actuellement soutenu par **aucun essai clinique** et seulement **2 publications** qui ne portent pas sur un usage antitumoral — l'analyse jointe au dossier suspecte une confusion algorithmique entre les noeuds « névralgie » et « néoplasme » trijéminal.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non documentée dans le dossier structuré (lacune DG002). D'après la littérature du dossier, lamotrigine est classée comme anticonvulsivant à large spectre, utilisé notamment dans l'épilepsie (crises partielles, absences) [PMID 20200383, 34931602] |
| Nouvelle Indication Prédite | Neoplasme du Nerf Trijumeau (*trigeminal nerve neoplasm*) |
| Score de Prédiction TxGNN | 99.97 % (rang 544) |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le mécanisme d'action détaillé de la lamotrigine n'est pas disponible dans ce dossier (lacune de données, DG002). D'après la littérature associée à ce candidat et aux prédictions voisines, la lamotrigine agit comme stabilisateur des canaux sodiques voltage-dépendants, réduisant la libération de glutamate et l'excitabilité neuronale — un mécanisme validé dans l'épilepsie et dans certaines douleurs neuropathiques (dont la névralgie du trijumeau, cf. rang 2 ci-dessous).

Ce mécanisme peut expliquer un bénéfice symptomatique sur une douleur neuropathique liée à une compression tumorale du nerf trijumeau, mais **il n'existe aucune preuve ni rationnel pharmacologique d'un effet antiprolifératif ou antitumoral** de la lamotrigine. Les deux publications rattachées à cette prédiction traitent en réalité de traitements (chirurgicaux, radiochirurgicaux) de la névralgie du trijumeau, pas du néoplasme du nerf trijumeau en tant que tel.

L'évaluation jointe au dossier signale explicitement que cette indication est **probablement un artefact du modèle** : TxGNN semble avoir confondu le nœud « névralgie du trijumeau » (*trigeminal neuralgia*, une entité douloureuse fonctionnelle) avec le nœud « néoplasme du nerf trijumeau » (*trigeminal nerve neoplasm*, une entité tumorale structurelle) — deux concepts proches lexicalement mais cliniquement très différents.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Revue | Expert Review of Neurotherapeutics | Panorama des traitements médicaux et chirurgicaux de la névralgie du trijumeau (douleur faciale) ; ne traite pas d'un néoplasme ni d'un effet antitumoral |
| [30650431](https://pubmed.ncbi.nlm.nih.gov/30650431/) | 2018 | Rapport de cas | Stereotactic and Functional Neurosurgery | Traitement par radiochirurgie Gamma Knife d'une névralgie du trijumeau causée par un cavernome ; approche non médicamenteuse, sans lien avec la lamotrigine |

Aucune des deux publications ne soutient directement l'indication « néoplasme du nerf trijumeau ».

---

## Informations de Marché en France

Aucune AMM enregistrée — médicament non commercialisé selon les données disponibles dans ce dossier (0 licence recensée).

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

*Note : la collecte des mises en garde/contre-indications TFDA est marquée comme lacune bloquante (DG001) dans ce dossier — elle empêche toute évaluation de sécurité initiale (étape S1) pour ce candidat.*

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Niveau de preuve L5 (aucun essai clinique, littérature non spécifique à l'indication) et stade de décision S0.
- Le lien mécanistique est absent : la lamotrigine n'a pas de propriété antitumorale connue, et l'indication est suspectée d'être une confusion du modèle entre « névralgie » et « néoplasme » trijéminal plutôt qu'un signal biologique réel.
- La lacune bloquante sur les mises en garde/contre-indications (DG001) empêche de toute façon la progression vers une évaluation de sécurité (S1).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération des mises en garde/contre-indications TFDA (DG001, bloquant) pour permettre une évaluation de sécurité de base.
- Confirmation du mécanisme d'action (MOA) via DrugBank (DG002).
- Vérification auprès de l'équipe modèle de la confusion présumée entre les nœuds « trigeminal neuralgia » et « trigeminal nerve neoplasm » dans le graphe TxGNN.
- À titre de comparaison, la prédiction voisine « **névralgie du trijumeau** » (rang 2, score 99.89 %) dispose d'un niveau de preuve nettement supérieur (L2, plusieurs essais Phase 2/3 complétés dont NCT00913107 et NCT00203229) et d'une recommandation « Proceed with Guardrails » — elle constitue un signal plus solide à prioriser que le présent candidat.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

