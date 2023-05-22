import streamlit as st
st.title("Hydro Capital")
st.header("Compre H2V")
st.markdown(
    """
    <style>
        /* Add your CSS styles specific to the Marketplace page */
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

# Create three columns with equal width
col1, col2, col3 = st.columns(3)

# Column 1
with col1:
    st.markdown(f"<div class='marketplace-container'> <h3>Usina de Hidrogênio Verde Itaipu</h3> <p>Lote: ITP73</p> <p>Quantidade: 600000 MMbtu</p> <p>Preço estimado: R$ 539.400</p> <button>Entrar em contato</button></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='marketplace-container'> <h3>Parque Eólico de Pecém</h3> <p>Lote: PEP08</p> <p>Quantidade: 170000 MMbtu</p> <p>Preço estimado: R$ 152.830</p><button>Entrar em contato</button></div>", unsafe_allow_html=True)


# Column 2
with col2:
    st.markdown(f"<div class='marketplace-container'> <h3>Grãos de Hidrogênio</h3> <p>Lote: GH2R14</p> <p>Quantidade: 200000 MMbtu</p> <p>Preço estimado: R$ 179.800</p><button>Entrar em contato</button></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='marketplace-container'> <h3>Complexo Solar de Pirapora</h3> <p>Lote: CSP20</p> <p>Quantidade: 433000 MMbtu</p> <p>Preço estimado: R$ 386.570</p><button>Entrar em contato</button></div>", unsafe_allow_html=True)

# Column 3
with col3:
    st.markdown(f"<div class='marketplace-container'> <h3>H2 Sergipe</h3> <p>Lote: H2S35</p> <p>Quantidade: 370000 MMbtu</p> <p>Preço estimado: R$ 332.630</p><button>Entrar em contato</button></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='marketplace-container'> <h3>Parque Eólico de Rio do Vento</h3> <p>Lote: PEV88</p> <p>Quantidade: 120000 MMbtu</p> <p>Preço estimado: R$ 107.880</p> <button>Entrar em contato</button></div>", unsafe_allow_html=True)