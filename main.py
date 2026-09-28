import textwrap
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# 1. Initialize the FastAPI app
app = FastAPI(
    title="💖 Love Message App 💖",
    description="A romantic FastAPI app for Khushi."
)

# 2. Mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# 3. HTML Content Generator
def get_khushi_html_content() -> str:
    html_content = textwrap.dedent("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>For Khushi ❤️</title>
            <!-- Canvas Confetti Library -->
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
            <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
            
            <style>
                :root {
                    --primary-color: #ff2a5f;
                    --secondary-color: #ff758f;
                    --bg-light: #fff0f5;
                }
                * { box-sizing: border-box; margin: 0; padding: 0; }
                body {
                    background: linear-gradient(135deg, var(--bg-light) 0%, #ffe4e1 100%);
                    font-family: 'Poppins', sans-serif;
                    text-align: center;
                    padding: 30px 15px;
                    min-height: 100vh;
                    overflow-x: hidden;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
                .content-box {
                    background-color: rgba(255, 255, 255, 0.75);
                    background-image: url('/static/khushi_photo.jpg?v=2');
                    background-size: cover;
                    background-position: center;
                    background-repeat: no-repeat;
                    background-blend-mode: overlay;
                    border-radius: 25px;
                    padding: 35px 25px;
                    max-width: 650px;
                    width: 100%;
                    box-shadow: 0 15px 35px rgba(255, 42, 95, 0.25);
                    position: relative;
                    z-index: 1;
                }
                h1 {
                    font-family: 'Dancing Script', cursive;
                    font-size: 3.5rem;
                    color: var(--primary-color);
                    text-shadow: 0 0 10px rgba(255, 42, 95, 0.2);
                    margin-bottom: 5px;
                }
                #typed-message {
                    font-size: 1.2rem;
                    color: #555;
                    min-height: 30px;
                    margin-bottom: 20px;
                    font-weight: 600;
                }
                
                /* Relationship Counter */
                .counter-box {
                    background: rgba(255, 240, 243, 0.9);
                    border: 1px dashed var(--secondary-color);
                    border-radius: 15px;
                    padding: 15px;
                    margin: 20px 0;
                }
                .counter-title {
                    font-size: 0.9rem;
                    color: var(--primary-color);
                    font-weight: 700;
                    text-transform: uppercase;
                    margin-bottom: 8px;
                }
                .timer {
                    display: flex;
                    justify-content: space-around;
                }
                .time-unit span:first-child {
                    font-size: 1.4rem;
                    font-weight: 700;
                    color: var(--primary-color);
                }
                .time-unit span:last-child {
                    font-size: 0.75rem;
                    color: #666;
                }

                /* Photo Flip Cards */
                .gallery-title {
                    font-size: 1rem;
                    color: var(--primary-color);
                    margin: 15px 0 10px 0;
                    font-weight: 700;
                }
                .cards-grid {
                    display: flex;
                    justify-content: center;
                    gap: 12px;
                    margin-bottom: 25px;
                    flex-wrap: wrap;
                }
                .flip-card {
                    width: 120px;
                    height: 140px;
                    perspective: 1000px;
                    cursor: pointer;
                }
                .flip-card-inner {
                    position: relative;
                    width: 100%;
                    height: 100%;
                    text-align: center;
                    transition: transform 0.6s;
                    transform-style: preserve-3d;
                    border-radius: 12px;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                }
                .flip-card:hover .flip-card-inner, .flip-card.flipped .flip-card-inner {
                    transform: rotateY(180deg);
                }
                .flip-card-front, .flip-card-back {
                    position: absolute;
                    width: 100%;
                    height: 100%;
                    backface-visibility: hidden;
                    border-radius: 12px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 8px;
                    font-size: 0.82rem;
                    font-weight: 600;
                }
                .flip-card-front {
                    background-color: #ffb3c1;
                    color: #800f2f;
                }
                .flip-card-back {
                    background-color: var(--primary-color);
                    color: white;
                    transform: rotateY(180deg);
                }

                /* Music Section & Vinyl */
                .music-section {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    gap: 12px;
                    margin-top: 15px;
                }
                .vinyl-container {
                    width: 65px;
                    height: 65px;
                    border-radius: 50%;
                    background: radial-gradient(circle, #333 30%, #111 70%);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    box-shadow: 0 0 10px rgba(0,0,0,0.3);
                }
                .vinyl-center {
                    width: 22px;
                    height: 22px;
                    background: var(--primary-color);
                    border-radius: 50%;
                    border: 2px solid white;
                }
                .spinning {
                    animation: spin 3s linear infinite;
                }
                @keyframes spin { 100% { transform: rotate(360deg); } }

                #music-button {
                    background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
                    color: white;
                    border: none;
                    padding: 12px 28px;
                    border-radius: 50px;
                    cursor: pointer;
                    font-size: 1rem;
                    font-weight: 700;
                    box-shadow: 0 4px 15px rgba(255, 42, 95, 0.4);
                    transition: all 0.3s ease;
                }
                #music-button:hover {
                    transform: scale(1.05);
                }

                .message-p {
                    font-size: 1.1em;
                    line-height: 1.6;
                    margin-top: 20px;
                    font-weight: 600;
                    color: #333;
                }

                /* Floating Hearts */
                .heart {
                    position: fixed;
                    color: var(--secondary-color);
                    animation: floatUp var(--duration) linear infinite;
                    font-size: var(--size);
                    opacity: 0.8;
                    pointer-events: none;
                    z-index: 0;
                }
                @keyframes floatUp {
                    0% { transform: translateY(110vh) rotate(0deg); opacity: 1; }
                    100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
                }
            </style>
        </head>
        <body>
            <div class="content-box">
                <h1>💖 I Love You Khushi 💖</h1>
                <div id="typed-message"></div>

                <!-- Relationship Timer -->
                <div class="counter-box">
                    <div class="counter-title">Together Since 💕</div>
                    <div class="timer">
                        <div class="time-unit"><span id="days">0</span><span>Days</span></div>
                        <div class="time-unit"><span id="hours">0</span><span>Hours</span></div>
                        <div class="time-unit"><span id="minutes">0</span><span>Mins</span></div>
                        <div class="time-unit"><span id="seconds">0</span><span>Secs</span></div>
                    </div>
                </div>

                <!-- Flip Cards -->
                <div class="gallery-title">Tap Cards to Reveal Memories 📸</div>
                <div class="cards-grid">
                    <div class="flip-card" onclick="this.classList.toggle('flipped')">
                        <div class="flip-card-inner">
                            <div class="flip-card-front">Memory 1 👀</div>
                            <div class="flip-card-back">Whenever I looked at you, you would blush 💖</div>
                        </div>
                    </div>
                    <div class="flip-card" onclick="this.classList.toggle('flipped')">
                        <div class="flip-card-inner">
                            <div class="flip-card-front">Memory 2 💃</div>
                            <div class="flip-card-back">Playing Dodhiya Together 💃✨</div>
                        </div>
                    </div>
                    <div class="flip-card" onclick="this.classList.toggle('flipped')">
                        <div class="flip-card-inner">
                            <div class="flip-card-front">Memory 3 🌸</div>
                            <div class="flip-card-back">When you fed me 5-Star 🍫 with your own hands ✨</div>
                        </div>
                    </div>
                    <div class="flip-card" onclick="this.classList.toggle('flipped')">
                        <div class="flip-card-inner">
                            <div class="flip-card-front">Memory 4 🌟</div>
                            <div class="flip-card-back">Whenever you get cute-angry at me "😤😤"</div>
                        </div>
                    </div>
                </div>

                <!-- Music Player -->
                <div class="music-section">
                    <div class="vinyl-container" id="vinyl">
                        <div class="vinyl-center"></div>
                    </div>
                    <button id="music-button">Tap Me to Start the Music 🎵</button>
                </div>

                <p class="message-p">You are the best decision my heart ever made 🌸<br>
                I love you more than words can ever capture ✨<br>
                You are my always 💕</p>
            </div>

            <!-- Static Audio File Reference -->
            <audio id="romantic-song" src="/static/audio.mp3" loop preload="auto"></audio>

            <script>
                document.addEventListener("DOMContentLoaded", function() {
                    // 1. Typing Effect
                    const textToType = "💍 Forever & Always Yours 💍";
                    const element = document.getElementById("typed-message");
                    let i = 0;
                    function typeWriter() {
                        if (i < textToType.length) {
                            element.innerHTML += textToType.charAt(i);
                            i++;
                            setTimeout(typeWriter, 75);
                        }
                    }
                    setTimeout(typeWriter, 500);

                    // 2. Music & Vinyl Spinning
                    const audio = document.getElementById('romantic-song');
                    const musicButton = document.getElementById('music-button');
                    const vinyl = document.getElementById('vinyl');
                    let isPlaying = false;

                    musicButton.addEventListener('click', function() {
                        if (!isPlaying) {
                            audio.play().then(() => {
                                vinyl.classList.add('spinning');
                                musicButton.innerText = "Pause Music ⏸️";
                                isPlaying = true;
                                confetti({
                                    particleCount: 80,
                                    spread: 70,
                                    origin: { y: 0.6 },
                                    colors: ['#ff2a5f', '#ff758f', '#ffb3c1']
                                });
                            });
                        } else {
                            audio.pause();
                            vinyl.classList.remove('spinning');
                            musicButton.innerText = "Tap Me to Start the Music 🎵";
                            isPlaying = false;
                        }
                    });

                    // 3. Relationship Counter (Date: 31 July 2025, 6:30 PM)
                    const startDate = new Date("2025-07-31T18:30:00");
                    function updateTimer() {
                        const now = new Date();
                        const diff = now - startDate;
                        document.getElementById("days").innerText = Math.floor(diff / (1000 * 60 * 60 * 24));
                        document.getElementById("hours").innerText = Math.floor((diff / (1000 * 60 * 60)) % 24);
                        document.getElementById("minutes").innerText = Math.floor((diff / (1000 * 60)) % 60);
                        document.getElementById("seconds").innerText = Math.floor((diff / 1000) % 60);
                    }
                    setInterval(updateTimer, 1000);
                    updateTimer();

                    // 4. Floating Hearts
                    function createHeart() {
                        const heart = document.createElement("div");
                        const symbols = ["❤️", "💖", "✨", "🌸", "💕"];
                        const randomSymbol = symbols[Math.floor(Math.random() * symbols.length)];
                        const duration = Math.random() * 4 + 5;

                        heart.className = "heart";
                        heart.innerHTML = randomSymbol;
                        heart.style.setProperty('--duration', duration + 's');
                        heart.style.setProperty('--size', (Math.random() * 10 + 16) + 'px');
                        heart.style.left = Math.random() * 100 + "vw";

                        document.body.appendChild(heart);
                        setTimeout(() => heart.remove(), duration * 1000);
                    }
                    setInterval(createHeart, 300);
                });
            </script>
        </body>
        </html>
    """)
    return html_content

# 4. FastAPI Endpoints
@app.get("/", response_class=HTMLResponse)
@app.get("/khushi", response_class=HTMLResponse)
def love_message() -> HTMLResponse:
    return HTMLResponse(content=get_khushi_html_content(), status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
