---
layout: default
title: Tipranavir
parent: Prédiction du modèle uniquement (L5)
nav_order: 766
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tipranavir : nouvelle indication prédite, Syndrome d'immunodéficience acquise féline (niveau de preuve L5). Indication d'origine : Infection par le VIH, SIDA"
monitor_inn: "TIPRANAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "benign prostate phyllodes tumor"]
---

# Tipranavir
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Tipranavir : Du VIH/SIDA au Syndrome d'immunodéficience acquise féline

## Résumé en Une Phrase

Tipranavir est un inhibiteur non peptidique de la protéase du VIH-1, initialement utilisé pour traiter l'infection par le VIH et le SIDA.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome d'immunodéficience acquise féline** (indication vétérinaire), mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection par le VIH, SIDA (selon le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Syndrome d'immunodéficience acquise féline |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement annulé (AMM annulée) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le tipranavir est un inhibiteur non peptidique de la protéase du VIH-1. Son efficacité dans l'infection par le VIH est établie, et il pourrait mécanistiquement s'appliquer à d'autres lentivirus.

Le virus de l'immunodéficience féline (FIV) est un lentivirus dont la protéase est structurellement apparentée à celle du VIH-1, d'où un lien plausible. Toutefois, la protéase du FIV diffère par sa spécificité de substrat et sa sensibilité aux inhibiteurs, et aucune donnée n'étaye ce lien.

Le score élevé reflète probablement la proximité dans le réseau avec les indications VIH, plutôt qu'une preuve indépendante. Il s'agit en outre d'une indication vétérinaire, ce qui limite sa pertinence pour le repositionnement chez l'humain.

Autres prédictions du modèle, toutes de niveau L5 et en statut Hold :
- **Infection par le virus de l'immunodéficience simienne** (99,99 %) : protéase très homologue à celle du VIH-1, plausible, mais modèle animal et sans données.
- **Complexe lié au SIDA** et **VIH congénital** (99,83 %) : reformulations de l'indication existante, sans véritable repositionnement.
- **Trouble neurodéveloppemental rare** (99,99 %), **fibrome de la prostate**, **tumeur de Brenner**, **néoplasme bénin de l'appareil reproducteur**, **tumeur phyllode bénigne de la prostate** (≈ 99,3–99,4 %) : aucun lien mécanistique identifié, probablement des artefacts du graphe.
- **Hyperlipidémie combinée familiale (terme obsolète)** (99,93 %) : les inhibiteurs de protéase du VIH provoquent des dyslipidémies ; le tipranavir risquerait d'aggraver cette maladie. Prédiction probablement erronée et potentiellement nocive.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67219072 | APTIVUS 250 mg, capsule molle (Boehringer Ingelheim International ; statut : annulée) | Capsule molle | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : insuffisance hépatique, maladie du foie, hépatite (dont infections chroniques par les virus des hépatites B et C), maladie de la vésicule biliaire, hyperglycémie, diabète, acidocétose diabétique, troubles de la coagulation, hémophilie, hypertriglycéridémie, hyperbilirubinémie (dont forme héréditaire et syndrome de Gilbert), traumatisme, tumeur cérébrale et hémorragie intracrânienne.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi les principales :
  - **Majeures** : acide acétylsalicylique, éluxadoline.
  - **Modérées** : antidiabétiques (acarbose, albiglutide, alogliptine, metformine, pioglitazone, canagliflozine, dapagliflozine, empagliflozine, linagliptine, dulaglutide, chlorpropamide), lopéramide, dexaméthasone, acide cholique, clarithromycine, oxyde de magnésium, éliglustat, métronidazole (topique).
- Les mises en garde et contre-indications issues de la notice de l'ANSM n'ont pas pu être consultées. Veuillez consulter la notice pour les informations de sécurité complètes. Les données de prédiction mentionnent par ailleurs des mises en garde encadrées pour hémorragie intracrânienne et hépatotoxicité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication. L'indication est vétérinaire, l'AMM française est annulée et le profil de sécurité est lourd (hépatotoxicité, hémorragie intracrânienne, nombreuses interactions). Les autres prédictions sont soit des reformulations de l'indication existante, soit des artefacts probables du modèle.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), point bloquant pour le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (MOA) via DrugBank
- Données précliniques sur l'inhibition de la protéase du FIV/SIV par le tipranavir
- Évaluer la pertinence d'une indication vétérinaire au regard d'un objectif de repositionnement chez l'humain
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

