---
layout: default
title: Pembrolizumab
parent: 僅模型預測 (L5)
nav_order: 230
evidence_level: L5
indication_count: 10
---

# Pembrolizumab
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

# Pembrolizumab : De l'Immunotherapie Anti-PD-1 en Oncologie a la Fibromatose Gingivale

## Resume en Une Phrase

Pembrolizumab est un anticorps monoclonal anti-PD-1 utilise en immuno-oncologie (non commercialise en France selon les donnees recues, 0 AMM). Le modele TxGNN predit en tete de liste qu'il pourrait etre efficace pour la **Fibromatose Gingivale**, avec un score de **99.40%**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction, et l'analyse mecanistique jointe au dossier juge cette prediction non plausible.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non disponible dans les donnees recues (0 AMM en France ; d'apres la litterature attachee aux autres candidats de ce dossier, pembrolizumab est un inhibiteur de checkpoint anti-PD-1 utilise en oncologie, notamment dans le cancer bronchique non a petites cellules) |
| Nouvelle Indication Predite | Fibromatose Gingivale (fibromatosis, gingival) |
| Score de Prediction TxGNN | 99.40% |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Non commercialise |
| Nombre d'AMM | 0 |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Le champ structure de mecanisme d'action (MOA) est un manque de donnees signale dans le dossier (DG002, severite High). Neanmoins, la litterature jointe aux autres candidats de ce meme dossier decrit de facon repetee le pembrolizumab comme un anticorps monoclonal humanise IgG4-kappa qui bloque l'interaction PD-1/PD-L1, restaurant ainsi l'activite antitumorale des lymphocytes T epuises — un mecanisme d'immuno-oncologie etabli et documente dans de multiples essais de phase 3 (par exemple KEYNOTE-024, KEYNOTE-010, KEYNOTE-042 pour le CBNPC ; KEYNOTE-164 pour le cancer colorectal MSI-H ; LEAP-002 pour le carcinome hepatocellulaire).

La fibromatose gingivale, en revanche, est une hyperplasie fibreuse **benigne** du tissu conjonctif gingival, souvent induite par des medicaments (ciclosporine, phenytoine, inhibiteurs calciques) ou d'origine hereditaire. Il ne s'agit pas d'une pathologie neoplasique dependante d'un mecanisme d'echappement immunitaire, et aucune association physiopathologique connue avec l'axe PD-1/PD-L1 n'existe.

Sur cette base, le lien mecanistique est juge non plausible : la recherche cible (essais cliniques, ICTRP, PubMed) sur la paire pembrolizumab + fibromatose gingivale n'a retourne **aucun resultat** (0/0/0). Ce profil correspond typiquement a un signal artefactuel d'un modele d'embeddings comme TxGNN en l'absence de tout lien biologique direct, plutot qu'a une piste de repositionnement authentique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associe enregistre actuellement.

---

## Preuves de la Litterature

Aucune litterature associee disponible actuellement.

---

## Informations de Marche en France

Aucune AMM enregistree pour le pembrolizumab en France selon les donnees recues (statut : non commercialise, 0 licence).

---

## Cytotoxicite

Le pembrolizumab est un agent antineoplasique (inhibiteur de checkpoint immunitaire), mais il ne s'agit pas d'une chimiotherapie cytotoxique conventionnelle. Les elements ci-dessous sont issus de la litterature de securite jointe au dossier (rattachee a d'autres candidats mais portant sur le profil general du medicament).

| Element | Contenu |
|------|------|
| Classification de Cytotoxicite | Immunotherapie (inhibiteur de checkpoint anti-PD-1), non cytotoxique conventionnel |
| Risque de Myelosuppression | Faible — les inhibiteurs de PD-1 ne sont generalement pas myelosuppresseurs ; le risque dominant est celui d'evenements indesirables lies au systeme immunitaire (irAE), avec atteintes rapportees : hypophysite (PMID 30352754), atteintes neurologiques (PMID 32126176), myocardite/myosite/myasthenie ("Triple M Overlap Syndrome", PMID 39897316), syndrome de Stevens-Johnson (PMID 40210540) |
| Classification d'Emetogenicite | Faible — profil generalement peu emetisant compare a la chimiotherapie cytotoxique classique |
| Elements de Surveillance | Fonction thyroidienne et surrenalienne/hypophysaire, fonction hepatique et renale, surveillance cardiaque (troponine) en cas de symptomes, examen neurologique, examen cutane ; profil de securite agrege sur 8937 patients disponible (PMID 38295556) |
| Protection de Manipulation | Anticorps monoclonal administre en perfusion — manipulation selon les procedures standard des produits biologiques ; les mesures specifiques de protection cytotoxique (type chimiotherapie classique) ne s'appliquent pas |

---

## Considerations de Securite

Veuillez consulter la notice pour les informations de securite (donnees TFDA/DDI non disponibles dans ce dossier — voir manque de donnees bloquant ci-dessous).

---

## Autres Indications Candidates Explorees (Rang 2 a 10)

Ce dossier (candidate_id multi) a evalue 10 indications au total pour le pembrolizumab. Par transparence, voici un resume des 9 autres candidats :

| Rang | Indication | Score TxGNN | Niveau Preuve | Recommandation | Commentaire |
|------|------|------|------|------|------|
| 2 | IBM avec maladie de Paget precoce +/- demence frontotemporale | 99.37% | L5 | Hold | Maladie genetique rare (mutation VCP) sans lien avec PD-1 ; 20 refs = revues generiques sur la demence frontotemporale, aucune ne concerne le pembrolizumab (faux positif probable) |
| 3 | Hamartome pulmonaire | 99.35% | L5 | Hold | Tumeur benigne, aucune preuve |
| 4 | Carcinome du hile pulmonaire | 99.35% | L3 | Research Question | Sous-type anatomique de CBNPC, mecanisme plausible, mais les 2 seules publications rapportent des effets indesirables (hyperprogression, hypophysite/hypothyroidie) et non une efficacite ; risque d'hyperprogression a evaluer en priorite |
| 5 | Fibrome pulmonaire | 99.34% | L5 | Hold | Tumeur benigne, aucune preuve |
| 6 | Neoplasme pulmonaire benin | 99.32% | L4 | Hold | Anomalie probable d'ontologie de maladie : toute la litterature jointe (KEYNOTE-024, KEYNOTE-010...) concerne le CBNPC malin, deja indication approuvee existante — ne pas soumettre comme nouvelle indication sans correction du mappage |
| 7 | Ovarioleucodystrophie | 99.32% | L5 | Hold | Entite de maladie non identifiable, probable erreur d'ontologie |
| 8 | Tumeur germinale pulmonaire | 99.29% | L3 | Research Question | Mecanisme plausible mais 50 essais = paniers pan-tumeurs solides non specifiques ; expression PD-L1 generalement faible dans les tumeurs germinales, preuve directe insuffisante |
| 9 | Neoplasme du sillon pulmonaire (tumeur de Pancoast) | 99.29% | L4 | Research Question | Sous-type anatomique de CBNPC, mecanisme deja valide par ailleurs, mais 0 essai / 0 publication specifique — extrapolation uniquement |
| 10 | Syndrome leucomelanodermie-infantilisme-deficience intellectuelle-hypodontie-hypotrichose | 99.28% | L5 | Hold | Syndrome genetique ultra-rare, litterature jointe sans rapport (indications oncologiques etablies et irAE du pembrolizumab) |

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
Le score TxGNN le plus eleve du dossier (99.40%) porte sur une pathologie benigne, non neoplasique, sans lien physiopathologique connu avec l'axe PD-1/PD-L1, et aucun essai clinique ni publication ne l'appuie (0/0). Il s'agit vraisemblablement d'un artefact du modele plutot que d'un signal de repositionnement authentique.

**Pour avancer, les elements suivants sont necessaires :**
- Obtenir le texte des mises en garde/contre-indications TFDA (DG001, severite Blocking) — indispensable avant toute evaluation de securite S1
- Completer les donnees structurees de mecanisme d'action via l'API DrugBank (DG002, severite High)
- Si une piste doit etre priorisee malgre tout, se tourner plutot vers les candidats rang 4 (carcinome du hile pulmonaire) et rang 9 (tumeur de Pancoast), qui reposent sur un mecanisme deja valide (CBNPC), en commencant par une revue de securite dediee (signal d'hyperprogression rapporte au rang 4) avant toute etude d'efficacite
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

