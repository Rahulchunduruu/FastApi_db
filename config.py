import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

class Config:
    #APP_NAME = os.getenv('APP_NAME')
    #DEBUG = os.getenv('DEBUG', 'False') == 'True'
    #DATABASE_URL = os.getenv('DATABASE_URL')
    #API_KEY = os.getenv('API_KEY')
    #EXTERNAL_API_URL = os.getenv('EXTERNAL_API_URL')
    DATABASE_URL=st.secrets("DATABASE_URL")
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL not found in .env file. Please add your database URL.")
    API_KEY=st.secrets("API_KEY")
    if not API_KEY:
        raise ValueError("API_KEY not found in .env file. Please add your API key.")
    EXTERNAL_API_URL=st.secrets("EXTERNAL_API_URL")
    if not EXTERNAL_API_URL:
        raise ValueError("EXTERNAL_API_URL not found in .env file. Please add your API URL.")
