---
layout: default
title: Fosamprenavir
parent: Preuves modérées (L3-L4)
nav_order: 347
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-14
description: "Fosamprenavir : nouvelle indication prédite, Syndrome d'immunodéficience acquise féline (niveau de preuve L4). Indication d'origine : Infection par le VIH, SIDA"
---

# Fosamprenavir
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **7** 
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

# Fosamprénavir : Du VIH/SIDA au Syndrome d'immunodéficience acquise féline

## Résumé en Une Phrase

Le fosamprénavir est une prodrogue de l'amprénavir, un inhibiteur de la protéase du VIH-1, initialement utilisé pour le traitement de l'infection par le VIH et du SIDA.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome d'immunodéficience acquise féline** (FIV), mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection par le VIH, SIDA (d'après le graphe de connaissances ; aucune AMM française disponible) |
| Nouvelle Indication Prédite | Syndrome d'immunodéficience acquise féline |
| Score de Prédiction TxGNN | 99,88 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, le fosamprénavir est la prodrogue de l'amprénavir, un inhibiteur de la protéase du VIH-1. Son efficacité dans l'infection par le VIH est établie, et il pourrait être mécanistiquement applicable à d'autres lentivirus.

Le virus de l'immunodéficience féline (FIV) est un lentivirus apparenté au VIH, et sa protéase présente une similarité structurale avec celle du VIH-1. Cela fournit un argument mécanistique de départ. Toutefois, la protéase du FIV diffère de celle du VIH-1 par sa spécificité de substrat et sa sensibilité aux inhibiteurs, et les inhibiteurs de la classe de l'amprénavir sont connus pour y être moins efficaces.

Le score élevé du modèle reflète vraisemblablement la proximité du FIV avec le VIH dans le graphe de connaissances, et non une preuve clinique. Il s'agit essentiellement d'une reformulation de l'indication anti-VIH d'origine dans un contexte vétérinaire, de valeur limitée comme opportunité de repositionnement chez l'humain.

### Autres prédictions du modèle

| Rang | Maladie prédite | Score TxGNN | Niveau de preuve | Commentaire |
|------|------|------|------|------|
| 2 | Infection par le virus de l'immunodéficience simienne (VIS) | 99,88 % | L4 | Lentivirus de primates très proche du VIH ; plausible mécanistiquement, mais surtout utile en recherche préclinique (modèle macaque) |
| 3 | Trouble neurodéveloppemental avec démarche ataxique, absence de parole et diminution de la substance blanche corticale | 99,86 % | L5 | Aucun lien mécanistique identifié ; pénétration cérébrale faible |
| 4 | Maladie fibrokystique du sein | 99,57 % | L5 | Aucun lien mécanistique établi |
| 5 | Adénose apocrine du sein | 99,34 % | L5 | Probablement un artefact de voisinage dans le graphe |
| 6 | Adénose à canaux dilatés du sein | 99,34 % | L5 | Score identique au précédent : signal lié à l'ontologie, non au médicament |
| 7 | Dysplasie mammaire bénigne | 99,10 % | L5 | Terme proche de la maladie fibrokystique ; même regroupement ontologique |

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
- Toutes les indications prédites reposent uniquement sur des scores computationnels, sans essai clinique ni publication. Pour la première, le lien mécanistique est indirect et la protéase du FIV est moins sensible à cette classe d'inhibiteurs. Les autres prédictions (troubles neurodéveloppementaux, pathologies bénignes du sein) n'ont pas de fondement mécanistique identifié. De plus, le médicament n'est pas commercialisé en France et présente une charge d'interactions élevée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice ANSM (mises en garde et contre-indications) : lacune bloquante pour tout passage à l'évaluation de sécurité
- Données détaillées sur le mécanisme d'action (MOA), à obtenir via DrugBank
- Données précliniques d'activité de l'amprénavir sur la protéase du FIV/VIS, si l'on souhaite poursuivre ces pistes
- Confirmation de la pertinence d'un usage vétérinaire ou préclinique, car ces indications offrent peu de valeur pour un repositionnement chez l'humain
- Définition d'une hypothèse biologique explicite avant toute exploration des indications neurodéveloppementale et mammaires
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

