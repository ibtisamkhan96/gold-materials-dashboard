"""
Gold Materials Data Series - data pipeline.
Compiles cited, verified figures into tidy CSVs for the dashboard and carousel.

Primary sources (verified 2026-06):
- USGS Mineral Commodity Summaries 2026, "Gold" chapter (world mine production by country 2024
  and 2025, reserves, the Engelhard average price, global consumption split, central-bank and ETF
  flows via the World Gold Council).
  https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-gold.pdf
- World Gold Council for the consumption split and for the above-ground stock (~210,000 t of gold
  ever mined).

The headline story: gold is the oldest money, and it just hit a record price. The 2025 average
reached about $3,300 a troy ounce, up roughly 38% in a year, driven by central-bank buying and a
surge into gold funds. Over half of demand is now store-of-value (bars, central banks, coins)
rather than jewellery. Mining is the most diversified of any metal (the top five countries are
only 41%), and almost all the gold ever mined still exists, about 210,000 tonnes, enough to fit in
a cube about 22 metres on a side.
"""

import pandas as pd
import os

os.makedirs("data", exist_ok=True)

WORLD_MINE_T = 3_300         # USGS 2025e world gold mine production, tonnes of gold content
WORLD_RESERVES_T = 66_000    # USGS reserves
EVER_MINED_T = 210_000       # World Gold Council, all gold ever mined (above ground)

# 1) Gold mine production by country, 2025e (tonnes). USGS MCS 2026.
production = pd.DataFrame([
    ["China",          380, 11.5],
    ["Russia",         310,  9.4],
    ["Australia",      280,  8.5],
    ["Canada",         200,  6.1],
    ["United States",  160,  4.8],
    ["Ghana",          150,  4.5],
    ["Mexico",         140,  4.2],
    ["Kazakhstan",     130,  3.9],
    ["Uzbekistan",     130,  3.9],
    ["Peru",           110,  3.3],
    ["Other",        1_310, 39.7],
], columns=["country", "tonnes", "share_pct"])
production.to_csv("data/production.csv", index=False)

# 2) Gold reserves by country (tonnes). USGS MCS 2026; world ~66,000 t.
reserves = pd.DataFrame([
    ["Australia",     12_000],
    ["Russia",        12_000],
    ["South Africa",   5_000],
    ["Indonesia",      3_600],
    ["China",          3_200],
    ["Canada",         3_200],
    ["United States",  3_000],
    ["Brazil",         2_500],
    ["Kazakhstan",     2_300],
    ["Peru",           2_200],
    ["Uzbekistan",     2_200],
], columns=["country", "reserves_t"])
reserves.to_csv("data/reserves.csv", index=False)

# 3) Global gold consumption split (%, excludes ETFs). USGS / World Gold Council.
end_uses = pd.DataFrame([
    ["Jewellery",               40, "rings, chains, ornaments"],
    ["Physical bars",           24, "private investment"],
    ["Central banks",           21, "official reserves"],
    ["Coins and medals",         7, "official and imitation coins"],
    ["Electronics",              7, "connectors, chips, contacts"],
    ["Other",                    1, "dentistry, industrial"],
], columns=["use", "share_pct", "note"])
end_uses.to_csv("data/end_uses.csv", index=False)

# 4) Store of value vs jewellery vs technology (%).
store_split = pd.DataFrame([
    ["Store of value (bars, central banks, coins)", 52],
    ["Jewellery",                                   40],
    ["Technology",                                   7],
    ["Other",                                        1],
], columns=["use", "share_pct"])
store_split.to_csv("data/store_split.csv", index=False)

# 5) Stock vs flow: how little annual mining adds to the world's gold (tonnes).
stock_flow = pd.DataFrame([
    ["All gold ever mined", EVER_MINED_T],
    ["In central bank vaults", 37_000],
    ["Mined in 2025",      WORLD_MINE_T],
], columns=["pool", "tonnes"])
stock_flow.to_csv("data/stock_flow.csv", index=False)

# 6) Price history. Engelhard average gold price, USD per troy ounce. USGS MCS 2026.
price = pd.DataFrame([
    [2021, 1801],
    [2022, 1802],
    [2023, 1945],
    [2024, 2388],
    [2025, 3300],
], columns=["year", "usd_per_troy_oz"])
price.to_csv("data/price_history.csv", index=False)

# 7) How diversified mining is (% of 2025 output). USGS-derived. The opposite of concentration.
concentration = pd.DataFrame([
    ["China (top miner)", 12],
    ["Russia",             9],
    ["Top 5 producers",   41],
    ["Top 10 producers",  60],
], columns=["measure", "share_pct"])
concentration.to_csv("data/concentration.csv", index=False)

# 8) Scale comparisons (make it tangible).
GOLD_DENSITY_KG_M3 = 19_300
cube_all = (EVER_MINED_T * 1000 / GOLD_DENSITY_KG_M3) ** (1 / 3)
cube_year = (WORLD_MINE_T * 1000 / GOLD_DENSITY_KG_M3) ** (1 / 3)
scale = pd.DataFrame([
    ["All gold ever, as a cube", round(cube_all, 1), "metres on a side holds every gram ever mined"],
    ["A year of mining, as a cube", round(cube_year, 1), "metres on a side holds a whole year of gold"],
    ["Store-of-value share", 52, "percent of demand that is investment and central banks"],
    ["Price in 2025", 3300, "USD per troy ounce, a record annual average"],
    ["Price rise in 2025", 38, "percent increase in one year"],
], columns=["item", "value", "unit"])
scale.to_csv("data/scale_comparisons.csv", index=False)

print("Gold datasets written to data/:")
for f in sorted(os.listdir("data")):
    print("  -", f)
print(f"\nMine production 2025e: ~{WORLD_MINE_T:,} t  |  top 5 only ~41% (most diversified)")
print(f"Price 2025 avg ~$3,300/oz (+38%, record)  |  store of value ~52% of demand")
print(f"All gold ever mined ~{EVER_MINED_T:,} t = a cube ~{cube_all:.0f} m on a side")
print(f"A year of mining = a cube ~{cube_year:.1f} m on a side")
