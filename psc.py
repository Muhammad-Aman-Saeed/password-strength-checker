import re
import streamlit as st

# styling

st.set_page_config (page_title = "Password Strength Checker", page_icon = "🔐")

st.title ("🔐 Password Strength Checker")
st.markdown("""
## Welcome To Password Strength Checker by Aman Saeed..!
    Check your password strength 🔏""")

password = st.text_input ("Enter Password:", type = "password", help = "Ensure your password is strong 🔒")

def check_password_strength (password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score +=1 
    else:
        feedback.append ("❌ Password should be at least 8 character long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score +=1
    else:
        feedback.append("❌ Passwprd should include both Upper-Case (A-Z) and Lower-Case (a-z) letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include at least one number (0-9).")

    if re.search(r"[!@#$%&*]", password):
        score += 1
    else:
        feedback.append ("❌ Password shuold include at least one special character (!@#$%&*).")


    

    #show strength

    if score == 4:
        st.success ("✔️ **Strong Password** - Your password is secure")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Need more improvement")
    else:
        st.error("❌ **Weak Password** - Poor password")


    if feedback:
        with st.expander ("🔍**Improve Your Password**"):
            for item in feedback:
                st.write (item)


#button
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning ("⚠️ Please enter a password first:") #this suggestion will show if the password is empty