---
layout: default
title: Efmoroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 10
---

# Efmoroctocog Alfa
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

# Efmoroctocog Alfa : De l'Hémophilie A à la Pseudo-maladie de von Willebrand

## Résumé en Une Phrase

Efmoroctocog alfa est une protéine de fusion recombinante Facteur VIII-Fc (rFVIIIFc), approuvée dans plusieurs pays (commercialisé sous les noms Eloctate/Elocta) pour le traitement de l'hémophilie A, un déficit congénital en Facteur VIII de la coagulation.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **pseudo-maladie de von Willebrand**,
avec **0 essai clinique** et **0 publication** soutenant actuellement cette direction — la prédiction repose exclusivement sur le graphe de connaissances biomédicales.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hémophilie A (déficit congénital en Facteur VIII) |
| Nouvelle Indication Prédite | Pseudo-maladie de von Willebrand |
| Score de Prédiction TxGNN | 99.997% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé (aucune AMM) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données source. Sur la base des informations connues, efmoroctocog alfa est une protéine de fusion recombinante Facteur VIII-Fc dont l'efficacité dans l'hémophilie A a été prouvée à l'échelle internationale. Il agit en compensant le déficit en Facteur VIII, restaurant la formation du complexe tenase intrinsèque nécessaire à l'activation du Facteur X dans la cascade de coagulation. La fusion Fc prolonge la demi-vie plasmatique par recyclage via le récepteur néonatal FcRn.

La pseudo-maladie de von Willebrand (pseudo-vWD) est une pathologie fondamentalement différente : elle résulte d'une mutation gain-de-fonction du récepteur plaquettaire GPIbα, qui provoque une liaison spontanée et pathologique des plaquettes au facteur von Willebrand (vWF) circulant, entraînant une thrombopénie et une déplétion en vWF de haut poids moléculaire. Il s'agit d'un dysfonctionnement de l'axe plaquettes/vWF, sans lien direct avec l'activité du Facteur VIII.

Le score TxGNN extrêmement élevé (99.997%) reflète très probablement les larges réseaux de comorbidité partagés dans le graphe de connaissances entre les maladies hémorragiques rares, plutôt qu'une pertinence mécanistique directe. Le Facteur VIII circulant est transporté par le vWF comme protéine chaperonne, ce qui crée une association fonctionnelle dans le graphe — mais cette association n'implique pas que l'efmoroctocog alfa puisse corriger le défaut intrinsèque du récepteur GPIbα propre à la pseudo-vWD.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La pseudo-maladie de von Willebrand résulte d'un défaut du récepteur plaquettaire GPIbα — un mécanisme pathologique fondamentalement distinct du déficit en Facteur VIII que corrige l'efmoroctocog alfa. Aucune preuve clinique ou préclinique spécifique à cette association n'existe (niveau L5 : prédiction du modèle uniquement), et le rationnel mécanistique est insuffisant pour justifier un investissement de développement.

> **Note sur les autres prédictions :** Sur les 10 indications prédites dans ce pack, la plus prometteuse sur le plan mécanistique est la **pseudo-maladie de von Willebrand (rang 1, Hold)** et l'**hémophilie A avec anomalie vasculaire (rang 9, Research Question)** — cette dernière étant une sous-population de l'indication approuvée du médicament, avec un rationnel mécanistique solide, mais sans données cliniques dédiées à ce sous-groupe. La **déficience acquise en facteurs de coagulation (rang 5, Research Question)**, notamment l'hémophilie A acquise à faible titre d'inhibiteurs, représente également une piste explorée. Les 7 autres indications présentent une pertinence mécanistique faible à nulle.

**Pour avancer, les éléments suivants sont nécessaires :**

- **Mécanisme d'action (MOA)** : Obtenir les données complètes depuis DrugBank (DG002 — priorité haute)
- **Données de sécurité** : Télécharger et analyser la notice officielle ANSM ou EMA (DG001 — priorité bloquante)
- **Clarification réglementaire** : Vérifier le statut AMM européenne d'Elocta (Sobi/Sanofi) et son applicabilité en France
- **Réévaluation de la prédiction** : Avant tout travail préclinique sur la pseudo-vWD, reconsidérer si l'hémophilie A avec anomalie vasculaire (rang 9) ne constitue pas une cible plus directement exploitable en tant que sous-indication de l'indication approuvée
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

