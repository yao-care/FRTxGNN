---
layout: default
title: Fosamprenavir
parent: Prédiction du modèle uniquement (L5)
nav_order: 347
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-20
monitor_inn: "fosamprenavir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "breast fibrocystic disease", "apocrine adenosis of breast", "blunt duct adenosis of breast", "benign mammary dysplasia"]
description: "Fosamprenavir : nouvelle indication prédite, Syndrome d'immunodéficience acquise féline (feline acquired immunodeficiency syndrome) (niveau de preuve L5). Indication d'origine : Non renseignée dans l…"
---

# Fosamprenavir
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

## Fosamprenavir: Syndrome d'immunodéficience acquise féline (feline acquired immunodeficiency syndrome)
{: .text-alpha }

## Résumé en Une Phrase

Le fosamprénavir est une prodrogue de l'amprénavir, un inhibiteur de la protéase du VIH-1, initialement utilisé pour le traitement de l'infection par le VIH et du SIDA.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome d'immunodéficience acquise féline** (FIV), mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Syndrome d'immunodéficience acquise féline (feline acquired immunodeficiency syndrome) |
| Score de Prédiction TxGNN | 0.9988 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé (aucune autorisation enregistrée) |
| Nombre d'AMM | 0 (valides : 0) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon les rubriques « Mechanism of Action » et « Microbiology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Fosamprenavir (traduction non officielle) : « Le fosamprénavir est un agent antirétroviral anti-VIH-1. […] Le fosamprénavir est une prodrogue qui est rapidement hydrolysée en amprénavir par les phosphatases cellulaires de l'épithélium intestinal au cours de son absorption. L'amprénavir est un inhibiteur de la protéase du VIH-1. L'amprénavir se lie au site actif de la protéase du VIH-1 et empêche ainsi la maturation des précurseurs polyprotéiques viraux Gag et Gag-Pol, ce qui entraîne la formation de particules virales immatures non infectieuses. » Texte original en anglais : "Fosamprenavir is an HIV-1 antiretroviral agent. […] Fosamprenavir is a prodrug that is rapidly hydrolyzed to amprenavir by cellular phosphatases in the gut epithelium as it is absorbed. Amprenavir is an inhibitor of HIV-1 protease. Amprenavir binds to the active site of HIV-1 protease and thereby prevents the processing of viral Gag and Gag-Pol polyprotein precursors, resulting in the formation of immature non-infectious viral particles." ([DailyMed: fosamprenavir calcium prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5cd1eead-9fc1-426c-bee8-214ffa7d9dc1), version du 2026-06-30 ; consulté le 2026-11-19). Sur la base des connaissances générales, le fosamprénavir est la prodrogue de l'amprénavir, un inhibiteur de la protéase du VIH-1. Son efficacité dans l'infection par le VIH est établie, et il pourrait être mécanistiquement applicable à d'autres lentivirus.

Le virus de l'immunodéficience féline (FIV) est un lentivirus apparenté au VIH, et sa protéase présente une similarité structurale avec celle du VIH-1. Cela fournit un argument mécanistique de départ. Toutefois, la protéase du FIV diffère de celle du VIH-1 par sa spécificité de substrat et sa sensibilité aux inhibiteurs, et les inhibiteurs de la classe de l'amprénavir sont connus pour y être moins efficaces.

Il s'agit essentiellement d'une reformulation de l'indication anti-VIH d'origine dans un contexte vétérinaire, de valeur limitée comme opportunité de repositionnement chez l'humain.

### Autres prédictions du modèle

| Rang | Maladie prédite | Score TxGNN | Niveau de preuve | Commentaire |
|------|------|------|------|------|
| 2 | Infection par le virus de l'immunodéficience simienne (VIS) | 0,9988 | L5 | Lentivirus de primates très proche du VIH ; plausible mécanistiquement, mais surtout utile en recherche préclinique (modèle macaque) |
| 3 | Trouble neurodéveloppemental avec démarche ataxique, absence de parole et diminution de la substance blanche corticale | 0,9986 | L5 | Aucun lien mécanistique identifié ; pénétration cérébrale faible |
| 4 | Maladie fibrokystique du sein | 0,9957 | L5 | Aucun lien mécanistique établi |
| 6 | Adénose à canaux dilatés du sein | 0,9934 | L5 | Score identique au précédent : signal lié à l'ontologie, non au médicament |
| 7 | Dysplasie mammaire bénigne | 0,9910 | L5 | Terme proche de la maladie fibrokystique ; même regroupement ontologique |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées. Les éléments suivants proviennent du graphe de connaissances et des bases d'interactions.

- **Contre-indications issues du graphe de connaissances** (à confirmer avec la notice officielle) : hypertension, maladie hépatique, maladie de la vésicule biliaire, hyperglycémie, diabète, acidocétose diabétique, hépatite C chronique, hépatite B chronique, hypertriglycéridémie, coronaropathie, obésité, infarctus du myocarde, thrombose coronarienne, hémoglobinopathie, néphrolithiase, néphropathie urique aiguë, anémie hémolytique, hémophilie, lipodystrophie.
- **Interactions médicamenteuses** : 231 interactions répertoriées. Parmi celles listées :
  - **Majeure** : budésonide.
  - **Modérée** : acarbose, famotidine, ranitidine, rabéprazole, hydrocortisone, albiglutide, alogliptine, alosétron, aprépitant, bétaméthasone, budésonide (nasal), canagliflozine, chlorpropamide, cimétidine, dapagliflozine, dexaméthasone (ophtalmique), dexlansoprazole, dulaglutide.
  - **Mineure** : clarithromycine.

Pour les informations de sécurité complètes, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Toutes les indications prédites reposent uniquement sur des scores computationnels, sans essai clinique ni publication. Pour la première, le lien mécanistique est indirect et la protéase du FIV est moins sensible à cette classe d'inhibiteurs. Les autres prédictions (troubles neurodéveloppementaux, pathologies bénignes du sein) n'ont pas de fondement mécanistique identifié.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice ANSM (mises en garde et contre-indications) : lacune bloquante pour tout passage à l'évaluation de sécurité
- Données détaillées sur le mécanisme d'action (MOA), à obtenir via DrugBank
- Données précliniques d'activité de l'amprénavir sur la protéase du FIV/VIS, si l'on souhaite poursuivre ces pistes
- Confirmation de la pertinence d'un usage vétérinaire ou préclinique, car ces indications offrent peu de valeur pour un repositionnement chez l'humain
- Définition d'une hypothèse biologique explicite avant toute exploration des indications neurodéveloppementale et mammaires

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: fosamprenavir calcium prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5cd1eead-9fc1-426c-bee8-214ffa7d9dc1) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

