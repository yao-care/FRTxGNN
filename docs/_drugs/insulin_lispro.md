---
layout: default
title: Insulin Lispro
parent: Prédiction du modèle uniquement (L5)
nav_order: 404
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "insulin lispro"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
description: "Insulin Lispro : nouvelle indication prédite, Ovarite auto-immune (autoimmune oophoritis) (niveau de preuve L5). En France, AMM dans la BDPM : 13 (valides : 13)"
---

# Insulin Lispro
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

## Insulin Lispro: Ovarite auto-immune (autoimmune oophoritis)
{: .text-alpha }

## Résumé en Une Phrase

L'insuline lispro est un analogue de l'insuline à action rapide, initialement utilisé pour le traitement du diabète de type 1 et de type 2 ainsi que de l'acidocétose diabétique.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**ovarite auto-immune**, mais cette prédiction repose uniquement sur le calcul : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Ovarite auto-immune (autoimmune oophoritis) |
| Score de Prédiction TxGNN | 0.9978 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 13 sur 13) |
| Nombre d'AMM | 13 (valides : 13) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Insulin Lispro (traduction non officielle) : « La régulation du métabolisme du glucose est l'activité principale des insulines et des analogues de l'insuline, y compris les produits à base d'insuline lispro. Les insulines abaissent la glycémie en stimulant la captation périphérique du glucose par le muscle squelettique et le tissu adipeux, et en inhibant la production hépatique de glucose. » Texte original en anglais : "Regulation of glucose metabolism is the primary activity of insulins and insulin analogs, including insulin lispro products. Insulins lower blood glucose by stimulating peripheral glucose uptake by skeletal muscle and fat, and by inhibiting hepatic glucose production." ([DailyMed: Admelog (insulin lispro) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12ec9e3f-e2ac-43a1-b334-8b6538cf2bb0), version du 2026-09-03 ; consulté le 2026-11-19). Sur la base des informations connues, l'insuline lispro est un analogue de l'insuline humaine. Son efficacité dans le diabète est établie : elle remplace ou complète l'insuline endogène pour contrôler la glycémie.

Le lien avec l'ovarite auto-immune est probablement indirect. Cette maladie coexiste souvent avec les syndromes polyendocriniens auto-immuns, dont fait partie le diabète de type 1. Le score du modèle TxGNN (deep learning) peut donc refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique : il traduit plus vraisemblablement une **co-occurrence de maladies** qu'un effet thérapeutique. On ne s'attend pas à ce que l'insuline traite le processus auto-immun ovarien lui-même.

**Autres prédictions du modèle (toutes de niveau L5, sauf mention contraire, décision Hold) :**

| Maladie prédite | Score TxGNN | Interprétation |
|------|------|------|
| Syndrome de dysfonctionnement répondant à la thiamine | 0,9937 | Prise en charge symptomatique du diabète associé ; le traitement principal est la thiamine |
| Syndrome de l'homme raide classique | 0,9936 | Probable comorbidité avec le diabète de type 1 (auto-immunité anti-GAD65) |
| Syndrome du membre raide focal | 0,9936 | Même explication que ci-dessus |
| Opsismodysplasie | 0,9934 | Lien hypothétique via INPPL1 (SHIP2), régulateur de la voie insuline/PI3K |
| Lipodystrophie localisée d'origine médicamenteuse | 0,9909 | Probable effet indésirable connu des injections d'insuline, donc probable faux positif |
| Agénésie pancréatique | 0,9909 | Substitution hormonale rationnelle (niveau L4), mais ce n'est pas un vrai repositionnement |
| Lipodystrophie centrifuge | 0,9904 | Aucun mécanisme clair |
| Lipoatrophie localisée induite par la pression | 0,9903 | Non étayée ; l'insuline est aussi associée à la lipoatrophie au site d'injection |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'ovarite auto-immune.

