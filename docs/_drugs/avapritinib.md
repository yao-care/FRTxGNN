---
layout: default
title: Avapritinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 82
evidence_level: L5
indication_count: 10
---

# Avapritinib
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

# Avapritinib : De la tumeur stromale gastro-intestinale à la dysplasie spondylométaphysaire axiale

## Résumé en Une Phrase

Avapritinib est un inhibiteur de kinases (KIT/PDGFRA), initialement utilisé pour le traitement de la tumeur stromale gastro-intestinale.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **dysplasie spondylométaphysaire axiale**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Tumeur stromale gastro-intestinale (d'après le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Dysplasie spondylométaphysaire axiale |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Autorisations toutes annulées |
| Nombre d'AMM | 5 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, avapritinib est un inhibiteur des kinases KIT et PDGFRA, dont l'efficacité dans la tumeur stromale gastro-intestinale est le fondement de son usage d'origine.

Aucun lien mécanistique n'est étayé par les données compilées pour ce rapport. La dysplasie spondylométaphysaire axiale est une maladie osseuse rare, associée à une biologie de type ciliopathie (gène CFAP410), et rien ne la relie à la signalisation KIT/PDGFRA. Le score élevé (99,92 %) reflète une proximité dans le réseau du modèle, et non une preuve clinique ou biologique.

À titre d'information, les autres indications prédites les mieux classées concernent surtout le groupe de la sclérose latérale amyotrophique et des maladies du motoneurone. Pour celles-ci, un raisonnement spéculatif existe (modulation des mastocytes et de la microglie via KIT, comme explorée avec le masitinib), mais la pénétration du système nerveux central de l'avapritinib n'est pas établie et aucune donnée ne le soutient.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63189920 | AYVAKYT 200 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 63220091 | AYVAKYT 50 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 65304816 | AYVAKYT 300 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 68115906 | AYVAKYT 25 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 64069767 | AYVAKYT 100 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase KIT/PDGFRA) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 100 interactions ont été identifiées dans les données compilées (extrait de 20 affichées). Parmi elles, les interactions de niveau **majeur** concernent notamment :
  - aprépitant, clarithromycine, cobicistat, dexaméthasone (probablement liées au métabolisme par le CYP3A4, à confirmer) ;
  - acide acétylsalicylique ;
  - déférasirox, défériprone ;
  - ibritumomab tiuxétan, tositumomab (I-131), samarium (153Sm) lexidronam.
- Interactions de niveau **modéré** : cimétidine, clotrimazole, miconazole, dexfenfluramine, fenfluramine, glycérol phénylbutyrate, métréleptine, sibutramine, troglitazone, chlorure de strontium Sr-89.

Les mises en garde et contre-indications de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication ni lien mécanistique démontré. De plus, toutes les AMM françaises sont annulées et les données de sécurité de la notice sont absentes, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice ANSM (mises en garde et contre-indications), point bloquant
- Données détaillées sur le mécanisme d'action (requête DrugBank)
- Démonstration d'un lien biologique entre KIT/PDGFRA et la dysplasie spondylométaphysaire axiale (études précliniques)
- Clarification de la situation réglementaire en France (raison de l'annulation des AMM)
- Évaluation de la pertinence des indications du groupe SLA/motoneurone, notamment la pénétration du système nerveux central
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

