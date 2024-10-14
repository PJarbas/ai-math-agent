import os
from langchain_openai import AzureChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain.agents import load_tools
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

load_dotenv()


# pip install wolframalpha

# get your developer simpleAPI key here: https://developer.wolframalpha.com/access
os.environ["WOLFRAM_ALPHA_APPID"] = "Your_Key"

template = '''
You are a reasoning agent tasked with solving 
the user's math and logic-based questions. Logically arrive at the solution, and be 
factual. In your answers, clearly detail the steps involved and give the 
final answer.

Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}'''

prompt = PromptTemplate.from_template(template)

llm = AzureChatOpenAI(
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
    openai_api_version=os.getenv('AZURE_OPENAI_API_VERSION'),
    openai_api_key=os.getenv('AZURE_OPENAI_API_KEY'),
    temperature=0
)

tool_names = ["wolfram-alpha"]
tools = load_tools(tool_names=tool_names)

agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
memory.output_key = "output"

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True, 
    return_intermediate_steps=True

)

query = ("I have 3 apples and 4 oranges. I give half of my oranges" 
         "away and buy two dozen new ones, alongwith three packs of" 
         "strawberries. Each pack of strawberry has 30 strawberries." 
          "How  many total pieces of fruit do I have at the end?")

query2 = "What is the derivative of cos(x)"

response = agent_executor.invoke({"input":query2})

print(response)
