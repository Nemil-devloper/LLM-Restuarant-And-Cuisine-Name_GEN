import streamlit as st
from langchain_helper import *

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine",("Indian","Italian","Mexican","French","Araibic","Japanese","American","Thai"))

# def generator_reresturant_name_and_items(cuisine):
#     return{
#         'restaurant_name':'Curry Delight',
#         'menu_items':'samosa,panner tikka',
#     }

if cuisine:
    response = generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-",item)
