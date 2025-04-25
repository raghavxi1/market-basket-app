import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="🧠 Market Basket Rules Viewer", layout="wide")

st.title("🛒 Market Basket Analysis Viewer")
st.markdown("Visualizing Apriori-generated rules from your `association_rules.csv` file.")

# Load association_rules.csv
file_path = "association_rules.csv"

# Check if file exists
if not os.path.exists(file_path):
    st.error(f"❌ File '{file_path}' not found. Please place it in the project folder.")
else:
    try:
        df = pd.read_csv(file_path)

        # Optional cleanup if needed (some R exports use weird formats)
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

        st.success("✅ File loaded successfully!")

        # Sidebar filters
        st.sidebar.header("📊 Filter Rules")
        min_support = st.sidebar.slider("Minimum Support", 0.0, 1.0, 0.01, step=0.01)
        min_confidence = st.sidebar.slider("Minimum Confidence", 0.0, 1.0, 0.5, step=0.01)
        min_lift = st.sidebar.slider("Minimum Lift", 0.0, 5.0, 1.0, step=0.1)

        # Filter the data
        filtered_df = df[
            (df['support'] >= min_support) &
            (df['confidence'] >= min_confidence) &
            (df['lift'] >= min_lift)
        ]

        # Display filtered data
        st.subheader(f"📋 Filtered Association Rules ({len(filtered_df)} rules found)")
        st.dataframe(filtered_df)

        # Show top 10 by lift
        st.subheader("🏆 Top 10 Rules by Lift")
        top_rules = filtered_df.sort_values(by="lift", ascending=False).head(10)

        # Make sure lift is numeric for chart
        if not pd.api.types.is_numeric_dtype(top_rules["lift"]):
            top_rules["lift"] = pd.to_numeric(top_rules["lift"], errors="coerce")

        st.bar_chart(top_rules.set_index(top_rules.index)["lift"])

    except Exception as e:
        st.error(f"🚨 Failed to load or process CSV: {e}")
