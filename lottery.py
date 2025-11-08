#########################################################################
# Python x AI Agent
# bs4, requests, json - URL/HTTP 處理示範
#
# [題意]
# 彩券號碼解析
# 需求：解析貼上的 .ball-container HTML，輸出開獎號碼相關資訊。
###########################################################################

import json
import requests


def format_output(normals, bonus):
    print("開獎號碼:", "  ".join(f"{n:02d}" for n in normals) if normals else "—")
    print("大小順序:", "  ".join(f"{n:02d}" for n in sorted(normals)) if normals else "—")
    print("第二區  :", f"{bonus:02d}" if bonus is not None else "—")


if __name__ == "__main__":
    url = "https://api.taiwanlottery.com/TLCAPIWeB/Lottery/SuperLotto638Result?period&month=2025-11&pageSize=31"
    print("網頁下載中 ...")
    response = requests.get(url)
    print("網頁下載完成")
    data = response.json()
    super_result = data['content']['superLotto638Res'][0]
    period = super_result['period']
    draw_order = super_result['drawNumberAppear']
    normals = draw_order[:-1]
    bonus = draw_order[-1]
    print(f"第{period}期")
    print(f"串列長度: {len(normals) + 1}")
    format_output(normals, bonus)
