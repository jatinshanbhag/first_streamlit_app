import streamlit
streamlit.title("My Parents New Healthy Dinner")


streamlit.header("Breakfast Menu")
streamlit.text("🥣 🥗 🐔 🥑🍞")
streamlit.text("Bread and Egg")
streamlit.text("Sausages")



streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')




import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dateframe(my_fruit_list)
