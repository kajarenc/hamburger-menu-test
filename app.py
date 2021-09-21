import streamlit as st

menu_options = {
	'Get help': 'https://url.com',
	'Report a bug': 'https://url.com',
	'About': '''
	 ## My Custom App
	 This app uses our ML Model to demonstrate churn prediction.
	'''
}



st.set_page_config(menu_items=menu_options)

st.title("HELLO WORLD!")
st.write(45)
