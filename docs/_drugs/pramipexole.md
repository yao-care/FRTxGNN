---
layout: default
title: Pramipexole
parent: 僅模型預測 (L5)
nav_order: 243
evidence_level: L5
indication_count: 10
---

# Pramipexole
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

# Pramipexole : De la Maladie de Parkinson au Trouble Deficitaire de l'Attention avec Hyperactivite (TDAH)

## Resume en Une Phrase

Pramipexole est un agoniste dopaminergique D2/D3, utilise a l'origine dans le traitement de la maladie de Parkinson (et du syndrome des jambes sans repos).
Le modele TxGNN predit qu'il pourrait etre efficace pour le **Trouble Deficitaire de l'Attention avec Hyperactivite (TDAH)**,
mais cette direction n'est actuellement soutenue que par **1 essai clinique de pertinence incertaine** et **9 publications**, majoritairement des rapports de cas et etudes indirectes, sans essai clinique dedie de phase avancee.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Maladie de Parkinson (et syndrome des jambes sans repos) — d'apres le contexte clinique connu ; le produit n'etant pas commercialise sur ce marche, aucune notice officielle locale n'est disponible |
| Nouvelle Indication Predite | Trouble Deficitaire de l'Attention avec Hyperactivite (TDAH) |
| Score de Prediction TxGNN | 99.998 % |
| Niveau de Preuve | L4 |
| Statut de Marche en France | ✗ Non commercialise |
| Nombre d'AMM | 0 |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action ne sont pas disponibles. Sur la base des informations connues, Pramipexole fait partie de la classe des agonistes dopaminergiques non ergotes, selectifs des recepteurs D2/D3 ; son efficacite dans la maladie de Parkinson (et le syndrome des jambes sans repos) a ete largement demontree, et mecanistiquement il pourrait, en theorie, etre applicable au TDAH.

L'hypothese dopaminergique du TDAH repose sur un deficit de transmission dopaminergique au niveau du cortex prefrontal, ce qui presente une relation directionnelle theorique avec l'action agoniste D2/D3 de pramipexole. Cependant, les traitements de reference du TDAH (methylphenidate, amphetamines) agissent en augmentant la concentration synaptique de dopamine et de noradrenaline — un mecanisme different de l'activation directe des recepteurs postsynaptiques par un agoniste comme pramipexole.

De plus, un agoniste dopaminergique peut activer preferentiellement les autorecepteurs presynaptiques a faible dose, ce qui pourrait au contraire **reduire** la liberation de dopamine plutot que de la compenser. La coherence directionnelle du mecanisme reste donc incertaine, et la prediction doit etre consideree comme une hypothese a valider plutot qu'un lien mecanistique etabli.

---

## Preuves d'Essais Cliniques

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT00558766](https://clinicaltrials.gov/study/NCT00558766) | N/A | Termine | 35 | Etude sur la signalisation de recompense au niveau du cortex moteur chez des patients atteints de la **maladie de Parkinson** (stimulation magnetique transcranienne). Le sujet reel de l'essai ne concerne pas le TDAH ; il s'agit probablement d'un appariement indirect ou errone issu du graphe de connaissances (pertinence evaluee « C »). |

---

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [22407510](https://pubmed.ncbi.nlm.nih.gov/22407510/) | 2012 | ECR | Movement Disorders | Essai multicentrique randomise controle par placebo de pramipexole dans le **syndrome de Tourette** (hypothese d'hypersensibilite dopaminergique centrale) — pas une etude sur le TDAH lui-meme |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Revue | Revue neurologique | Revue sur le syndrome des jambes sans repos (SJSR) ; mentionne les agonistes dopaminergiques comme traitement de reference, condition frequemment comorbide avec le TDAH |
| [19412489](https://pubmed.ncbi.nlm.nih.gov/19412489/) | 2006 | Revue | Neuropsychiatric Disease and Treatment | « Nouvel usage pour un ancien medicament » : potentiel de pramipexole dans le traitement du SJSR, pas du TDAH directement |
| [15540638](https://pubmed.ncbi.nlm.nih.gov/15540638/) | 2004 | Cohorte | Developmental Medicine and Child Neurology | Mouvements periodiques des jambes chez des enfants prepuberes souffrant de troubles du sommeil, certains traites par pramipexole ; lien indirect avec le TDAH via les troubles du sommeil |
| [24992083](https://pubmed.ncbi.nlm.nih.gov/24992083/) | 2014 | Cohorte | Clinical Neuropharmacology | Essai comparatif de 11 semaines chez des patients parkinsoniens somnolents (piribedil vs pramipexole vs ropinirole) sur la vigilance — hors-sujet TDAH direct |
| [37342213](https://pubmed.ncbi.nlm.nih.gov/37342213/) | 2023 | Rapport de Cas | Frontiers in Pain Research | Remission de lombalgie chronique et dysesthesie orale comorbides avec un TDAH, sous traitement combine atomoxetine + pramipexole |
| [38649244](https://pubmed.ncbi.nlm.nih.gov/38649244/) | 2024 | Rapport de Cas | BMJ Case Reports | Hypokaliemie liee a une consommation excessive de boissons cola chez un patient avec antecedent de TDAH traite entre autres par pramipexole ; aucune evaluation d'efficacite sur le TDAH |
| [24079375](https://pubmed.ncbi.nlm.nih.gov/24079375/) | 2013 | Etude Preclinique | Journal of Motor Behavior | Modele animal (rat SHR) explorant le lien entre SJSR, mouvements periodiques des jambes et TDAH — base mecanistique animale uniquement |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Etude de Mecanisme | Pharmacological Research | Etude in vitro sur l'heteromerisation des recepteurs adrenergiques alpha2A et dopaminergiques D4, pertinente pour les troubles du controle des impulsions dont le TDAH |

---

## Informations de Marche en France

Pramipexole n'est actuellement **pas commercialise** sur ce marche : aucune AMM n'est enregistree (0 licence recensee). Aucune information sur la forme pharmaceutique ou l'indication approuvee localement n'est donc disponible.

---

## Considerations de Securite

Veuillez consulter la notice pour les informations de securite.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
Le niveau de preuve actuel (L4) repose uniquement sur une hypothese mecanistique et des publications indirectes (revues sur le SJSR, rapports de cas isoles, un ECR portant en realite sur le syndrome de Tourette) ; le seul essai clinique associe concerne en fait la maladie de Parkinson et non le TDAH. De plus, la direction meme du mecanisme (agoniste presynaptique pouvant reduire la liberation de dopamine) reste debattue. Sans donnees de securite officielles disponibles, ce dossier ne peut pas franchir l'etape S1 d'evaluation de securite.

**Pour avancer, les elements suivants sont necessaires :**
- Obtenir les mises en garde et contre-indications officielles (notice/PDF), actuellement bloquantes pour l'evaluation de securite S1
- Clarifier le mecanisme d'action detaille via l'API DrugBank
- Identifier ou lancer un essai clinique dedie specifiquement au TDAH (la seule etude associee actuellement concerne la maladie de Parkinson, appariement probablement errone)
- Reevaluer manuellement la pertinence des correspondances predites afin d'ecarter les faux positifs issus du graphe de connaissances
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

