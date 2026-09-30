---
layout: default
title: Axitinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 50
evidence_level: L5
indication_count: 10
---

# Axitinib
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

# Axitinib : Du Carcinome Rénal Avancé au Carcinome Rénal à Translocation Xp11.2/TFE3

## Résumé en Une Phrase

L'axitinib est un inhibiteur des récepteurs VEGFR 1 à 3, commercialisé en France dans le carcinome rénal avancé (l'indication d'origine n'est pas renseignée dans les données ANSM du dossier).
Le modèle TxGNN prédit qu'il pourrait être efficace dans le **carcinome rénal associé aux translocations Xp11.2/fusions du gène TFE3**,
mais seul **1 essai clinique** (15 patients, sans résultats) et **aucune publication** soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM (le dossier indique une commercialisation dans le carcinome rénal avancé) |
| Nouvelle Indication Prédite | Carcinome rénal associé aux translocations Xp11.2/fusions du gène TFE3 |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L2 selon le dossier (à nuancer : l'essai n'est ni terminé ni publié) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

L'axitinib est un inhibiteur de tyrosine kinase qui cible sélectivement VEGFR-1, -2 et -3. Il bloque ainsi la signalisation qui alimente l'angiogenèse tumorale. Les données DrugBank détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. La description ci-dessus provient de l'argumentaire de repositionnement fourni.

Le carcinome rénal à fusion TFE3 est un sous-type rare de cancer du rein, avec un profil tumoral très vascularisé. Une activité des inhibiteurs de VEGFR est donc plausible. Elle est cohérente avec l'efficacité de l'axitinib dans le carcinome rénal avancé, démontrée par des essais de phase 3 (dont AXIS).

Cette plausibilité reste théorique. Aucune publication ne documente l'axitinib dans ce sous-type précis, et le seul essai identifié est très petit. La prédiction relève pour l'instant d'une hypothèse de recherche.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Phase 2 | Actif, hors recrutement (fin prévue : 13/11/2026) | 15 | Axitinib + nivolumab contre nivolumab seul dans le carcinome rénal à translocation TFE (tRCC), non résécable ou métastatique, tous âges. Aucun résultat disponible. |

Cet essai est directement pertinent (grade A), mais son effectif de 15 patients et l'absence de résultats ne permettent aucune conclusion sur l'efficacité.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Sur 20 AMM au total, voici 5 exemples :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69083347 | INLYTA 3 mg (Pfizer Europe MA EEIG) | Comprimé pelliculé | Non renseignée |
| 67939209 | INLYTA 5 mg (Pfizer Europe MA EEIG) | Comprimé pelliculé | Non renseignée |
| 64662504 | AXITINIB TEVA 3 mg (Teva) | Comprimé pelliculé | Non renseignée |
| 69115535 | AXITINIB TEVA 5 mg (Teva) | Comprimé pelliculé | Non renseignée |
| 62215554 | AXITINIB TEVA 7 mg (Teva) | Comprimé pelliculé | Non renseignée |

## Cytotoxicité

L'axitinib est un anticancéreux. Les éléments ci-dessous reposent sur les connaissances générales de sa classe, car le dossier ne contient pas de données de toxicité DrugBank.

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase anti-VEGFR), non cytotoxique conventionnel |
| Risque de Myélosuppression | Faible (à confirmer dans la notice) |
| Classification d'Émétogénicité | Faible |
| Éléments de Surveillance | Tension artérielle, fonction thyroïdienne, protéinurie, fonction hépatique, NFS. À confirmer dans la notice. |
| Protection de Manipulation | Comprimé oral. Veuillez consulter la notice pour les précautions de manipulation. |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La seule preuve clinique directe est un essai de phase 2 de 15 patients, sans résultats, et aucune publication ne soutient cette indication.
- Les mises en garde et contre-indications de la notice ANSM ne sont pas disponibles, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Résultats publiés de NCT03595124 (fin prévue en novembre 2026)
- Notice ANSM (mises en garde, contre-indications, interactions)
- Données DrugBank sur le mécanisme d'action
- Texte des indications approuvées pour les AMM françaises

**Remarque :** parmi les autres prédictions du modèle, le « carcinome rénal » (rang 6) correspond à une indication déjà commercialisée. Il s'agit d'une confirmation, pas d'un repositionnement nouveau. Il est étayé par plusieurs essais de phase 3 (AXIS, JAVELIN Renal 101, KEYNOTE-426). Le carcinome des tubes collecteurs (rang 9) est un sujet de recherche plus prometteur, avec un essai de phase 2 en cours de recrutement (NCT06211114).

*Ce rapport est destiné à la recherche et ne constitue pas un avis médical. Tout candidat au repositionnement nécessite une validation clinique avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

