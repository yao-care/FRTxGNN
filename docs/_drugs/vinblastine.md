---
layout: default
title: Vinblastine
parent: Preuves modérées (L3-L4)
nav_order: 813
evidence_level: L4
indication_count: 10
---

# Vinblastine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **10** 
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

# Vinblastine : Du Lymphome de Hodgkin au Rhabdomyosarcome

## Resume en Une Phrase

Vinblastine est un alcaloide de la pervenche (vinca), initialement utilise pour traiter des lymphomes (maladie de Hodgkin, lymphomes non hodgkiniens, lymphome a cellules du manteau), le mycosis fongoide et l'histiocytose a cellules de Langerhans.
Le modele TxGNN predit qu'il pourrait etre efficace pour le **rhabdomyosarcome**, mais **aucun essai clinique** n'est enregistre et la litterature disponible se limite a des **cas cliniques, des etudes precliniques et des revues** (7 publications retenues).

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non precisee dans les donnees reglementaires francaises (texte d'indication vide). D'apres le graphe de connaissances : lymphome de Hodgkin, lymphomes non hodgkiniens, mycosis fongoide, histiocytose a cellules de Langerhans |
| Nouvelle Indication Predite | Rhabdomyosarcome |
| Score de Prediction TxGNN | 99.86% |
| Niveau de Preuve | L4 |
| Statut de Marche en France | Autorisation annulee uniquement |
| Nombre d'AMM | 1 (annulee) |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action ne sont pas disponibles dans les donnees compilees pour ce rapport. D'apres les connaissances pharmacologiques generales, la vinblastine est un alcaloide de la pervenche qui se lie a la tubuline et inhibe la polymerisation des microtubules, ce qui provoque un arret de la mitose. Les cellules a prolifération rapide y sont donc potentiellement sensibles.

Les indications d'origine (lymphomes, histiocytose) sont des hemopathies a forte activite proliferative, tandis que le rhabdomyosarcome est un sarcome des tissus mous, frequent chez l'enfant. Les alcaloides de la pervenche, principalement la vincristine, font deja partie des schemas standards du rhabdomyosarcome. Un mecanisme antimitotique commun rend donc la prediction plausible.

Les donnees indirectes vont dans ce sens : un schema metronomique pediatrique a quatre medicaments et une etude de letalite synthetique entre inhibiteurs de PLK1 et agents destabilisant les microtubules (modeles precliniques de rhabdomyosarcome). Ces elements ne constituent pas une preuve clinique directe pour la vinblastine seule.

## Preuves d'Essais Cliniques

Aucun essai clinique associe enregistre actuellement.

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [38050209](https://pubmed.ncbi.nlm.nih.gov/38050209/) | 2023 | Cas clinique/Revue | Medicine | Rhabdomyosarcome perianal de l'adulte : reponse partielle apres nivolumab, dacarbazine, cisplatine et vinblastine, puis chirurgie |
| [41216926](https://pubmed.ncbi.nlm.nih.gov/41216926/) | 2026 | Cohorte (indirecte) | Pediatric Blood & Cancer | Essais CWS-96 et CWS-2002P sur les sarcomes des tissus mous non rhabdomyosarcomateux de l'enfant ; donnees indirectes |
| [22156656](https://pubmed.ncbi.nlm.nih.gov/22156656/) | 2011 | Etude pilote | Oncotarget | Schema metronomique pediatrique a quatre medicaments |
| [2451411](https://pubmed.ncbi.nlm.nih.gov/2451411/) | 1987 | Cas clinique/Revue | Hinyokika Kiyo | Rhabdomyosarcome refractaire de la prostate : reduction rapide de la masse pelvienne avec cisplatine, vinblastine et pepleomycine |
| [26024389](https://pubmed.ncbi.nlm.nih.gov/26024389/) | 2015 | Preclinique | Cell Death & Differentiation | Letalite synthetique entre inhibiteurs de PLK1 et agents destabilisant les microtubules dans des modeles de rhabdomyosarcome |
| [3329524](https://pubmed.ncbi.nlm.nih.gov/3329524/) | 1987 | Preclinique/Mecanistique | Anti-Cancer Drug Design | Selectivite therapeutique des alcaloides de la pervenche sur des xenogreffes de rhabdomyosarcome humain chez la souris |
| [14328283](https://pubmed.ncbi.nlm.nih.gov/14328283/) | 1965 | Revue (historique) | British Journal of Clinical Practice | Chimiotherapie des tumeurs de l'enfant (pas de resume disponible) |

Pour les sous-types predits suivants, la litterature est tres limitee : le rhabdomyosarcome embryonnaire de la prostate (rang 5) ne repose que sur deux cas cliniques des annees 1980 ([2417460](https://pubmed.ncbi.nlm.nih.gov/2417460/), [2444085](https://pubmed.ncbi.nlm.nih.gov/2444085/)), dans lesquels la vinblastine etait integree a des associations, et sa contribution propre ne peut etre isolee. Les autres sous-types (botryoide du vagin, parameningé, voies biliaires) ne disposent d'aucune donnee.

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 68875332 | VELBE 10 mg, poudre pour solution injectable I.V. (EG LABO - Laboratoires Eurogenerics) | Poudre pour solution injectable | Non renseignee (AMM annulee) |

## Cytotoxicite

| Element | Contenu |
|------|------|
| Classification de Cytotoxicite | Cytotoxique conventionnel (alcaloide de la pervenche, poison du fuseau) |
| Risque de Myelosuppression | Eleve (la neutropenie, l'agranulocytose et la thrombocytopenie figurent parmi les contre-indications du graphe de connaissances) |
| Classification d'Emetogenicite | Faible a moyenne (d'apres la classe du medicament) |
| Elements de Surveillance | NFS avec formule (neutrophiles, plaquettes), fonction hepatique (bilirubine), signes de neuropathie peripherique, fonction respiratoire |
| Protection de Manipulation | Doit suivre les reglementations de manipulation des medicaments cytotoxiques |

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hepatique, thrombocytopenie, neutropenie, agranulocytose, neuropathie peripherique et maladies du systeme nerveux peripherique, hyperbilirubinemie (dont syndrome de Gilbert), maladies pulmonaires, ischemie myocardique et maladie coronarienne, infections (dont mycoses et dermatophytoses), troubles anxieux et nevrotiques, dysthymie, hyperuricemie.
- **Interactions medicamenteuses** : 371 interactions recensees. Interaction **majeure** avec la clarithromycine. Interactions **moderees** notamment avec l'aprepitant, la dexamethasone, le metronidazole, le miconazole, le rolapitant, la rosuvastatine, la simvastatine, le tinidazole, l'eliglustat, le phenylbutyrate de glycerol et la troglitazone. Interaction **mineure** avec la levofloxacine.
- Les mises en garde et contre-indications issues de la notice ne sont pas disponibles : veuillez consulter la notice pour les informations de securite.
- Dans la litterature, un cas d'ileus severe a ete rapporte avec une perfusion de cisplatine et de vinblastine (neuroblastome).

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prediction est tres bien classee par le modele (99.86%), mais les preuves restent de niveau L4 : aucun essai enregistre, uniquement des cas cliniques anciens ou recents en association, et des etudes precliniques.
- La seule AMM francaise est annulee, et les donnees de securite de la notice sont absentes, ce qui bloque le passage a un criblage de securite.

**Pour avancer, les elements suivants sont necessaires :**
- Recuperer et analyser la notice (mises en garde et contre-indications) aupres de l'ANSM
- Obtenir les donnees detaillees sur le mecanisme d'action (DrugBank)
- Rechercher des essais cliniques pertinents (rhabdomyosarcome, y compris pediatriques) et des donnees comparant la vinblastine a la vincristine, deja etablie dans cette indication
- Evaluer la disponibilite actuelle du produit en France, compte tenu de l'annulation de l'AMM
- Etablir un plan de surveillance hematologique, hepatique et neurologique
- Pour les autres predictions (sous-types de rhabdomyosarcome, foie, leucemie monocytaire, neuroblastome), les preuves sont insuffisantes ou indirectes ; la leucemie monocytaire (niveau L3) repose sur des series anciennes des annees 1970 et ne justifie, a ce stade, qu'une question de recherche.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

