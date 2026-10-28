---
layout: default
title: Ivosidenib
parent: Prédiction du modèle uniquement (L5)
nav_order: 421
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
monitor_inn: "ivosidenib"
predicted_indications: ["bulbar polio"]
description: "Ivosidenib : nouvelle indication prédite, Poliomyélite bulbaire (bulbar polio) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Ivosidenib
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

## Ivosidenib: Poliomyélite bulbaire (bulbar polio)
{: .text-alpha }

## Résumé en Une Phrase

Ivosidénib est un inhibiteur de l'enzyme IDH1 mutée, initialement utilisé dans le traitement de la leucémie myéloïde aiguë (LAM).
Le modèle TxGNN (apprentissage profond) prédit qu'il pourrait être efficace pour la **poliomyélite bulbaire**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction. L'analyse mécanistique ne retient aucun lien biologique plausible : le score élevé provient du modèle TxGNN et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Poliomyélite bulbaire (bulbar polio) |
| Score de Prédiction TxGNN | 0.9931 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, l'ivosidénib inhibe l'isocitrate déshydrogénase 1 (IDH1) mutée. Il réduit l'oncométabolite 2-hydroxyglutarate (2-HG) et lève le blocage de différenciation observé dans les hémopathies myéloïdes porteuses d'une mutation IDH1.

La poliomyélite bulbaire est une infection virale des motoneurones causée par le poliovirus. Elle ne dépend ni d'une mutation d'IDH1 ni de la signalisation par le 2-HG. **Aucun lien mécanistique plausible n'a été identifié** entre l'indication d'origine et cette nouvelle indication. Le score TxGNN très élevé (0,9931) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une justification biologique.

### Autres prédictions du modèle

Deux autres prédictions de score très proche (0,9931) sont biologiquement plus plausibles :

- **LAM et syndromes myélodysplasiques liés à la radiothérapie**
- **LAM et syndromes myélodysplasiques liés aux agents alkylants**

Ces entités sont des néoplasmes myéloïdes secondaires à un traitement, qui peuvent porter une mutation IDH1 dans une partie des cas. Un bénéfice éventuel serait limité aux patients porteurs de la mutation, quelle que soit l'étiologie. Elles recoupent largement les indications déjà listées (LAM et SMD liés au traitement, LAM liée aux inhibiteurs de la topoisomérase II). Il vaut mieux les traiter comme une question de sous-groupe défini par biomarqueur ou d'extension d'indication existante que comme un vrai repositionnement. Aucun essai ni publication spécifique n'a été fourni pour ces sous-types.

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
| 63239234 (annulée) | TIBSOVO 250 mg, comprimé pelliculé (LES LABORATOIRES SERVIER) | Comprimé pelliculé | Non renseignée |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur d'IDH1 mutée) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

Les mises en garde et contre-indications de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

- **Interactions Médicamenteuses** : 413 interactions sont recensées. Parmi les principales, de niveau **majeur** :
  - Aprépitant
  - Clarithromycine
  - Dolasétron
  - Palonosétron
  - Cisapride
  - Granisétron
  - Lévofloxacine

  Des interactions de niveau **modéré** sont aussi rapportées, notamment avec :
  - Famotidine
  - Lopéramide
  - Bisacodyl
  - Saxagliptine
  - Éliglustat
  - Linagliptine
  - Plusieurs laxatifs et préparations de lavage intestinal (picosulfate, polyéthylène glycol, sulfate de sodium, huile de ricin, glycérine, lactitol, lactulose)

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la poliomyélite bulbaire repose uniquement sur le modèle (niveau L5). Elle n'a aucun essai ni publication à l'appui et aucun lien mécanistique plausible. L'AMM française est de plus annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour l'évaluation de sécurité)
- Compléter les données sur le mécanisme d'action (via DrugBank)
- Pour la poliomyélite bulbaire : une justification biologique indépendante, faute de quoi la piste devrait être abandonnée
- Pour les LAM/SMD liés à la radiothérapie ou aux agents alkylants : évaluer la piste comme sous-groupe défini par le statut mutationnel IDH1, avec recherche d'études spécifiques
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

