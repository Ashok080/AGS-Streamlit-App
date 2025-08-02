import streamlit as st
import json
import os

st.set_page_config(page_title="AGS - Artificial General System", layout="wide")

st.title("🧠 AGS - Artificial General System")
st.markdown("Multimodal reasoning + memory + voice-ready AGS agent (Streamlit demo)")

# 📁 Local datasets directory
DATA_DIR = "datasets"

# 📂 List available datasets
def list_datasets():
    return [f for f in os.listdir(DATA_DIR) if f.endswith(".json")]

# 📖 Load dataset
def load_dataset(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r") as f:
        data = json.load(f)
    return data

# 🎯 Simulated reasoning output
def ags_reasoning(example):
    return f"🤖 AGS says: '{example}' likely implies logical thinking or emotional reasoning.'"

# 🕽️ Dataset selector
if not os.path.exists(DATA_DIR):
    st.error("The 'datasets' folder is missing. Please upload your datasets.")
    st.stop()

try:
    datasets = list_datasets()
except Exception as e:
    st.error(f"Error reading datasets folder: {e}")
    st.stop()

if not datasets:
    st.warning("No .json files found in the datasets folder.")
    st.stop()

selected = st.selectbox("Choose a dataset to explore:", datasets)

if selected:
    try:
        data = load_dataset(selected)
        st.success(f"Loaded `{selected}` ✅")

        # Display preview
        preview = data[:3] if isinstance(data, list) else list(data.items())[:3]
        st.json(preview)

        if isinstance(data, list) and st.button("Run AGS Reasoning on Sample"):
            st.markdown("### 🧠 AGS Reasoning Output")
            st.info(ags_reasoning(data[0]))

    except Exception as e:
        st.error(f"Failed to load dataset: {e}")
