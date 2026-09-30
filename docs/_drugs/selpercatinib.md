---
layout: default
title: Selpercatinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 280
evidence_level: L5
indication_count: 3
---

# Selpercatinib
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

# Sélpercatinib : Des cancers à altération de RET à l'hypertension pulmonaire

## Résumé en Une Phrase

Le sélpercatinib est un inhibiteur sélectif de la kinase RET, dont la littérature associe l'usage aux cancers du poumon non à petites cellules avec fusion de RET et au cancer médullaire de la thyroïde. Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertension pulmonaire**, mais **aucun essai clinique** et **aucune publication** ne soutiennent directement cette indication. Cette prédiction repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM (la littérature mentionne le CBNPC avec fusion de RET et le cancer médullaire de la thyroïde) |
| Nouvelle Indication Prédite | Hypertension pulmonaire |
| Score de Prédiction TxGNN | 99,18 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le sélpercatinib est un inhibiteur de kinase hautement sélectif de RET, avec très peu d'activité sur le VEGFR. Son efficacité a été documentée dans des cancers dépendants de RET, mais rien n'indique qu'il soit applicable mécanistiquement à l'hypertension pulmonaire.

**Aucun lien mécanistique établi.** RET n'a pas de rôle reconnu dans le remodelage vasculaire pulmonaire. Le score élevé (99,18 %) provient d'une prédiction du graphe de connaissances, sans confirmation clinique ni préclinique dans les données fournies. Les indications d'origine et le mécanisme d'action manquant, la plausibilité mécanistique ne peut pas être vérifiée par rapport aux données sources.

Point d'attention : l'hypertension artérielle systémique est un effet indésirable connu du sélpercatinib. Cela constitue un signal de sécurité et non un argument en faveur de l'indication prédite.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune de ces publications n'étudie le sélpercatinib dans l'hypertension pulmonaire. Elles concernent son usage ou son profil de sécurité dans d'autres contextes.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Pharmacovigilance (base FAERS) | Front Pharmacol | Comparaison des événements indésirables du pralsétinib et du sélpercatinib en vie réelle |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Cohorte rétrospective | Ther Adv Med Oncol | Sélpercatinib dans le CBNPC avec fusion de RET (étude SIREN), patients traités via un programme d'accès |
| [41918669](https://pubmed.ncbi.nlm.nih.gov/41918669/) | 2026 | Rapport de cas | Cureus | Cancer médullaire de la thyroïde métastatique dans la NEM 2B (mutation RET M918T) : prise en charge à long terme et thérapie ciblée |

## Informations de Marché en France

Le texte des indications approuvées n'est pas renseigné dans les données disponibles.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 66580529 | RETSEVMO 40 mg, gélule | Gélule |
| 65136400 | RETSEVMO 80 mg, comprimé pelliculé | Comprimé pelliculé |
| 61648467 | RETSEVMO 80 mg, gélule | Gélule |

Titulaire : ELI LILLY NEDERLAND BV (Pays-Bas).

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur sélectif de la kinase RET) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Mise en garde connue** : l'hypertension artérielle systémique est un effet indésirable connu du sélpercatinib. Cela est particulièrement préoccupant dans un contexte d'hypertension pulmonaire.

Pour les autres informations de sécurité (contre-indications, interactions médicamenteuses), veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5) : aucun essai clinique, aucune publication ciblant l'hypertension pulmonaire et aucun lien mécanistique plausible. Un effet indésirable connu (hypertension systémique) va dans le sens opposé.
- Les deux autres prédictions (migraine, migraine avec aura du tronc cérébral) sont aussi au niveau L5 et sans aucune preuve. Elles semblent être des artefacts du graphe de connaissances.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice ANSM (mises en garde, contre-indications), une lacune bloquante pour le criblage de sécurité
- Indications approuvées et mécanisme d'action détaillé (DrugBank)
- Données précliniques montrant un rôle de RET dans la vasculopathie pulmonaire
- Analyse du signal d'hypertension avant toute poursuite de l'évaluation
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

