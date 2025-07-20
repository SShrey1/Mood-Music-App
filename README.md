# 🎵 Mood Music App

A Python-based application that detects a user's mood using facial expressions and voice, then recommends songs via Spotify tailored to their emotional state.

---

##  Features

- **Mood Detection**: Uses facial emotion recognition and voice input to determine the user’s mood.
- **Spotify Integration**: Automatically fetches and plays music that matches the detected mood.
- **Mood History**: Stores past moods in a local SQLite database (`mood_history.db`) for tracking patterns over time.
- **Voice Recognition**: Optional mood input via voice if facial detection is unavailable.

---

## 🗂️ Project Structure
Mood-Music-App-master/
├── app.py # Main application entry point
├── db.py # Handles database operations
├── facial_emotion.py # Detects emotion from facial expressions
├── mood_detection.py # Core logic for determining mood
├── mood_history.db # SQLite database file for storing history
├── spotify_client.py # Spotify API interaction and music playback
├── voice_input.py # Voice-based mood detection
└── .idea/ # IDE config (can be ignored)


