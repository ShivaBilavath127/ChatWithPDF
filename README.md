# ChatPDF - AI-Powered PDF Question Answering System

ChatPDF is a web application that allows users to upload PDF documents and ask questions about their content. The application uses AI to analyze the PDF and provide relevant answers to user queries.

## Features

- PDF document upload and processing
- AI-powered question answering
- Real-time responses
- User-friendly interface
- Cross-origin resource sharing (CORS) enabled

## Tech Stack

### Backend
- Python 3.x
- Flask (Web framework)
- Flask-CORS (Cross-origin resource sharing)
- PyMuPDF (PDF processing)
- Together AI API (AI model integration)

### Frontend
- React.js
- Axios (HTTP client)
- TailwindCSS (Styling)
- Modern React features and hooks

## Project Structure

```
chatPDF/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── uploads/
└── frontend/
    ├── public/
    ├── src/
    ├── package.json
    └── README.md
```

## Setup and Installation

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask server:
   ```bash
   python app.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

## API Endpoints

### Backend API

1. `POST /upload`
   - Upload a PDF file
   - Returns success message upon successful upload

2. `POST /ask`
   - Send questions about the uploaded PDF
   - Returns AI-generated answers based on the PDF content

## Environment Variables

The backend requires the following environment variable:
- `TOGETHER_API_KEY`: Your Together AI API key for AI model access

## Usage

1. Open the application in your web browser
2. Upload a PDF document using the file upload interface
3. Once the PDF is processed, you can start asking questions about its content
4. The AI will analyze the PDF and provide relevant answers to your questions

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Together AI for providing the AI model
- PyMuPDF for PDF processing capabilities
- React and Flask communities for their excellent documentation 