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
| Data Lead | Preet | `github-handle` |
| ETL Lead | Shourya | `github-handle` |
| Analysis Lead | Mihika | `github-handle` |
| Visualization Lead | Vaageesh | `github-handle` |
| Strategy Lead | Gauri | `github-handle` |
| PPT & Quality Lead | Pratyaksha | `github-handle` |

> **Note:** Replace all `github-handle` placeholders with actual GitHub usernames. Every member must have visible commits and pull requests.

---

## Business Problem

Myntra, India's leading online fashion and lifestyle retailer, operates in a fiercely competitive e-commerce landscape where pricing strategy, brand positioning, and discount depth directly determine revenue and customer retention. The category management and merchandising teams struggle to identify which product categories, brands, and gender segments drive the most value — and whether current discount structures are eroding margin without meaningfully improving volume. This project serves the Head of Category Management and the Pricing Strategy team as primary decision-makers.

**Core Business Question**

> Which product categories, brands, and customer segments on Myntra offer the highest revenue potential, and how should discount and pricing strategies be optimised to maximise both sales volume and profitability?

**Decision Supported**

> This analysis will enable the Category Management team to prioritise high-performing brands and categories for promotional spend, restructure discount tiers for underperforming segments, and align inventory investments with actual customer demand — directly improving gross margin and reducing unsold stock.

---

## Dataset

| Attribute | Details |
|---|---|
| **Source Name** | Kaggle — Raw Dataset (manishmathias/myntra-fashion-dataset) |
| **Direct Access Link** | [https://www.kaggle.com/datasets/manishmathias/myntra-fashion-dataset/data](https://www.kaggle.com/datasets/manishmathias/myntra-fashion-dataset/data) |
| **Row Count** | ~1,00,000+ product listings (verify after download) |
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

| KPI | Definition | Formula / Computation |
|---|---|---|
| **Average Discount Rate (%)** | Measures how aggressively products are discounted on average across categories | `((MRP − DiscountPrice) / MRP) × 100` — computed per category in `04_statistical_analysis.ipynb` |
| **Effective Revenue Index** | Proxy revenue score combining sell-through price with review volume as a demand signal | `DiscountPrice × log(1 + Reviews)` — computed per brand in `05_final_load_prep.ipynb` |
| **Rating-to-Discount Correlation** | Measures whether heavier discounts correlate with better or worse customer ratings | Pearson correlation between `Discount %` and `Ratings` in `04_statistical_analysis.ipynb` |
| **Category Value Score** | Ranks categories by their balance of high price, high rating, and high review count | Composite normalised score: `0.4×Price + 0.3×Rating + 0.3×log(Reviews)` in `05_final_load_prep.ipynb` |
| **Brand Concentration Index** | Share of total listings held by the top 10 brands — measures market concentration | `(Top 10 Brand Listings / Total Listings) × 100` in `03_eda.ipynb` |

Document KPI logic clearly in `notebooks/04_statistical_analysis.ipynb` and `notebooks/05_final_load_prep.ipynb`.

---

## Tableau Dashboard

| Item | Details |
|---|---|
| **Dashboard URL** | _Paste Tableau Public link here after publishing_ |
| **Executive View** | High-level KPI summary: Total Listings, Average Discount Rate, Top Revenue Category, Top Rated Brand — filterable by Gender |
| **Operational View** | Category and brand drill-down: Discount vs Rating scatter, Top Brands by Effective Revenue, Category Value Score ranking, Price distribution by Gender segment |
| **Main Filters** | Gender, Category, Brand, Discount Range (slider), Rating Range |

Store dashboard screenshots in [`tableau/screenshots/`](tableau/screenshots/) and document the public links in [`tableau/dashboard_links.md`](tableau/dashboard_links.md).

---

## Key Insights

_To be populated after full analysis. Template entries shown below as placeholders — replace with data-backed findings from your notebooks._

1. **Discount depth does not drive ratings** — A weak or negative correlation between discount percentage and customer ratings suggests that price cuts alone do not improve perceived product quality or customer satisfaction.
2. **Topwear dominates listing volume but Footwear commands higher average price points** — indicating a cross-category opportunity to push premium Footwear listings harder.
3. **Women's fashion accounts for the majority of listings yet shows higher average discount rates** — pointing to potential margin erosion that requires category-level pricing review.
4. **Top 10 brands account for a disproportionate share of all listings** — reflecting high market concentration; long-tail brands need visibility support or should be rationalised.
5. **Products priced in the ₹500–₹1,500 mid-range receive the highest volume of reviews** — suggesting this price band captures the largest active buyer cohort.
6. **Heavily discounted products (>50% off) receive fewer reviews on average** — implying that deep discounts may signal low-quality perception rather than driving purchases.
7. **Kids' fashion is the smallest segment by listing count but carries above-average MRP** — an underserved, high-margin segment worth targeted expansion.
8. **Certain brand–category combinations consistently achieve ratings above 4.0 with minimal discounting** — identifying brand-category pairs that can sustain premium pricing.
9. _Insight 9 — to be filled after EDA_
10. _Insight 10 — to be filled after statistical analysis_

---

## Recommendations

| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | Discount depth does not improve ratings | Cap discount offers at 30–35% for categories where ratings are already high; redirect discount budget to loyalty rewards instead | Estimated 5–8% improvement in gross margin on top-rated SKUs |
| 2 | Women's segment shows high discount rates with average ratings | Conduct a SKU rationalisation for low-rated, high-discount women's products; reduce listing clutter and focus on proven brands | Reduce markdown losses by an estimated 10–15% in the Women's segment |
| 3 | Mid-range ₹500–₹1,500 segment drives highest engagement | Prioritise this price band for new brand onboarding and seasonal campaign targeting | Estimated 12–18% uplift in review volume, improving social proof for conversion |
| 4 | Kids' fashion is high-margin and underserved | Increase Kids' category SKU count by sourcing 2–3 premium brand partnerships; run targeted back-to-school and festive campaigns | Expand Kids' category GMV by an estimated 20% within one season |
| 5 | Top brand concentration creates platform dependency risk | Develop a Myntra Emerging Brands programme to uplift mid-tier brands with curated visibility — reducing top-10 brand dependency | Improve platform resilience and diversify revenue across 30+ brands |

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
6. **Recommend** — 5 data-backed business recommendations delivered, each tied to a specific KPI finding.
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
- [ ] 3–5 actionable recommendations with impact estimates
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
| Priyanshu (Project Lead) | Support | Support | Support | Support | Support | Support | Owner |
| Preet (Data Lead) | Owner | Support | Support | Support | Support | Support | Support |
| Shourya (ETL Lead) | Support | Owner | Support | Support | Support | Support | Support |
| Mihika (Analysis Lead) | Support | Support | Owner | Owner | Support | Support | Support |
| Vaageesh (Viz Lead) | Support | Support | Support | Support | Owner | Support | Support |
| Gauri (Strategy Lead) | Support | Support | Support | Support | Support | Owner | Support |
| Pratyaksha (PPT & Quality Lead) | Support | Support | Support | Support | Support | Owner | Owner |

_Declaration: We confirm that the above contribution details are accurate and verifiable through GitHub Insights, PR history, and submitted artifacts._

**Team Lead Name:** Priyanshu

**Date:** _______________

---

## Academic Integrity

All analysis, code, and recommendations in this repository are the original work of Team DVA-D-G2 listed above. Free-riding is tracked via GitHub Insights and pull request history. Any mismatch between the contribution matrix and actual commit history may result in individual grade adjustments.

---

*Newton School of Technology — Data Visualization & Analytics | Capstone 2 | SectionD_G2_MyntraAnalytics*
