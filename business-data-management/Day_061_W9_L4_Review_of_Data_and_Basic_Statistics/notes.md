![Course](https://img.shields.io/badge/Course-Business%20Data%20Management-blue?style=for-the-badge)
![Learning Path](https://img.shields.io/badge/Learning%20Path-100%20Days-green?style=for-the-badge)
![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Diploma-orange?style=for-the-badge)
![Day](https://img.shields.io/badge/Day-061-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

# 📝 Day 061 Notes — Review of Data and Basic Statistics

## 1. Purpose of Data Review

Data review is the process of understanding a dataset before analysis.
It helps identify structural and quality issues.
It also confirms that variables are suitable for the planned analysis.

## 2. Record Review

Count the number of observations.
Check whether every record has a unique identifier.
Review whether the observation period is consistent.
Check whether the dataset contains unexpected rows.

## 3. Missing Values

Missing values should be identified before calculating statistics.
A missing value can change counts and averages.
The treatment of missing data should depend on the business context.

## 4. Duplicate Records

Duplicate identifiers can indicate repeated records.
Duplicates should be investigated before aggregation.
Do not automatically delete records without understanding their meaning.

## 5. Categorical Variables

Department, region and internal source are categorical variables.
Frequency tables can summarize their distribution.
Counts can reveal how observations are distributed across categories.

## 6. Numerical Variables

Internal cost, planned days and actual days are numerical variables.
Satisfaction is represented numerically in this illustrative dataset.
Numerical variables support descriptive statistical analysis.

## 7. Mean

Mean = Sum of observations ÷ Number of observations.
Mean uses every observation.
It can be influenced by unusually high or low values.

## 8. Median

Median is the middle value after sorting.
For an even number of observations, the median is the average of the two middle values.
Median is often useful when values are unevenly distributed.

## 9. Mode

Mode is the most frequently occurring value.
It is especially useful for categorical variables.
A dataset can have more than one mode.

## 10. Minimum and Maximum

Minimum identifies the smallest observed value.
Maximum identifies the largest observed value.
Together they show the observed endpoints.

## 11. Range

Range = Maximum − Minimum.
Range is simple to calculate.
It uses only the two extreme values.

## 12. Standard Deviation

Standard deviation measures dispersion around the mean.
A larger standard deviation indicates greater spread in the observations.
A smaller standard deviation indicates observations are more concentrated around the mean.

## 13. Quartiles

Q1 represents the 25th percentile.
Q2 corresponds to the median.
Q3 represents the 75th percentile.

## 14. Interquartile Range

IQR = Q3 − Q1.
IQR describes the spread of the middle 50 percent of observations.
It is less affected by extreme observations than the full range.

## 15. Grouped Statistics

Statistics can be calculated by department.
They can also be calculated by region or internal source.
Group comparisons should use consistent definitions.

## 16. Excel Review

Use COUNT and COUNTA for counts.
Use SUM for totals.
Use AVERAGE for the mean.
Use MEDIAN for the median.
Use MIN and MAX for endpoints.
Use STDEV.S for sample standard deviation.
Use QUARTILE.INC for quartiles.

## 17. Python Review

Use pandas read_excel to load the workbook.
Use describe() for a quick numerical summary.
Use mean(), median(), std(), min() and max().
Use groupby() for segmented analysis.

## 18. Interpretation

Statistics describe observed data.
They do not automatically establish reasons.
Business context is needed before explaining patterns.

## 19. Day 061 Summary

Review the data first.
Check quality before calculating.
Use multiple statistics to describe numerical variables.
Compare mean and median.
Use standard deviation and IQR to understand variation.
Use grouped summaries for business segmentation.

## 🏅 Badges

🔍 Data Review
📐 Statistics
📗 Excel
🐍 Python
🎓 BDM