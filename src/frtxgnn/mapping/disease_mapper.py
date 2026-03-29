"""疾病映射模組 - 葡萄牙語適應症/治療類別映射至 TxGNN 疾病本體"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


# 葡萄牙語-英語疾病/症狀對照表
DISEASE_DICT = {
    # === Système cardiovasculaire ===
    "hypertension": "hypertension",
    "hypertension artérielle": "hypertension",
    "hypotension": "hypotension",
    "infarctus du myocarde": "myocardial infarction",
    "crise cardiaque": "myocardial infarction",
    "angine de poitrine": "angina",
    "arythmie": "arrhythmia",
    "fibrillation auriculaire": "atrial fibrillation",
    "insuffisance cardiaque": "heart failure",
    "maladie coronarienne": "coronary artery disease",
    "thrombose veineuse profonde": "deep vein thrombosis",
    "embolie pulmonaire": "pulmonary embolism",
    "hypercholestérolémie": "hypercholesterolemia",
    "dyslipidémie": "dyslipidemia",
    "athérosclérose": "atherosclerosis",
    "endocardite": "endocarditis",
    "myocardite": "myocarditis",
    "péricardite": "pericarditis",
    # === Système respiratoire ===
    "bronchopneumopathie chronique obstructive": "chronic obstructive pulmonary disease",
    "bpco": "chronic obstructive pulmonary disease",
    "asthme": "asthma",
    "pneumonie": "pneumonia",
    "bronchite": "bronchitis",
    "grippe": "influenza",
    "tuberculose": "tuberculosis",
    "mucoviscidose": "cystic fibrosis",
    "apnée du sommeil": "obstructive sleep apnea",
    "dyspnée": "dyspnea",
    "emphysème": "emphysema",
    "sinusite": "sinusitis",
    "rhinite allergique": "allergic rhinitis",
    # === Système digestif ===
    "reflux gastro-œsophagien": "gastroesophageal reflux disease",
    "rgo": "gastroesophageal reflux disease",
    "ulcère gastrique": "gastric ulcer",
    "ulcère duodénal": "duodenal ulcer",
    "gastrite": "gastritis",
    "syndrome du côlon irritable": "irritable bowel syndrome",
    "maladie inflammatoire de l'intestin": "inflammatory bowel disease",
    "maladie de crohn": "crohn disease",
    "rectocolite hémorragique": "ulcerative colitis",
    "constipation": "constipation",
    "diarrhée": "diarrhea",
    "nausée": "nausea",
    "vomissement": "vomiting",
    "stéatose hépatique": "hepatic steatosis",
    "cirrhose": "liver cirrhosis",
    "hépatite": "hepatitis",
    "hépatite b": "hepatitis b",
    "hépatite c": "hepatitis c",
    "pancréatite": "pancreatitis",
    "calculs biliaires": "cholelithiasis",
    # === Système nerveux ===
    "maladie d'alzheimer": "alzheimer disease",
    "alzheimer": "alzheimer disease",
    "maladie de parkinson": "parkinson disease",
    "parkinson": "parkinson disease",
    "épilepsie": "epilepsy",
    "sclérose en plaques": "multiple sclerosis",
    "migraine": "migraine",
    "céphalée": "headache",
    "mal de tête": "headache",
    "accident vasculaire cérébral": "stroke",
    "avc": "stroke",
    "neuropathie": "neuropathy",
    "neuropathie périphérique": "peripheral neuropathy",
    "méningite": "meningitis",
    "encéphalite": "encephalitis",
    # === Troubles psychiatriques ===
    "dépression": "depression",
    "trouble dépressif majeur": "major depressive disorder",
    "anxiété": "anxiety disorder",
    "trouble anxieux généralisé": "generalized anxiety disorder",
    "trouble bipolaire": "bipolar disorder",
    "schizophrénie": "schizophrenia",
    "trouble obsessionnel compulsif": "obsessive-compulsive disorder",
    "toc": "obsessive-compulsive disorder",
    "trouble de stress post-traumatique": "post-traumatic stress disorder",
    "tspt": "post-traumatic stress disorder",
    "insomnie": "insomnia",
    "trouble du déficit de l'attention": "attention deficit hyperactivity disorder",
    "tdah": "attention deficit hyperactivity disorder",
    # === Système endocrinien ===
    "diabète": "diabetes mellitus",
    "diabète de type 1": "type 1 diabetes mellitus",
    "diabète de type 2": "type 2 diabetes mellitus",
    "hypothyroïdie": "hypothyroidism",
    "hyperthyroïdie": "hyperthyroidism",
    "goitre": "goiter",
    "syndrome de cushing": "cushing syndrome",
    "maladie d'addison": "addison disease",
    "obésité": "obesity",
    "syndrome métabolique": "metabolic syndrome",
    "goutte": "gout",
    "hyperuricémie": "hyperuricemia",
    # === Système musculo-squelettique ===
    "arthrite": "arthritis",
    "polyarthrite rhumatoïde": "rheumatoid arthritis",
    "arthrose": "osteoarthritis",
    "ostéoporose": "osteoporosis",
    "lupus érythémateux disséminé": "systemic lupus erythematosus",
    "lupus": "systemic lupus erythematosus",
    "fibromyalgie": "fibromyalgia",
    "spondylarthrite ankylosante": "ankylosing spondylitis",
    "tendinite": "tendinitis",
    "lombalgie": "low back pain",
    # === Maladies de la peau ===
    "psoriasis": "psoriasis",
    "eczéma": "eczema",
    "dermatite atopique": "atopic dermatitis",
    "urticaire": "urticaria",
    "acné": "acne",
    "rosacée": "rosacea",
    "vitiligo": "vitiligo",
    "alopécie": "alopecia",
    "zona": "herpes zoster",
    "herpès": "herpes simplex",
    "mycose": "fungal infection",
    # === Système urinaire ===
    "infection urinaire": "urinary tract infection",
    "cystite": "cystitis",
    "néphrite": "nephritis",
    "insuffisance rénale": "renal failure",
    "maladie rénale chronique": "chronic kidney disease",
    "calculs rénaux": "nephrolithiasis",
    "hypertrophie bénigne de la prostate": "benign prostatic hyperplasia",
    "incontinence urinaire": "urinary incontinence",
    # === Ophtalmologie ===
    "glaucome": "glaucoma",
    "cataracte": "cataract",
    "dégénérescence maculaire": "macular degeneration",
    "conjonctivite": "conjunctivitis",
    "rétinopathie diabétique": "diabetic retinopathy",
    "sécheresse oculaire": "dry eye syndrome",
    # === ORL ===
    "otite moyenne": "otitis media",
    "pharyngite": "pharyngitis",
    "amygdalite": "tonsillitis",
    "laryngite": "laryngitis",
    "vertige": "vertigo",
    # === Maladies infectieuses ===
    "infection au vih": "hiv infection",
    "sida": "acquired immunodeficiency syndrome",
    "paludisme": "malaria",
    "covid-19": "covid-19",
    "septicémie": "sepsis",
    "candidose": "candidiasis",
    "toxoplasmose": "toxoplasmosis",
    # === Allergies ===
    "allergie": "allergy",
    "anaphylaxie": "anaphylaxis",
    "asthme allergique": "allergic asthma",
    "rhinite": "rhinitis",
    "dermatite de contact": "contact dermatitis",
    "allergie alimentaire": "food allergy",
    # === Gynécologie ===
    "endométriose": "endometriosis",
    "syndrome des ovaires polykystiques": "polycystic ovary syndrome",
    "ménopause": "menopause",
    "dysménorrhée": "dysmenorrhea",
    "aménorrhée": "amenorrhea",
    "vaginite": "vaginitis",
    "fibrome utérin": "uterine fibroid",
    "prééclampsie": "preeclampsia",
    # === Cancer ===
    "cancer": "cancer",
    "cancer du sein": "breast cancer",
    "cancer du poumon": "lung cancer",
    "cancer colorectal": "colorectal cancer",
    "cancer de la prostate": "prostate cancer",
    "cancer du foie": "liver cancer",
    "cancer de l'estomac": "stomach cancer",
    "cancer du pancréas": "pancreatic cancer",
    "leucémie": "leukemia",
    "lymphome": "lymphoma",
    "mélanome": "melanoma",
    "cancer du rein": "kidney cancer",
    "cancer de la vessie": "bladder cancer",
    "cancer de la thyroïde": "thyroid cancer",
    # === Symptômes généraux ===
    "fièvre": "fever",
    "douleur": "pain",
    "douleur chronique": "chronic pain",
    "inflammation": "inflammation",
    "œdème": "edema",
    "fatigue": "fatigue",
    "anémie": "anemia",
}


def load_disease_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 疾病詞彙表"""
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "disease_vocab.csv"
    return pd.read_csv(filepath)


