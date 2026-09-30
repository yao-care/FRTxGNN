---
layout: default
title: Clidinium
parent: Prédiction du modèle uniquement (L5)
nav_order: 79
evidence_level: L5
indication_count: 10
---

# Clidinium
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

# Clidinium : D'une indication non renseignée au syndrome de la queue de cheval

## Résumé en Une Phrase

Le clidinium est un anticholinergique (antimuscarinique) commercialisé en France dans la spécialité LIBRAX, mais le texte de son indication d'origine n'est pas renseigné dans les données d'AMM disponibles.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de la queue de cheval**, sans aucun **essai clinique** ni **publication** à l'appui à ce jour : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM (texte d'indication vide) |
| Nouvelle Indication Prédite | Syndrome de la queue de cheval (cauda equina syndrome) |
| Score de Prédiction TxGNN | 99,93 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le clidinium est un antimuscarinique de structure ammonium quaternaire, qui pénètre peu dans le système nerveux central. Ce type de molécule réduit la motricité et les spasmes des muscles lisses.

Dans le syndrome de la queue de cheval, le clidinium pourrait en théorie atténuer les troubles vésicaux ou intestinaux secondaires. Il ne traite cependant pas la cause sous-jacente, une compression nerveuse qui constitue une urgence chirurgicale. Le score élevé de TxGNN reflète probablement la proximité dans le graphe de connaissances avec la vessie neurogène, et non une efficacité démontrée.

La prédiction doit donc être considérée comme une hypothèse de traitement symptomatique éventuel, pas comme une alternative au traitement de la cause. Aucune donnée clinique ne permet aujourd'hui de la valider.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66803576 | LIBRAX, comprimé enrobé | Comprimé enrobé | Non renseignée |
| 67627992 | LIBRAX, comprimé enrobé | Comprimé enrobé | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

À noter : d'autres prédictions du modèle concernent la myasthénie (myasthénie auto-immune, néonatale, etc.). Les anticholinergiques sont généralement déconseillés dans ces pathologies car ils peuvent aggraver la faiblesse musculaire. Ces prédictions doivent être traitées comme un signal de sécurité potentiel, et non comme une opportunité de repositionnement.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour le syndrome de la queue de cheval repose uniquement sur le score du modèle (niveau L5), sans essai ni publication, et le clidinium n'agit pas sur la cause de cette urgence chirurgicale.
- Les données de sécurité de la notice ANSM sont manquantes, ce qui empêche de passer à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde et contre-indications), manque bloquant.
- Obtenir les données de mécanisme d'action via DrugBank (DB00771) et le texte de l'indication approuvée des deux AMM.
- Réorienter l'évaluation vers des prédictions mieux documentées :
  - **Ulcère peptique** (niveau L3) : séries cliniques anciennes sur l'association clidinium/chlordiazépoxide, dont [PMID 4892352](https://pubmed.ncbi.nlm.nih.gov/4892352/) (1969) et [PMID 14477958](https://pubmed.ncbi.nlm.nih.gov/14477958/) (1962). L'étude de 2016 [PMID 27386057](https://pubmed.ncbi.nlm.nih.gov/27386057/), sur l'ajout de clidinium-C à la trithérapie anti-*H. pylori*, est la plus récente. Son design reste à vérifier et elle pourrait passer en L2 si c'est un essai randomisé. L'apport du clidinium seul reste confondu avec celui de l'association, et les IPP modernes rendent sa valeur incrémentale incertaine.
  - **Gastroduodénite** (niveau L3) et **maladie du gros intestin** (niveau L4) : preuves anciennes ou indirectes seulement, à traiter comme des questions de recherche.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

