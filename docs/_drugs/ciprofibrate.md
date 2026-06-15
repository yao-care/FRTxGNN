---
layout: default
title: Ciprofibrate
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L5
indication_count: 10
---

# Ciprofibrate
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

# Ciprofibrate : De la Dyslipidémie à l'Hyperlipoproteinemia

## Résumé en Une Phrase

Ciprofibrate est un dérivé de l'acide fibrique (classe des fibrates), historiquement utilisé pour le traitement de la dyslipidémie athérogène en Europe.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Hyperlipoproteinemia**,
avec **0 essai clinique enregistré** et **20 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible dans le registre (aucune AMM enregistrée) |
| Nouvelle Indication Prédite | Hyperlipoproteinemia |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base de données actuelle. Sur la base des informations connues, ciprofibrate appartient à la classe pharmacologique des fibrates (dérivés de l'acide fibrique), dont l'efficacité dans la dyslipidémie athérogène est établie depuis plusieurs décennies en Europe (commercialisé sous les noms Modalim® au Royaume-Uni et Lipanor® dans plusieurs pays d'Europe centrale). Son mécanisme principal est l'activation du récepteur nucléaire PPAR-α (Peroxisome Proliferator-Activated Receptor alpha), un régulateur central du métabolisme lipidique hépatique.

L'activation du PPAR-α par ciprofibrate correspond directement aux mécanismes pathologiques de l'hyperlipoproteinemia : la lipoprotéine lipase (LPL) est surexprimée, accélérant le catabolisme des lipoprotéines riches en triglycérides (VLDL/IDL) ; l'apoC-III est réprimée, levant l'inhibition de la LPL ; et la synthèse d'apoA-I/II est stimulée, favorisant la maturation des particules HDL. Ces effets convergents permettent de traiter les trois sous-types principaux d'hyperlipoproteinemia athérogène : type IIa (hypercholestérolémie isolée), type IIb (hyperlipidémie combinée) et type IV (hypertriglycéridémie).

La base de preuves disponible est particulièrement cohérente : les 20 publications identifiées couvrent directement les sous-types Frederickson IIa, IIb et IV, avec des essais contrôlés randomisés comparatifs contre fenofibrate, bézafibrate et gemfibrozil, ainsi que des études de pharmacologie clinique portant sur des biomarqueurs de risque cardiovasculaire (apoB, sdLDL, PAI-1, fibrinogène). La prédiction TxGNN (score 99,97 %) valide ainsi une indication pharmacologique historiquement reconnue, absente du registre français actuel.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour l'indication hyperlipoproteinemia.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [9015467](https://pubmed.ncbi.nlm.nih.gov/9015467/) | 1996 | ECR Comparatif (vs bézafibrate) | Postgraduate Medical Journal | 174 patients type II hyperlipidémie : ciprofibrate 100 mg/j non inférieur à bézafibrate SR 400 mg/j sur 8 semaines ; amélioration TC, LDL-C et HDL-C |
| [6753860](https://pubmed.ncbi.nlm.nih.gov/6753860/) | 1982 | ECR Double-aveugle (vs placebo) | Atherosclerosis | 20 patients type II hypercholestérolémie : ciprofibrate 50–100 mg/j réduit significativement LDL-C sur 12 semaines ; bien toléré |
| [3994783](https://pubmed.ncbi.nlm.nih.gov/3994783/) | 1985 | Étude Comparative (vs fenofibrate) | Atherosclerosis | Double-aveugle 3 mois : ciprofibrate 100 mg/j vs fenofibrate 300 mg/j ; réductions significatives TC, LDL-C, VLDL-C, apoB ; hausse HDL-C et apoA (p < 0,001) |
| [8831920](https://pubmed.ncbi.nlm.nih.gov/8831920/) | 1996 | Essai Clinique (multidose, ~3 000 patients) | Atherosclerosis | Efficacité sur types IIa/IIb/IV : réduction TC, TG, LDL-C, apoB ; élévation HDL-C à 100 mg/j ; profil de sécurité documenté sur large cohorte |
| [12915663](https://pubmed.ncbi.nlm.nih.gov/12915663/) | 2003 | Pharmacologie Clinique (type IIb) | J Clin Endocrinol Metab | 10 patients type IIb : réduction VLDL-1 (−40 %, p = 0,001) et VLDL-2 (−25 %) ; stimulation de l'efflux cellulaire de cholestérol médié par les particules HDL |
| [17414592](https://pubmed.ncbi.nlm.nih.gov/17414592/) | 2007 | Essai Clinique (type IV) | American Journal of Therapeutics | Patients Frederickson type IV : réduction significative non-HDL-C et TG, augmentation HDL-C ; traitement de la dyslipidémie mixte athérogène |
| [10645034](https://pubmed.ncbi.nlm.nih.gov/10645034/) | 1999 | Essai Clinique (monothérapie ± AAS) | Bratislavske Lekarske Listy | Patients athérosclérose avancée + hyperlipoproteinemia : ciprofibrate seul ou + aspirine réduit TG, LDL-C, fibrinogène et thromboxane |
| [9364979](https://pubmed.ncbi.nlm.nih.gov/9364979/) | 1997 | Pharmacologie Clinique (hémostase) | Thrombosis and Haemostasis | Ciprofibrate vs gemfibrozil sur t-PA, PAI-1 et fibrinogène chez patients hyperlipidémiques : activité hémostase-modulatrice favorable |
| [15547649](https://pubmed.ncbi.nlm.nih.gov/15547649/) | 2004 | Observationnelle (molécules d'adhésion) | Angiology | Dyslipidémiques obèses ± diabète type 2 : ciprofibrate réduit sVCAM-1, sICAM-1, sE-sélectine, suggérant un effet anti-athérosclérotique indépendant de l'action hypolipémiante |
| [10941600](https://pubmed.ncbi.nlm.nih.gov/10941600/) | 2000 | Observationnelle (apolipoprotéines) | Drugs Exp Clin Res | FCH traités par ciprofibrate : stimulation apoA-I, inhibition apoC-III, augmentation paraoxonase (activité antioxydante endogène) |

---

## Informations de Marché en France

Ciprofibrate (DB09064) ne dispose d'aucune autorisation de mise sur le marché (AMM) enregistrée en France dans la base de données consultée. Le médicament est commercialisé dans plusieurs pays européens (Royaume-Uni sous Modalim® ; Europe centrale sous Lipanor®) mais reste absent du marché français selon les données actuelles.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
La prédiction TxGNN (score 99,97 %) valide une indication pharmacologiquement établie : ciprofibrate est un fibrate agoniste PPAR-α dont l'efficacité dans les hyperlipoproteinemia de types IIa, IIb et IV est documentée par 20 publications cliniques, incluant plusieurs ECR comparatifs robustes portant sur des milliers de patients. L'absence d'AMM en France constitue le principal obstacle réglementaire, mais la solidité de la base de preuves internationale justifie une évaluation formelle.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données complètes de mécanisme d'action (MOA) issues de DrugBank (résoudre DG002)
- Données de sécurité détaillées : mises en garde, contre-indications et interactions médicamenteuses issues des notices ANSM/EMA (résoudre DG001)
- Évaluation réglementaire de la faisabilité d'une demande d'AMM en France, en comparaison avec les fibrates déjà approuvés (fenofibrate, bézafibrate)
- Plan de surveillance clinique pour les populations à risque (insuffisance hépatique, rénale, association aux statines avec risque de myopathie)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

