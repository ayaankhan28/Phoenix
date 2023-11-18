
# AI Virtual Assistant(Phoenix)

This project is an AI virtual assistant that can perform various tasks, including speech recognition, web searches, and more. It utilizes the OpenAI API and other Python libraries for audio processing and interaction.
Installation Instructions:
Include instructions on how to set up and run your project. List any dependencies and provide installation commands.

markdown
Copy code
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   
Install dependencies:

SpeechRecognition,PyAudio,Openai.



## Code Structure

- `Asst-1.py`: Main script for running the virtual assistant.
- `speech.py`: Module for assisstant voice.
- `Listen.py`: Module Speech recognition.
- `output.mp3`: Module Speech recognition.


- **Speech Recognition:**
  The assistant can recognize speech using the `recognize_speech` function.

  ```bash python
  result = recognize_speech()
  print(result)
Text-to-Speech:
The speak function converts text to speech using the OpenAI TTS API.


## Troubleshooting:
Problems with dependencies, audio configuration, or API key issues,.

## Future Enhancements

- Implement multi-language support for speech recognition.
- Add a more sophisticated natural language processing (NLP) system.
- Enhance error handling and provide more informative error messages.
- More RPM(request per minute)
## Known Issues

- Limited accuracy in noisy environments for speech recognition.
- Issues with PyAudio on certain operating systems.
- Very low end hardware
Examples:
Detailed examples of how users can interact with virtual assistant. Provided real-world scenarios to showcase its capabilities.


## Examples
```python
# Open a video on YouTube
open_video("Loki Season 2 trailer")
Memory Keeping
# Save important information
memory_keeping("Ayaan Khan, 19, I love Marvel's Avengers", "movie tonight")
Web Search
# Perform a web search
open_web("When is GTA 6 game trailer releasing?")
Exiting the Assistant
# Exit the assistant
speak("Goodbye!")
