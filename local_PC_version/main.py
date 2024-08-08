import streamlit as st
import os
import tiktoken
import openai
# import tempfile
# import whisper
import pytube
import re
# import pinecone


from openai import OpenAI
from dotenv import load_dotenv
from tiktoken import encoding_for_model
from langchain_openai.chat_models import ChatOpenAI
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
# from langchain_pinecone import PineconeVectorStore
# from pinecone import Pinecone, ServerlessSpec



################################
# Secretos
################################

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
print("'Secretos' cargados correctamente")



################################
# Vídeo de prueba
################################

YOUTUBE_VIDEO_URL = "https://www.youtube.com/watch?v=dgZaIk3iFhc" # Clase MEP de IDESIE
# YOUTUBE_VIDEO_URL = "https://www.youtube.com/watch?v=ROax8vdhuEQ"

LOGO_URL_LARGE = "logo.png"






################################
# Vector store
################################





###############################################################################
# Construimos la página web
###############################################################################


# Logo
st.logo(
    LOGO_URL_LARGE,
    link="https://idesie.com"
)

# Pestañas
pages = {
    "Inteligencia IDESIE": [
        st.Page("inicio.py", title="Inicio"),
        st.Page("ia.py", title="Accede a nuestra IA"),
        st.Page("repositorio.py", title="Repositorio de clases"),
        st.Page("acerca_de.py", title="Acerca de"),
    ],
}

pg = st.navigation(pages)
pg.run()


