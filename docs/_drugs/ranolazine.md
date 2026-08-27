---
layout: default
title: Ranolazine
parent: 僅模型預測 (L5)
nav_order: 256
evidence_level: L5
indication_count: 1
---

# Ranolazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Ranolazine : De l'Angine de Poitrine Chronique au Syndrome Néphrogénique de Sécrétion Inappropriée d'Hormone Antidiurétique

## Résumé en Une Phrase

La ranolazine est un inhibiteur du courant sodique tardif (late INa) utilisé dans le traitement de l'angine de poitrine chronique (angor stable).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome néphrogénique de sécrétion inappropriée d'hormone antidiurétique (NSIAD)**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Angine de poitrine chronique |
| Nouvelle Indication Prédite | Syndrome néphrogénique de sécrétion inappropriée d'hormone antidiurétique (NSIAD) |
| Score de Prédiction TxGNN | 99.65% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action officiel (DrugBank) ne sont pas disponibles pour ce rapport. Sur la base des informations connues, la ranolazine est un inhibiteur du courant sodique tardif (late INa), sa cible pharmacologique principale étant le canal sodique du myocarde ; son efficacité dans l'angine de poitrine chronique est bien établie.

Le NSIAD est causé par des mutations à gain de fonction du récepteur V2 de la vasopressine (AVPR2), qui active ce récepteur indépendamment de l'ADH et entraîne une surexpression de l'aquaporine-2, provoquant une rétention hydrique. Il n'existe actuellement **aucune preuve** que la ranolazine agisse, directement ou hors cible, sur l'AVPR2 ou sur la voie cAMP/aquaporine-2 en aval : son mécanisme d'inhibition du canal sodique ne présente aucun recoupement connu avec cette voie de signalisation couplée aux protéines G.

Cette indication repose uniquement sur une similarité d'embedding dans le réseau TxGNN (score 0,996), sans plausibilité mécanistique établie et sans aucun essai clinique ni littérature à l'appui. Elle doit donc être interprétée comme une hypothèse générée par le modèle, et non comme une piste étayée par des données biologiques ou cliniques.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement

## Preuves de la Littérature

Aucune littérature associée disponible actuellement

## Informations de Marché en France

La ranolazine n'est actuellement **pas commercialisée en France** (statut : "未上市" / non commercialisé) et ne dispose d'aucune AMM enregistrée dans les données disponibles.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose exclusivement sur une similarité d'embedding TxGNN (niveau de preuve L5), sans aucun essai clinique, sans aucune publication, et sans lien mécanistique plausible identifié entre l'inhibition du canal sodique et la voie AVPR2/aquaporine-2 impliquée dans le NSIAD. De plus, l'absence de données réglementaires TFDA (mises en garde/contre-indications) empêche toute évaluation de sécurité préliminaire (S1).

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice/mises en garde TFDA (donnée bloquante — DG001) pour permettre l'évaluation de sécurité S1
- Données de mécanisme d'action confirmées via DrugBank (DG002)
- Études précliniques explorant un éventuel effet hors cible de la ranolazine sur l'AVPR2 ou la voie aquaporine-2
- Surveillance continue de la littérature et des registres d'essais cliniques pour toute nouvelle preuve
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

