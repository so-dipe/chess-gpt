import streamlit as st
from inference import generate_next_move

st.title("Chess Move Generator")

previous_moves = st.text_area("Enter previous chess moves (e.g., d4 d5 ...):")

if st.button("Generate Next Move"):
    if previous_moves:
        next_move = generate_next_move(previous_moves)
        st.success(f"Next move: {next_move}")
    else:
        st.warning("Please input a move.")
