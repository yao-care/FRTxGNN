---
layout: default
title: Etravirine
parent: Prédiction du modèle uniquement (L5)
nav_order: 310
evidence_level: L5
indication_count: 10
---

# Etravirine
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

# Étravirine : Du VIH/SIDA au Syndrome d'immunodéficience acquise féline

## Résumé en Une Phrase

L'étravirine est un inhibiteur non nucléosidique de la transcriptase inverse (INNTI), initialement utilisé pour traiter l'infection par le VIH et le SIDA.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome d'immunodéficience acquise féline**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection par le VIH, SIDA (les textes d'indication des AMM ne sont pas renseignés ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Syndrome d'immunodéficience acquise féline |
| Score de Prédiction TxGNN | 99,98 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'étravirine fait partie de la classe des INNTI, active contre la transcriptase inverse du VIH-1, et son efficacité dans l'infection par le VIH est établie.

Le virus de l'immunodéficience féline (FIV) est un lentivirus apparenté au VIH, ce qui explique en partie la proximité observée dans le graphe de connaissances. Toutefois, la transcriptase inverse du FIV est généralement peu sensible aux INNTI. Le score élevé reflète donc probablement une similarité de réseau avec le VIH/SIDA plutôt qu'une activité démontrée.

Cette prédiction doit donc être considérée comme une hypothèse de faible plausibilité mécanistique, sans donnée expérimentale pour la soutenir.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour cette indication.

*Pour information, parmi les autres indications prédites, une seule publication indirecte (PMID [26529558](https://pubmed.ncbi.nlm.nih.gov/26529558/), 2015, Molecular Pharmaceutics, étude préclinique sur des combinaisons d'antirétroviraux en nanoparticules) concerne l'infection par le virus de l'immunodéficience simienne. Elle ne documente pas l'effet de l'étravirine chez le chat.*

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66595716 | INTELENCE 25 mg, comprimé | Comprimé | Non renseignée (AMM annulée) |
| 63514730 | INTELENCE 100 mg, comprimé | Comprimé | Non renseignée (AMM annulée) |
| 64044237 | INTELENCE 200 mg, comprimé | Comprimé | Non renseignée (AMM annulée) |

Les trois AMM, détenues par Janssen-Cilag International NV, sont annulées : aucune AMM valide n'est actuellement recensée.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : infection chronique par le virus de l'hépatite C, infection par le virus de l'hépatite C, infection chronique par le virus de l'hépatite B, maladie du système nerveux périphérique, neuropathie périphérique.
- **Interactions médicamenteuses** : 216 interactions recensées. Parmi celles listées, une est de niveau mineur (ranitidine) et les autres de niveau modéré :
  - Inhibiteurs de la pompe à protons et anti-H2 : oméprazole, rabéprazole, cimétidine
  - Corticoïdes : hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone
  - Antidiabétiques : pioglitazone, saxagliptine, linagliptine, glimépiride, chlorpropamide
  - Autres : clarithromycine, métronidazole, aprépitant, dronabinol, éliglustat, naldémédine, naloxégol

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucune donnée clinique ni publication ne soutient cette indication (niveau L5). La plausibilité mécanistique est faible, car la transcriptase inverse du FIV est peu sensible aux INNTI. Les AMM françaises sont toutes annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données in vitro d'activité de l'étravirine sur la transcriptase inverse du FIV et sur des cellules félines infectées
- Données détaillées sur le mécanisme d'action (MOA)
- Texte de la notice de l'ANSM (mises en garde et contre-indications)
- Données de pharmacocinétique et de tolérance chez le chat, ainsi que l'évaluation de la voie d'administration
- Clarification du cadre réglementaire (usage vétérinaire) et de l'intérêt de la prédiction

*Remarque : parmi les autres prédictions, « complexe lié au SIDA » correspond à une indication existante sous une ancienne dénomination. « VIH congénital » (niveau L3, statut « question de recherche ») repose sur une série de cas observationnelle chez des femmes enceintes. Les prédictions relatives aux tumeurs bénignes, à l'hyperlipidémie obsolète et au trouble neurodéveloppemental rare ne présentent aucun lien plausible et semblent être des artefacts du graphe.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

