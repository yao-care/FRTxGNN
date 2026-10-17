---
layout: default
title: Lansoprazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 436
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Lansoprazole : nouvelle indication prédite, Reflux duodéno-gastrique (niveau de preuve L5). Indication d'origine : Ulcère gastrique, ulcère peptique, reflux gastro-œsophagien…"
monitor_inn: "LANSOPRAZOLE"
predicted_indications: ["duodenal obstruction"]
---

# Lansoprazole
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

# Lansoprazole : Du Reflux Gastro-Œsophagien au Reflux Duodéno-Gastrique

## Résumé en Une Phrase

Lansoprazole est un inhibiteur de la pompe à protons (IPP), initialement utilisé pour traiter les ulcères gastriques et duodénaux, le reflux gastro-œsophagien et l'œsophagite.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **reflux duodéno-gastrique**, mais **aucun essai clinique** n'est enregistré et **une seule publication** (une revue générale sur les IPP, non spécifique à cette indication) est disponible : la prédiction repose pour l'instant uniquement sur le modèle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Ulcère gastrique, ulcère peptique, reflux gastro-œsophagien, œsophagite, ulcère duodénal, syndrome de Zollinger-Ellison (source : graphe de connaissances, les textes d'indication des AMM sont vides) |
| Nouvelle Indication Prédite | Reflux duodéno-gastrique |
| Score de Prédiction TxGNN | 99,69 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement ; aucune étude spécifique à l'indication) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le lansoprazole fait partie de la classe des inhibiteurs de la pompe à protons, qui suppriment la sécrétion d'acide gastrique. Son efficacité dans le reflux gastro-œsophagien, l'œsophagite et les ulcères est établie, et il pourrait mécanistiquement soulager les lésions muqueuses liées au reflux.

Le reflux duodéno-gastrique (reflux biliaire) est proche des indications d'origine : la suppression acide peut atténuer les symptômes et les lésions de la muqueuse. Cependant, les IPP ne corrigent pas la cause sous-jacente (dysfonction pylorique, troubles de la motilité), de sorte que le lien mécanistique n'est qu'indirect.

Le score TxGNN très élevé (0,997) reflète probablement la proximité dans le réseau avec les indications liées à l'acidité, plutôt qu'une preuve indépendante. Cette prédiction doit donc être considérée comme une question de recherche.

La seconde prédiction du modèle, l'**obstruction duodénale** (score 99,68 %), n'est pas retenue : il s'agit d'une affection mécanique ou structurelle nécessitant une intervention endoscopique ou chirurgicale, sans lien mécanistique clair, sans essai ni publication à l'appui.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Revue | Eur J Clin Pharmacol | Mise à jour sur l'usage clinique et la pharmacocinétique des IPP, traitement de première intention de l'ulcère peptique, de l'infection à *H. pylori*, du RGO, des lésions liées aux AINS et du syndrome de Zollinger-Ellison. Ne traite pas spécifiquement du reflux duodéno-gastrique. |

---

## Informations de Marché en France

Les 20 AMM recensées sont toutes annulées ; aucune n'est actuellement valide. Les textes d'indication approuvée ne sont pas renseignés. Principales AMM (5 sur 20) :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69499833 | Lansoprazole Cristers 15 mg | Gélule gastro-résistante | Non renseignée (annulée) |
| 67240910 | Lansoprazole EG 30 mg | Comprimé orodispersible | Non renseignée (annulée) |
| 62911490 | Lansoprazole Arrow Lab 30 mg | Gélule gastro-résistante | Non renseignée (annulée) |
| 68088245 | Ogastoro 30 mg (Takeda France) | Comprimé orodispersible | Non renseignée (annulée) |
| 61527857 | Ogast 15 mg (Takeda France) | Gélule gastro-résistante | Non renseignée (annulée) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie du graphe, et non texte de la notice) : hypertension, syndrome du QT long et torsades de pointes, insuffisance hépatique et maladies hépatiques, porphyries, maladie rénale, insuffisance cardiaque congestive, ostéoporose (dont postménopausique), infarctus du myocarde, accident vasculaire cérébral et infarctus cérébral, troubles de la coagulation, anémies et hémoglobinopathies, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, myasthénie, abus/dépendance à des substances, maladie de la vésicule biliaire. Ces éléments sont à interpréter avec prudence et à confirmer avec la notice officielle.
- **Interactions médicamenteuses** : 100 interactions recensées ; parmi celles listées, deux sont de niveau **majeur** : **acalabrutinib** et **atazanavir**. Plusieurs interactions de niveau modéré concernent notamment l'atorvastatine, le fénofibrate, l'apalutamide, l'aprépitant, le bosutinib, le brigatinib, la bromocriptine, l'amphétamine, l'hydrochlorothiazide, l'amikacine, l'ampicilline et l'amphotéricine B. Des interactions mineures concernent l'acide acétylsalicylique, l'axitinib, le brivaracétam et la cyanocobalamine.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5) : aucun essai clinique et aucune publication spécifique au reflux duodéno-gastrique. Le lien mécanistique n'est qu'indirect, et toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications officielles de la notice (ANSM), indispensables avant tout examen de sécurité
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Une revue de la littérature ciblée sur les IPP dans le reflux biliaire/duodéno-gastrique
- Des études cliniques ou observationnelles spécifiques à cette indication
- La clarification de la situation réglementaire (AMM toutes annulées) et de la disponibilité du produit en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

