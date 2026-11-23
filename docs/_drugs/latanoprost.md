---
layout: default
title: Latanoprost
parent: Prédiction du modèle uniquement (L5)
nav_order: 439
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "LATANOPROST"
predicted_indications: ["visceral calciphylaxis", "hypotrichosis simplex of the scalp", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "congenital hypotrichosis milia", "angiodysplasia of stomach", "blue toe syndrome", "lymphangiectasis"]
description: "Latanoprost : nouvelle indication prédite, Visceral calciphylaxis (niveau de preuve L5). En France, AMM dans la BDPM : au moins 20"
---

# Latanoprost
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

## Latanoprost: Visceral calciphylaxis
{: .text-alpha }

## Résumé en Une Phrase

Latanoprost est un analogue de la prostaglandine F2-alpha, initialement utilisé pour traiter le glaucome à angle ouvert et l'hypertension oculaire.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Visceral calciphylaxis |
| Score de Prédiction TxGNN | 0.9983 |
| Niveau de Preuve | L5 (prédiction du modèle uniquement, aucune étude réelle) |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 19) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

*Remarque : les données compilées classent cette piste en niveau L4 (question de recherche), en raison de la plausibilité mécanistique. En l'absence de toute étude de mécanisme, d'essai ou de publication fournie, le niveau L5 est retenu ici selon les règles de détermination.*

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Latanoprost (traduction non officielle) : « Le latanoprost est un analogue de la prostaglandine F 2α dont on pense qu'il réduit la pression intraoculaire (PIO) en augmentant l'écoulement de l'humeur aqueuse. Des études chez l'animal et chez l'homme suggèrent que le principal mécanisme d'action est une augmentation de l'écoulement uvéoscléral. » Texte original en anglais : "Latanoprost is a prostaglandin F 2α analogue that is believed to reduce the intraocular pressure (IOP) by increasing the outflow of aqueous humor. Studies in animals and man suggest that the main mechanism of action is increased uveoscleral outflow." ([DailyMed: Xelpros (latanoprost) prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=34ad5cf6-4df0-4104-bddd-4c7631133ded), version du 2025-12-18 ; consulté le 2026-11-19). D'après les connaissances pharmacologiques établies, le latanoprost est un analogue de la prostaglandine F2-alpha qui abaisse la pression intraoculaire (PIO) en augmentant l'écoulement uvéoscléral de l'humeur aqueuse.

Le glaucome héréditaire primaire (congénital ou juvénile) se caractérise par une PIO élevée liée à une dysgénésie des voies d'écoulement. Un médicament qui abaisse la PIO est donc biologiquement plausible dans cette situation.

Il faut toutefois rester prudent : l'indication d'origine (glaucome à angle ouvert) est très proche, de sorte qu'il s'agit plutôt d'une extension au sein de la famille des glaucomes que d'un véritable repositionnement. L'efficacité pourrait être limitée en cas de dysgénésie du trabéculum, et les données pédiatriques sont contrastées.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Le texte d'indication approuvée n'est pas renseigné dans les données compilées. Principales AMM (5 sur 20) :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 60047271 | XALATAN 50 microgrammes/mL | Collyre en solution | Active |
| 63781007 | XALACOM 50 µg/mL + 5 mg/mL (latanoprost/timolol) | Collyre en solution | Active |
| 64928570 | LATANOPROST BIOGARAN 0,005 % | Collyre en solution | Annulée |
| 60643442 | LATANOPROST ZENTIVA 0,005 % | Collyre en solution | Active |
| 64224662 | ROCLANDA 50 µg/mL + 200 µg/mL (latanoprost/nétarsudil) | Collyre en solution | Active |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : uvéite, maladie de l'iris, maladie du corps ciliaire, panuvéite, œdème maculaire rétinien, œdème maculaire cystoïde, iritis, conjonctivite (dont conjonctivite contagieuse aiguë).
- **Interactions médicamenteuses** : 100 interactions recensées, mais leur niveau de gravité est classé « inconnu ». Parmi les médicaments concernés figurent le calcitriol, le glimépiride, la doxycycline, l'atropine, la metformine, la morphine, la prednisone, la simvastatine et la triamcinolone. Ces données n'ont pas de valeur clinique en l'absence de niveau de gravité.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

---

## Autres Prédictions Examinées

Les autres pistes prédites présentent des scores TxGNN élevés (0,9967 à 0,9983) mais aucune preuve clinique :

| Indication Prédite | Niveau | Évaluation |
|------|------|------|
| Hypotrichose simple du cuir chevelu | L4 | Question de recherche : les analogues de prostaglandines prolongent la phase anagène, mais la cause génétique pourrait ne pas répondre à ce signal |
| Calciphylaxie viscérale | L5 | Hold : aucun lien mécanistique clair |
| Syndromes du défilé thoracique (artériel, veineux, neurogène) | L5 | Hold : troubles de compression mécanique, aucun mécanisme plausible |
| Hypotrichose congénitale avec milia | L5 | Hold : maladie ultra-rare, lien très faible |
| Angiodysplasie de l'estomac | L5 | Hold : aucun rôle établi, risque théorique d'aggravation du saignement |
| Syndrome de l'orteil bleu | L5 | Hold : exposition systémique non pertinente avec un collyre |
| Lymphangiectasie | L5 | Hold : cible thérapeutique non établie |

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé, mais aucun essai ni aucune publication ne le soutient.
- Les données de sécurité de la notice (ANSM) manquent, ce qui bloque le passage à l'étape de dépistage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications)
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Rechercher des essais cliniques et des publications sur le latanoprost dans le glaucome congénital/juvénile, notamment pédiatriques
- Évaluer la compatibilité des voies d'administration (analyse en attente)

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Xelpros (latanoprost) prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=34ad5cf6-4df0-4104-bddd-4c7631133ded) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

