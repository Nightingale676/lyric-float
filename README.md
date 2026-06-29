# 🎵 Lyric Float

A desktop app that makes synced lyrics **float up your screen** in little popup boxes, timed to a song — like karaoke confetti for your desktop. ✨

Built with **Python + Tkinter** for the visuals and **Pygame** for audio playback.

---

## 🗂️ Repo Contents

```
lyric-float/
├── .gitignore
├── README.md
└── coding.py     # main script
```

> 📝 Note: an audio file (e.g. `song3.mp3`) is required to run this but is **not included in the repo** — add your own MP3 to the same folder before running.

---

## 🚀 Features

- 🫧 Lyric lines spawn as floating boxes that rise from the bottom of the screen
- ⌨️ Typewriter-style text reveal for each lyric box
- 🔄 Boxes alternate spawning left/right so they don't overlap
- 🎶 Synced audio playback via Pygame
- 🪟 Borderless, always-on-top popup windows for a clean overlay look
- 🧹 Auto-cleanup of boxes once they float off-screen

---

## 📦 Requirements

- 🐍 Python 3.8+
- 🎮 [`pygame`](https://pypi.org/project/pygame/) (for audio — optional but recommended)

```bash
pip install pygame
```

> 💡 If `pygame` isn't installed, the app still runs — it just skips audio and shows lyrics silently.

---

## ▶️ How to Run

1. Place your audio file in the **same folder** as `coding.py`.
2. Update the filename near the top of the script:
   ```python
   AUDIO_FILE = "song3.mp3"
   ```
3. Run from a terminal (so you can see any errors):
   ```bash
   python coding.py
   ```
4. Click **Start** 🟢 — the window minimizes, audio begins, and lyrics float up in sync.

---

## ⏱️ Customizing Lyrics & Timing

Lyrics live in the `LYRICS` list near the top of `coding.py`:

```python
LYRICS = [
    (5.0, "Your lyric line here"),
    (8.2, "Next line..."),
]
```

Each entry is `(start_time_in_seconds, "text")`. 🎯

---

## 🎨 Customization Options

| Setting | What it controls |
|---|---|
| `BOX_W`, `BOX_H` 📐 | Size of each lyric popup |
| `FONT` 🔤 | Font family, size, weight |
| `BG_COLOR` / `FG_COLOR` 🎨 | Background & text color |
| `RISE_SPEED` 🚀 | How fast boxes float upward (px/sec) |
| `BOTTOM_SPAWN_OFFSET` 📍 | How far above the bottom edge boxes spawn |

---

## 🐛 Troubleshooting

**Audio not playing?**
1. ✅ Run from a terminal, not by double-clicking — errors print there
2. ✅ Confirm `pygame` is installed
3. ✅ Confirm the audio file is in the same folder as `coding.py`
4. ✅ Try `.wav` or `.ogg` if `.mp3` fails to load

---

## 📜 License

Personal/educational use. 🎤
