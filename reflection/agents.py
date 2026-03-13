from google.adk.agents import LlmAgent, LoopAgent
from tools import write_irt_file, execute_irt_file, read_irt_file, exit_loop, replace
from prompts import irit_assistant_prompt, irit_reflector_prompt

irit_assistant = LlmAgent(
    name="irit_assistant",
    model="gemini-3-flash-preview",
    instruction=irit_assistant_prompt,
    tools=[write_irt_file, replace],
)

irit_reflector = LlmAgent(
    name="irit_reflector",
    model="gemini-3-flash-preview",
    instruction=irit_reflector_prompt,
    tools=[execute_irt_file, read_irt_file, exit_loop],
)

root_agent = LoopAgent(
    name="loop_agent",
    max_iterations=3,
    sub_agents=[irit_assistant, irit_reflector],
)