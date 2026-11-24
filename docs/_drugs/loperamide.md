---
layout: default
title: Loperamide
parent: Prédiction du modèle uniquement (L5)
nav_order: 460
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "loperamide"
predicted_indications: ["acute contagious conjunctivitis", "amebic dysentery", "conjunctivitis", "gastroduodenitis", "pseudomembranous conjunctivitis", "chronic follicular conjunctivitis", "conjunctival folliculosis", "serous conjunctivitis except viral", "parasitic conjunctivitis", "Angelucci syndrome"]
description: "Loperamide : nouvelle indication prédite, Acute contagious conjunctivitis (niveau de preuve L5). En France, AMM dans la BDPM : au moins 20"
---

# Loperamide
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

## Loperamide: Acute contagious conjunctivitis
{: .text-alpha }

## Resume en Une Phrase

Le lopéramide est un antidiarrhéique, initialement utilisé pour traiter les maladies diarrhéiques et la dysenterie.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **conjonctivite contagieuse aiguë**, mais cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Predite | Acute contagious conjunctivitis |
| Score de Prediction TxGNN | 0.9997 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 16) |
| Nombre d'AMM | au moins 20 |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Loperamide (traduction non officielle) : « Les études in vitro et chez l'animal montrent que les gélules de chlorhydrate de lopéramide agissent en ralentissant la motilité intestinale et en modifiant les mouvements d'eau et d'électrolytes dans l'intestin. Le lopéramide se lie aux récepteurs opiacés de la paroi intestinale. » Texte original en anglais : "In vitro and animal studies show that loperamide hydrochloride capsules act by slowing intestinal motility and by affecting water and electrolyte movement through the bowel. Loperamide binds to the opiate receptor in the gut wall." ([DailyMed: loperamide hydrochloride prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=74b9893a-18c3-4117-85c2-edab8e7b3b3b), version du 2026-07-09 ; consulté le 2026-11-19). D'après les connaissances pharmacologiques générales, le lopéramide est un agoniste périphérique des récepteurs opioïdes mu, agissant sur les neurones du plexus myentérique de l'intestin pour ralentir le transit et réduire les sécrétions.

Il n'existe **aucun lien mécanistique clair** avec la conjonctivite. Aucune activité oculaire ni anti-infectieuse n'est établie pour le lopéramide. Le score élevé (0,9997) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique ou clinique.

Les autres prédictions du modèle vont dans le même sens : plusieurs entités conjonctivales (conjonctivite, conjonctivite pseudomembraneuse, conjonctivite folliculaire chronique, folliculose conjonctivale, conjonctivite parasitaire, syndrome d'Angelucci) présentent des scores identiques ou très proches, signe de similarités apprises par le modèle TxGNN (apprentissage profond) entre maladies apparentées plutôt que d'une preuve propre à chaque maladie. La seule piste proche de l'indication d'origine est la dysenterie amibienne, mais elle soulève surtout un problème de sécurité (voir ci-dessous).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Litterature

Aucune littérature associée disponible actuellement pour la conjonctivite contagieuse aiguë.

À titre d'information, deux publications concernent la deuxième prédiction (dysenterie amibienne) :

<!-- review:begin fr-lic-20261106-loperamide-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les deux AMM sont annulées : aucune présentation n'est actuellement commercialisée sous ces autorisations. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 2 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-loperamide-1 -->

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/) | 2007 | Rapport de cas | Journal of Travel Medicine | Colite amibienne fulminante chez un patient ayant largement utilisé du lopéramide ; l'évolution a pu être aggravée par le ralentissement du transit |
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Revue | The American Journal of Medicine | Traitements non liquidiens de la diarrhée aiguë ; la réhydratation orale reste la base, les agents symptomatiques peuvent réduire les symptômes |

