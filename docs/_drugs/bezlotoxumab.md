---
layout: default
title: Bezlotoxumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 56
evidence_level: L5
indication_count: 10
---

# Bezlotoxumab
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

# Bézlotoxumab : De la prévention des récidives d'infection à C. difficile à la péritonite pelvienne aiguë de la femme

## Résumé en Une Phrase

Le bézlotoxumab est un anticorps monoclonal qui neutralise la toxine B de *Clostridioides difficile*. Il est connu pour être utilisé contre les récidives d'infection à *C. difficile*, mais cette indication n'est pas renseignée dans les données ANSM reçues.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **péritonite pelvienne aiguë de la femme**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM (usage connu : récidives d'infection à *C. difficile*) |
| Nouvelle Indication Prédite | Péritonite pelvienne aiguë de la femme |
| Score de Prédiction TxGNN | 99,89 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les connaissances générales, le bézlotoxumab est un anticorps dirigé contre la toxine B de *C. difficile*. Son rôle est de neutraliser cette toxine, et non d'agir directement sur la bactérie.

**Ici, la prédiction ne repose sur aucun lien mécanistique établi.** La péritonite pelvienne est en général polymicrobienne (bactéries entériques à Gram négatif, anaérobies, *Chlamydia*, *Neisseria*). Aucun rôle de la toxine B de *C. difficile* n'y est démontré. Le seul recoupement imaginable serait une infection à *C. difficile* survenant comme complication d'une antibiothérapie. Il s'agirait alors de l'usage déjà connu (prévention des récidives) et non d'une nouvelle indication.

Le score élevé reflète probablement la proximité dans le graphe de connaissances, et non une preuve biologique. Les neuf autres prédictions les mieux classées sont toutes des affections gynécologiques, pelviennes ou abdominales, ou musculo-squelettiques : trompe de Fallope, grossesse extra-utérine, ligament large, sténose lombaire, varices pelviennes, etc. Elles ont le même niveau de preuve (L5), aucune donnée clinique et aucun lien plausible avec la neutralisation d'une toxine bactérienne.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69894104 | ZINPLAVA 25 mg/mL, solution à diluer pour perfusion (MERCK SHARP & DOHME, Pays-Bas) | Solution à diluer pour perfusion | Non renseignée dans les données reçues |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données reçues.

Comme il s'agit d'un anticorps dirigé contre une toxine bactérienne, son utilisation dans des affections liées à la grossesse (grossesse extra-utérine, par exemple) soulèverait des questions de sécurité qui n'ont pas été étudiées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication.
- Elle ne s'appuie sur aucun lien mécanistique plausible avec la neutralisation de la toxine B.
- Les données de sécurité de l'ANSM manquent, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications) et l'indication approuvée de l'AMM.
- Compléter les données sur le mécanisme d'action via DrugBank.
- Faire une revue de la littérature pour rechercher un rôle de *C. difficile* ou de la toxine B dans les affections pelviennes prédites.
- Ne relancer l'évaluation que si un lien biologique plausible est identifié. Sinon, considérer cette prédiction comme un artefact du modèle.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

