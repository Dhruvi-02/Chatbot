from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_reply(message):
    msg = message.lower()

    if "hello" in msg or "hi" in msg:
        return "Hello! How can I help you?"

    elif "python" in msg:
        return "Python is a programming language used for AI, ML, and web development."

    elif "ai" in msg:
        return "AI means making machines smart so they can think and learn."

    elif "ml" in msg:
        return "Machine Learning is a part of artificial intelligence where computers learn from data and improve without being explicitly programmed."

    elif "bye" in msg:
        return "Goodbye!"

    else:
        return "Sorry, I don't understand that yet. I'm still in developing phase."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    reply = get_reply(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)