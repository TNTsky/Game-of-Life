# 康威生命遊戲
## 介紹
    康威生命遊戲是於1970年由英國數學家約翰康威(John Horton Conway)首先提出的細胞自動機。
    它建構在一個方格的世界中，一個方格稱做一個「細胞」，
    細胞會遵循一定的規則改變它的生命狀態，細胞的狀態可以是存活或死亡，
    並且此刻的細胞狀態將會影響下一代的細胞狀態，如此不斷地演化下去，
    藉此觀察細胞的各種行為和演化。
    本次將透過Python程式來實現這個遊戲。
## 繁衍規則
細胞的繁衍遵循以下幾條規則:
+ 孤獨而死: 若細胞為存活狀態時，當周圍的存活細胞低於2個時（不包含2個），該細胞於下一刻死亡。
+ 生存競爭: 若細胞為存活狀態時，當周圍有超過3個存活細胞時，該細胞於下一刻死亡。
+ 舒適圈: 若細胞為存活狀態時，當周圍有2~3個存活的細胞時，細胞維持原樣。
+ 增殖繁衍: 若細胞為死亡狀態時，當周圍有3個存活細胞時，該細胞於下一刻復活。
## 操作提示
+ 在**方形模式**下點擊右鍵快速切換添加與移除功能
+ 在**方形模式**下使用滑鼠滾輪可改變範圍大小，點擊滾輪可將範圍縮至最小
+ 除**方形模式**外滾輪用以旋轉方向
+ **暫停狀態**下長按可連續放置
+ **執行狀態**下僅**方形模式**可連續放置
