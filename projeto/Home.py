import streamlit as st
from PIL import Image

st.title("Hydro Capital")
# Logo
image = Image.open('Hackathon-iHach2Green/projeto/img')
st.image(image, width=200)

# # Description section
# st.header("Description")
# st.write("Bem-vindo à Hydro Capital! Somos uma equipe de profissionais dedicados ao avanço da energia sustentável, especialmente no campo do hidrogênio verde. Nossa missão é fornecer informações valiosas, análises e orientações financeiras para investimentos em projetos de hidrogênio verde. Seja você um investidor individual, uma empresa ou uma instituição financeira, a Hydro Capital é sua fonte de referência para compreender o potencial e a lucratividade das empreitadas de hidrogênio verde.")

# # Team section
# st.header("Team")

# # Team member 1
# st.subheader("Celine de Souza")
# team_member1_image = Image.open('img/Celine.jpeg')
# st.image(team_member1_image, width=200)
# st.write("John Doe is a seasoned energy analyst with a deep understanding of the green hydrogen market. With his expertise in financial modeling and market research, John brings valuable insights to our team.")

# # Team member 2
# st.subheader("Felipe Campos")
# team_member2_image = Image.open('img/Felipe.jpeg')
# st.image(team_member2_image, width=200)
# st.write("Jane Smith is an experienced renewable energy engineer with a passion for sustainable technologies. Her technical expertise and project management skills make her an invaluable asset to our team.")

# # Team member 3
# st.subheader("Vinicius ")
# team_member3_image = Image.open('img/Vinicius.jpeg')
# st.image(team_member3_image, width=200)
# st.write("Michael Johnson is a financial analyst with a strong background in investment strategies. His knowledge of the green energy sector and financial markets adds a unique perspective to our team.")

# # Team member 4
# st.subheader("Emily Wilson")
# team_member4_image = Image.open('img/Vivian.jpeg')
# st.image(team_member4_image, width=200)
# st.write("Emily Wilson is a communications specialist with expertise in content creation and marketing. Her skills in storytelling and branding help us effectively convey our message to a wide audience.")

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