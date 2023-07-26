import streamlit as st

from eda_sect import eda_section
from ml_sect import ml_section

def main_section():
     st.image("images/DS.png", caption="Data Science Batch 26", use_column_width=True)
     st.title("Home/Main Section")

     st.header("Meet Our Team")

     # Create a container to align images side by side
     col1, col2, col3, col4 = st.columns(4)

     team_members = {
          "Anindya Lokeswara": "images/Anin.jpg",
          "Tatag Suryo Pambudi": "images/Tatag.jpg",
          "Erdiah Ashida Nasirin": "images/Erdiah.jpg",
          "Andi Muhammad Yusuf": "images/Andi.jpg"
     }

     # Use the columns to align images side by side
     with col1:
          st.image(team_members["Anindya Lokeswara"], caption="Anindya Lokeswara", width=150)

     with col2:
          st.image(team_members["Tatag Suryo Pambudi"], caption="Tatag Suryo Pambudi", width=150)

     with col3:
          st.image(team_members["Erdiah Ashida Nasirin"], caption="Erdiah Ashida Nasirin", width=150)

     with col4:
          st.image(team_members["Andi Muhammad Yusuf"], caption="Andi Muhammad Yusuf", width=150)

     st.header("About the Project")
     st.write("The purpose of this project is to complete the final project of Digital Skola Data Science Bootcamp.")

     st.header("General Overview")
     st.write("Add the general overview of the topic and data source here.")


def main():
    st.set_page_config(page_title="Data Science Bootcamp Final Project", page_icon=":chart_with_upwards_trend:")
    st.sidebar.title("Navigation")
    section = st.sidebar.radio("Go to", ("Home", "Exploratory Data Analysis", "Machine Learning"))

    if section == "Home":
        main_section()
    elif section == "Exploratory Data Analysis":
        eda_section()
    elif section == "Machine Learning":
        ml_section()


if __name__ == "__main__":
    main()
