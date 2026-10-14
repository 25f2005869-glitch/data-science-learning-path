![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-066-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 066 Notes — Selection Criteria

## 1. Meaning of Selection Criteria

Selection criteria are measurable requirements used to evaluate candidates.

They translate a role requirement into an assessment rule.

## 2. Threshold Criterion

A threshold specifies a minimum acceptable value.

Example: Technical Score >= 70.

## 3. Technical Criterion

Technical score represents role-related technical assessment.

The threshold must match the intended assessment scale.

## 4. Communication Criterion

Communication score measures the communication dimension in this illustrative model.

The threshold is 75.

## 5. Interview Criterion

Interview score is treated as another selection input.

The illustrative threshold is 80.

## 6. Overall Criterion

Overall Score provides a composite assessment field.

The threshold is 75.

## 7. Experience Criterion

Experience Years is checked against a minimum requirement.

The model uses at least one year.

## 8. Eligibility Flag

A Boolean condition can be converted into 1 or 0.

1 means the candidate meets that criterion.

0 means the candidate does not.

## 9. Criteria Pass Count

Criteria_Pass_Count is the sum of the individual criterion flags.

It gives a compact view of threshold attainment.

## 10. Criteria Met Status

The learning model marks a candidate as Criteria Met when at least four criteria are passed.

This is an illustrative rule.

## 11. Weighted Scoring

Weighted scoring assigns different importance to different criteria.

The weights should be defined before calculating the final score.

## 12. Weight Sum

The four scoring weights are 30%, 20%, 30% and 20%.

They sum to 100%.

## 13. Why Weighting Matters

Equal scoring assumes equal importance.

Weighting allows the analyst to represent different importance levels.

## 14. Department Analysis

Department grouping shows how criteria attainment varies across functions.

This is descriptive segmentation.

## 15. Role Analysis

Role grouping helps identify differences across target positions.

Different roles may require different criteria in real settings.

## 16. Experience-Level Analysis

Graduate and experienced groups can be compared.

Experience level can provide useful context for score distributions.

## 17. Region Analysis

Regional grouping provides geographic segmentation.

It does not explain why regional differences occur.

## 18. Criteria vs Selection

Criteria_Met is a calculated learning status.

Selected_Flag is a separate illustrative outcome.

The two should not be silently treated as identical.

## 19. Data Quality

Check missing assessment scores.

Check score ranges.

Check candidate IDs.

Check duplicate records.

Check threshold definitions.

## 20. Excel Workflow

Review Selection_Criteria.

Inspect Candidate_Summary.

Use department and role summaries.

Review the dashboard.

## 21. Python Workflow

Read Selection_Data.

Create eligibility flags.

Calculate weighted score.

Group by relevant dimensions.

Export summaries and charts.

## 22. Real-World Extension

A real selection model could include:

Structured assessment rubrics.

Role-specific technical requirements.

Experience relevance.

Qualification requirements.

Reference checks.

Work samples.

## 🧠 Summary

Selection criteria provide structure to candidate evaluation.

Thresholds make requirements explicit.

Weights represent relative importance.

Segmentation shows how criteria behave across candidate groups.