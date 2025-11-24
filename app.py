import streamlit as st

st.set_page_config(page_title="Sidebar Navigation", layout="wide")

# Fixed header (always visible and does not change)
st.image("Olumide Buari- Researcher.jpg", width=60)


st.markdown(
    """
    <div style="background-color:black;padding:15px;border-radius:5px;">
        <h2 style="margin:0;text-align:center;">Buari Olumide</h2>
        
    </div>
    <br>
    """,
    unsafe_allow_html=True
)

# Sidebar menu
menu = st.sidebar.radio(
    "Navigation",
    ["Introduction", "Dashboard", "Settings", "About"]
)

# Main page content
if menu == "Introduction":
    st.title("About Me")
    st.write(
        """Hello! I'm Olumide Adekunle B, a versatile professional 
        operating at the intersection of Data Science, Machine Learning, AI Agent development, Academic Research, and Natural Language Processing. My passion lies in transforming complex data into 
        actionable insights, designing intelligent systems, 
        and contributing to cutting-edge advancements in Artificial Intelligence. This comprehensive portfolio is a testament to my expertise in leveraging data-driven 
        approaches to solve real-world problems and drive innovation.
        
        """ 
        )

elif menu == "Dashboard":
    st.title("Dashboard")
    st.write("Dashboard content goes here.")

elif menu == "Settings":
    st.title("Settings")
    st.write("Settings panel content.")

elif menu == "About":
    st.title("About")
    st.write("About the app.")
