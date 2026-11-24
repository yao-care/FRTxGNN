---
layout: default
title: Verapamil
parent: Prédiction du modèle uniquement (L5)
nav_order: 809
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "verapamil"
predicted_indications: ["obsolete bundle branch block", "malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "periodic paralysis with transient compartment-like syndrome"]
description: "Verapamil : nouvelle indication prédite, Bloc de branche (obsolete bundle branch block) (niveau de preuve L5). En France, AMM dans la BDPM : 16 (valides : 15)"
---

# Verapamil
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Verapamil: Bloc de branche (obsolete bundle branch block)
{: .text-alpha }

> Remarque : la prédiction au rang 1 (« obsolete bundle branch block ») correspond à un terme d'ontologie obsolète et est mécanistiquement douteuse. Le rapport suit néanmoins la prédiction de rang 1 telle que fournie dans les données compilées.

## Résumé en Une Phrase

Le vérapamil est un inhibiteur calcique de type L, initialement utilisé pour l'hypertension, la fibrillation auriculaire, le syndrome coronarien aigu, l'angor de Prinzmetal et la tachycardie ventriculaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **bloc de branche (terme obsolète)**, mais **aucun essai clinique et aucune publication** ne soutiennent cette direction : il s'agit d'une prédiction de modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Bloc de branche (obsolete bundle branch block) |
| Score de Prédiction TxGNN | 0.9962 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 15 sur 16) |
| Nombre d'AMM | 16 (valides : 15) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Verapamil (traduction non officielle) : « Angor : Le mécanisme d'action précis du chlorhydrate de vérapamil en tant qu'agent antiangoreux reste à déterminer entièrement, mais il comprend les deux mécanismes suivants : 1. Relaxation et prévention du spasme des artères coronaires : Le chlorhydrate de vérapamil dilate les principales artères coronaires et les artérioles coronaires, tant dans les régions normales que dans les régions ischémiques, et est un puissant inhibiteur du spasme des artères coronaires, qu'il soit spontané ou induit par l'ergonovine. » Texte original en anglais : "Angina: The precise mechanism of action of verapamil hydrochloride as an antianginal agent remains to be fully determined, but includes the following two mechanisms: 1. Relaxation and prevention of coronary artery spasm: Verapamil hydrochloride dilates the main coronary arteries and coronary arterioles, both in normal and ischemic regions, and is a potent inhibitor of coronary artery spasm, whether spontaneous or ergonovine-induced." ([DailyMed: verapamil hydrochloride prescribing information, Preferred Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c7a54ee0-80c0-4c7e-a6a3-cb60142f860c), version du 2026-10-30 ; consulté le 2026-11-19). D'après les connaissances générales, le vérapamil est un inhibiteur calcique qui ralentit la conduction du nœud auriculo-ventriculaire (AV) et réduit la résistance vasculaire. Son efficacité dans les arythmies supraventriculaires et l'hypertension est établie.

Pour le bloc de branche, le lien est faible. Il s'agit d'un trouble de conduction du système de His-Purkinje, pour lequel le blocage du nœud AV n'offre aucun bénéfice thérapeutique clair et pourrait aggraver la conduction. De plus, le terme « obsolete » indique probablement une entrée d'ontologie dépréciée. La prédiction est donc mécanistiquement douteuse.

Parmi les autres prédictions, la plus plausible est l'**hypertension rénale maligne** (rang 2, score 0,9927) et l'**hypertension rénovasculaire maligne** (rang 3) : elles prolongent l'usage antihypertenseur connu, mais sans preuve directe. Les prédictions suivantes (hypertension pulmonaire, syndrome de Braddock, paralysie périodique) sont spéculatives ; pour l'hypertension pulmonaire, l'effet inotrope négatif du vérapamil constitue en outre une préoccupation de sécurité.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'indication de rang 1.

