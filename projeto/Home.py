import streamlit as st
from PIL import Image

st.markdown("<h1 style='font-weight: bold;'>Hydro Capital</h1>", unsafe_allow_html=True)

# Logo
image = Image.open('img\meu-primeiro-gato.jpg')
st.image(image, use_column_width=True)

# Description section
st.header("Description")
st.write("Welcome to Hydro Capital! We are a team of professionals dedicated to the advancement of sustainable energy, particularly in the field of green hydrogen. Our mission is to provide valuable insights, analysis, and financial guidance for investing in green hydrogen projects. Whether you are an individual investor, a company, or a financial institution, Hydro Capital is your go-to resource for understanding the potential and profitability of green hydrogen ventures.")

# Team section
st.header("Team")

# Team member 1
st.subheader("John Doe")
team_member1_image = Image.open('img\meu-primeiro-gato.jpg')
st.image(team_member1_image, use_column_width=True)
st.write("John Doe is a seasoned energy analyst with a deep understanding of the green hydrogen market. With his expertise in financial modeling and market research, John brings valuable insights to our team.")

# Team member 2
st.subheader("Jane Smith")
team_member2_image = Image.open('img\meu-primeiro-gato.jpg')
st.image(team_member2_image, use_column_width=True)
st.write("Jane Smith is an experienced renewable energy engineer with a passion for sustainable technologies. Her technical expertise and project management skills make her an invaluable asset to our team.")

# Team member 3
st.subheader("Michael Johnson")
team_member3_image = Image.open('img\meu-primeiro-gato.jpg')
st.image(team_member3_image, use_column_width=True)
st.write("Michael Johnson is a financial analyst with a strong background in investment strategies. His knowledge of the green energy sector and financial markets adds a unique perspective to our team.")

# Team member 4
st.subheader("Emily Wilson")
team_member4_image = Image.open('img\meu-primeiro-gato.jpg')
st.image(team_member4_image, use_column_width=True)
st.write("Emily Wilson is a communications specialist with expertise in content creation and marketing. Her skills in storytelling and branding help us effectively convey our message to a wide audience.")
