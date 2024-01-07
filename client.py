import time

import httpx
from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8000/agent/")

trials = 5
while True:
    try:
        res = remote_chain.invoke({
                # "input": "how can langsmith help with testing?",
                "input": "Is the langsmith a possible to local run?",
                "chat_history": [
                ]
            })
        print(res["output"])
        break
    except httpx.ConnectError as e:
        print("Connection error, retrying")
        trials -= 1
        print(f"{trials} trials left")
        if trials == 0:
            raise e
        time.sleep(5)
