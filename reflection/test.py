import asyncio
from google.genai import types
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from agents import root_agent

async def run_test():
    runner = Runner(
        app_name="reflection-test",
        agent=root_agent,
        session_service=InMemorySessionService(),
        auto_create_session=True
    )
    
    print("Starting Agent Loop Test...\n")
    
    # We send a triggering message to start the loop
    initial_message = types.Content(role="user", parts=[types.Part.from_text(text="Please generate an IRIT script for a unit sphere.")])
    
    # Using run_async allows us to pass state_delta for the {topic} variable
    async for event in runner.run_async(
        user_id="test", 
        session_id="test_session1", 
        new_message=initial_message,
        state_delta={"topic": "unit sphere"}
    ):
        if event.content and event.content.parts and event.content.parts[0].text:
            print(f"[{event.author}] {event.content.parts[0].text[:100]}...")
            
        function_calls = event.get_function_calls()
        if function_calls:
            for call in function_calls:
                print(f"[{event.author}] executes tool: {call.name}")

def main():
    asyncio.run(run_test())

if __name__ == "__main__":
    main()
