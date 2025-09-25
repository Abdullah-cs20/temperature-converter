import streamlit as st

def c_to_f(c):
    return c * 9/5 + 32
def c_to_k(c):
    return c + 273.15

def f_to_c(f):
    return (f - 32) * 5/9
def f_to_k(f):
    return (f - 32) * 5/9 + 273.15

def k_to_c(k):
    return k - 273.15
def k_to_f(k):
    return (k - 273.15) * 9/5 + 32


CONVERTERS = {
    ("Celsius", "Fahrenheit"): c_to_f,
    ("Celsius", "Kelvin"): c_to_k,

    ("Fahrenheit", "Celsius"): f_to_c,
    ("Fahrenheit", "Kelvin"): f_to_k,

    ("Kelvin", "Celsius"): k_to_c,
    ("Kelvin", "Fahrenheit"): k_to_f,
}

UNIT_SYMBOL = {
    "Celsius": "°C",
    "Fahrenheit": "°F",
    "Kelvin": "K"
}

st.title("🌡️ Temperature Converter")
st.write("Convert temperature values between Celsius, Fahrenheit and Kelvin.")

with st.form("converter_form"):
    col1, col2 = st.columns([1, 1])
    with col1:
        from_unit = st.selectbox("From unit", ["Celsius", "Fahrenheit", "Kelvin"])
        input_value = st.text_input("Enter temperature", value="0")
    with col2:
        to_unit = st.selectbox("To unit", ["Celsius", "Fahrenheit", "Kelvin"], index=1)

    submitted = st.form_submit_button("Convert")


def parse_number(s):
    try:
        return float(str(s).replace(",", "").strip())
    except ValueError:
        return None


if submitted:
    x = parse_number(input_value)
    if x is None:
        st.error("Please enter a valid number (e.g. 36.6 or -40).")
    else:
        if from_unit == to_unit:
            result = x
        else:
            func = CONVERTERS.get((from_unit, to_unit))
            if not func:
                st.error("Conversion not supported.")
                st.stop()
            result = func(x)

        def fmt(val):
            s = f"{val:.6f}".rstrip("0").rstrip(".")
            return s

        st.success(f"{fmt(x)} {UNIT_SYMBOL[from_unit]}  →  {fmt(result)} {UNIT_SYMBOL[to_unit]}")
