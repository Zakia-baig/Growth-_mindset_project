
# Streamlit Project
import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱")

st.title("🚀 Growth Mindset Challenge: Web App with Streamlit")

st.header("📢 Welcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app is designed to help you develop a growth mindset through self-reflection, challenges, and achievements.")

# Quote section
st.header("🌟 Today's Growth Mindset Quote")
st.write("**'True growth begins where comfort ends—every challenge is a stepping stone to the mind’s greatest potential.'**")

# Challenge input
st.header("💡 What Challenge Are You Facing Today?")
user_input = st.text_input("Describe a challenge you're currently dealing with:")

if user_input:
    st.success(f"You're facing: **{user_input}**. Keep pushing forward—every step counts!")
else:
    st.warning("Share your challenge to begin your growth journey!")

# Reflection section
st.header("📝 Reflect on Your Learning")
reflection = st.text_area("Write down your thoughts and insights:")

if reflection:
    st.success(f"Great insight! Here's your reflection: **{reflection}**")
else:
    st.info("Reflecting on your experiences helps you grow. Share your thoughts!")

# Achievement section
st.header("🎉 Celebrate Your Wins!")
achievement = st.text_input("What’s something you've recently accomplished?")

if achievement:
    st.success(f"Awesome! You achieved: **{achievement}** 🎊")
else:
    st.info("Every achievement matters, no matter how small. Share one now!")

# Footer
st.write("---")
st.write("🌱 Keep believing in yourself—growth is a journey, not a destination.")
st.write("💻 Created by **Zakia Baig**")
