![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-081-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 081 Notes — A/B Testing of PayLater Nudges

## 1. PayLater Nudge Experiment
- The exercise combines nudge analysis with A/B testing.
- The central comparison is Control versus Treatment.
- Nudge_Type describes the intervention category.
- PayLater usage is the main binary outcome.

## 2. Control Variant
- Control is the reference experience.
- In this synthetic dataset it is associated with No Nudge.
- Control provides the comparison rate.
- Treatment results are interpreted relative to this reference.

## 3. Treatment Variant
- Treatment represents a changed experience.
- The treatment records use different synthetic nudge messages.
- Treatment exposure must be measured consistently.
- The intervention should be clearly defined before analysis.

## 4. Eligibility
- Eligibility identifies the intended analysis population.
- Not every raw record must necessarily be eligible.
- Exposure-based metrics use actual exposure counts.
- Eligibility and exposure are different concepts.

## 5. Nudge Exposure
- Nudge_Shown records whether a nudge was shown.
- Exposure is the denominator for conversion calculations.
- Exposure counts should be reported with rates.
- A rate without its denominator is incomplete.

## 6. Click Behaviour
- Clicked is a binary response.
- Click rate = clicks / exposures × 100.
- Click is an earlier funnel-stage outcome.
- Click behaviour does not guarantee PayLater usage.

## 7. PayLater Usage
- PayLater_Used_Flag is the primary outcome.
- It is represented as 0 or 1.
- Conversion rate measures PayLater usage among exposures.
- The outcome definition must remain constant across variants.

## 8. Absolute Lift
- Absolute lift compares treatment and control conversion rates.
- Formula: Treatment Rate − Control Rate.
- The unit is percentage points.
- It directly describes the observed rate difference.

## 9. Relative Lift
- Relative lift scales the absolute difference by control.
- Formula: (Treatment − Control) / Control × 100.
- Relative lift is useful for proportional comparison.
- It can become large when the baseline is small.

## 10. Nudge-Type Analysis
- No Nudge acts as the descriptive reference.
- Reminder Nudge is one treatment category.
- Social Proof is another treatment category.
- Limited Time Message is another treatment category.
- Each category should be compared using the same outcome definition.

## 11. Segment Analysis
- Customer segments can show heterogeneous response.
- Consumer, Retail, Business and Investor are synthetic categories.
- Segment-level exposure counts should be checked.
- Small groups can produce unstable rates.

## 12. Region Analysis
- Region provides a geographic grouping.
- North, South, West and East are synthetic.
- Regional differences can reflect composition.
- They do not automatically explain customer behaviour.

## 13. Device Analysis
- Device represents the synthetic access environment.
- Mobile, Desktop and Tablet are included.
- Device analysis provides descriptive context.
- Device is not automatically a causal mechanism.

## 14. Repayment
- Repayment_Flag is a secondary outcome.
- Repayment is distinct from PayLater conversion.
- A customer can use PayLater without being coded as repaid in this simplified dataset.
- Repayment should therefore be analysed separately.

## 15. Purchase Value
- Purchase_Value_Rupee is a monetary measure.
- Total purchase value and conversion answer different questions.
- Higher purchase value does not necessarily mean higher conversion.
- Monetary outcomes require clear unit definitions.

## 16. A/B Design
- Define the business question.
- Define the variants.
- Define the analysis population.
- Define exposure.
- Define the primary outcome.
- Define the measurement period.

## 17. Randomisation
- Random assignment helps balance observed and unobserved characteristics in expectation.
- It supports causal interpretation under appropriate assumptions.
- Random sampling and random assignment are different.
- The dataset is synthetic and does not document a real randomisation process.

## 18. Statistical Testing
- Conversion is a binary outcome.
- Two-proportion methods can compare conversion rates.
- Chi-square tests can assess categorical association.
- Confidence intervals describe uncertainty.
- Statistical significance is not the same as practical importance.

## 19. Sample Size
- Larger samples generally provide more stable estimates.
- Small samples can create large percentage fluctuations.
- Counts should accompany rates.
- Experiment duration and sample size should be planned.

## 20. Learning Outcome
- Explain PayLater nudge A/B testing.
- Calculate conversion.
- Calculate lift.
- Compare nudge categories.
- Analyse segments.
- Distinguish association from causality.

## 21. Practical Comparison
- Always compare the same population definition.
- Always use the same exposure rule.
- Keep primary and secondary outcomes separate.
- Report counts before interpreting percentages.

## 22. Reporting
- State the control rate.
- State the treatment rate.
- State absolute lift.
- State relative lift.
- State the sample size.
- State the main limitation.

## 23. Experiment Discipline
- Avoid changing the primary metric after seeing results.
- Record assumptions before analysis.
- Preserve the raw data.
- Keep derived fields reproducible.