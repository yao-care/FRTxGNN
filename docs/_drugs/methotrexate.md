---
layout: default
title: Methotrexate
parent: Prédiction du modèle uniquement (L5)
nav_order: 487
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
monitor_inn: "methotrexate"
predicted_indications: ["pulmonary blastoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "Hodgkins lymphoma", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
description: "Methotrexate : nouvelle indication prédite, Pulmonary blastoma (niveau de preuve L5). En France, AMM dans la BDPM : au moins 20"
---

# Methotrexate
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

## Methotrexate: Pulmonary blastoma
{: .text-alpha }

## Résumé en Une Phrase

Le méthotrexate est un antimétabolite (antifolate) utilisé à l'origine dans la leucémie aiguë lymphoblastique, les lymphomes, la polyarthrite rhumatoïde et le psoriasis.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **blastome pulmonaire** (score le plus élevé), mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette prédiction.
Parmi les 10 indications prédites, seules quelques-unes disposent de données réelles (notamment le lymphome de Hodgkin et le rhabdomyosarcome), qui restent indirectes.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Pulmonary blastoma |
| Score de Prédiction TxGNN | 0.9945 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Methotrexate (traduction non officielle) : « Le méthotrexate inhibe la dihydrofolate réductase. Les dihydrofolates doivent être réduits en tétrahydrofolates par cette enzyme avant de pouvoir être utilisés comme transporteurs de groupements monocarbonés dans la synthèse des nucléotides puriques et du thymidylate. » Texte original en anglais : "Methotrexate inhibits dihydrofolic acid reductase. Dihydrofolates must be reduced to tetrahydrofolates by this enzyme before they can be utilized as carriers of one-carbon groups in the synthesis of purine nucleotides and thymidylate." ([DailyMed: Jylamvo (methotrexate) prescribing information, SHORLA ONCOLOGY INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=96e931f5-51ae-4bdf-a441-bb0dd26d4c0e), version du 2026-11-05 ; consulté le 2026-11-19). Sur la base des informations connues, le méthotrexate est un antifolate : il inhibe la dihydrofolate réductase et freine la synthèse de l'ADN dans les cellules à division rapide. Son efficacité est établie dans les hémopathies lymphoïdes (leucémie lymphoblastique aiguë, lymphome non hodgkinien).

Le blastome pulmonaire est une tumeur embryonnaire rare et agressive du poumon. Une activité antiprolifératice est plausible, mais rien dans les données compilées ne la démontre. La prédiction reflète probablement une proximité dans le réseau de connaissances (tumeurs de type embryonnaire) plutôt qu'une sensibilité aux antifolates démontrée.

Les indications suivantes du classement sont mieux étayées, sans être concluantes :
- **Rhabdomyosarcome** (L2) : un essai de phase 2 de méthotrexate à haute dose chez des enfants à haut risque (PMID 9329466) existe, mais sa population exacte n'est pas confirmée et le méthotrexate ne fait pas partie des protocoles standards.
- **Lymphome de Hodgkin** (L3) : le schéma historique VBM (vinblastine, bléomycine, méthotrexate) a donné de bons taux de rémission dans les stades précoces (PMID 21592816), mais n'est plus un standard.
- **Lymphome pulmonaire primitif** (L4) : le méthotrexate à haute dose est central dans les lymphomes du SNC, mais aucune donnée spécifique au poumon n'a été identifiée.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour le blastome pulmonaire.

À titre informatif, voici les essais les plus pertinents pour les autres indications prédites :

| Numéro d'Essai | Indication | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|------|---------|
| [NCT03520842](https://clinicaltrials.gov/study/NCT03520842) | Cancer du poumon (CBNPC) | Phase 2 | Terminé | 22 | Régorafénib + méthotrexate oral dans le CBNPC avec mutation KRAS (petit échantillon, pas de cancer à petites cellules) |
| [NCT05663866](https://clinicaltrials.gov/study/NCT05663866) | Cancer du poumon (CBNPC) | Phase 2 | Actif, non en recrutement | 68 | Méthotrexate sous-cutané pour prévenir les réactions à la perfusion d'amivantamab (usage de support) |
| [NCT00290498](https://clinicaltrials.gov/study/NCT00290498) | Lymphome (Hodgkin, rang 5) | Phase 2 | Terminé | 67 | R-HCVAD alterné avec rituximab-méthotrexate-cytarabine vs R-CHOP dans les lymphomes B agressifs |
| [NCT01399372](https://clinicaltrials.gov/study/NCT01399372) | Lymphome (Hodgkin, rang 5) | Phase 2 | Terminé | 91 | Rituximab, méthotrexate, procarbazine, vincristine, cytarabine ± radiothérapie cérébrale dans le lymphome primitif du SNC |
| [NCT03206671](https://clinicaltrials.gov/study/NCT03206671) | Lymphome (Hodgkin, rang 5) | Phase 3 | Actif, non en recrutement | 650 | Protocole B-NHL 2013 : rôle du rituximab dans les lymphomes B agressifs de l'enfant (non-Hodgkinien, pas Hodgkin) |

La plupart des essais liés au lymphome de Hodgkin concernent des lymphomes non hodgkiniens ou la prophylaxie de la maladie du greffon contre l'hôte, où le méthotrexate n'est pas l'agent antitumoral pour le Hodgkin.

---

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement pour le blastome pulmonaire.

Publications les plus pertinentes pour les autres indications prédites :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [9329466](https://pubmed.ncbi.nlm.nih.gov/9329466/) | 1997 | Essai de phase 2 | J Pediatr Hematol Oncol | Méthotrexate à haute dose chez des enfants non traités atteints de rhabdomyosarcome à haut risque |
| [21592816](https://pubmed.ncbi.nlm.nih.gov/21592816/) | 2012 | Revue | Crit Rev Oncol Hematol | Schéma VBM + radiothérapie dans le Hodgkin précoce : rémission complète de 94 à 100 %, toxicité pulmonaire dans les premiers essais |
| [8384659](https://pubmed.ncbi.nlm.nih.gov/8384659/) | 1993 | ECR | J Chemother | CEV-M vs CAV dans le cancer bronchique à petites cellules : taux de réponse de 75 % (stade limité) vs 61 % |
| [24282143](https://pubmed.ncbi.nlm.nih.gov/24282143/) | 2013 | Revue systématique | Cochrane Database Syst Rev | Chimiothérapie vs meilleurs soins de support dans le cancer à petites cellules étendu |
| [11244328](https://pubmed.ncbi.nlm.nih.gov/11244328/) | 2001 | Étude clinique | Oncology | Méthotrexate à haute dose + vincristine + procarbazine puis radiothérapie dans le lymphome primitif du SNC |
| [14635074](https://pubmed.ncbi.nlm.nih.gov/14635074/) | 2003 | Étude clinique | Cancer | VBM + irradiation dans le Hodgkin précoce de pronostic favorable |
| [32152484](https://pubmed.ncbi.nlm.nih.gov/32152484/) | 2020 | Revue | Nat Rev Clin Oncol | Récepteur alpha des folates comme cible en oncologie (poumon inclus) |
| [3475644](https://pubmed.ncbi.nlm.nih.gov/3475644/) | 1987 | Étude clinique | Oncology | Doxorubicine + méthotrexate hebdomadaires dans les sarcomes : réponse objective chez 28 % des patients aux doses élevées |

Aucun de ces travaux ne concerne directement le blastome pulmonaire.

---

## Informations de Marché en France

Le texte de l'indication approuvée n'est pas disponible dans les données compilées.

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 61972768 | IZIXATE 30 mg/0,60 mL, solution injectable en stylo injecteur prérempli | Solution injectable | ACCORD HEALTHCARE FRANCE | Active |
| 64739573 | METOTAB 2,5 mg, comprimé | Comprimé | MEDAC | Active |
| 63424973 | NORDIMET 15 mg, solution injectable en stylo prérempli | Solution injectable | NORDIC GROUP (PAYS-BAS) | Active |
| 64768062 | METOJECT 10 mg/0,2 ml, solution injectable en seringue préremplie | Solution injectable | MEDAC GESELLSCHAFT FUR KLINISCHE SPEZIALPRAPARATE (ALLEMAGN… | Active |
| 61981906 | METHOTREXATE VIATRIS 25 mg/ml, solution injectable | Solution injectable | VIATRIS SANTE | Active |
| 67791066 | METOJECT 22,5 mg/0,45 ml, solution injectable en stylo prérempli | Solution injectable | MEDAC GESELLSCHAFT FUR KLINISCHE SPEZIALPRAPARATE (ALLEMAGN… | Active |
| 62537295 | METOTAB 10 mg, comprimé sécable | Comprimé sécable | MEDAC | Active |
| 60705972 | IMETH 25 mg/ml, solution injectable en seringue préremplie | Solution injectable | NORDIC GROUP (PAYS-BAS) | Active |
| 61872547 | IMETH 20 mg/0,8 ml, solution injectable en seringue préremplie | Solution injectable | NORDIC GROUP (PAYS-BAS) | Active |
| 69310332 | METOJECT 20 mg/0,4 ml, solution injectable en seringue préremplie | Solution injectable | MEDAC GESELLSCHAFT FUR KLINISCHE SPEZIALPRAPARATE (ALLEMAGN… | Active |
| 65288721 | METHOTREXATE TEVA 2,5 POUR CENT (500 mg/20 mL), solution injectable | Solution injectable | TEVA SANTE | Active |
| 67670463 | METOJECT 15 mg/0,30 ml, solution injectable en stylo prérempli | Solution injectable | MEDAC GESELLSCHAFT FUR KLINISCHE SPEZIALPRAPARATE (ALLEMAGN… | Active |
| 66035589 | IZIXATE 10 mg/0,20 mL, solution injectable en stylo injecteur prérempli | Solution injectable | ACCORD HEALTHCARE FRANCE | Active |
| 68781833 | IMETH 17,5 mg/0,7 ml, solution injectable en seringue préremplie | Solution injectable | NORDIC GROUP (PAYS-BAS) | Active |
| 66253794 | METOJECT 15 mg/0,3 ml, solution injectable en seringue préremplie | Solution injectable | MEDAC GESELLSCHAFT FUR KLINISCHE SPEZIALPRAPARATE (ALLEMAGN… | Active |
| 69991749 | METOJECT 7,5 mg/0,15 ml, solution injectable en seringue préremplie | Solution injectable | MEDAC GESELLSCHAFT FUR KLINISCHE SPEZIALPRAPARATE (ALLEMAGN… | Active |
| 64229894 | IZIXATE 20 mg/0,40 mL, solution injectable en stylo injecteur prérempli | Solution injectable | ACCORD HEALTHCARE FRANCE | Active |
| 67311325 | NORDIMET 10 mg, solution injectable en stylo prérempli | Solution injectable | NORDIC GROUP (PAYS-BAS) | Active |
| 67853564 | NOVATREX 2,5 mg, comprimé | Comprimé | PFIZER HOLDING FRANCE | Active |
| 67217445 | METHOTREXATE VIATRIS 100 mg/ml, solution injectable | Solution injectable | VIATRIS SANTE | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.
Les données ne contiennent qu'une partie des autorisations ; la liste peut être incomplète.

<!-- licenses:end -->

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (antimétabolite, classe des antifolates) |
| Risque de Myélosuppression | Élevé à moyen selon la dose ; les données de contre-indication signalent thrombopénie, leucopénie et anémie |
| Classification d'Émétogénicité | Faible à moyenne aux doses habituelles, plus élevée à haute dose |
| Éléments de Surveillance | NFS avec formule, fonction hépatique et rénale, surveillance de la fonction pulmonaire ; taux sériques de méthotrexate en cas de haute dose |
| Protection de Manipulation | Les mesures de manipulation des médicaments cytotoxiques s'appliquent. Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

- **Affections associées à une contre-indication (graphe de connaissances, et non texte de la notice)** : insuffisance hépatique, maladie hépatique, maladie rénale, thrombopénie, leucopénie, anémie (dont macrocytaire), maladie pulmonaire interstitielle, fibrose pulmonaire, ulcère gastrique ou peptique, rectocolite hémorragique, maladie inflammatoire de l'intestin, stomatite, maladie du système immunitaire, maladie de la vésicule biliaire, pyo-uretère, abus ou dépendance à une substance.
- **Interactions médicamenteuses** : 784 interactions recensées. Parmi les exemples, **majeures** : rabéprazole, amoxicilline, acide acétylsalicylique ; **modérées** : doxycycline, tétracycline, clarithromycine, corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, budésonide), amphotéricine B, mésalazine, balsalazide, pioglitazone, bupropion, acarbose, acide chénodésoxycholique ; **mineure** : citrate de potassium.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le blastome pulmonaire n'a aucune preuve clinique ou publiée (niveau L5) : la prédiction repose uniquement sur le modèle.
- Parmi les autres indications du classement, le rhabdomyosarcome (L2) et le lymphome de Hodgkin (L3) sont mieux étayés et pourraient constituer des questions de recherche prioritaires, mais leurs preuves restent indirectes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications, indications approuvées), qui est un point bloquant
- Obtenir les données sur le mécanisme d'action depuis DrugBank
- Vérifier l'existence de cas publiés ou de données précliniques sur le blastome pulmonaire (et le carcinome fœtal bien différencié du poumon)
- Confirmer la population réellement incluse dans les études de méthotrexate classées sous rhabdomyosarcome
- Clarifier le statut réglementaire en France (la plupart des AMM sont actives ; certaines sont abrogées ou archivées) et la faisabilité de la voie d'administration
- Établir un plan de surveillance de la sécurité (hématologique, hépatique, rénale, pulmonaire)

<!-- review:begin fr-lic-20261115-methotrexate-1 -->

> **Correction de vérification (2026-11-15)**: Texte initial : « Clarifier le statut réglementaire en France (AMM annulées) » D’après la BDPM complète (CIS_bdpm et CIS_COMPO_bdpm, 2026-11-15), les spécialités contenant MÉTHOTREXATE comptent 71 AMM, dont 63 actives et 8 abrogées ou archivées. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_bdpm.txt); [Base de données publique des médicaments (BDPM) – CIS_COMPO_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_COMPO_bdpm.txt).

<!-- review:end fr-lic-20261115-methotrexate-1 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-15 | « Clarifier le statut réglementaire en France (AMM a » → « Clarifier le statut réglementaire en France (la pl » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_bdpm.txt); [Base de données publique des médicaments (BDPM) – CIS_COMPO_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_COMPO_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Jylamvo (methotrexate) prescribing information, SHORLA ONCOLOGY INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=96e931f5-51ae-4bdf-a441-bb0dd26d4c0e) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

