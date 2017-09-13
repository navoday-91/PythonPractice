import requests
import asyncio

def http_call_sync():
    r = requests.get('https://httpbin.org/status/200')
    print(r.status_code)

    r = requests.get('https://httpbin.org/status/204')
    print(r.status_code)

async def http_call_async():
    urllist = ['https://httpbin.org/status/200', 'https://httpbin.org/status/204']
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(
            None,
            requests.get,
            urllist[i]
        )
        for i in range(2)
    ]
    for response in await asyncio.gather(*futures):
        print(response.status_code)

print("Synchronous Attempt:")
http_call_sync()
print("Asynchronous Attempt:")
loop = asyncio.get_event_loop()
loop.run_until_complete(http_call_async())