# API 取得方法

## 方法概述
本文檔說明如何從台灣樂透官方網站獲取彩券 API。

## 步驟 1: 開啟開發者工具
使用以下方式之一打開開發者工具：
- **Chrome**: F12 或右鍵點擊 → Inspect
- **Edge**: F12 或右鍵點擊 → Inspect
- **Firefox**: F12 或右鍵點擊 → Inspect Element

網址: https://www.taiwanlottery.com.tw

## 步驟 2: 查看網路請求
在開發者工具中：
1. 點擊「Network」標籤
2. 重新整理網頁（F5）

## 步驟 3: 篩選 AJAX 請求
在 Network 標籤中：
- 點擊「XHR/Fetch」篩選器，只顯示 AJAX 請求

## 步驟 4: 監控 API 呼叫
重新整理網頁時，查看網路標籤中的請求。您應該看到：
- 請求名稱：`lottolatestresult638649`

## 步驟 5: 檢查 API 回應
點擊該請求，然後：
1. 點擊「Response」標籤查看 JSON 回應
2. 點擊「Preview」查看格式化的數據

## 獲得的 API 資訊

### 基本 API 端點
```
https://api.taiwanlottery.com/TLCAPIWeBLottery/LatestResult
```

### 查詢特定期數
```
https://api.taiwanlottery.com/TLCAPIWeBLotterySuperLotto638Result?period=month&2025-01&pageSize=31
```

### 回應範例
JSON 回應包含：
- `superLotto638Result`: 超級大樂透開獎結果
- `drawNumberAppear`: 開出號碼（如：11, 18, 20, 25, 29, 37, 8）
- `period`: 期號（例如：114000089）

## 步驟 6: 提取 Headers（可選）
如果需要複製完整的 API 呼叫，包括 Headers：
```
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
```

## Python 實現範例

### 使用 requests 庫
```python
import requests

response = requests.get('https://api.taiwanlottery.com/TLCAPIWeBLottery/LatestResult')
data = response.json()
```

### 測試檔案
- `lottery.py`: 主要實現
- `testApi.py`: 測試 API

## 相關資源
- 台灣樂透官方網站: https://www.taiwanlottery.com.tw
- GitHub Repository: https://github.com/pppeee861005/lottery
