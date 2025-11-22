import textwrap
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# 1. Initialize the FastAPI app
app = FastAPI(
    title="💖 Love Message App 💖",
    description="A simple, romantic FastAPI app for Khushi."
)

# 2. Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")


# 3. Function to generate the HTML content
def get_khushi_html_content() -> str:
    """
    Generates the full HTML content for the love message page,
    including a background image and a button to start the music.
    """

    html_content = textwrap.dedent("""
        <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>For Khushi ❤️</title>
                <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@300;700&display=swap" rel="stylesheet">
                <style>
                    :root {
                        --primary-color: #ff1493; /* Deep Pink */
                        --secondary-color: #ff69b4; /* Hot Pink */
                        --background-light: #fff0f5; /* Lavender Blush */
                        --text-color: #4a4a4a;
                    }
                    body {
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
                        /* --- BACKGROUND IMAGE CODE ADDED HERE --- */
                        background-color: rgba(255, 255, 255, 0.85); /* Slightly less opaque white for blend */
                        background-image: url('/static/khushi_photo.jpg'); /* Ensure your photo is named khushi_photo.jpg in the static folder */
                        background-size: cover; /* Cover the entire box */
                        background-position: center; /* Center the image */
                        background-repeat: no-repeat;
                        background-blend-mode: overlay; /* Blends the image softly with the white color for better readability */
                        /* -------------------------------------- */

                        border-radius: 25px;
                        padding: 30px;
                        margin: 0 auto;
                        max-width: 800px;
                        box-shadow: 0 10px 30px rgba(255, 20, 147, 0.3), 0 0 50px rgba(255, 20, 147, 0.15);
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
                        display: block; /* Ensure it takes up space */
                    }
                    p {
                        font-size: 1.2em;
                        line-height: 1.6;
                        margin-top: 30px;
                        font-weight: 700; /* Bolding text slightly for better readability over image */
                        color: var(--text-color);
                    }
                    #music-button {
                        background-color: var(--secondary-color);
                        color: white;
                        border: none;
                        padding: 12px 25px;
                        border-radius: 50px;
                        cursor: pointer;
                        font-size: 1.1em;
                        font-weight: 700;
                        margin-top: 25px;
                        box-shadow: 0 4px 15px rgba(255, 105, 180, 0.6);
                        transition: all 0.3s ease;
                        letter-spacing: 0.5px;
                    }
                    #music-button:hover {
                        background-color: var(--primary-color);
                        transform: translateY(-2px);
                        box-shadow: 0 6px 20px rgba(255, 20, 147, 0.4);
                    }

                    @keyframes fadeIn {
                        from { opacity: 0; }
                        to { opacity: 1; }
                    }
                    @keyframes pulse {
                        0% { transform: scale(1); }
                        100% { transform: scale(1.03); }
                    }
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
                    @media (max-width: 600px) {
                        h1 {
                            font-size: 2.8em;
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
                    <h1>💖 I Love You Khushi 💖</h1>
                    <h2 id="typed-message"></h2>

                    <button id="music-button">Tap Me to Start the Music 🎵</button>
                    <p>You are the most beautiful part of my life 🌸<br>
                    Whenever you smile, the whole world feels brighter ✨<br>
                    You are my happiness, my heart, and my forever 💕</p>
                </div>

                <audio id="romantic-song" preload="auto" loop style="display: none;">
                    <source src="/static/adio.mp3" type="audio/mpeg">
                    Your browser does not support the audio element.
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
                                setTimeout(typeWriter, 75);
                            }
                        }
                        setTimeout(typeWriter, 1000);

                        // --- Music Play Script (Activated by button click) ---
                        const audio = document.getElementById('romantic-song');
                        const musicButton = document.getElementById('music-button');

                        musicButton.addEventListener('click', function() {
                            audio.play()
                                .then(() => {
                                    // If successful, hide the button so she knows the music is playing
                                    musicButton.style.display = 'none';
                                })
                                .catch(error => {
                                    console.error("Audio playback error:", error);
                                    musicButton.innerText = "Error: Music blocked. Try clicking again!";
                                });
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
    """)
    return html_content


# 4. Define the Endpoint
@app.get("/", response_class=HTMLResponse)
@app.get("/khushi", response_class=HTMLResponse)
def love_message() -> HTMLResponse:
    """
    Serves the romantic HTML page for Khushi.
    """
    html_content = get_khushi_html_content()
    return HTMLResponse(content=html_content, status_code=200)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)