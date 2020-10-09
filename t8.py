import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def primo_number():
    number = 3
    inicio = 1
    prime = "2, "

    while inicio != 100:
        isprime = 0
        for i in range(2, number):
            if number % i == 0:
                isprime = 1
                break
        if isprime:
            prime = prime + str(number) + ", "
            inicio += 1
        number += 1
    return prime

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
