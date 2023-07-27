import streamlit as st

from eda_sect import eda_section
from ml_sect import ml_section
from about_sect import about_section
from prep_sect import prep_section

home_temp = """
            <div style="background-color:#0d0d0c;padding:1px;border-radius:25px">
		        <h2 style="color:white;font-family:calibri;text-align:center;">Final Project - Data Science </h2>
            </div>
"""

def main_section():

    # Display the images side by side
    col1, mid, mid, col2 = st.columns(4, gap = 'large')

    with col1:
        st.image('images/DS.png', caption="Data Science Batch 26", width=460)

    with mid:
        pass

    with mid:
        pass
        
    with col2:
        st.image('images/Unicorn.png', caption="Unicorn Team", width=120)

    st.write(home_temp,unsafe_allow_html=True)

    st.subheader("Meet Our Team")

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

    st.write("This project was created by the Unicorn Team as part of the final project for the Data Science Bootcamp at Digital Skola.")

def main():
    st.set_page_config(page_title="Data Science Bootcamp Final Project", page_icon=":chart_with_upwards_trend:")
    st.sidebar.title("Navigation")
    section = st.sidebar.radio("Go to Menu", ("Home", "About Project","Data Preprocessing & Cleansing","Exploratory Data Analysis", "Machine Learning"))

    if section == "Home":
        main_section()
    elif section == "About Project":
        about_section()
    elif section == "Data Preprocessing & Cleansing":
        prep_section()
    elif section == "Exploratory Data Analysis":
        eda_section()
    elif section == "Machine Learning":
        ml_section()


if __name__ == "__main__":
    main()
