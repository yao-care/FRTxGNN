---
layout: default
title: Estramustine
parent: Prédiction du modèle uniquement (L5)
nav_order: 301
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
monitor_inn: "estramustine"
predicted_indications: ["fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "prostate leiomyoma", "benign prostate phyllodes tumor", "female breast carcinoma", "HIV infectious disease", "breast fibrocystic disease"]
description: "Estramustine : nouvelle indication prédite, Fibroma of prostate (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Estramustine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

## Estramustine: Fibroma of prostate
{: .text-alpha }

## Résumé en Une Phrase

L'estramustine est un agent cytotoxique, initialement utilisé dans le traitement du cancer de la prostate.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **susceptibilité au cancer de la prostate/du cerveau**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction.
Cette « indication » est une étiquette de prédisposition génétique et non une maladie traitable. Le score élevé reflète surtout la proximité de ce nœud avec l'usage existant dans le cancer de la prostate.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Fibroma of prostate |
| Score de Prédiction TxGNN | 0.9999 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé (aucune autorisation enregistrée) |
| Nombre d'AMM | 0 (valides : 0) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les sources compilées pour ce rapport. D'après les informations connues, l'estramustine associe une fraction estradiol à un carbamate de moutarde azotée. Il se lie aux protéines associées aux microtubules et à la tubuline, ce qui lui confère une activité antimitotique. Il s'accumule aussi dans le tissu prostatique grâce à une protéine de liaison spécifique (EMBP).

La prédiction est peu convaincante. « Susceptibilité au cancer de la prostate/du cerveau » désigne un terrain génétique et non une maladie à traiter. Il ne repose pas sur une logique thérapeutique propre.

Aucune donnée ne documente un bénéfice dans le cancer du cerveau. Le seul indice indirect, absent des données de ce nœud, est l'expression de l'EMBP dans les gliomes. Le lien mécanistique reste donc spéculatif.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (antimitotique, dérivé d'estradiol et de moutarde azotée) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | NFS, fonction hépatique et rénale, pression artérielle, glycémie, calcémie |
| Protection de Manipulation | Suivre les réglementations de manipulation des médicaments cytotoxiques |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : hypertension, épilepsie, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, insuffisance cardiaque congestive, diabète et acidocétose diabétique, gynécomastie, hypercalcémie, néphrocalcinose, thrombophlébite, migraine, maladie coronarienne et infarctus du myocarde, hémoglobinopathie, hyperbilirubinémie (dont syndrome de Gilbert), maladie cérébrovasculaire, troubles de la fonction sexuelle masculine.
- **Interactions médicamenteuses** : 111 interactions recensées. Les principales, de niveau modéré, concernent :
  - les corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, budésonide) ;
  - les antidiabétiques (metformine, acarbose, inhibiteurs de SGLT2, inhibiteurs de DPP-4, agonistes du GLP-1, chlorpropamide) ;
  - l'amphotéricine B ;
  - les sels de calcium et le calcitriol.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication. Elle porte sur une étiquette de prédisposition génétique, non sur une maladie traitable.

**Pour avancer, les éléments suivants sont nécessaires :**
- Reformuler la cible en une maladie cliniquement définie (par exemple le cancer du cerveau/glioblastome) avant toute évaluation.
- Récupérer la notice ANSM (mises en garde et contre-indications) et les données détaillées sur le mécanisme d'action.
- Clarifier la disponibilité du médicament en France.

**Remarque :** d'autres candidats du même médicament sont mieux étayés. Le carcinome mammaire féminin (L2) s'appuie sur un essai de phase 2 (NCT00003066, docétaxel + estramustine, 40 patients, statut inconnu) et sur plusieurs publications cliniques de phase I/II. Il constitue plutôt une question de recherche qu'une piste de développement, faute de données de phase 3. La catégorie « cancer de l'appareil reproducteur masculin » (L1) correspond surtout à l'indication d'origine (cancer de la prostate) et ne constitue pas un véritable repositionnement.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

