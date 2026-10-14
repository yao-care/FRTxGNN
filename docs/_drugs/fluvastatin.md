---
layout: default
title: Fluvastatin
parent: Prédiction du modèle uniquement (L5)
nav_order: 343
evidence_level: L5
indication_count: 10
---

# Fluvastatin
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

# Fluvastatine : De l'athérosclérose à l'hypercholestérolémie familiale

## Résumé en Une Phrase

La fluvastatine est une statine (inhibiteur de l'HMG-CoA réductase), initialement utilisée pour traiter l'athérosclérose et les hyperlipidémies familiales combinées.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hypercholestérolémie familiale**, avec **1 essai clinique de Phase 3 directement pertinent** (sur 4 essais listés) et **21 publications** soutenant actuellement cette direction.
Cette indication recoupe fortement l'usage d'origine du médicament : il s'agit d'une indication de même classe, et non d'un repositionnement véritablement nouveau.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Athérosclérose, hyperlipidémie familiale combinée (d'après le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Hypercholestérolémie familiale |
| Score de Prédiction TxGNN | 99,89 % |
| Niveau de Preuve | L1 (selon le dossier ; un seul essai de Phase 3 fluvastatine terminé est identifié, ce qui relève plutôt de L2 par application stricte des règles) |
| Statut de Marché en France | ✗ Toutes les AMM sont annulées |
| Nombre d'AMM | 15 (toutes annulées) |
| Décision Recommandée | Proceed with Guardrails |

> Remarque : parmi les 10 indications prédites, l'hypercholestérolémie familiale est celle qui dispose des preuves les plus solides. Les autres candidates (hyperlipoprotéinémie, hypercholestérolémie familiale homozygote, infection par le VIH, etc.) sont soit sans preuve directe, soit de niveau L3 à L5.

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées. Sur la base des connaissances pharmacologiques établies, la fluvastatine appartient à la classe des statines : elle inhibe l'HMG-CoA réductase, réduit la synthèse hépatique du cholestérol et favorise l'expression des récepteurs hépatiques du LDL, ce qui abaisse le LDL-cholestérol.

Les indications d'origine (athérosclérose, hyperlipidémies familiales combinées) relèvent du même domaine : le métabolisme lipidique et la prévention cardiovasculaire. Dans l'hypercholestérolémie familiale hétérozygote, la fonction résiduelle des récepteurs du LDL permet à une statine d'agir par le même mécanisme. La prédiction est donc cohérente, mais elle correspond à un usage dans le champ thérapeutique natif du médicament.

À l'inverse, dans la forme homozygote, l'activité des récepteurs du LDL est quasi nulle : la réponse aux statines est limitée et le mécanisme n'est que partiellement applicable.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00171236](https://clinicaltrials.gov/study/NCT00171236) | Phase 3 | Terminé | 84 | Efficacité et sécurité de la fluvastatine chez des enfants atteints d'hypercholestérolémie familiale hétérozygote : preuve directe |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Phase 3 | Terminé | 153 | Alirocumab versus placebo chez l'enfant et l'adolescent avec HF hétérozygote (ne teste pas la fluvastatine) |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Terminé | 18 | Alirocumab en ouvert dans l'HF homozygote pédiatrique (ne teste pas la fluvastatine) |
| [NCT01890967](https://clinicaltrials.gov/study/NCT01890967) | Phase 2 | Terminé | 527 | Étude de détermination de dose de LY3015014 (anticorps anti-PCSK9) dans l'hypercholestérolémie primaire (ne teste pas la fluvastatine) |

Seul NCT00171236 apporte une preuve directe pour la fluvastatine. Les trois autres essais portent sur d'autres molécules et ne servent que de contexte pour la maladie.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [8157036](https://pubmed.ncbi.nlm.nih.gov/8157036/) | 1993 | Étude en double aveugle | Eur J Clin Pharmacol | Efficacité et sécurité de la fluvastatine à haute dose chez 52 patients avec HF |
| [17062478](https://pubmed.ncbi.nlm.nih.gov/17062478/) | 2006 | Essai clinique | Acta Paediatr | Fluvastatine chez l'enfant et l'adolescent avec HF hétérozygote : profils lipidiques et modifications vasculaires |
| [8192170](https://pubmed.ncbi.nlm.nih.gov/8192170/) | 1994 | Essai comparatif | Am J Med | Fluvastatine + bézafibrate comparée à fluvastatine + cholestyramine dans l'HF hétérozygote |
| [7604807](https://pubmed.ncbi.nlm.nih.gov/7604807/) | 1995 | Étude ouverte | Am J Cardiol | Trithérapie fluvastatine-bézafibrate-cholestyramine dans l'HF sévère (22 patients) |
| [7604804](https://pubmed.ncbi.nlm.nih.gov/7604804/) | 1995 | Étude ouverte | Am J Cardiol | Fluvastatine à forte dose avec bézafibrate dans l'HF hétérozygote |
| [8198022](https://pubmed.ncbi.nlm.nih.gov/8198022/) | 1994 | Cohorte | Am J Cardiol | Réponse à la fluvastatine en association dans l'HF |
| [8462179](https://pubmed.ncbi.nlm.nih.gov/8462179/) | 1993 | Étude génétique | Circulation | Déterminants génétiques de la réponse à la fluvastatine dans l'HF hétérozygote |
| [16002074](https://pubmed.ncbi.nlm.nih.gov/16002074/) | 2006 | Étude génétique | Atherosclerosis | Polymorphismes de CETP et MDR1 et réponse lipidique à la fluvastatine dans l'HF |
| [7604789](https://pubmed.ncbi.nlm.nih.gov/7604789/) | 1995 | Étude clinique | Am J Cardiol | Effets de la fluvastatine sur le profil lipidique chez 31 patients chinois hypercholestérolémiques (dont 6 avec HF) |
| [8875971](https://pubmed.ncbi.nlm.nih.gov/8875971/) | 1996 | Revue | Am J Cardiol | Revue des données cliniques sur la fluvastatine |

Aucun essai randomisé de grande envergure ni méta-analyse récente n'est présent. La littérature est ancienne (années 1990 et 2000) et comprend de nombreuses études ouvertes de petite taille.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60852004 | LESCOL L.P. 80 mg | Comprimé pelliculé à libération prolongée | Non renseignée (AMM annulée) |
| 66946962 | FLUVASTATINE BIOGARAN 40 mg | Gélule | Non renseignée (AMM annulée) |
| 66605982 | FLUVASTATINE CEVIDRA 20 mg | Gélule | Non renseignée (AMM annulée) |
| 68067589 | FLUVASTATINE SANDOZ LP 80 mg | Comprimé pelliculé à libération prolongée | Non renseignée (AMM annulée) |
| 62756595 | FLUVASTATINE SANDOZ 20 mg | Gélule | Non renseignée (AMM annulée) |

Au total, 15 AMM sont recensées, toutes annulées : aucune spécialité à base de fluvastatine n'est actuellement autorisée en France selon les données compilées.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie hépatique, maladie de la vésicule biliaire, myopathie, maladies musculaires, rhabdomyolyse, paralysie périodique familiale, troubles hypotenseurs, abus ou dépendance à des substances, fasciite nodulaire, traumatisme.
- **Interactions médicamenteuses** : 159 interactions recensées. Parmi les principales de niveau modéré : rosuvastatine, simvastatine, aprépitant, métronidazole, tinidazole, naltrexone, natéglinide, nitisinone, oxandrolone, glibenclamide, pectine. Plusieurs autres (acide acétylsalicylique, cimétidine, famotidine, pantoprazole, doxycycline, calcitriol, etc.) sont de niveau non déterminé.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- L'hypercholestérolémie familiale (forme hétérozygote) est soutenue par un essai de Phase 3 terminé avec la fluvastatine et par de nombreuses études cliniques, mais il s'agit d'une indication dans le champ natif du médicament, et non d'un repositionnement nouveau. La fluvastatine est moins puissante que les statines récentes et aucune AMM n'est actuellement valide en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications officielles de la notice (ANSM), actuellement manquantes (point bloquant pour le criblage de sécurité)
- Obtenir les données détaillées sur le mécanisme d'action
- Examiner les 159 interactions médicamenteuses, notamment avec les autres statines
- Examiner les résultats publiés de NCT00171236
- Clarifier le statut réglementaire (AMM annulées) et la pertinence d'une fluvastatine par rapport aux alternatives disponibles
- Pour les autres prédictions (VIH, HF homozygote, etc.), considérées au stade « Hold » ou « Research Question », prévoir des études spécifiques avant toute évaluation
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

