---
layout: default
title: Fomepizole
parent: Prédiction du modèle uniquement (L5)
nav_order: 345
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Fomepizole : nouvelle indication prédite, Cholangite sclérosante (niveau de preuve L5). Indication d'origine : Non renseignée dans l'AMM (texte d'indication vide)"
monitor_inn: "fomepizole"
predicted_indications: ["sclerosing cholangitis"]
---

# Fomepizole
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

## Fomépizole : D'une indication d'origine non renseignée à la cholangite sclérosante
{: .text-alpha }

## Résumé en Une Phrase

Le fomépizole est un inhibiteur de l'alcool déshydrogénase, utilisé en clinique dans les intoxications à l'éthylène glycol et au méthanol. Les données compilées pour ce rapport ne contiennent pas de texte d'indication issu de l'ANSM.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **cholangite sclérosante**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans l'AMM (texte d'indication vide) |
| Nouvelle Indication Prédite | Cholangite sclérosante |
| Score de Prédiction TxGNN | 0,9928 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances générales, le fomépizole est un inhibiteur compétitif de l'alcool déshydrogénase. Il est utilisé en clinique pour les intoxications à l'éthylène glycol et au méthanol, en bloquant la transformation de ces substances en métabolites toxiques.

Un lien plausible, mais **non vérifié**, serait une modulation de l'alcool déshydrogénase et du stress oxydatif lié au CYP2E1, ainsi que du métabolisme des acides biliaires ou des aldéhydes dans les cholangiocytes. Aucune étude mécanistique, aucun modèle préclinique et aucune observation clinique n'a été fournie pour étayer ce lien.

Le seul appui est donc le score TxGNN très élevé (0,9928). Ce score provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique. La similarité avec l'indication d'origine ne peut pas être évaluée, faute de données.

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
| 63945150 | FOMEPIZOLE AP-HP 5 mg/mL, solution à diluer pour perfusion (AP-HP) | Solution à diluer pour perfusion | Non renseignée (AMM active) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie de PrimeKG, et non texte de la notice) : maladie rénale, pyourètre (pus dans l'uretère), maladie hépatique, maladie de la vésicule biliaire. Ces éléments sont à interpréter avec prudence : la maladie hépatobiliaire concerne directement la nouvelle indication visée.
- **Interactions médicamenteuses** : 1 interaction de niveau **majeur** identifiée, avec l'**éthanol** (source : DDInter).

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur un score de modèle (niveau L5), sans essai, publication ni donnée mécanistique. De plus, l'unique AMM française est annulée et les données de sécurité officielles sont absentes, ce qui bloque l'évaluation de sécurité.
- Les contre-indications du graphe de connaissances (maladies hépatique et biliaire) appellent une vigilance particulière pour une indication hépatobiliaire.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications officielles de la notice sur le site de l'ANSM
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Réaliser une revue de la littérature et des études précliniques sur le lien entre l'inhibition de l'alcool déshydrogénase et la cholangite sclérosante
- Clarifier la situation réglementaire (AMM annulée) et la faisabilité de la voie d'administration (perfusion) pour cette indication
- Évaluer la sécurité du fomépizole chez les patients atteints d'une atteinte hépatique ou biliaire
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

