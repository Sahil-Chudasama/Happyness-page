from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles  # 1. CRITICAL: Import StaticFiles

app = FastAPI()

# 2. CRITICAL: Mount the static directory to serve your song
app.mount("/static", StaticFiles(directory="static"), name="static")

html_content = """
<html>
    <head>
        <title>Will You Marry Me, Khushi? 💍</title>
        <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@300;700&display=swap" rel="stylesheet">
        <style>
            :root {
                --primary-color: #e53995; /* Deep Rose Pink for drama */
                --secondary-color: #ff69b4; /* Hot Pink for hearts */
                --background-light: #fff0f5; /* Lavender Blush */
            }
            body {
                /* SOFT GRADIENT BACKGROUND (as requested) */
                background: linear-gradient(135deg, var(--background-light) 0%, #ffe4e1 100%); 
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
                padding: 40px;
                margin: 60px auto 0;
                max-width: 700px;
                box-shadow: 0 10px 40px rgba(229, 57, 149, 0.5);
                position: relative;
                z-index: 10;
            }
            /* The BIG Proposal Question */
            h1 {
                font-family: 'Pacifico', cursive;
                font-size: 5.5em; 
                font-weight: normal;
                margin-top: 0;
                color: var(--primary-color);
                text-shadow: 0 0 20px #fff, 0 0 40px var(--secondary-color), 0 0 60px var(--primary-color);
                animation: pulse 1.5s infinite alternate; 
            }
            /* The build-up line (typing effect) */
            #typed-message {
                font-size: 1.8em;
                font-weight: 300;
                min-height: 30px;
                animation: fadeIn 2s ease-in-out;
                color: #555; 
            }
            /* The supportive declaration */
            p {
                font-size: 1.6em; 
                line-height: 1.6;
                margin-top: 30px;
                font-weight: 700; 
                color: #4a4a4a;
            }
            @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
            @keyframes pulse { 0% { transform: scale(1); } 100% { transform: scale(1.04); } }

            /* --- FLOATING HEART FIX: CSS variables must be defined here --- */
            .heart {
                position: fixed;
                color: var(--secondary-color);
                animation: floatUp var(--duration) linear infinite; /* Uses CSS variable */
                font-size: var(--size); /* Uses CSS variable */
                opacity: 0.8;
                pointer-events: none;
                z-index: -1;
            }
            @keyframes floatUp {
                0% { transform: translateY(110vh) translateX(0) rotate(0deg); opacity: 1; }
                50% { transform: translateY(50vh) translateX(var(--drift)) rotate(180deg); } /* Uses CSS variable */
                100% { transform: translateY(-10vh) translateX(0) rotate(360deg); opacity: 0; }
            }

            /* --- Responsive Design for Mobile --- */
            @media (max-width: 600px) {
                h1 { font-size: 3.5em; }
                #typed-message { font-size: 1.4em; }
                p { font-size: 1.2em; }
                .content-box { margin-top: 30px; padding: 25px; }
            }
        </style>
    </head>
    <body>
        <div class="content-box">
            <h1>💖 Will You Marry Me? 💖</h1>

            <h2 id="typed-message"></h2> 

            <p>
                💍I love you, Khushi, now and forever.💍
            </p>
        </div>

        <audio id="myAudio" autoplay loop>
            <source src="/static/adio.mp3" type="audio/mpeg">
        </audio>

        <script>
            // --- Typing Effect Script ---
            document.addEventListener("DOMContentLoaded", function() {
                // The dramatic line
                const textToType = "From the moment I met you, I knew you were my forever.";
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

            // --- FLOATING HEART FIX: JavaScript must set the CSS variables ---
            function createHeart() {
                const heart = document.createElement("div");
                const symbols = ["❤️", "💖", "✨", "🌸", "💕", "💞"];
                const randomSymbol = symbols[Math.floor(Math.random() * symbols.length)];

                // Set dynamic properties for size, duration, and drift
                const size = Math.random() * 10 + 16;
                const duration = Math.random() * 4 + 6;
                const drift = (Math.random() - 0.5) * 50 + "px";

                heart.className = "heart";
                heart.innerHTML = randomSymbol;

                // CRITICAL: Inject variables into the element's style
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