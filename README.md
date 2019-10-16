# -Machine-Learning-1081-0316-Project-management-HW3

輸入資料，輸入10個 log files，總共 21,978 frames，資料排列如下
x軸為ball的x座標，y軸為ball的y座標，z為該求出現在此座標的數量

![image](https://github.com/wasteee/-Machine-Learning-1081-0316-Project-management-HW3/blob/master/graph/kmeans.png)

對映到遊戲畫面

![image](https://github.com/wasteee/-Machine-Learning-1081-0316-Project-management-HW3/blob/master/graph/Inkedkmeans_LI.jpg)

上圖為每個xy軸皆取一次z，因此較為密集且不易觀看，可將xy改成每5格取一次z

![image](https://github.com/wasteee/-Machine-Learning-1081-0316-Project-management-HW3/blob/master/graph/kmeans_per5.png)

此圖可看見球的路徑有三處較多，且有部分區域是沒有出現過的
我們可以改用另一種表示方式，將球沒有經過的座標z值改為2，有經過的改為0

![image](https://github.com/wasteee/-Machine-Learning-1081-0316-Project-management-HW3/blob/master/graph/kmeansnodata_per5.png)

而透過此圖就可以較為明顯的看出來仍有許多座標是沒有被記錄到 log files內的
若拿此資料下去做訓練，則資料量會不足
所以我們將log files的數量增加到1,146個，總共 1,989,834 frames
資料排列如下圖

![image](https://github.com/wasteee/-Machine-Learning-1081-0316-Project-management-HW3/blob/master/graph/alldata_per5.png)

可以看到每個座標的分布更為多的
再來看有哪些座標是沒有被記錄的

![image](https://github.com/wasteee/-Machine-Learning-1081-0316-Project-management-HW3/blob/master/graph/allnodata_per5.png)

則可以看到其中有大部分的資料都有被記錄
但是在左下的部分則出現一個三角形的區域是明顯少很多資料的
對映到遊戲畫面大概是下方所顯示的部分

![image](https://github.com/wasteee/-Machine-Learning-1081-0316-Project-management-HW3/blob/master/graph/gaming.PNG)

而此詳細原因還需要再做研究
