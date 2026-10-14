---
layout: default
title: Mupirocin
parent: Prédiction du modèle uniquement (L5)
nav_order: 518
evidence_level: L5
indication_count: 2
---

# Mupirocin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Mupirocine : De l'impétigo à l'empyème pleural

## Résumé en Une Phrase

La mupirocine est un antibiotique topique, initialement utilisé pour le traitement de l'impétigo et de l'impétigo bulleux.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**empyème pleural**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Impétigo, impétigo bulleux (le texte d'indication des AMM n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Empyème pleural |
| Score de Prédiction TxGNN | 99,49 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées (non commercialisé) |
| Nombre d'AMM | 7 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, la mupirocine est un antibiotique topique qui inhibe l'isoleucyl-ARNt synthétase bactérienne et agit principalement sur *Staphylococcus aureus* (y compris le SARM) et sur les streptocoques. Ces informations ne proviennent pas des données de mécanisme du dossier et ne sont donc pas retenues comme preuve.

Le lien avec l'empyème pleural est lâche : cette infection est souvent causée par ces mêmes germes, d'où une certaine logique antibactérienne. Toutefois, la plausibilité pharmacocinétique est **très faible**. La mupirocine n'est approuvée que par voie topique, son exposition systémique est négligeable et elle est rapidement hydrolysée en acide monique inactif. Elle ne convient donc pas au traitement systémique ou intrapleural d'une infection profonde.

Le score TxGNN très élevé (0,995) reflète une proximité dans le graphe de connaissances, et non une preuve d'efficacité.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 66325311 | BACTROBAN 2 %, pommade nasale | Pommade | Non renseignée | Annulée |
| 69265691 | MUPIDERM 2 %, pommade | Pommade | Non renseignée | Annulée |
| 65777420 | MUPIROCINE VIATRIS 2 %, pommade | Pommade | Non renseignée | Annulée |
| 64347960 | MUPIROCINE EG 2 %, pommade | Pommade | Non renseignée | Annulée |
| 61059102 | MUPIROCINE ARROW 2 %, pommade | Pommade | Non renseignée | Annulée |

## Considérations de Sécurité

- **Contre-indication issue du graphe de connaissances** : dermatite (information issue du graphe de connaissances, et non du texte de la notice).
- **Interactions médicamenteuses** : 118 interactions recensées, toutes de niveau « inconnu ». Exemples : calcitriol, clotrimazole, morphine, metformine, pantoprazole, oméprazole, sucralfate, vancomycine, triamcinolone, prednisone.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et la voie topique de la mupirocine est incompatible avec une infection pleurale profonde.
- Toutes les AMM françaises sont annulées et les données de sécurité officielles sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle de l'ANSM (mises en garde et contre-indications), une lacune bloquante pour l'évaluation de sécurité
- Obtenir les données détaillées sur le mécanisme d'action depuis DrugBank
- Démontrer une faisabilité pharmacocinétique (exposition locale ou systémique suffisante, voie d'administration compatible)
- Rechercher des données précliniques ou cliniques sur l'empyème pleural

**Note sur la seconde prédiction :** la kératoconjonctivite épithéliale ponctuée (score TxGNN 99,10 %, niveau L5, Hold) n'est étayée par aucune preuve directe. La pommade de mupirocine n'est ni formulée ni approuvée pour l'usage ophtalmique, et sa sécurité sur la surface oculaire n'est pas établie. Seul un sous-groupe d'origine staphylococcique pourrait présenter un lien antibactérien.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

