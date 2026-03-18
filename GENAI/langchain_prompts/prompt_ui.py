import streamlit as st
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.prompts import load_prompt
# Load env variables
load_dotenv()

# Initialize model
model = ChatGoogleGenerativeAI()

st.header("Research Tool")
#static prompt
#user_input = st.text_input("Enter your query about a research paper:")

# dynamic prompts
paper_input = st.selectbox(
    "Select research paper name",
    [
        "Select...",
        "Attention is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs",
        "AlphaFold"
    ]
)

style_input = st.selectbox(
    "Select explanation style",
    ["Beginner-Friendly", "Technical", "Core-oriented", "Mathematical", "Visual"]
)

length_input = st.selectbox(
    "Select explanation length",
    ["Short", "Medium", "Long"]
)

# Prompt template
template = load_prompt('research_summary_template.json')

# Button
if st.button("Generate Explanation"):
    chain = model | template
    prompt = chain.invoke({ "paper": paper_input, "style": style_input, "length": length_input 
        })
    st.subheader("Generated Explanation:")
    st.write(result.content)