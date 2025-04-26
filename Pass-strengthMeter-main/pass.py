import streamlit as st
import re

def check_password_strength(password):
    strength = "Weak"
    score = 0
    
    # Conditions for strength
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  # Escaped the double quotes
        score += 1
    
    # Determine strength
    if score >= 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    
    return strength, score

def main():
    st.title("🔒 Password Strength Meter")
    st.markdown("💡 *'A strong password is the first step to digital security.'*")
    st.write("Enter a password to check its strength.")
    
    password = st.text_input("Enter Password:", type="password")
    
    if password:
        strength, score = check_password_strength(password)
        
        st.subheader(f"Password Strength: {strength}")
        
        # Motivational Quote Based on Strength
        if strength == "Weak":
            st.info("🔴 'A weak password is like an unlocked door—secure it before it's too late.'")
        elif strength == "Moderate":
            st.info("🟡 'A good password is a shield; make it stronger to guard your data!'")
        else:
            st.info("🟢 'A strong password is your digital armor—well done!'")
        
        st.progress(score / 5)
        
        # Strength Messages
        if strength == "Weak":
            st.error("Your password is weak! Try adding uppercase, lowercase, numbers, and special characters.")
        elif strength == "Moderate":
            st.warning("Your password is moderate! Consider adding more complexity.")
        else:
            st.success("Your password is strong! Well done.")
    
    # Show creator name in the browser
    st.markdown("---")
    st.markdown("**Created by Ahsan Durrani**")
    
if __name__ == "__main__":
    main()