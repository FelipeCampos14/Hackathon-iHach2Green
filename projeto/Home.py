import streamlit as st
from PIL import Image

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Hydro Capital")
# Logo
image = Image.open('img\logo.png')
st.image(image, width=200)

# Description section
st.header("Description")
st.write("Bem-vindo à Hydro Capital! Somos uma equipe de profissionais dedicados ao avanço da energia sustentável, especialmente no campo do hidrogênio verde. Nossa missão é fornecer informações valiosas, análises e orientações financeiras para investimentos em projetos de hidrogênio verde. Seja você um investidor individual, uma empresa ou uma instituição financeira, a Hydro Capital é sua fonte de referência para compreender o potencial e a lucratividade das empreitadas de hidrogênio verde.")

# Team section
st.header("Team")

# Team member 1
st.subheader("Celine de Souza")
team_member1_image = Image.open('img\Celine.jpeg')
st.image(team_member1_image, width=200)
st.write("John Doe is a seasoned energy analyst with a deep understanding of the green hydrogen market. With his expertise in financial modeling and market research, John brings valuable insights to our team.")

# Team member 2
st.subheader("Felipe Campos")
team_member2_image = Image.open('img\Felipe.jpeg')
st.image(team_member2_image, width=200)
st.write("Jane Smith is an experienced renewable energy engineer with a passion for sustainable technologies. Her technical expertise and project management skills make her an invaluable asset to our team.")

# Team member 3
st.subheader("Vinicius ")
team_member3_image = Image.open('img\Vinicius.jpeg')
st.image(team_member3_image, width=200)
st.write("Michael Johnson is a financial analyst with a strong background in investment strategies. His knowledge of the green energy sector and financial markets adds a unique perspective to our team.")

# Team member 4
st.subheader("Emily Wilson")
team_member4_image = Image.open('img\Vivian.jpeg')
st.image(team_member4_image, width=200)
st.write("Emily Wilson is a communications specialist with expertise in content creation and marketing. Her skills in storytelling and branding help us effectively convey our message to a wide audience.")
