---
layout: default
title: Avelumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Avelumab : nouvelle indication prédite, Tumeur liée à l'herpèsvirus humain 8 (niveau de preuve L5). Indication d'origine : Carcinome neuroendocrine cutané (texte d'indication de l'AMM non rens…"
monitor_inn: "avelumab"
predicted_indications: ["human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "adenosine deaminase deficiency", "reticular dysgenesis", "Immunoerythromyeloid hypoplasia", "non-severe combined immunodeficiency", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma"]
---

# Avelumab
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

## Avelumab : Du Carcinome Neuroendocrine Cutané à la Tumeur Liée à l'Herpèsvirus Humain 8
{: .text-alpha }

## Résumé en Une Phrase

Avelumab est un anticorps anti-PD-L1, initialement associé au traitement du carcinome neuroendocrine cutané (carcinome à cellules de Merkel).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **tumeur liée à l'herpèsvirus humain 8** (par exemple le sarcome de Kaposi), mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : la prédiction repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carcinome neuroendocrine cutané (texte d'indication de l'AMM non renseigné) |
| Nouvelle Indication Prédite | Tumeur liée à l'herpèsvirus humain 8 |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement annulée (AMM annulée) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, l'avelumab est un anticorps dirigé contre PD-L1 : il bloque l'interaction PD-L1/PD-1 et restaure l'activité des lymphocytes T contre les cellules tumorales.

Les tumeurs liées à l'HHV-8 (sarcome de Kaposi, lymphome primitif des séreuses) impliquent une échappée immunitaire d'origine virale et une possible surexpression de la voie PD-L1/PD-1. Un blocage des points de contrôle immunitaires est donc biologiquement plausible. Toutefois, ce lien repose uniquement sur le score TxGNN et un raisonnement mécanistique général ; la similarité avec l'indication originale n'a pas été évaluée.

**Autres prédictions du modèle (toutes de niveau L5, sans essai ni publication) :**

- **Plus plausibles :** le carcinome urothélial de l'urètre prostatique et le carcinome à cellules transitionnelles sarcomatoïde du bassinet du rein (score respectif de 99,92 % et 99,91 %). L'avelumab dispose d'une preuve de phase 3 dans le carcinome urothélial en traitement d'entretien (JAVELIN Bladder 100), mais aucune donnée spécifique à ces sites n'a été fournie. Ces deux pistes sont classées « Research Question ». Une revue des sous-groupes des essais existants serait une étape raisonnable.
- **Peu plausibles :** la tumeur neuroendocrine de l'oreille moyenne, la tumeur cutanée à cellules granuleuses maligne et l'ectomésenchymome n'ont pas de justification mécanistique claire. Les déficits immunitaires primitifs (déficit en adénosine désaminase, dysgénésie réticulaire, hypoplasie immuno-érythro-myéloïde, immunodéficience combinée non sévère) ne peuvent pas être corrigés par un blocage de PD-L1 ; ces scores élevés sont probablement des artefacts du modèle.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60199966 | BAVENCIO 20 mg/mL, solution à diluer pour perfusion (MERCK EUROPE, Pays-Bas) | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Immunothérapie (anticorps monoclonal anti-PD-L1) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Interactions Médicamenteuses** (3 interactions de niveau majeur identifiées) :
  - Lénalidomide
  - Pomalidomide
  - Thalidomide

Pour les mises en garde et contre-indications, veuillez consulter la notice : ces informations ne sont pas disponibles dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la tumeur liée à l'HHV-8 n'est soutenue par aucun essai ni publication (niveau L5). L'AMM française est annulée et les données de sécurité de la notice sont absentes, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications)
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Rechercher des essais et publications sur l'avelumab dans les tumeurs liées à l'HHV-8 (sarcome de Kaposi, lymphome primitif des séreuses)
- Examiner les données de sous-groupes des essais dans le carcinome urothélial pour les pistes de l'urètre prostatique et du bassinet du rein
- Vérifier le statut réglementaire actuel (AMM annulée) et les autres autorisations européennes éventuelles
- Évaluer la portée clinique des interactions majeures avec lénalidomide, pomalidomide et thalidomide
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

