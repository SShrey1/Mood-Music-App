import streamlit as st
from mood_detection import get_mood
from spotify_client import create_spotify_client
from voice_input import get_voice_input
from db import init_db, insert_record, get_history, clear_history
from deep_translator import GoogleTranslator


def translate_to_english(text):
    try:
        translated = GoogleTranslator(source='auto', target='en').translate(text)
        return translated
    except Exception as e:
        st.error(f"Translation error: {e}")
        return text  # fallback


# 🚀 Initialize DB and Streamlit Page
init_db()
st.set_page_config(page_title="Mood-Based Hindi Music", page_icon="🎧")
st.title("🎶 Mood-Based Hindi Music Recommender")
st.markdown("Tell us how you're feeling, and get music for your mood.")

# 📤 Mood Input Section
st.markdown("---")
st.header("🗣️ Mood Input")

user_input = st.text_input("Tell us how you're feeling (in any language):")

if st.button("🎤 Speak Your Mood"):
    voice_text = get_voice_input()
    if voice_text:
        user_input = voice_text
        st.write("🗣️ You said:", voice_text)
    else:
        st.warning("Couldn't detect your voice.")

# 🌐 Translate & Detect Mood
if user_input:
    translated_input = translate_to_english(user_input)
    st.write(f"🌐 Translated to English: `{translated_input}`")

    mood = get_mood(translated_input)
    st.success(f"😊 Detected Mood: **{mood}**")

    # 🎧 Spotify Recommendation
    genre = "Bollywood"
    query = f"{mood} {genre} Hindi"

    with st.spinner("🎵 Fetching songs for you..."):
        sp = create_spotify_client()
        results = sp.search(q=query, type='track', limit=5, market='IN')

        if results['tracks']['items']:
            for track in results['tracks']['items']:
                track_name = track['name']
                artist = track['artists'][0]['name']
                url = track['external_urls']['spotify']
                preview_url = track['preview_url']
                image_url = track['album']['images'][0]['url']

                # 🖼️ Display Track Info
                st.image(image_url, width=200)
                st.write(f"**{track_name}** by *{artist}*")
                if preview_url:
                    st.audio(preview_url, format='audio/mp3')
                st.markdown(f"[🎧 Listen on Spotify]({url})")
                st.markdown("---")

                # ✅ Save to History
                insert_record(mood, track_name)
        else:
            st.error("😕 No songs found! Try another mood.")

# 🕘 Mood & Song History
st.markdown("---")
st.header("📊 Mood & Song History")

if st.button("🧹 Clear History"):
    clear_history()
    st.success("History cleared!")

history = get_history()
if history:
    for mood, song, timestamp in history:
        st.write(f"🕒 {timestamp} | 😊 Mood: **{mood}** | 🎵 Song: *{song}*")
else:
    st.info("No history found yet. Play some music!")

