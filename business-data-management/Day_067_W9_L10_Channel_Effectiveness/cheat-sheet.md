![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-067-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 067 Cheat Sheet — Channel Effectiveness

## Core Definitions

Channel = sourcing route.

Candidate = sourcing record used for analysis.

Selected = Selected_Flag equals 1.

Selection Rate = Selected / Candidates × 100.

Total Cost = sum of Sourcing_Cost.

Average Cost = mean of Sourcing_Cost.

Average Days = mean of Days_to_Fill.

Cost per Selected = Total Cost / Selected.

Average Satisfaction = mean of Satisfaction_Score.

## Channel Fields

Sourcing_Channel

Candidate_ID

Department

Region

Target_Role

Month

Application_Count

Days_to_Fill

Sourcing_Cost

Satisfaction_Score

Selected_Flag

## Excel Functions

COUNTIF()

COUNTIFS()

SUMIF()

SUMIFS()

AVERAGEIF()

AVERAGEIFS()

IF()

ROUND()

## Useful Excel Formulas

Selection Rate:

=Selected/Candidates

Cost per Selected:

=Total_Sourcing_Cost/Selected

Average Cost:

=AVERAGE(Cost_Range)

Average Days:

=AVERAGE(Days_Range)

Selected Count:

=SUM(Selected_Flag_Range)

## Python Pattern

pd.read_excel()

pd.to_numeric()

groupby()

agg()

mean()

sum()

to_csv()

## Grouping

groupby("Sourcing_Channel")

groupby("Department")

groupby("Region")

groupby("Month")

groupby("Target_Role")

## Channel KPIs

Candidates

Applications

Selected

Selection Rate

Average Days to Fill

Average Sourcing Cost

Total Sourcing Cost

Average Satisfaction

Cost per Selected

## Dashboard Metrics

Candidates → reach.

Selection Rate → conversion.

Average Cost → resource use.

Average Days → speed.

## Interpretation Rules

High volume is not equal to high conversion.

High conversion is not equal to low cost.

Low cost is not equal to fast hiring.

Fast hiring is not equal to high satisfaction.

Use several metrics together.

## Data Checks

Check missing values.

Check duplicate candidates.

Check invalid flags.

Check negative costs.

Check zero selected records before dividing.

Check consistent month values.

## Quick Questions

What is channel effectiveness?

What is selection rate?

Why use cost per selected?

Why compare average and total cost?

Why segment by department?

Why examine monthly trends?

What is the limitation of synthetic data?

## Python Output Files

channel_effectiveness_data.csv

channel_effectiveness_summary.csv

department_channel_summary.csv

region_channel_summary.csv

monthly_channel_summary.csv

role_channel_summary.csv

## Chart Files

candidates_by_channel.png

selection_rate_by_channel.png

average_sourcing_cost_by_channel.png

average_days_to_fill_by_channel.png

## Revision Formula

Effectiveness analysis =

Reach + Conversion + Cost + Speed + Quality Context.