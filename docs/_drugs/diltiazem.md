---
layout: default
title: Diltiazem
parent: Prédiction du modèle uniquement (L5)
nav_order: 245
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Diltiazem : nouvelle indication prédite, Susceptibilité à l'accident vasculaire cérébral ischémique (terme obs… (niveau de preuve L5). Indication d'origine : Hypertension artérielle"
monitor_inn: "DILTIAZEM"
predicted_indications: ["obsolete susceptibility to ischemic stroke"]
---

# Diltiazem
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

# Diltiazem : De l'Hypertension à la Susceptibilité à l'Accident Vasculaire Cérébral Ischémique (terme obsolète)

## Résumé en Une Phrase

Le diltiazem est un inhibiteur calcique non dihydropyridinique, initialement utilisé pour traiter l'hypertension artérielle, la fibrillation auriculaire, l'angor de Prinzmetal et la tachycardie ventriculaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **susceptibilité à l'accident vasculaire cérébral ischémique** (terme classé comme « obsolète » dans l'ontologie).
Aucun essai clinique et aucune publication ne soutiennent actuellement cette direction : la prédiction repose uniquement sur le score du modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle (les textes d'indication des AMM françaises ne sont pas renseignés ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Susceptibilité à l'accident vasculaire cérébral ischémique (terme obsolète) |
| Score de Prédiction TxGNN | 99,08 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Uniquement des AMM annulées |
| Nombre d'AMM | 5 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le diltiazem fait partie des inhibiteurs calciques non dihydropyridiniques. Son efficacité dans l'hypertension et dans certains troubles du rythme cardiaque est établie, et il pourrait mécanistiquement être applicable à la prévention vasculaire cérébrale.

L'hypothèse la plus plausible est indirecte : l'hypertension est le principal facteur de risque modifiable de l'AVC ischémique, et la baisse de la pression artérielle pourrait donc réduire ce risque. Un effet vasodilatateur sur les vaisseaux cérébraux est également concevable sur le plan biologique, mais il n'est pas démontré par les données disponibles.

Il faut rester prudent : le terme de la maladie prédite est marqué « obsolète » dans l'ontologie, c'est-à-dire qu'il s'agit d'un concept dépassé, probablement rattaché à une entrée plus large ou nommée différemment. Le score élevé pourrait donc refléter des artefacts de structure du graphe (liens avec l'hypertension et les maladies vasculaires) plutôt qu'un véritable signal thérapeutique distinct.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les cinq AMM identifiées sont toutes annulées ; aucune AMM valide n'est recensée. Le texte de l'indication approuvée n'est pas renseigné pour ces AMM.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 60998977 | TILDIEM 100 mg, poudre pour solution injectable (IV) | Poudre pour solution injectable | Annulée |
| 63692245 | TILDIEM 60 mg, comprimé | Comprimé | Annulée |
| 68227652 | BI TILDIEM L.P. 90 mg | Comprimé enrobé à libération prolongée | Annulée |
| 65662076 | BI TILDIEM L.P. 120 mg | Comprimé enrobé à libération prolongée | Annulée |
| 62018628 | TILDIEM 25 mg, poudre et solution pour préparation injectable I.V. | Poudre et solution pour préparation injectable | Annulée |

Titulaire de toutes les AMM : SANOFI WINTHROP INDUSTRIE.

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

- **Contre-indications issues du graphe de connaissances** (à titre indicatif, ne provenant pas du texte de la notice) : bloc auriculo-ventriculaire, maladie du sinus (dysfonction sinusale), syndrome de Wolff-Parkinson-White et syndrome de Lown-Ganong-Levine, sténose aortique, cardiomyopathie hypertrophique, états hypotensifs, tachycardie ventriculaire, insuffisance rénale ou hépatique, maladie de la vésicule biliaire, angio-œdèmes (y compris héréditaire), neutropénie et agranulocytose, ainsi que certaines maladies du tissu conjonctif, osseuses et cartilagineuses.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi celles listées, une est de niveau **majeur** : le **lopéramide**. Les autres sont de niveau modéré, notamment les corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, budésonide), la pioglitazone, le bupropion, l'aprépitant, la morphine, l'acide acétylsalicylique, la canagliflozine et plusieurs sels de calcium.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication. Le terme de la maladie est obsolète, et le médicament n'a plus d'AMM valide en France. Les données de sécurité issues de la notice manquent, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications)
- Obtenir les données sur le mécanisme d'action depuis DrugBank
- Faire correspondre le terme obsolète à une entité actuelle de risque d'AVC ischémique et réévaluer le score
- Rechercher des essais cliniques et de la littérature sur le diltiazem dans la prévention de l'AVC
- Clarifier la situation réglementaire (AMM annulées) et la compatibilité des voies d'administration
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

