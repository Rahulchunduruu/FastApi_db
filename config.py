import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


class Config:
    DATABASE_URL = os.getenv("DATABASE_URL") or st.secrets.get("DATABASE_URL")
    API_KEY = os.getenv("API_KEY") or st.secrets.get("API_KEY")
    EXTERNAL_API_URL = os.getenv("EXTERNAL_API_URL") or st.secrets.get("EXTERNAL_API_URL")

    if not DATABASE_URL:
        raise ValueError("DATABASE_URL not found")
    