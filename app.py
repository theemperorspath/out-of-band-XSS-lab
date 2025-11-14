from flask import Flask, request, jsonify, render_template_string, make_response
import time
from admin_bot import start_bot_thread

app = Flask(__name__)

STORED_PAYLOADS = []

# MAIN FLAG (Only visible to admin)
MAIN_FLAG = "THM{blind_xss_master}"


@app.route("/")
def index():
    resp = make_response("""
        <h1>Blind XSS Lab by 0days</h1>
        <p>Submit a raw XSS payload. The admin bot will execute it with real cookies.</p>

        <form method="POST" action="/submit">
            <textarea name="payload" style="width:400px;height:120px" placeholder="<script>..."></textarea><br><br>
            <button>Submit</button>
        </form>
    """)

    # Give visitors a dummy user cookie
    resp.set_cookie("sessionid", "USER-" + str(int(time.time())))
    return resp


@app.route("/submit", methods=["POST"])
def submit():
    payload = request.form.get("payload", "").strip()
    if not payload:
        return "No payload supplied."
    STORED_PAYLOADS.append(payload)
    return "Payload stored! Admin will review it shortly."


@app.route("/admin/pending")
def admin_pending():
    return jsonify(STORED_PAYLOADS)


@app.route("/admin/review/<int:idx>")
def admin_review(idx):
    # Only admin bot should have this cookie
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


# -------------------------------
# NEW SECRET ENDPOINT FOR THE FLAG
# -------------------------------

@app.route("/secret")
def secret_flag():
    """
    This endpoint holds the MAIN FLAG for the TryHackMe room.
    It only returns the flag if the requester has the admin cookie.
    """

    cookie = request.cookies.get("sessionid", "")

    # Only the admin bot will ever have one
    if cookie.startswith("ADMIN-"):
        return f"<h1>{MAIN_FLAG}</h1>"

    return "403 — Forbidden. This area is restricted to admin staff."


# Auto-start admin bot at boot
start_bot_thread()


if __name__ == "__main__":
    print("[LAB] Running on http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000)
