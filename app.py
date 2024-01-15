"""This is a flask module."""

from flask import Flask, jsonify, request

from hunter_client import HunterClient, EmailVerificationService

from typing import  Dict, Any

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

import os

app = Flask(__name__)
API_KEY = os.getenv("API_KEY")
hunter_client = HunterClient(api_key=API_KEY)
verification_service = EmailVerificationService()


@app.route('/verify_email', methods=['POST'])
def verify_email() -> jsonify:
    data: Dict[str, Any] = request.get_json()
    email: str = data.get('email', 'example@gmail.com')

    if not email:
        return jsonify({'error': 'Missing email parameter'}), 400

    verification_result: Dict[str, Any] = hunter_client.verify_email(email)
    verification_service.save_result(email, verification_result)

    return jsonify({'email': email, 'result': verification_result})


@app.route('/get_results', methods=['GET'])
def get_results() -> jsonify:
    return jsonify(verification_service.get_results())


@app.route('/clear_results', methods=['POST'])
def clear_results() -> jsonify:
    verification_service.clear_results()
    return jsonify({'message': 'Results cleared successfully'})


if __name__ == '__main__':
    app.run(debug=False)
