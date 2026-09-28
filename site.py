from flask import Flask, render_template_string, url_for

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Вадим Песков</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: #000;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background-color: #ffe6e6;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
            width: 600px;
            text-align: center;
        }
        .header {
            padding: 15px;
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }
        .content {
            display: flex;
        }
        .photo-section {
            width: 400px;
        }
        .photo {
            width: 100%;
            height: auto;
            display: block;
        }
        .info-section {
            width: 200px;
            background-color: #9c00ff;
            color: white;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        .name {
            font-size: 16px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .footer {
            padding: 10px;
            background-color: #ffe6e6;
            font-size: 12px;
            color: #555;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">Куплю комаров. Продам трёх поросят все разного пола.</div>
        <div class="content">
            <div class="photo-section">
                <!-- Правильная ссылка на статический файл -->
                <img src="{{ url_for('static', filename='photo.jpg') }}" alt="Вадим Песков" class="photo">
            </div>
            <div class="info-section">
                <div class="name">Песков Вадим</div>
            </div>
        </div>
        <div class="footer">Связаться по <a href="https://discord.com/users/pirpiksss">Discord</a>
 или через <a href="https://vk.ru/id362021479">ВК</a>
 </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
