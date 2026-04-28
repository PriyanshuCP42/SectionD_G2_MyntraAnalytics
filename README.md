# SectionD_G2_MyntraAnalytics


## Project Overview

| Field | Details |
|---|---|
| **Project Title** | Myntra Fashion Analytics — Decoding India's Online Fashion Market |
| **Sector** | E-Commerce / Fashion Retail |
| **Team ID** | DVA-D-G2 |
| **Section** | Section D |
| **Faculty Mentor** | Archit Raj|
| **Institute** | Newton School of Technology |
| **Submission Date** | _To be filled by team_ |

### Team Members

| Role | Name | GitHub Username |
|---|---|---|
| Project Lead | Priyanshu | `PriyanshuCP42` |
| Data Lead | Preet | `preetvardhan10` |
| ETL Lead | Shourya | `shourya2006` |
| Analysis Lead | Mihika | `mihikamathur` |
| Visualization Lead | Vaageesh | `Vaageesh-Git` |
| Strategy Lead | Gauri | `gaurimehrotra1623 ` |
| PPT & Quality Lead | Pratyaksha | `Pratyaksha37` |

---

### 📊 Project Snapshot (At a Glance)
- **Total Catalogue Size:** 526,564 Fashion Products
- **Brand Portfolio:** 1,719+ Unique Brands
- **Total Revenue (Captured):** ₹68.9 Cr
- **Margin Leakage:** ₹58.21 Cr (Potential revenue lost to discounts)
- **Revenue Split:** 62.79% Women | 37.21% Men
- **Platform Efficiency:** Only ~₹58 collected for every ₹100 listed (45.9% Value Erosion)

---

Myntra, India's leading online fashion and lifestyle retailer, operates in a fiercely competitive e-commerce landscape where pricing strategy, brand positioning, and discount depth directly determine revenue and customer retention. The category management and merchandising teams struggle to identify which product categories, brands, and gender segments drive the most value — and whether current discount structures are eroding margin without meaningfully improving volume. This project serves the Head of Category Management and the Pricing Strategy team as primary decision-makers.

**Core Business Question**

> How can Myntra optimize its product assortment and pricing strategy across different gender categories and sub-categories to maximize value-for-money perception and rating performance?

**Decision Supported**

> This analysis will enable stakeholders (Category Managers and Pricing Strategists) to decide which specific product categories require price adjustments (discounts) to improve customer satisfaction ratings and which brands/categories are currently underperforming in terms of review volume versus rating quality.

---

## Dataset

