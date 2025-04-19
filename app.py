import streamlit as st                        # pip install streamlit
from deep_translator import GoogleTranslator  # pip install -U deep-translator
import pyperclip                              # pip install pyperclip
# Page Configuration
st.set_page_config(
    page_title='tyrex Translator - Free Online Translator',
    page_icon='🌍',
    layout="centered"
)


links_row = "<a href='https://www.linkedin.com/in/nadeem-akhtar-/' target='_blank'>" \
            "<img src='https://img.icons8.com/color/48/000000/linkedin.png' width='30'></a>" \
            " | " \
            "<a href='https://github.com/NadeemAkhtar1947' target='_blank'>" \
            "<img src='https://img.icons8.com/color/48/000000/github.png' width='30'></a>" \
            " | " \
            "<a href='https://www.kaggle.com/mdnadeemakhtar/code' target='_blank'>" \
            "<img src='https://www.kaggle.com/static/images/site-logo.png' width='30'></a>" \
            " | " \
            "<a href='https://nsde.netlify.app/' target='_blank'>" \
            "<img src='https://img.icons8.com/color/48/000000/globe--v1.png' width='30'></a>"

# Display the links row using Markdown
st.markdown(links_row, unsafe_allow_html=True)

# Initialize Session States
if 'translate' not in st.session_state:
    st.session_state.translate = []  # For storing translations

if 'get_value' not in st.session_state:
    st.session_state.get_value = ''  # For uploaded file content

if 'widget' not in st.session_state:
    st.session_state.widget=''     # For clearing text area

if 'input_language' not in st.session_state:
    st.session_state.input_language = 'English'  # Default input language

if 'output_language' not in st.session_state:
    st.session_state.output_language = 'Bhojpuri'  # Default output language

# Functions
def translator():
    try:
        translation = GoogleTranslator(
            source=st.session_state.input_language.lower(),
            target=st.session_state.output_language.lower()
        ).translate(st.session_state.get_value or text_area)
        st.session_state.translate = [translation]
    except Exception as e:
        st.error(f"Translation error: {e}")

def clear_text():
    st.session_state.pop('get_value')  # Clear content from uploaded file
    st.session_state.widget=''         # Clear content from keyboard

def swap_languages():
    st.session_state.input_language, st.session_state.output_language = (
        st.session_state.output_language,
        st.session_state.input_language,
    )

def copy_to_clipboard():
    if st.session_state.translate:
        pyperclip.copy("".join(st.session_state.translate))
        st.success("Translation copied to clipboard!")

# Main Content
st.header("📑 Tyrex Translator")
st.write("Translate text across multiple languages quickly and easily!")

languages=[
    "Afrikaans","Akan","Albanian","Amharic","Arabic","Armenian","Assamese","Aymara","Azerbaijani",
    "Bambara","Bangla","Basque","Belarusian","Bhojpuri","Bosnian","Bulgarian","Burmese",
    "Catalan","Cebuano","Central Kurdish","Chinese (Simplified)","Chinese (Traditional)","Corsican",
    "Croatian","Czech", "Danish","Divehi","Dogri","Dutch","English","Esperanto",
    "Estonian","Ewe","Filipino","Finnish","French", "Galician","Ganda","Georgian","German","Goan Konkani",
    "Greek", "Guarani","Gujarati", "Haitian Creole","Hausa","Hawaiian","Hebrew",
    "Hindi","Hmong","Hungarian", "Icelandic","Igbo","Iloko","Indonesian","Irish","Italian","Japanese",
    "Javanese", "Kannada","Kazakh","Khmer","Kinyarwanda","Korean","Krio","Kurdish","Kyrgyz",
    "Lao","Latin","Latvian","Lingala","Lithuanian","Luxembourgish",
    "Macedonian","Maithili","Malagasy","Malay","Malayalam","Maltese","Manipuri (Meitei Mayek)","Māori",
    "Nepali","Northern Sotho","Norwegian","Nyanja","Odia","Oromo", "Pashto","Persian","Polish","Portuguese","Punjabi",
    "Quechua", "Marathi","Mizo","Mongolian", "Romanian","Russian", "Samoan","Sanskrit"
    ,"Scottish Gaelic","Serbian","Shona","Sindhi","Sinhala","Slovak","Slovenian","Somali","Southern Sotho",
    "Tajik","Tamil","Tatar","Telugu","Thai","Tigrinya","Tsonga","Turkish","Turkmen",
    "Ukrainian","Urdu","Uyghur","Uzbek","Vietnamese", "Spanish","Sundanese","Swahili","Swedish",
    "Welsh","Western Frisian","Xhosa","Yiddish","Yoruba","Zulu"
]

# Sort the languages alphabetically
languages_sorted = sorted(languages)

# Language Selection with Clear Text
col1, col2, col3 = st.columns([1,0.7,1])
with col1:
    st.session_state.input_language = st.selectbox(
        "**Input Language**", languages_sorted, index=languages_sorted.index(st.session_state.input_language)
    )
with col2:
    #st.markdown("<div style='display: flex; justify-content: center;'  height: 100%;>", unsafe_allow_html=True)
    st.button("🔁 Swap Languages", on_click=swap_languages, key="swap_languages_button_1")
    #st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.session_state.output_language = st.selectbox(
        "**Output Language**", languages_sorted, index=languages_sorted.index(st.session_state.output_language)
    )

# Input text area
text_area=st.text_area(label='Input',value=st.session_state.get_value, height=150,
                        placeholder='Enter text', help='Enter the text need to be translated!',
                        key='widget', label_visibility='collapsed')

# File Upload
file = st.file_uploader("Or upload a .txt file", type="txt")
if file:
    st.session_state.get_value = file.read().decode("utf-8")

# Buttons
col1,col2,col3=st.columns([1,1,1])
with col1:   # Clear input text area Button
   st.button(label='**Clear**',type='secondary',on_click=clear_text)
with col2:   # Translate input text area Button
   st.button(label='**Translate**',type='secondary', on_click=translator)
with col3:  # Copy to Clipboard Button
    st.button(label="**Copy Translation**", on_click=copy_to_clipboard)

# Output
if st.session_state.translate:
    st.text_area(
        "Translation:",
        value="".join(st.session_state.translate),
        height=150,
    )

st.markdown("---")
st.markdown("Copyright © Nadeem Akhtar. All Rights Reserved")
