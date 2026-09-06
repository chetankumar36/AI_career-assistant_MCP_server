from mcp.server import MCPServer
import requests

mcp = MCPServer("AI Career Assistant")


# -------------------------
# TOOL 1: Check role match
# -------------------------

@mcp.tool()
def check_role_match(skills: str, role: str) -> str:
    """Check how well a user's skills match an AI role."""

    role_skills = {
        "ai engineer": {
            "python",
            "machine learning",
            "deep learning",
            "fastapi",
            "git",
            "mcp"
        },

        "ml engineer": {
            "python",
            "machine learning",
            "pandas",
            "numpy",
            "scikit-learn",
            "git"
        },

        "genai engineer": {
            "python",
            "llm",
            "rag",
            "embeddings",
            "fastapi",
            "mcp"
        }
    }

    role = role.lower()

    if role not in role_skills:
        return "Role not found."

    user_skills = {
        skill.strip().lower()
        for skill in skills.split(",")
    }

    required = role_skills[role]

    matched = user_skills.intersection(required)
    missing = required - user_skills

    score = (len(matched) / len(required)) * 100

    return (
        f"Role: {role.title()}\n"
        f"Match Score: {score:.0f}%\n"
        f"Matched Skills: {', '.join(sorted(matched))}\n"
        f"Missing Skills: {', '.join(sorted(missing))}"
    )


# -------------------------
# TOOL 2: GitHub API
# -------------------------

@mcp.tool()
def get_github_profile(username: str) -> str:
    """Get public GitHub profile information."""

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url, timeout=10)

    if response.status_code == 404:
        return "GitHub user not found."

    response.raise_for_status()

    data = response.json()

    return (
        f"Username: {data.get('login')}\n"
        f"Name: {data.get('name')}\n"
        f"Public Repositories: {data.get('public_repos')}\n"
        f"Followers: {data.get('followers')}\n"
        f"Following: {data.get('following')}\n"
        f"Profile: {data.get('html_url')}"
    )


# -------------------------
# RESOURCE
# -------------------------

@mcp.resource("career://roadmap")
def career_roadmap() -> str:
    """AI application engineer learning roadmap."""

    return """
AI Application Engineer Roadmap

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
"""


# -------------------------
# PROMPT
# -------------------------

@mcp.prompt()
def interview_prep(role: str) -> str:
    """Generate an interview preparation prompt."""

    return (
        f"You are an interviewer for a {role} position. "
        f"Ask technical questions one by one. "
        f"After every answer, explain whether it is correct "
        f"and provide a better answer."
    )