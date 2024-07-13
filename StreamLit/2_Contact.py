import streamlit as st
import webbrowser


st.title("CONTACT")



col1,col2,col3=st.columns(3)
with col1:
    st.image(r'Pages\Chaitanya.jpeg')
    st.markdown("Chaitanya Jagtap")
    linkedin = 'https://www.linkedin.com/in/chaitanya-jagtap-0699b5222'
    github='https://github.com/jagtapchaitanya'
    if st.button('LinkedIn Chaitanya Jagtap '):
        webbrowser.open_new_tab(linkedin)
    if st.button('GitHub Chaitanya Jagtap'):
        webbrowser.open_new_tab(github)


with col2:
    st.image(r'Pages\Devansh1.jpeg')
    st.markdown("Devansh Singh")
    linkedin1 = 'https://www.linkedin.com/in/devansh-singh-61743b23b'
    github1='https://github.com/devaanshh'
    if st.button('LinkedIn Devansh Singh'):
        webbrowser.open_new_tab(linkedin1)
    if st.button('GitHub Devansh Singh'):
        webbrowser.open_new_tab(github1)


with col3:
    st.image(r'Pages\WhatsApp Image 2023-04-29 at 9.25.24 AM.jpeg')
    st.markdown("Kedar Hardikar")
    linkedin2 = 'https://www.linkedin.com/in/kedar-hardikar-445205202'
    github2='https://github.com/kedarhardikar'
    if st.button('LinkedIn Kedar Hardikar'):
        webbrowser.open_new_tab(linkedin2)
    if st.button('GitHub Kedar Hardikar'):
        webbrowser.open_new_tab(github2)