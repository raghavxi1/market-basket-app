# 🧠 Market Basket Analysis Viewer

Welcome to the **Market Basket Analysis Viewer**, a web-based tool that allows you to visualize and explore association rules generated from transaction data using the Apriori algorithm.

## 📦 Project Overview

This app enables users to:

🔍 Upload or generate association rules from transactional data
📊 Filter the rules based on Support, Confidence, and Lift
📈 View the top rules by Lift in a dynamic bar chart
🧾 Understand customer purchasing behavior through rule mining

---

## 🛠️ Features

🧮 Uses the Apriori algorithm to identify frequent itemsets and generate association rules
📂 Automatically reads from a generated `association_rules.csv` file
🎛️ Real-time filtering with interactive Streamlit sidebar
📊 Visualizes rules and highlights top-performing ones by lift

---

## 📁 Project Structure

```
market-basket-app/
├── app.py                    # Streamlit front-end
├── generate_rules.py         # Script to generate association_rules.csv
├── association_rules.csv     # Output file with generated rules
├── requirements.txt          # Python dependencies
├── .streamlit/
│   └── config.toml           # Streamlit UI theming
└── README.md                 # Project documentation
```

---

## 🚀 Getting Started

1. Clone this repository and navigate to the project folder:

   ```
   git clone https://github.com/your-username/market-basket-app.git
   cd market-basket-app
   ```

2. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

3. Generate the association rules:

   ```
   python generate_rules.py
   ```

4. Launch the Streamlit app:

   ```
   streamlit run app.py
   ```

---

## 📂 Data Format

The app expects a file named `association_rules.csv` generated using `generate_rules.py`. It must include columns like:

* `antecedents`
* `consequents`
* `support`
* `confidence`
* `lift`

Make sure your transaction data in `generate_rules.py` is varied and sufficient for rule generation.

---

## 🎨 Customization

You can update the UI theme in `.streamlit/config.toml`. For example:

```
[theme]
primaryColor = "#6C63FF"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F5F6FA"
textColor = "#262730"
font = "sans serif"
```

---

## 📌 Dependencies

* Streamlit
* pandas
* mlxtend

All dependencies are listed in `requirements.txt`.

---

## 🤝 Contribution

Pull requests and suggestions are welcome. Feel free to fork the project and submit improvements or bug fixes!

---

## 📧 Contact

For questions, reach out to:
raghavsid2005@gmail.com
## View My Project at StreamLit
http://localhost:8501 
