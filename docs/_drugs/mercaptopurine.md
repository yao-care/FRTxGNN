---
layout: default
title: Mercaptopurine
parent: Prédiction du modèle uniquement (L5)
nav_order: 480
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Mercaptopurine : nouvelle indication prédite, Leucémie myéloïde (niveau de preuve L5). Indication d'origine : Leucémie aiguë lymphoblastique"
monitor_inn: "MERCAPTOPURINE"
predicted_indications: ["myeloid leukemia", "pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "pulmonary blastoma", "Hodgkins lymphoma", "primary pulmonary lymphoma", "small cell lung carcinoma", "well-differentiated fetal adenocarcinoma of the lung"]
---

# Mercaptopurine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Mercaptopurine : De la leucémie aiguë lymphoblastique à la leucémie myéloïde

## Résumé en Une Phrase

La mercaptopurine est un antimétabolite analogue des purines, utilisé à l'origine dans le traitement de la leucémie aiguë lymphoblastique.
Le modèle TxGNN prédit qu'elle pourrait être utile dans la **leucémie myéloïde**, mais les données compilées ne permettent pas d'isoler son effet propre : elle apparaît surtout comme composante de protocoles multi-médicaments. Les données comptent **14 essais cliniques** (dont 6 de phase 3 terminés) et **20 publications**, avec un niveau de preuve direct limité.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Leucémie aiguë lymphoblastique (indication issue du graphe de connaissances, le texte d'indication de l'AMM française n'étant pas renseigné) |
| Nouvelle Indication Prédite | Leucémie myéloïde |
| Score de Prédiction TxGNN | 99,94 % |
| Niveau de Preuve | L2 (voir la note ci-dessous) |
| Statut de Marché en France | Autorisation annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 (0 valide, 1 annulée) |
| Décision Recommandée | Hold |

*Note sur le niveau de preuve :* en application stricte des critères, six essais de phase 3 terminés sont listés, ce qui correspondrait à L1. Aucun ne teste toutefois la mercaptopurine comme variable étudiée : elle n'y figure qu'au sein de schémas de chimiothérapie ou de traitements d'entretien. J'ai donc retenu L2, plus prudent.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances pharmacologiques établies, la mercaptopurine est un antimétabolite des purines. Ses métabolites actifs, les nucléotides de thioguanine, s'incorporent à l'ADN et à l'ARN et inhibent la synthèse de novo des purines. Cela est毒 pour les cellules à prolifération rapide, comme les myéloblastes leucémiques.

La leucémie aiguë lymphoblastique et la leucémie myéloïde sont deux hémopathies malignes à prolifération rapide, ce qui rend le mécanisme potentiellement transposable. Dans la littérature, la mercaptopurine intervient surtout comme composante de schémas associés : entretien oral mercaptopurine/méthotrexate dans la LAM non éligible à la greffe, consolidation de type LAL dans la LAM de l'enfant, et entretien de la leucémie aiguë promyélocytaire (LAP).

Il faut rester prudent : aucune des données ne permet d'attribuer un bénéfice à la mercaptopurine seule. Les essais de phase 3 listés testent d'autres variables (arsenic, ATRA, cytarabine, etc.). Seul un essai de phase 1 (association vénétoclax + 6-MP, 10 patients) cible directement le médicament dans la LAM en rechute ou réfractaire.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Phase 1 | En recrutement | 10 | Vénétoclax + 6-mercaptopurine dans la LAM en rechute ou réfractaire (étude ouverte non commerciale) ; pertinence mécanistique, mais effectif très faible |
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Phase 1/2 | En recrutement | 48 | Hydroxyurée + acide valproïque, ou 6-MP + acide valproïque, chez des patients atteints de LAM ou de SMD à haut risque non éligibles au traitement standard ; évalue sécurité, tolérance et efficacité préliminaire |
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Phase 3 | Terminé | 420 | Trétinoïne + chimiothérapie avec ou sans trioxyde d'arsenic dans la LAP ; l'entretien compare trétinoïne intermittente seule vs trétinoïne + mercaptopurine + méthotrexate |
| [NCT00492856](https://clinicaltrials.gov/study/NCT00492856) | Phase 3 | Terminé | 105 | Étude S0521 : entretien vs observation dans la LAP de risque faible ou intermédiaire ; rôle de la mercaptopurine supposé mais non confirmé |
| [NCT02688140](https://clinicaltrials.gov/study/NCT02688140) | Phase 3 | Terminé | 133 | Trioxyde d'arsenic + ATRA + idarubicine vs schéma AIDA dans la LAP à haut risque ; l'effet de la mercaptopurine n'est pas isolé |
| [NCT00002701](https://clinicaltrials.gov/study/NCT00002701) | Phase 3 | Inconnu | 750 | ATRA + idarubicine, consolidation puis greffe ou entretien randomisé selon la maladie résiduelle dans la LAP ; l'entretien classique associe 6-MP et méthotrexate |
| [NCT00482833](https://clinicaltrials.gov/study/NCT00482833) | Phase 3 | Terminé | 276 | Trioxyde d'arsenic + ATRA vs schéma AIDA dans la LAP de risque non élevé ; essai randomisé ouvert multicentrique |
| [NCT00866918](https://clinicaltrials.gov/study/NCT00866918) | Phase 3 | Terminé | 106 | Traitement adapté au risque de la LAP de l'enfant avec trioxyde d'arsenic en consolidation |
| [NCT02521493](https://clinicaltrials.gov/study/NCT02521493) | Phase 3 | Actif, non en recrutement | 280 | Chimiothérapie stratifiée selon la réponse dans la LAM ou le SMD de l'enfant trisomique 21 ; rôle de la mercaptopurine incertain |
| [NCT00136084](https://clinicaltrials.gov/study/NCT00136084) | Phase 3 | Terminé | 238 | Comparaison de deux schémas multi-agents avec différentes doses de cytarabine dans la LAM ou la myélodysplasie nouvellement diagnostiquée ; contribution indirecte de la mercaptopurine |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | Cohorte | J Korean Med Sci | Entretien oral par 6-MP quotidienne + méthotrexate hebdomadaire pendant 2 ans chez des patients atteints de LAM non éligibles à la greffe, après consolidation |
| [38828002](https://pubmed.ncbi.nlm.nih.gov/38828002/) | 2024 | Cohorte | Ther Adv Hematol | Chimiothérapie intensive avec double induction et consolidation de type LAL dans la LAM de l'enfant (centres chinois) |
| [27275453](https://pubmed.ncbi.nlm.nih.gov/27275453/) | 2016 | Étude pilote prospective | South Asian J Cancer | Chimiothérapie métronomique par 6-MP orale dans la LAM du sujet âgé, comme option palliative |
| [22715121](https://pubmed.ncbi.nlm.nih.gov/22715121/) | 2012 | Cohorte (phase 2) | Blood | Protocole APML4 : ATRA, idarubicine et arsenic IV dans la LAP |
| [32459546](https://pubmed.ncbi.nlm.nih.gov/32459546/) | 2020 | Rétrospective | Pediatr Hematol Oncol | Devenir de patients atteints de leucémie myélomonocytaire juvénile après traitement séquentiel cytarabine puis 6-MP |
| [3513537](https://pubmed.ncbi.nlm.nih.gov/3513537/) | 1986 | Étude clinique | Am J Clin Oncol | Hydroxyurée + 6-MP dans la leucémie granulocytaire chronique (92 patients, deux études successives) |
| [2676034](https://pubmed.ncbi.nlm.nih.gov/2676034/) | 1989 | Revue | Blood Rev | Métabolisme des purines comme cible de la chimiothérapie des leucémies ; la 6-mercaptopurine y figure parmi les analogues structuraux des purines |
| [12057059](https://pubmed.ncbi.nlm.nih.gov/12057059/) | 2000 | Revue | Curr Treat Options Oncol | Prise en charge de la LAP : ATRA essentiel à l'induction, consolidation sans cytarabine à haute dose |
| [34442422](https://pubmed.ncbi.nlm.nih.gov/34442422/) | 2021 | Revue | J Pers Med | Importance des polymorphismes de NUDT15 et TPMT pour la toxicité des thiopurines (myélosuppression, alopécie) |
| [28152123](https://pubmed.ncbi.nlm.nih.gov/28152123/) | 2017 | Étude associée à la sécurité | JAMA Oncol | Néoplasmes myéloïdes secondaires après traitement de maladies auto-immunes ; signal de sécurité, non une preuve d'efficacité |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63377491 | PURINETHOL 50 mg, comprimé | Comprimé | Non renseignée (AMM annulée, laboratoire ASPEN PHARMA TRADING, Irlande) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (antimétabolite, analogue des purines) |
| Risque de Myélosuppression | Élevé (neutropénie, thrombopénie, leucopénie et anémie figurent parmi les contre-indications du graphe de connaissances ; la littérature décrit une myélosuppression fréquente nécessitant des ajustements de dose) |
| Classification d'Émétogénicité | Faible (voie orale) |
| Éléments de Surveillance | NFS avec formule, fonction hépatique (bilirubine, transaminases), fonction rénale, amylase/lipase en cas de douleurs abdominales ; génotypage TPMT/NUDT15 avant traitement |
| Protection de Manipulation | Les précautions de manipulation des médicaments cytotoxiques s'appliquent |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie rénale, pancréatite, maladie hépatique, maladie de la vésicule biliaire, pyourètre, thrombopénie, neutropénie, agranulocytose, leucopénie, anémie (dont macrocytaire), hyperbilirubinémie (dont héréditaire), syndrome de Gilbert, cholestase (dont cholestase intrahépatique récurrente bénigne et familiale), lymphome hépatosplénique à cellules T.
- **Interactions médicamenteuses** : 100 interactions répertoriées. Les principales sont de niveau modéré avec la mésalazine, le balsalazide, l'olsalazine, la sulfasalazine et la naltrexone. La lévofloxacine est de niveau mineur. Plusieurs autres (pantoprazole, oméprazole, prednisone, metformine, vancomycine, etc.) sont de niveau inconnu. La littérature compilée évoque aussi les inhibiteurs de la xanthine oxydase (allopurinol), qui modifient l'exposition aux métabolites actifs.
- **Pharmacogénétique** : les variants de TPMT et NUDT15 sont associés à une myélosuppression sévère et à une intolérance ; une adaptation de dose guidée par le génotype est nécessaire.

Les mises en garde et contre-indications de la notice n'ont pas pu être consultées : veuillez vous reporter à la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les données sur la leucémie myéloïde sont indirectes : la mercaptopurine n'est jamais la variable testée dans les essais de phase 3 listés, et le seul essai ciblant le médicament (phase 1, 10 patients) est précoce.
- Aucune AMM valide n'est disponible en France et les informations de sécurité de la notice manquent, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde, contre-indications) auprès de l'ANSM, et vérifier la disponibilité réelle d'une formulation commercialisée.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Consulter les protocoles complets des essais NCT00003934, NCT00492856 et NCT00002701 pour déterminer si la mercaptopurine y est réellement utilisée et si son effet peut être évalué.
- Attendre ou rechercher des résultats d'essais ciblant spécifiquement la mercaptopurine dans la LAM (par ex. NCT05506332 avec le vénétoclax).
- Prévoir un plan de sécurité : génotypage TPMT/NUDT15, surveillance hématologique et hépatique, gestion des interactions.

*Remarque :* l'indication d'origine (leucémie aiguë lymphoblastique) et la leucémie/lymphome lymphoblastique précurseur restent des usages établis, et non du repositionnement. Les autres prédictions (leucémie lymphoïde chronique, lymphome de Hodgkin, carcinome à petites cellules du poumon, etc.) reposent sur très peu de preuves, voire aucune, et sont en attente.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

