---
layout: default
title: Nicorandil
parent: Preuves modérées (L3-L4)
nav_order: 535
evidence_level: L4
indication_count: 7
---

# Nicorandil
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **7** 
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

# Nicorandil : De l'angor chronique stable à l'hyperplasie bénigne de la prostate

## Résumé en Une Phrase

Nicorandil est un vasodilatateur ouvreur des canaux potassiques ATP-dépendants et donneur de monoxyde d'azote, utilisé à l'origine dans le traitement de l'angor chronique stable.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hyperplasie bénigne de la prostate (HBP)**, mais **aucun essai clinique** n'est enregistré et seules **3 publications** (revues et étude animale) soutiennent actuellement cette piste.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Angor chronique stable (d'après les données pharmacologiques ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Hyperplasie bénigne de la prostate |
| Score de Prédiction TxGNN | 99,71 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées (aucune AMM valide) |
| Nombre d'AMM | 14 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les informations pharmacologiques connues, le nicorandil ouvre les canaux potassiques sensibles à l'ATP (sous-unités Kir6.1 et Kir6.2) et libère du monoxyde d'azote, ce qui entraîne une vasodilatation. Son efficacité dans l'angor chronique stable repose sur cet effet vasculaire.

L'hypothèse avancée dans la littérature est qu'une ischémie prostatique et une baisse du flux sanguin de la prostate contribuent à l'HBP et aux symptômes du bas appareil urinaire (SBAU). Dans un modèle de rat spontanément hypertendu, l'ischémie prostatique a induit une hyperplasie de la prostate ventrale, et le nicorandil, traité pendant six semaines, a été étudié comme vasodilatateur susceptible d'améliorer la perfusion prostatique.

Ce raisonnement est plausible mais reste au stade de l'hypothèse et de l'étude préclinique. Le score TxGNN, très élevé, est une prédiction informatique et ne remplace pas une validation clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [24448152](https://pubmed.ncbi.nlm.nih.gov/24448152/) | 2014 | Étude animale (rat SHR) | Scientific Reports | L'ischémie prostatique induit une hyperplasie de la prostate ventrale chez le rat hypertendu ; le nicorandil a été administré pendant six semaines pour évaluer le flux sanguin prostatique et les marqueurs de stress oxydatif |
| [31735753](https://pubmed.ncbi.nlm.nih.gov/31735753/) | 2019 | Revue | Nihon Yakurigaku Zasshi | Le flux sanguin prostatique comme cible dans l'HBP ; l'altération de l'apport sanguin du bas appareil urinaire pourrait favoriser l'HBP, avec une association avec les maladies athéroscléreuses |
| [26165338](https://pubmed.ncbi.nlm.nih.gov/26165338/) | 2015 | Revue | Nihon Yakurigaku Zasshi | Les SBAU vus comme un dysfonctionnement vasculaire ; effet du nicorandil comme vasodilatateur (résumé non disponible) |

## Informations de Marché en France

Toutes les AMM listées ci-dessous sont annulées ; le texte de l'indication approuvée n'est pas renseigné dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 64614712 | NICORANDIL EG 10 mg | Comprimé sécable | Annulée |
| 66925249 | NICORANDIL ALMUS 10 mg | Comprimé sécable | Annulée |
| 61503831 | NICORANDIL ZENTIVA 10 mg | Comprimé sécable | Annulée |
| 61630825 | NICORANDIL SANDOZ 10 mg | Comprimé sécable | Annulée |
| 61786176 | IKOREL 20 mg | Comprimé | Annulée |

Au total, 14 AMM figurent dans les données (toutes en monothérapie et toutes annulées).

## Considérations de Sécurité

**Interactions et pharmacologie :** les données compilées signalent uniquement une activité sur les canaux potassiques Kir6.1 et Kir6.2, qui correspond au mécanisme pharmacologique du médicament et non à une interaction médicamenteuse cliniquement documentée.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'hypothèse repose uniquement sur une étude animale et deux revues, sans aucun essai clinique, et le médicament ne dispose plus d'aucune AMM valide en France. Le niveau de preuve (L4) ne permet pas d'aller plus loin pour l'instant.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (donnée bloquante pour le criblage de sécurité)
- Les données détaillées sur le mécanisme d'action
- Des données cliniques chez l'humain sur la perfusion prostatique ou les SBAU
- Une clarification de la raison de l'annulation des AMM et de la faisabilité d'une remise sur le marché

## Autres Indications Prédites (pour information)

Les autres prédictions n'ont aucune preuve clinique ni bibliographique dans les données compilées ; elles sont toutes de niveau L5 avec une recommandation Hold.

| Indication Prédite | Score TxGNN | Remarque |
|------|------|------|
| Alopécie | 99,61 % | Lien hypothétique avec les ouvreurs de canaux K-ATP (type minoxidil), non étayé |
| Hypotrichose simple du cuir chevelu | 99,51 % | Maladie génétique rare, justification faible |
| Hypotrichose congénitale avec milium | 99,51 % | Probable proximité dans le graphe de connaissances, mécanisme spéculatif |
| Pelade diffuse | 99,48 % | Maladie auto-immune, mécanisme du nicorandil non adapté |
| Susceptibilité à l'arthrose | 99,44 % | Aucun lien mécanistique identifiable |
| Arthrose | 99,40 % | Lien spéculatif via les canaux K-ATP ou le NO, non étayé |
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

