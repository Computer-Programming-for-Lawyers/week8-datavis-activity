## Week 8 In-Class Activity: Group B — Visualizing Toxic Release Data

*April 13, 2026*

The EPA's [Toxics Release Inventory](https://www.epa.gov/toxics-release-inventory-tri-program) tracks how much of each toxic chemical U.S. facilities release into the environment each year. This repo includes a script to download that data for 2020–2024.

### Step 1: Download the data

Run the download script first — it will fetch the TRI data files from the EPA website and extract them into `us_20XX/` folders:

```
python download_data.py
```

Each year's data will land in a folder like `us_2024/`. The file you want is `US_1a_20XX.txt`.

### Step 2: Load and explore

These are tab-separated files, not comma-separated — you'll need to tell pandas that. You'll probably also hit an error on your first load attempt. Read the error message carefully: it tells you exactly what's wrong and where. Google the error type with "pandas read_csv" to find the fix.

Once one year loads, try combining all five into a single DataFrame.

### Step 3: Find useful columns

There are 282 columns. The ones worth focusing on: year, facility name, state, chemical name, whether the chemical is a carcinogen, whether it's a PFAS compound, and total on-site release in pounds. Print `df.columns.tolist()` and `df.head()` to orient yourself — the column names are numbered and the ones you want are roughly in the middle of the list.

### Your goal

Pick any question the data can answer and make a chart that shows it. It doesn't have to be one of these — if something else about toxic releases interests you, go for it. Some starting points:

- Which states have the highest total toxic releases? Has that changed from 2020 to 2024?
- Are carcinogen releases going up or down over time?
- PFAS ("forever chemicals") reporting was expanded recently — how has reported PFAS release volume changed year over year?
- Which facilities are the largest releasers in a given state?
- Pick a specific chemical — lead compounds, mercury, arsenic — and look at where it's being released and how much.

### What to aim for

At least one labeled, titled chart that answers a specific question.

### If you finish early

Go back to the source. The `download_data.py` script does this for you — but look at what it's doing. Can you extend it to also pull data from years before 2020? Or rewrite it from scratch by scraping the download links directly off [the TRI data page](https://www.epa.gov/toxics-release-inventory-tri-program/tri-basic-plus-data-files-calendar-years-1987-present)?

### At the end of class

One person from your group shares their screen: what question did you ask, what does the chart show, and did anything surprise you?
