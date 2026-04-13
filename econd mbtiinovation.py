import streamlit as st

# 1. Inisialkan "ingatan" kalau belum ada
if 'soalan_ke' not in st.session_state:
    st.session_state.soalan_ke = 1
    st.session_state.jawapan = []

# Fungsi untuk pergi ke soalan seterusnya
def next_question(pilihan):
    st.session_state.jawapan.append(pilihan)
    st.session_state.soalan_ke += 1

# --- LOGIC SOALAN ---

if st.session_state.soalan_ke == 1:
    st.header("Question 1")
    st.write("At a party or banquet, you usually mingle with...")
    
    col1, col2 = st.columns(2)
    if col1.button("A. Many people including strangers"):
        next_question("A")
        st.rerun() # Guna st.rerun() supaya dia terus refresh ke soalan 2
    if col2.button("B. A few people you know"):
        next_question("B")
        st.rerun()

elif st.session_state.soalan_ke == 2:
    st.header("Question2")
    st.write("Do you prefer logic or emotion?")
    
    col1, col2 = st.columns(2)
    if col1.button("A. Logic"):
        next_question("A")
        st.rerun()
    if col2.button("B. Emotion"):
        next_question("B")
        st.rerun()
        
elif st.session_state.soalan_ke == 3:
    st.header("Question3")
    st.write("Which of the following is less acceptable?")

    col1, col2 = st.columns(2)
    if col1.button("A. Have your (head in the clouds)"):
        next_question("A")
        st.rerun()
    if col2.button("B. Be (in a rut)"):
        next_question("B")
        st.rerun()

elif st.session_state.soalan_ke == 4:
    st.header("Question4")
    st.write("When judging others,you are more often influence by?")

    col1, col2 = st.columns(2)
    if col1.button("A. Rules than by circumstances"):
        next_question("A")
        st.rerun()
    if col2.button("B. Circumstances than by rules"):
        next_question("B")
        st.rerun()

elif st.session_state.soalan_ke == 5:
    st.header("Question5")
    st.write("You are more attracted to things..")

    col1, col2 = st.columns(2)
    if col1.button("A. Convincing"):
        next_question("A")
        st.rerun()
    if col2.button("B. Moving"):
        next_question("B")
        st.rerun()

elif st.session_state.soalan_ke == 6:
    st.header("Question6")
    st.write("You prefer events that start with...")

    col1, col2 = st.columns(2)
    if col1.button("A.Punctuality"):
        next_question("A")
        st.rerun()
    if col2.button("B.Fun"):
        next_question("B")
        st.rerun()

elif st.session_state.soalan_ke == 7:
    st.header("Question7")
    st.write("You usually make choices...")

    col1, col2 = st.columns(2)
    if col1.button("A. Carefully"):
        next_question("A")
        st.rerun()
    if col2.button("B. Somewhat impulsively"):
        next_question("B")
        st.rerun()

elif st.session_state.soalan_ke == 8:
    st.header("Question8")
    st.write("In terms of receiving information in your social group, you are the")

    col1, col2 = st.columns(2)
    if col1.button("A. First to receive information"):
        next_question("A")
        st.rerun()
    if col2.button("B. Last to receive information"):
        next_question("B")
        st.rerun()

elif st.session_state.soalan_ke == 9:
    st.header("Question9")
    st.write("Facts should be...")

    col1, col2 = st.columns(2)
    if col1.button("A. Facts should be facts in themselves"):
        next_question("A")
        st.rerun()
    if col2.button("B. Facts should explain principles"):
        next_question("B")
        st.rerun()

elif st.session_state.soalan_ke == 10:
    st.header("Question 10")
    st.write("Authors should write based on?")

    col1, col2 = st.columns(2)
    if col1.button("A. Authors should write based on facts and truth"):
        next_question("A")
        st.rerun()
    if col2.button("B. Authors should write based on analogies and imagination"):
        next_question("B")
        st.rerun()

elif st.session_state.soalan_ke == 11:
    st.header("Question 11")
    st.write("You are a person who is better recognized as..")

    col1, col2 = st.columns(2)
    if col1.button("A. Calm"):
        next_question("A")
        st.rerun()
    if col2.button("B. Friendly"):
        next_question("B")
        st.rerun()
        