Pour information, les publications retrouvées pour les indications de rang inférieur ne fournissent pas non plus de preuve clinique d'efficacité du vérapamil. Pour l'hypertension rénovasculaire maligne (rang 3), il s'agit d'une revue sur le rapport aldostérone/rénine (2012) et d'un rapport de cas pédiatrique (1999), sans lien avec le vérapamil. Pour l'hypertension pulmonaire hypoxique (rang 4), la littérature est essentiellement hors sujet ou préclinique.

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 69181930 | VERAPAMIL EG L.P. 240 mg, comprimé pelliculé sécable à libération prolongée | Comprimé pelliculé sécable à libération prolongée | EG LABO - LABORATOIRES EUROGENERICS | Active |
| 69865024 | ISOPTINE 40 mg, comprimé enrobé | Comprimé enrobé | VIATRIS MEDICAL | Active |
| 63803877 | ISOPTINE L.P. 240 mg, comprimé pelliculé sécable à libération prolongée | Comprimé pelliculé sécable à libération prolongée | VIATRIS MEDICAL | Active |
| 60614889 | ISOPTINE 5 mg/2 ml, solution injectable | Solution injectable | VIATRIS MEDICAL | Active |
| 66814925 | ISOPTINE 120 mg, gélule | Gélule | VIATRIS MEDICAL | Active |
| 60628554 | VERAPAMIL BIOGARAN L.P. 240 mg, gélule à libération prolongée | Gélule à libération prolongée | BIOGARAN | Active |
| 62607039 | VERAPAMIL TEVA 40 mg, comprimé pelliculé | Comprimé pelliculé | TEVA SANTE | Active |
| 62901254 | VERAPAMIL TEVA 120 mg, comprimé pelliculé | Comprimé pelliculé | TEVA SANTE | Active |
| 67429380 | VERAPAMIL SANDOZ 120 mg, comprimé pelliculé | Comprimé pelliculé | SANDOZ | Active |
| 68325609 | VERAPAMIL VIATRIS 120 mg, gélule | Gélule | VIATRIS SANTE | Active |
| 69166273 | VERAPAMIL VIATRIS LP 240 mg, comprimé pelliculé sécable à libération prolongée | Comprimé pelliculé sécable à libération prolongée | VIATRIS SANTE | Active |
| 69548383 | VERAPAMIL TEVA L. P. 240 mg, gélule à liberation prolongée | Gélule à libération prolongée | TEVA SANTE | Active |
| 60516982 | TARKA LP 240 mg/4 mg, comprimé pelliculé à libération prolongée | Comprimé pelliculé à libération prolongée | VIATRIS MEDICAL | Active |
| 62404028 | TARKA LP 180 mg/2 mg, comprimé pelliculé à libération prolongée | Comprimé pelliculé à libération prolongée | VIATRIS MEDICAL | Active |
| 64603331 | TARKA LP 240 mg/2 mg, comprimé pelliculé à libération prolongée | Comprimé pelliculé à libération prolongée | VIATRIS MEDICAL | Active |
| 61377350 | VERAPAMIL MYLAN L.P. 240 mg, comprimé pelliculé sécable à libération prolongée | Comprimé pelliculé sécable à libération prolongée | MYLAN SAS | Abrogée |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance cardiaque, bloc auriculo-ventriculaire, sténose aortique, cardiomyopathie hypertrophique, trouble hypotensif, tachycardie ventriculaire, myasthénie grave, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, angio-œdème (dont héréditaire), neutropénie et agranulocytose, sténose de l'artère rénale, entre autres.
- **Interactions médicamenteuses** : 328 interactions recensées. Parmi celles affichées, la plus sévère est avec le **lopéramide (majeure)**. Les interactions modérées concernent notamment la cimétidine, la clarithromycine, la metformine, le bupropion, l'aprépitant, l'acide acétylsalicylique, les corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), la canagliflozine et plusieurs sels de calcium. L'interaction avec la morphine est mineure.

Les mises en garde et contre-indications de la notice ne sont pas disponibles : veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication. Le mécanisme est douteux (le bloc de branche est un trouble de conduction infranodal, et le terme est obsolète). Le vérapamil reste par ailleurs commercialisé en France (statut des AMM : voir l'Aperçu rapide).

<!-- review:begin fr-lic-20261106-verapamil-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Le vérapamil n'a par ailleurs plus d'AMM valide en France (5 AMM annulées). » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans l'Aperçu rapide. Les nombres d'AMM écrits en dur dans le texte corrigé sont retirés. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261106-verapamil-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Vérifier la validité du terme d'ontologie et envisager de privilégier les prédictions plus plausibles (hypertension maligne avec atteinte rénale)
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Récupérer les mises en garde et contre-indications de la notice (site de l'ANSM), étape bloquante pour le dépistage de sécurité
- Rechercher des études cliniques ou observationnelles spécifiques au vérapamil dans l'indication retenue
- Clarifier le statut réglementaire : le médicament est commercialisé, avec des AMM valides (statut des AMM : voir l'Aperçu rapide)

<!-- review:begin fr-lic-20261124-verapamil-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « avec 5 AMM valides sur 5 » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans l'Aperçu rapide. Les nombres d'AMM écrits en dur dans le texte corrigé sont retirés : le nombre et le statut à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché, générés à partir des données BDPM. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-verapamil-1 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-24 | Supprimé : « (5 AMM annulées) » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: verapamil hydrochloride prescribing information, Preferred Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c7a54ee0-80c0-4c7e-a6a3-cb60142f860c) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

