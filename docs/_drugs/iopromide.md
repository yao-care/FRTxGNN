---
layout: default
title: Iopromide
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 10
---

# Iopromide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Iopromide : De l'Agent de Contraste Radiographique à la Susceptibilité à l'Arthrose

## Résumé en Une Phrase

Iopromide est un agent de contraste iodé à faible osmolarité, utilisé en imagerie radiographique (RX/CT) pour le rehaussement diagnostique des tissus, et non un médicament à visée thérapeutique systémique.
Le modèle TxGNN prédit qu'il pourrait être associé à la **Susceptibilité à l'Arthrose** (*osteoarthritis susceptibility*),
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction — il s'agit d'un signal statistique isolé, sans corrélat mécanistique identifié dans les données disponibles.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Agent de contraste radiographique (imagerie RX/CT) |
| Nouvelle Indication Prédite | Susceptibilité à l'Arthrose (*Osteoarthritis Susceptibility*) |
| Score de Prédiction TxGNN | 99.57 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action (MOA) formel d'iopromide ne sont pas disponibles dans cette évaluation (écart de données classé « High »). Sur la base des informations contextuelles recueillies durant la revue de preuves, iopromide agit par un mécanisme purement physique : il s'agit d'une molécule iodée qui atténue les rayons X, permettant le rehaussement de contraste en imagerie diagnostique. Ce mécanisme ne comporte aucune activité pharmacologique, immunomodulatrice ou anti-inflammatoire connue.

La nouvelle indication prédite, la susceptibilité à l'arthrose, relève de mécanismes génétiques et inflammatoires (par exemple des voies de signalisation impliquées dans le remodelage du cartilage), qui n'ont aucun recoupement biologique connu avec un agent de contraste radiographique. L'analyse de rationnel fournie avec cette prédiction indique explicitement l'absence de tout lien mécanistique plausible.

En conséquence, cette prédiction doit être interprétée avec prudence : il s'agit très probablement d'un artefact de similarité d'embedding du modèle TxGNN (co-occurrence de iopromide dans des contextes d'imagerie orthopédique/rhumatologique diagnostique), plutôt que d'une hypothèse pharmacologique authentique. Aucune preuve clinique ou littérature ne vient aujourd'hui corroborer cette piste.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Iopromide n'est associé à aucune Autorisation de Mise sur le Marché (AMM) enregistrée dans les données disponibles (0 AMM, statut « non commercialisé »).

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité (aucune mise en garde, contre-indication ou interaction médicamenteuse officielle n'est disponible dans les données actuelles).

**Signal de sécurité identifié lors de la revue de littérature (hors indication évaluée) :**
Une recherche de littérature associée à une autre piste explorée pour ce médicament (hémoglobinopathie) a mis en évidence un cas publié d'événement vaso-occlusif cérébral survenu chez un patient drépanocytaire après administration d'un produit de contraste intraveineux à faible osmolarité ([PMID 16628721](https://pubmed.ncbi.nlm.nih.gov/16628721/)). Bien que ce signal ne concerne pas directement l'indication « susceptibilité à l'arthrose » traitée dans ce rapport, il constitue une information de pharmacovigilance pertinente sur le profil de risque général du produit et devrait être vérifié dans la notice officielle avant toute utilisation clinique élargie.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Malgré un score de similarité TxGNN élevé (99.57 %), aucune preuve clinique ou littérature spécifique ne soutient un lien thérapeutique entre iopromide et la susceptibilité à l'arthrose (niveau de preuve L5). L'analyse mécanistique disponible indique explicitement l'absence de lien pharmacologique plausible, suggérant un signal de bruit du modèle plutôt qu'une véritable hypothèse de repositionnement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les données officielles de la notice/ANSM (mises en garde, contre-indications) — actuellement bloquant pour toute évaluation de sécurité (S1)
- Obtenir les données de mécanisme d'action (MOA) formelles via DrugBank
- Rechercher une littérature ciblée et indépendante sur l'exposition aux agents de contraste iodés et le risque/protection articulaire, actuellement inexistante
- Clarifier et documenter le signal de sécurité identifié chez les patients drépanocytaires exposés à des produits de contraste, indépendamment de cette piste de repositionnement
- Compte tenu de l'absence totale de rationnel mécanistique et de preuve clinique, il est recommandé de ne pas prioriser davantage de ressources sur cette piste sans nouveau signal indépendant
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

