# Gold, Materials Data Series #18

An interactive data dashboard and LinkedIn carousel on the oldest money, at a record price. In 2025 gold reached a record average near $3,300 a troy ounce, up about 38% in a year, driven by central banks and investors rather than jewellers. Over half of demand is now store-of-value, mining is the most diversified of any metal, and almost every gram ever mined still exists.

Part of my Materials Data Series, where I take one material at a time and tell it as a materials engineer who works in data. This is the eighteenth: steel, aluminium, copper, rare earths, lithium, nickel, cobalt, titanium, graphite, silicon, silver, tin, magnesium, tungsten, manganese, zinc and uranium came first.

**Live dashboard:** _(deploy `index.html` to Netlify/GitHub Pages)_

---

## What's inside

| File | What it is |
|------|-----------|
| `index.html` | Interactive Chart.js dashboard, 5 tabs: Production & Geography (with a highlighted world map), All the Gold Ever, Where It Goes, Price & Demand, Why It Matters |
| `fetch_data.py` | Reproducible Python pipeline that compiles the cited figures into `data/*.csv` |
| `data/*.csv` | Tidy datasets (production, reserves, consumption split, store-of-value split, stock vs flow, price history, mining diversification, scale anchors) |
| `carousel/index.html` | 9-slide LinkedIn carousel (1080x1080) |
| `Gold_Materials_Carousel.pdf` | Exported carousel, ready to upload |
| `linkedin-post.txt` | Post caption, with the LinkedIn document title and GitHub slug at the top |

## Reproduce the data

```bash
python fetch_data.py      # writes data/*.csv
```

The dashboard embeds the same numbers in JS so it runs from `file://` with no server.

## What the data shows

- The world mined about **3,300 tonnes of gold in 2025**, a tiny annual flow. Mining is the **most diversified of any metal**: China leads at only about **12%**, the top five just **41%**, the top ten about 60%. No country controls it.
- The **2025 average price** reached a record near **$3,300 a troy ounce**, up about **38%** in a year (on top of a record 2024), with spot prices running higher still.
- More than half of demand is **store-of-value**: physical bars (24%), central banks (21%) and coins (7%) total about 52%, jewellery is about 40%, and only about **7%** is **electronics**. Gold mostly holds value rather than doing work.
- Almost every gram ever mined still exists, about **210,000 tonnes**, which would fit in a cube only about **22 metres** on a side. Annual mining adds only about **1.6%** to that stock, so the price is set by demand for safety, not by tonnage.
- The 2025 rally was driven by **central banks** (diversifying away from the dollar) and **investors** (gold-fund holdings up more than 25 fold versus a year earlier), while high prices cut jewellery buying about 20%.

## Sources

USGS Mineral Commodity Summaries 2026, the Gold chapter (world mine production by country for 2024 and 2025, reserves, the Engelhard average price, global consumption split, central-bank and ETF flows via the World Gold Council). Above-ground stock (~210,000 t of gold ever mined) and central-bank holdings from the World Gold Council.

Production and reserves in tonnes of gold content. The consumption split excludes exchange-traded funds. Prices are the Engelhard annual average in USD per troy ounce; the 2025 figure is a USGS estimate from January to November. The stock-versus-flow chart and the cube comparisons use standard gold density (19.3 g/cm³). Figures rounded and attributed.

---

*Built by Ibtisam Ahmed Khan · June 2026 · [linkedin.com/in/ibtisam-ahmed-khan](https://linkedin.com/in/ibtisam-ahmed-khan)*
