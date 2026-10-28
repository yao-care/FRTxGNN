---
layout: default
title: Atezolizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 78
evidence_level: L5
indication_count: 6
monitor_inn: "atezolizumab"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-10-23
description: "Atezolizumab : nouvelle indication prédite, Adénocarcinome du ligament utérin (niveau de preuve L5). Indication d'origine : Carcinome urothélial"
---

# Atezolizumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Atézolizumab : Du carcinome urothélial à l'adénocarcinome du ligament utérin
{: .text-alpha }

## Résumé en Une Phrase

L'atézolizumab est un anticorps monoclonal anti-PD-L1, dont l'usage d'origine est le carcinome urothélial (carcinome à cellules transitionnelles).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**adénocarcinome du ligament utérin** (première prédiction du classement), mais aucune étude ne l'évalue directement : le niveau de preuve est **L5**.
Pour la prédiction suivante, le **carcinome endocervical**, on dénombre **2 essais cliniques** et **1 publication** (une revue sur une autre entité, le carcinome neuroendocrine à petites cellules du col).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carcinome urothélial (relation enregistrée dans le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Adénocarcinome du ligament utérin |
| Score de Prédiction TxGNN | 0,9993 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, l'atézolizumab est un inhibiteur de point de contrôle immunitaire qui bloque PD-L1 et peut ainsi restaurer l'activité antitumorale des lymphocytes T.

La relation avec l'indication d'origine (carcinome urothélial) repose sur ce principe : de nombreuses tumeurs solides expriment PD-L1. Un adénocarcinome gynécologique pourrait donc, en théorie, répondre à un blocage de cette voie.

Cette hypothèse reste toutefois **spéculative** pour l'adénocarcinome du ligament utérin : aucun essai ni publication ne l'étudie, et le score élevé du modèle est une prédiction purement computationnelle. Le mécanisme d'action d'origine n'étant pas documenté, le lien mécanistique ne peut pas être vérifié.

**Autres prédictions du classement (pour information) :**

| Rang | Maladie prédite | Score | Niveau de preuve |
|------|------|------|------|
| 2 | Carcinome endocervical | 0,9992 | L5 (voir ci-dessous) |
| 3 | Carcinome adénoïde kystique du col utérin | 0,9992 | L5 |
| 4 | Adénocarcinome séreux du ligament utérin | 0,9992 | L5 |
| 5 | Adénocarcinome mucineux du col, variante à cellules en bague à chaton | 0,9991 | L5 |
| 6 | Adénocarcinome mucineux du col, variante intestinale | 0,9991 | L5 |

---

## Preuves d'Essais Cliniques

Pour la première prédiction (adénocarcinome du ligament utérin) : aucun essai clinique associé n'est enregistré actuellement.

À titre informatif, deux essais portent sur le carcinome du col utérin (prédiction de rang 2, carcinome endocervical) :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02921269](https://clinicaltrials.gov/study/NCT02921269) | Phase 2 | Terminé | 11 | Atézolizumab + bévacizumab dans le cancer du col récidivant, persistant ou métastatique ; petit effectif, résultats d'efficacité non fournis |
| [NCT03738228](https://clinicaltrials.gov/study/NCT03738228) | Phase 1 | Terminé | 40 | Atézolizumab en amorçage immunitaire puis avec chimioradiothérapie à champ étendu dans le cancer du col localement avancé avec atteinte ganglionnaire ; pas de données d'efficacité fournies |

---

## Preuves de la Littérature

Pour la première prédiction (adénocarcinome du ligament utérin) : aucune littérature associée n'est disponible actuellement.

Pour le carcinome endocervical (rang 2) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Revue | Biomedical Journal | Carcinome neuroendocrine à petites cellules du col : bases moléculaires et avancées thérapeutiques ; les données publiées se limitent à des séries et rapports de cas |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69209340 | TECENTRIQ 1 875 mg, solution injectable | Solution injectable | Non renseignée |
| 64422886 | TECENTRIQ 840 mg, solution à diluer pour perfusion | Solution à diluer pour perfusion | Non renseignée |
| 60345905 | TECENTRIQ 1200 mg, solution à diluer pour perfusion | Solution à diluer pour perfusion | Non renseignée |

L'atézolizumab est commercialisé en France (titulaire : Roche Registration, Allemagne).

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Immunothérapie (anticorps anti-PD-L1) |
| Risque de Myélosuppression | Faible (non cytotoxique conventionnel ; aucune donnée de toxicité détaillée disponible) |
| Classification d'Émétogénicité | Faible |
| Éléments de Surveillance | NFS, fonctions hépatique, rénale et thyroïdienne (effets immuno-médiés) |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

**Interactions médicamenteuses** : 75 interactions sont recensées. Parmi les principales :
- **Majeures** : adalimumab, baricitinib, vaccin BCG (souche Tice vivante).
- **Modérées** : corticoïdes (hydrocortisone, triamcinolone, bétaméthasone, budésonide, dexaméthasone, prednisolone, prednisone, méthylprednisolone, déflazacort), roflumilast, azathioprine, alemtuzumab, anakinra, alefacept, vaccin anthrax, vaccin antitétanique, vaccin adénovirus de type 4.

Ces interactions concernent surtout les immunosuppresseurs et les vaccins vivants. Pour les mises en garde et contre-indications, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Pour l'adénocarcinome du ligament utérin, aucun essai ni publication ne l'étudie directement ; la prédiction repose uniquement sur le modèle (niveau L5).
- Le carcinome endocervical, mieux documenté (essais de phase 1 et 2 terminés, petits effectifs, sans résultats d'efficacité fournis), constitue une piste plus concrète à examiner comme question de recherche.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (analyse de sécurité impossible sans elles)
- Les données détaillées sur le mécanisme d'action
- Des données d'expression de PD-L1 et des études spécifiques aux histologies gynécologiques rares concernées
- Les résultats d'efficacité des essais NCT02921269 et NCT03738228 pour évaluer le carcinome endocervical
- Les textes d'indication des AMM pour confirmer les usages approuvés
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

