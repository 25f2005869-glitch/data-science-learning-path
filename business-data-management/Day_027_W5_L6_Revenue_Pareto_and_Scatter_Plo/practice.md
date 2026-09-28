# 📊 Day 027 — Practice

**Author:** Saloni Tiwari
**Programme:** IIT Madras BS Degree — Diploma Level
**Day:** 027
**Topic:** Revenue Pareto and Scatter Plot

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

## Practice Questions

Q1. Which product has the highest revenue?

Q2. Which product has the lowest revenue?

Q3. What is the total revenue?

Q4. Calculate the revenue share of the top product.

Q5. Which products belong to the core revenue group?

Q6. At what point does cumulative revenue cross 80%?

Q7. Which month has the highest revenue?

Q8. Which channel has the highest revenue?

Q9. Which region has the highest revenue?

Q10. Which product sells the most units?

Q11. Does the highest-volume product also have the highest revenue?

Q12. Identify one high-volume product with comparatively lower revenue.

Q13. Identify one lower-volume product with comparatively high revenue.

Q14. What business action would you recommend for the top revenue product?

Q15. Why is Pareto useful for inventory prioritization?

## Excel Tasks

Create a Pivot Table by Product.

Add Units and Revenue as values.

Sort revenue from largest to smallest.

Calculate revenue share.

Calculate cumulative revenue share.

Create a column chart for revenue by product.

Create a scatter chart using Units and Revenue.

Add suitable chart titles.

Write three observations below the charts.

## Python Tasks

Read the workbook with pandas.

Group by Product.

Aggregate Orders, Units and Revenue_Lakh.

Sort revenue descending.

Calculate revenue share.

Calculate cumulative revenue share.

Create the revenue chart.

Create the Pareto curve.

Create the scatter plot.

Export summary CSV files.

## 🏅 Badges

- 🏅 **IIT Madras BS Degree**
- 🏅 **Business Data Management**
- 🏅 **Day 027 — Revenue Pareto & Scatter Plot**
- 🏅 **E-Commerce Case Study**
- 🏅 **Revenue Analytics Practice**