


from browser_use import Agent, ChatGoogle
from dotenv import load_dotenv
import asyncio
import json
import os

load_dotenv()

def get_task_from_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        # Get the first task's description
        return data['tasks'][0]['description'] if data['tasks'] else None

async def main():
    llm = ChatGoogle(model="gemini-2.5-flash")
    # Path to tasks.json
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, 'test_cases', 'tasks.json')
    task = get_task_from_json(json_path)
    print(f"Loaded task: {task}")
    if not task:
        print("No task found in tasks.json.")
        return
    agent = Agent(task=task, llm=llm)
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())