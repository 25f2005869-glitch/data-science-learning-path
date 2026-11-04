![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-068-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 068 Notes — Composite Score and Ranking

## 1. Composite Score

A composite score combines multiple numerical inputs into one calculated measure.

## 2. Component

Each assessment variable is a component of the composite score.

## 3. Technical Score

Technical Score contributes 30 percent.

## 4. Communication Score

Communication Score contributes 20 percent.

## 5. Interview Score

Interview Score contributes 30 percent.

## 6. Overall Score

Overall Score contributes 20 percent.

## 7. Weight

A weight represents the contribution assigned to a component.

## 8. Weight Validation

The weights should sum to 100 percent.

## 9. Weighted Contribution

Weighted contribution equals score multiplied by its weight.

## 10. Composite Formula

The four weighted contributions are added.

## 11. Ranking

Ranking orders records according to composite score.

## 12. Rank One

The highest composite score receives rank one.

## 13. Ties

Equal composite scores can create tied ranks.

## 14. Percentile

Percentile provides a relative position within the dataset.

## 15. Department Segmentation

Department grouping shows descriptive differences in composite scores.

## 16. Experience Segmentation

Experience level provides another grouping dimension.

## 17. Region Segmentation

Region provides geographic context.

## 18. Role Segmentation

Target role allows role-level score analysis.

## 19. Selection Status

Selected_Flag is kept separate from the calculated ranking.

## 20. Ranking vs Selection

A rank describes position under the scoring model.

Selection status represents the separate illustrative outcome.

## 21. Weight Sensitivity

Changing weights changes composite scores.

## 22. Example

Increasing the technical weight makes technical performance contribute more strongly.

## 23. Score Scale

Components should use compatible scales before combining them.

## 24. Scale Problem

Different scales can distort a weighted sum.

## 25. Missing Values

Missing component scores should be reviewed before calculating a composite.

## 26. Data Quality

Candidate identifiers should be checked for duplicates.

## 27. Formula Audit

Each weight and formula should be documented.

## 28. Ranking Audit

Sort order should be verified.

## 29. Tie Handling

The ranking method should be explicitly documented.

## 30. Top-N Analysis

Top five and top ten groups can be extracted for review.

## 31. Rank Bands

Rank bands divide candidates into predefined position groups.

## 32. Dashboard

The dashboard summarizes grouped composite scores and the top ten.

## 33. Excel

SUMPRODUCT can calculate a weighted score.

## 34. Python

Pandas rank can create a ranking column.

## 35. Business Use

Composite scoring can support structured analysis when inputs and assumptions are transparent.

## 36. Limitation

A numeric score does not capture every qualitative factor.

## 37. Model Governance

Weights should be documented and reviewed.

## 38. Interpretation

A ranking is conditional on the scoring framework.

## 39. Synthetic Data

The dataset is created for practice.

## 40. Final Learning

Composite scoring demonstrates how multiple business variables can be converted into a structured analytical measure.