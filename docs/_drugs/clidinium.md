---
layout: default
title: Clidinium
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 10
---

# Clidinium
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Clidinium : De l'Anticholinergique Gastro-intestinal à la Maladie Ulcéreuse Peptique

## Résumé en Une Phrase

Clidinium (bromure de clidinium) est un anticholinergique quaternaire historiquement utilisé pour réduire les sécrétions gastriques et les spasmes du tube digestif, notamment en association avec le chlordiazépoxide (Librax®). Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Maladie Ulcéreuse Peptique**, avec **0 essai clinique enregistré** et **7 publications** (dont 1 essai clinique adjuvant) soutenant cette direction. Cette prédiction est remarquablement cohérente avec l'usage historique du médicament, antérieur à l'ère des antihistaminiques H2 et des inhibiteurs de pompe à protons.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Troubles gastro-intestinaux / Spasmes intestinaux (usage historique ; combinaison Librax®) |
| Nouvelle Indication Prédite | Maladie Ulcéreuse Peptique (Peptic Ulcer Disease) |
| Score de Prédiction TxGNN | 99.83% (rang TxGNN #4 par score ; rang #1 par niveau de preuve parmi les 10 prédictions) |
| Niveau de Preuve | L3 (études observationnelles + essai clinique adjuvant) |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base de données actuelle. Sur la base de la littérature disponible, clidinium est un anticholinergique quaternaire (sel d'ammonium quaternaire) agissant comme antagoniste des récepteurs muscariniques M1 et M3.

L'antagonisme M1/M3 se traduit par une double action : réduction de la sécrétion acide des cellules pariétales gastriques (voie M1) et diminution de la tension musculaire lisse gastroduodénale (voie M3). Ce mécanisme est directement pertinent pour la maladie ulcéreuse peptique. Avant l'avènement des anti-H2 (cimétidine, 1977) et des IPP (oméprazole, 1989), les anticholinergiques constituaient le traitement de référence de l'ulcère peptique. Clidinium, en combinaison avec le chlordiazépoxide (Librax®), ciblait simultanément le composant sécrétoire acide et la composante anxio-spastique de la maladie.

Une publication de 2016 (PMID 27386057) ouvre par ailleurs une piste clinique moderne distincte : clidinium comme adjuvant à la trithérapie 14 jours anti-*Helicobacter pylori*, avec un effet potentiel d'amélioration de la tolérance du traitement. Cette convergence entre usage historique et données récentes renforce la pertinence de la prédiction TxGNN.

> **Note sur la prédiction rang #1 (Cauda Equina Syndrome) :** Le modèle TxGNN attribue le score le plus élevé à cette indication (99.93%), mais le rationale mécanistique est contradictoire — un anticholinergique peut **aggraver** la rétention urinaire présente dans ce syndrome. Cette prédiction est probablement un artefact de propagation de voisinage dans le graphe de connaissances (GNN). Recommandation : Hold.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour la maladie ulcéreuse peptique avec clidinium (en monothérapie ou en combinaison moderne).

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [27386057](https://pubmed.ncbi.nlm.nih.gov/27386057/) | 2016 | Essai clinique (adjuvant RCT) | Caspian J Intern Med | Évaluation de l'ajout de clidinium-C à la trithérapie IPP 14 jours pour l'éradication d'*H. pylori* : efficacité d'éradication et prévention des effets indésirables |
| [4892352](https://pubmed.ncbi.nlm.nih.gov/4892352/) | 1969 | Évaluation clinique | Br J Clin Pract | Évaluation clinique de clidinium et Libraxin dans la prise en charge de l'ulcère duodénal |
| [6896942](https://pubmed.ncbi.nlm.nih.gov/6896942/) | 1982 | Cohorte / Étude clinique | Wiad Lek | Prévention des récidives d'ulcère duodénal après traitement par cimétidine ; rôle complémentaire des anticholinergiques |
| [14477958](https://pubmed.ncbi.nlm.nih.gov/14477958/) | 1962 | Série de cas | Hospital (Rio de Janeiro) | Traitement de l'ulcère gastroduodénal peptique par la combinaison bromure de clidinium et chlordiazépoxide |
| [14142206](https://pubmed.ncbi.nlm.nih.gov/14142206/) | 1964 | Série de cas | Rev Clin Esp | Résultats de l'association chlordiazépoxide (anxiolytique) + bromure de clidinium (anticholinergique) dans l'ulcère gastroduodénal |
| [14497768](https://pubmed.ncbi.nlm.nih.gov/14497768/) | 1962 | Série de cas | Minerva Medica | Essais cliniques de Librax Roche (bromure de clidinium + méthaminodiazépoxide) dans les maladies du tube digestif |
| [28539](https://pubmed.ncbi.nlm.nih.gov/28539/) | 1978 | Étude animale | Pharmacology | Interaction benzodiazépine–anticholinergique : effet additif ou supra-additif dans la protection contre les érosions gastriques induites par le stress chez la souris |

---

## Informations de Marché en France

Clidinium n'est pas commercialisé en France. Aucune AMM répertoriée à ce jour.

---

## Considérations de Sécurité

Veuillez consulter la notice officielle pour les informations de sécurité complètes. Les données spécifiques — mises en garde, contre-indications et interactions médicamenteuses — ne sont pas disponibles dans ce pack de données.

> **Point d'attention clinique :** En tant qu'anticholinergique quaternaire, clidinium partage les contre-indications de classe (glaucome à angle fermé, rétention urinaire, iléus paralytique, myasthénie grave) et les interactions attendues avec d'autres anticholinergiques ou dépresseurs du SNC. Ces éléments doivent être vérifiés via la monographie DrugBank ou la notice EMA avant tout usage clinique.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
La littérature documentée sur six décennies (1962–2016) confirme l'usage de clidinium dans l'ulcère peptique, et une publication de 2016 explore un rôle adjuvant potentiel dans la trithérapie anti-*H. pylori* — une piste clinique moderne qui mérite investigation. Cependant, les preuves restent majoritairement anciennes et produites dans un contexte pré-IPP, et aucun essai clinique contemporain contrôlé n'est disponible pour la maladie ulcéreuse en tant qu'indication principale.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données complètes de mécanisme d'action (MOA) via DrugBank API (DG002)
- Profil de sécurité complet : mises en garde TFDA/EMA, contre-indications, interactions médicamenteuses (DG001)
- Évaluation pharmacocinétique : biodisponibilité orale du sel quaternaire (absorption gastro-intestinale limitée, sélectivité intestinale élevée)
- Lecture complète de PMID 27386057 pour extraire les données d'efficacité et de tolérance de l'essai adjuvant H. pylori
- Évaluation de faisabilité réglementaire pour un repositionnement comme adjuvant de la trithérapie anti-*H. pylori* en France
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