## Informations de Marche en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 61203061 | IMODIUMCAPS 2 mg, gélule | Gélule | KENVUE FRANCE | Active |
| 60095095 | IMODIUMLIQUICAPS 2 mg, capsule molle | Capsule molle | KENVUE FRANCE | Active |
| 61257269 | LOPERAMIDE ALMUS 2 mg, gélule | Gélule | BIOGARAN | Active |
| 61370480 | LOPERAMIDE BIOGARAN CONSEIL 2 mg, gélule | Gélule | BIOGARAN | Active |
| 61450026 | LOPERAMIDE ARROW LAB 2 mg, gélule | Gélule | ARROW GENERIQUES | Active |
| 61651634 | IMODIUM 2 mg, gélule | Gélule | KENVUE FRANCE | Active |
| 61710577 | LOPERAMIDE LYOC 2 mg, lyophilisat oral | Lyophilisat | TEVA SANTE | Active |
| 62144356 | LOPERAMIDE ZENTIVA CONSEIL 2 mg, gélule | Gélule | ZENTIVA FRANCE | Active |
| 62179122 | LOPERAMIDE TEVA 2 mg, comprimé pelliculé | Comprimé pelliculé | TEVA SANTE | Active |
| 62821961 | LOPERAMIDE ZYDUS FRANCE 2 mg, gélule | Gélule | ZYDUS FRANCE | Active |
| 63029111 | LOPERAMIDE BIOGARAN 2 mg, gélule | Gélule | BIOGARAN | Active |
| 63178870 | LOPERAMIDE VIATRIS 2 mg, gélule | Gélule | VIATRIS SANTE | Active |
| 63276510 | LOPERAMIDE ZYDUS 2 mg, gélule | Gélule | ZYDUS FRANCE | Active |
| 64433231 | LOPERAMIDE VIATRIS CONSEIL 2 mg, lyophilisat oral | Lyophilisat | VIATRIS SANTE | Active |
| 65181566 | LOPERAMIDE ZENTIVA 2 mg, gélule | Gélule | ZENTIVA FRANCE | Active |
| 65272215 | IMODIUMLINGUAL 2 mg, lyophilisat oral | Lyophilisat | KENVUE FRANCE | Active |
| 69522794 | IMODIUM 0,2 mg/ml ENFANTS, solution buvable | Solution buvable | JANSSEN CILAG | Archivée |
| 61303791 | LOPERAMIDE ARROW 2 mg, gélule | Gélule | ARROW GENERIQUES | Abrogée |
| 63088070 | LOPERAMIDE REF 2 mg, gélule | Gélule | BIOGARAN | Archivée |
| 63672883 | INDIARAL 2 mg, gélule | Gélule | GIFRER BARBEZAT | Archivée |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.
Les données ne contiennent qu'une partie des autorisations ; la liste peut être incomplète.

<!-- licenses:end -->

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : maladie hépatique, maladie de la vésicule biliaire, iléus paralytique, occlusion intestinale, myopathie viscérale familiale, dysenterie, maladies diarrhéiques, diarrhées infectieuses, maladies infectieuses intestinales.
- **Interactions médicamenteuses** : 591 interactions répertoriées. Parmi les interactions majeures figurent l'abiratérone, la ranitidine, le fosamprénavir et le gemfibrozil. Les interactions modérées incluent notamment les opioïdes (codéine, dihydrocodéine, tramadol), des antihistaminiques (chlorphéniramine, cétirizine, acrivastine), l'éthanol et le salbutamol.
- **Point d'attention (dysenterie amibienne)** : le ralentissement du transit en cas d'infection invasive peut favoriser une colite fulminante et un mégacôlon toxique.

Les mises en garde détaillées de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Etapes

**Décision : Hold**

**Justification :**
La prédiction pour la conjonctivite aiguë contagieuse repose uniquement sur le score du modèle (niveau L5), sans mécanisme plausible, essai ni publication. Les autres indications prédites sont également non étayées, et la piste la plus proche (dysenterie amibienne) soulève plutôt une alerte de sécurité. De plus, le médicament est commercialisé en France, avec au moins 16 AMM valides.

<!-- review:begin fr-lic-20261124-loperamide-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « avec 1 AMM valide sur 2. » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans le Résumé rapide. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-loperamide-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications), actuellement bloquante pour le criblage de sécurité
- Compléter les données sur le mécanisme d'action (via DrugBank)
- Démontrer une activité oculaire ou anti-infectieuse par des études précliniques avant toute évaluation clinique
- Évaluer la compatibilité de la voie d'administration (les formes existantes sont orales ; une voie ophtalmique serait nécessaire)
- Clarifier le statut réglementaire du produit en France

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Les deux AMM sont annulées : aucune présentation n'est actuellement commercialisée sous ces autorisations » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: loperamide hydrochloride prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=74b9893a-18c3-4117-85c2-edab8e7b3b3b) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

