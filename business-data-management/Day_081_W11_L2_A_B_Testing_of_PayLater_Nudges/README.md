![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-081-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📊 Day 081 — A/B Testing of PayLater Nudges

## 🎯 Objective
- Apply A/B testing to a PayLater nudge scenario.
- Compare control and treatment experiences.
- Measure PayLater usage.
- Calculate click and conversion rates.
- Calculate absolute and relative lift.

## 🧩 Case Context
- The package uses a synthetic PayLater learning dataset.
- Control represents the reference experience.
- Treatment represents a changed nudge experience.
- The data is not official IIT Madras data.
- The data is not real PayLater customer data.

## 🧪 Experiment Structure
- Experiment_ID identifies each observation.
- Customer_ID identifies the synthetic customer.
- Variant identifies Control or Treatment.
- Nudge_Type identifies the nudge category.
- Eligibility_Flag identifies the analysis population.
- Nudge_Shown identifies exposure.

## 📈 Primary Outcome
- PayLater_Used_Flag is the primary binary outcome.
- Conversion Rate = PayLater Users / Exposures × 100.
- Click rate measures an earlier response stage.
- Repayment is treated as a secondary outcome.

## 🧮 Main Metrics
- Control conversion rate.
- Treatment conversion rate.
- Absolute lift.
- Relative lift.
- Click rate.
- Repayment rate.
- Purchase value.

## 📂 Workbook
- PayLater_AB_Data contains the source dataset.
- Variant_Summary compares control and treatment.
- AB_Test_Metrics contains lift calculations.
- Nudge_Summary compares individual nudge types.
- Segment_Analysis examines customer segments.
- Region_Analysis examines geography.
- Device_Analysis examines device behaviour.
- AB_Testing_KPIs contains headline measures.
- Experiment_Framework defines key concepts.
- Analysis_Questions contains business questions.
- Business_Insights contains descriptive observations.
- Data_Dictionary documents the variables.
- PayLater_AB_Dashboard contains prepared charts.

## 📊 Dashboard
- Control versus treatment conversion.
- Conversion by nudge type.
- Conversion by customer segment.
- Conversion by region.

## 🐍 Python
- Reads the Excel source.
- Calculates variant-level metrics.
- Calculates nudge-level metrics.
- Creates segment, region and device summaries.
- Exports CSV files.
- Generates PNG charts.

## ⚠️ Interpretation
- An observed difference is not automatically causal evidence.
- Random assignment supports causal interpretation.
- Sample size affects estimate precision.
- Synthetic results cannot be generalised to real PayLater users.

## 🏅 Badges
- 🧪 A/B Testing.
- 💳 PayLater.
- 📊 Business Analytics.
- 📈 Experimentation.
- 🐍 Python.
- 📗 Excel.

## ✅ Completion
- Dataset prepared.
- Variant analysis prepared.
- Nudge comparison prepared.
- Segment analysis prepared.
- Dashboard prepared.
- Python outputs generated.
- Documentation completed.

## 📌 Repository Use
- Keep the Excel workbook in the Day 081 root folder.
- Keep the Python script inside the code folder.
- Keep generated CSV and PNG outputs inside python_outputs.
- Use the workbook dashboard for presentation practice.
- Use the Markdown files for revision and documentation.

## 🔗 Learning Connection
- Day 080 introduced general A/B testing.
- Day 081 applies the framework to PayLater nudges.
- The next analyses can extend the experiment with stronger statistical methods.