# HoneyGainManager - 蜜罐裝置管理器
基於 PyWebIO 實現的一個簡易 HoneyGain 裝置狀態顯示，並支援多個帳號

# 功能
- [X] 顯示各裝置狀態
- [X] 支援多帳號
- [X] 自動領取蜜罐

# 效果圖
![image](https://user-images.githubusercontent.com/25722976/168449617-ec58c3df-04fa-4e9c-a7f0-a8a65bfcfa94.png)

# 使用方式
自己到網站取 Header 中的 Bearer 的 Token 部分，並丟到 config.json 下
如不想自動領取蜜罐，請將 config.json 底下的 auto_get_contest_winnings 設置為 false 即可

# 桌上版本
如需已編譯版本可至 [Release](https://github.com/ontisme/HoneyGainManager/releases/tag/v1.0.1) 下載單獨執行文件
