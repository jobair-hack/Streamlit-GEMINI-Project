import streamlit as st
from api_calling import Note_Generator,audio_transcrept,Quiz_Generator
from PIL import Image
#Title
st.title("Note Summary and Quiz Genarator")
st.markdown("Upload up-to 3 images to generate Note summary and Quizzes")
st.divider()

#image upload
with st.sidebar:
    st.header("let")
    images = st.file_uploader("upload your Notes",
                     type = ['jpg','png','jpeg'],
                     accept_multiple_files = True)
    
    images = [Image.open(x) for x in images]
    
    if images:
        if len(images) > 5:
            st.error(" Can't Upload more then 5 images")
        else:
            st.subheader("Image Uploaded")
            col = st.columns(len(images))
            for i,per_image in enumerate(images):
                with col[i]:
                    st.image(per_image)
#difficulty

    select_op = st.selectbox("Select your difficulty of Quize",
             ("Easy","Medium","Hard"),
             index = None)


    press = st.button("Click the button to initiate AI",type = "primary")

if press:
    if not images:
        st.error("You Must Upload One Image")
    if not select_op:
        st.error("You Must Select a Difficulty")
    if images and select_op:

        #Note
        with st.container(border = True):
            st.subheader("Your Note")
            with st.spinner("Searching"):
                note_g = Note_Generator(images)
                
            st.markdown(note_g)



        #Audio

        with st.container(border = True):
            st.subheader("Your Audio")
            with st.spinner("transcrepting"):
                note_g = note_g.replace("*"," ")
                note_g =  note_g.replace('#'," ")
                audio_tr = audio_transcrept(note_g)
            
            st.audio(audio_tr)

        #Quiz


        with st.container(border = True):
            st.subheader(f"Quiz ({select_op}) dificulty")
            with st.spinner("Generating Quiz"):
                quiz_g = Quiz_Generator(images,select_op)
            
            st.markdown(quiz_g)