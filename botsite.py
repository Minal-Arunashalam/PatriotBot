from flask import Flask, render_template, url_for, request, redirect
from pbot import get_info, respond
from ai import primeAI

app = Flask(__name__)

# @app.route("/", methods=["POST", "GET"])
# def home(info=None, question=None):
#     if request.method == "POST":
#         try:
#             quest = request.form.get("question")
#             #print(quest)
#             scraped_data = get_info("https://www.gmu.edu/student-life/where-eat")
#         except Exception:
#             return render_template("index.html", info=None, question=None)
        
#         return redirect(url_for("response", info=scraped_data, question=quest))
    
#     else:
#         return render_template("index.html", info=None, question=None)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/response", methods=["POST", "GET"])
def response(question=None):
    if request.method == "POST":
        question = request.form.get("user_input")

        links = [
        "https://www.gmu.edu/student-life/where-eat",
        "https://www.gmu.edu/student-life/health-and-wellness",
        "https://www.gmu.edu/student-life/activities-and-events",
        "https://www.gmu.edu/student-life/recreation",
        "https://www.gmu.edu/student-life/housing",
        "https://www.gmu.edu/academics/undergraduate-programs",
        ]

        # Loop through the links and call get_info for each one
        for link in links:
            info = get_info(link)
            primeAI(info)

        # info = get_info("https://www.gmu.edu/student-life/where-eat")
        bot_response = respond(question)
        
        return render_template("response.html", response=bot_response)
    
    else:
        return render_template("response.html", response="Ask something!")

# @app.route("/response")
# @app.route("/response/<string:q>")
# def response(q=None):
#         return render_template("response.html", response=q)
    



if __name__ == "__main__":
    app.run(debug=True)