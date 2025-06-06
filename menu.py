import streamlit as st


def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.page_link("app.py", label="Homepage")
    st.sidebar.page_link("pages/aboutme.py", label="About Me")
    st.sidebar.page_link("pages/chatbot.py", label="Pirate Chatbot")
    st.sidebar.page_link("pages/stability.py", label="Prompted Pictures")
    st.sidebar.page_link("pages/voyagergpt.py", label="VoyagerGPT")
    st.sidebar.page_link("pages/warcraft.py", label="Warcraft World")    
    st.sidebar.page_link("pages/dune.py", label="Dune Universe")
    # st.sidebar.page_link("pages/pps.py", label="Dune Movie")


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("app.py", label="Log in")


def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    authenticated_menu()


def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("app.py")
    menu()