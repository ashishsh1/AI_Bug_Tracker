import streamlit as st
import os
import pandas as pd
from src.engine import train_system, predict_bug
from src.database import init_db, log_bug, get_all_bugs

# 1. Page Configuration
st.set_page_config(page_title="Smart Bug Tracker", layout="wide", page_icon="🐞")

# 2. Initialize Database & AI Models
init_db()

@st.cache_resource
def load_logic():
    return train_system()

p_model, c_model = load_logic()

# --- SIDEBAR (Control Panel) ---
with st.sidebar:
    st.title("⚙️ Settings")
    st.info("AI-powered triage for Bugs/Defects/Findings")
    
    st.divider()
    
    # Export Feature
    st.subheader("Reports")
    df_history = get_all_bugs()
    if not df_history.empty:
        csv = df_history.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download CSV Report",
            data=csv,
            file_name='qa_bug_report.csv',
            mime='text/csv',
            use_container_width=True
        )
    
    st.divider()
    
    # Reset Feature
    if st.button("🗑️ Clear All Logs", type="secondary", use_container_width=True):
        if os.path.exists('data/bug_logs.db'):
            os.remove('data/bug_logs.db')
            init_db()
            st.success("Database cleared!")
            st.rerun()

# --- MAIN PAGE (Reporting & History) ---
st.title("🐞 Smart Bug Tracker")

col1, col2 = st.columns([1, 1.2])

with col1:
    st.header("Report a New Bug")
    desc = st.text_area("Bug Description:", placeholder="e.g., Reels fail to spin on iPhone 16...", height=150)
    
    if st.button("Analyze & Log Bug", type="primary", use_container_width=True):
        if desc.strip():
            # AI Analysis
            priority, component = predict_bug(desc, p_model, c_model)
            
            # Save to SQLite
            log_bug(desc, priority, component)
            
            # Display Results
            st.divider()
            st.subheader("AI Prediction")
            res_a, res_b = st.columns(2)
            with res_a:
                st.metric("Component", component)
            with res_b:
                st.metric("Priority", priority)
            
            if priority == "High":
                st.error("Action Required: High Priority Bug detected.")
        else:
            st.warning("Please enter a description.")

with col2:
    st.header("Bug History")
    if not df_history.empty:
        # Show newest bugs first
        st.dataframe(
            df_history.sort_values(by="id", ascending=False),
            use_container_width=True,
            hide_index=True,
            column_config={
                "id": "ID",
                "description": "Bug Description",
                "priority": st.column_config.TextColumn("Priority"),
                "component": "Component"
            }
        )
    else:
        st.info("No logs found. Use the left panel to report your first bug!")

# --- FOOTER INSIGHTS ---
if not df_history.empty:
    st.divider()
    st.header("📊 Triage Insights")
    chart_a, chart_b = st.columns(2)
    with chart_a:
        st.write("**Bugs by Component**")
        st.bar_chart(df_history['component'].value_counts())
    with chart_b:
        st.write("**Priority Volume**")
        st.line_chart(df_history['priority'].value_counts())