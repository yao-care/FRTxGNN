---
layout: default
title: Enoxaparin
parent: Prédiction du modèle uniquement (L5)
nav_order: 283
evidence_level: L5
indication_count: 1
---

# Enoxaparin
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

# Énoxaparine : De l'embolie pulmonaire à la thrombophilie par déficit en protéine C (autosomique récessif)

## Résumé en Une Phrase

L'énoxaparine est une héparine de bas poids moléculaire, initialement utilisée dans la prise en charge de l'embolie pulmonaire, de la coagulation intravasculaire disséminée (CIVD) et du purpura fulminans.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **thrombophilie due à un déficit en protéine C (autosomique récessif)**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction issue du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Embolie pulmonaire, coagulation intravasculaire disséminée, purpura fulminans (indications issues du graphe de connaissances, le texte des indications de l'AMM n'étant pas renseigné) |
| Nouvelle Indication Prédite | Thrombophilie due à un déficit en protéine C, autosomique récessif |
| Score de Prédiction TxGNN | 99,58 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances pharmacologiques générales, l'énoxaparine potentialise l'inhibition par l'antithrombine du facteur Xa (et, dans une moindre mesure, de la thrombine). Ce mécanisme n'a pas pu être vérifié à partir des données fournies.

Dans le déficit sévère congénital en protéine C, la perte de l'activité anticoagulante de cette protéine entraîne une génération incontrôlée de thrombine, source de thromboses et de purpura fulminans. Un anticoagulant agissant sur la cascade de coagulation pourrait donc, en théorie, compenser en partie ce déficit.

Les indications d'origine (purpura fulminans, purpura fulminans acquis, CIVD, embolie pulmonaire) partagent une physiopathologie proche : défaillance de la voie de la protéine C et thrombose microvasculaire ou veineuse. Cela explique probablement le score élevé du modèle. Ce score reste toutefois une prédiction fondée sur le graphe, sans confirmation clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 20 AMM recensées sont toutes annulées ; aucune n'est actuellement valide. Le texte des indications approuvées n'est pas renseigné. Les 5 premières AMM sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67464342 | LOVENOX 8 000 UI (80 mg)/0,8 ml | Solution injectable en seringue préremplie | Non renseignée |
| 67759517 | ENOXAPARINE ARROW 2 000 UI (20 mg)/0,2 mL | Solution injectable en seringue préremplie | Non renseignée |
| 63601263 | ENOXAPARINE EG 4 000 UI (40 mg)/0,4 mL | Solution injectable en seringue préremplie | Non renseignée |
| 69247501 | INHIXA 2 000 UI (20 mg)/0,2 mL | Solution injectable en seringue préremplie | Non renseignée |
| 63009219 | ENOXAPARINE VENIPHARM 6 000 UI (60 mg)/0,6 mL | Solution injectable en seringue préremplie | Non renseignée |

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées ; veuillez consulter la notice pour ces informations.

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique, thrombopénie, thrombopénie induite par l'héparine, maladies hémorragiques et troubles de la coagulation (dont l'hémophilie, la thrombasthénie de Glanzmann et les anomalies qualitatives des plaquettes), hémorragie intracrânienne ou intracérébrale, décollement placentaire, ulcère gastroduodénal actif, endocardite infectieuse (dont l'endocardite bactérienne subaiguë), rétinopathies (diabétique, hypertensive), maladies inflammatoires de l'intestin (dont la rectocolite hémorragique), maladies des voies biliaires, ictère obstructif, déficit en antithrombine III, ostéoporose (dont post-ménopausique) et artériosclérose oblitérante.
- **Interactions médicamenteuses** : 174 interactions recensées. Parmi les principales, de niveau majeur : acide acétylsalicylique, ibuprofène, kétorolac, abciximab, alteplase, acalabrutinib, déférasirox, trastuzumab emtansine, ibritumomab tiuxétan et tositumomab (dont I-131). Des interactions de niveau modéré concernent notamment la fenfluramine, la dexfenfluramine, la sibutramine, le sugammadex, l'aliskiren, les iodures I-123 et I-131, le diclofénac topique et le kétorolac ophtalmique.

Le risque hémorragique inhérent à un anticoagulant, ainsi que ces contre-indications, doivent être évalués avec soin chez les patients atteints d'un déficit sévère en protéine C.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé et une plausibilité biologique existe, mais la prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. De plus, toutes les AMM françaises sont annulées et les données de sécurité de la notice sont absentes, ce qui empêche l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), point bloquant.
- Obtenir les données détaillées du mécanisme d'action (DrugBank).
- Réaliser une revue systématique de la littérature (séries de cas, recommandations sur le déficit congénital en protéine C et le purpura fulminans néonatal).
- Vérifier la situation réglementaire : l'annulation des 20 AMM et l'éventuelle disponibilité de l'énoxaparine sous d'autres autorisations.
- Évaluer la compatibilité des voies d'administration et la similarité avec les indications d'origine (actuellement en attente).
- Définir un plan de surveillance hémorragique et plaquettaire pour cette population.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

