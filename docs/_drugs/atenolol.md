---
layout: default
title: Atenolol
parent: Prédiction du modèle uniquement (L5)
nav_order: 77
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Atenolol : nouvelle indication prédite, Infarctus du myocarde postéro-latéral (niveau de preuve L5). Indication d'origine : Hypertension artérielle, infarctus du myocarde"
monitor_inn: "atenolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
---

# Atenolol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

# Aténolol : De l'hypertension et de l'infarctus du myocarde à l'infarctus du myocarde postéro-latéral

## Résumé en Une Phrase

L'aténolol est un bêta-bloquant cardiosélectif (bêta-1), initialement utilisé pour traiter l'hypertension artérielle et l'infarctus du myocarde.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infarctus du myocarde postéro-latéral**, mais cette prédiction correspond surtout à un sous-type anatomique d'une indication déjà connue.
Aucun essai clinique et aucune publication spécifique ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle, infarctus du myocarde (texte d'indication des AMM non renseigné ; indications issues du graphe de connaissances) |
| Nouvelle Indication Prédite | Infarctus du myocarde postéro-latéral |
| Score de Prédiction TxGNN | 99,87 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'aténolol appartient à la classe des bêta-1 bloquants. Son efficacité dans l'infarctus du myocarde et l'hypertension est établie. Il réduit la demande en oxygène du myocarde et la charge ischémique, et diminue la libération de rénine.

L'infarctus postéro-latéral est un sous-type anatomique de l'infarctus du myocarde, déjà une indication connue. Le score élevé du modèle reflète donc surtout l'indication parente et non une véritable opportunité de repositionnement.

Les autres prédictions du modèle (infarctus postéro-inférieur et septal, atteinte rénale hypertensive maligne, hypertension rénovasculaire maligne, hypertensions pulmonaires, cœur pulmonaire chronique, syndrome de Braddock) obtiennent des scores comparables (99,04 % à 99,87 %). Elles sont soit des sous-types d'indications existantes, soit mécanistiquement fragiles. Pour les hypertensions pulmonaires et le cœur pulmonaire chronique, les bêta-bloquants posent même des problèmes de sécurité (bronchospasme, baisse du débit cardiaque, dépendance du ventricule droit au tonus sympathique).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature spécifique à l'infarctus postéro-latéral n'est disponible. À titre indicatif, voici les publications retrouvées pour des sous-types voisins (infarctus postéro-inférieur et septal) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | ECR (petit, simple aveugle, croisé) | La Revue de médecine interne | Comparaison de l'activité anti-ischémique de l'aténolol (200 mg) et du diltiazem (240 mg) chez 23 patients après un infarctus postéro-inférieur ou antérieur limité ; preuve indirecte et ancienne |
| [7257500](https://pubmed.ncbi.nlm.nih.gov/7257500/) | 1981 | Étude diagnostique clinique (petite) | Zeitschrift für Kardiologie | Scintigraphie de stress au thallium-201 chez 14 patients coronariens après aténolol 5 mg IV ; étude diagnostique, sans preuve d'efficacité thérapeutique |

## Informations de Marché en France

Les 20 AMM recensées sont annulées. Aucun texte d'indication approuvée n'est renseigné. Principales AMM :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62022861 | ATENOLOL VIATRIS 100 mg | Comprimé pelliculé sécable | Non renseignée (AMM annulée) |
| 65634625 | ATENOLOL BIOGARAN 100 mg | Comprimé sécable | Non renseignée (AMM annulée) |
| 65366472 | TENORMINE 50 mg | Comprimé pelliculé sécable | Non renseignée (AMM annulée) |
| 62215045 | ATENOLOL SANDOZ 100 mg | Comprimé pelliculé sécable | Non renseignée (AMM annulée) |
| 61436304 | TENORMINE 5 mg/10 ml | Solution injectable IV | Non renseignée (AMM annulée) |

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : asthme (y compris allergique et intrinsèque), bloc atrioventriculaire, maladie de Raynaud, diabète (types 1 et 2, acidocétose diabétique), insuffisance hépatique, psoriasis, lupus érythémateux systémique, goutte, anaphylaxie, pancréatite, anurie, hypercalcémie, néphrocalcinose, carence en potassium, troubles anxieux et dysthymiques.
- **Interactions médicamenteuses** : 294 interactions recensées. Parmi les premières, de niveau modéré : épinéphrine, hydrocortisone, hyoscyamine, bupropion, triamcinolone, morphine, acétohexamide, atropine, bétaméthasone, budésonide, ainsi que plusieurs sels de calcium. Interactions mineures : acide acétylsalicylique, hydroxyde d'aluminium, attapulgite.
- **Dose en cas d'insuffisance rénale** : l'aténolol est éliminé par voie rénale, un ajustement posologique est nécessaire.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction concerne un sous-type d'une indication déjà établie, sans essai ni publication spécifique (niveau L5). Toutes les AMM françaises sont annulées, et les données de sécurité issues de la notice manquent, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Clarifier le statut réglementaire (raisons de l'annulation des AMM et existence éventuelle d'autres spécialités commercialisées)
- Vérifier si l'infarctus postéro-latéral apporte une valeur ajoutée par rapport à l'indication « infarctus du myocarde » déjà connue
- Écarter ou réévaluer les prédictions à risque (hypertensions pulmonaires, cœur pulmonaire chronique) au regard de la sécurité des bêta-bloquants
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

