---
layout: default
title: Cladribine
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 7
---

# Cladribine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Cladribine : De la Leucémie à Tricholeucocytes au Rhabdomyosarcome Embryonnaire Paraméningé

## Résumé en Une Phrase

Cladribine (2-chlorodéoxyadénosine, 2-CdA) est un analogue nucléosidique purinique cytotoxique, principalement utilisé dans le traitement de la leucémie à tricholeucocytes (*hairy cell leukemia*) et, plus récemment, de la sclérose en plaques récurrente-rémittente.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Rhabdomyosarcome Embryonnaire Paraméningé** (*parameningeal embryonal rhabdomyosarcoma*),
avec **0 essai clinique** et **0 publication** soutenant directement cette direction — la prédiction repose uniquement sur la structure du graphe de connaissances biomédicales.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Leucémie à tricholeucocytes (*hairy cell leukemia*) |
| Nouvelle Indication Prédite | Rhabdomyosarcome Embryonnaire Paraméningé |
| Score de Prédiction TxGNN | 99,77 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce pack d'évidences. Sur la base des informations connues dans la littérature scientifique, cladribine est un analogue nucléosidique purinique résistant à la désamination par l'adénosine déaminase (ADA). Il est activé intracellullairement par la déoxycytidine kinase (DCK) en son triphosphate actif (2-CdATP), qui s'incorpore dans l'ADN pour provoquer des cassures de brins, et inhibe simultanément la ribonucléotide réductase. Cette double action le rend cytotoxique aussi bien pour les cellules en division que pour celles en phase de repos — caractéristique rare qui explique son efficacité dans des hémopathies à cellules quiescentes comme la leucémie à tricholeucocytes.

La connexion hypothétique avec le rhabdomyosarcome (RMS) repose sur l'observation que certaines lignées cellulaires de RMS présentent un rapport DCK/5'-nucléotidase (5'-NT) élevé, ce qui pourrait théoriquement favoriser l'accumulation intracellulaire de 2-CdATP et conférer une sensibilité au médicament. Le rhabdomyosarcome embryonnaire paraméningé est une tumeur pédiatrique des tissus mous d'origine musculaire squelettique dont le traitement standard reste le protocole VAC/VDC-IE (vincristine, actinomycine D, cyclophosphamide en alternance avec ifosfamide et étoposide). Aucun analogue nucléosidique purinique n'est actuellement inclus dans les référentiels thérapeutiques de cette indication.

La haute prédiction TxGNN (score 99,77 %, rang 2 155 global) découle principalement de la connectivité structurelle partagée entre les nœuds du graphe de connaissances au niveau de l'ontologie des maladies du RMS, et non d'une preuve clinique ou translationelle directe. En l'absence totale de données d'essais cliniques ou de publications ciblées, cette prédiction doit être considérée comme une piste de recherche préliminaire à valider en contexte préclinique avant toute considération clinique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour cette indication.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour cette indication.

---

## Cytotoxicité

| Élément | Contenu |
|---|---|
| Classification de Cytotoxicité | Cytotoxique conventionnel (classe : analogue nucléosidique purinique / antinéoplasique) |
| Risque de Myélosuppression | **Élevé** — neutropénie, thrombocytopénie et anémie sévères et prolongées sont des effets attendus ; immunosuppression prolongée avec risque accru d'infections opportunistes (dont Pneumocystis jirovecii) |
| Classification d'Émétogénicité | Faible à modérée |
| Éléments de Surveillance | NFS avec différentielle (hebdomadaire en début de traitement), bilan hépatique et rénal, surveillance infectieuse (fièvre, CD4 si traitement prolongé), bilan immunologique |
| Protection de Manipulation | Manipulation obligatoire selon les réglementations des médicaments cytotoxiques ; préparation sous hotte à flux laminaire vertical ; équipements de protection individuelle requis |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

> Les données de sécurité spécifiques (mises en garde, contre-indications, interactions médicamenteuses) n'étaient pas disponibles dans ce pack d'évidences. Une consultation directe de la notice du produit ou des fiches DrugBank et Vidal est indispensable avant toute utilisation ou évaluation clinique.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction TxGNN repose exclusivement sur la structure du graphe de connaissances (niveau L5), sans aucun essai clinique ni publication scientifique soutenant l'usage de cladribine dans le rhabdomyosarcome embryonnaire paraméningé. Le traitement standard de cette tumeur pédiatrique est bien établi autour des protocoles VAC/VDC-IE, sans recours aux analogues puriniques. Par ailleurs, cladribine n'est pas commercialisé en France (0 AMM), ce qui constitue un obstacle réglementaire supplémentaire.

**Pour avancer, les éléments suivants sont nécessaires :**
- **Études in vitro** : mesure de l'expression de DCK et du rapport DCK/5'-NT dans des lignées cellulaires de RMS embryonnaire paraméningé, et détermination de l'IC₅₀ de cladribine
- **Modèles précliniques** : évaluation in vivo dans des modèles PDX (*Patient-Derived Xenograft*) de RMS paraméningé avant toute considération clinique
- **Données pharmacocinétiques** : pénétration de cladribine dans les tissus paraméningés et le système nerveux central (région anatomiquement critique dans cette localisation tumorale)
- **Mécanisme d'action complet** : interrogation DrugBank API (DG002) pour disposer d'un MOA structuré et permettre l'analyse de pertinence mécanistique
- **Données de sécurité** : résolution de DG001 via téléchargement de la notice TFDA et des mises en garde officielles
- **Revue de la littérature élargie** : recherche sur l'ensemble des analogues nucléosidiques (clofarabine, nélarabine) dans les sarcomes pédiatriques, pour contextualiser la classe thérapeutique
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

