# HoneyGainManager - 蜜罐裝置管理器
基於 PyWebIO 實現的一個簡易 HoneyGain 裝置狀態顯示，並支援多個帳號

# 功能
- [X] 顯示各裝置狀態
- [X] 支援多帳號
- [X] 自動領取蜜罐

可以修改 `config.json` 中的 `dashbaord_type` 參數來改變顯示方式
支援的參數有
* honeygain
* jumptask

`honeygain` 會顯示詳細的裝置資訊以及擁有的星點

`jumptask` 僅顯示擁有的 JMPT 數量以及其總計美金價值

### 請注意 `Honeygain` 與 `Jumptask` 的 `Token` 不同，但取得方式同理
# 效果圖
Honeygain

![image](https://user-images.githubusercontent.com/25722976/168449617-ec58c3df-04fa-4e9c-a7f0-a8a65bfcfa94.png)

Jumptask

![image](https://user-images.githubusercontent.com/25722976/168487531-b7d5f4e0-424e-43dd-bfef-1295874cdc6d.png)


# 使用方式
自己到網站取 `Header` 中的 `Bearer` 的 `Token` 部分，並丟到 `config.json` 下

如不想自動領取蜜罐，請將 `config.json` 底下的 `auto_get_contest_winnings` 設置為 `false` 即可

# 桌上版本
如需已編譯版本可至 [Release](https://github.com/ontisme/HoneyGainManager/releases/tag/v1.0.1) 下載單獨執行文件

# 什麼是HoneyGain?
一個依賴你IP掛機賺錢的網站，每月收益10~20美金不等，有興趣的話可以使用我的[推薦連結](https://r.honeygain.me/ONTISAC9BA)
