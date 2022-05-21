from colorama import Fore
from colorama import Style
from flask import Flask
from threading import Thread
 
app = Flask('')
 
@app.route('/')
def main():
    html = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Akaza-V2</title>
</head>
<body>
    <h2>Bot running...</h2>
    <div class="progress">
		<progress id="bar" max="91" value="100"></progress>
		<span></span>
		</div>
    <style>
        h2 {
            color: #1ED442;
        }
    </style>
    <script type="text/javascript"> 

        window.onload = function() { 
            
            animateprogress("#bar",91);
            
        };
    </script>
</body>
</html>'''
    return str(html)
  
def run():
  app.run(host="0.0.0.0", port=8000)
 
def keep_alive():
    server = Thread(target=run)
    server.start()
    print(Fore.GREEN + "--------------- ONLINE ---------------" + Style.RESET_ALL)
