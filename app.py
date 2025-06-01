import streamlit as st
import pandas as pd
from datetime import datetime

# --- הגדרות ראשוניות ---
st.set_page_config(page_title="ברית זהב", layout="centered", page_icon="💼")
st.markdown("""
    <style>
        body, html, [class*="css"] {
            direction: rtl;
            font-family: "Alef", sans-serif;
        }
        .title {
            color: gold;
            font-size: 40px;
            text-align: center;
            margin-bottom: 20px;
        }
        .stDataFrame thead tr th {
            background-color: black;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# --- כותרת ---
st.markdown('<div class="title">ברית זהב - טבלת מחירי מטבעות</div>', unsafe_allow_html=True)

# --- קלט משתמש ---
price_per_gram = st.number_input("הכנס את מחיר הזהב לגרם בשקלים (ש"ח):", min_value=0.0, value=300.0, step=1.0)
markup_percent = st.slider("הכנס את אחוז הרווח לסוחר:", 0, 100, 10)

# --- חישוב מטבעות ---
weights = [1, 2, 4, 8, 16, 20, 31.1]
data = []

for w in weights:
    market_price = round(w * price_per_gram, 2)
    final_price = round(market_price * (1 + markup_percent / 100), 2)
    diff = final_price - market_price
    color = "red" if diff > 0 else ("blue" if diff < 0 else "black")
    data.append({
        "משקל (גרם)": w,
        "מחיר שוק": market_price,
        "מחיר סופי": final_price,
        "הפרש": f"{diff:.2f}",
        "צבע": color
    })

# --- הצגת טבלה ---
df = pd.DataFrame(data)

# צביעת תאים לפי ערך
def style_row(row):
    color = row["צבע"]
    return ["color: red" if color == "red" else "color: blue" if color == "blue" else "" for _ in row]

styled_df = df.drop("צבע", axis=1).style.apply(style_row, axis=1)
st.dataframe(styled_df, use_container_width=True)

# --- חותמת זמן ---
st.caption(f"עודכן בתאריך: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
