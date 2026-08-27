---
layout: default
title: Iodixanol
parent: 僅模型預測 (L5)
nav_order: 150
evidence_level: L5
indication_count: 3
---

# Iodixanol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Iodixanol : D'Agent de Contraste Radiologique (Indication Originale Non Documentee) a l'Arthrose / Polyarthrite Rhumatoide (Predictions Non Confirmees)

## Resume en Une Phrase

Iodixanol est un agent de contraste radiologique iode non ionique ; aucune indication d'origine approuvee n'est enregistree a Taiwan (le medicament n'y est pas commercialise). Le modele TxGNN predit un lien avec l'**arthrose** et deux entites apparentees (**susceptibilite a l'arthrose**, **polyarthrite rhumatoide**), mais ces trois predictions ne sont soutenues par **aucun essai clinique** et seulement **8 publications au total**, dont l'analyse indique qu'elles decrivent l'usage d'iodixanol comme outil d'imagerie du cartilage/de l'articulation, et non comme traitement.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non disponible (aucune AMM enregistree ; medicament non commercialise a Taiwan ; MOA officiel en Data Gap) |
| Nouvelle Indication Predite | Susceptibilite a l'Arthrose (*Osteoarthritis Susceptibility*) — voir aussi 2 entites apparentees ci-dessous |
| Score de Prediction TxGNN | 99,16 % (rang 5595) |
| Niveau de Preuve | L5 (prediction de modele uniquement, aucune etude clinique reelle) |
| Statut de Marche | ✗ Non commercialise |
| Nombre d'AMM | 0 |
| Decision Recommandee | Hold |

**Note sur les predictions apparentees :** le modele TxGNN a genere trois entites tres proches pour ce candidat, avec des scores quasi identiques :

| Rang | Indication Predite | Score TxGNN | Essais Cliniques | Litterature |
|------|------|------|------|------|
| 1 | Susceptibilite a l'Arthrose | 99,16 % | 0 | 0 |
| 2 | Arthrose (Osteoarthritis) | 99,07 % | 0 | 7 |
| 3 | Polyarthrite Rhumatoide | 99,00 % | 0 | 1 |

L'analyse fournie dans le dossier de preuves indique que ces trois entites representent tres probablement **une seule et meme projection biaisee** repartie sur des noeuds d'ontologie de maladies distincts, plutot que trois signaux independants.

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Les donnees detaillees sur le mecanisme d'action officiel d'iodixanol ne sont pas disponibles dans DrugBank (Data Gap). Sur la base des elements presents dans le dossier d'evaluation, iodixanol est un **agent de contraste radiologique iode non ionique**, dont l'action pharmacologique se limite a fournir un contraste radiographique lors d'examens d'imagerie (rayons X, tomodensitometrie). Il ne possede pas de mecanisme anti-inflammatoire, chondroprotecteur ou immunomodulateur connu.

L'examen des 8 publications associees montre qu'il s'agit systematiquement d'etudes methodologiques ou biomecaniques utilisant iodixanol (ou la molecule apparentee iohexol) **comme outil d'imagerie** pour etudier le cartilage articulaire, le transport de solutes a l'interface os-cartilage, ou la fonction du cartilage dans des modeles d'arthrose — et non comme agent therapeutique teste chez des patients atteints d'arthrose ou de polyarthrite rhumatoide. La seule publication liee a la polyarthrite rhumatoide est un rapport de cas de desensibilisation a une reaction allergique au produit de contraste chez une patiente arthritique venant subir un examen d'imagerie, ce qui reflete une co-occurrence de population (patients arthritiques necessitant une imagerie) plutot qu'un lien de traitement.

En consequence, le score TxGNN eleve (~99 %) reflete tres vraisemblablement un **biais de co-occurrence** dans la litterature (« iodixanol utilise pour imager l'arthrose » confondu avec « iodixanol traite l'arthrose »), plutot qu'une relation pharmacologique reelle. Aucun element du dossier ne permet a ce stade de justifier une hypothese mecanistique credible reliant iodixanol a l'arthrose ou a la polyarthrite rhumatoide.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associe enregistre actuellement (0 essai pour les trois indications predites : susceptibilite a l'arthrose, arthrose, polyarthrite rhumatoide).

---

## Preuves de la Litterature

*Litterature combinee pour les indications apparentees "Arthrose" et "Polyarthrite Rhumatoide" (aucune publication pour "Susceptibilite a l'Arthrose").*

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Modelisation par elements finis | Journal of Biomechanics | Utilise iodixanol (~1550 Da) comme traceur de diffusion neutre pour etudier la permeabilite de l'interface os-cartilage dans des modeles equins/humains d'arthrose (outil d'imagerie, non traitement) |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Modelisation par elements finis | Journal of Biomechanics | Modele biphasique de transport de solutes neutres a l'interface osteo-chondrale, utilisant un agent de contraste CT pour etudier la progression de l'arthrose |
| [28518064](https://pubmed.ncbi.nlm.nih.gov/28518064/) | 2017 | Modelisation par elements finis | Journal of Visualized Experiments (JoVE) | Protocole experimental/EF pour etudier le transport de solutes neutres et charges a travers le cartilage articulaire dans le contexte de l'arthrose |
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Methode/Imagerie | Annals of Biomedical Engineering | Agent de double contraste (nanoparticule + moleculaire) en CT a comptage de photons pour evaluer la sante du cartilage articulaire |
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Methode/Imagerie | Annals of Biomedical Engineering | Imagerie de diffusion de nanoparticules par CT pour caracteriser la fonction du cartilage |
| [30145230](https://pubmed.ncbi.nlm.nih.gov/30145230/) | 2018 | Science fondamentale (ex vivo) | Osteoarthritis and Cartilage | Etude ex vivo sur la rigidite du cartilage condylien mandibulaire chez le cheval avec le vieillissement (utilisation d'agent de contraste pour l'imagerie) |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | In vitro | Journal of Experimental Orthopaedics | Les agents de contraste iodes n'influencent pas la fonction du plasma riche en plaquettes (PRP) a un stade precoce in vitro (etude de securite d'usage combine, non therapeutique) |
| [36628042](https://pubmed.ncbi.nlm.nih.gov/36628042/) | 2022 | Rapport de cas | Cureus | Desensibilisation reussie a l'iohexol (produit de contraste) chez une patiente avec amylose secondaire a une polyarthrite rhumatoide, avant angioplastie — cas de tolerance a l'imagerie, non lie a un effet therapeutique sur la PR |

**Constat cle :** l'ensemble de ces publications concerne l'usage d'iodixanol/iohexol **comme outil d'imagerie ou de diagnostic**, jamais comme intervention therapeutique testee contre l'arthrose ou la polyarthrite rhumatoide.

---

## Considerations de Securite

Veuillez consulter la notice pour les informations de securite.

*(Mises en garde, contre-indications et interactions medicamenteuses ne sont pas disponibles dans les sources consultees a ce jour ; le dossier signale ce point comme un ecart bloquant — DG001 — empechant l'entree en evaluation de securite S1.)*

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- Aucune des trois entites de maladie predites (susceptibilite a l'arthrose, arthrose, polyarthrite rhumatoide) ne dispose d'essai clinique, et l'analyse mecanistique disponible juge le lien pharmacologique non plausible — la litterature existante documente un usage d'iodixanol comme outil d'imagerie, pas comme traitement.
- Le medicament n'est pas commercialise a Taiwan (0 AMM), et les donnees de securite critiques (mises en garde, contre-indications) sont totalement manquantes (ecart bloquant DG001), ce qui empeche toute progression vers une evaluation de securite S1.

**Pour avancer, les elements suivants sont necessaires :**
- Obtenir le notice/RCP officiel (TFDA ou equivalent) pour lever l'ecart bloquant DG001 (mises en garde et contre-indications)
- Obtenir les donnees de mecanisme d'action formelles via l'API DrugBank (DG002)
- Clarifier aupres du modele TxGNN si les trois entites "arthrose / susceptibilite a l'arthrose / polyarthrite rhumatoide" doivent etre fusionnees ou filtrees comme artefact de biais de co-occurrence lie a l'usage d'iodixanol comme agent d'imagerie plutot que comme signal de repositionnement therapeutique authentique
- En l'absence de nouvelle preuve therapeutique (essai clinique ou etude mecanistique dediee), ne pas faire progresser ce candidat au-dela du stade S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

