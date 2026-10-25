# 📝 Day 098 — Credit Risk Analysis — Practice

![IIT Madras](https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red?style=for-the-badge)
![Business Data Management](https://img.shields.io/badge/Business%20Data%20Management-Day%20098-blue?style=for-the-badge)
![Credit Risk](https://img.shields.io/badge/Credit%20Risk-Practice-green?style=for-the-badge)
![Excel](https://img.shields.io/badge/Excel-Practice-orange?style=for-the-badge)

---

## 👤 Metadata

- **Author:** Saloni Tiwari
- **Programme:** IIT Madras BS Degree — Diploma Level
- **Day:** 098
- **Topic:** Credit Risk Analysis

---

# 1. Basic Understanding

1. What is Credit Risk?
2. What is Credit Risk Analysis?
3. Why is Credit Risk Analysis important in business data analysis?
4. What is a Credit Score?
5. What is Loan Amount?
6. What is Loan Tenure?
7. What is Debt-to-Income Ratio?
8. What is Loan Status?
9. What is a Defaulted Loan?
10. What is Risk Category?

---

# 2. Dataset Understanding

11. What is the purpose of `Customer_ID`?
12. What information does `Loan_Date` provide?
13. Why is `Monthly_Income` useful in credit-risk analysis?
14. Why is `Credit_Score` important?
15. What does `Loan_Amount` represent?
16. What does `Interest_Rate_%` represent?
17. What does `Loan_Tenure_Months` represent?
18. What does `Existing_Loans` represent?
19. What does `Debt_to_Income_Ratio_%` represent?
20. What are the four Risk Categories in the dataset?
21. What are the four Loan Status values in the dataset?

---

# 3. Risk Classification Practice

22. What variables are used to calculate the practice Risk Category?
23. What Credit Score and DTI conditions define Low Risk?
24. What conditions define Medium Risk?
25. What conditions define High Risk?
26. What happens when a record does not satisfy the Low, Medium or High conditions?
27. Why is Risk Category recalculated after cleaning?

---

# 4. Risk Classification Questions

Using the Day 098 risk rules, identify the category.

28. Credit Score = 760, DTI = 25%. What is the Risk Category?

29. Credit Score = 700, DTI = 35%. What is the Risk Category?

30. Credit Score = 650, DTI = 45%. What is the Risk Category?

31. Credit Score = 600, DTI = 55%. What is the Risk Category?

32. Credit Score = 750, DTI = 35%. Which condition does this record satisfy?

33. Credit Score = 690, DTI = 45%. Which risk category applies?

34. Credit Score = 630, DTI = 48%. Which risk category applies?

35. Credit Score = 800, DTI = 20%. Which risk category applies?

---

# 5. Data Quality Practice

36. Why should data quality be checked before analysis?
37. Why are extra spaces a data-quality problem?
38. Why can inconsistent capitalization affect analysis?
39. Why are negative Loan Amount values invalid?
40. Why are negative Existing Loans invalid?
41. Why should Credit Score be validated?
42. Why should DTI be validated?
43. Why should Loan Tenure be positive?
44. Why can duplicate rows distort KPIs?
45. Why should invalid numeric text such as `N/A` be handled?

---

# 6. Data Cleaning Practice

46. What should be done with extra spaces in City?
47. How should inconsistent Employment Type labels be standardised?
48. How are missing Age values handled in this project?
49. How are missing Monthly Income values handled?
50. How are invalid Credit Score values handled?
51. How are missing Loan Amount values handled?
52. How are negative Loan Amount values handled?
53. How are missing Interest Rate values handled?
54. How are invalid Loan Tenure values handled?
55. How are negative Existing Loans handled?
56. How are invalid DTI values handled?
57. Why is the raw Risk Category not directly used after cleaning?
58. Why are exact duplicate rows removed?

---

# 7. Data Validation Tasks

59. Check whether any Credit Score is below 300.
60. Check whether any Credit Score is above 850.
61. Check whether any Loan Amount is negative.
62. Check whether any Interest Rate is invalid.
63. Check whether any Loan Tenure is zero or negative.
64. Check whether any Existing Loans value is negative.
65. Check whether any DTI is below 0%.
66. Check whether any DTI is above 100%.
67. Check whether any exact duplicate rows remain.
68. Verify that all Risk Categories belong to the expected four categories.
69. Verify that all Loan Status values are valid.

---

# 8. Credit Risk Summary Practice

70. Calculate the total number of customers.
71. Calculate the total loan amount.
72. Calculate the average Credit Score.
73. Calculate the average Monthly Income.
74. Calculate the average DTI.
75. Count High-risk customers.
76. Count Very High-risk customers.
77. Calculate the combined High/Very High-risk customer count.
78. Count Active Loans.
79. Count Defaulted Loans.
80. Calculate the Default Rate.

---

# 9. Risk Category Analysis

81. Create a summary by Risk Category.
82. Calculate customer count for each risk category.
83. Calculate total Loan Amount for each risk category.
84. Calculate average Credit Score for each risk category.
85. Calculate average Monthly Income for each risk category.
86. Calculate average DTI for each risk category.
87. Calculate Default Count by Risk Category.
88. Calculate Default Rate by Risk Category.
89. Compare loan exposure across risk categories.
90. Compare customer counts across risk categories.

---

# 10. Loan Analysis

91. Create a summary by Loan Status.
92. Calculate customer count by Loan Status.
93. Calculate total Loan Amount by Loan Status.
94. Calculate average Loan Amount by Loan Status.
95. Calculate average Interest Rate by Loan Status.
96. Calculate average Loan Tenure by Loan Status.
97. Identify the number of Defaulted records.
98. Compare loan exposure across loan statuses.

---

# 11. Customer Analysis

99. Review customer-level credit information.
100. Analyse customers by City.
101. Analyse customers by Employment Type.
102. Compare Credit Score across Employment Types.
103. Compare Monthly Income across Employment Types.
104. Compare Loan Amount across Employment Types.
105. Analyse the distribution of Risk Categories by City.
106. Analyse Loan Status by City.

---

# 12. Monthly Credit Risk Analysis

107. Create a monthly credit-risk summary.
108. Calculate customer count by month.
109. Calculate total Loan Amount by month.
110. Calculate average Credit Score by month.
111. Calculate average DTI by month.
112. Calculate High/Very High-risk customer count by month.
113. Calculate Default Count by month.
114. Create a monthly loan exposure chart.
115. Describe the pattern visible in the monthly loan exposure data.

---

# 13. KPI Practice

116. Calculate Total Customers.
117. Calculate Total Loan Exposure.
118. Calculate Average Credit Score.
119. Calculate Average Monthly Income.
120. Calculate Average DTI.
121. Calculate High/Very High Risk Rate.
122. Calculate Default Count.
123. Calculate Default Rate.
124. Calculate Active Loan Count.
125. Create a one-page KPI summary.

---

# 14. Excel Formula Practice

126. Use `SUM()` to calculate total Loan Amount.
127. Use `AVERAGE()` to calculate average Credit Score.
128. Use `AVERAGE()` to calculate average Monthly Income.
129. Use `AVERAGE()` to calculate average DTI.
130. Use `COUNTIF()` to count Defaulted loans.
131. Use `COUNTIF()` to count Active loans.
132. Use `COUNTIF()` to count High-risk customers.
133. Use `COUNTIF()` to count Very High-risk customers.
134. Use `COUNTIFS()` to count records satisfying multiple conditions.
135. Use `SUMIF()` to calculate loan exposure by Risk Category.
136. Use `SUMIFS()` to calculate loan exposure using multiple conditions.
137. Use `AVERAGEIF()` to calculate average Credit Score for a category.
138. Use `TRIM()` to remove unnecessary spaces.
139. Use `PROPER()` to standardise text labels.
140. Use `IF()` to create conditional classifications.

---

# 15. Pivot Table Practice

141. Create a Pivot Table by Risk Category.
142. Add Customer Count to the Pivot Table.
143. Add Loan Amount to the Pivot Table.
144. Add Default Count to the Pivot Table.
145. Create a Pivot Table by Loan Status.
146. Add Customer Count by Loan Status.
147. Add Loan Amount by Loan Status.
148. Add Average Credit Score by Loan Status.
149. Create a Pivot Table by City.
150. Create a Pivot Table by Employment Type.

---

# 16. Chart Practice

151. Create a column chart for Customers by Risk Category.
152. Create a bar chart for Loan Amount by Risk Category.
153. Create a line chart for Monthly Loan Exposure.
154. Add appropriate chart titles.
155. Add meaningful axis labels.
156. Check whether the chart is easy to understand.
157. Compare customer count and loan exposure using separate charts.
158. Write one observation for each chart.

---

# 17. Business Insight Practice

159. Which risk categories have the highest customer counts?
160. Which risk categories have the highest loan exposure?
161. How does average Credit Score vary across risk categories?
162. How does average DTI vary across risk categories?
163. How does average income vary across risk categories?
164. Which Loan Status has the largest loan exposure?
165. How many records are Defaulted?
166. What is the Default Rate?
167. How does loan exposure change over time?
168. What observations can be made from the monthly trend?

---

# 18. Interpretation Practice

169. Why should customer count and loan exposure be analysed separately?
170. Why should Default Count and Default Rate be viewed together?
171. Why should Credit Score and DTI be considered together in this project?
172. Why should data quality be checked before calculating KPIs?
173. Why can duplicate records affect business analysis?
174. Why is monthly analysis useful?
175. Why are Pivot Tables useful?
176. Why are charts useful for communicating business data?

---

# 19. Python Practice

177. Load the workbook using Pandas.
178. Read `Raw_Credit_Risk_Data`.
179. Inspect the first five rows.
180. Inspect the data types.
181. Check missing values.
182. Check duplicate rows.
183. Clean text columns.
184. Convert numeric columns.
185. Handle missing Age.
186. Handle invalid Credit Score.
187. Handle invalid Loan Amount.
188. Handle invalid Interest Rate.
189. Handle invalid Loan Tenure.
190. Handle negative Existing Loans.
191. Handle invalid DTI.
192. Recalculate Risk Category.
193. Group data by Risk Category.
194. Group data by Loan Status.
195. Calculate monthly loan exposure.
196. Calculate credit-risk KPIs.
197. Export cleaned data to CSV.
198. Create credit-risk charts using Matplotlib.

---

# 20. Pandas Practice

199. Use `read_excel()` to load the workbook.
200. Use `head()` to inspect records.
201. Use `info()` to inspect data types.
202. Use `isna()` to identify missing values.
203. Use `duplicated()` to identify duplicate rows.
204. Use `drop_duplicates()` to remove exact duplicates.
205. Use `to_numeric()` for numeric conversion.
206. Use `to_datetime()` for date conversion.
207. Use `groupby()` for Risk Category analysis.
208. Use `groupby()` for Loan Status analysis.
209. Use `agg()` to calculate multiple metrics.
210. Use `to_csv()` to export analysis results.

---

# 21. Mini Project

Complete the following workflow independently:

### Step 1 — Understand

Review all fields in the raw dataset.

### Step 2 — Inspect

Identify missing, invalid and duplicate records.

### Step 3 — Clean

Apply the Day 098 cleaning rules.

### Step 4 — Validate

Check whether cleaned values satisfy the validation rules.

### Step 5 — Classify

Recalculate Risk Category.

### Step 6 — Analyse

Perform:

- Risk Category Analysis
- Loan Analysis
- Customer Analysis
- Monthly Analysis

### Step 7 — KPI

Calculate the main Credit Risk KPIs.

### Step 8 — Visualise

Create:

- Customers by Risk Category
- Loan Amount by Risk Category
- Monthly Loan Exposure Trend

### Step 9 — Insights

Write at least five data-supported observations.

### Step 10 — Report

Prepare a final Credit Risk Analysis summary.

---

# 22. Challenge Questions

211. Why can a category with fewer customers still have substantial loan exposure?

212. Why should loan exposure be analysed alongside customer count?

213. Why should risk classification be based on cleaned data?

214. What problems can occur if inconsistent Risk Category labels are used directly?

215. Why is Default Rate not sufficient without Default Count?

216. How can missing financial data affect credit-risk analysis?

217. Why should negative financial values be investigated?

218. Why is validation necessary after cleaning?

219. Why should synthetic dataset results not be treated as real-world lending decisions?

220. How would you improve this educational credit-risk analysis if more historical loan-performance data were available?

---

# 23. Final Practice Checklist

## Data Understanding

- [ ] Understand all dataset fields
- [ ] Understand Risk Categories
- [ ] Understand Loan Status
- [ ] Understand Credit Score
- [ ] Understand DTI
- [ ] Understand Loan Exposure

## Data Cleaning

- [ ] Remove extra spaces
- [ ] Standardise text
- [ ] Convert dates
- [ ] Convert numeric values
- [ ] Handle missing values
- [ ] Handle invalid values
- [ ] Handle negative values
- [ ] Remove exact duplicates

## Analysis

- [ ] Credit Risk Summary
- [ ] Risk Category Analysis
- [ ] Loan Analysis
- [ ] Customer Analysis
- [ ] Monthly Credit Risk
- [ ] KPI Analysis
- [ ] Pivot Analysis

## Visualisation

- [ ] Risk Category chart
- [ ] Loan Amount chart
- [ ] Monthly Loan Exposure chart

## Python

- [ ] Pandas
- [ ] NumPy
- [ ] Matplotlib
- [ ] Groupby
- [ ] Aggregation
- [ ] CSV export

## Business Insights

- [ ] Customer distribution
- [ ] Loan exposure
- [ ] Risk distribution
- [ ] Default analysis
- [ ] Monthly trends
- [ ] Data-supported observations

---

# 🔑 Final Takeaway

**Practice the complete Credit Risk Analysis workflow:**

**Understand → Inspect → Clean → Validate → Classify → Analyse → Calculate KPIs → Visualise → Interpret**

The main goal of Day 098 is to become comfortable working with customer and loan data and converting it into structured credit-risk analysis.