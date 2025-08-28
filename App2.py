# ------------------------------
# Display Plot and Capture Multi-Click
# ------------------------------
st.subheader("Merchant Growth Chart")
selected_points = plotly_events(fig, click_event=True, hover_event=False, select_event=False, override_height=500)
clicked_merchants = [pt['x'] for pt in selected_points] if selected_points else []

# ------------------------------
# Advanced Table with Conditional Formatting & Multi-Click Highlight
# ------------------------------
st.subheader("Merchant Summary Table")
display_df = df_plot[['merchant_id','avg_MoM_txn','avg_QoQ_txn','avg_YoY_txn','CAGR_num']].copy()
for col in ['avg_MoM_txn','avg_QoQ_txn','avg_YoY_txn','CAGR_num']:
    display_df[col] = display_df[col].map(lambda x: f"{x:.2f}%" if pd.notnull(x) else "")

def color_top_bottom(val):
    if val == "":
        return ""
    num = float(val.strip('%'))
    if num > 0: return 'color: green'
    elif num < 0: return 'color: red'
    else: return ''

def highlight_click(merchant_id):
    if merchant_id in clicked_merchants:
        return 'background-color: yellow; font-weight: bold'
    return ''

def style_table(row):
    styles = []
    for col in display_df.columns:
        if col != 'merchant_id':
            styles.append(color_top_bottom(row[col]))
        else:
            styles.append(highlight_click(row['merchant_id']))
    return styles

st.dataframe(display_df.style.apply(style_table, axis=1), use_container_width=True)
