# Day 033 — Days of Sales of Inventory Notes

![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-033-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 033  
**Topic:** Days of Sales of Inventory

## 📚 Lecture

W6_L5 focuses on Days of Sales of Inventory.

The topic continues the inventory analysis sequence.

The main objective is to understand inventory in relation to sales.

## 📦 Inventory

Inventory is the stock of goods available for sale or business use.

Inventory changes because of purchases and sales.

Therefore, inventory analysis should consider movements over time.

## 📊 Sales Units

Sales Units represents the number of units sold.

Total sales units can be converted into an average daily sales figure.

This is necessary for calculating DSI.

## 📅 Observation Period

The observation period determines the number of days used in the calculation.

For the practical dataset:

Observation Days = Maximum Date − Minimum Date + 1

The same period should be used consistently.

## 🧮 Average Daily Sales

Formula:

Average Daily Sales = Total Sales Units / Observation Days

This converts total sales into a daily sales rate.

The resulting value is measured in units per day.

## 📌 Average Inventory

Average inventory represents the typical inventory level during the observation period.

The practical workbook uses recorded closing inventory values to calculate the average.

Formula:

Average Inventory = Average of Closing Stock

## 📐 DSI

Days of Sales of Inventory is calculated as:

DSI = Average Inventory / Average Daily Sales

The result is expressed in days.

## 🔍 Interpretation

If DSI is higher:

- More inventory is held relative to daily sales.
- Inventory coverage is higher.
- The observed sales rate is lower relative to inventory.

If DSI is lower:

- Fewer inventory days are represented.
- Sales velocity is higher relative to inventory.
- Inventory coverage is lower.

## 🔄 Inventory Turnover

Inventory turnover is another inventory-efficiency measure.

For this exercise:

Inventory Turnover = Total Sales Units / Average Inventory

It shows sales volume relative to average inventory.

## 📊 Product Analysis

Product-level analysis allows comparison between products.

For each product calculate:

- Total purchases
- Total sales units
- Average inventory
- Closing inventory
- Average daily sales
- DSI
- Inventory turnover

## 📈 Monthly Analysis

Monthly inventory analysis helps identify changes over time.

The workbook includes monthly inventory information.

This can be used to observe:

- Purchases
- Sales
- Closing inventory

## 🧠 Business Meaning

DSI should not be interpreted alone.

A product may have high DSI because:

- Sales are relatively slow.
- Inventory is intentionally maintained.
- Demand is seasonal.
- Replenishment policy requires additional stock.

These are possible explanations, not conclusions from DSI alone.

## ⚠️ Important Limitation

DSI does not directly measure:

- Profitability
- Revenue
- Customer satisfaction
- Product quality

It is an inventory-related metric.

## 💻 Excel Practice

Open the workbook.

Start with Inventory_Data.

Review:

- Dates
- Products
- Sales units
- Closing stock

Then open Product_DSI_Analysis.

## 📊 Dashboard Practice

Use DSI_Dashboard to review:

- DSI by product
- Monthly closing inventory
- Inventory turnover

Compare the products using the same methodology.

## 🐍 Python Practice

The Python script uses pandas.

Basic workflow:

```text
Read Excel
↓
Convert Date
↓
Calculate period
↓
Group by Product
↓
Calculate inventory
↓
Calculate sales rate
↓
Calculate DSI
↓
Calculate turnover
↓
Export results