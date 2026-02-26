import asyncio
import time


async def download_task_async(name):
    print(f"协程 {name}: 开始下载...")
    # 注意：这里必须使用 asyncio.sleep 而不能用 time.sleep
    # 因为 time.sleep 会卡死整个线程，导致协程无法切换
    await asyncio.sleep(2)
    print(f"协程 {name}: 下载完成")


async def run_coroutines():
    start_time = time.time()

    # 创建任务列表
    tasks = [
        download_task_async("C-0"),
        download_task_async("C-1"),
        download_task_async("C-2")
    ]

    # 并发运行所有协程
    await asyncio.gather(*tasks)

    print(f"--- 协程总耗时: {time.time() - start_time:.2f} 秒 ---")


if __name__ == "__main__":
    # 启动异步事件循环
    asyncio.run(run_coroutines())
    print(download_task_async)