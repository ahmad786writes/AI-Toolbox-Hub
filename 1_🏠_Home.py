import streamlit as st
from translator.languages import languages

from transformers import pipeline 


# Include Font Awesome CDN
st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """,
    unsafe_allow_html=True,
)


# Page title
st.title('Welcome to the World of AI(AI Applications, All You need)')

# Sections for each AI tool
tools = ['🏠Home','📙Language Translation', '📝Summarization', 'Other Tools']
selected_tool = st.sidebar.selectbox('Select an AI Tool:', tools)


if selected_tool == '🏠Home':
    with st.sidebar:
        st.sidebar.image: st.sidebar.image("imgs/logo.png", use_column_width=True)
        st.write("-----------------------------------------")
        st.write("Tools like Language Translator, Summarizer, MP3 to MP4 and many More are waiting for YOU")

     
    st.header('About Me')
    st.write("""
    Hi! I'm Ahmad Liaqat AKA Xu-Ansari, a passionate AI enthusiast. 
    I love exploring the latest in artificial intelligence and sharing my knowledge with the community.
    """)

    # Personal links
    st.subheader('Connect with Me:')
    st.markdown("<i class='fab fa-github'></i>-->[GitHub](https://github.com/ahmad786writes) ", unsafe_allow_html=True)
    st.markdown("<i class='fab fa-linkedin'></i>-->[LinkedIn](https://www.linkedin.com/in/ahmad-liaqat-270247253) ", unsafe_allow_html=True)

    st.write("""
    Explore the world of AI through this showcase of cutting-edge tools and technologies.
    """)

elif selected_tool == '📙Language Translation':
    st.header('📙Language Translator')
    with st.sidebar:
        st.sidebar.image: st.sidebar.image("imgs/language_tool.png", use_column_width=True)
        st.write("-----------------------------------------")
        st.write("NLLB-200 is a machine translation model developed by Meta AI with a primary focus on research, particularly for low-resource languages. It offers the ability to translate single sentences across an impressive range of 200 languages.")

    def translate_text(text, source_language, target_language):

        # Option 2: Using Hugging Face Transformers
        translator = pipeline("translation", model="facebook/nllb-200-distilled-600M")
        text_translated = translator(text,
                                src_lang=source_language,
                                tgt_lang=target_language)
        
        return text_translated[0]['translation_text']


    # Creating an instance of the Languages class
    languages_instance = languages()
    languages_dict = languages_instance.get_languages_dict()
    # Language selection options
    source_languages = all_languages_list = languages_instance.get_all_languages()
    target_languages = source_languages.copy()  # Can also be a custom subset

    source_lang = st.selectbox("Source Language", source_languages)
    target_lang = st.selectbox("Target Language", target_languages)


    source_lang = languages_dict[source_lang]
    target_lang = languages_dict[target_lang]

    # Text input area
    user_text = st.text_area("Enter text to translate:", height=100)

    # Translate button
    if st.button("Translate"):
        if user_text:
            translated_text = translate_text(text=user_text, source_language=source_lang, target_language=target_lang)
            st.write("Translation:")
            st.markdown(f"<div style='background-color: darkblue; padding: 10px; border-radius: 5px;'>{translated_text}</div>", unsafe_allow_html=True)
        else:
            st.warning("Please enter some text to translate.")

    # Display information about the chosen library (optional)
    st.write("Translation powered by:", "Hugging Face NLLB-200 distilled 600M variant")  


elif selected_tool == '📝Summarization':
    st.header('📝Summarization Tool')
    with st.sidebar:
        st.sidebar.image: st.sidebar.image("imgs/Summarization.png", use_column_width=True)
        st.write("-----------------------------------------")
        st.write("Bidirectional Autoregressive Transformer (BART) is a Transformer-based encoder-decoder model, often used for sequence-to-sequence tasks like summarization and neural machine translation. BART is pre-trained in a self-supervised fashion on a large text corpus.")
    # Function to translate text (replace with your chosen library)
    def summarize(text, min_length, max_length):

        # Option 2: Using Hugging Face Transformers
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        summary = summarizer(text,
                     min_length=min_length,
                     max_length=max_length)
        
        return summary[0]['summary_text']

    # Text input area
    user_text = st.text_area("Enter text you want to summarize:", height=200)
    min_value = st.number_input("Minimum length of summary:",min_value=1,max_value=200,step=1)
    max_value = st.number_input("Maximum length of summary:",min_value=min_value,max_value=200,step=1)


    # Translate button
    if st.button("summarize"):
        if user_text and min_value and max_value:
            summarized_text = summarize(text=user_text, min_length=min_value, max_length=max_value)
            st.write("Translation:")
            st.markdown(f"<div style='background-color: darkblue; padding: 10px; border-radius: 5px;'>{summarized_text}</div>", unsafe_allow_html=True)
        else:
            st.warning("Please enter some text to translate. Or set the minimum and maximum length of a summary")

    # Display information about the chosen library (optional)
    st.write("Summarization powered by:", "Hugging Face BART (large-sized model), fine-tuned on CNN Daily Mail")  

else:
    st.header('Other Tools')
    # Add content for other tools
    st.write("""
    This section showcases other AI tools that are not covered in the main categories above.
    """)





