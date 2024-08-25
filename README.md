# Gemini-based Chatbot Application

This project is a web application built with Streamlit that integrates with Google's Gemini AI model. It allows users to input text and upload images to interact with a generative AI model. The application showcases how to use the Google Generative AI API in a web-based interface.

## Features

- **Text Input**: Allows users to provide a text prompt.
- **Image Upload**: Users can upload an image to be processed by the AI.
- **AI Response**: Displays the AI-generated response based on the input text and/or image.

## Requirements

- Python 3.7 or higher
- Streamlit
- \`python-dotenv\` for environment variable management
- \`google-generativeai\` for interacting with the Google Generative AI API
- \`Pillow\` for image processing

## Setup

### 1. Clone the Repository

`\`bash
git clone https://github.com/riturajs12/Gemini-based-chatbot.git
cd your-repository
\`

### 2. Create a Virtual Environment

\`bash
python -m venv venv
source venv/bin/activate  # On Windows use \`venv\\Scripts\\activate\`
\`

### 3. Install Dependencies

\`bash
pip install -r requirements.txt
\`

### 4. Set Up Environment Variables

Create a \`.env\` file in the root directory of your project and add your Google API key:

\`
GOOGLE_API_KEY=your_google_api_key_here
\`

### 5. Run the Application

\`bash
streamlit run app.py
\`

Replace \`app.py\` with the name of your Python file if it's different.

## Usage

1. Open the application in your web browser.
2. Enter a text prompt in the "Input Prompt" field.
3. Optionally, upload an image by clicking the "Choose an image" button.
4. Click the "Click me" button to generate and view the AI response.
