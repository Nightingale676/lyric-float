import tkinter as tk
import time
import random
import math

try:
    import pygame
    HAS_AUDIO = True
except ImportError:
    HAS_AUDIO = False


AUDIO_FILE = r".\redred.mp3"  # set to "" to disable audio

# DEBUG: Enable to see timing info
DEBUG_MODE = True

# (start_time_in_seconds, "lyric text")
LYRICS = [
    (8.0, "Green, green"),
    (8.28, "따바라 한 모금 sip (Woo)"),
    (10.12, "Caffeine 또 kickin' in"),
    (12.08, "어젯밤에 만들던 beat (Beat)"),
    (14.1, "내 폰에 다 담아서 거리로 나갔어"),
    (16.18, "다섯 시 공기를 빙빙"),
    (18.2, "입꼬리 올라가 힝힝"),
    (20.18, "핸드폰 바꿔 놔 D-N-D"),
    (21.65, "Seeing all kinds of green, green"),
    (24.9, "하파이브. 하파이브"),
    (25.92, "I put my hands in my pocket"),
    (28.83, "Outside, 한 밤에 (한 밤에)"),
    (30.12, "사람 없는 스팟으로 빨리 (Woo)"),
    (31.88, "I do this shit with my team"),
    (34.14, "누누군가 싫어할 짓 (It, it)"),
    (36.1, "알 바가 아니여 get it, get it"),
    (38.02, "신호등 바뀌었어 green, green"),
    (40.04, "팔랑이 팔랑이. That's red"),
    (42.0, "눈치나 사비. That's red"),
    (43.88, "동아리 사디. That's red"),
    (46.02, "넘어가 울타리 green, green"),
    (47.96, "군대 이과디. That's red"),
    (49.94, "주변을 사비. That's red"),
    (51.9, "크라잉 쳐제과. That's red"),
    (53.92, "You should come mess with the team"),
    (55.76, "내 친구들 전부 한 트럭에 다 담아서 거리로 나갔어 빙빙"),
    (59.84, "거리서 돌다가 돌아가 스튜디오"),
    (61.82, "끈끈어지게 stinky"),
    (63.84, "팔랑이 팔랑이. That's red"),
    (65.89, "눈치나 사비. That's red"),
    (67.84, "동아리 사디. That's red"),
    (69.8, "You should come mess with the team"),
    (71.28, "They called me a freak, 홀린 듯이, yeah"),
    (73.26, "만들던 tracks, yeah"),
    (74.24, "두고 모일 friends. yeah"),
    (75.28, "하루가 갈수록 늘어가 pack"),
    (77.22, "진짜 뱅기처럼 밟아가 step"),
    (79.12, "Huh. screaming loud like yeah yeah"),
    (81.68, "꼴깍 달려 like yeah yeah"),
    (83.64, "F1, 들지 마 red flag"),
    (85.66, "You should come mess with the team (Tell me what's red)"),
    (87.26, "Everyone scream"),
    (88.1, "짜여있는 반지넨 scene. That's red"),
    (90.12, "먼지가 쌓인 게 scene. That's red"),
    (92.18, "점수가 무다는 cc"),
    (93.64, "답답해 정수리 씨뻘게 지쳐. That's red"),
    (96.0, "우린 gotta 팍 나르 소화"),
    (97.78, "다시 배워봐 you gotta know down"),
    (99.72, "불러와 버리네 두 번째 오라"),
    (101.52, "신호등 바뀌었어 그린 그린"),
    (103.5, "팔랑이 팔랑이. That's red"),
    (105.52, "눈치나 사비. That's red"),
    (107.44, "동아리 사디. That's red"),
    (109.44, "너와 가온다리 그린 그린"),
    (111.42, "군대 이과디. That's red"),
    (113.44, "주변을 사비. That's red"),
    (115.38, "크라잉 쳐제과. That's red"),
    (117.38, "유주가 멘솔에 틴"),
    (119.34, "Ay. yeah, turn it up"),
    (122.56, "Ay. i told you to turn it up"),
    (123.72, "I don't mess with them stupid red signs"),
    (125.36, "신호등 바뀌었어 그린 그린"),
    (127.36, "팔랑이 팔랑이. That's red"),
    (129.28, "눈치나 사비. That's red"),
    (131.32, "동아리 사디. That's red"),
    (133.22, "넘어가 울타리 green, green"),
    (135.24, "군대 이과디. That's red"),
    (136.99, "주변을 사비. That's red"),
    (139.18, "크라잉 쳐제과. That's red"),
    (141.16, "You should come mess with the team"),
    (143.0, "내 친구들 전부 한 트럭에 다 담아서 거리로 나갔어 빙빙"),
    (147.16, "거리서 돌다가 돌아가 스튜디오"),
    (149.14, "Cookin' up 'til we get stinky"),
    (151.18, "팔랑이 팔랑이. That's red"),
    (153.08, "눈치나 사비. That's red"),
    (155.1, "동아리 사디. That's red"),
    (157.06, "You should come mess with the team"),
]
 

