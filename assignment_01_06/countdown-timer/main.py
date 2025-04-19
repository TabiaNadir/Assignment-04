import streamlit as st
import time

st.title("⏳ Streamlit Countdown Timer")

# Input time in seconds
seconds = st.number_input("Enter countdown time in seconds:", min_value=1, value=10, step=1)

# Start button
if st.button("Start Timer"):
    st.write("Countdown started!")
    placeholder = st.empty()  # Placeholder to update countdown text

    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        placeholder.markdown(f"## ⏱ Time Remaining: `{timer}`")
        time.sleep(1)
        seconds -= 1

    placeholder.markdown("## ✅ Time's up!")

if __name__ == "__main__":
    st.write("Build with ❤️ by [Tabia Nadir](https://github.com/TabiaNadir)")