Pour information, une seule publication a été identifiée pour une autre prédiction (agénésie pancréatique) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Revue | J Am Pharm Assoc | Revue générale de l'insulinothérapie dans le diabète de type 2 et de sa mise en place pratique ; preuve indirecte uniquement |

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 69727429 | LYUMJEV 100 unités/mL, solution injectable en flacon | Solution injectable | ELI LILLY NEDERLAND BV (PAY-BAS) | Active |
| 66817088 | LYUMJEV 100 unités/mL, solution injectable en cartouche | Solution injectable | ELI LILLY NEDERLAND BV (PAY-BAS) | Active |
| 66537912 | HUMALOG 100 unités/ml JUNIOR KWIKPEN solution injectable en stylo pré-rempli | Solution injectable | ELI LILLY NEDERLAND BV (PAY-BAS) | Active |
| 67759549 | HUMALOG 200 UI/ml KWIKPEN, solution injectable en stylo prérempli | Solution injectable | ELI LILLY NEDERLAND BV (PAY-BAS) | Active |
| 62000441 | LYUMJEV 100 unités/mL, Junior KwikPen solution injectable en stylo prérempli | Solution injectable | ELI LILLY NEDERLAND BV (PAY-BAS) | Active |
| 66599764 | LYUMJEV 200 unités/mL, KwikPen solution injectable en stylo prérempli | Solution injectable | ELI LILLY NEDERLAND BV (PAY-BAS) | Active |
| 61650831 | HUMALOG MIX50 100 UI/ml, suspension injectable en cartouche | Suspension injectable | ELI LILLY NEDERLAND BV (PAY-BAS) | Active |
| 61872223 | HUMALOG MIX25 100 UI/ml KWIKPEN, suspension injectable | Suspension injectable | ELI LILLY NEDERLAND BV (PAY-BAS) | Active |
| 64052173 | HUMALOG 100 UI/ml, solution injectable en cartouche | Solution injectable | ELI LILLY NEDERLAND BV (PAY-BAS) | Active |
| 65132156 | HUMALOG 100 UI/ml KWIKPEN, solution injectable | Solution injectable | ELI LILLY NEDERLAND BV (PAY-BAS) | Active |
| 65228400 | HUMALOG 100 UI/ml, solution injectable en flacon | Solution injectable | ELI LILLY NEDERLAND BV (PAY-BAS) | Active |
| 66081056 | HUMALOG MIX50 100 UI/ml KWIKPEN, suspension injectable | Suspension injectable | ELI LILLY NEDERLAND BV (PAY-BAS) | Active |
| 69304169 | HUMALOG MIX25 100 UI/ml, suspension injectable en cartouche | Suspension injectable | ELI LILLY NEDERLAND BV (PAY-BAS) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

Les 13 AMM (HUMALOG, LYUMJEV) sont détenues par ELI LILLY NEDERLAND BV.

<!-- review:begin fr-lic-20261106-insulin_lispro-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Une sixième AMM (66599764, LYUMJEV 200 unités/mL KwikPen) est également annulée. Les six AMM sont détenues par ELI LILLY NEDERLAND BV. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 6 AMM pour ce médicament, dont 6 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans le Résumé rapide. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261106-insulin_lispro-1 -->

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 352 interactions sont recensées. Celles affichées dans les données compilées sont surtout de niveau modéré :
  - Agents hyperglycémiants ou antagonisant l'effet de l'insuline : corticoïdes (hydrocortisone), œstrogènes et progestatifs (estradiol, éthinylestradiol, lévonorgestrel), diurétiques thiazidiques (hydrochlorothiazide), acétazolamide
  - Sympathomimétiques et bêta-agonistes : épinéphrine, phényléphrine, pseudoéphédrine, salbutamol, formotérol
  - Autres antidiabétiques (risque d'effet additif et d'hypoglycémie) : metformine, alogliptine, albiglutide
  - Autres : acébutolol (bêtabloquant pouvant masquer les signes d'hypoglycémie), doxycycline, alpélisib, éthanol
  - Les corticoïdes topiques (hydrocortisone, alclométasone) sont de niveau mineur.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les prédictions reposent uniquement sur le modèle (niveau L5) : aucun essai clinique ni publication ne les soutient. Elles reflètent surtout des comorbidités avec le diabète ou des effets indésirables connus (lipodystrophie), et non un effet thérapeutique.
- Les 13 AMM françaises sur 13 sont valides (médicament commercialisé), mais les données de sécurité de la notice manquent, ce qui bloque l'évaluation de sécurité.

<!-- review:begin fr-lic-20261124-insulin_lispro-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Les 6 AMM françaises sur 6 sont valides » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans le Résumé rapide. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-insulin_lispro-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Téléchargement et analyse des notices ANSM (mises en garde, contre-indications)
- Données sur le mécanisme d'action issues de DrugBank
- Recherche ciblée de littérature et d'essais pour l'ovarite auto-immune, en vérifiant si le signal vient d'une simple comorbidité
- Pour l'agénésie pancréatique, des données spécifiques à l'insuline lispro (cette indication relève d'une substitution hormonale et non d'un repositionnement)
- Vérification de la situation réglementaire actuelle et de la compatibilité de voie d'administration

<!-- review:begin fr-lic-20261106-insulin_lispro-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Vérification de la situation réglementaire actuelle (raisons de l'annulation des AMM) et de la compatibilité de voie d'administration » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 6 AMM pour ce médicament, dont 6 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-insulin_lispro-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-24 | Supprimé : « Une sixième AMM (66599764, LYUMJEV 200 unités/mL KwikPen) est également annulée » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |
| 2026-11-06 | Supprimé : « (raisons de l'annulation des AMM) » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Admelog (insulin lispro) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12ec9e3f-e2ac-43a1-b334-8b6538cf2bb0) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