elif st.session_state.soalan_ke == 12:
    st.header("Question 12")
    st.write("You are comfortable in making decisions related to?")

    col1, col2 = st.columns(2)
    if col1.button("A. Logical decisions"):
        next_question("A")
        st.rerun()
    if col2.button("B. Moral issues"):
        next_question("B")
        st.rerun()
        

elif st.session_state.soalan_ke == 13:
    st.header("Question 13")
    st.write("Life events should ideally take place...")

    col1, col2 = st.columns(2)
    if col1.button("A. planned"):
        next_question("A")
        st.rerun()
    if col2.button("B. randomly"):
        next_question("B")
        st.rerun()
       

elif st.session_state.soalan_ke == 14:
    st.header("Question 14")
    st.write("You think you are more?")

    col1, col2 = st.columns(2)
    if col1.button("A. serious"):
        next_question("A")
        st.rerun()
    if col2.button("B. determined"):
        next_question("B")
        st.rerun()
         
elif st.session_state.soalan_ke == 15:
    st.header("Question 15")
    st.write("When with others,you usually...")

    col1, col2 = st.columns(2)
    if col1.button("A. start the conversation"):
        next_question("A")
        st.rerun()
    if col2.button("B. wait for the conversation to start"):
        next_question("B")
        st.rerun()
        

elif st.session_state.soalan_ke == 16:
    st.header("Question 16")
    st.write("You are more inclined towards....")

    col1, col2 = st.columns(2)
    if col1.button("A. practical"):
        next_question("A")
        st.rerun()
    if col2.button("B. fantasy"):
        next_question("B")
        st.rerun()

elif st.session_state.soalan_ke == 17:
    st.header("Question 17")
    st.write("Children usually lack effort in?")

    col1, col2 = st.columns(2)
    if col1.button("A.study"):
        next_question("A")
        st.rerun()
    if col2.button("B.  play"):
        next_question("B")
        st.rerun()
elif st.session_state.soalan_ke == 18:
    st.header("Question 18")
    st.write("Which one of the following is more satisfactory?")

    col1, col2 = st.columns(2)
    if col1.button("A.discuss an issue in depth"):
        next_question("A")
        st.rerun()
    if col2.button("B. get agreement on something"):
        next_question("B")
        st.rerun()

elif st.session_state.soalan_ke == 19:
    st.header("Question 19")
    st.write("You are considered more")

    col1, col2 = st.columns(2)
    if col1.button("A.firm than soft"):
        next_question("A")
        st.rerun()
    if col2.button("B. soft than firm"):
        next_question("B")
        st.rerun()
elif st.session_state.soalan_ke == 20:
        st.header("Question 20")
        st.write("You are more comfortable with a job that is")

    col1, col2 = st.columns(2)
    if col1.button("A.Permanent"):
        next_question("A")
        st.rerun()
    if col2.button("B.  Part-time"):
        next_question("B")
        st.rerun()

elif st.session_state.soalan_ke == 21:
    st.header("Question 21")
    st.write("You prioritize things more")

    col1, col2 = st.columns(2)
    if col1.button("A. certainty"):
        next_question("A")
        st.rerun()
    if col2.button("B.  openness"):
        next_question("B")
        st.rerun()

