---
layout: default
title: Pentostatin
parent: Prédiction du modèle uniquement (L5)
nav_order: 589
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Pentostatin : nouvelle indication prédite, Rhabdomyosarcome embryonnaire de type botryoïde du vagin (niveau de preuve L5). Indication d'origine : Leucémie à tricholeucocytes et variante"
monitor_inn: "pentostatin"
predicted_indications: ["botryoid-type embryonal rhabdomyosarcoma of the vagina", "parameningeal embryonal rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "embryonal extrahepatic bile duct rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "liver sarcoma"]
---

# Pentostatin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

# Pentostatine : De la leucémie à tricholeucocytes au rhabdomyosarcome embryonnaire du vagin (type botryoïde)

## Résumé en Une Phrase

La pentostatine est un inhibiteur de l'adénosine désaminase (ADA), initialement utilisé pour traiter la leucémie à tricholeucocytes et sa forme variante.
Le modèle TxGNN la prédit comme potentiellement efficace pour le **rhabdomyosarcome embryonnaire de type botryoïde du vagin**, ainsi que pour six autres tumeurs apparentées (rhabdomyosarcomes et sarcome du foie).
Actuellement, **aucun essai clinique** et **aucune publication** ne soutiennent cette prédiction : elle repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Leucémie à tricholeucocytes et variante (selon le graphe de connaissances ; le texte d'indication de l'AMM française n'est pas renseigné) |
| Nouvelle Indication Prédite | Rhabdomyosarcome embryonnaire de type botryoïde du vagin |
| Score de Prédiction TxGNN | 99,54 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Autorisation annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, la pentostatine inhibe l'adénosine désaminase, ce qui entraîne une déplétion lymphocytaire. Son efficacité est établie dans la leucémie à tricholeucocytes, une hémopathie lymphoïde.

Aucune donnée ne relie l'inhibition de l'ADA à la biologie du rhabdomyosarcome, un sarcome solide, principalement pédiatrique. Le score élevé (0,995) reflète plus probablement la proximité dans le graphe de connaissances avec d'autres sous-types de rhabdomyosarcome qu'une preuve biologique directe. La similarité avec l'indication originale n'a pas été évaluée.

Les autres prédictions du modèle vont dans le même sens (score ≈ 0,994–0,995, sans aucune preuve) :
- rhabdomyosarcome embryonnaire paraméningé (99,52 %) ;
- rhabdomyosarcome, terme général (99,51 %) ;
- rhabdomyosarcome embryonnaire des voies biliaires extrahépatiques (99,51 %) et rhabdomyosarcome des voies biliaires extrahépatiques (99,50 %) ;
- rhabdomyosarcome embryonnaire de la prostate (99,50 %) ;
- sarcome du foie (99,42 %).

Ces entrées se recoupent largement et n'apportent pas de preuve indépendante.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67322542 | NIPENT 10 mg, poudre pour solution pour injection, poudre pour solution pour perfusion (Pfizer Holding France), statut : annulée | Poudre pour solution pour injection ou pour perfusion | Non renseignée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (analogue des purines / antimétabolite) |
| Risque de Myélosuppression | Élevé probable : le graphe de connaissances signale des contre-indications liées à la neutropénie, la thrombocytopénie, l'anémie, la leucopénie et l'agranulocytose |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | NFS avec formule, fonction rénale et hépatique |
| Protection de Manipulation | Appliquer les réglementations de manipulation des médicaments cytotoxiques |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie rénale, maladie hépatique, maladie de la vésicule biliaire, pyourétère, thrombocytopénie, neutropénie, agranulocytose, leucopénie, anémie (dont macrocytaire), maladie infectieuse, trouble hypotensif, œdème pulmonaire.
- **Interactions médicamenteuses** : 138 interactions recensées. Parmi les 20 premières renvoyées :
  - **Majeures** : défériprone, lexidronam de samarium (¹⁵³Sm), adalimumab, baricitinib.
  - **Modérées** : palifermine, chlorure de strontium (⁸⁹Sr), mercaptopurine, roflumilast, chloramphénicol (y compris ophtalmique), zidovudine, anatoxine tétanique, aldesleukine, alefacept, alemtuzumab, anakinra, vaccin contre l'anthrax, azathioprine.
  - **Mineures** : lévofloxacine, allopurinol.

Les mises en garde et contre-indications du texte de la notice ANSM n'ont pas pu être obtenues ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et aucun lien mécanistique plausible n'est étayé par les données.
- Le médicament n'a plus d'AMM valide en France, et le profil de sécurité (myélosuppression, interactions nombreuses) est préoccupant.
- Les données de sécurité de la notice sont manquantes, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications).
- Compléter les données sur le mécanisme d'action (par exemple via DrugBank).
- Réaliser une validation préclinique indépendante, comme des tests de sensibilité in vitro sur des lignées cellulaires de rhabdomyosarcome.
- Mener une revue de la littérature pour confirmer l'absence ou l'existence de données sur la pentostatine dans les sarcomes.
- Évaluer la situation réglementaire (AMM annulée) et la voie d'administration (injectable) si le projet se poursuit.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

