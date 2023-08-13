import Score
from flask import Flask, render_template

import Utils


def score_server(difficulty):
    score = Score.add_score(difficulty)
    error = Utils.BAD_RETURN_CODE

    try:
        response = 'The score is <div id="score">'+str(score)+'</div>'
    except:
        response = '<div id="score" style="color:red">'+str(error)+'</div>'

    return """<html>
    <head>
    <title>Scores Game</title>
    </head>
    <body>
    <body>
    <h1>"""+response+"""</h1>
    </body>
    </html>"""