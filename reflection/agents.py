from google.adk.agents import LlmAgent, LoopAgent
from .prompts import *

irit_agent = LlmAgent(
    name="irit_agent",
    model="gemini-3-flash-preview",
    prompt="",
)

reflector_agent = LlmAgent(
    name="reflector_agent",
    model="gemini-3-flash-preview",
    prompt="",
)

root_agent = LoopAgent(
    name="loop_agent",
    model="gemini-3-flash-preview",
    sub_agents=[irit_agent, reflector_agent],
)