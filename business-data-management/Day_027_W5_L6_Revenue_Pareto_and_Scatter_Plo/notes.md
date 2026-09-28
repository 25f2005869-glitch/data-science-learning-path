# 📊 Day 027 — Revenue Pareto & Scatter Plot

**Author:** Saloni Tiwari
**Programme:** IIT Madras BS Degree — Diploma Level
**Day:** 027
**Topic:** W5_L6 — Revenue Pareto & Scatter Plot | Excel Sales

## Learning Objective

Understand revenue-based Pareto analysis.

Rank products by revenue contribution.

Calculate revenue share and cumulative revenue share.

Identify the core revenue group using the 80% idea.

Understand why Pareto is a prioritization tool rather than a strict law.

Build a scatter plot comparing units sold with revenue.

Interpret high-volume and high-value products.

Connect spreadsheet analysis with business decisions.

## Dataset

The workbook uses an e-commerce sales dataset.

Each row represents an order-level observation.

Product identifies the product being sold.

Units records the quantity sold.

Revenue_Lakh records revenue in lakh.

Month supports time-based analysis.

Channel supports channel comparison.

Region supports geographic comparison.

Orders records the number of orders represented.

## Revenue Pareto

Start by grouping the data by Product.

Sum Revenue_Lakh for every product.

Sort products from highest revenue to lowest revenue.

Calculate total revenue across all products.

Revenue share equals product revenue divided by total revenue.

Multiply the share by 100 to express it as a percentage.

Cumulative share is the running total of revenue share.

Products near the beginning of the ranking deserve close attention.

The 80% reference helps define a practical core group.

## Scatter Plot

Use Units on the horizontal axis.

Use Revenue_Lakh on the vertical axis.

Each point represents a product summary.

A point farther right has greater unit volume.

A point higher on the chart has greater revenue.

High units and high revenue indicate strong volume and value.

High units with relatively low revenue may indicate lower-value products.

Lower units with high revenue may indicate premium products.

Outliers deserve investigation before a business decision is made.

## Business Interpretation

Revenue concentration can guide inventory priorities.

High-revenue products may require stronger availability controls.

Pareto can support focused marketing decisions.

Scatter analysis prevents volume-only decision making.

A product with many units is not automatically the best revenue contributor.

Revenue per unit provides an additional interpretation layer.

Channel and regional summaries add context to product analysis.

Business insights should be supported by calculations.

Avoid claiming causation from a descriptive chart alone.

## Excel Workflow

Open the Ecommerce_Data sheet first.

Review the Revenue_Pareto sheet.

Check Revenue_Share_%.

Check Cumulative_Revenue_Share_%.

Review Pareto_Group.

Open Scatter_Data.

Review Units and Revenue_Lakh together.

Check Monthly_Summary, Channel_Summary and Region_Summary.

Use the dashboard for a quick visual review.

## Revision

What is the purpose of a Pareto analysis?

Why must revenue be sorted before cumulative share is calculated?

What does cumulative revenue share represent?

Why is 80% used as a practical reference?

What does a scatter plot show?

What does a high-unit, low-revenue point suggest?

What does a low-unit, high-revenue point suggest?

Why should business insights use more than one metric?

How can this analysis support inventory planning?

## Important Formulas

Revenue Share % = Product Revenue / Total Revenue × 100.

Cumulative Share = Previous Cumulative Share + Current Revenue Share.

Average Revenue per Unit = Revenue / Units.

Use SUMIFS or Pivot Tables when working directly in Excel.

Use GROUPBY-style logic or Pivot Tables for quick summaries.

Always validate the total revenue after aggregation.

## Key Takeaways

Pareto answers where revenue is concentrated.

Scatter analysis answers how volume and revenue relate.

Together they create a stronger product-performance view.

The analysis is descriptive and should be combined with business context.

## 🏅 Badges

- 🏅 **IIT Madras BS Degree**
- 🏅 **Business Data Management**
- 🏅 **Day 027 — Revenue Pareto & Scatter Plot**
- 🏅 **E-Commerce Case Study**
- 🏅 **Revenue Analytics Practice**