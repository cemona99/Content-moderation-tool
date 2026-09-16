# Content Moderation Tool

An AI-assisted content moderation tool that automatically analyzes and categorizes text content, combining rule-based filtering with sentiment analysis. Inspired by real-world content review workflows.

## Features

- Detects banned words and spam patterns (excessive links, promotional keywords, excessive capitalization)
- Analyzes sentiment using NLP (VADER sentiment analysis)
- Classifies each piece of content as APPROVED, FLAGGED, or REJECTED
- Generates a structured JSON report with reasons for each decision
- Covered by unit tests to verify moderation logic

## How to run

1. Install dependencies: `pip install -r requirements.txt`
2. Add content to check in `sample_content.txt`, one entry per line
3. Run the moderation tool: `python3 main.py`
4. Check the console output or open `report.json` for full results

## Running tests

`python3 test_moderator.py`

## Example output

REJECTED - "CLICK HERE NOW FOR FREE MONEY!!!"
Reasons: spam patterns: click here, free money, excessive caps

APPROVED - "The weather today is quite nice"

## Built with

- Python
- vaderSentiment (NLP sentiment analysis)
