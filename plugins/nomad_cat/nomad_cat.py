from cat.mad_hatter.decorators import tool
from cat.mad_hatter.decorators import hook

@tool()
def test_tool(input,cat):
    """Are you a real cat?"""

    return f"No, I'm a dog"

@tool()
def world_tool(input,cat):
    """User send one of these: europe,usa-canada,australia,asia,latin-america. Input is the string sent."""

    return f"I live in {input}"

@tool
def convert_currency(tool_input, cat): # 
    """Useful to convert currencies. This tool converts euro (EUR) to dollars (USD).
     Input is an integer or floating point number.""" # 

    # Define fixed rate of change
    rate_of_change = 1.07

    # Parse input
    eur = float(tool_input) # 

    # Compute USD
    usd = eur * rate_of_change

    return usd

@hook
def agent_prompt_prefix(prefix, cat):

    prefix = """You are Nomad cat, a travelling cat living as a digital nomad.
    You are an expert in travels, coworking spaces around the world and tricks about low budget travels.
    """

    return prefix