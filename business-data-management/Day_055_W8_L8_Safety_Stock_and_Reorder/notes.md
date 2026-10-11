![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-055-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 055 Notes

## 🎯 Topic

Safety Stock and Reorder

## 1. Inventory Management

Inventory management ensures that a business maintains enough stock to support operations.

Too little inventory can cause shortages.

Too much inventory can increase holding costs.

Therefore, businesses need useful inventory control methods.

## 2. Demand

Demand represents the quantity required or consumed over a period.

For this analysis, average daily demand is used.

## 3. Lead Time

Lead time represents the time required to replenish inventory.

It is usually measured in days.

A longer lead time generally increases the inventory required before replenishment.

## 4. Lead-Time Demand

Lead-time demand estimates demand during the replenishment period.

Formula:

Average Daily Demand × Average Lead Time

## 5. Safety Stock

Safety stock is additional inventory maintained to protect against uncertainty.

Uncertainty can occur because of:

- Demand variation
- Supplier delays
- Production delays
- Delivery delays

## 6. Reorder Point

Reorder point identifies the inventory level at which replenishment should be initiated.

Formula:

Reorder Point = Lead-Time Demand + Safety Stock

## 7. Reorder Coverage

Reorder coverage days estimate how many average-demand days are represented by the reorder point.

Formula:

Reorder Coverage Days = Reorder Point / Average Daily Demand

## 8. Inventory Gap

Inventory gap compares closing inventory with reorder point.

Formula:

Inventory Gap = Closing Inventory − Reorder Point

## 9. Interpreting the Gap

If the gap is negative:

Inventory is below the reorder point.

If the gap is zero:

Inventory is exactly at the reorder point.

If the gap is positive:

Inventory is above the reorder point.

## 10. Stock Status

The workbook classifies records into:

- Below Reorder Point
- At/Above Reorder Point

## 11. Product Analysis

Product-level analysis helps identify products with higher inventory requirements.

The workbook analyzes:

- Gears
- Shafts
- Bearings

## 12. Regional Analysis

Regional analysis compares inventory requirements across:

- North
- South
- West

## 13. Monthly Analysis

Monthly analysis helps understand changes over time.

Important measures include:

- Demand
- Safety stock
- Lead-time demand
- Reorder point
- Closing inventory

## 14. Business Use

Reorder point analysis can support procurement and inventory planning.

It helps businesses identify potential replenishment requirements.

## 15. Excel Working

The workbook separates raw data from calculation sheets.

This makes the analysis easier to understand.

## 16. Python Working

Python reproduces the calculations programmatically.

The script also exports CSV files.

## 17. Visualization

Charts help communicate inventory patterns.

The dashboard contains product, monthly and regional views.

## 18. Important Learning

Safety stock and reorder point are different concepts.

Safety stock is additional protection.

Reorder point combines expected lead-time demand with safety stock.

## 19. Practical Question

If average daily demand increases while lead time remains unchanged, lead-time demand increases.

This can increase the reorder point.

## 20. Practical Question

If lead time increases while demand remains unchanged, lead-time demand increases.

Therefore, reorder requirements can also increase.

## 21. Summary

The main workflow is:

Raw Data

→ Demand Analysis

→ Lead-Time Demand

→ Safety Stock

→ Reorder Point

→ Inventory Gap

→ Stock Status

→ Business Insight

## 🏅 Badges

![Inventory](https://img.shields.io/badge/Inventory-Analysis-green)
![Excel](https://img.shields.io/badge/Excel-Practice-blue)
![Python](https://img.shields.io/badge/Python-Practice-orange)

## 👤 Author

Saloni Tiwari

## 🎓 Programme

IIT Madras BS Degree — Diploma Level

## 📅 Day

055

---