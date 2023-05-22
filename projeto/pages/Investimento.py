import streamlit as st 
st.title("Hydro Capital")
st.header("Investimento")

# Add CSS styling to the Marketplace page
st.markdown(
    """
    <style>
        /* Add your CSS styles specific to the Marketplace page */
        .marketplace-container {
            background-color: #d5ffd3;
            padding: 1rem;
            border-radius: 0.5rem;
            color: black;
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
        .marketplace-container {
            background-color: #d5ffd3;
            padding: 1rem;
            border-radius: 0.5rem;
            color: white;
            margin-bottom: 1rem;
            height: 300px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .marketplace-container h3 {
            font-size: 25px;
            margin-top: 0;
            margin-bottom: 0.5rem;
        }
        .marketplace-container p {
            font-size: 15px;
            line-height: 0.9;
            margin-top: 0;
            margin-bottom: 0.5rem;
            color: black;
        }
        .marketplace-container button {
            border-radius: 0.5rem;
            border: 1px;
            color: white;
            background-color: #032305;
            margin: 1px;
            align-self: flex-end;
        }
        .marketplace-container button:hover {
            background-color: white;
            color: #032305;
            border: 1px solid #032305;
        }
        /* body*/
        .css-uf99v8{
            background: #fefdf4;
        }
        /* sidebar*/
        .css-1cypcdb{
            background-color:#032305;
        }
        /* Title n headers*/
        .css-10trblm{
            color: black;
        }
        /* body text*/
        .css-q8sbsg {
            color: black;
            font-size: 40px;
        }
        /* info*/
        .st-ae {
            background-color: #d5ffd3;
        }
        /* info text*/
        .css-nahz7x{
            color: black;
        }
        /* button*/
        .css-b3z5c9{
            color:white;
            background-color: #032305;
            border: #032305;
        }
        .css-b3z5c9:focus:not(:active){
            color:#032305;
            background-color: white;
            border:#032305;
        }
        .css-b3z5c9:hover{
            color:#032305;
            background-color: white;
            border:#032305;
        }
        .css-1y4p8pa{
            /* From https://css.glass */
            background: rgba(255, 255, 255, 0.3);
            border-radius: 16px;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(5px);
            -webkit-backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            color: black;
        }
    </style>
    """,
    unsafe_allow_html=True
)
if 'card_counter' not in st.session_state:
    st.session_state['card_counter'] = 0
if st.session_state['card_counter'] == 0:
    st.info("Exporte um investimento da calculadora")

card_counter = st.session_state['card_counter']

for i in range(card_counter,-1,-1):
    if f'name{i}' not in st.session_state:
        st.session_state[f'name{i}'] = None

    if f'time{i}' not in st.session_state:
        st.session_state[f'time{i}'] = None

    if f'initial_investment{i}' not in st.session_state:
        st.session_state[f'initial_investment{i}'] = None

    if f'profits{i}' not in st.session_state:
        st.session_state[f'profits{i}'] = None

    if (st.session_state[f'name{i}'] != None) and (st.session_state[f'time{i}'] != None) and (st.session_state[f'initial_investment{i}'] != None) and (st.session_state[f'profits{i}'] != None):
        st.markdown(f"<div class='marketplace-container'> <h3>{st.session_state[f'name{i}']}</h3> <p>Anos: {st.session_state[f'time{i}']}</p> <p>Investimento inicial: R$ {st.session_state[f'initial_investment{i}']}</p> <p>Lucro Previsto: R$ {st.session_state[f'profits{i}'][-1]}</p> </div>", unsafe_allow_html=True)