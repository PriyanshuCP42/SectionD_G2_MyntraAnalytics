"""
etl_pipeline.py
===============
Myntra Fashion Analytics — ETL Pipeline
Team: DVA-D-G2 | Section D | Newton School of Technology

Usage:
    python scripts/etl_pipeline.py

Output:
    data/processed/myntra_cleaned.csv
    data/processed/myntra_kpis.csv
"""

import os
import sys
import logging
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Logging Configuration
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  [%(levelname)s]  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Path Configuration
# ---------------------------------------------------------------------------
BASE_DIR    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR     = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")

RAW_FILE        = os.path.join(RAW_DIR,       "myntra_products_catalog.csv")
CLEANED_FILE    = os.path.join(PROCESSED_DIR, "myntra_cleaned.csv")
KPI_FILE        = os.path.join(PROCESSED_DIR, "myntra_kpis.csv")


# ===========================================================================
# STEP 1 — EXTRACT
# ===========================================================================
def extract(filepath: str) -> pd.DataFrame:
    """
    Load the raw Myntra CSV from data/raw/ and do a quick data profile.

    Mirrors: notebooks/01_extraction.ipynb
    """
    log.info("=== STEP 1: EXTRACT ===")

    if not os.path.exists(filepath):
        log.error(f"Raw file not found: {filepath}")
        log.error("Download the dataset from: "
                  "https://www.kaggle.com/datasets/manishmathias/myntra-fashion-dataset/data")
        log.error(f"Place the CSV in: {RAW_DIR}")
        sys.exit(1)

    df = pd.read_csv(filepath)
    log.info(f"Loaded {len(df):,} rows × {df.shape[1]} columns from '{filepath}'")

    # --- Quick data profile ---
    log.info("--- Data Profile ---")
    log.info(f"Columns       : {list(df.columns)}")
    log.info(f"Dtypes        :\n{df.dtypes.to_string()}")
    log.info(f"Missing values:\n{df.isnull().sum().to_string()}")
    log.info(f"Duplicate rows: {df.duplicated().sum():,}")

    return df


# ===========================================================================
# STEP 2 — TRANSFORM / CLEAN
# ===========================================================================
def _parse_discount_offer(series: pd.Series) -> pd.Series:
    """
    Parse the DiscountOffer string column (e.g. '(50% OFF)') into a
    numeric discount percentage (float).  Returns NaN when unparseable.
    """
    # Extract digits from strings like '40% OFF', '(25% OFF)', '15%', etc.
    extracted = series.astype(str).str.extract(r"(\d+\.?\d*)")[0]
    return pd.to_numeric(extracted, errors="coerce")


