![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-066-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 066 Cheat Sheet — Selection Criteria

## Criteria

Technical >= 70

Communication >= 75

Interview >= 80

Overall >= 75

Experience >= 1 year

## Eligibility

Technical_Eligible = Technical >= 70

Communication_Eligible = Communication >= 75

Interview_Eligible = Interview >= 80

Overall_Eligible = Overall >= 75

Experience_Eligible = Experience >= 1

## Pass Count

Criteria_Pass_Count =
Technical_Eligible
+ Communication_Eligible
+ Interview_Eligible
+ Overall_Eligible
+ Experience_Eligible

## Criteria Met

Criteria_Met = 1 when Criteria_Pass_Count >= 4.

Otherwise Criteria_Met = 0.

## Weighted Score

Weighted Score =
Technical × 0.30
+ Communication × 0.20
+ Interview × 0.30
+ Overall × 0.20

## Excel

IF() → threshold test.

SUM() → count passed flags.

COUNTIF() → count candidates.

AVERAGEIF() → average score by group.

SUMIF() → grouped totals.

PivotTable → segmentation.

## Python

pd.read_excel()

pd.to_numeric()

groupby()

agg()

mean()

sum()

to_csv()

## Useful KPIs

Candidate Count

Criteria Met

Criteria Met Rate

Selected Count

Selection Rate

Average Weighted Score

Average Overall Score

## Analysis Dimensions

Department

Role

Experience Level

Region

## Checks

Thresholds must be explicit.

Weights should sum to 100%.

Score scales should be known.

Missing scores need review.

Selected status should remain distinct.

## Interpretation

Threshold = minimum requirement.

Weight = relative contribution.

Pass Count = number of criteria met.

Weighted Score = combined score.

Criteria Met = model-specific status.

## Quick Revision

1. What is a selection criterion?
2. What is a threshold?
3. Why use eligibility flags?
4. How is pass count calculated?
5. Why use weighted scores?
6. Why must weights sum to 100%?
7. What is the difference between criteria met and selected?
8. Why analyze criteria by department?

## Formula Checks

Weighted score remains on the score scale when weights sum to one.

Criteria pass count cannot exceed the number of criteria.

Criteria met rate = Criteria Met / Candidates × 100.

Selection rate = Selected / Candidates × 100.