from cat.mad_hatter.decorators import tool, hook

@tool()
def test_tool(input,cat):
    """Are you a real cat?"""

    return f"No, I'm a dog"

@tool()
def world_tool(input,cat):
    """User send one of these: europe,usa-canada,australia,asia,latin-america. Input is the string sent."""

    return f"I live in {input}"

@hook
def agent_prompt_prefix(prefix, cat):
    settings = cat.mad_hatter.get_plugin().load_settings()
    prefix = settings["prompt_prefix"]

    return prefix

@hook  # default priority = 1
def agent_prompt_suffix(prompt_suffix, cat):
    settings = cat.mad_hatter.get_plugin().load_settings()
    suffix = f"""
    # Context

    {{episodic_memory}}

    {{declarative_memory}}

    {{tools_output}}
    """

    if settings["language"] != "None":
            suffix += f"""
    ALWAYS answer in {settings["language"]}
    """

    suffix += f"""
    ## Conversation until now:{{chat_history}}
    - {settings["user_name"] if settings["user_name"] != "" else "Human" }: {{input}}
    - AI: """

    return suffix