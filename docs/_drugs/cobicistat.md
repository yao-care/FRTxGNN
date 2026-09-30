---
layout: default
title: Cobicistat
parent: Prédiction du modèle uniquement (L5)
nav_order: 89
evidence_level: L5
indication_count: 3
---

# Cobicistat
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

# Cobicistat : D'un booster pharmacocinétique du VIH-1 au syndrome d'immunodéficience acquise féline

## Résumé en Une Phrase

Le cobicistat est un inhibiteur du CYP3A utilisé comme « booster » pharmacocinétique : il augmente l'exposition à certains antirétroviraux du VIH-1 (inhibiteurs de protéase et d'intégrase). Le modèle TxGNN prédit qu'il pourrait être utile dans le **syndrome d'immunodéficience acquise féline**. **Aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction : c'est une hypothèse de recherche.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM ; usage clinique : booster pharmacocinétique d'antirétroviraux (VIH-1) |
| Nouvelle Indication Prédite | Syndrome d'immunodéficience acquise féline |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le cobicistat n'a pas d'activité antivirale propre. Il inhibe le CYP3A, l'enzyme qui métabolise de nombreux antirétroviraux, et permet ainsi de maintenir des concentrations efficaces de ces molécules. Les données détaillées sur son mécanisme d'action ne sont pas disponibles dans le dossier, et l'indication originale n'est pas renseignée dans les AMM.

Le virus de l'immunodéficience féline (FIV) est un lentivirus apparenté au VIH-1. Une approche fondée sur un antirétroviral « boosté » est donc concevable. Tout bénéfice viendrait du renforcement d'un antiviral co-administré, et non du cobicistat seul. La pharmacocinétique féline et l'homologie du CYP3A chez le chat n'ont pas été vérifiées.

Le même raisonnement vaut pour l'**infection par le virus de l'immunodéficience simienne (SIV)**, modèle animal du VIH chez les primates non humains. Son score TxGNN est identique (99,92 %), ce qui suggère un signal de voisinage commun dans le graphe de connaissances plutôt qu'une preuve indépendante. Une troisième prédiction, un trouble neurodéveloppemental rare avec ataxie, absence de parole et réduction de la substance blanche corticale (score 99,91 %), n'a aucun lien mécanistique identifiable avec l'inhibition du CYP3A. Elle est placée en attente (Hold).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65768058 | STRIBILD 150 mg/150 mg/200 mg/245 mg | Comprimé pelliculé | Non renseignée dans les données |
| 65453475 | GENVOYA 150 mg/150 mg/200 mg/10 mg | Comprimé pelliculé | Non renseignée dans les données |

Les deux spécialités sont fabriquées par Gilead Sciences Ireland UC (Irlande). Ce sont des associations à dose fixe contenant du cobicistat.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication. Le cobicistat n'a pas d'effet antiviral propre et son bénéfice éventuel dépendrait d'un antiviral associé. Les données de sécurité de l'ANSM manquent également, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde et contre-indications) pour le criblage de sécurité
- Obtenir les données de mécanisme d'action depuis DrugBank
- Vérifier la pharmacocinétique féline et l'homologie du CYP3A chez le chat et le primate non humain
- Identifier un antiviral partenaire pertinent pour le FIV ou le SIV, puis définir une étude préclinique de schéma « boosté »
- Établir un rationnel au niveau de la cible pour le trouble neurodéveloppemental avant de reconsidérer cette prédiction
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

