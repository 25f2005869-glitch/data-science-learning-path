![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-080-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 080 Notes — A/B Testing Introduction

## 1. A/B Testing
- A/B testing compares two or more variants.
- A simple A/B test commonly uses control and treatment.
- The purpose is to evaluate an outcome under different experiences.
- The experimental unit should be defined clearly.

## 2. Control
- Control is the reference experience.
- It provides the comparison level.
- Control should use the same outcome definition as treatment.
- A baseline is meaningful only when the groups are comparable.

## 3. Treatment
- Treatment is the changed experience.
- The treatment can modify a message, layout, feature or intervention.
- The exact treatment should be documented.
- Treatment results are interpreted relative to control.

## 4. Random Assignment
- Random assignment allocates units to variants by chance.
- It can reduce systematic differences between groups.
- It supports causal interpretation when other assumptions are satisfied.
- Random assignment is different from random sampling.

## 5. Exposure
- Exposure indicates that a unit received the relevant experience.
- Exposure is the denominator for exposure-based rates.
- The same exposure definition should be used across variants.
- Invalid denominators can produce misleading rates.

## 6. Binary Outcomes
- Clicked is represented as 0 or 1.
- Purchased_Flag is represented as 0 or 1.
- Binary outcomes are suitable for proportion-based analysis.
- Counts should be retained alongside percentages.

## 7. Conversion Rate
- Conversion rate is purchases divided by exposures.
- It is expressed as a percentage.
- Formula: Purchases / Exposures × 100.
- The denominator must be stated.

## 8. Click Rate
- Click rate is clicks divided by exposures.
- It describes an earlier response stage.
- A high click rate does not guarantee a high purchase rate.
- Funnel stages should be analysed separately.

## 9. Absolute Lift
- Absolute lift compares treatment and control rates directly.
- Formula: Treatment Rate − Control Rate.
- It is expressed in percentage points.
- Percentage points should not be confused with percent change.

## 10. Relative Lift
- Relative lift scales the difference by the control rate.
- Formula: (Treatment − Control) / Control × 100.
- It is expressed as a percentage.
- Relative lift can look large when the baseline is small.

## 11. Order Value
- Order value is a secondary monetary outcome.
- Total order value describes aggregate value.
- Average order value should focus on actual purchases.
- Monetary value and conversion measure different dimensions.

## 12. Segment Analysis
- Segment analysis checks whether response varies by customer group.
- Consumer, Retail, Business and Investor are synthetic categories.
- Segment comparisons should consider exposure counts.
- Small subgroup counts can make rates unstable.

## 13. Region Analysis
- Region provides a geographic comparison dimension.
- North, South, West and East are synthetic labels.
- Regional differences can reflect composition.
- Region alone does not explain behavioural causes.

## 14. Device Analysis
- Device represents the access environment.
- Mobile, Desktop and Tablet are included.
- Device-level rates can reveal descriptive variation.
- Device is not automatically a causal explanation.

## 15. Statistical Extension
- Binary outcomes can be analysed using proportion tests.
- Chi-square methods can be useful for categorical outcomes.
- Confidence intervals describe uncertainty.
- Statistical significance and practical significance are different concepts.

## 16. Sample Size
- Larger samples generally provide more stable estimates.
- Small samples can create large rate fluctuations.
- Exposure counts should accompany conversion rates.
- A percentage without its denominator is incomplete.

## 17. Presentation
- Start with the business question.
- Define control and treatment.
- Show sample counts.
- Show primary outcome rates.
- Show lift.
- Explain limitations.

## 18. Causal Interpretation
- Random assignment supports causal reasoning.
- Observational comparisons have additional confounding risks.
- A causal claim requires appropriate design and assumptions.
- The synthetic dataset is only an educational example.

## 19. Learning Outcome
- Explain A/B testing.
- Define control and treatment.
- Calculate conversion.
- Calculate lift.
- Analyse segments.
- Communicate experimental results responsibly.