---
layout: default
title: Cyclopentolate
parent: Prédiction du modèle uniquement (L5)
nav_order: 93
evidence_level: L5
indication_count: 3
---

# Cyclopentolate
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

# Cyclopentolate : Du Collyre Mydriatique et Cycloplégique au Syndrome de la Queue de Cheval

## Résumé en Une Phrase

Le cyclopentolate est un anticholinergique (antagoniste muscarinique) commercialisé en France sous forme de collyre, à usage ophtalmique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de la queue de cheval**, mais cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données de l'ANSM (collyre à usage ophtalmique) |
| Nouvelle Indication Prédite | Syndrome de la queue de cheval (cauda equina syndrome) |
| Score de Prédiction TxGNN | 99,54 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après la pharmacologie générale, le cyclopentolate est un antagoniste des récepteurs muscariniques. En ophtalmologie, il dilate la pupille et paralyse l'accommodation. Le collyre est son seul usage commercialisé en France.

Un antimuscarinique pourrait en théorie soulager certains symptômes vésicaux ou intestinaux secondaires au syndrome de la queue de cheval. En revanche, il ne traite pas la cause, c'est-à-dire la compression des racines nerveuses, qui est une urgence chirurgicale. Le lien mécanistique est donc faible et indirect. Le score du modèle seul ne suffit pas à le soutenir.

Deux autres prédictions ont un score comparable (toutes deux de niveau L5, sans essai ni publication) :
- **Vessie neurogène** (99,40 %) : la classe des antimuscariniques est bien établie pour l'hyperactivité du détrusor, mais des médicaments approuvés existent déjà. Le terme de maladie est signalé comme « obsolète » dans l'ontologie. Il faudrait revérifier la correspondance avec un terme actuel, par exemple l'hyperactivité neurogène du détrusor.
- **Syndrome de l'intestin irritable** (99,27 %) : les antispasmodiques antimuscariniques sont utilisés contre les douleurs abdominales. Aucune donnée n'existe pour le cyclopentolate par voie systémique ou orale. Les effets anticholinergiques systémiques (bouche sèche, tachycardie, effets centraux, constipation) sont préoccupants, surtout en cas de SII à prédominance constipation.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69255195 | SKIACOL 0,5 POUR CENT, collyre (Laboratoires Alcon) | Collyre en solution | Non précisée dans les données |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication.
- Le lien mécanistique avec la compression nerveuse du syndrome de la queue de cheval est faible.
- La seule forme commercialisée est un collyre.
- Les données de sécurité de la notice sont absentes du dossier.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde, contre-indications, indication approuvée). Ce point est bloquant pour le criblage de sécurité.
- Obtenir les données sur le mécanisme d'action (par exemple via l'API DrugBank).
- Réaliser une recherche systématique d'essais cliniques et de littérature pour les trois indications prédites.
- Évaluer la compatibilité des voies d'administration : le collyre ne permet pas d'atteindre une action vésicale ou intestinale.
- Recontrôler la correspondance du terme de maladie « obsolète » pour la vessie neurogène.
- Comparer avec les antimuscariniques déjà approuvés pour les symptômes vésicaux et intestinaux.

*Ces résultats sont fournis à titre de référence pour la recherche et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

