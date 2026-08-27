---
layout: default
title: Scopolamine
parent: 僅模型預測 (L5)
nav_order: 274
evidence_level: L5
indication_count: 6
---

# Scopolamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Scopolamine : D'une Indication Non Documentée au Syndrome de la Queue de Cheval

## Résumé en Une Phrase

Scopolamine est un antagoniste muscarinique (anticholinergique) dont l'indication d'origine et le mécanisme d'action détaillé ne sont **pas documentés** dans le dossier de preuves actuel. Le modèle TxGNN identifie six indications candidates, la mieux classée étant le **syndrome de la queue de cheval**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction — il s'agit d'une prédiction de niveau L5, fondée uniquement sur des associations du graphe de connaissances.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non documentée dans le dossier de preuves actuel (aucune indication ni AMM enregistrée) |
| Nouvelle Indication Prédite | Syndrome de la Queue de Cheval (Cauda Equina Syndrome) |
| Score de Prédiction TxGNN | 99.99 % |
| Niveau de Preuve | L5 |
| Statut de Marché (Taïwan / TFDA)* | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

*\*Le dossier de preuves fourni est d'origine taïwanaise (source : TFDA), et non française — cette précision remplace le libellé générique "France" du modèle de rapport pour éviter toute confusion.*

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le mécanisme d'action d'origine de la scopolamine (`original_moa`) n'est pas documenté dans le dossier de preuves actuel — il s'agit d'un écart de données classé sévérité "Haute" (DG002). Les informations disponibles indiquent néanmoins, via le raisonnement du modèle lui-même, que la scopolamine agit comme un antagoniste non sélectif des récepteurs muscariniques (M2/M3) — la même classe pharmacologique (anticholinergiques) que des traitements déjà utilisés pour la vessie hyperactive/neurogène, tels que l'oxybutynine ou la toltérodine.

Aucune indication d'origine ni aucune AMM n'est enregistrée pour la scopolamine dans ce dossier (`original_indications` vide, 0 licence à Taïwan), ce qui empêche toute comparaison directe entre l'usage historique du médicament et l'indication prédite. Cette absence de référence clinique documentée constitue en soi une limite majeure de l'évaluation.

Pour l'indication la mieux classée, le syndrome de la queue de cheval, le modèle TxGNN attribue un score très élevé (99.99 %), mais le raisonnement mécanistique fourni par le modèle lui-même souligne une limite importante : il s'agit d'une urgence chirurgicale causée par une compression des racines nerveuses sous le cône médullaire, dont le traitement standard est la décompression chirurgicale en urgence — non un traitement pharmacologique. L'effet anticholinergique de la scopolamine pourrait tout au plus atténuer un symptôme associé (vessie neurogène / hyperactivité du détrusor), sans agir sur la cause structurelle. Le score élevé provient très probablement d'une proximité indirecte, dans le graphe de connaissances, entre la scopolamine et le nœud « vessie neurogène », fréquemment associé au syndrome de la queue de cheval — plutôt que d'un véritable lien thérapeutique direct. Ce signal doit donc être considéré comme un **possible faux positif**.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement (recherches ClinicalTrials.gov et ICTRP effectuées le 2026-04-20 pour « scopolamine + syndrome de la queue de cheval », 0 résultat).

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement (recherche PubMed effectuée le 2026-04-20, 0 résultat).

---

## Autres Indications Prédites (Pour Référence)

Le modèle TxGNN a identifié cinq autres candidats, tous au même niveau de preuve minimal. Aucun n'est appuyé par un essai clinique ou une publication (22 requêtes croisées, toutes négatives).

| Rang | Indication Prédite | Score TxGNN | Niveau de Preuve | Décision | Résumé Mécanistique |
|---|---|---|---|---|---|
| 2 | Vessie Neurogène (terme obsolète) | 99.98 % | L5 | Hold | Même classe pharmacologique (anticholinergique) que les traitements existants de la vessie neurogène, mais aucune preuve directe pour la scopolamine ; l'étiquette diagnostique est elle-même marquée « obsolète » |
| 3 | Conjonctivite Papillaire | 99.98 % | L5 | Hold | La scopolamine ophtalmique produit mydriase et cycloplégie ; aucun mécanisme anti-allergique ou anti-inflammatoire connu |
| 4 | Conjonctivite Atopique | 99.80 % | L5 | Hold | Même limite : absence de mécanisme anti-Th2/IgE |
| 5 | Conjonctivite Rosacée | 99.40 % | L5 | Hold | Aucun lien connu avec la fonction des glandes de Meibomius ou l'inflammation vasculaire |
| 6 | Conjonctivite Vernale | 99.08 % | L5 | Hold | Aucun lien avec la réponse immunitaire IgE/lymphocytes T |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. À noter : l'absence des mises en garde, contre-indications et interactions médicamenteuses (TFDA) constitue un écart de données classé **bloquant** (DG001), qui empêche à ce stade toute évaluation initiale de sécurité (S1).

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les six indications prédites sont toutes de niveau de preuve L5 (prédiction du modèle seule), sans aucun essai clinique ni publication à l'appui (22 requêtes de recherche croisées, toutes négatives).
- Le raisonnement mécanistique du modèle identifie lui-même la prédiction la mieux classée comme un possible faux positif issu d'une association indirecte dans le graphe de connaissances, plutôt que d'un lien pharmacologique direct.
- Les données de sécurité (mises en garde, contre-indications, mécanisme d'action d'origine) sont totalement absentes, ce qui bloque toute évaluation de sécurité initiale selon DG001.
- Le médicament n'est pas commercialisé à Taïwan (0 AMM), réduisant les options de validation en conditions réelles.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice TFDA de la scopolamine (DG001, bloquant)
- Confirmation du mécanisme d'action d'origine via l'API DrugBank (DG002)
- Documentation de l'indication d'origine approuvée (historique réglementaire)
- Recherche ciblée complémentaire (études précliniques, séries de cas) pour vérifier si le lien scopolamine–vessie neurogène dépasse la simple co-occurrence dans le graphe de connaissances
- Réévaluation après comblement de ces écarts avant toute progression vers l'étape S1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

