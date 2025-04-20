# 🎶 Melodia: Interactive Audio Adventure

Welcome to **Melodia**, an educational and interactive audio-based web app that lets users explore the magical world of music effects through storytelling, voice recording, and sound transformation.

---

## 🌟 Purpose

Melodia was created to support **educational exploration** of sound processing and audio effects in a fun, gamified format. Built with the Faculty of Education in mind, it helps students:

- Understand audio effects like **Reverb**, **Delay**, **Distortion**, and **Chorus**
- Learn through interaction, exploration, and creativity
- Engage with signal processing in a magical fantasy narrative world

Each "stage" of the game represents a different sound effect — users record their voice and apply effects to progress through the story.

---

## 🧰 Tech Stack

### 🎤 Backend
- **FastAPI** – Serves the audio processing API
- **[Spotify Pedalboard](https://github.com/spotify/pedalboard)** – Applies real-time audio effects to user recordings
- **Poetry** – For Python dependency management

### 🖼 Frontend
- **Vanilla HTML, CSS, JavaScript** – Lightweight, fast, and fully customizable
- **Recorder.js** – Captures audio from the user’s microphone
- **Progress-based UI** – Built to visualize user advancement and unlock new levels

### 🐳 Deployment
- **Docker** – Containerized for consistent deployment
- **DigitalOcean App Platform** – Hosting the application using Docker images from Docker Hub

---

## 🚀 Running Locally

1. Clone this repository
2. Build the Docker image:

```bash
docker build -t melodia-app .
```

3. Run the app:

```bash
docker run -p 8000:8000 melodia-app
```

Then visit: [http://localhost:8000](http://localhost:8000)

---

## ✨ Highlights
- 🎮 Progression map and fantasy-themed story for each stage
- 🧙‍♂️ Final boss fight using all effects combined
- 🎧 Audio effects processed server-side with high quality
- 💾 All pages and assets served statically for performance

---

## 📁 Project Structure
```
frontend/
  ├── index.html
  ├── stage-map.html
  ├── stage1-distortion.html
  ├── stage2-chorus.html
  ├── stage3-reverb.html
  ├── stage4-delay.html
  ├── stage5-boss.html
  ├── picture/  # Images and icons
  └── style.css
backend/
  └── main.py  # FastAPI application
```

---

## 📜 License
MIT License — use and adapt freely for education and fun 💖

---

Feel free to contribute, remix, or deploy your own version of Melodia!

🎧 Happy adventuring through sound! 🎶
