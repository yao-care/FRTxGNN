---
layout: default
title: Imatinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 391
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Imatinib : nouvelle indication prédite, Fibrosarcome cardiaque (heart fibrosarcoma) (niveau de preuve L5). Indication d'origine : Mastocytose systémique, tumeur stromale gastro-intestinale…"
monitor_inn: "IMATINIB"
predicted_indications: ["heart fibrosarcoma", "fibroblastic neoplasm", "conventional fibrosarcoma", "kidney fibrosarcoma", "low grade fibromyxoid sarcoma", "liposarcoma", "liver fibrosarcoma", "autosomal recessive familial Mediterranean fever", "ovarian myxoid liposarcoma", "familial rhabdoid tumor"]
---

# Imatinib
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Imatinib : De la leucémie myéloïde chronique au fibrosarcome cardiaque

## Résumé en Une Phrase

Imatinib est un inhibiteur de tyrosine kinase, initialement utilisé pour traiter la leucémie myéloïde chronique BCR-ABL1 positive, les tumeurs stromales gastro-intestinales (GIST) et le dermatofibrosarcome protubérant.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **fibrosarcome cardiaque** (heart fibrosarcoma), mais aucun essai clinique ni aucune publication ne le soutiennent directement pour cette indication.
Les données compilées pour ce rapport ne contiennent que **1 publication** associée (une revue générale sur l'imatinib) et **0 essai clinique** pour cette prédiction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Mastocytose systémique, tumeur stromale gastro-intestinale, leucémie myéloïde chronique BCR-ABL1 positive (autres indications : dermatofibrosarcome protubérant, syndrome hyperéosinophilique) |
| Nouvelle Indication Prédite | Fibrosarcome cardiaque (heart fibrosarcoma) |
| Score de Prédiction TxGNN | 99,94 % |
| Niveau de Preuve | L5 (prédiction du modèle, sans étude directe ; le classement automatique indique L4) |
| Statut de Marché en France | AMM annulées uniquement |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

*Remarque : le texte des indications approuvées n'est pas renseigné dans les AMM françaises ; l'indication originale provient du graphe de connaissances.*

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances publiées, l'imatinib inhibe les kinases ABL, KIT et PDGFR. Son efficacité est établie dans la leucémie myéloïde chronique, les GIST et le dermatofibrosarcome protubérant (DFSP).

Le DFSP est souvent lié à la fusion COL1A1-PDGFB, qui active en continu le récepteur PDGFR-bêta, cible de l'imatinib. Le score élevé de TxGNN reflète probablement la proximité, dans le réseau de connaissances, entre le fibrosarcome cardiaque et le DFSP.

Cette extrapolation reste toutefois fragile. Pour un fibrosarcome cardiaque primitif, aucune donnée spécifique ne montre que ce mécanisme s'applique. La prédiction doit donc être considérée comme une hypothèse de recherche et non comme une indication étayée.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour le fibrosarcome cardiaque.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Revue | Prescrire international | Revue des nouvelles indications de l'imatinib (leucémie lymphoblastique aiguë Ph+, etc.), concluant que les preuves ne sont pas robustes ; aucun lien direct avec le fibrosarcome cardiaque |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63485353 | GLIVEC 400 mg, comprimé pelliculé (statut : annulée) | Comprimé pelliculé | Non renseignée |
| 64936439 | GLIVEC 100 mg, comprimé pelliculé (statut : annulée) | Comprimé pelliculé | Non renseignée |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase) |
| Risque de Myélosuppression | Moyen : neutropénie, thrombopénie et anémie figurent parmi les contre-indications relevées dans le graphe de connaissances |
| Classification d'Émétogénicité | Veuillez consulter la notice |
| Éléments de Surveillance | NFS, fonction hépatique et rénale, surveillance cardiaque et rétention hydrique |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

- **Affections signalées comme contre-indications dans le graphe de connaissances** (et non dans la notice) : insuffisance cardiaque et congestive, maladie des valves cardiaques, maladie coronarienne, épanchement péricardique, œdème pulmonaire, œdème cérébral, insuffisance hépatique, maladie rénale, thrombopénie, neutropénie, agranulocytose, anémie, hypertension, diabète et acidocétose diabétique, ulcère gastroduodénal actif, hypophosphatémie, hyperbilirubinémie (dont syndrome de Gilbert). Ces éléments sont particulièrement pertinents pour une tumeur cardiaque.
- **Interactions médicamenteuses** (100 interactions recensées ; principales) :
  - Majeures : éliglustat, naloxégol
  - Modérées : hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, budésonide, clarithromycine, cimétidine, pioglitazone, glimépiride, saxagliptine, morphine, aprépitant, lansoprazole, dexlansoprazole, naltrexone, naldémédine, metréleptine
- Un cas de syndrome DRESS induit par l'imatinib a été rapporté chez un patient atteint de DFSP (à titre d'information de sécurité).

La notice officielle (mises en garde et contre-indications) n'a pas pu être exploitée ; veuillez la consulter.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle : aucun essai, aucune donnée clinique pour le fibrosarcome cardiaque, et l'extrapolation depuis le DFSP reste indirecte.
- Les AMM françaises sont toutes annulées, et les données de sécurité de la notice manquent.

**Autres prédictions à noter (pour orientation) :**
- **Liposarcome** : preuve la plus avancée (3 essais de phase 1/2 et 2 sur sarcomes, niveau L2), mais non spécifiques à cette histologie ; question de recherche.
- **Fibrosarcome conventionnel et néoplasme fibroblastique** : littérature centrée sur le DFSP, déjà indication approuvée ; ce n'est pas une nouvelle opportunité de repositionnement.
- **Fibrosarcome rénal et hépatique, sarcome fibromyxoïde de bas grade, fièvre méditerranéenne familiale, liposarcome myxoïde ovarien, tumeur rhabdoïde familiale** : preuves absentes ou sans rapport ; à maintenir en attente.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (DrugBank) et analyse du lien avec le fibrosarcome cardiaque (statut PDGFB/PDGFR/KIT des tumeurs)
- Notice officielle de l'ANSM (mises en garde, contre-indications), et clarification du statut des AMM annulées
- Séries de cas ou données précliniques sur l'imatinib dans les sarcomes cardiaques
- Évaluation spécifique du risque cardiaque (insuffisance cardiaque, épanchement péricardique) avant toute étude
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

