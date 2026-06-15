---
layout: default
title: Golimumab
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 5
---

# Golimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Golimumab : De la Polyarthrite Rhumatoïde à la Vascularite Rhumatoïde

## Résumé en Une Phrase

Golimumab (Simponi®) est un anticorps monoclonal anti-TNF-α entièrement humain, initialement approuvé pour le traitement de la polyarthrite rhumatoïde, de l'arthrite psoriasique et de la spondylarthrite ankylosante dans de nombreux pays (FDA, EMA).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **vascularite rhumatoïde** (rheumatoid vasculitis),
avec **3 essais cliniques** et **6 publications** soutenant actuellement cette direction de recherche.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Polyarthrite rhumatoïde / Arthrite psoriasique / Spondylarthrite ankylosante (approbations FDA/EMA mondiales) |
| Nouvelle Indication Prédite | Vascularite Rhumatoïde (Rheumatoid Vasculitis) |
| Score de Prédiction TxGNN | 99,73 % |
| Niveau de Preuve | L4 |
| Statut de Marché (Taïwan) | Non commercialisé |
| Nombre d'AMM (Taïwan) | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Golimumab est un anticorps monoclonal IgG1κ entièrement humain qui se lie de manière sélective et de haute affinité au TNF-α humain soluble et transmembranaire, bloquant son interaction avec les récepteurs membranaires p55 et p75. Cette inhibition du TNF-α supprime la cascade inflammatoire médiée par NF-κB, réduisant la production de cytokines pro-inflammatoires (IL-1β, IL-6, IL-8), l'expression de molécules d'adhésion endothéliale et l'activation des cellules vasculaires. C'est précisément ce mécanisme central qui fonde son efficacité remarquable dans les arthrites inflammatoires chroniques.

La vascularite rhumatoïde est une manifestation extra-articulaire grave de la polyarthrite rhumatoïde sévère et séropositive (RF+, anti-CCP+), survenant chez 1 à 5 % des patients. Sa physiopathologie implique le dépôt de complexes immuns dans la paroi des petits et moyens vaisseaux, l'activation du complément, et une inflammation vasculaire médiée par TNF-α conduisant à une nécrose fibrinoïde et à une ischémie tissulaire (ulcères cutanés, mono/polynévrite, atteinte viscérale). Puisque la vascularite rhumatoïde est une complication directe de la PR et partage le même substrat immunopathologique TNF-α-dépendant, l'inhibition par golimumab représente une cible mécanistique biologiquement plausible.

Les données épidémiologiques soutiennent indirectement cette hypothèse : l'introduction des anti-TNF dans la prise en charge de la PR a été associée à une réduction significative de l'incidence de la vascularite rhumatoïde. Un rapport de cas publié en 2018 (PMID 29075910) mentionne explicitement cette tendance favorable, décrivant un patient sous golimumab chez qui une complication sévère est néanmoins survenue, soulignant la complexité de ce tableau clinique. En l'absence d'essai clinique randomisé spécifiquement dédié à cette sous-population, les preuves restent de niveau L4.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---|---|---|---|---|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Pas encore en recrutement | 80 | Évaluation de l'incidence des poussées rhumatologiques et des complications infectieuses lors de la gestion péri-opératoire des immunosuppresseurs (dont golimumab) chez des patients subissant une arthroplastie de l'épaule ; indirect, non ciblé sur la vascularite |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Terminé | 184 | Étude observationnelle multicentrique évaluant les schémas pratiques, l'efficacité et la sécurité du tocilizumab chez des patients PR avec réponse inadéquate aux DMARDs ou à un biologique ; contexte PR général, non spécifique à la vascularite rhumatoïde |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Inconnu | 750 000 | Très large étude observationnelle rétrospective évaluant le risque de nouvelles maladies inflammatoires immuno-médiées (IMID) chez des patients traités par biologiques ; fournit un contexte de sécurité général pour les anti-TNF, sans cibler spécifiquement la vascularite |

