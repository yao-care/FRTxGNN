---
layout: default
title: Simoctocog Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 705
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
monitor_inn: "SIMOCTOCOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "fetal and neonatal alloimmune thrombocytopenia", "thrombotic thrombocytopenic purpura"]
description: "Simoctocog Alfa : nouvelle indication prédite, Pseudo-maladie de von Willebrand (pseudo-von Willebrand disease) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Simoctocog Alfa
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

## Simoctocog Alfa: Pseudo-maladie de von Willebrand (pseudo-von Willebrand disease)
{: .text-alpha }

## Résumé en Une Phrase

Simoctocog alfa est un facteur VIII de coagulation humain recombinant (délété du domaine B), initialement utilisé dans le traitement de l'hémophilie.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **pseudo-maladie de von Willebrand**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Pseudo-maladie de von Willebrand (pseudo-von Willebrand disease) |
| Score de Prédiction TxGNN | 1.0000 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 8 sur 8) |
| Nombre d'AMM | 8 (valides : 8) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, simoctocog alfa est un facteur VIII recombinant. Son efficacité dans l'hémophilie A repose sur le remplacement du facteur VIII déficient.

**En réalité, la prédiction est peu plausible sur le plan mécanistique.** La pseudo-maladie de von Willebrand est un trouble plaquettaire causé par un gain de fonction de la GPIb-alpha, qui augmente la liaison au facteur de von Willebrand (VWF). Un apport de facteur VIII ne corrige pas ce défaut du récepteur plaquettaire. Le score élevé provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées (troubles hémorragiques), et non une preuve biologique.

### Autres indications prédites

Les neuf autres prédictions du modèle ne disposent pas non plus d'essais ni de publications :

| Rang | Maladie prédite | Score TxGNN | Niveau | Évaluation |
|---|---|---|---|---|
| 2 | Trouble de la libération plaquettaire primaire | 1,0000 | L5 | Défaut de sécrétion plaquettaire, indépendant du FVIII |
| 3 | Thrombasthénie de Glanzmann | 1,0000 | L5 | Défaut de l'intégrine αIIbβ3 ; traitement standard : transfusion plaquettaire ou FVIIa recombinant |
| 4 | Syndrome de Scott | 0,9997 | L5 | Lien théorique lointain (FVIII, cofacteur de la ténase), mais la surface phospholipidique manquante n'est pas restaurée |
| 5 | Déficit acquis en facteur de coagulation | 0,9995 | L5 | Lien le plus plausible (ex. hémophilie A acquise), mais les inhibiteurs neutraliseraient le produit ; les agents de contournement sont la norme |
| 6 | Diathèse hémorragique par défaut d'un récepteur du collagène | 0,9992 | L5 | Sans rapport avec le FVIII |
| 7 | Syndrome hémorragique par thrombopénie constitutionnelle | 0,9992 | L5 | Le FVIII ne corrige ni le nombre ni la fonction des plaquettes |
| 8 | Thrombopénie alloimmune fœtale et néonatale | 0,9984 | L5 | Mécanisme immunitaire ; prise en charge par IgIV, corticoïdes, transfusion plaquettaire |
| 10 | Purpura thrombotique thrombocytopénique | 0,9972 | L5 | Déficit en ADAMTS13 ; risque théorique d'aggravation de l'état prothrombotique |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66102792 | NUWIQ 1000 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 69144152 | NUWIQ 4000 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 63023286 | NUWIQ 250 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 63383804 | NUWIQ 1500 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 67351693 | NUWIQ 500 UI | Poudre et solvant pour solution injectable | Non renseignée |

Trois autres AMM actives existent (NUWIQ 2500, 3000 et 2000 UI) et ne sont pas détaillées ici.

<!-- review:begin fr-lic-20261106-simoctocog_alfa-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les 8 AMM, toutes de la gamme NUWIQ (Octapharma, Suède), sont annulées. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 8 AMM pour ce médicament, dont 8 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-simoctocog_alfa-1 -->

<!-- review:begin fr-lic-20261112-simoctocog_alfa-1 -->

> **Correction de vérification (2026-11-12)**: Texte initial : « Trois autres AMM annulées existent » D'après la BDPM (données du 2026-11-09), les 8 AMM de simoctocog alfa (gamme NUWIQ) sont toutes actives. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261112-simoctocog_alfa-1 -->

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées pour ce rapport. Une préoccupation théorique est toutefois soulevée pour le purpura thrombotique thrombocytopénique : l'apport de FVIII pourrait aggraver l'état prothrombotique, le FVIII élevé étant un facteur de risque thrombotique.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les dix indications prédites reposent uniquement sur le modèle (niveau L5, sauf une en L4), sans essai ni publication, et la plupart relèvent de défauts plaquettaires ou immunitaires sans lien mécanistique avec le FVIII.
- Le médicament est commercialisé en France : 8 AMM valides sur 8. Les données de sécurité de la notice sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération de la notice (mises en garde et contre-indications) sur le site de l'ANSM, étape bloquante pour le criblage de sécurité
- Données sur le mécanisme d'action depuis DrugBank
- Revue de la littérature et des registres d'essais pour les indications prédites
- Si une piste est poursuivie, priorité à l'hémophilie A acquise (rang 5) et à l'hémophilie A avec anomalie vasculaire (rang 9), comme questions de recherche et non comme candidats au repositionnement

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Les 8 AMM, toutes de la gamme NUWIQ (Octapharma, Suède), sont annulées » | Corrigé (révisé le 2026-11-12 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-12 | Les 3 autres AMM NUWIQ sont actives, non annulées | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

