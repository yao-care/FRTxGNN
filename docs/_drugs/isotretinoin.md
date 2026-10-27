---
layout: default
title: Isotretinoin
parent: Prédiction du modèle uniquement (L5)
nav_order: 417
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Isotretinoin : nouvelle indication prédite, Hypertension rénovasculaire maligne (niveau de preuve L5). Indication d'origine : Hypertension"
monitor_inn: "isotretinoin"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Isotretinoin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Isotrétinoïne : De l'Hypertension à l'Hypertension Rénovasculaire Maligne
{: .text-alpha }

## Résumé en Une Phrase

Selon le graphe de connaissances utilisé par le modèle, l'isotrétinoïne est associée à l'hypertension (indication d'origine dans ce graphe). En pratique, elle est connue en France sous des marques comme Procuta, Curacne ou Contracne.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hypertension rénovasculaire maligne**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension (selon le graphe de connaissances ; aucun texte d'indication dans les AMM compilées) |
| Nouvelle Indication Prédite | Hypertension rénovasculaire maligne |
| Score de Prédiction TxGNN | 99,01 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Seulement des AMM annulées |
| Nombre d'AMM | 17 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Le seul élément de soutien est le score élevé du modèle (0,990). Aucune voie biologique plausible reliant l'isotrétinoïne au contrôle de la pression artérielle dans l'hypertension rénovasculaire n'a été établie.

La signalisation des rétinoïdes a été explorée dans des modèles expérimentaux de régulation de la rénine et de remodelage vasculaire, mais cette piste reste spéculative et sans données cliniques. De plus, l'indication d'origine retenue par le graphe (hypertension) ne correspond pas à l'usage connu du médicament en France, qui est lié à l'acné sévère sous forme de capsules molles. Les AMM compilées ne contiennent d'ailleurs aucun texte d'indication.

Une seconde prédiction, l'**hypertension rénale maligne** (score identique de 99,01 %), provient très probablement du même voisinage dans le graphe (le parent « trouble hypertensif »). Les deux prédictions ne constituent donc pas des signaux indépendants.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 17 AMM sont annulées. Les 5 premières listées dans les données compilées :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69316449 | PROCUTA 5 mg | Capsule molle | Non renseignée |
| 62318935 | CURACNE 10 mg | Capsule molle | Non renseignée |
| 67682298 | PROCUTA 40 mg | Capsule molle | Non renseignée |
| 62872308 | ISOTRETINOINE ACNETRAIT 40 mg | Capsule molle | Non renseignée |
| 67952249 | PROCUTA 20 mg | Capsule molle | Non renseignée |

Une formulation topique (ROACCUTANE 0,05 %, gel pour application locale, SERP, AMM 66296030) figure également parmi les AMM annulées.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : troubles anxieux, troubles névrotiques et dysthymiques, maladie rénale, pancréatite, maladie hépatique, maladie de la vésicule biliaire, angio-œdème (y compris héréditaire et acquis), maladie inflammatoire de l'intestin, ostéoporose, lupus érythémateux systémique, troubles psychotiques et mentaux (dont schizophréniformes et schizo-affectifs), carence en potassium, diabète et acidocétose diabétique, neutropénie, agranulocytose et trouble hypotensif.
- **Interactions médicamenteuses** : 98 interactions recensées. Parmi les principales :
  - **Majeures** : doxycycline, minocycline, tétracycline, vitamine A.
  - **Modérées** : corticoïdes (bétaméthasone, budésonide, dexaméthasone, hydrocortisone, prednisolone, prednisone, triamcinolone), warfarine, dicoumarol, éthanol, naltrexone, nitisinone, fostamatinib, ivacaftor, lumacaftor, abamétapir (topique).

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui n'ont pas pu être compilées.

Le profil de risque connu de l'isotrétinoïne (tératogénicité, effets sur les lipides, atteintes hépatiques et rénales potentielles) est défavorable pour des patients souffrant d'hypertension maligne avec atteinte rénale. Les 98 interactions compliqueraient en outre l'association aux traitements antihypertenseurs.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai ni publication. Le mécanisme d'action est inconnu, le rapport bénéfice-risque semble défavorable et toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), actuellement bloquant pour le criblage de sécurité
- Obtenir les données sur le mécanisme d'action (requête DrugBank)
- Disposer de données précliniques ou cliniques, ou d'une revue de la littérature, soutenant un lien entre rétinoïdes et hypertension rénovasculaire
- Clarifier le fait que l'indication d'origine du graphe (hypertension) diffère de l'usage réel du médicament
- Évaluer la faisabilité de la voie d'administration et l'intérêt réglementaire, vu l'annulation de toutes les AMM
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

