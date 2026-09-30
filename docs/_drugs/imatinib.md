---
layout: default
title: Imatinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 149
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Imatinib : De la Leucémie Myéloïde Chronique au Fibrosarcome Cardiaque

## Résumé en Une Phrase

L'imatinib est un inhibiteur de tyrosine kinase, commercialisé à l'origine pour la leucémie myéloïde chronique et certaines tumeurs stromales gastro-intestinales (GIST).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **fibrosarcome cardiaque**, mais cette prédiction repose sur **0 essai clinique** et **1 publication** (un commentaire de 2008 non spécifique au cœur).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM ; selon la littérature citée : leucémie myéloïde chronique et GIST |
| Nouvelle Indication Prédite | Fibrosarcome cardiaque (heart fibrosarcoma) |
| Score de Prédiction TxGNN | 99,94 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans DrugBank pour ce dossier. D'après la littérature, l'imatinib inhibe les kinases KIT, PDGFR et ABL. Son efficacité est établie dans la leucémie myéloïde chronique et les GIST, où ces kinases jouent un rôle moteur.

Sur le plan théorique, un sarcome dépendant de la signalisation PDGFR ou KIT pourrait répondre à l'imatinib. Cette logique est bien documentée pour le dermatofibrosarcome de Darier-Ferrand, mais aucun élément du dossier ne relie l'imatinib au fibrosarcome cardiaque en particulier.

Le score TxGNN très élevé (99,94 %) provient très probablement du voisinage « fibrosarcome / dermatofibrosarcome » dans le graphe de connaissances, et non d'une preuve propre à cette localisation cardiaque. La seule référence liée est un commentaire de 2008 qui qualifie lui-même les preuves des nouvelles indications de « non robustes ».

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Commentaire | Prescrire international | Passe en revue les indications élargies de l'imatinib (dont la leucémie lymphoblastique aiguë Ph+, avec un taux de réponse hématologique supérieur à la chimiothérapie sur 55 patients). Conclut à des indications nouvelles mais sans preuves robustes. Ne traite pas des tumeurs cardiaques. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 63485353 | GLIVEC 400 mg, comprimé pelliculé (Novartis Europharm) | Comprimé pelliculé |
| 64936439 | GLIVEC 100 mg, comprimé pelliculé (Novartis Europharm) | Comprimé pelliculé |

Le texte des indications approuvées n'est pas renseigné pour ces deux AMM.

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase) |

Pour le risque de myélosuppression, l'émétogénicité, la surveillance biologique et la protection de manipulation, veuillez consulter les mises en garde et précautions de la notice.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Cette prédiction n'a ni essai clinique ni publication spécifique au fibrosarcome cardiaque. Le score TxGNN à lui seul ne suffit pas à justifier un développement (niveau L5).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications), étape bloquante pour le criblage de sécurité.
- Compléter les données sur le mécanisme d'action (DrugBank).
- Rechercher des cas cliniques ou séries de fibrosarcomes cardiaques traités par imatinib, avec confirmation d'une cible PDGFR/KIT.
- Envisager de prioriser d'autres prédictions du même dossier mieux étayées, notamment le dermatofibrosarcome de Darier-Ferrand (rang 2, « fibroblastic neoplasm », niveau L3, Proceed with Guardrails), dont la fusion COL1A1-PDGFB est ciblée par l'imatinib.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

