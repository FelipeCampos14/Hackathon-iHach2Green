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

# Add three columns
col1, col2, col3 = st.columns(3)

# Content for column 1
with col1:
    st.markdown('<div class="marketplace-container"> <h3>Nome</h3> <p>ações</p> <p>valor</p> <p>tempo</p> <p>lucro</p> <p>ROI</p> </div>', unsafe_allow_html=True)
    st.markdown('<div class="marketplace-container"> <h3>Nome</h3> <p>ações</p> <p>valor</p> <p>tempo</p> <p>lucro</p> <p>ROI</p> </div>', unsafe_allow_html=True)


# Content for column 2
with col2:
    st.markdown('<div class="marketplace-container"> <h3>Nome</h3> <p>ações</p> <p>valor</p> <p>tempo</p> <p>lucro</p> <p>ROI</p> </div>', unsafe_allow_html=True)
    st.markdown('<div class="marketplace-container"> <h3>Nome</h3> <p>ações</p> <p>valor</p> <p>tempo</p> <p>lucro</p> <p>ROI</p> </div>', unsafe_allow_html=True)


# Content for column 3
with col3:
    st.markdown('<div class="marketplace-container"> <h3>Nome</h3> <p>ações</p> <p>valor</p> <p>tempo</p> <p>lucro</p> <p>ROI</p> </div>', unsafe_allow_html=True)
    st.markdown('<div class="marketplace-container"> <h3>Nome</h3> <p>ações</p> <p>valor</p> <p>tempo</p> <p>lucro</p> <p>ROI</p> </div>', unsafe_allow_html=True)
