from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchResults
from langchain_community.utilities.duckduckgo_search import DuckDuckGoSearchAPIWrapper

# search_tool = DuckDuckGoSearchRun()
search_tool = DuckDuckGoSearchResults()
res = search_tool.run("what is the weather in SF")
print(res)


ddg_tool = DuckDuckGoSearchAPIWrapper()
res = ddg_tool.results("what is the weather in SF", 6)
print(res)
