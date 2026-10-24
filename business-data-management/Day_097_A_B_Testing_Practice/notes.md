# 📘 Day 097 — A/B Testing Practice — Notes

![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![BDM](https://img.shields.io/badge/Business%20Data%20Management-Day%20097-blue?style=for-the-badge)
![A/B Testing](https://img.shields.io/badge/A%2FB%20Testing-Practice-green?style=for-the-badge)

---

## 👤 Metadata

- **Author:** Saloni Tiwari
- **Programme:** IIT Madras BS Degree — Diploma Level
- **Day:** 097
- **Topic:** A/B Testing Practice

---

## 1. Introduction to A/B Testing

A/B testing is an experimental method used to compare two versions of a business experience.

The two versions are commonly represented as:

- **Group A — Control**
- **Group B — Treatment**

The purpose is to observe how the groups perform using predefined business metrics.

In this project, the main metrics include:

- Visitors
- Conversions
- Conversion Rate
- Revenue
- Average Order Value

The dataset is synthetic and is designed for educational practice.

---

## 2. Control Group

The **Control Group** is the reference group in an A/B test.

In this project:

**Group A = Control**

The Control group represents the existing or reference version of the business experience.

The performance of the Treatment group can be compared with the Control group.

---

## 3. Treatment Group

The **Treatment Group** receives the changed version of the experience being tested.

In this project:

**Group B = Treatment**

The Treatment group is compared with the Control group using the selected metrics.

---

## 4. A/B Testing Experiment

A simple A/B testing experiment can follow this structure:

**Users**

↓

**Randomly assigned to groups**

↓

**Control Group (A)**

**Treatment Group (B)**

↓

**User Behaviour**

↓

**Conversions and Revenue**

↓

**Metric Comparison**

The experiment should have a clearly defined business question and measurement metric.

---

## 5. Business Question

An A/B test should begin with a clear question.

Example:

> Does the Treatment version produce a different conversion rate compared with the Control version?

The question should be measurable using the available data.

---

## 6. A/B Testing Dataset

The Day 097 dataset contains fields such as:

| Field | Meaning |
|---|---|
| User_ID | Unique user identifier |
| Date | Experiment date |
| Group | Control or Treatment group |
| Customer_Segment | Customer segment |
| Device | User device |
| Channel | Acquisition channel |
| Age | User age |
| Visitors | Number of visitors |
| Converted | Conversion indicator |
| Order_Value | Value associated with a conversion |
| Revenue | Revenue generated |
| Conversion_Status | Conversion status |

---

## 7. User ID

**User_ID** identifies an individual record or user in the experiment dataset.

It helps with:

- Identifying records
- Detecting duplicates
- Tracking users
- Validating the dataset

Duplicate records should be reviewed before performing the analysis.

---

## 8. Date

The **Date** field represents when the experiment activity occurred.

Date information can be used to analyse:

- Daily visitors
- Daily conversions
- Daily conversion rate
- Daily revenue
- Trends over the experiment period

---

## 9. Customer Segment

Customer segments allow the A/B test to be examined across different types of customers.

The dataset contains:

- **New**
- **Regular**
- **Loyal**
- **At Risk**

Segment analysis can show whether the observed pattern is similar across customer groups.

---

## 10. Device

The **Device** field represents the type of device used by the customer.

Examples:

- Mobile
- Desktop
- Tablet

Device-level analysis can be useful when examining user behaviour.

---

## 11. Channel

The **Channel** field represents the source through which users reached the business experience.

Examples include:

- Organic
- Paid Search
- Social
- Email

Channel information can be used for additional segmentation.

---

## 12. Visitors

**Visitors** represents the number of users or visits considered in the experiment.

Visitors form the denominator when calculating the conversion rate.

---

## 13. Conversions

A **Conversion** occurs when a visitor completes the defined target action.

In this dataset:

- `1` = Converted
- `0` = Not Converted

The total number of conversions can be calculated by summing the Converted field.

---

## 14. Conversion Rate

Conversion Rate measures the percentage of visitors who converted.

### Formula

**Conversion Rate = (Conversions / Visitors) × 100**

Example:

If there are:

- 100 visitors
- 15 conversions

Then:

**Conversion Rate = (15 / 100) × 100 = 15%**

---

## 15. Comparing Conversion Rates

The conversion rates of Group A and Group B can be compared.

A simple difference can be calculated as:

**Conversion Rate Difference = Treatment Conversion Rate − Control Conversion Rate**

This provides a descriptive comparison.

A difference by itself does not establish whether the observed result is statistically significant.

---

## 16. Order Value

**Order_Value** represents the value associated with a conversion.

If a visitor does not convert, the order value is recorded as zero in the cleaned practice dataset.

Order value can be used to calculate revenue-related metrics.

---

## 17. Revenue

Revenue represents the amount generated from conversions.

For this practice dataset:

**Revenue = Converted × Order_Value**

If:

- Converted = 1
- Order Value = ₹5,000

Then:

**Revenue = ₹5,000**

If:

- Converted = 0

Then:

**Revenue = ₹0**

---

## 18. Average Order Value

Average Order Value measures the average revenue per conversion.

### Formula

**Average Order Value = Revenue / Conversions**

Example:

Revenue = ₹50,000

Conversions = 10

Average Order Value:

**₹50,000 / 10 = ₹5,000**

---

## 19. Data Quality in A/B Testing

Data quality is important because incorrect records can affect experiment metrics.

The raw Day 097 dataset contains practice issues such as:

- Extra spaces
- Inconsistent capitalization
- Missing age
- Missing visitors
- Invalid age
- Invalid visitor values
- Invalid conversion values
- Missing order value
- Invalid revenue
- Inconsistent conversion status
- Duplicate records

---

## 20. Data Cleaning Workflow

The cleaning process used in this project follows:

**Inspect**

↓

**Identify Issues**

↓

**Clean**

↓

**Validate**

↓

**Analyse**

Important cleaning activities include:

- Removing unnecessary spaces
- Standardizing text
- Handling missing values
- Correcting invalid numeric values
- Recalculating revenue
- Rebuilding conversion status
- Removing exact duplicates

---

## 21. Cleaning Group Values

Group values should contain valid A/B labels.

Examples of inconsistent values:

- `A`
- `A `
- ` b `
- `B`

A cleaning process can:

1. Remove spaces.
2. Convert text to a consistent case.
3. Validate that the value belongs to A or B.

---

## 22. Cleaning Customer Segments

Customer segment labels should use a consistent format.

For example:

` loyal `

can be standardised to:

`Loyal`

Similarly:

`AT RISK`

can be standardised to:

`At Risk`

Consistent labels are important for segment-level analysis.

---

## 23. Handling Missing Age

Missing or invalid age values should be handled before analysis.

For this educational dataset, missing or invalid ages are replaced using the median of valid ages.

This provides a simple practice method for handling numeric missing values.

---

## 24. Handling Visitors

Visitors should contain valid positive values.

Missing or invalid visitor values are replaced with:

**1**

This prevents invalid denominators during conversion-rate calculations.

---

## 25. Handling Converted Values

The Converted field should contain only:

- `0`
- `1`

Values outside this range are treated as invalid.

The practice cleaning rule replaces invalid conversion values with:

**0**

---

## 26. Handling Order Value

Order values should not be negative.

For this project:

- Missing order values → `0`
- Negative order values → `0`

This keeps the order-value field valid for revenue calculations.

---

## 27. Recalculating Revenue

Revenue is recalculated after cleaning.

### Formula

**Revenue = Converted × Order_Value**

Recalculating derived fields helps maintain consistency between the input fields and calculated metrics.

---

## 28. Conversion Status

Conversion Status is rebuilt from the Converted field.

If:

**Converted = 1**

then:

**Conversion Status = Converted**

If:

**Converted = 0**

then:

**Conversion Status = Not Converted**

This prevents inconsistent status labels.

---

## 29. Duplicate Records

Duplicate records can affect:

- Visitor counts
- Conversion counts
- Revenue
- Conversion rate

Therefore, exact duplicate records should be identified and removed where appropriate.

---

## 30. A/B Test Summary

The **AB_Test_Summary** sheet provides a group-level comparison.

Important columns include:

- Group Name
- Group
- Visitors
- Conversions
- Conversion Rate %
- Revenue
- Average Order Value

This provides a high-level view of the experiment.

---

## 31. Conversion Analysis

The **Conversion_Analysis** sheet focuses on:

- Visitors
- Conversions
- Conversion Rate

The analysis can be used to compare the descriptive conversion performance of Groups A and B.

---

## 32. Revenue Analysis

The **Revenue_Analysis** sheet focuses on:

- Revenue
- Conversions
- Average Order Value

Revenue should be considered together with conversion volume because revenue differences can result from different numbers of conversions as well as different order values.

---

## 33. Customer Segment Analysis

The **Segment_Analysis** sheet breaks the experiment down by:

- New
- Regular
- Loyal
- At Risk

For each segment and group, the analysis includes:

- Visitors
- Conversions
- Conversion Rate
- Revenue
- Average Order Value

This provides a more detailed view of the experiment.

---

## 34. Daily A/B Test Analysis

The **Daily_AB_Test** sheet provides daily metrics for each group.

Important metrics include:

- Date
- Group
- Visitors
- Conversions
- Conversion Rate
- Revenue

Daily analysis can help identify changes or unusual patterns during the experiment period.

---

## 35. KPI Analysis

The **AB_Test_KPI** sheet contains important experiment KPIs.

### Main KPIs

- Visitors
- Conversions
- Conversion Rate
- Revenue
- Average Order Value

KPIs make it easier to compare the two groups in a structured format.

---

## 36. Pivot-Style Analysis

Pivot-style summaries are included for:

### Group Analysis

Group-level metrics can be summarised by:

- Control
- Treatment

### Segment Analysis

Segment-level metrics can be summarised by:

- Customer Segment
- Group

Pivot-style analysis helps organise business data for comparison.

---

## 37. Visualisation

Charts can make A/B test results easier to understand.

The workbook contains:

- Conversion Rate by Group
- Revenue by Group
- Daily Conversion Rate Trend

Charts should support the numerical analysis rather than replace it.

---

## 38. Statistical Significance

A difference between two groups does not automatically mean that the difference is statistically meaningful.

Statistical testing can be used to evaluate whether an observed difference could reasonably occur because of random variation.

For conversion data, a suitable statistical approach may involve comparing proportions.

Important concepts include:

- Null hypothesis
- Alternative hypothesis
- Significance level
- P-value
- Confidence interval
- Sample size

The Day 097 workbook focuses mainly on practical A/B testing analysis rather than implementing a complete statistical test.

---

## 39. Null Hypothesis

The null hypothesis represents the assumption that there is no difference in the tested metric between the two groups.

For a conversion-rate experiment, it can be expressed conceptually as:

**H₀: Control and Treatment have the same conversion rate.**

---

## 40. Alternative Hypothesis

The alternative hypothesis represents a difference between the groups.

For conversion rate:

**H₁: Control and Treatment have different conversion rates.**

The exact hypothesis should match the experiment design.

---

## 41. P-Value

A p-value is used in statistical hypothesis testing to assess how compatible the observed data are with the null hypothesis under the chosen statistical model.

A p-value should not be interpreted as the probability that the null hypothesis is true.

It should be considered together with:

- Effect size
- Sample size
- Confidence intervals
- Experiment design
- Data quality

---

## 42. Confidence Interval

A confidence interval provides a range associated with an estimated parameter under a specified statistical method and confidence level.

For an A/B test, confidence intervals can help describe uncertainty around:

- Conversion rates
- Difference in conversion rates
- Other estimated metrics

---

## 43. Sample Size

Sample size affects the ability to detect differences.

Very small samples can produce unstable estimates.

A well-designed A/B test should consider sample size before the experiment begins.

---

## 44. Experiment Duration

An experiment should run for an appropriate period based on the business context and experiment design.

Daily analysis can help identify whether the collected data show changes across the experiment period.

The Day 097 dataset contains a synthetic 30-day period for practice.

---

## 45. Randomisation

Randomisation is an important part of experimental design.

Users should be assigned to groups using a process that reduces systematic differences between the groups.

This helps make the groups more comparable for the purpose of the experiment.

---

## 46. Business Interpretation

A good A/B testing report should clearly separate:

### Observed Data

What the dataset actually shows.

### Statistical Analysis

What the statistical test indicates about uncertainty.

### Business Interpretation

What the results may mean in the context of the experiment.

### Limitations

What the experiment cannot establish from the available data.

---

## 47. Important A/B Testing Questions

When reviewing an experiment, ask:

1. What is the business question?
2. What is the Control group?
3. What is the Treatment group?
4. What metric is being tested?
5. How many visitors are in each group?
6. How many conversions occurred?
7. What is the conversion rate?
8. What is the revenue?
9. What is the Average Order Value?
10. Are segment-level results consistent?
11. Are daily results consistent?
12. Is the observed difference statistically significant?
13. What are the limitations of the experiment?

---

## 48. Excel Functions for A/B Testing

Useful Excel functions include:

- `COUNT`
- `COUNTA`
- `COUNTIF`
- `COUNTIFS`
- `SUM`
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

These functions can be used for cleaning, aggregation and analysis.

---

## 49. Example Excel Calculation

A simple conversion rate calculation can use:

**Conversions ÷ Visitors**

For example:

`=C2/B2`

If the result is formatted as a percentage, it can be displayed as the conversion rate.

---

## 50. Python Connection

A/B testing can also be performed using Python.

Common libraries include:

- Pandas
- NumPy
- Matplotlib

### Pandas

Used for:

- Reading Excel data
- Cleaning data
- Filtering groups
- Grouping records
- Calculating metrics

### NumPy

Used for:

- Numeric operations
- Conditional calculations
- Array-based analysis

### Matplotlib

Used for:

- Conversion charts
- Revenue charts
- Trend visualisation

---

## 51. Python A/B Testing Workflow

A typical Python workflow is:

**Load Data**

↓

**Inspect Data**

↓

**Clean Data**

↓

**Validate Data**

↓

**Split Control and Treatment**

↓

**Calculate KPIs**

↓

**Analyse Segments**

↓

**Visualise Results**

↓

**Interpret Findings**

---

## 52. Limitations of This Practice Dataset

This project is designed for learning.

Important limitations include:

- Synthetic data
- Small educational dataset
- Artificially introduced data-quality issues
- Simplified experiment structure
- No real customer behaviour
- No complete statistical testing workflow

Therefore, the results should not be interpreted as evidence from a real business experiment.

---

## 53. Key Learning Points

- A/B testing compares two groups under an experimental design.
- Group A is the Control group in this project.
- Group B is the Treatment group in this project.
- Conversion Rate is a key A/B testing metric.
- Revenue and Average Order Value provide additional business context.
- Data quality must be checked before comparing groups.
- Segment-level analysis provides additional detail.
- Daily analysis helps examine trends over time.
- Statistical significance is different from simply observing a numerical difference.
- Business interpretation should consider uncertainty and experiment limitations.

---

## 54. Day 097 Summary

Day 097 combines **data cleaning, Excel analysis, business KPIs, group comparison, segmentation, visualisation and basic experimental concepts**.

The complete workflow is:

**Raw A/B Testing Data**

→ **Data Quality Check**

→ **Cleaning**

→ **Validation**

→ **Conversion Analysis**

→ **Revenue Analysis**

→ **Segment Analysis**

→ **Daily Analysis**

→ **KPI Analysis**

→ **Visualisation**

→ **Statistical Consideration**

→ **Business Interpretation**

---

## 🔑 Key Takeaway

**A/B testing is a structured method for comparing two groups using predefined metrics. Reliable analysis requires clean data, appropriate metrics, careful experiment design, statistical consideration and clear reporting of limitations.**

---

### 🚀 Day 097 Complete

**Business Data Management — A/B Testing Practice**