# agentic_automation

This project demonstrates agentic automation using Python, Playwright, and LLMs. It includes an example agent that can automate browser tasks, such as searching and playing videos on YouTube.

## Features
- Agent-based browser automation
- Integration with Playwright
- Uses LLMs (e.g., Gemini) for task instructions

## Project Structure
- `scripts/agentic_automation_script1.py`: Main script to run the agent
- `requirements.txt`: Python dependencies
- `setup.bat`: Batch file to set up the environment
- `.gitignore`: Files and folders to exclude from git

## Setup Instructions
1. Clone the repository:
	```powershell
	git clone https://github.com/sqavikas9/agentic_automation.git
	cd agentic_automation
	```
2. Run the setup script to create a virtual environment and install dependencies:
	```powershell
	setup.bat
	```
3. (If you see a script execution error, run this command first:)
	```powershell
	Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
	```

## Usage
Edit `scripts/agentic_automation_script1.py` to define your automation task. Example:
```python
task = "Navigate to YouTube, search for 'lofi hip hop', and play the first video."
```
Run the script:
```powershell
python scripts/agentic_automation_script1.py
```

## Troubleshooting
### fatal: No configured push destination
If you see this error:
```
fatal: No configured push destination.
```
Add your remote and push:
```powershell
git remote add origin https://github.com/your-username/your-repo.git
git push origin main
```

## License
MIT
