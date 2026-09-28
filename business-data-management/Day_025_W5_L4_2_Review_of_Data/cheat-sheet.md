# 🧠 Day 025 — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Course:** Business Data Management  
**Day:** 025  
**Topic:** Review of Data  

## ⚡ Data Review Order

Structure → Completeness → Duplicates → Categories → Numerical Fields → Business Measures → Limitations.

Review the raw data before creating conclusions.

Check the number of rows and columns.

Check column names.

Check data types.

Understand field meanings.

## 🔎 Quality Checks

Missing values → `isna().sum()`.

Duplicate rows → `duplicated().sum()`.

Duplicate IDs → `df['Order_ID'].duplicated().sum()`.

Unique values → `unique()`.

Unique count → `nunique()`.

Summary statistics → `describe()`.

## 📊 Excel

Filter → Inspect records.

Sort → Identify ranges and rankings.

Pivot Table → Summarise dimensions.

SUM → Total.

AVERAGE → Mean.

COUNT → Count numeric values.

Conditional formatting → Spot unusual values.

Chart → Communicate selected findings.

## 🐍 Python

`pd.read_excel()` → Load workbook.

`df.head()` → Preview data.

`df.shape` → Rows and columns.

`df.columns` → Field names.

`df.dtypes` → Data types.

`df.isna().sum()` → Missing values.

`df.duplicated().sum()` → Duplicate rows.

`df.nunique()` → Unique counts.

`df.describe()` → Numerical summary.

`df.groupby()` → Group analysis.

`df.to_csv()` → Export results.

## 📂 Field Mapping

`Order_ID` → Identifier.

`Month` → Time dimension.

`Category` → Product dimension.

`Channel` → Sales-platform dimension.

`Region` → Geographic dimension.

`Customer_Type` → Customer dimension.

`Orders` → Transaction volume.

`Units` → Product volume.

`Discount_Percent` → Pricing context.

`Revenue_Lakh` → Sales value.

## 🧠 Interpretation

Clean data supports reliable analysis.

A quality check does not guarantee perfect data.

Missing values should be understood before treatment.

Duplicates require investigation.

Unexpected categories should be checked.

Numerical ranges should be inspected.

Time values should be consistent.

Revenue is not profit.

## 📈 Visualisation

Monthly revenue → Column chart.

Category revenue → Bar or column chart.

Data quality → Column chart.

Use charts to support questions.

Do not create charts without a purpose.

Use clear titles.

Use meaningful axis labels.

Use explicit colours in Excel charts.

## 💰 Business Measures

Revenue → Sales value.

Orders → Transaction activity.

Units → Product volume.

Discount → Pricing context.

Profit → Requires cost information.

Revenue and profit are not interchangeable.

## 🔍 Data Quality Questions

Are the rows complete?

Are important fields missing?

Are records duplicated?

Are identifiers duplicated?

Are categories consistent?

Are numerical values reasonable?

Is the time field consistent?

Are business measures correctly defined?

## 📊 Review Workflow

Open workbook.

Inspect raw data.

Check structure.

Check missing values.

Check duplicates.

Check categories.

Check numerical values.

Review time field.

Create summaries.

Review charts.

Document limitations.

## 🏅 Badges

🏅 **IIT Madras BS Degree**

🏅 **Business Data Management**

🏅 **Day 025 — Review of Data**

🏅 **E-Commerce Case Study**

🏅 **Business Analytics Practice**

## 🚀 Quick Revision

Raw data first.

Quality checks second.

Summaries third.

Visualisation fourth.

Interpretation after review.

Document limitations.

Never confuse revenue with profit.

Always connect analysis to a business question.