def _parse_price(series: pd.Series) -> pd.Series:
    """
    Strip currency symbols / commas and convert to float.
    Handles values like 'Rs. 1,299', '₹999', '1299', etc.
    """
    cleaned = (
        series.astype(str)
        .str.replace(r"[^\d.]", "", regex=True)   # keep only digits and dot
        .str.strip()
    )
    return pd.to_numeric(cleaned, errors="coerce")


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Full cleaning and transformation pipeline.

    Operations performed:
      1. Rename columns to standard snake_case names
      2. Remove exact duplicate rows
      3. Parse MRP and DiscountPrice to numeric
      4. Parse DiscountOffer string → numeric discount_pct
      5. Derive discount_pct from prices when DiscountOffer is missing
      6. Standardise Gender and Category labels
      7. Handle missing Ratings and Reviews
      8. Drop rows where essential price data is still missing
      9. Reset index

    Mirrors: notebooks/02_cleaning.ipynb
    """
    log.info("=== STEP 2: TRANSFORM / CLEAN ===")

    # ------------------------------------------------------------------
    # 2.1  Rename columns to predictable snake_case
    # ------------------------------------------------------------------
    rename_map = {
        # Try common variations found in Kaggle Myntra datasets
        "ProductBrand"   : "brand",
        "Brand"          : "brand",
        "Price (MRP)"    : "mrp",
        "MRP"            : "mrp",
        "OriginalPrice"  : "mrp",
        "DiscountPrice"  : "discount_price",
        "SalePrice"      : "discount_price",
        "DiscountOffer"  : "discount_offer",
        "Discount"       : "discount_offer",
        "Ratings"        : "ratings",
        "Rating"         : "ratings",
        "Reviews"        : "reviews",
        "ReviewCount"    : "reviews",
        "Category"       : "category",
        "Gender"         : "gender",
        "PrimaryColor"   : "primary_color",
        "Color"          : "primary_color",
        "Description"    : "description",
        "ProductName"    : "product_name",
        "Name"           : "product_name",
    }
    # Only rename columns that actually exist
    actual_rename = {k: v for k, v in rename_map.items() if k in df.columns}
    df = df.rename(columns=actual_rename)
    log.info(f"Columns after rename: {list(df.columns)}")

    original_rows = len(df)

    # ------------------------------------------------------------------
    # 2.2  Drop exact duplicates
    # ------------------------------------------------------------------
    df = df.drop_duplicates()
    log.info(f"Removed {original_rows - len(df):,} duplicate rows "
             f"→ {len(df):,} rows remaining")

    # ------------------------------------------------------------------
    # 2.3  Parse price columns to numeric
    # ------------------------------------------------------------------
    for col in ["mrp", "discount_price"]:
        if col in df.columns:
            df[col] = _parse_price(df[col])
            log.info(f"  Parsed '{col}' to numeric — "
                     f"{df[col].isnull().sum():,} nulls remaining")

    # ------------------------------------------------------------------
    # 2.4  Parse DiscountOffer string → numeric discount_pct
    # ------------------------------------------------------------------
    if "discount_offer" in df.columns:
        df["discount_pct"] = _parse_discount_offer(df["discount_offer"])
        log.info(f"  Parsed 'discount_offer' → 'discount_pct' — "
                 f"{df['discount_pct'].isnull().sum():,} nulls")
    else:
        df["discount_pct"] = np.nan

    # ------------------------------------------------------------------
    # 2.5  Derive discount_pct from prices where still missing
    #       Formula: ((MRP - DiscountPrice) / MRP) * 100
    # ------------------------------------------------------------------
    if "mrp" in df.columns and "discount_price" in df.columns:
        mask = df["discount_pct"].isnull() & df["mrp"].notna() & df["discount_price"].notna()
        df.loc[mask, "discount_pct"] = (
            (df.loc[mask, "mrp"] - df.loc[mask, "discount_price"]) / df.loc[mask, "mrp"]
        ) * 100
        # Clip to [0, 100] — negative discounts (price > MRP) are set to 0
        df["discount_pct"] = df["discount_pct"].clip(lower=0, upper=100)
        log.info(f"  Derived 'discount_pct' from prices for {mask.sum():,} rows")

    # ------------------------------------------------------------------
    # 2.6  Standardise Gender labels
    # ------------------------------------------------------------------
    if "gender" in df.columns:
        gender_map = {
            "men"   : "Men",   "male"  : "Men",   "gents" : "Men",
            "women" : "Women", "female": "Women", "ladies": "Women",
            "kids"  : "Kids",  "child" : "Kids",  "boys"  : "Kids",
            "girls" : "Kids",  "unisex": "Unisex",
        }
        df["gender"] = (
            df["gender"]
            .astype(str).str.strip().str.lower()
            .map(gender_map)
            .fillna(df["gender"].astype(str).str.strip().str.title())
        )
        log.info(f"  Gender distribution:\n{df['gender'].value_counts().to_string()}")

    # ------------------------------------------------------------------
    # 2.7  Standardise Category labels (title-case, strip whitespace)
    # ------------------------------------------------------------------
    if "category" in df.columns:
        df["category"] = df["category"].astype(str).str.strip().str.title()
        log.info(f"  Unique categories ({df['category'].nunique()}): "
                 f"{sorted(df['category'].unique())[:15]} ...")

    # ------------------------------------------------------------------
    # 2.8  Handle missing Ratings and Reviews
    #       • Ratings  → fill with median per category (or global median)
    #       • Reviews  → fill with 0 (no reviews recorded ≠ missing)
    # ------------------------------------------------------------------
    if "ratings" in df.columns:
        df["ratings"] = pd.to_numeric(df["ratings"], errors="coerce")
        # Cap ratings at 5 (data quality guard)
        df["ratings"] = df["ratings"].clip(upper=5.0)
        if "category" in df.columns:
            df["ratings"] = df.groupby("category")["ratings"].transform(
                lambda x: x.fillna(x.median())
            )
        df["ratings"] = df["ratings"].fillna(df["ratings"].median())
        log.info(f"  'ratings' nulls after imputation: {df['ratings'].isnull().sum():,}")

    if "reviews" in df.columns:
        df["reviews"] = pd.to_numeric(df["reviews"], errors="coerce").fillna(0).astype(int)
        log.info(f"  'reviews' nulls after fill: {df['reviews'].isnull().sum():,}")

    # ------------------------------------------------------------------
    # 2.9  Drop rows where MRP or DiscountPrice is still null
    #       (cannot compute KPIs without price data)
    # ------------------------------------------------------------------
    essential_cols = [c for c in ["mrp", "discount_price"] if c in df.columns]
    before = len(df)
    df = df.dropna(subset=essential_cols)
    log.info(f"  Dropped {before - len(df):,} rows with null price data "
             f"→ {len(df):,} rows remaining")

    # ------------------------------------------------------------------
    # 2.10 Reset index
    # ------------------------------------------------------------------
    df = df.reset_index(drop=True)
    log.info(f"Transform complete — final shape: {df.shape}")

    return df


# ===========================================================================
# STEP 3 — KPI COMPUTATION
# ===========================================================================
def compute_kpis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute the 5 project KPIs at the product level and return an
    enriched DataFrame.  Aggregated views are saved to myntra_kpis.csv.

    KPIs (per README KPI Framework):
      1. discount_pct              — already computed in transform()
      2. effective_revenue_index   — DiscountPrice × log(1 + Reviews)
      3. rating_to_discount_corr   — logged per category (Pearson r)
      4. category_value_score      — 0.4×Price_norm + 0.3×Rating_norm + 0.3×log(Reviews)_norm
      5. brand_concentration_index — share of top-10 brands (scalar, logged)

    Mirrors: notebooks/05_final_load_prep.ipynb
    """
    log.info("=== STEP 3: KPI COMPUTATION ===")

    # ------------------------------------------------------------------
    # KPI 2 — Effective Revenue Index
    # ------------------------------------------------------------------
    if "discount_price" in df.columns and "reviews" in df.columns:
        df["effective_revenue_index"] = (
            df["discount_price"] * np.log1p(df["reviews"])
        )
        log.info(f"  KPI 2 'effective_revenue_index' computed — "
                 f"mean = {df['effective_revenue_index'].mean():.2f}")

    # ------------------------------------------------------------------
    # KPI 4 — Category Value Score
    #   Normalise each component to [0,1] using min-max scaling, then
    #   apply the weighted composite: 0.4*Price + 0.3*Rating + 0.3*log(Reviews)
    # ------------------------------------------------------------------
    def minmax(series: pd.Series) -> pd.Series:
        rng = series.max() - series.min()
        return (series - series.min()) / rng if rng > 0 else pd.Series(0.0, index=series.index)

    components = {}
    if "discount_price" in df.columns:
        components["price_norm"] = minmax(df["discount_price"])
    if "ratings" in df.columns:
        components["rating_norm"] = minmax(df["ratings"])
    if "reviews" in df.columns:
        components["log_reviews_norm"] = minmax(np.log1p(df["reviews"]))

    if len(components) == 3:
        df["category_value_score"] = (
            0.4 * components["price_norm"]
            + 0.3 * components["rating_norm"]
            + 0.3 * components["log_reviews_norm"]
        )
        log.info(f"  KPI 4 'category_value_score' computed — "
                 f"mean = {df['category_value_score'].mean():.4f}")

    # ------------------------------------------------------------------
    # KPI 3 — Rating-to-Discount Correlation (per category, logged)
    # ------------------------------------------------------------------
    if "category" in df.columns and "ratings" in df.columns and "discount_pct" in df.columns:
        corr_by_cat = (
            df.groupby("category")[["ratings", "discount_pct"]]
            .corr()
            .unstack()["ratings"]["discount_pct"]
            .reset_index()
            .rename(columns={"discount_pct": "rating_discount_corr"})
        )
        log.info(f"  KPI 3 'rating_discount_corr' by category:\n"
                 f"{corr_by_cat.to_string(index=False)}")

    # ------------------------------------------------------------------
    # KPI 5 — Brand Concentration Index
    # ------------------------------------------------------------------
    if "brand" in df.columns:
        top10_count = df["brand"].value_counts().head(10).sum()
        bci = (top10_count / len(df)) * 100
        log.info(f"  KPI 5 Brand Concentration Index (top-10) = {bci:.1f}%")
        df["_bci"] = bci   # store as constant column for reference

    return df


