---
layout: default
title: Adefovir Dipivoxil
parent: Prédiction du modèle uniquement (L5)
nav_order: 27
evidence_level: L5
indication_count: 10
---

# Adefovir Dipivoxil
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

# Adéfovir dipivoxil : De l'hépatite B chronique à l'infection par l'hépatite C chronique

## Résumé en Une Phrase

L'adéfovir dipivoxil est un analogue nucléotidique antiviral, initialement utilisé pour le traitement de l'**infection chronique par le virus de l'hépatite B**.
Le modèle TxGNN prédit en première position qu'il pourrait être efficace pour l'**infection chronique par le virus de l'hépatite C**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette prédiction.
Les données compilées pour ce rapport montrent en revanche que d'autres indications prédites (notamment l'infection par le VIH) disposent de preuves bien plus solides.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection chronique par le virus de l'hépatite B (aucun texte d'indication d'AMM disponible en France) |
| Nouvelle Indication Prédite | Infection chronique par le virus de l'hépatite C |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances pharmacologiques générales, l'adéfovir est un analogue nucléotidique acyclique : il est converti en diphosphate d'adéfovir, qui inhibe l'ADN polymérase / transcriptase inverse virale en entraînant l'arrêt de la chaîne d'élongation. C'est ce mécanisme qui sous-tend son efficacité dans l'hépatite B.

Pour l'hépatite C, le lien mécanistique est **faible**. Le VHC est un virus à ARN dont la réplication dépend de l'ARN polymérase ARN-dépendante NS5B, une cible différente de celle de l'adéfovir. Le score élevé de TxGNN reflète une proximité dans le graphe de connaissances (les deux maladies sont des hépatites virales) et non une preuve biologique ou clinique. Par ailleurs, les antiviraux à action directe actuels rendent un repositionnement peu justifié.

À noter : parmi les autres indications prédites, l'**infection par le VIH** (rang 2) est mécanistiquement plausible et dispose d'essais cliniques (niveau L2). Elle a toutefois été abandonnée en raison de la néphrotoxicité dose-limitante de l'adéfovir aux doses anti-VIH (120 mg), le ténofovir étant une alternative supérieure.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour l'hépatite C chronique.

*Pour information, l'essai le plus proche, NCT00051077 (Phase 2, co-infection VHB/VHC/VIH), est rattaché à l'indication « infection par le virus de l'hépatite C » (rang 7) ; il a été retiré avant inclusion de patients (0 inscrit) et n'a produit aucune donnée.*

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'hépatite C chronique.

---

## Informations de Marché en France

Aucune AMM n'est enregistrée en France pour ce médicament dans les données compilées (statut : non commercialisé). La disponibilité réelle doit être vérifiée auprès de l'ANSM.

---

## Cytotoxicité

Section non applicable : l'adéfovir dipivoxil est un antiviral et non un antinéoplasique.

---

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

- **Maladies associées à des contre-indications (graphe de connaissances, et non texte de notice)** : maladie rénale, pyourétère, obésité (y compris obésité monogénique), stéatose hépatique, stéatohépatite non alcoolique, acidose lactique.
- **Interactions médicamenteuses** : 25 interactions recensées, toutes de niveau de gravité non précisé. Parmi les principales : pantoprazole, oméprazole, lansoprazole, rabéprazole, ranitidine, famotidine, morphine, warfarine, héparine, ibuprofène, kanamycine, prednisolone, chlorure de potassium, lactulose, métoclopramide, miconazole, acide ursodésoxycholique, cyanocobalamine, lidocaïne, fexofénadine.
- **Point de vigilance général issu de la littérature fournie** : la néphrotoxicité dose-dépendante de l'adéfovir est documentée (surveillance de la fonction rénale et adaptation posologique nécessaires).

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour l'hépatite C chronique repose uniquement sur le score du modèle (niveau L5), sans essai ni publication, avec un lien mécanistique faible (virus à ARN, cible différente) et des alternatives modernes très efficaces.
- Les données de sécurité de la notice sont absentes, ce qui bloque tout passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications).
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Démontrer une activité anti-VHC par des données précliniques (in vitro) avant toute étude clinique.
- Si une piste de repositionnement doit être explorée, privilégier l'indication VIH (L2), en tenant compte de la néphrotoxicité et de la supériorité du ténofovir.
- Vérifier la disponibilité réelle du médicament en France, son statut étant « non commercialisé ».
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

