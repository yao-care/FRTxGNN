---
layout: default
title: Amsacrine
parent: Prédiction du modèle uniquement (L5)
nav_order: 38
evidence_level: L5
indication_count: 5
---

# Amsacrine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

# Amsacrine : De l'Indication Non Renseignée à l'Hyperthyroïdie (Prédiction Non Étayée)

## Résumé en Une Phrase

L'amsacrine est un antinéoplasique cytotoxique (intercalant de l'ADN et inhibiteur de la topoisomérase II), commercialisé en France sous le nom AMSALYO. Le texte de son indication approuvée n'est pas renseigné dans les données ANSM fournies.
Le modèle TxGNN prédit en première position l'**hyperthyroïdie** (score de 99,37 %), mais **aucun essai clinique et aucune publication** ne soutiennent cette piste. Elle ressemble à un artefact du graphe de connaissances.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM (texte d'indication vide) |
| Nouvelle Indication Prédite | Hyperthyroïdie |
| Score de Prédiction TxGNN | 99,37 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. On sait que l'amsacrine agit comme agent intercalant de l'ADN et inhibiteur de la topoisomérase II, avec une action cytotoxique sur les cellules en prolifération.

**Pour l'hyperthyroïdie, le lien est jugé non plausible.** Ce mécanisme n'a aucun effet connu sur la synthèse ou la signalisation des hormones thyroïdiennes. Le score élevé (0,994) provient d'une proximité dans le graphe de connaissances, sans essai ni littérature à l'appui. Il faut le traiter comme un artefact du modèle, pas comme un signal thérapeutique.

Parmi les cinq prédictions du dossier, seule une a un fondement mécanistique plausible et des données humaines : le **myélome plasmocytaire** (voir ci-dessous).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour l'hyperthyroïdie (ni dans ClinicalTrials.gov ni dans ICTRP). Aucun essai n'est non plus enregistré pour les autres indications prédites.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'hyperthyroïdie.

Les seules publications du dossier concernent la 2e prédiction, le **myélome plasmocytaire** (score 99,32 %, niveau L3, recommandation « Research Question ») :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [2913481](https://pubmed.ncbi.nlm.nih.gov/2913481/) | 1989 | Essai de phase II (myélome) | Med Pediatr Oncol | 74 patients déjà traités, 120 mg/m² toutes les 3 semaines : bonne réponse chez 2 (3 %), amélioration chez 3 (4 %), toxicité sévère chez 33 % des patients ayant reçu ≥3 cures. Schéma jugé généralement inefficace. |
| [6688199](https://pubmed.ncbi.nlm.nih.gov/6688199/) | 1983 | Essai de phase II (tumeurs solides, myélome, lymphome) | Cancer Treat Rep | 12 réponses partielles chez 221 patients évaluables (120 mg/m² IV toutes les 28 jours), activité antitumorale limitée. |
| [2064323](https://pubmed.ncbi.nlm.nih.gov/2064323/) | 1991 | Revue (leucémies, focus m-AMSA) | Anticancer Res | Panorama des nouveaux cytostatiques dans les leucémies. |
| [1958848](https://pubmed.ncbi.nlm.nih.gov/1958848/) | 1991 | Étude in vitro | Anti-Cancer Drugs | Comparaison de la cytotoxicité sur cellules cardiaques et cellules de myélome 8226 pour des intercalants de l'ADN (contexte de cardiotoxicité). |
| [2419036](https://pubmed.ncbi.nlm.nih.gov/2419036/) | 1985 | Revue (test de clonage tumoral) | Curr Probl Cancer | Contexte ex vivo, pas de résumé disponible. |
| [3910194](https://pubmed.ncbi.nlm.nih.gov/3910194/) | 1985 | Revue (corrélations cliniques du test de clonage) | Cancer Invest | Contexte ex vivo, pas de résumé disponible. |

La publication PMID 17133426 (bortézomib et zona, 2007) porte sur un autre médicament et n'est pas pertinente pour l'amsacrine.

Les données humaines sont anciennes et plutôt décevantes, et aucune n'est un essai randomisé de phase 2/3. Elles ne satisfont donc pas la définition du niveau L2.

Les autres prédictions (myélome indolent, résistance aux hormones thyroïdiennes par mutation de THRB, bronchite) sont toutes au niveau L5, sans essai ni publication, et toutes classées « Hold ».

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67581349 | AMSALYO 75 mg, poudre pour solution pour perfusion | Poudre pour solution pour perfusion | Non renseignée |

Titulaire : EUROCEPT INTERNATIONAL (Pays-Bas).

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (intercalant de l'ADN, inhibiteur de la topoisomérase II) |
| Risque de Myélosuppression | Élevé (myélosuppression signalée dans l'évaluation du dossier) |
| Classification d'Émétogénicité | Non documentée dans le dossier ; veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | NFS avec différentielle, fonction cardiaque (cardiotoxicité signalée), fonction hépatique et rénale, électrolytes |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'hyperthyroïdie n'a ni fondement mécanistique ni essai ni publication. Le score TxGNN de 99,37 % reflète très probablement un artefact du graphe. Le profil de toxicité de l'amsacrine (myélosuppression, cardiotoxicité) rend de toute façon le rapport bénéfice/risque défavorable pour une pathologie thyroïdienne.
- La seule piste défendable du dossier est le myélome plasmocytaire. Ses données de phase II sont anciennes et peu encourageantes, et elle est à replacer face aux traitements actuels (inhibiteurs du protéasome, IMiD, anti-CD38). Elle relève d'une question de recherche, pas d'un repositionnement à engager.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde, contre-indications) : lacune bloquante pour le criblage de sécurité.
- Compléter le mécanisme d'action et l'indication originale via DrugBank.
- Pour le myélome, réévaluer les résultats historiques (taux de réponse, schémas) avant toute décision.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement nécessite une validation clinique.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