elif st.session_state.soalan_ke == 22:
    st.header("Question 22")
    st.write("You prefer")

    col1, col2 = st.columns(2)
    if col1.button("A. many friends with less close and short-term relationships"):
        next_question("A")
        st.rerun()
    if col2.button("B.  a few friends with close and long-term relationships"):
        next_question("B")
        st.rerun()

    elif st.session_state.soalan_ke == 23:
    st.header("Question 23")
    st.write("You trust more")

    col1, col2 = st.columns(2)
    if col1.button("A. experience"):
        next_question("A")
        st.rerun()
    if col2.button("B.  gut feeling"):
        next_question("B")
        st.rerun()

    
    elif st.session_state.soalan_ke == 24:
    st.header("Question 24")
    st.write("You are more interested in")

    col1, col2 = st.columns(2)
    if col1.button("A. production and distribution"):
        next_question("A")
        st.rerun()
    if col2.button("B.  design and research"):
        next_question("B")
        st.rerun()

   elif st.session_state.soalan_ke == 25:
    st.header("Question 25")
    st.write("The most praised person is the one who has strength")

    col1, col2 = st.columns(2)
    if col1.button("A. clear thinking"):
        next_question("A")
        st.rerun()
    if col2.button("B.  strong feelings"):
        next_question("B")
        st.rerun()

 elif st.session_state.soalan_ke == 26:
    st.header("Question 26")
    st.write("In yourself, the most valued trait is")

    col1, col2 = st.columns(2)
    if col1.button("A. not being hesitant or hesitant"):
        next_question("A")
        st.rerun()
    if col2.button("B. being obedient"):
        next_question("B")
        st.rerun()

elif st.session_state.soalan_ke == 27:
    st.header("Question 27")
    st.write("Peacefully it is better")

    col1, col2 = st.columns(2)
    if col1.button("A. to determine and regulate the situation"):
        next_question("A")
        st.rerun()
    if col2.button("B. to let the situation develop on its own"):
        next_question("B")
        st.rerun()

elif st.session_state.soalan_ke == 28:
    st.header("Question 28")
    st.write("You feel more comfortable")

    col1, col2 = st.columns(2)
    if col1.button("A. after making a decision"):
        next_question("A")
        st.rerun()
    if col2.button("B. before making a decision"):
        next_question("B")
        st.rerun()

elif st.session_state.soalan_ke == 29:
    st.header("Question 29")
    st.write("When the phone rings, you")

    col1, col2 = st.columns(2)
    if col1.button("A. quickly answer it"):
        next_question("A")
        st.rerun()
    if col2.button("B. hope someone else answers it"):
        next_question("B")
        st.rerun()

elif st.session_state.soalan_ke == 30:
    st.header("Question 30")
    st.write("In your writing you choose things that are")

    col1, col2 = st.columns(2)
    if col1.button("A. literal"):
        next_question("A")
        st.rerun()
    if col2.button("B.  figurative"):
        next_question("B")
        st.rerun()   

elif st.session_state.soalan_ke == 31:
    st.header("Question 31")
    st.write("You are more interested in the elements of")

    col1, col2 = st.columns(2)
    if col1.button("A. basic and core"):
        next_question("A")
        st.rerun()
    if col2.button("B. derivative and ancillary"):
        next_question("B")
        st.rerun()   

elif st.session_state.soalan_ke == 32:
    st.header("Question 32")
    st.write("Which strength is more important?")

    col1, col2 = st.columns(2)
    if col1.button("A. the ability to reason clearly"):
        next_question("A")
        st.rerun()
    if col2.button("B.  the ability to be compassionate"):
        next_question("B")
        st.rerun()      

elif st.session_state.soalan_ke == 33:
    st.header("Question 33")
    st.write("Basically you consider yourself to be")

    col1, col2 = st.columns(2)
    if col1.button("A. stubborn"):
        next_question("A")
        st.rerun()
    if col2.button("B. soft-hearted"):
        next_question("B")
        st.rerun()       

elif st.session_state.soalan_ke == 34:
    st.header("Question 34")
    st.write("You are more inclined toward events that are")

    col1, col2 = st.columns(2)
    if col1.button("A. planned"):
        next_question("A")
        st.rerun()
    if col2.button("B. unplanned"):
        next_question("B")
        st.rerun() 

elif st.session_state.soalan_ke == 35:
    st.header("Question 35")
    st.write("You are a more personable person")

    col1, col2 = st.columns(2)
    if col1.button("A.normal and routine"):
        next_question("A")
        st.rerun()
    if col2.button("B.a bit awkward and irregular"):
        next_question("B")
        st.rerun()        
# --- RESULT ---
    
else:
    st.header("Result!")
    st.write(f"Answer that you chose: {st.session_state.jawapan}")
    if st.button("Repeat"):
        st.session_state.soalan_ke = 1
        st.session_state.jawapan = []
        st.rerun()