| Attribute | Details |
|---|---|
| **Source Name** | Kaggle — Raw Dataset (manishmathias/myntra-fashion-dataset) |
| **Direct Access Link** | [https://www.kaggle.com/datasets/manishmathias/myntra-fashion-dataset/data](https://www.kaggle.com/datasets/manishmathias/myntra-fashion-dataset/data) |
| **Row Count** | 526,564 product listings |
| **Column Count** | 10+ meaningful analytical columns |
| **Time Period Covered** | December 2021 — January 2023 |
| **Format** | CSV |

**Key Columns Used**

| Column Name | Description | Role in Analysis |
|---|---|---|
| `ProductBrand` | Brand name of the fashion product | Brand-level segmentation and revenue grouping |
| `Price (MRP)` | Maximum retail price before discount | Baseline for pricing analysis and margin calculation |
| `DiscountPrice` | Final selling price after discount applied | Used to compute Discount % and Effective Revenue |
| `DiscountOffer` | Discount label / percentage offered | KPI computation for Average Discount Rate |
| `Ratings` | Customer rating score (out of 5) | Quality segmentation and customer satisfaction KPI |
| `Reviews` | Number of customer reviews | Proxy for sales volume and demand signal |
| `Category` | Top-level product category (e.g., Topwear, Footwear) | Category-level aggregation and drill-down filtering |
| `Gender` | Target customer gender (Men / Women / Kids) | Segment-level performance comparison |
| `PrimaryColor` | Dominant product colour | Trend analysis and visual merchandising insight |
| `Description` | Product description text | NLP-based feature tagging (optional enrichment) |

For full column definitions, see [`docs/data_dictionary.md`](docs/data_dictionary.md).

---


## KPI Framework

| KPI | Definition | Value | Business Interpretation |
|---|---|---|---|
| **Total Revenue** | Total realized revenue after discounts | ₹689,054,937 | High volume driven by mid-segment sales |
| **Total SKU Count** | Total number of listed products | 526,564 | Massive assortment requiring high inventory management |
| **Revenue Share (W)** | % of revenue from women’s category | 62.79% | Primary revenue engine of the platform |
| **Average MRP** | Mean original price across products | ₹2,414 | Indicates mid-premium catalogue positioning |
| **Average Rating** | Mean customer rating (out of 5) | 4.095 | Strong overall customer satisfaction baseline |
| **Average Discount %** | Mean discount offered across platform | 41.98% | Significant reliance on discounting for sales volume |
| **Margin Leakage** | Estimated revenue loss due to markdowns | ₹58.21 Cr | Critical area for profitability optimization |
| **Disc–Rating Corr** | Relationship between discount depth and ratings | 0.10 | **Weak Correlation:** Discounts do not drive quality perception |
| **VFM Index** | Value-for-Money composite score | 2.015 | Moderate perceived value across the catalogue |

> **Note:** For detailed KPI logic and computation, refer to [`notebooks/04_statistical_analysis.ipynb`](notebooks/04_statistical_analysis.ipynb).

---

## Tableau Dashboard

| Item                       | Details                                                                                                                                                                                                                                                                                                                     |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Dashboard Views**        | 3 integrated dashboards: <br>1. **Category & Brand Revenue Intelligence** <br>2. **Value for Money & Assortment Optimization** <br>3. **Discount Depth & Margin Health**                                                                                                                                                    |
| **Executive KPIs**         | Revenue, SKU Count, Revenue Split (Gender), Avg Price, VFM Index, Ratings, Discount %, Margin Leakage                                                                                                                                                                                                                       |
| **Key Visuals**            | - Gender revenue split donut chart <br>- SKU distribution treemap <br>- Category × Gender revenue bars <br>- Brand SKU ranking <br>- Price vs Rating scatter (Brand Quadrant) <br>- VFM index by sub-category <br>- Discount vs Rating scatter <br>- Discount heatmaps & band distribution <br>- Margin leakage by category |
| **Main Filters**           | Brand Name, Category, Gender, Individual Category, Price Range, Discount %                                                                                                                                                                                                                                                  |
| **Analytical Focus Areas** | - Revenue concentration <br>- Value-for-money optimization <br>- Discount effectiveness vs ratings <br>- Margin leakage identification                                                                                                                                                                                      |
| **Interactivity**          | Fully filterable across category, gender, and pricing dimensions enabling drill-down from category → sub-category → brand                                                                                                                                                                                                   |

Store dashboard screenshots in [`tableau/screenshots/`](tableau/screenshots/) and document the public links in [`tableau/dashboard_links.md`](tableau/dashboard_links.md).

---

## Key Insights & Findings

### 🛍️ Market & Segment Performance
- **Women's Segment Dominance:** Accounts for **62.79%** of total revenue. While it is the core business driver, it is also the most heavily discounted, raising significant margin concerns.
- **Top Revenue Categories:** Indian Wear and Western Wear outperform all other categories. Strategic investment should focus on protecting these high-volume segments.

### 💰 Pricing & Discounting Audit
- **Unsustainable Discounting:** Widespread discounting (Avg **41.98%**, with 42% of SKUs over 50% off) indicates a heavy reliance on markdowns that may be unsustainable.
- **Significant Margin Leakage:** Estimated **₹58.21 Cr** in potential revenue is lost to discounting, representing the biggest financial impact on profitability.
- **Ineffective Deep Discounts:** Products with >50% discounts have an average rating of only **1.48**, suggesting deep markdowns signal low quality rather than attracting value-conscious buyers.

### ⚖️ Value & Quality Perception
- **Price-Rating Independence:** A weak correlation of **0.10** between discounts and ratings confirms that price cuts have almost no impact on customer satisfaction.
- **Premium Parity:** Higher-priced items do not consistently achieve better ratings, weakening the justification for premium pricing without accompanying quality differentiators.

### 📦 Assortment & Supply Chain
- **SKU Over-Supply:** High concentration in categories like Sarees, Kurtas, and Tops indicates a risk of over-supply and stock aging.
- **Brand Dependency:** Top brands like **Pothys, Roadster, and Kalini** dominate SKU counts. High dependency on a few brands increases platform risk.
- **Niche Opportunities:** Sub-categories like Accessories and Innerwear deliver high Value-for-Money (VFM) but are currently under-leveraged in revenue contribution.

---

## Recommendations

| #  | Insight                                                                | Recommendation                                                                                                                             | Expected Impact                                                                  |
| -- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| 1  | Heavy discounting (~42% avg, 42% SKUs >50%) with ₹58 Cr margin leakage | **Rationalize discounting strategy** — cap discounts at 30–40% for most categories and restrict >50% discounts to clearance inventory only | Reduce margin leakage by **15–25%** while maintaining sales volume               |
| 2  | Discount has negligible impact on ratings (correlation = 0.10)         | **Shift from price-led to value-led strategy** — invest in product quality, brand positioning, and reviews instead of deeper discounts     | Improve average ratings and long-term customer trust without sacrificing margins |
| 3  | Women’s category drives ~63% revenue but is highly discounted          | **Optimize women’s assortment** — reduce low-rated, high-discount SKUs and prioritize high VFM products                                    | Improve profitability of the largest revenue segment by **10–15%**               |
| 4  | High discount products have very low ratings (~1.48)                   | **Flag and prune poor-performing SKUs** — remove or rework products with high discounts and low ratings                                    | Increase overall platform rating and reduce negative customer perception         |
| 5  | Indian wear & Western wear dominate revenue but also margin leakage    | **Category-level pricing optimization** — introduce tighter discount bands and premium sub-lines in these categories                       | Recover margins from top revenue categories while sustaining demand              |
| 6  | High VFM SKUs (~79K) are under-leveraged                               | **Promote high VFM products** via search ranking, ads, and recommendations                                                                 | Increase conversion rates and customer satisfaction simultaneously               |
| 7  | Brand concentration is high (few brands dominate SKU share)            | **Diversify brand portfolio** — onboard and promote emerging brands with strong VFM scores                                                 | Reduce dependency risk and improve assortment variety                            |
| 8  | Optimal size depth ~5–6 options                                        | **Standardize size assortment** around high-performing size bands                                                                          | Reduce inventory complexity and improve availability efficiency                  |
| 9  | No clear advantage of premium pricing on ratings                       | **Re-evaluate premium pricing strategy** — ensure premium SKUs justify price via quality, branding, or exclusivity                         | Improve premium segment conversion and reduce price resistance                   |

---

## Repository Structure

```text
SectionD_G2_MyntraAnalytics/
│
├── README.md
│
├── data/
│   ├── raw/                         # Original Myntra dataset from Kaggle (never edited)
│   └── processed/                   # Cleaned output from ETL pipeline
│
├── notebooks/
│   ├── 01_extraction.ipynb          # Load raw CSV, initial inspection, data profiling
│   ├── 02_cleaning.ipynb            # Handle nulls, standardise formats, parse discount %
│   ├── 03_eda.ipynb                 # Distributions, brand/category analysis, outlier detection
│   ├── 04_statistical_analysis.ipynb # Correlation, regression, hypothesis testing on KPIs
│   └── 05_final_load_prep.ipynb     # KPI computation, final dataset export for Tableau
│
├── scripts/
│   └── etl_pipeline.py              # Modular ETL script (mirrors notebook 01 + 02 logic)
│
├── tableau/
│   ├── screenshots/                 # Dashboard screenshots (executive + operational views)
│   └── dashboard_links.md           # Tableau Public URL
│
├── reports/
│   ├── README.md
│   ├── project_report.pdf           # Final project report (10–15 pages)
│   └── presentation.pdf             # Final presentation deck (10–12 slides)
│
├── docs/
│   └── data_dictionary.md           # Full column definitions and data notes
│
├── DVA-oriented-Resume/             # Individual updated resumes
└── DVA-focused-Portfolio/           # Individual portfolio links / case studies
```

---

## Analytical Pipeline

The project follows a structured 7-step workflow:

1. **Define** — Sector selected (E-Commerce / Fashion Retail), problem statement scoped around Myntra pricing and category strategy, mentor approval obtained at Gate 1.
2. **Extract** — Raw Myntra dataset sourced from Kaggle and committed to `data/raw/`; data dictionary drafted in `docs/data_dictionary.md`.
3. **Clean and Transform** — Cleaning pipeline built in `notebooks/02_cleaning.ipynb`: handle missing values in `Ratings` and `Reviews`, parse `DiscountOffer` string into numeric discount percentage, standardise `Gender` and `Category` labels, remove duplicate product entries.
4. **Analyze** — EDA in notebook `03` (brand concentration, price distributions, rating patterns); Statistical analysis in notebook `04` (Pearson correlation between discount and rating, OLS regression of price on reviews, segment hypothesis testing).
5. **Visualize** — Interactive Tableau dashboard built with Executive KPI view and Operational drill-down; published on Tableau Public.
6. **Recommend** — 10 data-backed business recommendations delivered, each tied to a specific KPI finding.
7. **Report** — Final project report and presentation deck completed and exported to PDF in `reports/`.

---

## Tech Stack

| Tool | Status | Purpose |
|---|---|---|
| Python + Jupyter Notebooks | Mandatory | ETL, cleaning, EDA, statistical analysis, and KPI computation |
| Google Colab | Supported | Cloud notebook execution environment |
| Tableau Public | Mandatory | Dashboard design, publishing, and sharing |
| GitHub | Mandatory | Version control, collaboration, and contribution audit |
| SQL | Optional | Initial data extraction only, if documented |

**Python Libraries Used:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`

---

## Evaluation Rubric

| Area | Marks | Focus |
|---|---|---|
| Problem Framing | 10 | Is the business question clear and well-scoped? |
| Data Quality and ETL | 15 | Is the cleaning pipeline thorough and documented? |
| Analysis Depth | 25 | Are statistical methods applied correctly with insight? |
| Dashboard and Visualization | 20 | Is the Tableau dashboard interactive and decision-relevant? |
| Business Recommendations | 20 | Are insights actionable and well-reasoned? |
| Storytelling and Clarity | 10 | Is the presentation professional and coherent? |
| **Total** | **100** | |

> Marks are awarded for analytical thinking and decision relevance, not chart quantity, visual decoration, or code length.

---

## Submission Checklist

**GitHub Repository**

- [ ] Public repository created: `SectionD_G2_MyntraAnalytics`
- [ ] All notebooks committed in `.ipynb` format
- [ ] `data/raw/` contains the original, unedited Myntra CSV from Kaggle
- [ ] `data/processed/` contains the cleaned pipeline output
- [ ] `tableau/screenshots/` contains dashboard screenshots (executive + operational views)
- [ ] `tableau/dashboard_links.md` contains the Tableau Public URL
- [ ] `docs/data_dictionary.md` is complete with all 10+ column definitions
- [ ] `README.md` explains the project, dataset, KPIs, and team
- [ ] All 7 members have visible commits and pull requests

**Tableau Dashboard**

- [ ] Published on Tableau Public and accessible via public URL
- [ ] At least one interactive filter included (Gender, Category, or Brand)
- [ ] Dashboard directly addresses the pricing and category strategy business problem

**Project Report**

- [ ] Final report exported as PDF into `reports/` (10–15 pages)
- [ ] Cover page, executive summary, sector context, problem statement
- [ ] Data description, cleaning methodology, KPI framework
- [ ] EDA with written insights, statistical analysis results
- [ ] Dashboard screenshots and explanation
- [ ] 8–12 key insights in decision language
- [ ] 10 actionable recommendations with impact estimates
- [ ] Contribution matrix matches GitHub history

**Presentation Deck**

- [ ] Final presentation exported as PDF into `reports/` (10–12 slides)
- [ ] Title slide through recommendations, impact, limitations, and next steps

**Individual Assets**

- [ ] DVA-oriented resume updated to include this capstone
- [ ] Portfolio link or project case study added

---

## Contribution Matrix

This table must match evidence in GitHub Insights, PR history, and committed files.

| Team Member | Dataset and Sourcing | ETL and Cleaning | EDA and Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT and Viva |
|---|---|---|---|---|---|---|---|
| Priyanshu (Project Lead) | ✓ |  |  | ✓ |  |  |  |
| Preet (Data Lead) |  | ✓ |  |  |  | | |
| Shourya (ETL Lead) |  | ✓ | ✓ |  |  |  |  |
| Mihika (Analysis Lead) | ✓ |  |  | ✓ |  |  |  |
| Vaageesh (Viz Lead) |  |  |  |  | ✓ |  |  |
| Gauri (Strategy Lead) | ✓ |  | | | ✓ |  |  |
| Pratyaksha (PPT & Quality Lead) |  | |  | |  | ✓ | ✓ |

_Declaration: We confirm that the above contribution details are accurate and verifiable through GitHub Insights, PR history, and submitted artifacts._

**Team Lead Name:** Priyanshu

**Date:** _______________

---

## Academic Integrity

All analysis, code, and recommendations in this repository are the original work of Team DVA-D-G2 listed above. Free-riding is tracked via GitHub Insights and pull request history. Any mismatch between the contribution matrix and actual commit history may result in individual grade adjustments.

---

*Newton School of Technology — Data Visualization & Analytics | Capstone 2 | SectionD_G2_MyntraAnalytics*
