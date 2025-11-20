from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

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
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 25px;
                padding: 30px;
                margin: 0 auto;
                max-width: 800px;
                box-shadow: 0 10px 30px rgba(255, 20, 147, 0.3), 0 0 50px rgba(255, 20, 147, 0.15); /* Soft pink shadow */
            }
            h1 {
                font-family: 'Pacifico', cursive; /* Use the fancy font for the main message */
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
                min-height: 30px; /* Prevent layout shift while typing */
                animation: fadeIn 2s ease-in-out;
            }
            p {
                font-size: 1.2em;
                line-height: 1.6;
                margin-top: 30px;
                font-weight: 300;
                color: #4a4a4a; /* Darker text for readability */
            }
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            @keyframes pulse {
                0% { transform: scale(1); }
                100% { transform: scale(1.03); }
            }
            /* --- Floating Heart Styles --- */
            .heart {
                position: fixed;
                color: var(--secondary-color);
                animation: floatUp var(--duration) linear infinite;
                font-size: var(--size);
                opacity: 0.8;
                pointer-events: none;
                z-index: -1; /* Place hearts behind content */
            }
            @keyframes floatUp {
                0% { transform: translateY(110vh) translateX(0) rotate(0deg); opacity: 1; }
                50% { transform: translateY(50vh) translateX(var(--drift)) rotate(180deg); }
                100% { transform: translateY(-10vh) translateX(0) rotate(360deg); opacity: 0; }
            }

            /* --- Responsive Design for Mobile --- */
            @media (max-width: 600px) {
                h1 {
                    font-size: 2.8em; /* Smaller on small screens */
                    padding-top: 20px;
                }
                #typed-message {
                    font-size: 1.2em;
                }
                .content-box {
                    padding: 20px 15px;
                    border-radius: 15px;
                }
            }
        </style>
    </head>
    <body>
        <div class="content-box">
            <h1>💖 My Dearest Khushi 💖</h1>
            <h2 id="typed-message"></h2>
            <p>You are the most beautiful part of my life 🌸<br>
            Whenever you smile, the whole world feels brighter ✨<br>
            You are my happiness, my heart, and my forever 💕</p>
        </div>

        <audio autoplay loop>
            <source src="https://www.bensound.com/bensound-music/bensound-romantic.mp3" type="audio/mpeg">
        </audio>

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
                        setTimeout(typeWriter, 75); // Speed of typing
                    }
                }
                setTimeout(typeWriter, 1000); // Start typing after 1 second
            });

            // --- Floating Hearts Script ---
            function createHeart() {
                const heart = document.createElement("div");
                const symbols = ["❤️", "💖", "✨", "🌸", "💕", "💞"]; // Varied symbols
                const randomSymbol = symbols[Math.floor(Math.random() * symbols.length)];

                // Random properties for a better effect
                const size = Math.random() * 10 + 16; // 16px to 26px
                const duration = Math.random() * 4 + 6; // 6s to 10s
                const drift = (Math.random() - 0.5) * 50 + "px"; // Slight horizontal drift

                heart.className = "heart";
                heart.innerHTML = randomSymbol;

                // Set CSS variables for animation
                heart.style.setProperty('--duration', duration + 's');
                heart.style.setProperty('--size', size + 'px');
                heart.style.setProperty('--drift', drift);

                heart.style.left = Math.random() * 100 + "vw";
                heart.style.animationDelay = (Math.random() * 2) + "s"; // Stagger start times

                document.body.appendChild(heart);
                setTimeout(() => heart.remove(), duration * 1000); // Remove after animation ends
            }
            setInterval(createHeart, 250); // Create a new heart every 250ms
        </script>
    </body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
@app.get("/khushi", response_class=HTMLResponse)
def love_message():
    return html_content