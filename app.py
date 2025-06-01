import streamlit as st

st.set_page_config(page_title="ברית זהב - Gold Alliance", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: gold;'>ברית זהב</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align: center; color: white;'>מסחר במטבעות זהב לפי משקל</h3>",
    unsafe_allow_html=True
)

price_per_gram = st.number_input('הכנס את מחיר הזהב לגרם בשקלים ("ש"ח):', min_value=0.0, value=300.0, step=1.0)

coin_weights = [1, 2, 3.5, 5, 7.77, 10, 15.55, 20, 31.1]  # בגרמים
dealer_markup_percent = st.slider("אחוז רווח סוחר:", 0.0, 25.0, 5.0)

st.markdown("---")
st.markdown("### מחירי מטבעות:")

for weight in coin_weights:
    base_price = weight * price_per_gram
    dealer_price = base_price * (1 + dealer_markup_percent / 100)

    color = "white"
    if dealer_price > base_price:
        color = "red"
    elif dealer_price < base_price:
        color = "blue"

    st.markdown(
        f"<div style='color:{color}; direction:rtl;'>משקל: {weight} גרם | מחיר בסיס: {base_price:,.2f} ₪ | מחיר סופי: {dealer_price:,.2f} ₪</div>",
        unsafe_allow_html=True
    )
