![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-079-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 079 Notes — Factors for Nudge Presentation

## 1. What Is a Factor?
- A factor is a variable used to compare behaviour across groups.
- In this case factors include nudge type, segment, region, device and category.
- A factor should have clearly defined categories.
- Factor analysis is primarily comparative.

## 2. Nudge Type
- Nudge_Type identifies the intervention category.
- Different nudge types represent different presentation treatments.
- A default recommendation is used as a descriptive reference.
- Comparisons require a common outcome definition.

## 3. Nudge Exposure
- Nudge_Shown indicates whether the intervention was displayed.
- Exposure is the denominator for exposure-based rates.
- Records without exposure require careful treatment.
- A high exposure count increases the amount of observed response data.

## 4. Click Response
- Clicked is a binary response variable.
- Click rate measures click activity among exposures.
- Formula: Clicks / Exposures × 100.
- Click behaviour occurs before purchase behaviour in this simplified case.

## 5. Purchase Response
- Purchased_Flag represents the purchase outcome.
- Conversion rate measures purchases relative to exposures.
- Formula: Purchases / Exposures × 100.
- Conversion is different from click rate.

## 6. Order Value
- Order_Value_Rupee records the synthetic order amount.
- Zero values represent observations without a purchase.
- Total order value measures aggregate monetary activity.
- Average order value should normally be calculated over purchases.

## 7. Repeat Visit
- Repeat_Visit_Flag represents return behaviour.
- It adds a post-response engagement dimension.
- Repeat visits should not be treated as purchases.
- Repeat-visit rate can provide additional context.

## 8. Baseline
- A baseline gives the comparison reference.
- Default Recommendation is used as the reference in this package.
- Baseline conversion is calculated from the relevant observations.
- Lift is expressed in percentage points.

## 9. Lift
- Lift compares a factor's conversion rate with the baseline.
- Formula: factor conversion rate − baseline conversion rate.
- Positive lift means the observed rate is above the reference.
- Negative lift means the observed rate is below the reference.

## 10. Customer Segmentation
- Customer segments can reveal heterogeneous response.
- Consumer, Retail, Business and Investor are synthetic categories.
- Segment results should be checked for sufficient observations.
- Aggregate differences may reflect composition.

## 11. Device Factor
- Device represents the synthetic access category.
- Mobile, Desktop and Tablet are included.
- Device comparisons can identify descriptive response differences.
- Device alone does not establish why behaviour differs.

## 12. Region Factor
- Region groups observations geographically.
- North, South, West and East are synthetic labels.
- Region analysis provides contextual comparison.
- Regional differences may reflect sample composition.

## 13. Category Factor
- Category identifies the synthetic product category.
- Electronics, Fashion, Grocery and Finance are included.
- Category can affect order value and purchase behaviour.
- Category should be considered when interpreting nudge results.

## 14. Presentation Structure
- Start with the business question.
- Explain the dataset.
- Define factors.
- Establish the baseline.
- Show comparisons.
- Show segmentation.
- Present limitations.
- Close with evidence requirements.

## 15. Data Quality
- Check duplicate identifiers.
- Check missing outcomes.
- Validate binary fields.
- Check exposure denominators.
- Verify order-value units.

## 16. Causal Caution
- Association is not causation.
- Group differences can have multiple explanations.
- Randomisation improves causal interpretation.
- Confounding variables should be considered.

## 17. Visual Design
- Use one question per chart.
- Show units.
- Use consistent factor labels.
- Avoid unnecessary chart decoration.
- Keep presentation conclusions tied to observed data.

## 18. Learning Outcome
- Define nudge factors.
- Calculate response rates.
- Establish a baseline.
- Calculate lift.
- Segment response.
- Present evidence clearly.