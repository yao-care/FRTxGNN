---
layout: default
title: Nitisinone
parent: Prédiction du modèle uniquement (L5)
nav_order: 539
evidence_level: L5
indication_count: 10
---

# Nitisinone
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

# Nitisinone : De la Tyrosinémie à l'Acidose Tubulaire Rénale

## Résumé en Une Phrase

Nitisinone est un inhibiteur de la voie de dégradation de la tyrosine, initialement utilisé pour le traitement de la tyrosinémie héréditaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**acidose tubulaire rénale**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Tyrosinémie (source : graphe de connaissances TxGNN, le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Acidose tubulaire rénale |
| Score de Prédiction TxGNN | 99,96 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 9 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances pharmacologiques établies, la nitisinone inhibe la 4-hydroxyphénylpyruvate dioxygénase (HPPD), une enzyme de la dégradation de la tyrosine. Cette information est à confirmer auprès de DrugBank.

Dans la tyrosinémie héréditaire de type 1, l'accumulation de métabolites toxiques (notamment la succinylacétone) provoque, entre autres, une atteinte tubulaire proximale de type syndrome de Fanconi. En bloquant la formation de ces métabolites en amont, la nitisinone prévient cette atteinte. Le lien avec l'acidose tubulaire rénale est donc plausible, mais **indirect**.

Il convient toutefois d'être prudent : l'acidose tubulaire rénale primaire a des causes génétiques et de transport ionique distinctes de la voie de la tyrosine. Aucune donnée ne montre un bénéfice dans cette indication. Le score du modèle reste un signal computationnel qui nécessite une validation.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'acidose tubulaire rénale.

*Remarque : pour la 2ᵉ indication prédite (galactosémie), trois revues générales mentionnent côte à côte la galactosémie et la tyrosinémie dans le diagnostic différentiel des hépatopathies métaboliques pédiatriques. Elles ne démontrent pas d'efficacité de la nitisinone dans cette maladie.*

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 66880925 | ORFADIN 4 mg/ml | Suspension buvable | Annulée |
| 60459499 | ORFADIN 5 mg | Gélule | Annulée |
| 64147632 | ORFADIN 10 mg | Gélule | Annulée |
| 62524376 | NITISINONE DIPHARMA 5 mg | Gélule | Annulée |
| 67123316 | NITISINONE DIPHARMA 2 mg | Gélule | Annulée |

Au total, 9 AMM sont recensées, toutes annulées. Aucune AMM valide n'apparaît dans les données compilées. Le texte des indications approuvées n'est pas renseigné.

---

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

- **Contre-indications issues du graphe de connaissances** (à titre indicatif, hors texte de notice) : maladie rénale, pyourétère, thrombopénie, leucopénie, hypophosphatémie.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi les premières listées, la plupart sont de niveau modéré, notamment : abiratérone, isotrétinoïne, nifédipine, ibuprofène, aldesleukine, pioglitazone, amiodarone, amlodipine, apalutamide, aprépitant, atazanavir, baricitinib, dexaméthasone, bexarotène, bicalutamide. L'interaction avec l'armodafinil est de niveau mineur.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication. Le lien mécanistique est indirect, et les données de sécurité de la notice sont absentes, ce qui bloque l'évaluation de sécurité. Par ailleurs, les 9 AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications
- Confirmer le mécanisme d'action via DrugBank
- Réaliser une revue ciblée de la littérature sur l'atteinte tubulaire rénale sous nitisinone, et sur l'acidose tubulaire rénale primaire
- Examiner les contre-indications issues du graphe (maladie rénale, hypophosphatémie), potentiellement pertinentes pour une indication rénale
- Clarifier la situation réglementaire (AMM annulées) et la disponibilité du médicament en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

