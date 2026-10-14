---
layout: default
title: Metronidazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 494
evidence_level: L5
indication_count: 10
---

# Metronidazole
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

# Métronidazole : Des infections anaérobies et protozoaires à la pneumocystose

## Résumé en Une Phrase

Le métronidazole est un antibiotique et antiprotozoaire de la famille des nitro-imidazolés, utilisé à l'origine contre les infections à bactéries anaérobies, la giardiase, la vaginose bactérienne et la rosacée (forme topique).
Le modèle TxGNN le prédit comme potentiellement efficace pour la **pneumocystose**, mais **aucun essai clinique** n'est enregistré et la littérature disponible (**10 publications**) est essentiellement composée de revues générales et de cas isolés qui ne démontrent pas d'efficacité du métronidazole dans cette maladie.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Infections à bactéries anaérobies, giardiase, vaginose bactérienne, rosacée (liste issue du graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Predite | Pneumocystose |
| Score de Prediction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 20 (toutes annulées) |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, le métronidazole est un nitro-imidazole actif contre les anaérobies et certains protozoaires (Giardia, Entamoeba, Trichomonas). Son activation dépend de nitroréductases propres aux organismes anaérobies ou microaérophiles.

**Cette prédiction n'apparaît pas plausible sur le plan mécanistique.** *Pneumocystis jirovecii* est un champignon qui ne possède pas cette voie d'activation. Le score élevé du modèle reflète probablement une proximité dans le réseau de connaissances avec des médicaments antiparasitaires et anti-infectieux, et non une relation pharmacologique réelle. Le traitement de référence de la pneumocystose est le triméthoprime-sulfaméthoxazole.

Il faut donc considérer ce résultat comme un artefact probable de la prédiction computationnelle.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Revue | Mayo Clin Proc | Revue générale des antiparasitaires ; pas de données sur le métronidazole dans la pneumocystose |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Revue | Am Fam Physician | Le métronidazole est cité pour l'amibiase et la trichomonase ; la pneumocystose relève du triméthoprime-sulfaméthoxazole |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Revue | Clin Pharmacokinet | Justification pharmacocinétique des traitements antiprotozoaires |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Revue | Clin Pharm | Traitement des complications infectieuses du SIDA |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Revue | Top Antivir Med | Infections opportunistes liées au VIH, vue d'ensemble |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Rapport de cas | Am Rev Respir Dis | Pneumocystose et infection à CMV chez un adulte ayant reçu du métronidazole pour une diarrhée, sans bénéfice sur la pneumocystose |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Rapport de cas | Kansenshogaku Zasshi | Amibiase traitée par métronidazole chez des patients atteints du SIDA, pneumocystose survenue ensuite |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Revue | Rev Infect Dis | Critique des essais de prophylaxie antimicrobienne |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Rapport de cas | J Formos Med Assoc | Perforation colique avec amibiase et CMV chez un patient atteint du SIDA |
| [42178576](https://pubmed.ncbi.nlm.nih.gov/42178576/) | 2026 | Rapport de cas | J Med Case Rep | Abcès cérébelleux à *Streptococcus intermedius* révélant une sarcoïdose |

Ces publications mentionnent le métronidazole dans d'autres contextes ; aucune ne montre un effet sur la pneumocystose.

---

## Informations de Marche en France

Toutes les AMM listées sont annulées ; le texte d'indication approuvée n'est pas renseigné dans les données compilées.

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 67119549 | ROZEX 0,75 %, émulsion pour application cutanée | Émulsion pour application | Non renseignée (AMM annulée) |
| 60647323 | ROZEX 0,75 %, gel | Gel | Non renseignée (AMM annulée) |
| 66962240 | METRONIDAZOLE SUBSTIPHARM 250 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 63815096 | ROZAGEL, gel pour application locale | Gel | Non renseignée (AMM annulée) |
| 66095383 | METRONIDAZOLE B BRAUN 0,5 % | Solution pour perfusion | Non renseignée (AMM annulée) |

Au total, 20 AMM sont recensées (comprimés, gels, crèmes, ovules, suspension buvable, solutions injectables et associations avec la spiramycine), toutes annulées.

---

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique et maladies hépatiques, épilepsie, maladies rénales, maladies hématologiques (neutropénie, agranulocytose, leucopénie), troubles de la coagulation, neuropathie périphérique et maladies du système nerveux, maladies cérébrales, névrite optique et atteintes des voies visuelles, insuffisance cardiaque congestive, diabète et acidocétose diabétique, goutte, maladies de la vésicule biliaire, dermatite, méningite non infectieuse, abus de substances.
- **Interactions médicamenteuses** : 620 interactions recensées. Parmi les exemples, une interaction **majeure** avec l'éthanol (effet de type disulfirame) ; des interactions **modérées** avec le paclitaxel, l'adalimumab, le trastuzumab emtansine, l'éthinylestradiol, l'estradiol, le butalbital, l'amiodarone, le célécoxib, l'amobarbital et le lopéramide ; des interactions mineures avec notamment l'abiratérone, le tramadol, la famotidine, le salbutamol et le propofol.

Les mises en garde et contre-indications issues de la notice française n'ont pas pu être récupérées : veuillez consulter la notice.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5) : aucun essai clinique, pas de lien mécanistique plausible (*Pneumocystis* est un champignon sans voie d'activation du métronidazole), et une littérature sans démonstration d'effet. Un traitement de référence efficace existe déjà.
- Toutes les AMM françaises sont annulées, et les données de sécurité issues de la notice manquent (lacune bloquante).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Démontrer une activité in vitro ou précliniques sur *Pneumocystis*, sans quoi l'indication ne devrait pas être poursuivie

**Autres pistes plus plausibles parmi les prédictions du modèle** (niveau L4, à étudier comme questions de recherche) : la polypose en capuchon (*cap polyposis*, hypothèse anti-inflammatoire/dysbiose) et l'ulcération vulvaire (maladie de Crohn vulvaire, amibiase génitale), ainsi que la rectosigmoïdite ulcéreuse et la myiase (rôle d'appoint seulement).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

