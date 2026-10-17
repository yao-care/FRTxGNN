---
layout: default
title: Cobimetinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 194
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cobimetinib : nouvelle indication prédite, Sclérose latérale amyotrophique (niveau de preuve L5). Indication d'origine : Mélanome métastatique"
monitor_inn: "cobimetinib"
predicted_indications: ["amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "axial spondylometaphyseal dysplasia", "Mills syndrome", "amyotrophic lateral sclerosis, susceptibility to", "lower motor neuron syndrome with late-adult onset", "trichomegaly-retina pigmentary degeneration-dwarfism syndrome", "lethal arthrogryposis-anterior horn cell disease syndrome", "amyotrohpic lateral sclerosis type 22", "monomelic amyotrophy"]
---

# Cobimetinib
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Cobimétinib : Du Mélanome Métastatique à la Sclérose Latérale Amyotrophique

## Résumé en Une Phrase

Le cobimétinib était initialement utilisé pour le traitement du mélanome métastatique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **sclérose latérale amyotrophique (SLA)**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Mélanome métastatique (source : graphe de connaissances TxGNN ; le texte d'indication de l'AMM française n'est pas renseigné) |
| Nouvelle Indication Prédite | Sclérose latérale amyotrophique |
| Score de Prédiction TxGNN | 99,73 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement annulée (AMM annulée) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le cobimétinib appartient à la classe des inhibiteurs de MEK1/2, qui bloquent la voie MAPK/ERK. Son efficacité dans le mélanome métastatique (généralement en association avec un inhibiteur de BRAF) relève de cette classe pharmacologique.

L'activation de la voie MAPK/ERK a été évoquée dans la neuroinflammation et les réponses de stress des motoneurones dans la SLA. Un lien plausible existe donc, mais il n'est pas validé. Le score TxGNN est très élevé (0,997), sans aucun essai ni publication dans les données fournies.

Un point affaiblit encore l'hypothèse : la pénétration du cobimétinib dans le système nerveux central est limitée (substrat de la P-gp). La prédiction doit être considérée comme une simple génération d'hypothèse.

**Autres prédictions du modèle (toutes de niveau L5, sans aucune preuve) :** la majorité se situe dans le spectre des maladies du motoneurone (SLA de type 22, prédisposition à la SLA, syndrome de Mills, syndrome du motoneurone inférieur de l'adulte tardif, amyotrophie monomélique, syndrome arthrogrypose létale-corne antérieure). Plusieurs doivent être interprétées avec prudence :
- La « prédisposition à la SLA » est vraisemblablement un doublon du signal SLA, et non une indication thérapeutique distincte.
- L'amyotrophie monomélique est généralement autolimitée ; le rapport bénéfice/risque d'un inhibiteur de MEK toxique est défavorable.
- Pour le syndrome trichomégalie-dégénérescence rétinienne pigmentaire-nanisme, les inhibiteurs de MEK sont associés à une toxicité rétinienne (rétinopathie séreuse), ce qui constitue une préoccupation de sécurité.
- Pour la polymicrogyrie parasagittale pariéto-occipitale bilatérale et la dysplasie spondylométaphysaire axiale, aucun lien mécanistique n'est étayé.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65045274 | COTELLIC 20 mg, comprimé pelliculé (ROCHE REGISTRATION, Allemagne) | Comprimé pelliculé | Non renseignée (AMM annulée) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de MEK1/2) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Fonction hépatique, CPK (risque de rhabdomyolyse), examen ophtalmologique (rétinopathie), toxicité cutanée et digestive |
| Protection de Manipulation | Veuillez consulter la notice |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 266 interactions ont été identifiées. Parmi celles listées dans les données compilées, les interactions de niveau **majeur** concernent : aprépitant, dexaméthasone, clarithromycine, cobicistat et samarium (153Sm) lexidronam. Des interactions de niveau modéré sont notamment rapportées avec la cimétidine, le clotrimazole, le miconazole, l'éliglustat, la métréleptine, la naltrexone, le rolapitant, la troglitazone, le déférasirox, la palifermine, le chlorure de strontium Sr-89, le fostamatinib, le ticagrélor, la quinine et l'ivacaftor.
- **Signaux de toxicité de classe (issus de l'analyse des prédictions)** : éruption cutanée, diarrhée, élévation des CPK/rhabdomyolyse et rétinopathie.

Les mises en garde et contre-indications officielles ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai clinique ni publication. La pénétration limitée dans le SNC et le profil de toxicité des inhibiteurs de MEK affaiblissent le rapport bénéfice/risque. De plus, l'AMM française est annulée, et les données de sécurité de la notice manquent (point bloquant).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications) afin de permettre le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Études précliniques de la voie MAPK/ERK dans des modèles de SLA, avec évaluation de l'exposition cérébrale du cobimétinib
- Revue systématique de la littérature et des registres d'essais sur les inhibiteurs de MEK dans les maladies du motoneurone
- Clarifier la pertinence de l'AMM annulée (disponibilité du produit en France)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

