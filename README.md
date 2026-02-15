# ai-video-generation-pipeline
Automated AI pipeline that converts a topic into a YouTube-ready video using free tools.
# AI Video Generation Pipeline

This project implements an end-to-end automated pipeline that converts a user-provided topic into a YouTube-ready video using free tools.

##  Features

- AI script generation using Groq API
- Natural voice synthesis using Microsoft Edge TTS
- Automatic visual retrieval using Pexels API
- Automated video editing with MoviePy and FFmpeg
- Single input → complete video output
- Fully automated workflow

##  Workflow

Topic → Script → Voice → Visuals → Video (.mp4)

##  Technologies Used

- Python
- Groq API (LLaMA model)
- Edge TTS
- Pexels API
- MoviePy
- FFmpeg

##  Setup Instructions

1. Install dependencies:

   pip install -r requirements.txt

2. Create a `.env` file and add your API keys:

   GROQ_API_KEY=your_key_here  
   PEXELS_API_KEY=your_key_here  

3. Run the pipeline:

   python main.py

##  Output

The system generates a fully automated video ready for YouTube upload.

##  Use Case

Demonstrates how AI can automate content creation from a single topic input without manual editing.
