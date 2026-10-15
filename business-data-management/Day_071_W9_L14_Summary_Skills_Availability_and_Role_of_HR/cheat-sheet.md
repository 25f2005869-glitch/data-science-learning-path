![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-071-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 071 Cheat Sheet — Skills Availability and Role of HR

## Core Concepts
Skills Inventory.
Skill Availability.
Skill Gap.
Training Need.
Workforce Planning.
HR Analytics.

## Formulas
Availability Rate =
Available / Employees × 100.

Skill Gap Rate =
Skill Gaps / Employees × 100.

Training Need Rate =
Training Needs / Employees × 100.

Average Skill Score =
Sum of Skill Scores / Employees.

## Excel Functions
COUNTIF.
COUNTIFS.
SUMIF.
SUMIFS.
AVERAGEIF.
AVERAGEIFS.
IF.
IFERROR.
PivotTable.
Conditional Formatting.

## Example Excel Logic
=COUNTIF(skill_range,"Excel")

=COUNTIFS(dept_range,A2,skill_range,B2)

=IF(skill_score<70,1,0)

=Skill_Gaps/Employees*100

## Python
pd.read_excel()

pd.to_numeric()

groupby()

agg()

mean()

sum()

to_csv()

plt.bar()

plt.savefig()

## Main Fields
Employee_ID.
Department.
Region.
Job_Role.
Experience_Level.
Primary_Skill.
Secondary_Skill.
Skill_Score.
Training_Hours.
Performance_Score.

## Main Outputs
Skill Summary.
Department Summary.
Region Summary.
Role Summary.
Experience Summary.
KPI Summary.

## Dashboard
Employees by Skill.
Skill Gap by Department.
Availability by Region.
Average Skill Score by Role.

## HR Role
Inventory.
Gap analysis.
Training.
Workforce planning.
Internal mobility.
Development tracking.
Analytics.
Reporting.

## Data Checks
Unique Employee IDs.
No unexpected missing skills.
Consistent department labels.
Consistent role labels.
Valid score range.
Valid availability flags.
Valid gap flags.

## Interpretation Rules
Availability is descriptive.
A gap depends on its threshold.
Training hours do not prove improvement.
Group differences do not prove causation.
Synthetic data is for practice.

## Quick Questions
What is a skills inventory?
How is availability measured?
What is a skill gap?
Why document thresholds?
How can HR use skill data?
Why compare departments?
Why compare roles?
Why compare experience levels?

## Analysis Flow
Data → Skill Metric → Gap Analysis → Segmentation → HR Context → Dashboard.

## Final Reminder
Always document:
Metric.
Threshold.
Population.
Period.
Assumption.
Limitation.