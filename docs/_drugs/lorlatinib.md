---
layout: default
title: Lorlatinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 181
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

# Lorlatinib : Du CBNPC ALK-positif à la Fibromatose Gingivale

## Résumé en Une Phrase

Lorlatinib est un inhibiteur de tyrosine kinase de troisième génération (ALK/ROS1), pénétrant dans le cerveau. D'après la littérature fournie, il est utilisé dans le cancer bronchique non à petites cellules (CBNPC) ALK-positif ; le texte d'indication des AMM françaises n'est pas renseigné.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **fibromatose gingivale**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Fibromatose gingivale |
| Score de Prédiction TxGNN | 99,81 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans DrugBank. Sur la base des informations connues, lorlatinib est un inhibiteur des kinases ALK et ROS1. Son efficacité dans le CBNPC ALK-positif est établie par la littérature fournie, notamment l'essai de phase 3 CROWN.

Pour la fibromatose gingivale, aucun lien mécanistique n'est établi. Aucun rôle d'ALK ou de ROS1 dans cette pathologie n'est documenté dans les données fournies. Le score élevé de TxGNN (0,998) reflète une prédiction du modèle et n'est corroboré par aucun essai ni aucune publication. Le lien avec l'indication d'origine reste à évaluer.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 63776483 | LORVIQUA 25 mg, comprimé pelliculé | Comprimé pelliculé | Pfizer Europe MA EEIG (Belgique) |
| 66586838 | LORVIQUA 100 mg, comprimé pelliculé | Comprimé pelliculé | Pfizer Europe MA EEIG (Belgique) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase ALK/ROS1) |

Pour le risque de myélosuppression, l'émétogénicité, les éléments de surveillance et la protection de manipulation, veuillez consulter les mises en garde et précautions de la notice.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Les mises en garde, les contre-indications et les interactions médicamenteuses ne sont pas disponibles dans les données fournies, et la notice ANSM n'a pas encore été analysée.

À titre indicatif, la littérature récupérée pour d'autres indications prédites signale des événements indésirables du lorlatinib :
- Effets métaboliques : hypercholestérolémie, hypertriglycéridémie, prise de poids.
- Syndrome néphrotique associé à une hyperlipidémie.
- Syndrome de détresse respiratoire aiguë (cas rapporté).
- Événements indésirables du système nerveux central.
- Toxicité pulmonaire en association avec un anticorps anti-GD2 (neuroblastome).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication, et sans rationnel mécanistique plausible pour la fibromatose gingivale.
- L'analyse de sécurité est bloquée faute de notice ANSM exploitable.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications, indications autorisées) : lacune bloquante.
- Obtenir les données de mécanisme d'action via DrugBank.
- Identifier un rationnel biologique reliant ALK/ROS1 à la fibromatose gingivale, par exemple par des études précliniques, avant tout investissement clinique.
- Priorité de recherche : parmi les autres prédictions du modèle, le carcinome du hile pulmonaire (rang 4, niveau L4, stade S1) est le plus plausible. Il repose sur un cas rapporté de réponse complète pathologique en néoadjuvant dans un cancer du poumon ALK-positif, sans preuve indépendante pour cette entité.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

