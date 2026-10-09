![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-050-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 050 Notes — OEE Discussion

## 1. Introduction

OEE stands for Overall Equipment Effectiveness.
It combines three operational dimensions.
These are Availability, Performance and Quality.

## 2. Availability

Availability measures the proportion of planned production time during which production is running.

Formula:

Availability = Run Time / Planned Time.

## 3. Downtime

Downtime represents time unavailable for production.
Run Time equals Planned Time minus Downtime.

## 4. Performance

Performance compares actual output with ideal output.
Ideal output depends on run time and ideal cycle time.

Formula:

Performance = Actual Output / Ideal Output.

## 5. Quality

Quality measures good output relative to total output.

Formula:

Quality = Good Count / Total Count.

## 6. OEE

OEE combines the three components.

Formula:

OEE = Availability × Performance × Quality.

## 7. Why Components Matter

OEE alone is a combined value.
Component analysis provides more detail.

## 8. Product Analysis

OEE_Product_Summary compares products.
It includes the three components and OEE.

## 9. Monthly Analysis

OEE_Monthly tracks OEE over time.
It supports trend discussion.

## 10. Regional Analysis

OEE_Region compares operating regions.

## 11. Product-Region Analysis

OEE_Product_Region provides a more detailed comparison.

## 12. Excel Working

Start with planned time.
Subtract downtime to calculate run time.
Calculate availability.
Calculate ideal output.
Calculate performance.
Calculate quality.
Multiply components to calculate OEE.

## 13. Dashboard

The dashboard presents OEE and its components visually.
Use summary tables together with charts.

## 14. Python

Read OEE_Data with pandas.
Calculate ideal output.
Use groupby for product, month and region.
Calculate components.
Calculate OEE.
Export CSV summaries.
Create charts with matplotlib.

## 15. Interpretation

A component can be compared independently.
OEE differences should be examined through the component values.

## 16. Dataset Limitation

The data is illustrative.
It is not official IITM course data.

## 17. Business Use

OEE can support production monitoring.
It can support equipment discussion.
It can support comparison of operating periods.

## 18. Revision

Availability → Performance → Quality → OEE.

## 19. Learning Outcome

You should be able to calculate OEE and discuss its three components.

## 🏁 Summary

The key idea is to decompose OEE into Availability, Performance and Quality.

## 🏅 Badges

![BDM](https://img.shields.io/badge/BDM-OEE-blue?style=flat-square)
![Excel](https://img.shields.io/badge/Excel-OEE%20Analysis-green?style=flat-square)
![Analytics](https://img.shields.io/badge/Analytics-Manufacturing-orange?style=flat-square)