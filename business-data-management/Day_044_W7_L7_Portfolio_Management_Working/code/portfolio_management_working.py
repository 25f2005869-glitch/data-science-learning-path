from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = BASE_DIR / "Day_044_W7_L7_Portfolio_Management_Working.xlsx"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(INPUT_FILE, sheet_name="Portfolio_Data")

df["Gross_Margin"] = (
    df["Revenue"] - df["Production_Cost"]
)

df["Margin_%"] = (
    df["Gross_Margin"] / df["Revenue"]
)

portfolio = df.groupby(
    "Product",
    as_index=False
).agg(
    Production_Units=("Production_Units", "sum"),
    Sales_Units=("Sales_Units", "sum"),
    Scrap_Units=("Scrap_Units", "sum"),
    Revenue=("Revenue", "sum"),
    Production_Cost=("Production_Cost", "sum"),
    Gross_Margin=("Gross_Margin", "sum")
)

portfolio["Margin_%"] = (
    portfolio["Gross_Margin"] /
    portfolio["Revenue"]
)

portfolio["Revenue_Share_%"] = (
    portfolio["Revenue"] /
    portfolio["Revenue"].sum()
)

portfolio["Sales_Conversion_%"] = (
    portfolio["Sales_Units"] /
    portfolio["Production_Units"]
)

portfolio["Scrap_Rate_%"] = (
    portfolio["Scrap_Units"] /
    portfolio["Production_Units"]
)

portfolio["Revenue_Rank"] = (
    portfolio["Revenue"]
    .rank(ascending=False, method="min")
    .astype(int)
)

portfolio["Margin_Rank"] = (
    portfolio["Margin_%"]
    .rank(ascending=False, method="min")
    .astype(int)
)

portfolio = portfolio.sort_values(
    "Revenue",
    ascending=False
)

portfolio.to_csv(
    OUTPUT_DIR / "product_portfolio_summary.csv",
    index=False
)


def make_chart(
    values,
    title,
    ylabel,
    filename,
    color
):
    plt.figure(figsize=(8, 5))

    plt.bar(
        portfolio["Product"],
        values,
        color=color
    )

    plt.title(title)
    plt.xlabel("Product")
    plt.ylabel(ylabel)

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / filename,
        dpi=160
    )

    plt.close()


make_chart(
    portfolio["Revenue"],
    "Revenue by Product",
    "Revenue",
    "revenue_by_product.png",
    "#4472C4"
)

make_chart(
    portfolio["Gross_Margin"],
    "Gross Margin by Product",
    "Gross Margin",
    "gross_margin_by_product.png",
    "#ED7D31"
)

make_chart(
    portfolio["Revenue_Share_%"] * 100,
    "Revenue Share by Product",
    "Revenue Share (%)",
    "revenue_share_by_product.png",
    "#70AD47"
)


print("Portfolio analysis completed.")

print(
    portfolio.round(4).to_string(index=False)
)