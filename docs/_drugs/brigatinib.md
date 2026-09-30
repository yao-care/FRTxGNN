---
layout: default
title: Brigatinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 60
evidence_level: L5
indication_count: 10
---

# Brigatinib
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

# Brigatinib : Du Cancer Bronchique Non à Petites Cellules ALK-positif à la Fibromatose Gingivale

## Résumé en Une Phrase

Le brigatinib est un inhibiteur de tyrosine kinase utilisé à l'origine dans le traitement du cancer bronchique non à petites cellules (CBNPC) ALK-positif.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **fibromatose gingivale**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette prédiction : elle repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | CBNPC ALK-positif (d'après l'analyse de l'Evidence Pack ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Fibromatose gingivale |
| Score de Prédiction TxGNN | 99,89 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 4 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le brigatinib fait partie des inhibiteurs de tyrosine kinase ciblant ALK. Son efficacité dans le CBNPC ALK-positif est établie, mais rien dans les données fournies ne permet de l'appliquer mécanistiquement à la fibromatose gingivale.

Le score du modèle est très élevé (99,89 %). Toutefois, le modèle ne relie cette prédiction à aucune voie ALK ou EGFR plausible, et aucune étude ne l'appuie. L'indication originale est une tumeur maligne dépendante d'un oncogène. La fibromatose gingivale est une prolifération fibreuse bénigne de la gencive, sans dépendance à ALK connue dans les données disponibles.

Cette prédiction doit donc être considérée comme une simple hypothèse générée par le modèle, sans fondement biologique vérifié à ce stade.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60648770 | ALUNBRIG 90 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée dans les données |
| 66949061 | ALUNBRIG 180 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée dans les données |
| 61066196 | ALUNBRIG 90 mg + 180 mg, comprimé pelliculé | Comprimé pelliculé et comprimé pelliculé | Non renseignée dans les données |
| 62626993 | ALUNBRIG 30 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée dans les données |

Titulaire des quatre AMM : TAKEDA PHARMA (Danemark).

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase), et non cytotoxique conventionnel |

Veuillez consulter les mises en garde et précautions de la notice pour le risque de myélosuppression, l'émétogénicité, la surveillance et les mesures de protection lors de la manipulation.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication et sans lien mécanistique plausible. Les données de sécurité issues de la notice ANSM manquent aussi, ce qui empêche de passer à l'étape de sélection de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications), lacune bloquante
- Obtenir les données sur le mécanisme d'action (par exemple via l'API DrugBank)
- Rechercher dans la littérature un lien biologique entre les kinases ciblées par le brigatinib et la fibromatose gingivale
- Évaluer séparément le signal observé dans la schwannomatose liée à NF2 (étude clinique de 2024 et données précliniques), sans rapport direct avec cette prédiction mais potentiellement plus solide comme piste de repositionnement

*Ce rapport est fourni à titre de référence pour la recherche et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

