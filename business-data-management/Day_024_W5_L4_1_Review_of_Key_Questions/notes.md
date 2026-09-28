# 📘 Day 024 — Review of Key Questions

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Course:** Business Data Management  
**Day:** 024  
**Topic:** Review of Key Questions  

## 🎯 Introduction

Day 024 is based on the review of key questions from the e-commerce case study.

The purpose of this lecture is to review the important business questions.

The questions connect business requirements with data analysis.

A business analyst should understand the question before creating a calculation.

The data should be selected according to the question.

The correct measure should be used for the required analysis.

The result should then be interpreted in a business context.

## ❓ What Is a Business Question?

A business question is a question that helps understand a business situation.

It should have a clear purpose.

It should be connected to a business decision or analysis requirement.

Examples include questions about revenue.

Another example is identifying the highest-performing month.

A business question can also compare categories.

It can compare sales channels.

It can compare regions.

It can compare customer groups.

A good question helps define the required analysis.

## 📊 Question and Data

Different questions require different fields.

A total revenue question requires the Revenue_Lakh field.

A monthly revenue question requires Month and Revenue_Lakh.

A category question requires Category and a suitable measure.

A channel question requires Channel and a suitable measure.

A regional question requires Region and a suitable measure.

A customer question requires Customer_Type and a suitable measure.

A discount question requires Discount_Percent.

The selected data should directly support the question.

## 💰 Revenue Analysis

Revenue is an important measure in e-commerce analysis.

Total revenue gives an overall view of sales value.

Monthly revenue helps compare performance over time.

Category revenue helps compare product groups.

Channel revenue helps compare sales platforms.

Regional revenue helps compare geographic performance.

Customer-type revenue helps compare customer groups.

Revenue should always be interpreted with its unit.

In this workbook, revenue is represented in lakh.

Revenue should not automatically be considered profit.

Profit analysis would require cost information.

## 📅 Monthly Analysis

Monthly analysis helps identify changes over time.

The Month field provides the time dimension.

Revenue can be grouped by month.

Orders can also be grouped by month.

Units can also be grouped by month.

Average discount can be compared across months.

The highest-revenue month identifies the strongest observed month.

The lowest-revenue month identifies the weakest observed month.

A trend describes how the values change across the period.

## 🛍️ Category Analysis

Category analysis compares different product categories.

The Category field provides the grouping dimension.

Revenue can be aggregated for every category.

Orders can also be compared by category.

Units provide additional volume information.

Average discount provides pricing context.

A category with high revenue has a strong sales contribution.

However, high revenue does not automatically mean high profit.

Additional cost information would be required for profitability analysis.

## 📱 Channel Analysis

Channel analysis compares different sales platforms.

Examples in the practice dataset include Website, App, and Marketplace.

Revenue can be grouped by Channel.

Orders can be grouped by Channel.

Units can be grouped by Channel.

The highest-revenue channel can be identified by sorting the summary.

Channel performance can support business decisions.

However, channel revenue alone does not explain why a channel performs differently.

Traffic, conversion rate, marketing spend, and customer acquisition data could provide more context.

## 🌍 Regional Analysis

Regional analysis compares business performance across locations.

The Region field provides the geographic dimension.

Revenue can be grouped by region.

Orders can be grouped by region.

Units can be grouped by region.

A regional ranking can identify stronger and weaker regions.

Regional analysis can help identify areas requiring further investigation.

The current dataset provides only a limited geographic view.

More detailed geographic information could improve the analysis.

## 👥 Customer Analysis

Customer_Type provides a customer grouping.

The practice dataset contains New and Returning customers.

Revenue can be compared between these groups.

Orders can also be compared.

Units provide additional information about sales volume.

A higher revenue contribution indicates stronger observed sales value.

Customer analysis can support retention-related questions.

However, customer behaviour requires additional information for deeper analysis.

Examples include customer acquisition cost and repeat purchase frequency.

## 🏷️ Discount Analysis

Discount percentage provides pricing information.

Average discount can be calculated for each category.

Discount can also be compared across other dimensions.

A high discount does not automatically mean poor performance.

A low discount does not automatically mean high profitability.

Revenue, units, orders, and discount should be considered together.

Profit and margin would provide stronger financial context.

## 📈 Visual Review

Visualisation makes comparisons easier to understand.

A column chart can compare monthly revenue.

A bar chart can compare channels.

A category chart can compare product groups.

A regional chart can compare geographic performance.

Charts should have clear titles.

Axes should be labelled properly.

The selected chart should match the question.

A trend is generally easier to understand through a time-based chart.

## 🧠 Interpretation

Analysis produces numbers.

Interpretation explains what those numbers mean.

An answer should be based on evidence.

An insight should connect the evidence with a business meaning.

The analysis should not make unsupported claims.

A descriptive trend does not automatically prove causation.

For example, an increase in revenue does not by itself prove why revenue increased.

Additional data may be needed to explain the reason.

## 🔎 Review Approach

First read the business question.

Then identify the required dimension.

Identify the required measure.

Create the appropriate summary.

Check the calculated result.

Compare the result with related measures.

Use a suitable visualisation when required.

Finally, write a concise business interpretation.

## 📝 Key Questions for Day 024

What is the total revenue?

Which month has the highest revenue?

How does monthly revenue change?

Which category contributes the most revenue?

Which channel contributes the most revenue?

Which region contributes the most revenue?

How do New and Returning customers compare?

Which month has the highest order volume?

Which category has the highest average discount?

What additional data could strengthen the analysis?

## 💻 Excel Connection

Excel can answer many of these questions efficiently.

SUM can calculate total revenue.

Pivot Tables can group revenue by month.

Pivot Tables can group revenue by category.

Pivot Tables can group revenue by channel.

Pivot Tables can group revenue by region.

Pivot Tables can group revenue by customer type.

Sorting can identify the highest-performing group.

Charts can communicate the final results.

## 🐍 Python Connection

Python can make the analysis reproducible.

Pandas can load the Excel workbook.

`read_excel()` reads the dataset.

`groupby()` creates grouped summaries.

`sum()` calculates totals.

`mean()` calculates averages.

`sort_values()` can rank results.

`idxmax()` can locate the maximum.

Matplotlib can create charts.

CSV files can store the generated summaries.

## ⚠️ Important Limitations

The practice dataset is designed for learning.

It represents a simplified business case.

It does not contain every variable required for real business decisions.

Revenue does not provide profitability information.

Discount does not provide complete pricing information.

Customer type does not explain complete customer behaviour.

Regional data is limited.

Historical context is limited.

Therefore, conclusions should remain descriptive.

## 🏅 Course Badges

🏅 **IIT Madras BS Degree**

🏅 **Business Data Management**

🏅 **Day 024 — Review of Key Questions**

🏅 **E-Commerce Case Study**

🏅 **Business Analytics Practice**

## ✅ Day 024 Completion

Watch the W5_L4.1 lecture.

Review every key question.

Open the Day 024 Excel workbook.

Attempt the questions before checking the answers.

Verify the calculations.

Run the Python analysis.

Review the generated summaries.

Review the charts.

Write your own business insights.

Keep the interpretation evidence-based.

After completion, continue with W5_L4.2: Review of Data.