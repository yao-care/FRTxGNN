---
layout: default
title: Sulfasalazine
parent: Prédiction du modèle uniquement (L5)
nav_order: 292
evidence_level: L5
indication_count: 10
---

# Sulfasalazine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Sulfasalazine : De l'indication d'origine (non renseignée) au syndrome de brachydactylie-syndactylie

## Résumé en Une Phrase

La sulfasalazine est commercialisée en France (Salazopyrine 500 mg, comprimé enrobé gastro-résistant), mais l'indication d'origine n'est pas renseignée dans les données réglementaires disponibles.
Le modèle TxGNN la prédit comme potentiellement efficace pour le **syndrome de brachydactylie-syndactylie**, une malformation congénitale rare des membres.
Cette prédiction ne repose sur **aucun essai clinique** et **aucune publication** : c'est une sortie de modèle seule.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM |
| Nouvelle Indication Prédite | Syndrome de brachydactylie-syndactylie |
| Score de Prédiction TxGNN | 99,94 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les éléments d'analyse, la sulfasalazine exerce une action anti-inflammatoire, avec une inhibition de la voie NF-kB et du transporteur cystine/glutamate xCT.

L'analyse n'identifie **aucun lien mécanistique plausible** avec le syndrome de brachydactylie-syndactylie. Il s'agit d'une malformation congénitale rare des membres, dont la physiopathologie relève du développement embryonnaire. Elle n'a pas de rapport évident avec les effets anti-inflammatoires du médicament.

Le score TxGNN est très élevé (0,999), mais il reflète une proximité dans le graphe de connaissances, pas une preuve d'efficacité. Sans essai ni publication, cette prédiction doit être considérée comme non corroborée. La similarité avec l'indication d'origine reste à évaluer.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67124724 | SALAZOPYRINE 500 mg, comprimé enrobé gastro-résistant (PFIZER HOLDING FRANCE) | Comprimé enrobé gastro-résistant | Non renseignée dans les données |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le niveau de preuve est L5 : aucun essai, aucune publication, et aucun lien mécanistique plausible avec une malformation congénitale du développement des membres.
- Les données de sécurité de la notice ANSM sont absentes, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications) et l'indication approuvée de l'AMM.
- Obtenir les données sur le mécanisme d'action via l'API DrugBank.
- Établir un lien mécanistique et des données précliniques pour justifier la prédiction.

**Remarque :** dans le même dossier, deux autres prédictions sont mieux étayées et méritent d'être examinées en priorité (niveau L4, décision « Research Question »).
- **Arthrose** (score 99,64 %) : plusieurs études précliniques (modèles animaux et cartilage in vitro) vont dans le sens d'un effet protecteur. La pertinence des deux essais cliniques retrouvés n'est pas confirmée, et l'efficacité chez l'humain reste non démontrée.
- **Spondylarthropathie, susceptibilité** (score 99,53 %) : la littérature retrouvée se compose surtout de revues et d'études observationnelles ou génétiques, sans essai.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

