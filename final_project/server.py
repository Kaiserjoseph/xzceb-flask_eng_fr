from machinetranslation import translator
from flask import Flask, render_template, request
import json

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    transTest = translator.english_to_french(textToTranslate) # Write your code here
    return transTest

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    transTest = translator.french_to_english(textToTranslate) # Write your code here
    return transTest

@app.route("/")
def renderIndexPage():
    return render_template("index.html")# Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)