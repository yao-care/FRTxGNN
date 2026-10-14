---
layout: default
title: Ritonavir
parent: Preuves modérées (L3-L4)
nav_order: 674
evidence_level: L4
indication_count: 3
---

# Ritonavir
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **3** 
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

# Ritonavir : Du VIH/SIDA à l'infection par le virus de l'immunodéficience simienne

## Résumé en Une Phrase

Ritonavir est un inhibiteur de protéase, initialement utilisé pour le traitement de l'infection par le VIH/SIDA et de l'hépatite C.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infection par le virus de l'immunodéficience simienne (VIS)**,
mais **aucun essai clinique** n'est enregistré et seules **10 publications** (essentiellement précliniques ou in vitro) sont associées à cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection par le VIH / SIDA ; hépatite C chronique (d'après le graphe de connaissances ; le texte d'indication des AMM n'est pas disponible) |
| Nouvelle Indication Prédite | Infection par le virus de l'immunodéficience simienne |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Toutes les AMM sont annulées |
| Nombre d'AMM | 10 (dont 0 valide) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances pharmacologiques établies, le ritonavir inhibe la protéase aspartyle virale, ce qui bloque le clivage de la polyprotéine Gag-Pol et la production de virions matures. Il inhibe aussi le CYP3A4, d'où son usage comme « booster » pharmacocinétique d'autres inhibiteurs de protéase.

Le VIS est un lentivirus étroitement apparenté au VIH, et sa protéase est une cible plausible du ritonavir. Une étude in vitro (PMID 12709355) montre que le VIS (souche mac239) est inhibé par le ritonavir avec une concentration efficace à 50 % d'environ 13 nM, contre environ 25 nM pour le VIH-1.

Il faut toutefois relativiser : le VIS est un modèle de recherche du VIH chez le primate et non une indication clinique humaine. Il n'existe donc pas de voie de développement clinique chez l'humain. Le score élevé du modèle reflète probablement l'activité anti-VIH connue du ritonavir et sa proximité avec les indications d'origine, et non un signal de repositionnement indépendant.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro | Antimicrob Agents Chemother | Le VIS mac239 est inhibé par l'indinavir, le saquinavir et le ritonavir (CE50 du ritonavir : 13 nM contre 25 nM pour le VIH-1) |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro | Antivir Ther | Évaluation de l'activité de 16 antiviraux contre le VIH-2, le VIS et le SHIV |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Préclinique (macaque) | J Virol | Décroissance virale rapide chez des macaques infectés par le VIS sous quadrithérapie antirétrovirale |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Préclinique (macaque) | PLoS Pathog | Un traitement antirétroviral très intensifié induit une suppression virale durable et limite le réservoir viral dans un modèle de SIDA simien |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Préclinique (macaque) | PLoS One | Effets d'une cART suppressive associée au SAHA chez des macaques rhésus infectés par le VIS |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Préclinique (macaque) | J Virol Methods | Effet d'un traitement oral par AZT, 3TC et lopinavir/ritonavir sur les lymphocytes CD8 chez des macaques infectés par le SHIV 89.6P |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Non classé | Microbes Infect | Construction d'un SHIV portant la protéase du VIH-1, outil pour tester in vivo les inhibiteurs de protéase |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Revue | mBio | Les lentivirus persistent dans le cerveau malgré un traitement antirétroviral efficace |

Les données sont indirectes et proviennent de modèles animaux ou d'études in vitro ; aucune étude humaine n'est disponible.

## Informations de Marché en France

Toutes les AMM listées sont annulées ; aucune n'est actuellement valide. Le texte des indications approuvées n'est pas disponible.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 65102533 | NORVIR 100 mg, poudre pour suspension buvable | Poudre pour suspension buvable | Annulée |
| 62148415 | RITONAVIR ARROW 100 mg | Comprimé pelliculé | Annulée |
| 67851855 | NORVIR 100 mg | Comprimé pelliculé | Annulée |
| 61578339 | RITONAVIR VIATRIS 100 mg | Comprimé pelliculé | Annulée |
| 65579730 | PAXLOVID 150 mg + 100 mg | Comprimé pelliculé | Annulée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : syndrome du QT long (y compris familial), torsades de pointes, arrêt cardiaque soudain, maladies de la conduction cardiaque, bloc atrioventriculaire, cardiomyopathies, ischémie myocardique, maladie coronarienne, pancréatite, maladie hépatique et cirrhose, maladie de la vésicule biliaire, hyperglycémie, diabète et acidocétose diabétique, hépatite B chronique, hypertriglycéridémie et hyperlipidémies, hyperbilirubinémie (dont syndrome de Gilbert), goutte et hyperuricémie, carence en potassium, hémophilie.
- **Interactions médicamenteuses** : 100 interactions recensées, dont plusieurs de niveau **majeur** parmi les exemples disponibles : lopéramide, triamcinolone et budésonide. De nombreuses interactions de niveau modéré sont aussi rapportées (par exemple metformine, acarbose, alogliptine, dexaméthasone, hydrocortisone, clarithromycine, métronidazole, bupropion, aprépitant).

Les mises en garde et contre-indications issues des notices ANSM ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'indication prédite est un modèle animal de recherche et non une maladie humaine ; les preuves sont indirectes (in vitro et macaques) et il n'existe aucun essai clinique. Le score élevé du modèle ne constitue pas un signal de repositionnement indépendant. Par ailleurs, toutes les AMM françaises sont annulées et les données de sécurité de la notice sont manquantes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (DrugBank)
- Notices ANSM (mises en garde et contre-indications) pour l'évaluation de sécurité
- Définition d'une finalité réaliste (par exemple usage comme modèle de recherche préclinique) plutôt qu'un développement clinique humain
- Vérification du statut réglementaire actuel du ritonavir en France, compte tenu de l'annulation de toutes les AMM

Les deux autres prédictions de rang inférieur (SIDA félin et un trouble neurodéveloppemental rare avec ataxie) reposent uniquement sur le modèle (niveau L5), sans essai ni publication, et ne présentent pas de lien mécanistique plausible avec la pharmacologie connue du ritonavir ; elles restent en **Hold**.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

