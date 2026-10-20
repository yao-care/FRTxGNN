---
layout: default
title: Atorvastatin
parent: Preuves élevées (L1-L2)
nav_order: 79
evidence_level: L1
indication_count: 6
last_modified_at: 2026-10-14
description: "Atorvastatin : nouvelle indication prédite, Hypercholestérolémie familiale (niveau de preuve L1). Indication d'origine : Hypertriglycéridémie"
monitor_inn: "atorvastatin"
predicted_indications: ["HIV infectious disease", "brain stem infarction", "cholesterol-ester transfer protein deficiency", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Atorvastatin
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **6** 
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

# Atorvastatine : De l'hypertriglycéridémie à l'hypercholestérolémie familiale

## Résumé en Une Phrase

L'atorvastatine est une statine initialement utilisée pour traiter les dyslipidémies (hypertriglycéridémie, hypercholestérolémie familiale homozygote) et pour la prévention des maladies cardiovasculaires et cérébrovasculaires.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hypercholestérolémie familiale** (forme incluant notamment la forme hétérozygote et pédiatrique), avec **15 essais cliniques** et **20 publications** soutenant actuellement cette direction.
Il s'agit d'une prédiction proche d'un usage déjà reconnu, puisque la forme homozygote figure déjà parmi les indications d'origine.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertriglycéridémie (les textes d'indication des AMM ne sont pas renseignés ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Hypercholestérolémie familiale |
| Score de Prédiction TxGNN | 99,42 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✗ Toutes les AMM sont annulées |
| Nombre d'AMM | 13 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, l'atorvastatine appartient à la classe des statines : elle inhibe l'HMG-CoA réductase, ce qui réduit la synthèse hépatique du cholestérol et augmente le nombre de récepteurs du LDL, donc la clairance du LDL-cholestérol.

L'hypercholestérolémie familiale homozygote figure déjà parmi les indications d'origine ; l'utilisation dans cette maladie est donc de fait sur l'indication ou très proche. Les formes hétérozygote et pédiatrique relèvent de la même physiopathologie, ce qui rend la prédiction cohérente.

Une limite doit être notée : l'efficacité est atténuée chez les patients dont la fonction du récepteur du LDL est très réduite. C'est pourquoi des traitements complémentaires (ézétimibe, acide bempédoïque, évinacumab) sont utilisés en association.

---

## Preuves d'Essais Cliniques

Parmi les 15 essais compilés, voici les 10 plus pertinents.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00827606](https://clinicaltrials.gov/study/NCT00827606) | Phase 3 | Terminé | 272 | Étude ouverte de 3 ans : croissance, développement et réduction du cholestérol sous atorvastatine chez des enfants et adolescents atteints d'HF hétérozygote |
| [NCT00134485](https://clinicaltrials.gov/study/NCT00134485) | Phase 3 | Terminé | 400 | Torcétrapib/atorvastatine versus atorvastatine seule, en double aveugle, dans l'HF hétérozygote (projet torcétrapib arrêté en 2006 pour raisons de sécurité) |
| [NCT00134511](https://clinicaltrials.gov/study/NCT00134511) | Phase 3 | Terminé | 30 | Étude ouverte de la combinaison torcétrapib/atorvastatine dans l'HF homozygote |
| [NCT00136981](https://clinicaltrials.gov/study/NCT00136981) | Phase 3 | Terminé | 800 | Évaluation échographique carotidienne de l'effet anti-athéroscléreux de la combinaison versus atorvastatine seule dans l'HF hétérozygote |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Terminé | 50 | Efficacité et sécurité de l'ézétimibe ajouté à l'atorvastatine ou à la simvastatine dans l'HF homozygote |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Terminé | 44 | Extension ouverte de 24 mois sur la sécurité à long terme de l'ézétimibe associé à l'atorvastatine ou à la simvastatine dans l'HF homozygote |
| [NCT00739999](https://clinicaltrials.gov/study/NCT00739999) | Phase 1 | Terminé | 39 | Pharmacocinétique, pharmacodynamique et tolérance de l'atorvastatine sur 8 semaines chez des enfants et adolescents atteints d'HF hétérozygote |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Terminé | 249 | Alirocumab versus placebo dans l'HF hétérozygote insuffisamment contrôlée par le traitement hypolipémiant |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Phase 3 | Terminé | 153 | Alirocumab versus placebo chez l'enfant et l'adolescent atteints d'HF hétérozygote, sous statine |
| [NCT01279590](https://clinicaltrials.gov/study/NCT01279590) | Phase 2 | Terminé | 282 | PPD10558 versus atorvastatine : incidence des myalgies liées aux statines chez des patients intolérants aux statines |

Remarque : dans plusieurs essais, l'atorvastatine est le traitement de fond ou le comparateur et non le seul produit testé. Seuls les essais pédiatriques NCT00827606 et NCT00739999 évaluent l'atorvastatine seule.

---

## Preuves de la Littérature

Parmi les 20 publications compilées, voici les plus pertinentes.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [25760954](https://pubmed.ncbi.nlm.nih.gov/25760954/) | 2015 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | Efficacité de l'atorvastatine sur les lipides, en fonction de la dose |
| [27678432](https://pubmed.ncbi.nlm.nih.gov/27678432/) | 2016 | Étude clinique | J Clin Lipidol | Étude de 3 ans sur l'atorvastatine chez l'enfant et l'adolescent atteints d'HF hétérozygote |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Étude comparative | Nutr Metab Cardiovasc Dis | Atorvastatine versus simvastatine dans l'HF hétérozygote : atteinte des objectifs de LDL-C et variables de coagulation |
| [12883464](https://pubmed.ncbi.nlm.nih.gov/12883464/) | 2003 | Étude clinique | Med Sci Monit | L'atorvastatine réduit la microalbuminurie chez des patients atteints d'HF |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Recommandations | Endocr Pract | Recommandations AACE/ACE sur la prise en charge de la dyslipidémie |
| [14604738](https://pubmed.ncbi.nlm.nih.gov/14604738/) | 2003 | Revue | Clin Ther | Ézétimibe, notamment en association avec la simvastatine ou l'atorvastatine dans l'HF homozygote |
| [15199433](https://pubmed.ncbi.nlm.nih.gov/15199433/) | 2004 | Revue | Semin Vasc Med | Aspects diagnostiques, cliniques et thérapeutiques de l'HF chez l'enfant |
| [10582478](https://pubmed.ncbi.nlm.nih.gov/10582478/) | 1999 | Revue | Rev Med Brux | Présentation de l'atorvastatine : inhibition de l'HMG-CoA réductase et réduction de la production d'apoB |
| [40874855](https://pubmed.ncbi.nlm.nih.gov/40874855/) | 2026 | Étude en vie réelle | J Clin Res Pediatr Endocrinol | Aspects génétiques et thérapeutiques de l'HF hétérozygote pédiatrique en Turquie |
| [40254247](https://pubmed.ncbi.nlm.nih.gov/40254247/) | 2025 | Préclinique | Toxicology | Myotoxicité des statines lipophiles et hydrophiles sur des cellules musculaires dérivées de patients atteints d'HF |

---

## Informations de Marché en France

Les 13 AMM recensées sont toutes annulées ; aucune AMM valide n'est actuellement répertoriée. Le texte d'indication n'est pas renseigné pour ces AMM. Voici 5 d'entre elles :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67059408 | ATORVASTATINE HCS 10 mg | Comprimé pelliculé | Non renseignée |
| 63366057 | ATORVASTATINE SANDOZ 80 mg | Comprimé pelliculé sécable | Non renseignée |
| 65168323 | ATORVASTATINE HCS 80 mg | Comprimé pelliculé | Non renseignée |
| 64176801 | ATORVASTATINE HCS 20 mg | Comprimé pelliculé | Non renseignée |
| 66331392 | ATORVASTATINE TEVA SANTE 20 mg | Comprimé pelliculé | Non renseignée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : insuffisance hépatique, maladie hépatique, maladie rénale, maladie de la vésicule biliaire, hypothyroïdie (dont myxœdème et hypothyroïdie congénitale), myopathie et maladies musculaires, rhabdomyolyse, paralysie périodique familiale, hypotension, abus ou dépendance à des substances, pyourétère, fasciite nodulaire, traumatisme.
- **Interactions médicamenteuses** : 301 interactions recensées.
  - Majeure : clarithromycine.
  - Modérées (principales) : aprépitant, oméprazole, ésoméprazole, lansoprazole, pantoprazole, cimétidine, clotrimazole, miconazole, dexaméthasone, métronidazole, naltrexone, rosuvastatine, simvastatine, éliglustat, éluxadoline, pectine.
  - Mineures : hydroxyde d'aluminium, hydroxyde de magnésium, liraglutide.
- L'atorvastatine est un substrat du CYP3A4 ; une attention particulière est nécessaire avec les inhibiteurs de ce cytochrome.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

---

## Autres Indications Prédites (Pour Information)

| Rang | Indication | Score | Niveau de Preuve | Recommandation |
|---|---|---|---|---|
| 2 | Infection par le VIH | 99,31 % | L2 | Question de recherche : intérêt surtout métabolique et cardiovasculaire, sans preuve d'effet antiviral |
| 3 | Infarctus du tronc cérébral | 99,31 % | L4 | Hold : preuves indirectes, indication AVC déjà couverte |
| 4 | Déficit en protéine de transfert des esters de cholestérol | 99,25 % | L4 | Hold : pas de cible thérapeutique claire |
| 5 | Hypercholestérolémie par déficit en cholestérol 7α-hydroxylase | 99,20 % | L5 | Hold : réponse clinique probablement faible, données animales seulement |
| 6 | Trouble neurodéveloppemental avec ataxie et absence de parole | 99,13 % | L5 | Hold : aucune donnée |

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de phase 3 (dont des études pédiatriques de longue durée) et des revues soutiennent l'efficacité de l'atorvastatine dans l'hypercholestérolémie familiale. Cependant, l'indication est proche d'un usage déjà établi, toutes les AMM françaises sont annulées et les données de sécurité issues de la notice manquent.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice officielle (ANSM), absentes des données compilées et bloquantes pour l'évaluation de sécurité.
- Les données détaillées sur le mécanisme d'action (DrugBank).
- La vérification du statut réglementaire actuel en France, y compris les spécialités princeps, puisque les 13 AMM génériques répertoriées sont annulées.
- Un plan de surveillance spécifique (fonction hépatique, symptômes musculaires, interactions CYP3A4) et des précisions sur les populations pédiatriques.
- La confirmation des comparateurs et populations des essais dont les titres sont tronqués.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

