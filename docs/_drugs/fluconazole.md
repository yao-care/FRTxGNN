---
layout: default
title: Fluconazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 331
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "FLUCONAZOLE"
predicted_indications: ["punctate epithelial keratoconjunctivitis"]
description: "Fluconazole : nouvelle indication prédite, Kératoconjonctivite épithéliale ponctuée (punctate epithelial keratoconjunctivitis) (niveau de preuve L5). Indication d'origine : Non renseignée dans les do…"
---

# Fluconazole
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Fluconazole: Kératoconjonctivite épithéliale ponctuée (punctate epithelial keratoconjunctivitis)
{: .text-alpha }

## Résumé en Une Phrase

Le fluconazole est un antifongique azolé, initialement utilisé pour traiter les candidoses (buccale, vulvovaginale, œsophagienne, candidémie, candidose disséminée) et la méningite à cryptocoque.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **kératoconjonctivite épithéliale ponctuée**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Kératoconjonctivite épithéliale ponctuée (punctate epithelial keratoconjunctivitis) |
| Score de Prédiction TxGNN | 0.9924 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Fluconazole (traduction non officielle) : « Le fluconazole est un inhibiteur hautement sélectif de l'enzyme fongique dépendante du cytochrome P450, la lanostérol 14-α-déméthylase. Cette enzyme a pour fonction de convertir le lanostérol en ergostérol. La perte consécutive des stérols normaux est corrélée à l'accumulation de 14-α-méthylstérols chez les champignons et pourrait être responsable de l'activité fongistatique du fluconazole. » Texte original en anglais : "Fluconazole is a highly selective inhibitor of fungal cytochrome P450 dependent enzyme lanosterol 14-α-demethylase. This enzyme functions to convert lanosterol to ergosterol. The subsequent loss of normal sterols correlates with the accumulation of 14-α-methyl sterols in fungi and may be responsible for the fungistatic activity of fluconazole." ([DailyMed: Diflucan (fluconazole) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f694c617-3383-416c-91b6-b94fda371204), version du 2026-04-02 ; consulté le 2026-11-19). Sur la base des connaissances générales, le fluconazole est un antifongique azolé qui inhibe la lanostérol 14-alpha-déméthylase fongique (CYP51), ce qui perturbe la synthèse de l'ergostérol, composant essentiel de la membrane des champignons. Son efficacité dans les infections à *Candida* et à *Cryptococcus* est établie.

Le seul soutien à la prédiction est le score élevé du modèle (0,9924). Un lien plausible, mais non vérifié, serait que le modèle associe les kératoconjonctivites d'origine fongique ou infectieuse à l'activité antifongique. Or la kératoconjonctivite épithéliale ponctuée est souvent d'origine virale (par exemple adénovirus) ou liée à une atteinte de la surface oculaire ; dans ces situations, un antifongique n'agirait pas sur la cause.

La prédiction ne peut donc pas être considérée comme soutenue sur le plan mécanistique sans preuves supplémentaires. La similarité avec l'indication d'origine reste à évaluer, et la compatibilité des voies d'administration (les formes disponibles sont orales et perfusion, aucune forme ophtalmique) n'a pas été établie.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les 5 premières sont listées ci-dessous (le texte d'indication n'est pas renseigné dans les données).

