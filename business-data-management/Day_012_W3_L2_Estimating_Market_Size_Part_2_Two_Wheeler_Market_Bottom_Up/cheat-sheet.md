# ⚡ Day 012 — Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level  
**Day:** 012  
**Topic:** Estimating Market Size — Part 2 — Two-Wheeler Market (Bottom-Up)

---

## 🧮 Core Formulas

### Estimated Buyers

`= Households × Potential Buyer Rate`

---

### Market Value

`= Estimated Buyers × Average Bike Price`

---

### Loan Customers

`= Estimated Buyers × Loan Rate`

---

### Potential Loan Market

`= Loan Customers × Average Loan Amount`

---

### Total Market

`= SUM(All Segment Market Values)`

---

## 📊 Excel Functions

### SUM

`=SUM(Range)`

Adds values.

### COUNTIF

`=COUNTIF(Range,Criteria)`

Counts values matching a condition.

### AVERAGE

`=AVERAGE(Range)`

Calculates the average.

### AVERAGEIF

`=AVERAGEIF(Criteria_Range,Criteria,Average_Range)`

Calculates a conditional average.

### IFERROR

`=IFERROR(Calculation,0)`

Prevents an error from being displayed.

---

## 🔄 Bottom-Up Flow

**Segments**

↓

**Households**

↓

**Buyer Rate**

↓

**Estimated Buyers**

↓

**Average Price**

↓

**Market Value**

---

## 🏦 Loan Flow

**Estimated Buyers**

↓

**Loan Rate**

↓

**Loan Customers**

↓

**Average Loan Amount**

↓

**Potential Loan Market**

---

## 🔑 Remember

**Bottom-Up = Segment-wise estimation + aggregation**