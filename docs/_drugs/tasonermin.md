---
layout: default
title: Tasonermin
parent: Prédiction du modèle uniquement (L5)
nav_order: 732
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "tasonermin"
predicted_indications: ["prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "renal pelvis papillary urothelial carcinoma", "HER2 positive breast carcinoma", "uterine ligament adenocarcinoma", "endocervical carcinoma", "uterine ligament serous adenocarcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament clear cell adenocarcinoma"]
description: "Tasonermin : nouvelle indication prédite, Carcinome urothélial de l'urètre prostatique (prostatic urethra urothelial carcinoma) (niveau de preuve L5). Indication d'origine : Non renseignée dans les d…"
---

# Tasonermin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

## Tasonermin: Carcinome urothélial de l'urètre prostatique (prostatic urethra urothelial carcinoma)
{: .text-alpha }

## Résumé en Une Phrase

Tasonermin est du TNF-alpha humain recombinant, initialement utilisé pour le traitement des sarcomes des tissus mous, par perfusion isolée de membre.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **carcinome urothélial de l'urètre prostatique**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction issue du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Carcinome urothélial de l'urètre prostatique (prostatic urethra urothelial carcinoma) |
| Score de Prédiction TxGNN | 0.9981 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, tasonermin est une forme recombinante du TNF-alpha humain, utilisée avec la perfusion isolée de membre pour les sarcomes des tissus mous des membres. Une hypothèse plausible est que le TNF-alpha détruit la vascularisation tumorale et améliore la pénétration de la chimiothérapie.

Rien dans les données compilées pour ce rapport ne relie ce mécanisme au carcinome urothélial de l'urètre prostatique. Le score élevé (0,9981) provient du modèle TxGNN (apprentissage profond) et peut refléter des similitudes apprises par le modèle entre maladies apparentées, et non une preuve biologique ni une preuve de efficacité. Par ailleurs, l'usage approuvé est strictement limité à la perfusion régionale d'un membre, car le TNF-alpha administré par voie systémique présente une toxicité limitante. Cette voie d'administration n'est pas transposable telle quelle à une tumeur de l'urètre.

D'autres prédictions du modèle présentent des scores très proches (0,9960 à 0,9980) : carcinome urothélial sarcomatoïde du bassinet du rein, variant sarcomatoïde du carcinome urothélial vésical infiltrant, carcinome urothélial papillaire du bassinet, carcinome mammaire HER2 positif, ainsi que plusieurs adénocarcinomes gynécologiques (ligament utérin, endocol). Les variants sarcomatoïdes partagent des caractéristiques histologiques avec les sarcomes, ce qui les rend un peu plus plausibles sur le plan biologique, mais aucune de ces prédictions n'est corroborée par des essais ou des publications.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69328782 | BEROMUN 1 mg, poudre pour solution pour perfusion (BELPHARMA, Luxembourg) | Poudre pour solution pour perfusion | Non renseignée (AMM active) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Immunothérapie / modulateur biologique (cytokine, TNF-alpha recombinant) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter la notice ; en pratique, surveillance hémodynamique et des fonctions hépatique et rénale en cas de fuite systémique |
| Protection de Manipulation | Veuillez consulter la notice pour les mesures de manipulation |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été identifiée dans les données compilées. Cette absence ne doit pas être interprétée comme une absence de risque : le TNF-alpha systémique est connu pour sa toxicité dose-limitante (hypotension, syndrome de fuite capillaire).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Le mécanisme n'est pas documenté, la voie d'administration approuvée (perfusion isolée de membre) n'est pas adaptée à l'urètre, et l'AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Informations de sécurité issues de la notice ANSM (mises en garde, contre-indications), actuellement manquantes et bloquantes pour tout examen de sécurité
- Données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Recherche d'études précliniques ou observationnelles sur le TNF-alpha dans les carcinomes urothéliaux
- Évaluation de la faisabilité d'une voie d'administration régionale adaptée (par exemple intravésicale), avec un profil de toxicité acceptable
- Clarification du statut réglementaire, l'AMM étant annulée
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

