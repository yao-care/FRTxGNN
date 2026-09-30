---
layout: default
title: Arginine
parent: Preuves modérées (L3-L4)
nav_order: 42
evidence_level: L4
indication_count: 1
---

# Arginine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **1** 
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

# Arginine : D'une Indication Originale Non Documentée à la Gastroparésie

## Résumé en Une Phrase

L'arginine est commercialisée en France sous forme de solutions buvables, de comprimés effervescents et de solutions pour perfusion. Les données disponibles ne précisent pas son indication originale.
Le modèle TxGNN prédit qu'elle pourrait être utile dans la **gastroparésie**.
Cette direction repose sur **1 essai clinique** (non pertinent) et **10 publications** précliniques (études animales, un rapport de cas), sans aucune donnée d'efficacité chez l'humain.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données réglementaires |
| Nouvelle Indication Prédite | Gastroparésie |
| Score de Prédiction TxGNN | 99,42 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans DrugBank. Sur la base des connaissances générales, l'arginine (L-arginine) est le substrat des NO synthases (NOS), qui produisent le monoxyde d'azote (NO).

La vidange gastrique dépend en partie d'une transmission nitrergique inhibitrice (nNOS/NO), qui permet notamment la relaxation du pylore et l'accommodation gastrique. Un déficit en substrat (arginine) ou en cofacteur de la NOS pourrait donc ralentir la vidange gastrique. Cette hypothèse est le lien mécanistique proposé entre l'arginine et la gastroparésie.

Trois études précliniques vont dans ce sens :
- Chez la souris, la gastroparésie induite par les glucocorticoïdes passe par une déplétion en L-arginine (PMID 25057793).
- Chez le souriceau, un déficit en tétrahydrobioptérine, cofacteur de la NOS, provoque une gastroparésie (PMID 23639814).
- Chez le rat parkinsonien, la relaxation nitrergique du sphincter pylorique est altérée (PMID 35380456).

Ces travaux montrent qu'une voie NO déficiente s'associe à un retard de vidange gastrique. Ils ne démontrent pas qu'un apport d'arginine améliore la gastroparésie chez l'humain. Le score TxGNN de 0,994 reste une prédiction du modèle et non une preuve clinique.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01702051](https://clinicaltrials.gov/study/NCT01702051) | N/A | Inconnu | 150 | Étude observationnelle de l'autotransplantation d'îlots pancréatiques pour le contrôle glycémique après pancréatectomie. Sans lien avec l'arginine ni la gastroparésie (pertinence : C) |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [25057793](https://pubmed.ncbi.nlm.nih.gov/25057793/) | 2014 | Étude animale (souris) | Endocrinology | La dexaméthasone provoque une gastroparésie chez la souris par déplétion en L-arginine |
| [23639814](https://pubmed.ncbi.nlm.nih.gov/23639814/) | 2013 | Étude animale (souris) | Am J Physiol Gastrointest Liver Physiol | Le déficit en tétrahydrobioptérine (cofacteur de la NOS) induit une gastroparésie chez le souriceau |
| [35380456](https://pubmed.ncbi.nlm.nih.gov/35380456/) | 2022 | Étude animale (rat) | Am J Physiol Gastrointest Liver Physiol | Relaxation nitrergique altérée du sphincter pylorique dans un modèle parkinsonien |
| [18312542](https://pubmed.ncbi.nlm.nih.gov/18312542/) | 2008 | Étude animale (rat) | Neurogastroenterol Motil | Neuropathie myentérique jéjunale chez le rat diabétique BB, dans le contexte de la baisse d'expression de la nNOS |
| [18322959](https://pubmed.ncbi.nlm.nih.gov/18322959/) | 2008 | Étude animale (souris) | World J Gastroenterol | Effets moteurs gastriques de la ghréline et du GHRP-6 chez des souris diabétiques avec gastroparésie |
| [19023028](https://pubmed.ncbi.nlm.nih.gov/19023028/) | 2009 | Étude animale (chien, stimulation électrique) | Am J Physiol Gastrointest Liver Physiol | La stimulation électrique gastrique synchronisée améliore l'accommodation gastrique via la voie nitrergique |
| [21193530](https://pubmed.ncbi.nlm.nih.gov/21193530/) | 2011 | Étude animale (souris) | Am J Physiol Gastrointest Liver Physiol | L'inhibition de la motilité gastrique par l'hyperglycémie passe par les canaux KATP des ganglions nodosus |
| [31984783](https://pubmed.ncbi.nlm.nih.gov/31984783/) | 2020 | Étude animale (rat, neuromodulation) | Am J Physiol Gastrointest Liver Physiol | La stimulation du nerf sacré augmente l'accommodation gastrique chez le rat |
| [8194696](https://pubmed.ncbi.nlm.nih.gov/8194696/) | 1994 | Étude animale (rat) | Gastroenterology | Réponse motrice gastrique à l'anaphylaxie alimentaire chez le rat |
| [33867519](https://pubmed.ncbi.nlm.nih.gov/33867519/) | 2021 | Rapport de cas | Am J Case Rep | Normalisation du lactate sérique par modification du mode de vie chez une porteuse de la variante m.3243A>G |

Seules les trois premières publications se rattachent directement à l'hypothèse arginine/NO. Les autres décrivent des modèles de gastroparésie sans étudier l'arginine. Leur évaluation de pertinence est encore en attente.

## Informations de Marché en France

Le marché compte 20 AMM au total, dont voici les 5 principales. Le texte de l'indication approuvée n'est pas renseigné pour ces AMM.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 64556465 | SARGENOR 1 g/5 ml, solution buvable | Solution buvable |
| 62999615 | SARGENOR A LA VITAMINE C | Comprimé effervescent |
| 61960303 | AMINOVEN 10 POUR CENT | Solution pour perfusion |
| 69667989 | AMINOVEN 5 POUR CENT | Solution pour perfusion |
| 63183821 | AMINOPLASMAL 8 | Solution pour perfusion |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les preuves se limitent à des études animales (niveau L4). Il n'existe aucune donnée humaine d'efficacité ou de sécurité de l'arginine dans la gastroparésie, et le score TxGNN élevé ne suffit pas à lui seul.
- Les données de sécurité de la notice ANSM manquent et bloquent le criblage de sécurité. Le stade actuel est S0 (question de recherche).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications), une lacune bloquante.
- Obtenir les données de mécanisme d'action via DrugBank.
- Identifier l'indication originale de chaque AMM (textes d'indication non renseignés).
- Rechercher des études humaines (essais cliniques, séries de cas) sur l'arginine ou les donneurs de NO dans la gastroparésie.
- Évaluer la compatibilité des voies d'administration (orale ou perfusion) avec l'usage visé.
- Finaliser l'évaluation de pertinence des publications, actuellement en attente.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

