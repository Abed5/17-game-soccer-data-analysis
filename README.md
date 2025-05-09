# Analysis of 17-Game Soccer Pool Outcomes

This Python project analyzes historical soccer pool (jackpot) outcomes from the website [soccerplatform.me](https://soccerplatform.me). It specifically focuses on evaluating the predictive performance and statistical distribution of results for 17-game soccer betting pools spanning from 2016 to 2022.

The analysis includes parsing historical data, transforming raw match outcomes into numerical insights, and visualizing patterns across hundreds of jackpots.

## 📁 Project Structure

* **`data_download.py`** – Downloads and parses historical jackpot tables from web pages.
* **`data_analysis.py`** – Processes and analyzes downloaded results, providing statistical summaries and visualizations.
* **`soccerplatform-mega-jackpot-history-2016-2022.txt`** – A plain text file containing URLs to pages with jackpot outcome tables (provided by the user).

---

## 📌 Features

### Data Download

* Extracts HTML tables from URLs listed in a `.txt` file.
* Retrieves game results and predictions from each jackpot web page.

### Data Analysis

* Parses raw scorelines (e.g., "1-0") and converts them into categorical outcomes:

  * `'1'` → Home win
  * `'2'` → Away win
  * `'X'` → Draw
* Computes:

  * Frequency distribution of correct predictions.
  * Statistical summaries (mean, median, mode) for each outcome type.
  * Distribution of common outcome ratios per jackpot (e.g., 6:6:5 of 1:2\:X).
* Plots the number of correct predictions per jackpot for visual inspection.

---

## 📊 Sample Output

**From analysis of 186 jackpots (total 3,162 games):**

* **Correct Prediction Distribution (out of 17):**

  ```
  3: 1, 4: 6, 5: 13, 6: 14, 7: 37, 8: 34, 9: 27, 10: 22, 11: 19, 12: 8, 13: 3, 14: 2
  ```

* **Total Outcomes:**

  * Outcome '1': 1,135 times (35.9%)
  * Outcome '2': 1,110 times (35.1%)
  * Outcome 'X':   917 times (29.0%)

* **Average outcomes per jackpot (out of 17 games):**

  * Outcome '1': 6.1/17
  * Outcome '2': 5.9/17
  * Outcome 'X': 4.9/17

* **Standard Deviation of Correct Predictions:** `2.17`

* **Most Common 1:2\:X Ratios (per 17-game jackpot):**

  * 11 jackpots had ratio 6:6:5
  * 9 jackpots had ratios 7:5:5, 8:5:4, 7:6:4
  * ... (continued in full analysis)

---

## 🔧 Requirements

* Python 3.x
* Packages:

  * `requests`
  * `beautifulsoup4`
  * `matplotlib`
  * `scipy`
  * `numpy`
  * `IPython` (for clear output)

Install all dependencies using:

```bash
pip install -r requirements.txt
```

*(You may create `requirements.txt` by listing the above packages.)*

---

## 🚀 How to Run

1. Place the `soccerplatform-mega-jackpot-history-2016-2022.txt` file in your project directory.
2. Run `data_download.py` to download and store parsed data.
3. Save the data (e.g., in a `shelve` file or pickle format).
4. Run `data_analysis.py` to analyze and visualize the data.

---

## 🧠 Insights

This project helps uncover statistical regularities in soccer betting pools. By analyzing past jackpot outcomes, one can investigate:

* The likelihood of each outcome type.
* How often jackpots contain evenly distributed outcomes.
* Predictive performance metrics of historical forecasts.
* The overall ratio and modal frequency of the 1:2:X ratios

---

## 📌 Disclaimer

This project is for educational and analytical purposes only. It does not offer betting advice or guarantees regarding future outcomes.

---

