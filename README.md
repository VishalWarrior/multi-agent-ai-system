# Multi-Agent AI System (LangChain + Ollama)

## Overview
This project implements a multi-agent AI system using local LLM (Llama3 via Ollama).

## Architecture
User Input → Planner → Researcher → Writer → Validator → Output

## Features
- Multi-agent pipeline
- Validation loop (retry mechanism)
- Conversation memory
- Debug logging (trace execution)

## Tech Stack
- Python
- LangChain
- Ollama (Llama3)

## How to Run
pip install -r requirements.txt
python task9.py

## Example Flow
1. User asks question
2. Planner breaks task
3. Researcher gathers info
4. Writer generates response
5. Validator checks quality