# ===========================================================================
# STEP 4 — LOAD
# ===========================================================================
def load(df: pd.DataFrame, cleaned_path: str, kpi_path: str) -> None:
    """
    Save the cleaned + KPI-enriched DataFrame to data/processed/.

    Two files are written:
      • myntra_cleaned.csv  — full cleaned dataset (all columns)
      • myntra_kpis.csv     — category-level KPI aggregations for Tableau
    """
    log.info("=== STEP 4: LOAD ===")

    os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)

    # --- Full cleaned dataset ---
    df.to_csv(cleaned_path, index=False)
    log.info(f"  Cleaned data saved → '{cleaned_path}' ({len(df):,} rows)")

    # --- Category-level KPI aggregation for Tableau ---
    agg_cols = {}
    if "mrp"          in df.columns: agg_cols["avg_mrp"]            = ("mrp",          "mean")
    if "discount_price" in df.columns: agg_cols["avg_discount_price"] = ("discount_price","mean")
    if "discount_pct" in df.columns: agg_cols["avg_discount_pct"]   = ("discount_pct", "mean")
    if "ratings"      in df.columns: agg_cols["avg_rating"]         = ("ratings",      "mean")
    if "reviews"      in df.columns: agg_cols["total_reviews"]      = ("reviews",      "sum")
    if "effective_revenue_index" in df.columns:
        agg_cols["avg_eri"] = ("effective_revenue_index", "mean")
    if "category_value_score"    in df.columns:
        agg_cols["avg_cvs"] = ("category_value_score",    "mean")

    group_cols = [c for c in ["category", "gender"] if c in df.columns]

    if group_cols and agg_cols:
        kpi_df = df.groupby(group_cols).agg(**agg_cols).reset_index()
        kpi_df["listing_count"] = df.groupby(group_cols).size().values
        kpi_df.to_csv(kpi_path, index=False)
        log.info(f"  KPI aggregations saved → '{kpi_path}' ({len(kpi_df):,} rows)")
    else:
        log.warning("  Skipping KPI aggregation — required columns not found.")


