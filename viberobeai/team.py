from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team import Team
from agno.tools.dalle import DalleTools
from agno.tools.duckduckgo import DuckDuckGoTools

# https://docs.agno.com/tools/toolkits/toolkits
# --- VibeRobe.ai Agent Setup ---

stylist_agent = Agent(
    name='StylistAgent',
    role='You are a Fashion Stylist',
    description='You are an AI fashion consultant that suggests outfits based on the occasion, '
    'location, weather, and user preferences.',
    instructions='When given the occasion, location, weather, '
    'and user preferences (if available), '
    'suggest a complete outfit that is stylish and comfortable. '
    'Consider user-defined options like preferred colors, modesty, or body comfort. '
    'If the user intends to shop, ensure the items are shoppable. '
    'If the user wants inspiration only, focus on creativity and styling tips.',
    model=OpenAIChat(id='gpt-4o'),
    tools=[],
    show_tool_calls=True,
    markdown=True,
)

occasion_agent = Agent(
    name='OccasionAgent',
    role='You are an Event Context Analyzer',
    description='You interpret the nature of an event and map it to appropriate dress codes and style recommendations.',
    instructions="When given an event like 'rooftop dinner' or 'startup pitch', "
    'identify its typical formality and setting. '
    'Output relevant dress codes (e.g., smart casual) and any keywords that can guide the stylist '
    '(e.g., relaxed, evening vibe, modern).',
    model=OpenAIChat(id='gpt-4o'),
    tools=[],
    show_tool_calls=True,
    markdown=True,
)

location_agent = Agent(
    name='LocationAgent',
    role='You are a Geo Context Assistant',
    description='You provide real-time or seasonal weather context for a city to inform outfit suggestions.',
    instructions='Given a city and approximate date/time, fetch or infer weather details '
    'such as temperature and wind. '
    'Use DuckDuckGo to search if needed. I'
    'f real-time data is unavailable, infer from season/location. '
    "Output in a concise format like 'Bangalore in March evenings: ~22°C, dry, breezy'.",
    model=OpenAIChat(id='gpt-4o'),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

visualizer_agent = Agent(
    name='VisualizerAgent',
    role='You are an Outfit Visualizer',
    description="You generate a realistic visual for a fashion outfit based on the stylist's description.",
    instructions='When given an outfit description, generate a visual representation using DALL·E. '
    'Ensure the output reflects the described clothing (e.g., color, fit, style) and '
    'is aesthetically pleasing for a fashion app.',
    model=OpenAIChat(id='gpt-4o'),
    tools=[DalleTools()],
    show_tool_calls=True,
    markdown=True,
)

shopping_agent = Agent(
    name='ShoppingAgent',
    role='You are a Personal Shopper',
    description='You find matching items for a recommended outfit by searching online stores, '
    'only if the user intends to buy.',
    instructions='If the user specifies they want to shop the outfit, search amazon.in for similar or exact items. '
    'Use product name, price, link, and image.'
    'If shopping is not requested, skip this step.',
    model=OpenAIChat(id='gpt-4o'),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

# --- VibeRobe.ai Agent Team ---

agent_team = Team(
    name='VibeRobeTeam',
    description='A coordinated team of agents that collaboratively '
    'suggest an outfit and optionally place a purchase order.',
    mode='coordinate',
    members=[
        location_agent,
        occasion_agent,
        stylist_agent,
        visualizer_agent,
        shopping_agent,
    ],
    model=OpenAIChat(id='gpt-4o'),
    instructions=[
        'Always include sources when using search tools.',
        'Use tables to display outfit options or shopping results.',
        "Respect user's intent: inspiration only vs shopping.",
    ],
    success_criteria='Suggest a stylish, personalized outfit based on user input and location context. '
    'If the user intends to shop, return links to buy each item (preferably on amazon.in).',
    show_tool_calls=True,
    markdown=True,
)


async def viberobe(prompt: str):
    agent_team.print_response(
        # 'What should I wear for a rooftop dinner in Bangalore?',
        # 'Show me a dress for a rooftop dinner in Bangalore and suggest a matching jacket. Shop the products.',
        prompt,
        stream=True,
    )
    return 'Completed!'
