# y uise hota hai serahing something from wbe or y ek runnable hoita hai 
from langchain_community.tools import DuckDuckGoSearchRun
serach_tool=DuckDuckGoSearchRun()
results=serach_tool.invoke('stocks news')
print(results)