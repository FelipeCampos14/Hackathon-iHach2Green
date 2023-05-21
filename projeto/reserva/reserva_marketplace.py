import streamlit as st 

st.title("Marketplace")
# Add CSS styling to the Marketplace page
st.markdown(
    """
    <style>
        /* Add your CSS styles specific to the Marketplace page */
        .marketplace-container {
            background-color: black;
            padding: 1rem;
            border-radius: 0.5rem;
            color: white;
            margin-bottom: 1rem;
            max-width: 2 rem;
        }
        .marketplace-container h3 {
            font-size: 25px;
        }
        .marketplace-container p {
            font-size: 15px;
            line-height: 0.9;
        }
    </style>
    """,
    unsafe_allow_html=True
)
if 'card_counter' not in st.session_state:
    st.session_state['card_counter'] = 0

card_counter = st.session_state['card_counter']

for i in range(card_counter):
    if f'name{i}' not in st.session_state:
        st.session_state[f'name{i}'] = None

    if f'time{i}' not in st.session_state:
        st.session_state[f'time{i}'] = None

    if f'initial_investment{i}' not in st.session_state:
        st.session_state[f'initial_investment{i}'] = None

    if f'profits{i}' not in st.session_state:
        st.session_state[f'profits{i}'] = None

    if (st.session_state[f'name{i}'] != None) and (st.session_state[f'time{i}'] != None) and (st.session_state[f'initial_investment{i}'] != None) and (st.session_state[f'profits{i}'] != None):
        st.markdown(f"<div class='marketplace-container'> <h3>{st.session_state[f'name{i}']}</h3> <p>Anos: {st.session_state[f'time{i}']}</p> <p>Investimento inicial: R$ {st.session_state[f'initial_investment{i}']}</p> <p>Lucro: R$ {st.session_state[f'profits{i}'][-1]}</p> </div>", unsafe_allow_html=True)
