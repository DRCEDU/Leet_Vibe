# Use OpenAI Whisper for Automated Transcriptions

*Published on Towards Data Science, June 25, 2025*  
*By Eivind Kjosbakken*

## Overview

This article discusses how to leverage OpenAI's Whisper model for automated audio-to-text transcription, streamlining computer interactions and improving programming efficiency. The author shares practical setup steps, pros and cons, and workflow automation using hotkeys and scripts.

---

## Motivation

- OpenAI Whisper provides highly accurate speech-to-text transcription, outperforming built-in solutions like Apple's iPhone transcription.
- Especially useful for programmers who spend significant time writing English prompts for LLMs (e.g., ChatGPT, Cursor).
- Speaking is generally faster than typing: average talking speed is at least 110 words per minute, while fast typing rarely exceeds 100 wpm.

---

## Prerequisites

- **Alfred** (or similar tool) to trigger scripts via hotkeys on Mac/PC.
- OpenAI API key (for Whisper API access).

---

## Pros

- Much faster input for long prompts or text compared to typing.
- High transcription accuracy, even with technical terms and acronyms.
- Saves time and reduces risk of repetitive strain injuries from typing.

## Cons

- Not always practical to speak out loud (e.g., in public or shared spaces).
- For short prompts, the overhead of starting/stopping and API latency may outweigh speed benefits.

---

## How to Implement

1. **Clone the GitHub repository:**
   ```bash
git clone https://github.com/EivindKjosbakken/whisper-shortcut.git
```
2. **Set up the Python environment:**
   ```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
3. **Get an OpenAI API Key:**
   - Go to the [OpenAI API Overview](https://platform.openai.com/overview), log in, and create a new API key.
   - Save the key securely.
4. **Scripts in the repo:**
   - `start_recording.sh`: Starts recording your voice (requests microphone permission on first use).
   - `stop_recording.sh`: Stops recording, sends audio to OpenAI for transcription, copies result to clipboard, and pastes if a text field is selected.

---

## Alfred Workflow

- Download the Alfred workflow from the GitHub repo: `Transcribe.alfredworkflow`.
- Set up hotkeys (e.g., Option+Q to start, Option+W to stop and transcribe).
- *Figure: Screenshot of Alfred workflow with hotkeys for starting/stopping transcription.*
- **Note:** Keep a terminal window open to run the scripts (for microphone permissions).

---

## Cost

- OpenAI Whisper API usage is moderately priced.
- Example: 25 uses/day, up to 150 words each, costs less than $1/day.
- Heavy use could reach ~$30/month, but time savings may justify the cost.

---

## Conclusion

OpenAI Whisper enables near-perfect, fast, and accurate transcription, making it a powerful tool for programmers and anyone who needs to input large amounts of text. With simple scripting and workflow automation, you can integrate Whisper into your daily workflow and boost productivity.

---

**For more details, code, and workflow setup, see the full article:**  
[Use OpenAI Whisper for Automated Transcriptions](https://towardsdatascience.com/use-openai-whisper-for-automated-transcriptions/) 