<!-- review:begin fr-lic-20261106-fluconazole-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les 20 AMM recensées sont toutes annulées. Les 5 premières sont listées ci-dessous (le texte d'indication n'est pas renseigné dans les données). » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-fluconazole-1 -->

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 60560861 | FLUCONAZOLE EVOLUGEN 50 mg, gélule | Gélule | EVOLUPHARM | Active |
| 62033904 | FLUCONAZOLE SANDOZ 200 mg, gélule | Gélule | SANDOZ | Active |
| 63909389 | FLUCONAZOLE VIATRIS 50 mg, gélule | Gélule | VIATRIS SANTE | Active |
| 63206323 | FLUCONAZOLE PFIZER 150 mg, gélule | Gélule | PFIZER HOLDING FRANCE | Active |
| 69903578 | FLUCONAZOLE BIOGARAN 50 mg, gélule | Gélule | BIOGARAN | Active |
| 64080646 | TRIFLUCAN 50 mg, gélule | Gélule | PFIZER HOLDING FRANCE | Active |
| 64053193 | FLUCONAZOLE EVOLUGEN 100 mg, gélule | Gélule | EVOLUPHARM | Active |
| 66015693 | FLUCONAZOLE PFIZER 50 mg, gélule | Gélule | PFIZER HOLDING FRANCE | Active |
| 65826650 | TRIFLUCAN 200 mg, gélule | Gélule | PFIZER HOLDING FRANCE | Active |
| 64967484 | FLUCONAZOLE BIOGARAN 10 mg/ml, poudre pour suspension buvable | Poudre pour suspension buvable | BIOGARAN | Active |
| 62861105 | FLUCONAZOLE ARROW 10 mg/ml, poudre pour suspension buvable | Poudre pour suspension buvable | ARROW GENERIQUES | Active |
| 61530248 | FLUCONAZOLE EG 10 mg/ml, poudre pour suspension buvable | Poudre pour suspension buvable | EG LABO - LABORATOIRES EUROGENERICS | Active |
| 62504459 | FLUCONAZOLE TEVA 50 mg, gélule | Gélule | TEVA SANTE | Active |
| 66318142 | FLUCONAZOLE CRISTERS 100 mg, gélule | Gélule | CRISTERS | Active |
| 63870235 | FLUCONAZOLE ZYDUS 50 mg, gélule | Gélule | ZYDUS FRANCE | Active |
| 62994632 | FLUCONAZOLE KABI 2 mg/ml, solution pour perfusion | Solution pour perfusion | FRESENIUS KABI FRANCE | Active |
| 64940811 | TRIFLUCAN 40 mg/ml, poudre pour suspension buvable | Poudre pour suspension buvable | DIFARMED (ESPAGNE) | Active |
| 65880420 | FLUCONAZOLE PFIZER 200 mg, gélule | Gélule | PFIZER HOLDING FRANCE | Active |
| 61173013 | TRIFLUCAN 100 mg, gélule | Gélule | PFIZER HOLDING FRANCE | Active |
| 66407833 | FLUCONAZOLE TEVA 200 mg, gélule | Gélule | TEVA SANTE | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.
Les données ne contiennent qu'une partie des autorisations ; la liste peut être incomplète.

<!-- licenses:end -->

Les autres formes concernées par des AMM abrogées : poudre pour suspension buvable et gélule.

<!-- review:begin fr-lic-20261115-fluconazole-1 -->

> **Correction de vérification (2026-11-15)**: Texte initial : « Les autres formes concernées par des AMM annulées : poudre pour suspension buvable et solution pour perfusion. » D’après la BDPM complète (CIS_bdpm et CIS_COMPO_bdpm, 2026-11-15), les spécialités contenant FLUCONAZOLE comptent 60 AMM, dont 55 actives et 5 abrogées ou archivées. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_bdpm.txt); [Base de données publique des médicaments (BDPM) – CIS_COMPO_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_COMPO_bdpm.txt).

<!-- review:end fr-lic-20261115-fluconazole-1 -->

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : syndrome du QT long (y compris familial), maladie rénale, pyo-uretère, maladie hépatique, maladie de la vésicule biliaire.
- **Interactions médicamenteuses** (100 interactions recensées ; principales) :
  - **Majeure** : chlorpropamide.
  - **Modérée** : famotidine, rabéprazole, oméprazole, dexlansoprazole, hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, budésonide, lopéramide, aprépitant, bisacodyl, acide picosulfurique, polyéthylène glycol (3350 avec électrolytes), saxagliptine.
  - **Mineure** : amphotéricine B (y compris complexe lipidique), clarithromycine.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication, et le lien mécanistique est peu plausible pour une kératoconjonctivite souvent virale.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice (ANSM) pour permettre l'évaluation de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Rechercher des études cliniques ou précliniques du fluconazole dans la kératoconjonctivite épithéliale ponctuée et préciser l'étiologie ciblée (fongique ou autre).
- Évaluer la voie d'administration adaptée (aucune forme ophtalmique disponible) et la compatibilité avec la pathologie.
- Clarifier le statut réglementaire : le médicament est commercialisé et 20 AMM sont valides.

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Les 20 AMM recensées sont toutes annulées » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-15 | « Les autres formes concernées par des AMM annulées  » → « Les autres formes concernées par des AMM abrogées  » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_bdpm.txt); [Base de données publique des médicaments (BDPM) – CIS_COMPO_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_COMPO_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Diflucan (fluconazole) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f694c617-3383-416c-91b6-b94fda371204) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

