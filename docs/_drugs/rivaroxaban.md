---
layout: default
title: Rivaroxaban
parent: Prédiction du modèle uniquement (L5)
nav_order: 675
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Rivaroxaban : nouvelle indication prédite, Polyarthrite rhumatoïde (niveau de preuve L5). Indication d'origine : Non renseignée dans les données compilées"
---

# Rivaroxaban
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Rivaroxaban : De l'anticoagulation à la polyarthrite rhumatoïde

## Résumé en Une Phrase

Rivaroxaban est un anticoagulant oral inhibiteur direct du facteur Xa. Les données compilées pour ce rapport ne contiennent toutefois pas de texte d'indication officiel pour les AMM françaises.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **polyarthrite rhumatoïde**, mais **aucun essai clinique** ni **aucune publication** n'évalue réellement cet usage : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données compilées |
| Nouvelle Indication Prédite | Polyarthrite rhumatoïde |
| Score de Prédiction TxGNN | 99,57 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances générales, le rivaroxaban est un inhibiteur du facteur Xa, utilisé en prévention et traitement des événements thromboemboliques.

Une hypothèse indirecte existe : l'inflammation auto-immune est associée à un état d'hypercoagulabilité et à une génération accrue de thrombine, qui pourrait être une cible de l'inhibition du facteur Xa. Une revue française de 2021 sur le test de génération de thrombine dans les maladies auto-immunes va dans ce sens, mais sans évaluer le rivaroxaban.

Cette hypothèse ne suggère **aucune activité modificatrice de la maladie**. Le score élevé du modèle (0,996) n'est pas corroboré par des données cliniques.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune de ces publications n'évalue le rivaroxaban comme traitement de la polyarthrite rhumatoïde.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Revue | JAMA | Diagnostic et traitement de la thromboembolie veineuse des membres inférieurs ; contexte thromboembolique, pas d'évaluation dans la polyarthrite |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Revue | La Revue de médecine interne | Le test de génération de thrombine évalue l'hypercoagulabilité dans les maladies auto-immunes |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohorte | PloS one | Observance du rivaroxaban versus apixaban dans la fibrillation atriale non valvulaire |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Rapport de cas | Cureus | Infarctus cérébral thromboembolique chez une patiente de 88 ans sous corticoïdes pour polyarthrite rhumatoïde et anticoagulée ; la polyarthrite est une comorbidité |

## Informations de Marché en France

Les 20 AMM recensées sont toutes annulées ; aucun texte d'indication n'est disponible. Les 5 premières sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60474483 | RIVAROXABAN EVOLUGEN 20 mg | Comprimé pelliculé | Non renseignée |
| 68216702 | RIVAROXABAN ACCORD 15 mg | Comprimé pelliculé | Non renseignée |
| 61711184 | RIVAROXABAN VIATRIS 15 mg + 20 mg | Comprimé pelliculé | Non renseignée |
| 64290203 | RIVAROXABAN VIATRIS 15 mg | Comprimé pelliculé | Non renseignée |
| 67071218 | XARELTO 20 mg | Comprimé pelliculé | Non renseignée |

## Considérations de Sécurité

- **Maladies associées à une contre-indication (graphe de connaissances)** : insuffisance hépatique, maladie rénale, pyo-uretère, maladie hépatique, maladie de la vésicule biliaire, trouble de la coagulation sanguine. Ces éléments proviennent du graphe de connaissances et non du texte de la notice.
- **Interactions médicamenteuses** : 100 interactions recensées, dont les principales de niveau **majeur** :
  - Acide acétylsalicylique (risque hémorragique)
  - Cobicistat
  - Déférasirox
  - Ibritumomab tiuxétan
  - Tositumomab (I-131)

  Des interactions de niveau modéré existent aussi, notamment avec la clarithromycine, la cimétidine, la dexaméthasone, l'aprépitant et le miconazole.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé (99,57 %), mais il n'existe ni essai clinique ni publication évaluant l'efficacité du rivaroxaban dans la polyarthrite rhumatoïde (niveau L5). Les données de sécurité officielles sont absentes et le médicament n'a plus d'AMM valide en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde, contre-indications, indications) pour le dépistage de sécurité
- Obtenir les données sur le mécanisme d'action depuis DrugBank
- Mener des études précliniques ou observationnelles sur le lien entre génération de thrombine et activité de la polyarthrite
- Clarifier le statut réglementaire en France, toutes les AMM étant annulées
- Évaluer le rapport bénéfice/risque hémorragique chez des patients souvent sous corticoïdes ou AINS
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

