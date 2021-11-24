from pprint import pprint
from flask import Flask, request, jsonify
import vonage


fromm= "" # Enter Your name
key = ""
secret = ""

app = Flask(__name__)
client = vonage.Client(key=key, secret=secret)
sms = vonage.Sms(client)

persons = {"cayla": "6969696969", "john": "6969696969", "greg": "6969696969", "ben": "6969696969"}

@app.route("/next", methods=['GET'])
def check():
    file_ = open("codes.csv", "r")
    codes = file_.read().split(",")
    file_.close()
    yes = False
    number = persons[request.args.get("person")]
    message = request.args.get("message")
    code = request.args.get("code")
    if code in codes:
        yes = True
    else:
        return "Incorrect Code!", 404
    if yes == True:
        codes = [value for value in codes if value != code]
        file_ = open("codes.csv", "w")
        file_.write(",".join(codes))
        file_.close()
        responseData = sms.send_message(
            {
                "from": fromm,
                "to": number,
                "text": message.replace(r"\n", "\n"),
            }
        )
        return responseData



if __name__ == '__main__':
    app.run(host="0.0.0.0")
    
