#!/usr/bin/env python3

# SCRIPT NAME - GUI
# 2026 (c) YOUR NAME
# https://github.com/username/
# your.mail@mail.com

## disable unused variable checks for streamlit variables

# ruff: noqa: F841

"""
#####################################################
##                                                 ##
##            -- STREAMLIT MAIN APP --             ##
##                                                 ##
#####################################################
"""

import os
from tempfile import NamedTemporaryFile

import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile
from main import Character, character_factory, battle


@st.cache_data
def read_characters(
    uploaded_file: UploadedFile,
) -> list[Character]:
    r"""
    Reads an uploaded character file.
    """
    with NamedTemporaryFile(
        suffix=os.path.splitext(uploaded_file.name)[1], delete_on_close=False
    ) as f:
        f.write(uploaded_file.getbuffer())
        f.close()
        return character_factory(f.name)


# main page content
def main_page():
    r"""
    The Streamlit main page.
    """
    title = st.title("TITLE")

    general_description = """
    DESCRIPTION
    """
    description = st.markdown(general_description)

    header_1 = st.subheader("Battle Simulator", divider="rainbow")

    uploaded_file = st.file_uploader(
        "Upload a Character file:",
        type=["csv"],
        accept_multiple_files=False,
        key="uploaded_file",
        help="Upload a csv file containing character information of at least two characters.",
    )

    health = st.number_input(
        "Character health:",
        min_value=1.0,
        max_value=10000.0,
        value=130.0,
        step=1.0,
        help="How many hit points the characters have.",
    )

    if "astarion" not in st.session_state:
        st.session_state["astarion"] = 0
    if "shadowheart" not in st.session_state:
        st.session_state["shadowheart"] = 0

    total_wins = st.markdown(
        f"Astarion won a total of {st.session_state['astarion']} times and Shadowheart won a total of {st.session_state['shadowheart']} times!"
    )

    l1, l2, center, r1, r2 = st.columns(5)

    with center:
        compute = st.button("Battle!", type="secondary", width="stretch")

    if compute:
        if uploaded_file is not None:
            characters = read_characters(uploaded_file)
            if len(characters) < 2:
                st.error("You need to upload a file with at least two characters!")
            else:
                winner = battle(characters[0], characters[1], health=float(health))
                if winner.name == "Astarion":
                    st.session_state["astarion"] += 1
                    st.success("Astarion won the battle!")
                    with center:
                        st.image(
                            "https://bg3.wiki/w/images/3/3c/Astarion.png",
                            caption="(c) Larian Studios",
                            width="stretch",
                        )
                if winner.name == "Shadowheart":
                    st.session_state["shadowheart"] += 1
                    st.success("Shadowheart won the battle!")
                    with center:
                        st.image(
                            "https://bg3.wiki/w/images/f/f9/Shadowheart.png",
                            caption="(c) Larian Studios",
                            width="stretch",
                        )
        else:
            st.error("You need to upload a file with at least two characters!")


# side bar and main page loader
def main():
    r"""
    Streamlit app main function.
    """
    about_str = """
    ABOUT
    """

    st.set_page_config(
        page_title="TITLE",
        page_icon=":test_tube:",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            "Get Help": "https://github.com/YOUR_REPO/discussions",
            "Report a bug": "https://github.com/YOUR_REPO/issues",
            "About": about_str,
        },
    )

    title = st.sidebar.title("TITLE")

    logo = st.sidebar.image(
        "https://baldursgate3.game/png/logo-bg3.png",
        caption="(c) Larian Studios",
    )

    doc = st.sidebar.markdown(about_str)

    citing_str = "**Citing:**\n- CITATION INFO"
    citing = st.sidebar.markdown(citing_str)

    contact_str = "**Contact:**\n- CONTACT INFO"
    contact = st.sidebar.markdown(contact_str)

    project_license_str = "**License:**\n- [MIT License](https://github.com/YOUR_REPO/blob/master/LICENSE.md)"
    project_license = st.sidebar.markdown(project_license_str)

    project_str = "**Project Page:**\n- [GitHub](https://github.com/YOUR_REPO/)"
    project = st.sidebar.markdown(project_str)

    main_page()


if __name__ == "__main__":
    main()
