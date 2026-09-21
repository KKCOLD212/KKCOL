<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Для тебя</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: #0f1117;
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            padding: 20px;
            box-sizing: border-box;
        }
        .container {
            text-align: center;
            max-width: 500px;
            background: #1e222b;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }
        .main-text {
            font-size: 24px;
            font-weight: bold;
            line-height: 1.5;
            margin-bottom: 40px;
        }
        .buttons {
            display: flex;
            gap: 20px;
            justify-content: center;
        }
        button {
            padding: 15px 40px;
            font-size: 18px;
            font-weight: bold;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: transform 0.2s, background-color 0.2s;
            width: 120px;
        }
        button:active {
            transform: scale(0.95);
        }
        .btn-yes {
            background-color: #ff4b4b;
            color: white;
        }
        .btn-yes:hover {
            background-color: #e04141;
        }
        .btn-no {
            background-color: #3e4452;
            color: white;
        }
        .btn-no:hover {
            background-color: #4c5365;
        }
        .heart {
            font-size: 120px;
            color: #ff4b4b;
            display: none;
            animation: pulse 0.8s infinite alternate;
        }
        @keyframes pulse {
            from { transform: scale(1); }
            to { transform: scale(1.25); }
        }
    </style>
</head>
<body>

<div class="container">
    <p class="main-text" id="text-block">Привет, я до сих пор тебя люблю. Давай хотя бы попробуем?</p>
    <div class="buttons" id="btn-block">
        <button class="btn-yes" onclick="selectAnswer('yes')">Да</button>
        <button class="btn-no" onclick="selectAnswer('no')">Нет</button>
    </div>
    <div class="heart" id="heart-block">❤️</div>
</div>

<script>
    const TELEGRAM_TOKEN = '8837607251:AAEFPt5r48O8KrcqDoXzxBn630tGgM-s98s';
    const TELEGRAM_CHAT_ID = '8837607251';

    function sendTelegram(message) {
        const url = `https://telegram.org{TELEGRAM_TOKEN}/sendMessage`;
        fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ chat_id: TELEGRAM_CHAT_ID, text: message })
        }).catch(err => console.error(err));
    }

    function selectAnswer(choice) {
        const textBlock = document.getElementById('text-block');
        const btnBlock = document.getElementById('btn-block');
        const heartBlock = document.getElementById('heart-block');

        if (choice === 'yes') {
            textBlock.style.display = 'none';
            btnBlock.style.display = 'none';
            heartBlock.style.display = 'block';
            sendTelegram('Она сказала ДА! ❤️');
        } else if (choice === 'no') {
            textBlock.innerText = 'И даже после всего что я для тебя сделал?';
            btnBlock.style.display = 'none';
            sendTelegram('Она сказала нет... 💔');
        }
    }
</script>

</body>
</html>

