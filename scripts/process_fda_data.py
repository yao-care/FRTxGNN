#!/usr/bin/env python3
"""處理法國 ANSM 藥品資料

從 BDPM 下載 CIS_bdpm.txt（tab-delimited）並轉換為 JSON 格式。

使用方法:
    uv run python scripts/process_fda_data.py

資料來源:
    https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/

產生檔案:
    data/raw/fr_fda_drugs.json
"""

import json
from pathlib import Path

import pandas as pd
import requests
import yaml


def load_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def download_bdpm_data(output_path: Path) -> Path:
    """從 BDPM 下載 CIS_bdpm.txt 檔案

    BDPM 提供 tab-delimited 文字檔供批量下載。

    Args:
        output_path: 輸出路徑

    Returns:
        下載的檔案路徑
    """
    # CIS_bdpm.txt 直接下載 URL (2026 年起改為 index.php/download/file/ 路徑)
    url = "https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt"

    print("正在從 BDPM 下載 CIS_bdpm.txt...")
    print(f"URL: {url}")

    response = requests.get(url, timeout=120)
    response.raise_for_status()

    # 確保輸出目錄存在
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "wb") as f:
        f.write(response.content)

    print(f"下載完成: {output_path}")
    print(f"檔案大小: {output_path.stat().st_size / 1024 / 1024:.1f} MB")

    return output_path


def download_composition_data(output_path: Path) -> Path:
    """下載 CIS_COMPO_bdpm.txt（成分資料）

    Args:
        output_path: 輸出路徑

    Returns:
        下載的檔案路徑
    """
    url = "https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_COMPO_bdpm.txt"

    print("正在從 BDPM 下載 CIS_COMPO_bdpm.txt...")

    response = requests.get(url, timeout=120)
    response.raise_for_status()

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "wb") as f:
        f.write(response.content)

    print(f"下載完成: {output_path}")
    return output_path


def process_bdpm_data(cis_path: Path, compo_path: Path, output_path: Path) -> Path:
    """處理 BDPM Tab-delimited 檔案並轉換為 JSON

    CIS_bdpm.txt 欄位（tab-separated, no header）:
    0: CIS code
    1: Dénomination
    2: Forme pharmaceutique
    3: Voies d'administration
    4: Statut administratif de l'AMM
    5: Type de procédure d'AMM
    6: État de commercialisation
    7: Date d'AMM
    8: StatutBdm
    9: Numéro d'autorisation européenne
    10: Titulaire
    11: Surveillance renforcée

    Args:
        cis_path: CIS_bdpm.txt 檔案路徑
        compo_path: CIS_COMPO_bdpm.txt 檔案路徑
        output_path: JSON 輸出路徑

    Returns:
        輸出檔案路徑
    """
    config = load_config()

    print(f"讀取 CIS_bdpm.txt: {cis_path}")

    # 讀取主要藥品資料 (tab-separated, no header)
    cis_columns = [
        "CIS", "Dénomination", "Forme pharmaceutique",
        "Voies d'administration", "Statut administratif de l'AMM",
        "Type de procédure d'AMM", "État de commercialisation",
        "Date d'AMM", "StatutBdm", "Numéro européen",
        "Titulaire", "Surveillance renforcée",
    ]

    # BDPM 檔案使用 Latin-1 編碼（含法文字元如 é, è, ê, ç 等）
    df = pd.read_csv(
        cis_path,
        sep="\t",
        header=None,
        names=cis_columns,
        dtype=str,
        encoding="latin-1",
        on_bad_lines="skip",
    )

    print(f"CIS_bdpm 資料筆數: {len(df)}")

    # 讀取成分資料
    if compo_path.exists():
        print(f"讀取 CIS_COMPO_bdpm.txt: {compo_path}")
        compo_columns = [
            "CIS", "Élément pharmaceutique", "Code substance",
            "Substance active", "Dosage", "Référence dosage",
            "Nature du composant", "Numéro liaison SA-FT",
        ]
        # BDPM 檔案使用 Latin-1 編碼
        compo = pd.read_csv(
            compo_path,
            sep="\t",
            header=None,
            names=compo_columns,
            dtype=str,
            encoding="latin-1",
            on_bad_lines="skip",
        )

        # 聚合成分：每個 CIS 的所有活性成分用分號連接
        active_substances = (
            compo[compo["Nature du composant"].str.strip() == "SA"]
            .groupby("CIS")["Substance active"]
            .apply(lambda x: "; ".join(x.dropna().unique()))
            .reset_index()
        )
        active_substances.columns = ["CIS", "Substance active"]

        # 合併成分到主表
        df = df.merge(active_substances, on="CIS", how="left")
    else:
        df["Substance active"] = ""

    # 清理資料
    df = df.fillna("")

    # 轉換為 JSON
    data = df.to_dict(orient="records")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"儲存至: {output_path}")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"完成！共 {len(data)} 筆藥品資料")

    # 顯示統計
    print_statistics(df, config)

    return output_path


def print_statistics(df: pd.DataFrame, config: dict):
    """印出資料統計"""
    fm = config["field_mapping"]
    status_field = fm["status"]
    ingredients_field = fm["ingredients"]

    print("\n" + "=" * 50)
    print("資料統計")
    print("=" * 50)

    if status_field in df.columns:
        print(f"\n註冊狀態分布:")
        status_counts = df[status_field].value_counts()
        for status, count in status_counts.items():
            print(f"  {status}: {count:,}")

    if ingredients_field in df.columns:
        with_ingredients = (df[ingredients_field] != "").sum()
        print(f"\n有活性成分: {with_ingredients:,} ({with_ingredients/len(df)*100:.1f}%)")


def main():
    print("=" * 60)
    print("處理法國 ANSM/BDPM 藥品資料")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    raw_dir = base_dir / "data" / "raw"
    cis_path = raw_dir / "CIS_bdpm.txt"
    compo_path = raw_dir / "CIS_COMPO_bdpm.txt"
    output_path = raw_dir / "fr_fda_drugs.json"

    # 確保 raw 目錄存在
    raw_dir.mkdir(parents=True, exist_ok=True)

    # 下載資料（如果不存在）
    if not cis_path.exists():
        download_bdpm_data(cis_path)
    else:
        print(f"使用已存在的 CIS_bdpm.txt: {cis_path}")

    if not compo_path.exists():
        download_composition_data(compo_path)
    else:
        print(f"使用已存在的 CIS_COMPO_bdpm.txt: {compo_path}")

    # 處理資料
    process_bdpm_data(cis_path, compo_path, output_path)

    print()
    print("下一步: 準備詞彙表資料")
    print("  uv run python scripts/prepare_external_data.py")


if __name__ == "__main__":
    main()
