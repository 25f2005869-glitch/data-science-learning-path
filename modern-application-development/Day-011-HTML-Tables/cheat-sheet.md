
### `cheat-sheet.md`

```markdown
# ⚡ Day 011 — HTML Tables Cheat Sheet

**Author:** Saloni Tiwari  
**Programme:** IIT Madras BS Degree — Diploma Level

---

## 📊 Main Elements

| Element | Purpose |
|---|---|
| `<table>` | Creates a table |
| `<tr>` | Creates a table row |
| `<th>` | Creates a header cell |
| `<td>` | Creates a data cell |
| `<caption>` | Gives table a title |
| `<thead>` | Groups header rows |
| `<tbody>` | Groups main data rows |
| `<tfoot>` | Groups footer rows |

---

## 🧱 Basic Table

<table>

    <tr>
        <th>Name</th>
        <th>Course</th>
    </tr>

    <tr>
        <td>Saloni</td>
        <td>MAD</td>
    </tr>

</table>

---

## 📝 Caption

<caption>Student Details</caption>

---

## 🔝 Thead

<thead>

    <tr>
        <th>Name</th>
        <th>Course</th>
    </tr>

</thead>

---

## 📦 Tbody

<tbody>

    <tr>
        <td>Saloni</td>
        <td>MAD</td>
    </tr>

</tbody>

---

## 🔚 Tfoot

<tfoot>

    <tr>
        <td>Total</td>
        <td>2 Students</td>
    </tr>

</tfoot>

---

## ➡️ Colspan

One cell covers multiple columns.

<th colspan="3">
    Student Information
</th>

---

## ↕️ Rowspan

One cell covers multiple rows.

<td rowspan="2">
    Saloni
</td>

---

## ♿ Scope

### Column Header

<th scope="col">Name</th>

### Row Header

<th scope="row">Saloni</th>

---

## 🧠 Quick Memory

<table>
    ↓
<tr> = Row
    ↓
<th> = Header
<td> = Data

---

## 📌 Table Sections

<thead> = Header

<tbody> = Body

<tfoot> = Footer

---

## 🎯 Spanning

colspan → Multiple Columns

rowspan → Multiple Rows

---

## ⭐ Important Rule

Use HTML tables for:

**Tabular Data**

Do not use tables as the main webpage layout system.