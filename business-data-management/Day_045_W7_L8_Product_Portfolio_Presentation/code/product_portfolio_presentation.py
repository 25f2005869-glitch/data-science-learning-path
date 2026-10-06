from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

CODE_DIR = Path(__file__).resolve().parent
BASE_DIR = CODE_DIR.parent

INPUT_FILE = (
    BASE_DIR
    / "Day_045_W7_L8_Product_Portfolio_Presentation.xlsx"
)

OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Portfolio_Data"
)

df["Gross_Margin"] = (
    df["Revenue"]
    - df["Production_Cost"]
)

df["Margin_%"] = (
    df["Gross_Margin"]
    / df["Revenue"]
)

portfolio = df.groupby(
    "Product",
    as_index=False
).agg(
    Production_Units=(
        "Production_Units",
        "sum"
    ),
    Sales_Units=(
        "Sales_Units",
        "sum"
    ),
    Scrap_Units=(
        "Scrap_Units",
        "sum"
    ),
    Revenue=(
        "Revenue",
        "sum"
    ),
    Production_Cost=(
        "Production_Cost",
        "sum"
    ),
    Gross_Margin=(
        "Gross_Margin",
        "sum"
    )
)

portfolio["Margin_%"] = (
    portfolio["Gross_Margin"]
    / portfolio["Revenue"]
)

portfolio["Revenue_Share_%"] = (
    portfolio["Revenue"]
    / portfolio["Revenue"].sum()
)

portfolio["Sales_Conversion_%"] = (
    portfolio["Sales_Units"]
    / portfolio["Production_Units"]
)

portfolio["Scrap_Rate_%"] = (
    portfolio["Scrap_Units"]
    / portfolio["Production_Units"]
)

portfolio = portfolio.sort_values(
    "Revenue",
    ascending=False
)

portfolio.to_csv(
    OUTPUT_DIR
    / "product_portfolio_presentation_summary.csv",
    index=False
)


def save_bar(
    values,
    title,
    ylabel,
    filename,
    color
):
    plt.figure(
        figsize=(8, 5)
    )

    plt.bar(
        portfolio["Product"],
        values,
        color=color
    )

    plt.title(title)

    plt.xlabel(
        "Product"
    )

    plt.ylabel(
        ylabel
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / filename,
        dpi=160
    )

    plt.close()


save_bar(
    portfolio["Revenue"],
    "Revenue by Product",
    "Revenue",
    "revenue_by_product.png",
    "#4472C4"
)

save_bar(
    portfolio["Gross_Margin"],
    "Gross Margin by Product",
    "Gross Margin",
    "gross_margin_by_product.png",
    "#ED7D31"
)

save_bar(
    portfolio["Revenue_Share_%"] * 100,
    "Revenue Share by Product",
    "Revenue Share (%)",
    "revenue_share_by_product.png",
    "#70AD47"
)


plt.figure(
    figsize=(8, 5)
)

x = range(
    len(portfolio)
)

plt.bar(
    [
        i - 0.2
        for i in x
    ],
    portfolio[
        "Production_Units"
    ],
    width=0.4,
    label="Production Units",
    color="#8064A2"
)

plt.bar(
    [
        i + 0.2
        for i in x
    ],
    portfolio[
        "Sales_Units"
    ],
    width=0.4,
    label="Sales Units",
    color="#5B9BD5"
)

plt.xticks(
    list(x),
    portfolio["Product"]
)

plt.title(
    "Production vs Sales by Product"
)

plt.xlabel(
    "Product"
)

plt.ylabel(
    "Units"
)

plt.legend()

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR
    / "production_vs_sales.png",
    dpi=160
)

plt.close()


print(
    "Product portfolio presentation "
    "analysis completed."
)

print(
    portfolio
    .round(4)
    .to_string(index=False)
)