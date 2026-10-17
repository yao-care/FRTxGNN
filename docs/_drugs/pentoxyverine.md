---
layout: default
title: Pentoxyverine
parent: Prédiction du modèle uniquement (L5)
nav_order: 590
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Pentoxyverine : nouvelle indication prédite, Laryngopharyngite aiguë (niveau de preuve L5). Indication d'origine : Rhinite allergique, rhinite vasomotrice, pharyngite, rhume, rhinite…"
---

# Pentoxyverine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Pentoxyvérine : De la rhinite et de la pharyngite à la laryngopharyngite aiguë

## Résumé en Une Phrase

La pentoxyvérine est un médicament sous forme de sirop, initialement utilisé pour traiter des affections des voies respiratoires supérieures (rhinite allergique, rhinite vasomotrice, pharyngite, rhume, rhinopharyngite).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **laryngopharyngite aiguë**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Rhinite allergique, rhinite vasomotrice, pharyngite, rhume, rhinite, rhinopharyngite (selon le graphe de connaissances ; le texte des AMM ne précise pas d'indication) |
| Nouvelle Indication Prédite | Laryngopharyngite aiguë |
| Score de Prédiction TxGNN | 99,59 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Autorisations annulées uniquement |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Aucun lien mécanistique ne peut donc être établi à partir des données compilées pour ce rapport. Un mécanisme propre à la pentoxyvérine (par exemple une activité antitussive ou anticholinergique) n'est pas documenté et devrait être vérifié de manière indépendante.

La laryngopharyngite aiguë est très proche des indications d'origine du médicament (pharyngite, rhume, rhinopharyngite). Il s'agit donc probablement de la redécouverte d'un usage existant plutôt que d'une véritable opportunité de repositionnement. Le score élevé du modèle (99,59 %) reflète cette proximité thématique, mais il ne constitue pas une preuve d'efficacité.

Une seconde prédiction, la **maladie de la cavité nasale** (score 99,57 %), recoupe les indications d'origine (rhinite allergique, rhinite vasomotrice, rhinite). Elle correspond vraisemblablement à une catégorie plus large d'usages existants, et non à une indication distincte. Elle est également sans soutien clinique (niveau L5, Hold).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67025669 | PENTOXYVERINE CLARIX 0,15 % ADULTES | Sirop | Non renseignée (AMM annulée) |
| 67901144 | PENTOXYVERINE CLARIX 0,15 % ENFANTS | Sirop | Non renseignée (AMM annulée) |

Les deux autorisations sont annulées ; aucune AMM valide n'est actuellement recensée.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : hypertension et troubles hypertensifs, bronchopneumopathie chronique obstructive, pancréatite, ulcère gastroduodénal, troubles psychotiques et autres troubles mentaux (schizophréniforme, schizo-affectif), diabète et acidocétose diabétique, hyperplasie bénigne de la prostate, rhabdomyolyse, maladie coronarienne, infarctus du myocarde, thrombose coronaire, athérosclérose, hémoglobinopathie, hypertension oculaire, glaucome à angle fermé, acidose métabolique, arrêt cardiaque soudain, maladie de la conduction cardiaque.
- **Interactions médicamenteuses** : 233 interactions recensées. Les principales, de niveau modéré, concernent des dépresseurs du système nerveux central : opioïdes (morphine, codéine, dihydrocodéine, fentanyl, alfentanil, tramadol, opium), diphénoxylate et difénoxine, benzodiazépines (alprazolam), antihistaminiques sédatifs (prométhazine, chlorphéniramine, phényltoloxamine), cannabinoïdes (dronabinol, nabilone), éthanol, métoclopramide, sibutramine et dichloralphénazone. Le risque principal est une sédation additive.

Les mises en garde et contre-indications de la notice ANSM n'ont pas pu être consultées. Veuillez consulter la notice pour les informations de sécurité officielles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et recoupe très probablement des indications existantes plutôt qu'une nouveauté. Les AMM françaises sont toutes annulées et les données de sécurité officielles sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde et contre-indications), lacune bloquante pour le criblage de sécurité
- Obtenir les données de mécanisme d'action via DrugBank
- Confirmer si la prédiction constitue une réelle nouveauté ou une redécouverte d'indications existantes
- Rechercher des essais cliniques et des publications spécifiques à la laryngopharyngite aiguë
- Clarifier les raisons de l'annulation des AMM et vérifier la compatibilité des voies d'administration
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

