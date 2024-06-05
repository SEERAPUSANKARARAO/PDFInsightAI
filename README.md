Certainly! Here's an updated README file for your project:

---

# PDFInsight AI 📚🤖

Welcome to **PDFInsight AI**, your intelligent assistant for interacting with multiple PDFs using the power of AI. Ask questions, retrieve information, and gain insights effortlessly from your documents.

## 🌟 Features

- **Multi-PDF Support:** Upload and process multiple PDFs simultaneously.
- **AI Models Integration:** Choose between OpenAI and Google AI for text understanding.
- **Conversational Context Handling:** Maintain the flow of conversation with context-aware responses.
- **Downloadable History:** Export your conversation history as a CSV file for future reference.

## 🚀 Getting Started

Follow these instructions to set up and run PDFInsight AI on your local machine.

### Prerequisites

- Python 3.7+
- Streamlit

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/PDFInsightAI.git
    cd PDFInsightAI
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file and add your API keys:**

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key_here
    GOOGLE_API_KEY=your_google_api_key_here
    ```

### Usage

1. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

2. **Interact with the app:**
    - Select the AI model (OpenAI or Google AI) from the sidebar.
    - Enter your API key for the selected model.
    - Upload your PDF files.
    - Ask questions about the content of the uploaded PDFs.

## 📋 Project Structure

```
PDFInsightAI/
│
├── src/
│   ├── __init__.py
│   ├── utils.py
│   └── config.py
│
├── app.py
├── requirements.txt
├── .env
└── README.md
```

- `src/`: Contains utility functions and configuration files.
- `app.py`: The main application file.
- `requirements.txt`: List of dependencies.
- `.env`: Environment variables file for storing API keys.

---

### Enjoy using PDFInsight AI! 🚀📘

---
