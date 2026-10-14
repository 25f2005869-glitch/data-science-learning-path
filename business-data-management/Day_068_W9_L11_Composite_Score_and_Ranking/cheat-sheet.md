![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-068-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# ⚡ Day 068 Cheat Sheet — Composite Score and Ranking

## Weights

Technical = 30%.

Communication = 20%.

Interview = 30%.

Overall = 20%.

Total = 100%.

## Formula

Composite =
Technical × 0.30
+ Communication × 0.20
+ Interview × 0.30
+ Overall × 0.20.

## Excel

=SUMPRODUCT(B2:E2,$B$1:$E$1)

=RANK.EQ(F2,$F$2:$F$31,0)

=PERCENTRANK.INC($F$2:$F$31,F2)*100

## Python

df["Composite_Score"] = ...

df["Composite_Rank"] = df["Composite_Score"].rank(
    method="min",
    ascending=False
)

## Core Fields

Technical_Score

Communication_Score

Interview_Score

Overall_Score

Composite_Score

Composite_Rank

Composite_Percentile

Selected_Flag

## Ranking

Highest score → rank 1.

Descending order → highest first.

Equal values → tied ranks depending on ranking method.

## KPIs

Total Candidates.

Average Composite Score.

Highest Composite Score.

Lowest Composite Score.

Selected Candidate Average Score.

Selected Candidates.

## Grouping

Department.

Experience Level.

Region.

Target Role.

## Dashboard

Department average.

Experience-level average.

Region average.

Top ten ranking.

## Rank Bands

Top 5.

Top 10.

Top 25.

All Candidates.

## Checks

Weights sum to 100%.

All component scores use compatible scales.

No unexpected missing values.

Ranking order is descending.

Ties are documented.

Selected_Flag is not used to create Composite_Score.

## Interpretation

Composite score = combined measure.

Rank = relative position.

Percentile = relative standing.

Weight = contribution.

Selection = separate outcome.

## Common Mistakes

Forgetting a weight.

Using weights that do not sum to 100%.

Mixing score scales.

Sorting ascending accidentally.

Ignoring ties.

Treating rank as an absolute quality measure.

## Python Outputs

candidate_composite_scores.csv

department_composite_summary.csv

experience_level_composite_summary.csv

region_composite_summary.csv

role_composite_summary.csv

top_10_composite_ranking.csv

## Charts

average_composite_score_by_department.png

average_composite_score_by_experience_level.png

average_composite_score_by_region.png

top_10_composite_ranking.png

## Quick Revision

What is a composite score?

Why use weights?

Why must weights be documented?

How is rank calculated?

What is percentile?

How are ties handled?

Why separate ranking and selection?

What happens when weights change?

## Final Formula

Composite Score =
Σ(Component Score × Component Weight).