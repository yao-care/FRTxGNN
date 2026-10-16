---
layout: default
title: Raltitrexed
parent: Prédiction du modèle uniquement (L5)
nav_order: 648
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Raltitrexed : nouvelle indication prédite, Cholangite sclérosante (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM compilées (usage clinique connu…"
---

# Raltitrexed
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

# Raltitrexed : Du Cancer Colorectal au Cholangite Sclérosante

## Résumé en Une Phrase

Le raltitrexed est un inhibiteur de la thymidylate synthase (antifolate), utilisé en oncologie pour le traitement du cancer colorectal et du mésothéliome pleural malin.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **cholangite sclérosante**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées (usage clinique connu : cancer colorectal et mésothéliome malin) |
| Nouvelle Indication Prédite | Cholangite sclérosante |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Annulée uniquement (AMM annulée) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans l'AMM. Les données de pharmacologie compilées indiquent que le raltitrexed cible la thymidylate synthase (gène TYMS), enzyme clé de la synthèse de l'ADN. Son efficacité a été établie dans le cancer colorectal et le mésothéliome malin, des tumeurs à prolifération rapide.

Pour la cholangite sclérosante, **aucun lien mécanistique clair** n'est étayé par les données. Cette maladie est une atteinte cholestatique et fibro-inflammatoire des voies biliaires, très éloignée de l'action anti-prolifératrice d'un antifolate. Le score élevé (99,97 %) résulte uniquement d'une prédiction du modèle, sans essai ni publication à l'appui. Cette prédiction doit donc être considérée comme une hypothèse très préliminaire.

## Autres Indications Prédites

| Rang | Maladie prédite | Score TxGNN | Niveau de preuve | Commentaire |
|------|------|------|------|------|
| 2 | Syndrome myélodysplasique | 99,97 % | L5 | Hypothèse ciblant les cellules clonales prolifératives ; la myélosuppression connue des antifolates est préoccupante chez des patients déjà cytopéniques |
| 3 à 7 | Syndromes drépanocytaires (variantes Hb D, Hb C, Hb E, bêta-thalassémie, persistance héréditaire de l'hémoglobine fœtale) | 99,96 % | L5 | Hypothèse d'induction de l'hémoglobine fœtale, non étayée ; scores identiques, ce qui suggère un signal commun du graphe ; justification particulièrement faible en cas de persistance de l'HbF |
| 8 | Syndrome myélodysplasique non classé | 99,96 % | L5 | Même rationnel spéculatif et même préoccupation de myélosuppression |
| 9 | Cytopénie réfractaire de l'enfant | 99,96 % | L5 | Plausibilité biologique faible : un antifolate myélosuppresseur risque d'aggraver les cytopénies |
| 10 | Délétion partielle du bras long du chromosome 5 | 99,95 % | L5 | Aucun lien établi avec l'inhibition de la thymidylate synthase |

Toutes ces prédictions sont classées « Hold », sans essai clinique ni publication.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60985360 | TOMUDEX 2 mg, poudre pour solution pour perfusion (PFIZER HOLDING FRANCE) | Poudre pour solution pour perfusion | Non renseignée (AMM annulée) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (antimétabolite, antifolate inhibiteur de la thymidylate synthase) |
| Risque de Myélosuppression | Élevé (toxicité connue de la classe des antifolates ; préoccupation particulière dans les syndromes myélodysplasiques et les cytopénies) |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | NFS avec formule, fonction hépatique et rénale |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : la seule entrée disponible est une relation pharmacologique avec sa cible, la thymidylate synthase (TYMS). Aucune interaction médicamenteuse cliniquement classée n'a été identifiée dans les données compilées.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la cholangite sclérosante repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication ni lien mécanistique démontré. De plus, l'AMM française est annulée et les données de sécurité de la notice sont absentes, ce qui bloque toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice officielle (ANSM) pour les mises en garde et contre-indications
- Données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Études précliniques ou de mécanisme reliant l'inhibition de la thymidylate synthase à la physiopathologie de la cholangite sclérosante
- Revue de la littérature et recherche d'essais cliniques ciblés
- Évaluation de la compatibilité des voies d'administration et du rapport bénéfice/risque, compte tenu de la myélosuppression
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

