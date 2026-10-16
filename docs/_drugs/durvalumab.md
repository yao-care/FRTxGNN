---
layout: default
title: Durvalumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 265
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Durvalumab : nouvelle indication prédite, Carcinome urothélial de l'urètre prostatique (niveau de preuve L5). Indication d'origine : Carcinome à cellules transitionnelles"
---

# Durvalumab
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

# Durvalumab : Du Carcinome à Cellules Transitionnelles au Carcinome Urothélial de l'Urètre Prostatique

## Resume en Une Phrase

Durvalumab est un anticorps monoclonal anti-PD-L1, initialement rattaché au traitement du carcinome à cellules transitionnelles (carcinome urothélial).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **carcinome urothélial de l'urètre prostatique**, avec un score très élevé, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette indication précise.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Carcinome à cellules transitionnelles (source : graphe de connaissances ; le texte d'indication de l'AMM française n'est pas renseigné) |
| Nouvelle Indication Predite | Carcinome urothélial de l'urètre prostatique |
| Score de Prediction TxGNN | 99,98 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Annulée uniquement (AMM annulée) |
| Nombre d'AMM | 1 (0 valide, 1 annulée) |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, durvalumab est un inhibiteur du point de contrôle immunitaire ciblant PD-L1, et la voie PD-1/PD-L1 est pertinente dans les tumeurs urothéliales.

Le carcinome urothélial de l'urètre prostatique appartient à la même famille histologique que le carcinome à cellules transitionnelles. Il s'agit d'un sous-site de la même classe de maladie, et non d'une indication réellement nouvelle. L'extrapolation est donc biologiquement plausible, mais elle reste une prédiction : aucune donnée directe n'a été trouvée.

**Autres prédictions du modèle (pour contexte) :** parmi les 10 premières prédictions, plusieurs concernent d'autres tumeurs urothéliales (bassinet du rein, variante sarcomatoïde de la vessie) et des cancers gynécologiques (col de l'utérus, ligament utérin). Seules quelques-unes disposent d'essais précoces :

| Indication prédite | Score TxGNN | Niveau de preuve | Essais / publications |
|------|------|------|------|
| Carcinome urothélial sarcomatoïde du bassinet | 99,98 % | L3 | 1 essai / 0 |
| Carcinome urothélial infiltrant de la vessie, variante sarcomatoïde | 99,98 % | L3 | 2 essais / 0 |
| Carcinome de l'endocol | 99,91 % | L3 | 1 essai / 2 publications |

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour l'indication principale (carcinome urothélial de l'urètre prostatique).

À titre indicatif, des essais existent pour des indications voisines prédites :

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT03912818](https://clinicaltrials.gov/study/NCT03912818) | Phase 2 | Arrêté | 7 | Durvalumab + chimiothérapie néoadjuvante dans le cancer de la vessie à histologie variante ; arrêt après 7 patients, aucune conclusion d'efficacité possible |
| [NCT02812420](https://clinicaltrials.gov/study/NCT02812420) | Phase 1 précoce | Actif, non en recrutement | 54 | Étude pilote préopératoire durvalumab + trémélimumab dans le carcinome urothélial infiltrant à haut risque, inéligible au cisplatine ; pas de résultats publiés dans les données |
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Phase 1 | Terminé | 20 | Radiothérapie hypofractionnée + durvalumab + trémélimumab dans les cancers du col, du vagin ou de la vulve récidivants/métastatiques ; données de faisabilité et de sécurité |

## Preuves de la Litterature

Aucune littérature associée n'est disponible actuellement pour l'indication principale.

À titre indicatif, pour l'endocol (indication voisine prédite) :

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [42518016](https://pubmed.ncbi.nlm.nih.gov/42518016/) | 2026 | Essai clinique non randomisé (Phase 1) | Oncology and Therapy | Céralasertib + durvalumab chez des patients chinois atteints de tumeurs solides avancées, résistantes ou réfractaires à une immunothérapie anti-PD-(L)1 antérieure ; évaluation de la sécurité, de la pharmacocinétique et de l'activité antitumorale |
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Revue | Biomedical Journal | Carcinome neuroendocrine à petites cellules du col de l'utérus : bases moléculaires et avancées thérapeutiques ; pas de test direct d'efficacité du durvalumab |

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 63690956 | IMFINZI 50 mg/ml, solution à diluer pour perfusion (ASTRAZENECA AB) | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |

## Cytotoxicite

| Element | Contenu |
|------|------|
| Classification de Cytotoxicite | Immunothérapie (anticorps anti-PD-L1) |
| Risque de Myelosuppression | Faible (non cytotoxique conventionnel) ; données de toxicité non disponibles |
| Classification d'Emetogenicite | Faible |
| Elements de Surveillance | Veuillez consulter les mises en garde et précautions de la notice (suivi usuel des immunothérapies : NFS, fonction hépatique, rénale, thyroïdienne) |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considerations de Securite

**Interactions médicamenteuses** : 81 interactions sont recensées. Principales :
- **Majeure** : adalimumab
- **Modérée** : corticoïdes (hydrocortisone, prednisone, prednisolone, méthylprednisolone, dexaméthasone, bétaméthasone, budésonide, triamcinolone, déflazacort), roflumilast, alefacept, alemtuzumab, anakinra, vaccins (anatoxine tétanique, vaccin anti-charbon)
- **Mineure** : sels de zinc (acétate, gluconate, sulfate, chlorure)

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- Le score de prédiction est très élevé (99,98 %), mais aucune preuve clinique ni bibliographique directe n'existe pour le carcinome urothélial de l'urètre prostatique (niveau L5). Il s'agit d'un sous-site de la maladie d'origine, et l'AMM française est annulée.
- Les indications voisines (variantes sarcomatoïdes urothéliales, endocol) n'atteignent que le niveau L3 avec des essais précoces, petits ou arrêtés.

**Pour avancer, les elements suivants sont necessaires :**
- Mécanisme d'action détaillé (DrugBank)
- Mises en garde et contre-indications issues de la notice de l'ANSM, indispensables avant tout examen de sécurité
- Texte d'indication de l'AMM et clarification du statut réglementaire (AMM annulée)
- Données cliniques ou publications spécifiques à l'urètre prostatique et aux tumeurs urothéliales du haut appareil
- Résultats publiés des essais NCT02812420 et NCT03912818 (ce dernier terminé prématurément)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

