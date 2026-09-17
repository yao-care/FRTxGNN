---
layout: default
title: Sotatercept
parent: Prédiction du modèle uniquement (L5)
nav_order: 284
evidence_level: L5
indication_count: 10
---

# Sotatercept
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

# Sotatercept : D'une Indication d'Origine Non Renseignée à la Leucémie Lymphoblastique Aiguë

## Résumé en Une Phrase

Sotatercept est un piège à ligand du récepteur de l'activine de type IIA-Fc ; aucune indication d'origine ni AMM ne sont actuellement documentées dans les données disponibles pour ce dossier. Le modèle TxGNN le classe en priorité pour la **Leucémie Lymphoblastique Aiguë (LAL)**, mais cette direction n'est soutenue par **aucun essai clinique** ni **aucune publication**, et le lien mécanistique lui-même est qualifié de faible dans l'analyse.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication d'Origine | Non renseignée dans les données actuelles |
| Nouvelle Indication Prédite | Leucémie Lymphoblastique Aiguë (LAL) |
| Score de Prédiction TxGNN | 99,78 % (rang 2117) |
| Niveau de Preuve | L5 (prédiction du modèle seule, aucune étude réelle) |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le mécanisme d'action détaillé de Sotatercept n'est pas disponible dans la fiche produit de ce dossier. D'après les informations rattachées aux hypothèses de repositionnement, Sotatercept agit comme un piège à ligand du récepteur de l'activine de type IIA-Fc (Fc-fusion), un mode d'action qui a été exploré pour moduler la différenciation tardive de l'érythropoïèse — notamment dans des travaux antérieurs sur l'anémie d'origine rénale et la thalassémie.

L'indication d'origine du médicament n'étant pas renseignée dans les données actuelles, il n'est pas possible d'établir de relation documentée entre son usage historique et la LAL. L'hypothèse mécanistique proposée relie la LAL au profil hématologique de Sotatercept par proximité dans l'espace de représentation du modèle (embedding), plutôt que par un mécanisme biologique direct : la prolifération des lymphoblastes malins dans la LAL n'a pas de lien connu avec la modulation de l'activine.

En somme, cette prédiction est explicitement signalée comme mécanistiquement faible : elle reflète probablement un regroupement du modèle autour de pathologies hématologiques plutôt qu'une hypothèse thérapeutique fondée. C'est cette faiblesse qui justifie la recommandation de statu quo (Hold) associée à ce candidat.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le niveau de preuve est L5 : aucun essai clinique ni publication ne soutient la piste LAL, et le lien mécanistique proposé est lui-même qualifié de faible. Le médicament n'est par ailleurs pas commercialisé en France (0 AMM) et l'évaluation de sécurité ne peut pas être initiée en l'état.

**Pour avancer, les éléments suivants sont nécessaires :**
- Extraction du texte des mises en garde et contre-indications à partir du document TFDA déjà identifié (donnée actuellement bloquante pour l'évaluation de sécurité S1)
- Complément du champ mécanisme d'action (MOA) via les données structurées DrugBank
- Recherche documentaire indépendante pour vérifier ou infirmer l'hypothèse mécanistique LAL avant toute progression
- Confirmation du statut réglementaire (le médicament reste non commercialisé en France à ce jour)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

