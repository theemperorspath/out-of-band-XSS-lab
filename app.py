from flask import Flask, request, jsonify, render_template_string, make_response
import time
from admin_bot import start_bot_thread

app = Flask(__name__)

STORED_PAYLOADS = []


@app.route("/")
def index():
    resp = make_response("""
        <h1>Blind XSS Lab</h1>
        <p>Submit a raw XSS payload. The admin bot will execute it with real cookies.</p>
        <form method="POST" action="/submit">
            <textarea name="payload" style="width:400px;height:120px" placeholder="<script>..."></textarea><br><br>
            <button>Submit</button>
        </form>
    """)

    # Give visitor a dummy user cookie (NOT admin)
    resp.set_cookie("sessionid", "USER-" + str(int(time.time())))
    return resp


@app.route("/submit", methods=["POST"])
def submit():
    payload = request.form.get("payload", "").strip()
    if not payload:
        return "No payload supplied."
    STORED_PAYLOADS.append(payload)
    return "Payload stored! Admin will review it."


@app.route("/admin/pending")
def admin_pending():
    return jsonify(STORED_PAYLOADS)


@app.route("/admin/review/<int:idx>")
def admin_review(idx):
    cookie = request.cookies.get("sessionid", "")

    if not cookie.startswith("ADMIN-"):
        return "403 — Admins only."

    try:
        payload = STORED_PAYLOADS[idx]
    except:
        return "Invalid payload index"

    template = f"""
    <html>
    <body>
        <h3>Admin Reviewing Payload #{idx}</h3>
        <p>Admin Cookie: {cookie}</p>
        <div>{payload}</div>
    </body>
    </html>
    """

    return render_template_string(template)


# Auto-start bot on server launch
start_bot_thread()

if __name__ == "__main__":
    print("[LAB] Running on http://127.0.0.1:5000")
    app.run()
