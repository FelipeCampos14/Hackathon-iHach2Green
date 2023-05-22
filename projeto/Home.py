import streamlit as st
from PIL import Image

st.title("Hydro Capital")
# Logo
logo = "projeto/img/logo2.png"
st.image(logo)

# Add logo to the sidebar
logo_path = "projeto/img/logo2.png"
st.sidebar.image(logo_path, width=280)

# Description section
st.header("Descrição")
st.write("Bem-vindo à Hydro Capital! Somos uma equipe de profissionais dedicados ao avanço da energia sustentável, especialmente no campo do hidrogênio verde. Nossa missão é fornecer informações valiosas, análises e orientações financeiras para investimentos em projetos de hidrogênio verde. Seja você um investidor individual, uma empresa ou uma instituição financeira, a Hydro Capital é sua fonte de referência para compreender o potencial e a lucratividade das empreitadas de hidrogênio verde.")

# Team section
st.header("Team")

# Team member 1
st.subheader("Celine de Souza")
Celine = "projeto/img/Celine.jpeg"
st.image(Celine, width=200)
st.write("Responsável por UX e design, o modelo de negócios, a roterização do pitch, a locutora e criação do vídeo")

# Team member 2
st.subheader("Felipe Campos")
Felipe = "projeto/img/Felipe.jpeg"
st.image(Felipe, width=200)
st.write("Responsável por Desenvolvimento Web e implementação de aplicação em python")

# Team member 3
st.subheader("Vinicius ")
Vinicius = "projeto/img/Vinicius.jpeg"
st.image(Vinicius, width=200)
st.write("Responsável pelo Benchmark e desenvolvimento do algoritmo preditivo")

# Team member 4
st.subheader("Vivian Shibata")
Vivian = "projeto/img/Vivian.jpeg"
st.image(Vivian, width=200)
st.write("Responsável por UX e design, o modelo de negócios, a roterização do pitch e da apresentação.")

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
        .css-1v0mbdj{
            align-self: flex-end;
        }
        .css-e3xfei{
            align-self: flex-end;
        }
    </style>
    """,
    unsafe_allow_html=True
)