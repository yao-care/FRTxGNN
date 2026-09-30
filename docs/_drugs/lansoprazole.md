---
layout: default
title: Lansoprazole
parent: Preuves modérées (L3-L4)
nav_order: 169
evidence_level: L4
indication_count: 2
---

# Lansoprazole
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **2** 
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

# Lansoprazole : D'un Inhibiteur de la Pompe à Protons au Reflux Duodéno-Gastrique

## Résumé en Une Phrase

Le lansoprazole est un inhibiteur de la pompe à protons (IPP) qui réduit la sécrétion d'acide gastrique et est commercialisé en France sous forme de gélules et de comprimés orodispersibles.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **reflux duodéno-gastrique**, mais **aucun essai clinique** et seulement **2 publications** sont associés à cette indication. La seule étude directe (chez le rat) suggère plutôt un signal de risque qu'un bénéfice.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM du dossier |
| Nouvelle Indication Prédite | Reflux duodéno-gastrique |
| Score de Prédiction TxGNN | 99,69 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des connaissances générales, le lansoprazole appartient à la classe des IPP, qui suppriment l'acide gastrique. Il pourrait donc réduire les lésions muqueuses liées à l'acidité en cas de reflux duodéno-gastrique (reflux biliaire).

Ce lien reste toutefois fragile. Le reflux duodéno-gastrique est en grande partie non acide, et les IPP ne corrigent ni le trouble de la motricité ni le dysfonctionnement pylorique sous-jacents.

La seule étude directe est un modèle chez le rat, dans lequel le lansoprazole a favorisé la carcinogenèse gastrique en présence de reflux duodéno-gastrique, probablement par hypergastrinémie et inhibition acide. Il s'agit d'un signal de sécurité, pas d'un signal de bénéfice. Le score TxGNN très élevé (0,997) n'est donc corroboré par aucune donnée clinique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Étude animale (rat) | Gastric Cancer | Le lansoprazole associé à un reflux duodéno-gastrique favorise la carcinogenèse gastrique chez le rat. Signal de risque, pas de bénéfice. |
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Revue | Eur J Clin Pharmacol | Mise à jour sur l'usage clinique des IPP (ulcère peptique, infection à *H. pylori*, RGO, lésions liées aux AINS, syndrome de Zollinger-Ellison). Ne traite pas du reflux duodéno-gastrique. |

---

## Informations de Marché en France

Les textes d'indication approuvée ne sont pas renseignés pour ces AMM. Cinq des 20 AMM sont listées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|------|
| 69499833 | Lansoprazole Cristers 15 mg | Gélule gastro-résistante | Cristers |
| 67240910 | Lansoprazole EG 30 mg | Comprimé orodispersible | EG Labo - Laboratoires Eurogenerics |
| 62911490 | Lansoprazole Arrow Lab 30 mg | Gélule gastro-résistante | Arrow Génériques |
| 68088245 | Ogastoro 30 mg | Comprimé orodispersible | Takeda France |
| 62385791 | Lansoprazole Sandoz 30 mg | Comprimé orodispersible | Sandoz |

---

## Considérations de Sécurité

- **Signal préclinique** : chez le rat, le lansoprazole a favorisé la carcinogenèse gastrique en présence de reflux duodéno-gastrique (PMID 15052437). La transposabilité à l'humain n'est pas établie.

Aucune donnée d'interaction médicamenteuse n'a été trouvée. Veuillez consulter la notice pour les mises en garde, les contre-indications et les autres informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le niveau de preuve est L4. Il n'existe aucun essai clinique pour cette indication, et la seule étude directe (chez le rat) indique un risque. Le score TxGNN élevé reflète probablement une proximité dans le graphe de connaissances plutôt qu'un effet thérapeutique.
- La deuxième prédiction du modèle, l'obstruction duodénale (score 99,68 %), n'est pas plus étayée. Une obstruction est mécanique et l'inhibition acide ne la lève pas. Un seul essai de phase 3 complété sur le lansoprazole est cité (NCT00175032, ulcères liés aux AINS chez des patients sous aspirine), mais il ne porte pas sur l'obstruction.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications). Cette étape est bloquante pour tout criblage de sécurité.
- Obtenir les données de mécanisme d'action depuis DrugBank.
- Rechercher des études cliniques ou observationnelles sur les IPP dans le reflux biliaire ou duodéno-gastrique, afin de confirmer ou d'écarter le signal de risque observé chez le rat.
- Préciser les indications approuvées des AMM françaises, actuellement vides dans les données.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

