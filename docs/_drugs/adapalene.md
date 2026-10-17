---
layout: default
title: Adapalene
parent: Prédiction du modèle uniquement (L5)
nav_order: 26
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Adapalene : nouvelle indication prédite, Élévation du zinc plasmatique (niveau de preuve L5). Indication d'origine : Acné"
monitor_inn: "adapalene"
predicted_indications: ["zinc, elevated plasma"]
---

# Adapalene
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

# Adapalène : De l'acné à l'élévation du zinc plasmatique

## Résumé en Une Phrase

L'adapalène est un rétinoïde topique de troisième génération, initialement utilisé pour le traitement de l'acné.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**élévation du zinc plasmatique**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Acné |
| Nouvelle Indication Prédite | Élévation du zinc plasmatique |
| Score de Prédiction TxGNN | 99,51 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 9 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, l'adapalène est un rétinoïde topique qui se lie sélectivement aux récepteurs de l'acide rétinoïque (RAR-bêta et RAR-gamma) et module la différenciation des kératinocytes ainsi que l'inflammation. Son efficacité dans l'acné est établie.

**Aucun lien mécanistique établi** n'existe entre ces actions et l'homéostasie du zinc plasmatique (absorption, transport par les transporteurs ZIP/ZnT, régulation des métallothionéines). Tout lien reste spéculatif, par exemple via des effets des rétinoïdes sur l'expression de gènes impliqués dans le métabolisme du zinc, sans donnée à l'appui.

Par ailleurs, une élévation du zinc plasmatique est plutôt un constat biologique qu'une maladie cible classique, ce qui réduit encore la plausibilité clinique. Le score élevé (0,995) reflète uniquement la prédiction du modèle et doit être interprété avec une grande prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 9 AMM recensées sont toutes annulées ; aucune n'est actuellement valide. Le texte de l'indication approuvée n'est pas disponible dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 67245747 | ADAPALENE ZENTIVA 0,1 %, crème | Crème | Annulée |
| 62886560 | ADAPALENE ZENTIVA 0,1 %, gel | Gel | Annulée |
| 65099368 | ADAPALENE TEVA 0,1 POUR CENT, crème | Crème | Annulée |
| 63066469 | DIFFERINE 0,1 %, gel | Gel | Annulée |
| 69718483 | DIFFERINE 0,1 %, crème | Crème | Annulée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations du graphe TxGNN/PrimeKG, et non le texte de la notice) : réponse photoparoxystique, maladie de photosensibilité, dermatite exfoliative, dermatite.
- **Interactions médicamenteuses** : 58 interactions répertoriées, toutes de niveau de gravité non précisé. Parmi elles : pantoprazole, doxycycline, oméprazole, triamcinolone, prednisone, tétracycline, minocycline, métronidazole, ibuprofène et fluconazole.

Les mises en garde et contre-indications de la notice officielle ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (L5), sans essai clinique ni publication, sans lien mécanistique plausible, et la cible est un état biologique plutôt qu'une maladie. De plus, aucune AMM n'est actuellement valide en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (DrugBank)
- Mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Justification clinique de l'élévation du zinc plasmatique comme cible thérapeutique
- Études précliniques ou de mécanisme explorant un éventuel effet des rétinoïdes sur le métabolisme du zinc
- Évaluation de la compatibilité des voies d'administration (topique par rapport à une action systémique) et clarification du statut réglementaire
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

