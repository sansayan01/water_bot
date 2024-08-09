# H2O The Water Bot

H2O The Water Bot is a friendly assistant specializing in water and sanitation. This chatbot is built using Python with Flask for the backend and Google's Generative AI for the chatbot responses. The frontend is developed using HTML, CSS, and JavaScript.

## Requirements

- Python 3.7 or higher
- The following Python packages:
  - Flask
  - google-generativeai
  - requests

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/H2O-water-bot.git
    cd H2O-water-bot
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Add your Google Generative AI API key:**

    Open the `main.py` file and replace the placeholder `your_google_api_key` with your actual Google Generative AI API key.

## Usage

1. **Run the application:**

    ```bash
    python main.py
    ```

2. **Access the chatbot in your web browser:**

    The application will automatically open in your default web browser. If it doesn't, navigate to `http://127.0.0.1:5000` in your browser.

3. **Interact with the chatbot:**

    - Type your message in the input box and press Enter or click the Send button.
    - The chatbot will respond, and the conversation will be displayed on the screen.

## Project Structure

- `main.py`: The main Python script that runs the Flask server and handles chat interactions.
- `templates/index.html`: The HTML file for the frontend.
- `static/`: Directory containing static files (CSS, JavaScript).
- `requirements.txt`: List of Python packages required for the project.
- `README.md`: This file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Google Generative AI](https://ai.google.dev/gemini-api/docs/get-started/python)

## Contact

If you have any questions or suggestions, feel free to reach out to [your email or contact information].
