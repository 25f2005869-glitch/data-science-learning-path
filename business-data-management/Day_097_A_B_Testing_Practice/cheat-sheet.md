# 🧠 Day 097 — A/B Testing Practice — Cheat Sheet

![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Business Data Management](https://img.shields.io/badge/Business%20Data%20Management-Day%20097-blue?style=for-the-badge)
![A/B Testing](https://img.shields.io/badge/A%2FB%20Testing-Cheat%20Sheet-green?style=for-the-badge)

---

## 👤 Metadata

- **Author:** Saloni Tiwari
- **Programme:** IIT Madras BS Degree — Diploma Level
- **Day:** 097
- **Topic:** A/B Testing Practice

---

## 1. A/B Testing — Quick Definition

**A/B Testing** is an experimental method used to compare two groups or versions using predefined metrics.

- **Group A:** Control
- **Group B:** Treatment

---

## 2. Basic A/B Testing Structure

**Users**

→ **Control / Treatment**

→ **User Behaviour**

→ **Conversions**

→ **Business Metrics**

→ **Comparison**

---

## 3. Main Dataset Fields

| Field | Meaning |
|---|---|
| User_ID | User identifier |
| Date | Experiment date |
| Group | A or B |
| Customer_Segment | Customer type |
| Device | User device |
| Channel | Acquisition channel |
| Age | User age |
| Visitors | Number of visitors |
| Converted | Conversion indicator |
| Order_Value | Order value |
| Revenue | Revenue generated |
| Conversion_Status | Conversion status |

---

## 4. Control vs Treatment

| Group | Meaning |
|---|---|
| A | Control |
| B | Treatment |

**Control:** Reference version.

**Treatment:** Changed version being tested.

---

## 5. Customer Segments

- New
- Regular
- Loyal
- At Risk

---

## 6. Conversion

In the dataset:

- `1` = Converted
- `0` = Not Converted

**Total Conversions = SUM(Converted)**

---

## 7. Conversion Rate

### Formula

**Conversion Rate = (Conversions / Visitors) × 100**

Example:

Visitors = 100

Conversions = 15

Conversion Rate = **15%**

---

## 8. Conversion Rate Difference

### Formula

**Difference = Treatment Conversion Rate − Control Conversion Rate**

For this project:

**Difference = Group B Rate − Group A Rate**

This is a descriptive comparison.

---

## 9. Order Value

**Order_Value** represents the value associated with a conversion.

Non-converted records have an order value of zero in the cleaned practice dataset.

---

## 10. Revenue

### Formula

**Revenue = Converted × Order_Value**

Example:

Converted = 1

Order Value = ₹5,000

Revenue = **₹5,000**

---

## 11. Average Order Value

### Formula

**AOV = Revenue / Conversions**

Example:

Revenue = ₹50,000

Conversions = 10

AOV = **₹5,000**

---

## 12. Data Cleaning Checklist

Before analysis:

- [ ] Remove extra spaces
- [ ] Standardize capitalization
- [ ] Check Group values
- [ ] Check missing Age
- [ ] Check invalid Age
- [ ] Check missing Visitors
- [ ] Check invalid Visitors
- [ ] Validate Converted values
- [ ] Check missing Order Value
- [ ] Check negative Order Value
- [ ] Recalculate Revenue
- [ ] Rebuild Conversion Status
- [ ] Remove exact duplicates

---

## 13. Cleaning Rules

| Field | Rule |
|---|---|
| Group | Strip spaces and standardize A/B |
| Customer_Segment | Standardize text |
| Device | Standardize text |
| Channel | Standardize text |
| Age | Replace missing/invalid values with median |
| Visitors | Replace missing/invalid values with 1 |
| Converted | Keep only 0 or 1 |
| Order_Value | Replace missing/negative values with 0 |
| Revenue | Recalculate |
| Conversion_Status | Rebuild |
| Duplicate | Remove exact duplicates |

---

## 14. A/B Testing Workflow

**Inspect**

↓

**Identify Issues**

↓

**Clean**

↓

**Validate**

↓

**Analyse**

↓

**Compare A and B**

↓

**Interpret**

---

## 15. Group-Level Analysis

Compare:

- Visitors
- Conversions
- Conversion Rate
- Revenue
- Average Order Value

---

## 16. Segment Analysis

Analyse each segment separately:

**New**

**Regular**

**Loyal**

**At Risk**

Useful metrics:

- Visitors
- Conversions
- Conversion Rate
- Revenue
- Average Order Value

---

## 17. Daily Analysis

Track:

- Date
- Group
- Visitors
- Conversions
- Conversion Rate
- Revenue

Use daily analysis to observe patterns over time.

---

## 18. Main KPIs

| KPI | Formula |
|---|---|
| Visitors | Count/Sum of visitors |
| Conversions | Sum of Converted |
| Conversion Rate | Conversions / Visitors × 100 |
| Revenue | Converted × Order Value |
| AOV | Revenue / Conversions |

---

## 19. Excel Functions

Useful functions:

- `SUM`
- `COUNT`
- `COUNTA`
- `COUNTIF`
- `COUNTIFS`
- `SUMIF`
- `SUMIFS`
- `AVERAGE`
- `AVERAGEIF`
- `AVERAGEIFS`
- `IF`
- `IFERROR`
- `TRIM`
- `UPPER`
- `LOWER`
- `PROPER`

---

## 20. Important Excel Formula

### Conversion Rate

`=Conversions/Visitors`

Format the result as a percentage.

### AOV

`=Revenue/Conversions`

---

## 21. Pivot-Style Analysis

### Group Level

Analyse:

- Group
- Visitors
- Conversions
- Conversion Rate
- Revenue

### Segment Level

Analyse:

- Segment
- Group
- Visitors
- Conversions
- Revenue

---

## 22. Charts

Day 097 contains:

- Conversion Rate by Group
- Revenue by Group
- Daily Conversion Rate Trend

---

## 23. Statistical Significance

A numerical difference between two groups does not automatically establish that the difference is statistically meaningful.

Important concepts:

- Null Hypothesis
- Alternative Hypothesis
- P-value
- Confidence Interval
- Significance Level
- Sample Size

---

## 24. Null Hypothesis

For conversion rate:

**H₀: Control and Treatment have the same conversion rate.**

---

## 25. Alternative Hypothesis

For conversion rate:

**H₁: Control and Treatment have different conversion rates.**

---

## 26. P-Value

A p-value is used in hypothesis testing to assess compatibility of the observed data with the null hypothesis under the chosen statistical model.

Do not interpret it as the probability that the null hypothesis is true.

Consider it together with:

- Effect size
- Sample size
- Confidence interval
- Experiment design
- Data quality

---

## 27. Confidence Interval

A confidence interval describes uncertainty around an estimated metric.

It can be used for:

- Conversion rate
- Difference in conversion rate
- Other experiment estimates

---

## 28. Sample Size

Sample size affects the stability of estimates and the ability to detect differences.

Small samples can produce unstable estimates.

---

## 29. Randomisation

Randomisation helps reduce systematic differences between Control and Treatment groups.

A well-designed experiment should use an appropriate assignment process.

---

## 30. Business Interpretation Checklist

Ask:

1. What is the experiment testing?
2. What is Group A?
3. What is Group B?
4. What is the primary metric?
5. How many visitors are there?
6. How many conversions occurred?
7. What are the conversion rates?
8. What is the revenue?
9. What is the AOV?
10. Are segment-level patterns consistent?
11. Are daily patterns consistent?
12. What does statistical analysis indicate?
13. What are the limitations?

---

## 31. Python Tools

### Pandas

- Read Excel
- Clean data
- Filter groups
- Group data
- Calculate KPIs

### NumPy

- Numeric operations
- Conditional calculations

### Matplotlib

- Create charts
- Visualise trends
- Compare groups

---

## 32. Python Workflow

**Load Data**

→ **Inspect**

→ **Clean**

→ **Validate**

→ **Separate A/B**

→ **Calculate KPIs**

→ **Analyse Segments**

→ **Visualise**

→ **Interpret**

---

## 33. Workbook Sheets

1. Instructions
2. Raw_AB_Test_Data
3. Data_Quality_Check
4. AB_Test_Cleaning
5. Cleaned_AB_Test_Data
6. AB_Test_Summary
7. Conversion_Analysis
8. Revenue_Analysis
9. Segment_Analysis
10. Daily_AB_Test
11. AB_Test_KPI
12. Pivot_Group
13. Pivot_Segment
14. Chart_Data
15. Charts
16. Business_Insights
17. Final_AB_Test_Analysis

---

## 34. Quick Revision

### A/B Testing

Compare two experimental groups.

### Control

Group A.

### Treatment

Group B.

### Conversion Rate

**Conversions ÷ Visitors × 100**

### Revenue

**Converted × Order Value**

### AOV

**Revenue ÷ Conversions**

### Important Statistical Concepts

**H₀ → H₁ → Test → P-value → Confidence Interval → Interpretation**

---

## 35. Key Takeaway

**A/B testing compares two groups using defined metrics. Always clean and validate the data first, compare multiple business metrics, examine segments and trends, and consider statistical uncertainty before interpreting experimental results.**

---

### 🚀 Day 097 — Quick Revision Complete

**Business Data Management — A/B Testing Practice**