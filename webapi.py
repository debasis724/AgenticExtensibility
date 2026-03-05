import time
import requests
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class GithubFileCheckerInput(BaseModel):
    repo_owner: str = Field(..., description="Owner of the GitHub repository")
    repo_name: str = Field(..., description="Name of the repository")
    file_path: str = Field(..., description="Path of the file inside the repo")
    branch: str = Field(default="main", description="Branch to check")
    github_token: str = Field(..., description="GitHub personal access token")


class GithubFileCheckerTool(BaseTool):
    name: str = "GitHub File Checker"
    description: str = (
        "Waits for 30 minutes and then checks whether a file exists in a GitHub repository."
    )
    args_schema: Type[BaseModel] = GithubFileCheckerInput

    def _run(
        self,
        repo_owner: str,
        repo_name: str,
        file_path: str,
        branch: str,
        github_token: str,
    ) -> str:

        # Wait 30 minutes
        print("Waiting for 30 minutes before checking GitHub...")
        time.sleep(1800)

        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"

        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {github_token}",
        }

        params = {"ref": branch}

        try:
            response = requests.get(url, headers=headers, params=params)

            if response.status_code == 200:
                return "File exists in the GitHub repository."

            elif response.status_code == 404:
                return "File does NOT exist in the GitHub repository."

            else:
                return f"Unexpected response: {response.status_code} - {response.text}"

        except Exception as e:
            return f"Error checking file: {str(e)}"
