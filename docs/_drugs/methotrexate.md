---
layout: default
title: Methotrexate
parent: Prédiction du modèle uniquement (L5)
nav_order: 487
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
monitor_inn: "methotrexate"
predicted_indications: ["pulmonary blastoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "Hodgkins lymphoma", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
description: "Methotrexate : nouvelle indication prédite, Pulmonary blastoma (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
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
| Nombre d'AMM | 20 (dont 20 annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le méthotrexate est un antifolate : il inhibe la dihydrofolate réductase et freine la synthèse de l'ADN dans les cellules à division rapide. Son efficacité est établie dans les hémopathies lymphoïdes (leucémie lymphoblastique aiguë, lymphome non hodgkinien).

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

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61972768 | IZIXATE 30 mg/0,60 mL (Accord Healthcare France) | Solution injectable (stylo prérempli) | Non disponible |
| 64739573 | METOTAB 2,5 mg (Medac) | Comprimé | Non disponible |
| 63424973 | NORDIMET 15 mg (Nordic Group) | Solution injectable (stylo prérempli) | Non disponible |
| 64768062 | METOJECT 10 mg/0,2 ml (Medac) | Solution injectable (seringue préremplie) | Non disponible |
| 61981906 | METHOTREXATE VIATRIS 25 mg/ml | Solution injectable | Non disponible |

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
- Clarifier le statut réglementaire en France (AMM annulées) et la faisabilité de la voie d'administration
- Établir un plan de surveillance de la sécurité (hématologique, hépatique, rénale, pulmonaire)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

