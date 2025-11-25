import streamlit as st

st.set_page_config(page_title="Sidebar Navigation", layout="wide")

# Fixed header (always visible and does not change)
st.image("Olumide_Buari-Researcher.jpg")
#st.image("**Olumide Buari- Researcher.jpg**")


st.markdown(
    """
    <div style=padding:15px;border-radius:5px;">
        <h2 style="margin:0;text-align:center;">Olumide Adekunle B.</h2>
        
    </div>
    <br>
    """,
    unsafe_allow_html=True
)

# Sidebar menu
menu = st.sidebar.radio(
    "Navigation",
    ["Introduction", "Curriculum Vitae", "Settings", "About"]
)

# Main page content
if menu == "Introduction":
    st.title("About Me")
    st.write(
        """Hello! I'm Olumide Adekunle B, a versatile professional 
        operating at the intersection of Data Science, Machine Learning, AI Agent development, Academic Research, and Natural Language Processing. My passion lies in transforming complex data into 
        actionable insights, designing intelligent systems, 
        and contributing to cutting edge advancements in Artificial Intelligence. This comprehensive portfolio is a testament to my expertise in leveraging impact meaningful
        approaches to solve real Life Practical problems and drive innovation.
        
        """ 
        )