> **Note :** Aucun essai clinique randomisé n'est spécifiquement enregistré pour golimumab dans la vascularite rhumatoïde. Les 3 essais identifiés présentent une pertinence indirecte (grade C) pour cette indication.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Cohorte/Comparative | Int. Journal of Molecular Sciences | Méta-analyse en réseau de 36 ECR comparant les 5 inhibiteurs de TNF approuvés (dont golimumab) ; tous réduisent de manière similaire la destruction articulaire radiographique dans la PR, sans différence significative entre originator et biosimilaires |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Revue | BMC Medicine | Mise à jour sur les thérapies biologiques pour les maladies rhumatologiques auto-immunes ; évalue les indications, les avantages et les limites des anti-TNF comme alternative aux DMARDs conventionnels |
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Rapport de cas | Rheumatology International | Décrit un cas de pyoderma gangrenosum et arthrite pyogène chez un patient PR traité par golimumab ; mentionne explicitement la réduction de l'incidence de la vascularite rhumatoïde depuis l'avènement des agents biologiques anti-TNF |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Rapport de cas | Joint Bone Spine | Deux cas d'artérite de Takayasu survenus sous anti-TNF ; illustre le rôle du TNF-α dans les vascularites à grands vaisseaux et la complexité des interactions entre anti-TNF et vascularites systémiques |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Rapport de cas | Ocular Immunology and Inflammation | Uvéite associée à la maladie de Behçet (vascularite systémique) traitée avec succès par golimumab hors AMM ; soutient l'efficacité potentielle de golimumab dans les manifestations vasculaires inflammatoires à médiation TNF-α |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Cohorte | Seminars in Arthritis and Rheumatism | Détermine la fréquence et les causes d'insuffisance rénale terminale dans la PR, avec la vascularite rhumatoïde identifiée comme cause pertinente ; données contextuelles sur la sévérité de la complication |

---

## Informations de Marché (Taïwan — TFDA)

Golimumab **n'est pas enregistré à Taïwan** (statut TFDA : non commercialisé, 0 licence d'AMM). Aucun tableau de licences n'est disponible.

> **Contexte international :** Golimumab (Simponi®, Simponi Aria® IV) est approuvé par la FDA (États-Unis) et l'EMA (Europe) pour la polyarthrite rhumatoïde, l'arthrite psoriasique, la spondylarthrite axiale (dont l'ankylosante) et la colite ulcéreuse. La formulation intraveineuse est également approuvée par la FDA pour la polyarthrite juvénile idiopathique à évolution polyarticulaire. Son absence de commercialisation à Taïwan constitue un enjeu d'accès à considérer pour tout développement dans cette région.

---

## Considérations de Sécurité

Les données de sécurité spécifiques (avertissements officiels TFDA, contre-indications formelles) ne sont pas disponibles dans ce dossier. Sur la base du profil de sécurité mondial connu de golimumab en tant qu'inhibiteur du TNF-α :

- **Risque infectieux :** Augmentation du risque d'infections graves, notamment tuberculose (dépistage obligatoire avant instauration), infections fongiques invasives (histoplasmose, coccidioïdomycose), infections bactériennes et virales opportunistes.
- **Réactivation virale :** Risque de réactivation de l'hépatite B chez les porteurs chroniques ; sérologie HBV obligatoire en pré-thérapeutique.
- **Risque de malignité :** Signal de risque accru de lymphomes et d'autres malignités, notamment chez les patients pédiatriques traités par anti-TNF combiné à un immunomodulateur.

> Veuillez consulter la notice officielle (EMA/FDA) pour les informations complètes de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La vascularite rhumatoïde partage le même substrat pathologique TNF-α-dépendant que la PR classique, et des données épidémiologiques indirectes suggèrent un effet protecteur des anti-TNF sur cette complication. Cependant, l'absence totale d'essai clinique randomisé spécifiquement dédié, une base littéraire limitée à des rapports de cas et des études observationnelles indirectes (niveau de preuve L4), et l'absence d'enregistrement à Taïwan ne permettent pas de recommander un passage en évaluation clinique formelle sans travaux préliminaires complémentaires.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtention des données de mécanisme d'action (MOA) détaillées depuis DrugBank (DG002 — priorité haute)
- Récupération des avertissements et contre-indications officiels TFDA (DG001 — priorité bloquante)
- Revue systématique de la littérature dédiée à la vascularite rhumatoïde sous anti-TNF (au-delà des 6 publications actuelles)
- Conception d'un registre ou d'une étude de cohorte prospective ciblant spécifiquement les patients PR sévères avec vascularite confirmée traités par golimumab
- Évaluation du chemin réglementaire nécessaire pour un enregistrement à Taïwan avant toute étude locale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