def build_disease_index(disease_df: pd.DataFrame) -> Dict[str, Tuple[str, str]]:
    """建立疾病名稱索引（關鍵詞 -> (disease_id, disease_name)）"""
    index = {}

    for _, row in disease_df.iterrows():
        disease_id = row["disease_id"]
        disease_name = row["disease_name"]
        name_upper = row["disease_name_upper"]

        # 完整名稱
        index[name_upper] = (disease_id, disease_name)

        # 提取關鍵詞（按空格和逗號分割）
        keywords = re.split(r"[,\s\-]+", name_upper)
        for kw in keywords:
            kw = kw.strip()
            if len(kw) > 3 and kw not in index:  # 只保留較長的關鍵詞
                index[kw] = (disease_id, disease_name)

    return index


def extract_indications(indication_str: str) -> List[str]:
    """從適應症/治療類別文字提取個別適應症

    使用葡萄牙語常見分隔符分割
    """
    if not indication_str:
        return []

    # 正規化
    text = indication_str.strip().lower()

    # 使用分隔符分割
    parts = re.split(r"[.;]", text)

    indications = []
    for part in parts:
        # 再用逗號細分
        sub_parts = re.split(r"[,/]", part)
        for sub in sub_parts:
            sub = sub.strip()
            # 移除常見前綴
            sub = re.sub(r"^(para |tratamento de |indicado para |usado para )", "", sub)
            # 移除常見後綴
            sub = re.sub(r"( e outros| etc\.?)$", "", sub)
            sub = sub.strip()
            if sub and len(sub) >= 2:
                indications.append(sub)

    return indications


