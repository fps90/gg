from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/run-python", methods=["POST"])
def run_python():
    data = request.get_json()
    code = data.get("code", "")

    try:
        # تشغيل كود Python المدخل
        result = subprocess.run(["python3", "-c", code], capture_output=True, text=True, timeout=5)
        output = result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        output = f"خطأ: {str(e)}"

    return jsonify({"output": output})

if __name__ == "__main__":
    app.run(debug=True)
