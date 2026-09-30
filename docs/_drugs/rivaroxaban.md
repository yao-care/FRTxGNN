---
layout: default
title: Rivaroxaban
parent: Prédiction du modèle uniquement (L5)
nav_order: 268
evidence_level: L5
indication_count: 4
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

Le rivaroxaban est un anticoagulant oral, inhibiteur direct du facteur Xa, utilisé en France dans la prévention et le traitement des maladies thromboemboliques. Le modèle TxGNN prédit qu'il pourrait être efficace pour la **polyarthrite rhumatoïde**.
À ce jour, **aucun essai clinique** et **4 publications seulement** sont associés à cette prédiction, et aucune de ces publications ne teste le rivaroxaban dans la polyarthrite rhumatoïde.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Polyarthrite rhumatoïde |
| Score de Prédiction TxGNN | 99,57 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement ; le pack indique L4, mais aucune étude ne teste le rivaroxaban dans la polyarthrite rhumatoïde) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la source. Le rivaroxaban est un inhibiteur direct du facteur Xa. Son efficacité dans les maladies thromboemboliques est établie, et il pourrait être applicable à la polyarthrite rhumatoïde uniquement sur la base d'une hypothèse.

Le lien mécanistique repose sur les interactions entre coagulation et inflammation. Le facteur Xa et la thrombine peuvent activer des voies inflammatoires via les récepteurs PAR. Un état d'hypercoagulabilité est par ailleurs décrit dans les maladies auto-immunes, comme le montre la revue sur le test de génération de thrombine.

Ce lien reste hypothétique. Aucune publication retrouvée n'évalue le rivaroxaban sur l'activité de la maladie ou les résultats cliniques de la polyarthrite rhumatoïde. Le score élevé de TxGNN est une prédiction computationnelle, sans confirmation expérimentale ou clinique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Revue | La Revue de médecine interne | Le test de génération de thrombine permet d'évaluer l'hypercoagulabilité dans les maladies auto-immunes (par ex. syndrome des antiphospholipides). Ne teste pas le rivaroxaban. |
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Revue | JAMA | Diagnostic et traitement de la thromboembolie veineuse des membres inférieurs. Concerne l'usage anticoagulant, pas la polyarthrite rhumatoïde. |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohorte | PloS one | Comparaison de l'observance du rivaroxaban et de l'apixaban dans la fibrillation atriale non valvulaire. Sans lien avec la polyarthrite rhumatoïde. |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Rapport de cas | Cureus | Infarctus cérébral thromboembolique périopératoire chez une patiente de 88 ans sous corticoïdes pour polyarthrite rhumatoïde. La polyarthrite n'est ici qu'une comorbidité. |

---

## Informations de Marché en France

Les textes d'indication approuvée ne sont pas renseignés dans les données.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 60474483 | RIVAROXABAN EVOLUGEN 20 mg | Comprimé pelliculé |
| 68216702 | RIVAROXABAN ACCORD 15 mg | Comprimé pelliculé |
| 61711184 | RIVAROXABAN VIATRIS 15 mg + 20 mg | Comprimé pelliculé (deux dosages) |
| 64290203 | RIVAROXABAN VIATRIS 15 mg | Comprimé pelliculé |
| 67071218 | XARELTO 20 mg | Comprimé pelliculé |

Ces 5 AMM sont les principales sur un total de 20.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle : aucun essai clinique, et aucune publication ne teste le rivaroxaban dans la polyarthrite rhumatoïde.
- Les données de sécurité de la notice ANSM manquent, ce qui bloque le passage à l'étape de criblage de sécurité.
- Les trois autres prédictions (goutte, infection à VIH, syndrome brachydactylie-syndactylie) sont également non étayées. Pour le VIH, la littérature ne montre qu'un signal de sécurité et d'interactions, pas d'effet thérapeutique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (télécharger et analyser le PDF).
- Compléter le mécanisme d'action via DrugBank afin d'analyser le lien mécanistique.
- Renseigner les indications approuvées des AMM françaises pour confirmer l'indication d'origine.
- Mener une recherche ciblée (rivaroxaban, facteur Xa et polyarthrite rhumatoïde) pour identifier d'éventuelles études précliniques ou observationnelles.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

