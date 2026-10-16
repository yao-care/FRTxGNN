---
layout: default
title: Ustekinumab
parent: Preuves élevées (L1-L2)
nav_order: 800
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Ustekinumab : nouvelle indication prédite, Dermatite (niveau de preuve L2). Indication d'origine : Rhumatisme psoriasique, psoriasis, parapsoriasis"
---

# Ustekinumab
{: .fs-9 }

Niveau de preuve: **L2** | Indications prédites: **10** 
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

# Ustékinumab : Du Psoriasis à la Dermatite

## Résumé en Une Phrase

Ustékinumab est un anticorps monoclonal initialement utilisé pour le traitement du rhumatisme psoriasique, du psoriasis et du parapsoriasis.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **dermatite**, avec **6 essais cliniques** enregistrés (dont seulement 2 testent directement ustékinumab dans la dermatite atopique) et **aucune publication** disponible actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Rhumatisme psoriasique, psoriasis, parapsoriasis (selon le graphe de connaissances TxGNN ; le texte d'indication des AMM n'est pas disponible) |
| Nouvelle Indication Prédite | Dermatite |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | Uniquement annulées |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Selon l'analyse mécanistique disponible, ustékinumab bloque la sous-unité p40 commune à l'IL-12 et à l'IL-23, ce qui inhibe les voies Th1 et Th17. Ces voies sont impliquées dans le psoriasis, indication d'origine du médicament.

Ces mêmes voies contribuent à l'inflammation dans plusieurs sous-types de dermatite, notamment la dermatite atopique chronique. L'adéquation mécanistique reste toutefois **partielle** : la dermatite atopique est surtout dominée par la voie Th2 (IL-4/IL-13), ce qui pourrait expliquer l'efficacité limitée observée dans les essais.

Il convient aussi de noter que le score TxGNN élevé est en grande partie lié au terme très large et peu spécifique de « dermatite » et à sa proximité avec le psoriasis dans le graphe de connaissances. Ce score doit donc être interprété avec prudence.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01945086](https://clinicaltrials.gov/study/NCT01945086) | Phase 2 | Terminé | 79 | Étude randomisée en double aveugle contre placebo d'ustékinumab (2 doses) chez des adultes japonais atteints de dermatite atopique sévère ; pertinence probable, à vérifier |
| [NCT01806662](https://clinicaltrials.gov/study/NCT01806662) | Phase 2 | Terminé | 32 | Étude pilote randomisée d'ustékinumab dans la dermatite atopique chronique avec réponse sous-optimale aux traitements antérieurs ; petit effectif limitant les conclusions |
| [NCT05535738](https://clinicaltrials.gov/study/NCT05535738) | Phase 2/3 | Actif, non en recrutement | 45 | Modèle de dermatite de contact avec des biothérapies pour étudier l'inflammation cutanée ; étude mécanistique, rôle précis d'ustékinumab incertain |
| [NCT02074982](https://clinicaltrials.gov/study/NCT02074982) | Phase 3 | Terminé | 676 | Sécukinumab comparé à ustékinumab dans le psoriasis en plaques (CLEAR) ; pas de preuve directe dans la dermatite |
| [NCT01356758](https://clinicaltrials.gov/study/NCT01356758) | N/A | Terminé | 126 | Évaluation du risque cardiovasculaire chez des patients atteints de psoriasis sévère sous biothérapies ; ne porte pas sur l'efficacité dans la dermatite |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | Pas encore en recrutement | 10 | Microdispositif cutané pour tester des médicaments in situ (dermatite atopique, psoriasis) ; étude méthodologique sans preuve d'efficacité |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67522169 | STELARA 45 mg, solution injectable | Solution injectable | Non disponible (AMM annulée) |
| 65283311 | STELARA 45 mg, solution injectable en seringue préremplie | Solution injectable | Non disponible (AMM annulée) |
| 69661655 | STELARA 90 mg, solution injectable en stylo prérempli | Solution injectable | Non disponible (AMM annulée) |
| 66170398 | STELARA 90 mg, solution injectable en seringue préremplie | Solution injectable | Non disponible (AMM annulée) |
| 61145149 | OTULFI 130 mg, solution à diluer pour perfusion | Solution à diluer pour perfusion | Non disponible (AMM annulée) |

Au total, 20 AMM sont enregistrées (Stelara et plusieurs biosimilaires : Wezenla, Otulfi, Uzpruvo, Pyzchiva, Imuldosa, Yesintek, Steqeyma), toutes au statut annulé.

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 333 interactions sont recensées. Les principales, de niveau modéré, concernent les corticoïdes (hydrocortisone, triamcinolone, dexaméthasone, bétaméthasone, budésonide, prednisone, prednisolone), la simvastatine, les anticoagulants (apixaban, warfarine, rivaroxaban, dicoumarol) et des radiopharmaceutiques (iobenguane I-131, ibritumomab tiuxétan, tositumomab). Les sels de zinc présentent des interactions mineures.

Les mises en garde et contre-indications de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations. Cette lacune est bloquante pour une évaluation de sécurité complète.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Deux essais de phase 2 testent directement ustékinumab dans la dermatite atopique, mais ils sont de petite taille et l'adéquation mécanistique est partielle (voie Th2 dominante). Le score TxGNN est gonflé par un terme très général, les AMM françaises sont toutes annulées et les données de sécurité de la notice manquent.

**Pour avancer, les éléments suivants sont nécessaires :**
- Résultats détaillés des essais NCT01945086 et NCT01806662 (efficacité et sécurité)
- Notice de l'ANSM (mises en garde et contre-indications) pour lever la lacune de sécurité bloquante
- Données détaillées sur le mécanisme d'action (DrugBank)
- Précision de la population « dermatite » visée (atopique, de contact, autre)
- Clarification du statut réglementaire actuel en France (AMM annulées)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

