---
layout: default
title: Benzydamine
parent: Prédiction du modèle uniquement (L5)
nav_order: 53
evidence_level: L5
indication_count: 1
---

# Benzydamine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

Le skill txgnn-pipeline couvre la gestion du pipeline — la génération du rapport suit le format du prompt système. Je génère directement le rapport :

---

# Benzydamine : D'Anti-inflammatoire Local à l'Hyperplasie Bénigne de la Prostate

## Résumé en Une Phrase

Benzydamine est un anti-inflammatoire non stéroïdien (AINS) à usage local, doté d'une activité anesthésique topique, principalement utilisé dans le traitement des inflammations oro-pharyngées.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Hyperplasie Bénigne de la Prostate (HBP)**,
avec **0 essai clinique** et **0 publication** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Anti-inflammatoire local (usage oro-pharyngé) |
| Nouvelle Indication Prédite | Hyperplasie Bénigne de la Prostate (HBP) |
| Score de Prédiction TxGNN | 99,26% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action de Benzydamine ne sont pas disponibles dans ce dossier. Sur la base des informations pharmacologiques connues, Benzydamine est un AINS atypique dont le profil inclut l'inhibition de la COX, la modulation du TNF-α et un effet stabilisateur membranaire, ce qui le distingue des AINS classiques.

La biologie de l'HBP présente une composante inflammatoire tissulaire non négligeable : une inflammation histologique est observable dans 43 à 100 % des pièces de prostatectomie issues de patients HBP. C'est sur cette intersection que le modèle TxGNN pourrait avoir établi une association entre le nœud médicamenteux de Benzydamine et le nœud pathologique de l'HBP dans le graphe de connaissances biomédicales.

Cependant, cette connexion reste hautement spéculative. Les cibles thérapeutiques validées dans l'HBP sont la voie androgénique (inhibiteurs de la 5α-réductase), les récepteurs α1-adrénergiques et les inhibiteurs de la PDE5 — mécanismes qui sont distincts du profil anti-inflammatoire de Benzydamine. De plus, aucune donnée pharmacocinétique ne documente la pénétration tissulaire prostatique de ce composé, ce qui constitue une lacune critique pour évaluer la pertinence clinique de cette prédiction.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Benzydamine ne dispose d'aucune autorisation de mise sur le marché (AMM) en France. Aucune donnée réglementaire disponible.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
L'absence totale de preuves cliniques et de littérature publiée sur l'association Benzydamine–HBP, combinée à l'absence d'AMM en France et à des lacunes critiques sur le mécanisme d'action et la pharmacocinétique prostatique, ne permet pas de recommander une avancée à ce stade. La prédiction TxGNN repose uniquement sur la similarité structurelle du graphe de connaissances (L5), sans validation expérimentale ou clinique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de mécanisme d'action (MOA) détaillées issues de DrugBank ou de la littérature primaire
- Données pharmacocinétiques documentant la biodisponibilité systémique et la pénétration tissulaire prostatique
- Au moins une étude préclinique (in vitro ou in vivo) sur un modèle d'HBP pour élever le niveau de preuve de L5 à L4
- Profil de sécurité complet (avertissements, contre-indications, interactions médicamenteuses) avant toute évaluation clinique
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

