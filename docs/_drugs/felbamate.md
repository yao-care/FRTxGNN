---
layout: default
title: Felbamate
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 2
---

# Felbamate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Felbamate : De l'Antiépileptique au Néoplasme du Nerf Trijumeau

## Résumé en Une Phrase

Felbamate est un anticonvulsant agissant par blocage des canaux sodiques voltage-dépendants et antagonisme des récepteurs NMDA, initialement développé pour le traitement de l'épilepsie réfractaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Néoplasme du Nerf Trijumeau**,
avec **0 essai clinique** et **0 publication** soutenant directement cette direction.

> ⚠️ La deuxième prédiction — **Névralgie du Trijumeau** (rang 2, score 99,18 %) — présente un rationnel mécanistique nettement plus cohérent et dispose de 5 publications ; ses données sont présentées en section complémentaire ci-dessous.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Épilepsie réfractaire (anticonvulsant) |
| Nouvelle Indication Prédite | Néoplasme du Nerf Trijumeau |
| Score de Prédiction TxGNN | 99,62 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action de Felbamate ne sont pas disponibles dans le dossier actuel. Sur la base des informations connues dans la littérature, Felbamate est un anticonvulsant à double mécanisme : il bloque les canaux sodiques voltage-dépendants (réduisant l'excitabilité neuronale) et antagonise les récepteurs NMDA (inhibant la potentialisation synaptique). Ces deux actions convergent vers la suppression de l'hyperexcitabilité dans l'épilepsie réfractaire.

Concernant la prédiction pour le néoplasme du nerf trijumeau, le score élevé du modèle TxGNN (0,996) est vraisemblablement attribuable à une similarité anatomique et topographique — le nerf trijumeau est impliqué dans les deux contextes (néoplasie et douleur neurogène) — plutôt qu'à une relation mécanistique directe. En effet, le mécanisme sodium/NMDA de Felbamate ne possède aucune cible antiproliférative connue sur les cellules tumorales ; une indication oncologique nécessiterait un mécanisme d'inhibition de la prolifération cellulaire que Felbamate ne détient pas.

En revanche, la prédiction de rang 2 (**Névralgie du Trijumeau**) repose sur un rationnel mécanistique bien étayé : le blocage des canaux Nav1.7/Nav1.3, principale cible de Felbamate, est identique à celui de la Carbamazépine — traitement de première ligne dans cette pathologie. L'antagonisme NMDA apporte une base théorique additionnelle en inhibant la sensibilisation centrale. Toutefois, le profil de sécurité préoccupant de Felbamate (voir section Considérations de Sécurité) constitue un obstacle clinique majeur.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour le néoplasme du nerf trijumeau.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour le néoplasme du nerf trijumeau.

---

## Données Complémentaires — Névralgie du Trijumeau (Prédiction Rang 2)

**Score TxGNN : 99,18 % | Niveau de Preuve : L4 | Décision : Research Question**

> Ces données concernent la deuxième indication prédite et sont présentées à titre informatif pour orienter les décisions de recherche.

### Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour la névralgie du trijumeau.

### Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [7549170](https://pubmed.ncbi.nlm.nih.gov/7549170/) | 1995 | Rapport de Cas | The Clinical Journal of Pain | Évaluation de l'efficacité analgésique de Felbamate dans la névralgie du trijumeau ; soulagement rapporté |
| [23338129](https://pubmed.ncbi.nlm.nih.gov/23338129/) | 1997 | Revue Narrative | CNS Drugs | Guide de choix médicamenteux pour la névralgie du trijumeau ; Felbamate cité parmi les anticonvulsants à activité analgésique |
| [22022008](https://pubmed.ncbi.nlm.nih.gov/22022008/) | 2011 | Étude Animale | Indian Journal of Pharmacology | Comparaison de l'efficacité de Carbamazépine, Gabapentine et Lamotrigine sur douleur neuropathique ; Felbamate référencé comme antiépileptique actif dans la névralgie |
| [8877250](https://pubmed.ncbi.nlm.nih.gov/8877250/) | 1996 | Revue (PK/DDI) | Clinical Pharmacokinetics | Interactions pharmacocinétiques cliniquement significatives de la Carbamazépine ; contexte d'utilisation dans la névralgie du trijumeau et profil d'interactions à connaître |
| [7633024](https://pubmed.ncbi.nlm.nih.gov/7633024/) | 1995 | Rapport de Cas (Effet Indésirable) | Annals of Pharmacotherapy | Anaphylaxie tardive induite par Felbamate — signal de sécurité à considérer impérativement |

---

## Informations de Marché en France

Felbamate n'est pas commercialisé en France. Aucune autorisation de mise sur le marché (AMM) n'a été délivrée par l'ANSM à ce jour.

---

## Considérations de Sécurité

Les données formelles de sécurité (avertissements, contre-indications) ne sont pas disponibles dans le dossier actuel.

Veuillez consulter la notice officielle pour les informations de sécurité complètes.

> ⚠️ **Signal de la littérature :** La publication PMID [7633024](https://pubmed.ncbi.nlm.nih.gov/7633024/) rapporte un cas d'**anaphylaxie tardive** associée à Felbamate. Par ailleurs, les données de pharmacovigilance publiées mentionnent des risques graves d'**anémie aplasique** et d'**hépatotoxicité**, effets ayant conduit à des restrictions d'utilisation dans plusieurs pays. Ces éléments représentent un frein clinique majeur pour tout développement en repositionnement.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction TxGNN pour le néoplasme du nerf trijumeau repose exclusivement sur une inférence du modèle sans aucun soutien clinique ou préclinique (niveau L5), et le mécanisme d'action de Felbamate ne présente pas de cible antiproliférative directe pertinente pour une indication oncologique.

> **Note sur la prédiction de rang 2 :** La névralgie du trijumeau (L4, Research Question) présente un rationnel mécanistique cohérent, mais le développement de Felbamate dans cette indication se heurte à un profil de sécurité préoccupant et à l'existence d'alternatives thérapeutiques mieux établies (Carbamazépine, Oxcarbazépine).

**Pour avancer, les éléments suivants sont nécessaires :**

- Données officielles sur le mécanisme d'action (MOA) — à récupérer via DrugBank API (Data Gap DG002)
- Notice ANSM / données de sécurité complètes — à télécharger et analyser (Data Gap DG001)
- Pour le néoplasme du nerf trijumeau : études précliniques démontrant une activité antiproliférative spécifique avant toute considération clinique
- Pour la névralgie du trijumeau : revue systématique ciblée et évaluation rigoureuse du rapport bénéfice/risque avec plan de monitoring hématologique (NFS, bilan hépatique) avant tout essai
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

