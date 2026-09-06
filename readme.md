# AI Career Assistant MCP Server

A simple **Model Context Protocol (MCP)** project built with Python to demonstrate how an MCP server can expose **Tools, Resources, and Prompts** to an MCP client.

## Project Overview

This project implements an **AI Career Assistant MCP Server**.

It allows an MCP client to:

- Check how well a user's skills match an AI role
- Fetch public GitHub profile information
- Read an AI Application Engineer learning roadmap
- Generate a reusable interview-preparation prompt

The server was tested successfully using **MCP Inspector**.

## Features

### Tools

#### `check_role_match()`

Compares user skills with the required skills for a selected role.

Supported roles:

- AI Engineer
- ML Engineer
- GenAI Engineer

Example:

```text
Skills:
python, machine learning, deep learning, git, mcp

Role:
ai engineer
```

Example output:

```text
Role: AI Engineer
Match Score: 83%
Matched Skills: deep learning, git, machine learning, mcp, python
Missing Skills: fastapi
```

#### `get_github_profile()`

Fetches public GitHub profile information using the GitHub REST API.

It returns:

- Username
- Name
- Public repositories
- Followers
- Following
- GitHub profile URL

## Resource

### `career://roadmap`

Provides a learning roadmap for an AI Application Engineer.

Topics include:

1. Python
2. Machine Learning
3. Deep Learning
4. Generative AI
5. LLMs
6. RAG
7. FastAPI / APIs
8. Git & GitHub
9. MCP
10. AI Application Projects

## Prompt

### `interview_prep(role)`

Creates a reusable interview-preparation prompt for a selected role.

Example:

```text
AI Engineer
```

The prompt instructs the AI to ask technical interview questions one by one and provide feedback after each answer.

## MCP Architecture

```text
User
  ↓
MCP Client / MCP Inspector
  ↓
AI Career Assistant MCP Server
  ↓
├── Tools
│   ├── check_role_match()
│   └── get_github_profile()
│
├── Resource
│   └── career://roadmap
│
└── Prompt
    └── interview_prep()
```

For the GitHub tool:

```text
MCP Client
   ↓
MCP Server
   ↓
get_github_profile()
   ↓
GitHub REST API
   ↓
MCP Server
   ↓
Result
```

## Technologies Used

- Python
- Model Context Protocol (MCP)
- MCP Python SDK
- MCP Inspector
- Requests
- GitHub REST API

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd mcp-career-assistant
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install "mcp[cli]" requests
```

## Run the MCP Server

Start the server with:

```bash
mcp dev server.py
```

MCP Inspector will open in the browser.

Click **Connect** and test:

- Tools
- Resources
- Prompts

## Project Structure

```text
mcp-career-assistant/
│
├── server.py
├── README.md
└── requirements.txt
```

## requirements.txt

Add the following:

```text
mcp[cli]
requests
```

## What I Learned

Through this project, I learned:

- What MCP is and why it is used
- MCP Host, Client, and Server architecture
- How MCP clients communicate with MCP servers
- How to create MCP Tools
- How to expose MCP Resources using URIs
- How to create reusable MCP Prompts
- How to connect an MCP tool with an external REST API
- How to test and debug an MCP server using MCP Inspector

## Future Improvements

Possible improvements include:

- Connect the MCP server to an LLM-based AI assistant
- Add database integration
- Add resume analysis tools
- Add job recommendation tools
- Add real job-search APIs
- Add authentication and deployment

## Author

**Chetan Kumar N K**

AI / Machine Learning / Generative AI Learner