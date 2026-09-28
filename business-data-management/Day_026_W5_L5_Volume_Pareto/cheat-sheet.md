# 🧠 Day 026 — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Course:** Business Data Management  
**Day:** 026  
**Topic:** Volume Pareto  

## ⚡ Core Formulas

Unit Share % = Product Units / Total Units × 100.

Cumulative Units = Running sum of Units.

Cumulative Share % = Cumulative Units / Total Units × 100.

Sort Units in descending order before cumulative calculations.

80% is a practical reference threshold.

## 🐍 Pandas

df.groupby('Product')['Units'].sum() → Product volume.

sort_values('Units', ascending=False) → Rank volume.

cumsum() → Running total.

sum() → Total volume.

nunique() → Number of products.

to_csv() → Export Pareto table.

## 📊 Excel

Pivot Table → Product-wise Units.

Sort Largest to Smallest → Pareto order.

SUM → Total Units.

Running Total → Cumulative Units.

Percentage → Unit Share.

Running Percentage → Cumulative Share.

Combo Chart → Units plus cumulative share.

## 📌 Pareto Steps

Choose the volume measure.

Group by product.

Calculate total volume.

Rank products.

Calculate unit share.

Calculate cumulative units.

Calculate cumulative share.

Identify the practical 80% group.

Interpret the business meaning.

## 🧠 Interpretation

Top-ranked products contribute the most volume.

A concentrated curve means fewer products drive more volume.

A flatter curve means volume is more distributed.

The threshold is used for prioritisation.

Do not automatically interpret volume as profitability.

## 💼 Business Use

Inventory prioritisation.

Warehouse planning.

Fulfilment planning.

Stock monitoring.

Operational prioritisation.

Product portfolio review.

## ⚠️ Common Mistakes

Not sorting before cumulative calculations.

Using revenue instead of units for a volume Pareto.

Forgetting total units.

Calculating share from unsorted data.

Treating 80% as an exact universal rule.

Calling volume equal to profit.

## 🏅 Badges

🏅 **IIT Madras BS Degree**

🏅 **Business Data Management**

🏅 **Day 026 — Volume Pareto**

🏅 **E-Commerce Case Study**

🏅 **Pareto Analysis Practice**