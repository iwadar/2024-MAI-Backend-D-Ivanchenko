HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Приветики</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" integrity="sha384-B0vP5xmATw1+K9KRQjQERJvTumQW0nPEzvF6L/Z6nronJ3oUOFUFpCjEUQouq2+l" crossorigin="anonymous">
</head>
<body class="bg-info">
    <div class="container">
      <h1 class="text-white text-center mx-auto p-2 mt-4 mb-3">{greeting}</h1>
      <h1 class="text-white text-center mx-auto p-2 mt-4 mb-3">Твой IP-адрес</h1>
      <div class="bg-light card-block mx-auto text-center">
        <h1 class="display-3 p-2">{ip_address}</h1>
      </div>
    </div>
  </body>
</html>
"""

def app(environ, start_response):
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/html; charset=utf-8'),
    ]
    start_response(status, response_headers)
    name = 'Привет'
    # environ["REMOTE_ADDR"] = '90.09.09.09'
    if environ["REMOTE_ADDR"] == '127.0.0.1':
        name += ', Даша!'
    else:
        name += ', незнакомец!'
    html = HTML.format(greeting=name, ip_address=environ["REMOTE_ADDR"])
    html_as_bytes = html.encode('utf-8')
    return [html_as_bytes]