# ===========================================================================
# PIPELINE ORCHESTRATOR
# ===========================================================================
def run_pipeline(raw_filepath: str = RAW_FILE) -> pd.DataFrame:
    """
    Run the full ETL pipeline end-to-end.

    Parameters
    ----------
    raw_filepath : str
        Path to the raw Myntra CSV file.  Defaults to data/raw/myntra_products_catalog.csv

    Returns
    -------
    pd.DataFrame
        The fully cleaned and KPI-enriched DataFrame.
    """
    log.info("╔══════════════════════════════════════════════╗")
    log.info("║  Myntra Analytics — ETL Pipeline Starting   ║")
    log.info("╚══════════════════════════════════════════════╝")

    df = extract(raw_filepath)
    df = transform(df)
    df = compute_kpis(df)
    load(df, CLEANED_FILE, KPI_FILE)

    log.info("╔══════════════════════════════════════════════╗")
    log.info("║  Pipeline complete. Files written to         ║")
    log.info(f"║  {PROCESSED_DIR:<44}║")
    log.info("╚══════════════════════════════════════════════╝")

    return df


# ===========================================================================
# ENTRY POINT
# ===========================================================================
if __name__ == "__main__":
    # Allow passing a custom CSV path as CLI argument
    # e.g.  python scripts/etl_pipeline.py data/raw/my_file.csv
    custom_path = sys.argv[1] if len(sys.argv) > 1 else RAW_FILE
    run_pipeline(raw_filepath=custom_path)
