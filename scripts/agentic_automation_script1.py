from browser_use import Agent, ChatGoogle
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    
    llm = ChatGoogle(model="gemini-2.5-flash")
    task = "Navigate to YouTube, search for 'lofi hip hop', and play the first video."
    agent = Agent(task=task, llm=llm)
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())