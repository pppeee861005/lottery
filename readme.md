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

此项目仅供教育目的。
