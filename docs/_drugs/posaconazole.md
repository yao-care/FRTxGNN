---
layout: default
title: Posaconazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 243
evidence_level: L5
indication_count: 1
---

# Posaconazole
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Posaconazole : Des Infections Fongiques Invasives à la Pneumocystose

## Résumé en Une Phrase

Le posaconazole est un antifongique de la famille des triazolés, utilisé contre les infections fongiques invasives. Le texte d'indication de ses AMM françaises n'est pas renseigné dans le dossier.
Le modèle TxGNN prédit qu'il pourrait être efficace contre la **pneumocystose**. Cette prédiction repose sur **2 essais cliniques** et **5 publications**, mais aucun ne teste le posaconazole dans cette indication, et le mécanisme d'action rend ce signal peu plausible.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM (antifongique triazolé) |
| Nouvelle Indication Prédite | Pneumocystose |
| Score de Prédiction TxGNN | 99,77 % |
| Niveau de Preuve | L5 (aucune étude ne teste le posaconazole dans la pneumocystose ; le dossier source indique L4, mais aucune étude préclinique ou mécanistique n'y est documentée) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 10 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Le posaconazole fait partie des azolés antifongiques. Il inhibe la lanostérol 14-alpha-déméthylase (CYP51) et bloque ainsi la synthèse de l'ergostérol, un constituant de la membrane des champignons.

Ce mécanisme s'applique mal à la pneumocystose. *Pneumocystis jirovecii* n'a pas d'ergostérol dans sa membrane cellulaire (il utilise du cholestérol et des stérols apparentés). On n'attend donc pas d'activité significative des azolés contre lui.

Le score très élevé de TxGNN (0,998) reflète probablement l'association du médicament avec d'autres infections fongiques invasives dans le graphe de connaissances. Ce n'est pas un signal soutenu par le mécanisme. Comme le champ MOA de la source est vide, ce lien n'a pas pu être vérifié par rapport au mécanisme enregistré.

## Preuves d'Essais Cliniques

Les deux essais ci-dessous sont classés de pertinence faible (grade C). Aucun n'évalue le posaconazole dans la pneumocystose.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Terminé | 602 | Étude ReSPECT : rezafungine IV versus schéma antimicrobien standard pour prévenir les infections fongiques invasives après greffe allogénique de moelle. Le posaconazole n'est au mieux qu'une partie du comparateur. |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | En recrutement | 358 | Protocole plateforme de prophylaxie de la GVHD par cyclophosphamide post-greffe (donneur non apparenté HLA-incompatible). Les infections ne sont que des critères secondaires ou incidents. |

## Preuves de la Littérature

Aucune publication n'étudie l'efficacité du posaconazole dans la pneumocystose. Il s'agit de recommandations, de revues générales et d'une cohorte rétrospective.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2025 | Recommandations | Lancet Infect Dis | Mise à jour 2025 des recommandations de la British Society for Medical Mycology sur le diagnostic des maladies fongiques graves (microscopie, antigènes, anticorps, tests moléculaires). |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Recommandations | Zhonghua Jie He He Hu Xi Za Zhi | Recommandations chinoises 2025 sur le diagnostic et la prise en charge des mycoses pulmonaires invasives, notamment chez les patients non immunodéprimés. |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Revue | Swiss Med Wkly | Panorama des infections fongiques invasives (candidose, aspergillose, cryptococcose, pneumocystose). La prophylaxie par posaconazole, actif sur les moisissures, a réduit les infections fongiques chez les patients hémato-oncologiques à haut risque. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Revue (pharmacocinétique) | Clin Pharmacokinet | Pénétration des anti-infectieux dans le liquide de revêtement épithélial pulmonaire, avec des différences selon les antifongiques et les formulations. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohorte rétrospective | Transpl Infect Dis | Complications infectieuses de la GVHD aiguë après transplantation hépatique, principale cause de décès après le diagnostic de GVHD. |

## Informations de Marché en France

Le posaconazole compte 10 AMM au total ; les 5 principales sont listées ci-dessous. Le texte de l'indication approuvée n'est pas renseigné pour ces AMM. Le dossier signale aussi une forme en solution à diluer pour perfusion.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 69380042 | NOXAFIL 100 mg | Comprimé gastro-résistant | Merck Sharp & Dohme (Pays-Bas) |
| 63689562 | Posaconazole Zentiva 100 mg | Comprimé gastro-résistant | Zentiva France |
| 62713448 | Posaconazole Fresenius Kabi 100 mg | Comprimé gastro-résistant | Fresenius Kabi France |
| 67003384 | Posaconazole Viatris 40 mg/mL | Suspension buvable | Viatris Santé |
| 63474691 | Posaconazole AHCL 40 mg/mL | Suspension buvable | Accord Healthcare (Espagne) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucune étude clinique ne teste le posaconazole dans la pneumocystose, et *Pneumocystis* n'a pas d'ergostérol, cible du médicament. Le score TxGNN élevé semble refléter une association avec d'autres mycoses plutôt qu'un vrai signal thérapeutique.
- Les données de sécurité ANSM manquent et bloquent tout passage au criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications), en priorité car ces données sont bloquantes.
- Compléter les données sur le mécanisme d'action (DrugBank).
- Rechercher des données directes (in vitro, animales ou cliniques) sur l'activité du posaconazole contre *Pneumocystis*.
- Vérifier dans le graphe de connaissances l'origine de l'association posaconazole–pneumocystose.
- Renseigner les indications approuvées des AMM françaises.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