def translate_indication(indication: str) -> List[str]:
    """將葡萄牙語適應症翻譯為英文關鍵詞"""
    keywords = []
    indication_lower = indication.lower()

    for pt, en in DISEASE_DICT.items():
        if pt in indication_lower:
            keywords.append(en.upper())

    return keywords


def map_indication_to_disease(
    indication: str,
    disease_index: Dict[str, Tuple[str, str]],
) -> List[Tuple[str, str, float]]:
    """將單一適應症映射到 TxGNN 疾病

    Returns:
        [(disease_id, disease_name, confidence), ...]
    """
    results = []

    # 翻譯為英文關鍵詞
    keywords = translate_indication(indication)

    for kw in keywords:
        # 完全匹配
        if kw in disease_index:
            disease_id, disease_name = disease_index[kw]
            results.append((disease_id, disease_name, 1.0))
            continue

        # 部分匹配
        for index_kw, (disease_id, disease_name) in disease_index.items():
            if kw in index_kw or index_kw in kw:
                results.append((disease_id, disease_name, 0.8))

    # 去重並按信心度排序
    seen = set()
    unique_results = []
    for disease_id, disease_name, conf in sorted(results, key=lambda x: -x[2]):
        if disease_id not in seen:
            seen.add(disease_id)
            unique_results.append((disease_id, disease_name, conf))

    return unique_results[:5]  # 最多返回 5 個匹配


def map_fda_indications_to_diseases(
    fda_df: pd.DataFrame,
    disease_df: Optional[pd.DataFrame] = None,
    indication_field: str = "CLASSE_TERAPEUTICA",
) -> pd.DataFrame:
    """將巴西 ANVISA 藥品治療類別映射到 TxGNN 疾病"""
    if disease_df is None:
        disease_df = load_disease_vocab()

    disease_index = build_disease_index(disease_df)

    results = []

    for _, row in fda_df.iterrows():
        # ANVISA 使用 CLASSE_TERAPEUTICA 而非適應症
        indication_str = row.get(indication_field, "")
        if not indication_str:
            continue

        # 提取個別適應症
        indications = extract_indications(indication_str)

        for ind in indications:
            # 翻譯並映射
            matches = map_indication_to_disease(ind, disease_index)

            if matches:
                for disease_id, disease_name, confidence in matches:
                    results.append({
                        "NUMERO_REGISTRO_PRODUTO": row.get("NUMERO_REGISTRO_PRODUTO", ""),
                        "NOME_PRODUTO": row.get("NOME_PRODUTO", ""),
                        "CLASSE_TERAPEUTICA": indication_str[:100],
                        "extracted_indication": ind,
                        "disease_id": disease_id,
                        "disease_name": disease_name,
                        "confidence": confidence,
                    })
            else:
                results.append({
                    "NUMERO_REGISTRO_PRODUTO": row.get("NUMERO_REGISTRO_PRODUTO", ""),
                    "NOME_PRODUTO": row.get("NOME_PRODUTO", ""),
                    "CLASSE_TERAPEUTICA": indication_str[:100],
                    "extracted_indication": ind,
                    "disease_id": None,
                    "disease_name": None,
                    "confidence": 0,
                })

    return pd.DataFrame(results)


def get_indication_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """計算適應症映射統計"""
    total = len(mapping_df)
    mapped = mapping_df["disease_id"].notna().sum()
    unique_indications = mapping_df["extracted_indication"].nunique()
    unique_diseases = mapping_df[mapping_df["disease_id"].notna()]["disease_id"].nunique()

    return {
        "total_indications": total,
        "mapped_indications": int(mapped),
        "mapping_rate": mapped / total if total > 0 else 0,
        "unique_indications": unique_indications,
        "unique_diseases": unique_diseases,
    }
