---
layout: default
title: Cefpodoxime
parent: Prédiction du modèle uniquement (L5)
nav_order: 148
evidence_level: L5
indication_count: 2
monitor_inn: "cefpodoxime"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis"]
last_modified_at: 2026-11-20
description: "Cefpodoxime : nouvelle indication prédite, Arthrose (niveau de preuve L5). Indication d'origine : Non renseignée dans les textes d'AMM disponibles (antibiotique de la…"
---

# Cefpodoxime
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Cefpodoxime : De l'antibiothérapie à l'arthrose (prédiction du modèle)
{: .text-alpha }

## Résumé en Une Phrase

Cefpodoxime est une céphalosporine orale de troisième génération (antibiotique de la famille des bêta-lactamines). Le texte des indications figurant dans les AMM françaises n'est pas renseigné dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**arthrose**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les textes d'AMM disponibles (antibiotique de la famille des céphalosporines) |
| Nouvelle Indication Prédite | Arthrose |
| Score de Prédiction TxGNN | 0,9925 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 18 sur 18) |
| Nombre d'AMM | 18 (valides : 18) |
| Décision Recommandée | Hold |

Une seconde prédiction, la **polyarthrite rhumatoïde** (score 0,9924), figure également dans les données. Elle est de niveau L5 et de décision Hold, comme l'arthrose.

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon ChEMBL (EMBL-EBI), le mécanisme d'action enregistré pour Cefpodoxime est (traduction non officielle) : « Inhibiteur des protéines bactériennes de liaison aux pénicillines » Texte original en anglais : "Bacterial penicillin-binding protein inhibitor" ([ChEMBL CHEMBL1672 (cefpodoxime): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1672), CC BY-SA 3.0 ; consulté le 2026-11-19). D'après les informations connues, cefpodoxime est un antibiotique oral de la famille des céphalosporines de troisième génération. Cette classe inhibe la synthèse de la paroi cellulaire bactérienne.

Aucun lien mécanistique plausible n'est établi avec l'arthrose. Cette maladie est dégénérative et en grande partie non infectieuse : elle résulte de la dégradation du cartilage, de contraintes mécaniques et d'une inflammation de bas grade. Aucune cible antibactérienne n'est identifiable.

Le score élevé (0,9925) est une prédiction issue du modèle TxGNN (apprentissage profond). Il peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique. Pour la polyarthrite rhumatoïde, certaines tétracyclines (minocycline, doxycycline) ont été étudiées pour leurs effets anti-inflammatoires, mais cet effet de classe ne s'étend pas aux céphalosporines et ne peut pas être supposé pour cefpodoxime.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Cefpodoxime est commercialisé en France, avec 18 AMM valides (toutes en spécialité à principe actif unique). Le texte des indications approuvées n'est pas renseigné dans les données compilées. Les 5 premières AMM sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68474866 | Cefpodoxime Viatris Enfants et Nourrissons 40 mg/5 mL | Poudre pour suspension buvable | Non renseignée |
| 63386914 | Cefpodoxime Zydus 100 mg | Comprimé pelliculé | Non renseignée |
| 68951100 | Cefpodoxime Viatris 100 mg | Comprimé pelliculé | Non renseignée |
| 68497014 | Cefpodoxime Biogaran Enfants et Nourrissons 40 mg/5 mL | Poudre pour suspension buvable | Non renseignée |
| 69170898 | Cefpodoxime Sandoz Enfants et Nourrissons 40 mg/5 mL | Poudre pour suspension buvable | Non renseignée |

---

## Considérations de Sécurité

**Interactions médicamenteuses** : 78 interactions sont recensées, dont les 20 premières, toutes de niveau modéré, sont disponibles. Elles concernent principalement :
- les **antiacides** (hydroxyde d'aluminium, carbonate de calcium, magaldrate, carbonate, hydroxyde et oxyde de magnésium) ;
- les **antihistaminiques H2** (famotidine, ranitidine, cimétidine, nizatidine, ranitidine-citrate de bismuth) ;
- les **inhibiteurs de la pompe à protons** (oméprazole, ésoméprazole, lansoprazole, dexlansoprazole, pantoprazole, rabéprazole) ;
- les **aminosides** (kanamycine, néomycine) ;
- le **balsalazide**.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5). Aucun essai ni publication ne l'étaye, et aucun lien mécanistique plausible n'existe entre un antibiotique bêta-lactamine et l'arthrose.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les données sur le mécanisme d'action (DrugBank) afin d'analyser un éventuel lien mécanistique.
- Les mises en garde et contre-indications issues des notices ANSM, indispensables avant tout examen de sécurité.
- Les textes d'indications approuvées des AMM.
- Des études précliniques ou observationnelles étudiant directement cefpodoxime dans l'arthrose, ou dans la polyarthrite rhumatoïde.
- Une évaluation de la compatibilité des voies d'administration, encore en attente.

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [ChEMBL CHEMBL1672 (cefpodoxime): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1672) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

