# _*_ coding:utf-8 _*_
# @Author    :ran
# @time      :2018-12-03 10:47
# @File      :aiohttp_asynico.py
# @Software  :PyCharm

# 异步请求网页
import asyncio
import time
import aiohttp

URL = 'https://morvanzhou.github.io/'


async def job(session):
    # response = await session.get(URL)       # 等待并切换
    async with session.get(URL) as response:
        print(response.status)
        return str(response.url)


async def main(internal_loop):
    async with aiohttp.ClientSession() as session:      # 官网推荐建立 Session 的形式
        tasks = [internal_loop.create_task(job(session)) for _ in range(2)]
        finished, unfinished = await asyncio.wait(tasks)
        all_results = [r.result() for r in finished]    # 获取所有结果
        print(all_results)

if __name__ == "__main__":
    t1 = time.time()
    loop = asyncio.get_event_loop()             # 建立 loop
    loop.run_until_complete(main(loop))         # 执行 loop
    loop.close()   # 关闭 loop
    print("Async total time : ", time.time() - t1)
