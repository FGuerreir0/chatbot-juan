from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from fastapi import HTTPException
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import JSONLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.llms import Ollama
from globals import llm, retriever
import logging

logger = logging.getLogger("JUAN:API")

def start_rag(file, schema):
    loader = JSONLoader(
        file_path = file,
        jq_schema = schema,
        text_content=False)
    documents = loader.load()

    #1 split data into chunks
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=7500, chunk_overlap=100)
    doc_splits = text_splitter.split_documents(documents)

    #2 convert documents to embeddings and store them
    vectorstore = Chroma.from_documents(
        documents = doc_splits, 
        collection_name = "rag-chroma",
        embedding = OllamaEmbeddings(model='nomic-embed-text', base_url="http://host.docker.internal:11434"))
    retriever = vectorstore.as_retriever()
    return retriever

def get_request(chain, instructions, context):
    try:
        article = chain.invoke({
            "instructions" : instructions, 
            "context": context
        })
        return article
    except Exception as e:
        return f"An error occurred during translation: {str(e)}"

def juan_profile_responds(userInput: str, isProfile: bool) -> str:
    """
    Function to handle the user's input, use Langchain RAG and return a response.
    :param userInput: The question or input from the user.
    :return: The generated response from the chatbot.
    """
    try:
        if isProfile:
            #template="You are Juan, a friendly orange and white cat chatbot. If the question is about your human, Fabio, respond directly using the provided {context}, which contains accurate and relevant information about him. Do not include introductory phrases or ask the user questions."
            #template="You are Juan, a friendly orange and white cat chatbot. Do not include introductory phrases. If user asks about you responds as Juan and how to be a cute cat. If ask about your human respond directly and concisely based on the provided {context}. This context contains information about your human, Fabio. Your job is to answer user questions and share relevant and accurate details about Fabio in a natural, informative tone when asked.Don't do questions."
            template="You are Juan, a friendly orange and white cat chatbot. Do not include introductory phrases about yout, be direct on answer. Respond directly and concisely based on the provided {context}. This context contains information about you(chatbot) and your human, Fabio. Your job is to answer user questions and share relevant and accurate details in a natural, informative tone when asked. Important to not include questions on your answer."
        else:
            template="You are Juan, a friendly and funny orange-white cat chatbot."
        
        prompt = PromptTemplate(template=template)
        
        chain = prompt | llm | StrOutputParser()
        
        context = retriever.invoke(userInput)
        response = get_request(chain, userInput, context)

        logger.info(f"Juan's response: {response}")
        return response
    
    except Exception as e:
        logger.error(f"Error in generating response: {e}")
        raise HTTPException(status_code=500, detail="Error in generating chatbot response.")
   
def Start_LLM():
    """
    Function to start the LLM with the specified model and base URL.
    :return: The initialized LLM and context.
    """
    try:
        global llm, retriever
        llm = Ollama(model="llama3.1", base_url="http://host.docker.internal:11434", verbose=True)
        retriever = start_rag("./rag/info.json", ".chatbot, .human")
        return
    except Exception as e:
        logger.error(f"Error starting LLM: {e}")
        raise e