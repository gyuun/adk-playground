from google.adk.tools.tool_context import ToolContext

def write_irt_file(file_name: str, content: str):
    """Write content to a .irt file."""
    file_path = f"{file_name}.irt"
    with open(file_path, "w") as f:
        f.write(content)

def search_knowledge_base(query: str):
    """Search the knowledge base for relevant information."""
    pass

def execute_irt_file(file_name: str):
    """Execute an IRIT file."""
    pass

def replace(file_name: str, old_content: str, new_content: str):
    """Replace content in a file."""
    pass

def read_irt_file(file_name: str):
    """Read content from a .irt file."""
    file_path = f"{file_name}.irt"
    with open(file_path, "r") as f:
        return f.read()

def exit_loop(tool_context: ToolContext):
    """Call this function ONLY when the critique indicates no further changes are needed, signaling the iterative process should end."""
    print(f"  [Tool Call] exit_loop triggered by {tool_context.agent_name}")
    tool_context.actions.escalate = True
    tool_context.actions.skip_summarization = True
    # Return empty dict as tools should typically return JSON-serializable output
    return {}