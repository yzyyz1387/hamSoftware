import json
import httpx

async def get_status(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        url = data[item]['url']
        code = await get_url_status_code(url)
        data[item]['status'] = code
        print(f'{url} - {code}')
    with open(json_file , 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4,ensure_ascii=False)
    

async def get_url_status_code(url):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return response.status_code
    except Exception as e:
        print(f'Error: {e}')
        return 0

if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_status('res-web.json'))