# 📘 Day 025 — Notes

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Course:** Business Data Management  
**Day:** 025  
**Topic:** Review of Data  

## 🎯 Meaning of Data Review

Data review means inspecting the dataset before analysis.

The first step is understanding the structure.

The next step is checking quality.

Then the analyst reviews categories and numerical measures.

Finally, the analyst identifies limitations.

Data review reduces the chance of making incorrect conclusions.

## 📂 Dataset Structure

Rows represent observations in the practice dataset.

Columns represent variables.

`Order_ID` identifies an order.

`Month` provides the time dimension.

`Category` identifies the product category.

`Channel` identifies the sales platform.

`Region` identifies the geographic group.

`Customer_Type` identifies the customer group.

`Orders` represents order volume.

`Units` represents units sold.

`Discount_Percent` represents discount.

`Revenue_Lakh` represents revenue in lakh.

## 🔎 Missing Values

Missing values can affect analysis.

Each column should be checked for missing values.

A total missing-value count provides an initial quality signal.

Missing values should be investigated before analysis.

Treatment depends on the meaning and amount of missing data.

An analyst should not automatically replace every missing value.

The business meaning of the field should be considered.

## ♻️ Duplicate Review

Duplicate rows can affect totals.

Identifiers should also be checked for duplicates.

`Order_ID` is an identifier in this dataset.

A duplicate identifier may require investigation.

A duplicate row is different from two legitimate similar transactions.

Duplicate checks should be performed before aggregation.

## 🏷️ Categorical Review

Categorical fields contain groups.

`Category` contains product groups.

`Channel` contains sales platforms.

`Region` contains geographic groups.

`Customer_Type` contains customer groups.

Reviewing unique values helps detect unexpected categories.

Unique counts help understand dataset dimensions.

## 🔢 Numerical Review

`Orders` is numerical.

`Units` is numerical.

`Discount_Percent` is numerical.

`Revenue_Lakh` is numerical.

Descriptive statistics can show minimum, maximum, mean, and quartiles.

Numerical checks can reveal unusual values.

Ranges should be reasonable for the business context.

## 📅 Time Review

`Month` provides the time dimension.

Monthly analysis depends on consistent month values.

The practice dataset covers Jan-2023 through Jun-2023.

Time ordering should be checked before trend analysis.

A time field should be consistent across records.

## 💰 Business Measures

Revenue measures sales value.

Orders measure transaction activity.

Units measure volume.

Discount provides pricing context.

Revenue should not be interpreted as profit.

Profit requires cost information.

Different business questions require different measures.

## 📊 Grouped Review

Monthly grouping helps review trends.

Category grouping helps compare products.

Channel grouping helps compare sales platforms.

Regional grouping helps compare geographic performance.

Customer grouping helps compare customer types.

Grouped analysis should be performed only after data quality checks.

## 📈 Visual Review

Charts help communicate patterns.

A monthly revenue chart can show movement over time.

A category revenue chart can compare product groups.

A data-quality chart can show quality-check counts.

Visuals should be connected to a clear question.

A chart should not be created only for decoration.

## 💻 Excel Review

Excel can be used to inspect raw data.

Filters help locate records.

Sorting helps inspect ranges.

Pivot Tables help summarise data.

Basic formulas support calculations.

Charts support communication.

The workbook contains prepared review sheets.

## 🐍 Python Review

Pandas supports data inspection.

`read_excel()` loads the workbook.

`head()` previews records.

`shape` shows dimensions.

`dtypes` shows data types.

`isna()` supports missing-value checks.

`duplicated()` supports duplicate checks.

`nunique()` supports unique-value checks.

`describe()` provides descriptive statistics.

`groupby()` supports grouped analysis.

## ⚠️ Limitations

The practice dataset is simplified.

It does not contain complete cost information.

It does not contain detailed traffic information.

It does not contain complete customer behaviour.

It does not contain all operational variables.

Further business decisions would require additional data.

## 🧠 Key Takeaway

Do not begin interpretation before understanding the data.

Check quality first.

Understand every important field.

Use appropriate measures.

Document limitations.

## 🏅 Badges

🏅 **IIT Madras BS Degree**

🏅 **Business Data Management**

🏅 **Day 025 — Review of Data**

🏅 **E-Commerce Case Study**

🏅 **Business Analytics Practice**

## 🚀 Final Revision

Review structure.

Review completeness.

Review duplicates.

Review categories.

Review numerical fields.

Review time fields.

Review business measures.

Review limitations.

Then continue to the next stage.