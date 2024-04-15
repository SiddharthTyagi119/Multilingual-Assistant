#text to text
#converting the voice input to text and pass to the model .
#and then we are generating the response in the form of mp3 

import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech


def main():
    st.title("Multilingual AI Assistant 🤖")
    
    if st.button("Ask me anything"):
        with st.spinner("Listening..."):
            text=voice_input()                 #capturimg the voice input 
            response=llm_model_object(text)    #passing text to the llm model 
            text_to_speech(response)
            
    #voice input will be required, so we have to paas in the form of voice file
            audio_file=open("speech.mp3","rb")
            audio_bytes=audio_file.read()   #reading audio file
            
            
            st.text_area(label="Response:",value=response,height=350)
            st.audio(audio_bytes)
            st.download_button(label="Download Speech",
                               data=audio_bytes,
                               file_name="speech.mp3",
                               mime="audio/mp3")
            
if __name__=='__main__':
    main()