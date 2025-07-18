# Banking Agentic AI Application

This application aims to simulate common operations found in banking, using agentic AI.

- open an account
- deposit funds
- withdraw funds
- transfer funds
- close an account

This application makes use of uv, the Python package and project manager:

https://docs.astral.sh/uv/guides/projects

When this application was first created, a new uv project was created with:
uv init bank-of-ai

The python-dotenv package is used to load API keys and other tokens, etc. from an .env file. This is a best practice because such API keys, etc. should never be stored in a source control system, because if anyone were to gain access to your keys you could incur charges from LLMs, etc.

https://pypi.org/project/python-dotenv

