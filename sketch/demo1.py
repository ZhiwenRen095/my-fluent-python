import asyncio

from clockdemo import clock

async def brew_coffee():
    print("1. 开始煮咖啡...")
    await asyncio.sleep(7) # 煮咖啡需要 2 秒
    print("1. 咖啡煮好了！")
    return "Coffee"

async def toast_bread():
    print("2. 开始烤面包...")
    await asyncio.sleep(4) # 烤面包需要 1 秒
    print("2. 面包烤好了！")
    return "Toast"


async def main():
    print("--- 早餐准备开始 ---")
    # 并行处理
    results = await asyncio.gather(brew_coffee(), toast_bread())
    print(f"--- 早餐大功告成: {results} ---")

@clock
def start():
    asyncio.run(main())

if __name__ == '__main__':
    start()