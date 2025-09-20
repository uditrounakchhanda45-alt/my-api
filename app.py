from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/like', methods=['GET'])
def like():
    response = {
        "LikesGivenByAPI": 0,
        "LikesafterCommand": 348,
        "LikesbeforeCommand": 348,
        "PlayerLevel": "32",
        "PlayerNickname": "ᴍʀㅤᴜᴅɪᴛㅤ143ㅤ",
        "PlayerRegion": "IND",
        "UID": "10135553162",
        "owner": "@mr_udit_ff",
        "channel": "@UditGaming45",
        "group": "@UDIT_LIKE_GROUP",
        "status": 2
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