BOX_W, BOX_H = 300, 250
FONT = ("Helvetica", 22, "bold")
BG_COLOR = "#fdfdf5"
FG_COLOR = "#111111"

RISE_SPEED = 90        # pixels per second every box moves upward
SPAWN_INTERVAL_MIN = 0   # not used directly; spawning follows LYRICS times
SAFE_EDGE_MARGIN = 220    # min distance from left/right screen edges
BOTTOM_SPAWN_OFFSET = 150  # how far above the bottom edge new boxes spawn

GLOW_RADIUS = 200       # max radius (px) of the ambient traffic-light pulse
GLOW_PEAK_ALPHA = 0.35  # max opacity reached mid-pulse
GLOW_DURATION = 1.0     # seconds for one full breathe-in/breathe-out cycle
GLOW_RINGS = 6          # concentric rings used to fake a soft glow falloff
GLOW_MAX_WHITEN = 1.0   # cap on how washed-out the outermost ring gets



class TrafficGlow:
    """A soft ambient color pulse that breathes behind the lyric boxes,
    echoing the song's red/green traffic-light motif."""

    TRANSPARENT_KEY = "#010101"

    def __init__(self, master, color, cx, cy):
        self.win = tk.Toplevel(master)
        self.win.overrideredirect(True)
        # Deliberately NOT -topmost: lyric boxes are topmost, so leaving this
        # window in the normal z-order band keeps it reliably behind them.
        # (Toggling -topmost off via .lower() each frame is unreliable on
        # Windows and can bury the window behind the whole desktop stack.)

        size = GLOW_RADIUS * 2
        self.x = cx - GLOW_RADIUS
        self.y = float(cy - GLOW_RADIUS)
        self.win.geometry(f"{size}x{size}+{int(self.x)}+{int(self.y)}")
        self.win.configure(bg=self.TRANSPARENT_KEY)
        self.win.wm_attributes("-transparentcolor", self.TRANSPARENT_KEY)
        self.win.attributes("-alpha", 0.0)

        canvas = tk.Canvas(self.win, width=size, height=size,
                            bg=self.TRANSPARENT_KEY, highlightthickness=0)
        canvas.pack()

        # Concentric squares, brightest at the center, tinting toward white at the edge
        for i in range(GLOW_RINGS, 0, -1):
            r = GLOW_RADIUS * (i / GLOW_RINGS)
            shade = self._tint(color, (i / (GLOW_RINGS + 1)) * GLOW_MAX_WHITEN)
            canvas.create_rectangle(
                GLOW_RADIUS - r, GLOW_RADIUS - r,
                GLOW_RADIUS + r, GLOW_RADIUS + r,
                fill=shade, outline=""
            )

        self.start_time = time.time()
        self._animate()

    @staticmethod
    def _tint(hex_color, amount):
        """Blend hex_color toward white by `amount` (0 = full color, 1 = white)."""
        hex_color = hex_color.lstrip("#")
        r, g, b = (int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
        r = int(r + (255 - r) * amount)
        g = int(g + (255 - g) * amount)
        b = int(b + (255 - b) * amount)
        return f"#{r:02x}{g:02x}{b:02x}"

    def _animate(self):
        progress = (time.time() - self.start_time) / GLOW_DURATION
        if progress >= 1.0:
            try:
                self.win.destroy()
            except tk.TclError:
                pass
            return
        # Sine-shaped breathe: fades in, peaks at the midpoint, fades back out
        alpha = GLOW_PEAK_ALPHA * math.sin(progress * math.pi)
        # Rise in lockstep with the lyric box so the glow stays behind it
        elapsed = progress * GLOW_DURATION
        y = self.y - RISE_SPEED * elapsed
        try:
            self.win.geometry(f"+{int(self.x)}+{int(y)}")
            self.win.attributes("-alpha", max(alpha, 0.0))
        except tk.TclError:
            return
        self.win.after(16, self._animate)


class LyricBox:
    """A single fixed-size lyric popup that rises forever and stays visible."""

    def __init__(self, master, text, x, y, color=None):
        self.master = master
        self.win = tk.Toplevel(master)
        self.win.overrideredirect(True)   # no title bar, popup look
        self.win.attributes("-topmost", True)
        self.win.configure(bg=BG_COLOR)
        # Lock the geometry to the fixed box size — same as Start window
        self.win.geometry(f"{BOX_W}x{BOX_H}+{int(x)}+{int(y)}")
        self.win.resizable(False, False)

        self.full_text = text
        
        # Use custom color if provided, otherwise use default
        text_color = color if color else FG_COLOR

        self.label = tk.Label(
            self.win,
            text="",
            font=FONT,
            bg=BG_COLOR,
            fg=text_color,
            wraplength=BOX_W - 30,
            justify="center"
        )
        self.label.pack(expand=True, fill="both", padx=15, pady=15)

        self.typewriter_index = 0
        self.typewriter()

        self.x = x
        self.y = float(y)

    def rise(self, dy):
        self.y -= dy
        self.win.geometry(f"{BOX_W}x{BOX_H}+{int(self.x)}+{int(self.y)}")

    def is_offscreen(self):
        return self.y + BOX_H < -50

    def typewriter(self):
        if self.typewriter_index <= len(self.full_text):
            self.label.config(text=self.full_text[:self.typewriter_index])
            self.typewriter_index += 1
            # Faster typewriter speed
            self.win.after(100, self.typewriter)


class LyricFloatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lyric Float Controller")
        self.root.geometry(f"{BOX_W}x{BOX_H}")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        # Debug label
        if DEBUG_MODE:
            self.debug_label = tk.Label(
                root, text="Time: 0.0s | Lyrics: 0", font=("Helvetica", 10),
                bg=BG_COLOR, fg="#666666"
            )
            self.debug_label.pack(side="top", pady=3)

        self.start_btn = tk.Button(
            root, text="Start", font=FONT, bg=BG_COLOR, fg=FG_COLOR,
            relief="flat", command=self.start
        )
        self.start_btn.pack(expand=True, fill="both", padx=15, pady=15)

        self.screen_w = root.winfo_screenwidth()
        self.screen_h = root.winfo_screenheight()

        self.next_lyric_idx = 0
        self.boxes = []
        self.last_frame_time = None
        self.current_side = "left"  # Alternate between left and right

    def random_safe_x(self):
        """Alternate between left and right positions only."""
        # Calculate left and right positions - wider spread
        center_x = self.screen_w // 2
        spacing = BOX_W + 150  # Larger gap between left and right
        
        left_x = center_x - spacing
        right_x = center_x + 90
        
        # Alternate between left and right
        if self.current_side == "left":
            self.current_side = "right"
            return left_x
        else:
            self.current_side = "left"
            return right_x

    def start(self):
        self.start_btn.pack_forget()
        self.root.iconify()  
        self.start_time = time.time()
        self.last_frame_time = self.start_time

        if HAS_AUDIO and AUDIO_FILE:
            try:
                pygame.mixer.init()
                pygame.mixer.music.load(AUDIO_FILE)
                pygame.mixer.music.play()
            except Exception as e:
                print(f"Audio failed to load: {e}")

        self.tick()

    def tick(self):
        now = time.time()
        elapsed = now - self.start_time
        dt = now - self.last_frame_time
        self.last_frame_time = now

        # Update debug display
        if DEBUG_MODE:
            self.debug_label.config(text=f"Time: {elapsed:.1f}s | Spawned: {self.next_lyric_idx}/{len(LYRICS)}")

        # Spawn any lyric windows whose time has come
        while (self.next_lyric_idx < len(LYRICS) and
               LYRICS[self.next_lyric_idx][0] <= elapsed):
            t, text = LYRICS[self.next_lyric_idx]
            x = self.random_safe_x()
            y = self.screen_h - BOX_H - BOTTOM_SPAWN_OFFSET
            
            # Determine color based on lyric text
            text_lower = text.lower()
            if "red" in text_lower:
                lyric_color = "#FF0000"  # Red
            elif "green" in text_lower or "그린" in text:
                lyric_color = "#00CC00"  # Green
            else:
                lyric_color = FG_COLOR  # Default color

            if lyric_color != FG_COLOR:
                TrafficGlow(self.root, lyric_color, x + BOX_W // 2, y + BOX_H // 2)

            box = LyricBox(self.root, text, x, y, color=lyric_color)
            self.boxes.append(box)
            self.next_lyric_idx += 1

        # Continuously rise ALL existing boxes upward, every frame
        dy = RISE_SPEED * dt
        for box in self.boxes:
            box.rise(dy)

        # Boxes stay visible permanently; we just stop tracking ones that
        # have scrolled fully off the top of the screen (saves memory),
        # but we never fade or destroy them early.
        still_visible = []
        for box in self.boxes:
            if box.is_offscreen():
                try:
                    box.win.destroy()
                except tk.TclError:
                    pass
            else:
                still_visible.append(box)
        self.boxes = still_visible

        # Keep looping as long as there are lyrics left to show or
        # boxes still on screen
        if self.next_lyric_idx < len(LYRICS) or self.boxes:
            self.root.after(16, self.tick)  # ~60fps


if __name__ == "__main__":
    root = tk.Tk()
    app = LyricFloatApp(root)
    root.mainloop()