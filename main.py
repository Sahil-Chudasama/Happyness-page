from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles  # 1. ADD: Import StaticFiles

app = FastAPI()

# 2. ADD: Mount the static directory to serve adio.mp3
# This makes files in the 'static' folder accessible at /static/
app.mount("/static", StaticFiles(directory="static"), name="static")

html_content = """
<html>
    <head>
        <title>For Khushi ❤️</title>
        <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@300;700&display=swap" rel="stylesheet">
        <style>
            :root {
                --primary-color: #ff1493; /* Deep Pink */
                --secondary-color: #ff69b4; /* Hot Pink */
                --background-light: #fff0f5; /* Lavender Blush */
            }
            body {
                background: linear-gradient(135deg, var(--background-light) 0%, #ffe4e1 100%); /* Subtle Gradient */
                font-family: 'Poppins', sans-serif;
                text-align: center;
                padding: 40px 20px;
                color: var(--primary-color);
                min-height: 100vh;
                margin: 0;
                overflow-x: hidden;
            }
            .content-box {
                background-color: rgba(255, 255, 255, 0.95);
                border-radius: 25px;
                padding: 30px;
                margin: 0 auto;
                max-width: 800px;
                box-shadow: 0 10px 30px rgba(255, 20, 147, 0.3), 0 0 50px rgba(255, 20, 147, 0.15);
                position: relative;
                z-index: 10;
            }
            h1 {
                font-family: 'Pacifico', cursive;
                font-size: 4.5em;
                font-weight: normal;
                margin-top: 0;
                color: var(--primary-color);
                text-shadow: 0 0 15px var(--secondary-color), 0 0 5px var(--primary-color);
                animation: pulse 2s infinite alternate;
            }
            #typed-message {
                font-size: 1.8em;
                font-weight: 300;
                min-height: 30px;
                animation: fadeIn 2s ease-in-out;
            }
            p {
                font-size: 1.2em;
                line-height: 1.6;
                margin-top: 30px;
                font-weight: 300;
                color: #4a4a4a;
            }
            @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
            @keyframes pulse { 0% { transform: scale(1); } 100% { transform: scale(1.03); } }

            /* --- Floating Heart Styles (from previous version) --- */
            .heart {
                position: fixed;
                color: var(--secondary-color);
                animation: floatUp var(--duration) linear infinite;
                font-size: var(--size);
                opacity: 0.8;
                pointer-events: none;
                z-index: -1;
            }
            @keyframes floatUp {
                0% { transform: translateY(110vh) translateX(0) rotate(0deg); opacity: 1; }
                50% { transform: translateY(50vh) translateX(var(--drift)) rotate(180deg); }
                100% { transform: translateY(-10vh) translateX(0) rotate(360deg); opacity: 0; }
            }

            /* --- Play Button Styles --- */
            #playMusicBtn {
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                padding: 18px 35px;
                font-size: 1.3em;
                font-family: 'Pacifico', cursive;
                color: white;
                background-color: var(--primary-color);
                border: 2px solid white;
                border-radius: 50px;
                cursor: pointer;
                z-index: 1000;
                box-shadow: 0 5px 20px rgba(0,0,0,0.4);
                transition: opacity 0.5s, transform 0.5s;
                letter-spacing: 1px;
            }
            #playButtonContainer.fade-out {
                opacity: 0;
                pointer-events: none;
            }

            /* --- Responsive Design for Mobile --- */
            @media (max-width: 600px) {
                h1 { font-size: 2.8em; }
                #typed-message { font-size: 1.2em; }
                .content-box { padding: 20px 15px; border-radius: 15px; }
                #playMusicBtn { padding: 12px 25px; font-size: 1em; }
            }
        </style>
    </head>
    <body>
        <div class="content-box">
            <h1>💖 I LOVE YOU KHUSHI 💖</h1>
            <h2 id="typed-message"></h2> <p>You are the most beautiful part of my life 🌸<br>
            Whenever you smile, the whole world feels brighter ✨<br>
            You are my happiness, my heart, and my forever 💕</p>
        </div>

        <audio id="myAudio" loop>
            <source src="/static/adio.mp3" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>

        <div id="playButtonContainer">
            <button id="playMusicBtn">Click to Start the Music! 🎶</button>
        </div>


        <script>
            // --- Typing Effect Script ---
            document.addEventListener("DOMContentLoaded", function() {
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
                setTimeout(typeWriter, 1000);
            });

            // --- Interactive Play Button Script ---
            document.addEventListener("DOMContentLoaded", function() {
                const audio = document.getElementById('myAudio');
                const playButtonContainer = document.getElementById('playButtonContainer');
                const playButton = document.getElementById('playMusicBtn');

                playButton.addEventListener('click', () => {
                    audio.play().catch(error => {
                        console.error("Audio playback failed:", error);
                    });

                    // Start the fade-out effect
                    playButtonContainer.classList.add('fade-out');

                    // Remove the element completely after the transition ends
                    setTimeout(() => playButtonContainer.remove(), 500); 
                });
            });


            // --- Floating Hearts Script ---
            function createHeart() {
                const heart = document.createElement("div");
                const symbols = ["❤️", "💖", "✨", "🌸", "💕", "💞"];
                const randomSymbol = symbols[Math.floor(Math.random() * symbols.length)];

                const size = Math.random() * 10 + 16;
                const duration = Math.random() * 4 + 6;
                const drift = (Math.random() - 0.5) * 50 + "px";

                heart.className = "heart";
                heart.innerHTML = randomSymbol;

                heart.style.setProperty('--duration', duration + 's');
                heart.style.setProperty('--size', size + 'px');
                heart.style.setProperty('--drift', drift);

                heart.style.left = Math.random() * 100 + "vw";
                heart.style.animationDelay = (Math.random() * 2) + "s";

                document.body.appendChild(heart);
                setTimeout(() => heart.remove(), duration * 1000);
            }
            setInterval(createHeart, 250);
        </script>
    </body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
@app.get("/khushi", response_class=HTMLResponse)
def love_message():
    return html_content