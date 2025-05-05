import httpx
import asyncio

async def is_social_link_valid(url):
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get(url)
            if response.status_code == 200 and "suspended" not in response.text.lower():
                return True
    except Exception:
        pass
    return False

async def validate_social_links(socials: dict):
    platforms = ["twitter", "telegram", "discord"]
    tasks = []

    for platform in platforms:
        url = socials.get(platform)
        if url and url.startswith("http"):
            tasks.append(is_social_link_valid(url))

    results = await asyncio.gather(*tasks)
    return sum(results)

def check_social_presence(token_data):
    socials = token_data.get("info", {}).get("socials", {})
    try:
        valid_count = asyncio.run(validate_social_links(socials))
    except RuntimeError:
        import nest_asyncio
        nest_asyncio.apply()
        valid_count = asyncio.run(validate_social_links(socials))

    if valid_count >= 2:
        return "STRONG"
    elif valid_count == 1:
        return "WEAK"
    else:
        return "NONE"
