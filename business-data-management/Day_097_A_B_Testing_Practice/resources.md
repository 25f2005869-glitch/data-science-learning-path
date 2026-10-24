# 📚 Day 097 — A/B Testing Practice — Resources

![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Business Data Management](https://img.shields.io/badge/Business%20Data%20Management-Day%20097-blue?style=for-the-badge)
![A/B Testing](https://img.shields.io/badge/A%2FB%20Testing-Resources-green?style=for-the-badge)
![Excel](https://img.shields.io/badge/Tool-Microsoft%20Excel-orange?style=for-the-badge)

---

## 👤 Metadata

- **Author:** Saloni Tiwari
- **Programme:** IIT Madras BS Degree — Diploma Level
- **Day:** 097
- **Topic:** A/B Testing Practice

---

# 1. 📌 A/B Testing Fundamentals

### Topics to Study

- A/B Testing
- Control Group
- Treatment Group
- Experiment Design
- Randomisation
- Hypothesis
- Primary Metric
- Conversion Rate
- Sample Size
- Statistical Significance

### Recommended Study Order

**A/B Testing Basics**

→ **Control vs Treatment**

→ **Experiment Design**

→ **Metrics**

→ **Conversion Rate**

→ **Statistical Testing**

→ **Business Interpretation**

---

# 2. 🧪 Experiment Design

Study the basic components of an experiment:

- Business Question
- Control Group
- Treatment Group
- Random Assignment
- Primary Metric
- Experiment Duration
- Sample Size
- Data Collection
- Analysis
- Interpretation

### Practice Question

> What business decision is the experiment designed to inform?

---

# 3. 📊 Conversion Rate

### Formula

**Conversion Rate = (Conversions / Visitors) × 100**

Study:

- Visitors
- Conversions
- Conversion Rate
- Conversion Rate Difference

### Practice

Calculate conversion rates separately for:

- Control Group
- Treatment Group
- Customer Segments
- Daily observations

---

# 4. 💰 Revenue Analysis

Study:

- Revenue
- Order Value
- Average Order Value
- Revenue per Visitor

### Important Formula

**Average Order Value = Revenue / Conversions**

### Practice

Compare revenue-related metrics between the two experimental groups.

---

# 5. 👥 Customer Segmentation

Study A/B testing results across different customer segments.

Day 097 segments:

- New
- Regular
- Loyal
- At Risk

Useful metrics:

- Visitors
- Conversions
- Conversion Rate
- Revenue
- Average Order Value

---

# 6. 📅 Time-Based Analysis

Study how experiment metrics change over time.

Useful metrics:

- Daily Visitors
- Daily Conversions
- Daily Conversion Rate
- Daily Revenue

### Practice

Create a daily trend chart and inspect whether the observed pattern changes during the experiment period.

---

# 7. 🧹 Data Cleaning Resources

Before analysing an experiment, study:

- Missing values
- Duplicate records
- Invalid numeric values
- Inconsistent categories
- Extra spaces
- Text standardisation
- Data validation
- Derived-column recalculation

### Useful Excel Functions

- `TRIM`
- `UPPER`
- `LOWER`
- `PROPER`
- `IF`
- `IFERROR`
- `COUNTIF`
- `COUNTIFS`
- `SUMIF`
- `SUMIFS`
- `AVERAGEIF`
- `AVERAGEIFS`

---

# 8. 📈 Excel A/B Testing Practice

Use Excel to practise:

- Filtering Control and Treatment groups
- `COUNTIF`
- `COUNTIFS`
- `SUMIF`
- `SUMIFS`
- `AVERAGEIF`
- Conversion Rate calculations
- Revenue calculations
- KPI summaries
- Pivot Tables
- Charts

### Recommended Workflow

**Raw Data**

→ **Cleaning**

→ **Pivot Table**

→ **KPI Summary**

→ **Charts**

→ **Business Interpretation**

---

# 9. 🔄 Pivot Table Practice

Create Pivot Tables using:

### Group

- Group
- Visitors
- Conversions
- Revenue

### Segment

- Customer Segment
- Group
- Visitors
- Conversions
- Revenue

### Additional Analysis

Try filtering by:

- Device
- Channel
- Customer Segment
- Date

---

# 10. 📊 Visualisation Resources

Practise creating:

### Chart 1

**Conversion Rate by Group**

### Chart 2

**Revenue by Group**

### Chart 3

**Daily Conversion Rate Trend**

### Visualisation Tips

- Use clear titles.
- Label important metrics.
- Keep Control and Treatment clearly distinguishable.
- Avoid unnecessary chart elements.
- Use charts together with the underlying numbers.

---

# 11. 🧮 Statistical Significance

Study the following concepts:

- Null Hypothesis
- Alternative Hypothesis
- Significance Level
- P-value
- Confidence Interval
- Effect Size
- Sample Size
- Statistical Power

### Core Idea

A difference in observed metrics does not automatically establish that the difference is statistically meaningful.

Statistical analysis helps quantify uncertainty around the observed result.

---

# 12. 📐 Hypothesis Testing

### Null Hypothesis

For a conversion-rate experiment:

**H₀: The Control and Treatment groups have the same conversion rate.**

### Alternative Hypothesis

**H₁: The Control and Treatment groups have different conversion rates.**

The hypothesis should match the actual experiment design.

---

# 13. 📉 P-Value

Study:

- What a p-value measures
- How it is used in hypothesis testing
- Significance level
- Interpretation limitations

### Important Note

A p-value is not the probability that the null hypothesis is true.

It should be interpreted with:

- Effect size
- Sample size
- Confidence interval
- Experimental design
- Data quality

---

# 14. 📏 Confidence Intervals

Study confidence intervals for:

- Conversion Rate
- Difference in Conversion Rates
- Other experiment estimates

Focus on understanding:

- Point estimate
- Uncertainty
- Interval interpretation

---

# 15. 👥 Sample Size

Study why sample size matters.

Important concepts:

- Small sample
- Large sample
- Statistical power
- Detectable effect
- Sampling variation

### Practice Question

> Why can a small experiment produce an unstable conversion-rate estimate?

---

# 16. 🎲 Randomisation

Study:

- Random assignment
- Control/Treatment comparability
- Selection bias
- Experimental validity

Randomisation is an important part of A/B test design.

---

# 17. 🐍 Python Resources

Useful Python libraries:

### Pandas

Use for:

- Reading Excel
- Cleaning data
- Filtering groups
- Grouping data
- Aggregating metrics
- KPI calculations

### NumPy

Use for:

- Numeric calculations
- Conditional operations
- Array-based processing

### Matplotlib

Use for:

- Bar charts
- Line charts
- Trend analysis
- Experiment visualisation

---

# 18. 🐼 Pandas Practice

Practise:

- `pd.read_excel()`
- `df.head()`
- `df.info()`
- `df.describe()`
- `df.isna().sum()`
- `df.drop_duplicates()`
- `df.groupby()`
- `df.sum()`
- `df.mean()`
- Boolean filtering

### Example Workflow

**Read**

→ **Inspect**

→ **Clean**

→ **Group**

→ **Aggregate**

→ **Visualise**

---

# 19. 📉 Matplotlib Practice

Practise:

- Bar charts
- Line charts
- Axis labels
- Chart titles
- Legends
- Figure sizing

Suggested charts:

- Conversion Rate by Group
- Revenue by Group
- Daily Conversion Rate

---

# 20. 💼 Business Interpretation

Study how to convert numerical analysis into a structured business report.

A report should contain:

1. Experiment Objective
2. Control Group
3. Treatment Group
4. Data Quality
5. Conversion Analysis
6. Revenue Analysis
7. Segment Analysis
8. Daily Analysis
9. Statistical Consideration
10. Limitations

---

# 21. ⚠️ A/B Testing Limitations

Important limitations to study:

- Small sample size
- Poor randomisation
- Data-quality problems
- Short experiment duration
- External factors
- Multiple comparisons
- Incorrect metric selection
- Incomplete tracking
- Selection bias

---

# 22. 📂 Day 097 Workbook Resources

The project workbook contains:

1. `Instructions`
2. `Raw_AB_Test_Data`
3. `Data_Quality_Check`
4. `AB_Test_Cleaning`
5. `Cleaned_AB_Test_Data`
6. `AB_Test_Summary`
7. `Conversion_Analysis`
8. `Revenue_Analysis`
9. `Segment_Analysis`
10. `Daily_AB_Test`
11. `AB_Test_KPI`
12. `Pivot_Group`
13. `Pivot_Segment`
14. `Chart_Data`
15. `Charts`
16. `Business_Insights`
17. `Final_AB_Test_Analysis`

---

# 23. 🗂️ Recommended Study Sequence

Follow this order:

### Step 1
Read the `Instructions` sheet.

### Step 2
Inspect `Raw_AB_Test_Data`.

### Step 3
Review `Data_Quality_Check`.

### Step 4
Study `AB_Test_Cleaning`.

### Step 5
Review `Cleaned_AB_Test_Data`.

### Step 6
Study `AB_Test_Summary`.

### Step 7
Practise `Conversion_Analysis`.

### Step 8
Practise `Revenue_Analysis`.

### Step 9
Study `Segment_Analysis`.

### Step 10
Review `Daily_AB_Test`.

### Step 11
Review `AB_Test_KPI`.

### Step 12
Practise Pivot-style analysis.

### Step 13
Study the charts.

### Step 14
Write business observations.

### Step 15
Complete the final analysis.

---

# 24. 🌐 Useful Learning Platforms

For additional learning, search for A/B testing and experimentation material on:

- Coursera
- edX
- Kaggle Learn
- Microsoft Learn
- Google Analytics learning resources
- Official Python documentation
- Pandas documentation
- NumPy documentation
- Matplotlib documentation

---

# 25. 🔎 Search Topics for Further Study

Use these search topics when you need additional practice:

- `A/B testing fundamentals`
- `control and treatment groups`
- `conversion rate analysis`
- `A/B test experiment design`
- `A/B testing sample size`
- `A/B testing statistical significance`
- `p value explained`
- `confidence interval A/B testing`
- `A/B testing with Python`
- `Pandas groupby analysis`
- `Matplotlib business charts`
- `Excel A/B testing analysis`

---

# 26. 📝 Revision Questions

Before completing Day 097, make sure you can answer:

1. What is A/B testing?
2. What is a Control Group?
3. What is a Treatment Group?
4. What is Conversion Rate?
5. How is Revenue calculated?
6. What is Average Order Value?
7. Why is data cleaning necessary?
8. Why is randomisation important?
9. Why does sample size matter?
10. What is a Null Hypothesis?
11. What is a p-value?
12. What is a confidence interval?
13. Why is segment analysis useful?
14. Why is daily analysis useful?
15. What limitations should be reported?

---

# 27. 🧪 Practice Resources in This Project

Use the workbook together with:

- `notes.md` → Detailed concepts
- `cheat-sheet.md` → Quick revision
- `practice.md` → Questions and tasks
- `resources.md` → Learning resources
- `ab_testing_practice.py` → Python practice
- `Day_097_A_B_Testing_Practice.xlsx` → Excel practice

---

# 28. ✅ Resource Checklist

- [ ] A/B testing fundamentals
- [ ] Control vs Treatment
- [ ] Experiment design
- [ ] Conversion Rate
- [ ] Revenue
- [ ] Average Order Value
- [ ] Customer segmentation
- [ ] Daily analysis
- [ ] Data cleaning
- [ ] Excel formulas
- [ ] Pivot Tables
- [ ] Charts
- [ ] Python Pandas
- [ ] NumPy
- [ ] Matplotlib
- [ ] Hypothesis testing
- [ ] P-value
- [ ] Confidence intervals
- [ ] Sample size
- [ ] Randomisation
- [ ] Business interpretation

---

## 🔑 Final Takeaway

**Use these resources to move from basic A/B testing concepts to practical business analysis: understand the experiment, clean the data, calculate KPIs, compare groups, analyse segments and trends, and consider statistical uncertainty before interpreting the results.**

---

### 🚀 Day 097 Resources Complete

**Business Data Management — A/B Testing Practice**