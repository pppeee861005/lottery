# Lottery Number Parser

A Python script to fetch and parse the latest Taiwan Lottery Super Lotto 638 results.

## Features

- Fetches the latest Super Lotto 638 results from the official Taiwan Lottery API
- Displays the winning numbers in draw order and sorted order
- Shows the second area bonus number

## Requirements

- Python 3.x
- requests library

## Installation

1. Install the required library:
   ```bash
   pip install requests
   ```

## Usage

Run the script:
```bash
python lottery.py
```

## Output Example

```
網頁下載中 ...
網頁下載完成
第114000089期
串列長度: 7
開獎號碼: 25  20  29  18  37  11
大小順序: 11  18  20  25  29  37
第二區  : 08
```

## API Information

- API Endpoint: https://api.taiwanlottery.com/TLCAPIWeB/Lottery/SuperLotto638Result?period&month=2025-11&pageSize=31
- Data Structure: The latest result is in `data['content']['superLotto638Res'][0]`
- Draw Order: `drawNumberAppear` (first 6 numbers are first area, last is second area)

## License

This project is for educational purposes.

---

# 彩票号码解析器

一个Python脚本，用于获取和解析最新的台湾彩票超级乐透638结果。

## 功能

- 从官方台湾彩票API获取最新的超级乐透638结果
- 以开奖顺序和排序顺序显示中奖号码
- 显示第二区奖金号码

## 要求

- Python 3.x
- requests库

## 安装

1. 安装所需的库：
   ```bash
   pip install requests
   ```

## 使用方法

运行脚本：
```bash
python lottery.py
```

## 输出示例

```
網頁下載中 ...
網頁下載完成
第114000089期
串列長度: 7
開獎號碼: 25  20  29  18  37  11
大小順序: 11  18  20  25  29  37
第二區  : 08
```

## API信息

- API端点：https://api.taiwanlottery.com/TLCAPIWeB/Lottery/SuperLotto638Result?period&month=2025-11&pageSize=31
- 数据结构：最新结果在 `data['content']['superLotto638Res'][0]`
- 开奖顺序：`drawNumberAppear`（前6个号码为第一区，最后一个为第二区）

## 许可证
總結如下：
你目前看到的連結 https://api.taiwanlottery.com/TLCAPIWeB/Lottery/LatestResult 是台灣彩券的 API，回傳最新彩券結果資料（JSON 格式），不是一般視覺化的網頁。
這個 API 通常不是讓人直接用瀏覽器瀏覽，而是前端網頁（像 www.taiwanlottery.com）用 JavaScript 透過 Ajax、fetch 或 XHR 等方法「動態載入」這份資料，然後再渲染在網頁上。
所以，官方網站的彩券結果顯示，並不是寫死在 HTML 裡，而是每次動態請求這個 API，把最新內容即時更新在網頁裡。
簡單說，你看到的資料就是官方網站動態載入的來源，屬於資料介面，而非直接顯示內容。

此项目仅供教育目的。

