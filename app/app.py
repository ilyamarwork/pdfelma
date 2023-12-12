from flask import Flask, request, jsonify
from services import convert_to_pdf_service

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health(): 
    return jsonify(
        status = 'UP'
    )

@app.route("/convert", methods=['POST'])
def convert():
    try:
        data = request.get_json(silent=True)
        filename, output_base64 = convert_to_pdf_service(data)
        return jsonify(
            status = 'Success',
            message = 'Converted to PDF',
            filename = filename,
            output_base64 = output_base64
        )
    except Exception as e:
            return jsonify(
                status = 'Error',
                message = str(e)
            ) , 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

