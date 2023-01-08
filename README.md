# twitter_project
This is repository for several twitter bot projects. 
I made three twitter bots. 

[1] [오늘의 뮤지컬 스케쥴](https://twitter.com/today_perform)  
[2] [지금 공연중인 뮤지컬 알림봇](https://twitter.com/now_performKr)    
[3] [{KR} 넷플릭스 상영 예정작 트윗봇](https://twitter.com/now_netflixKR) [(연관 블로그 포스트)](https://leeleelee3264.github.io/backend/2021/04/16/twitterbot-with-git-action.html) 



<br>

Basic system architecutre for the pojects is looking like this.  
![updated_twitter drawio (1)](https://user-images.githubusercontent.com/35620531/137567303-9155675c-932e-4331-8207-701b45f0f76f.png)

<br>
<br>

## [1] 오늘의 뮤지컬 스케쥴
<br>

| Start Date      | 2021-12-25                                          |
|-----------------|-----------------------------------------------------|
| End Date        | 2021-12-25                                          |
| Twitter Account | [@today_perform](https://twitter.com/today_perform) |  

<br> 

### Purpose of Project 
9 months ago, I built 'Now playing performance in Korea Bot' program. But it was only about which musicals are now playing in Korea.  
I wanted to make a musical bot with more information just like casting. Because most of musical fans think casting of the day is the most important part of the performance. They decide getting a ticket or not with casting info. So I built new one. 

<br> 


### development stack
| stack      | info |
|-----------------|------------|
| Backend language       |   python         |
| Backend api | twitter api |  
| Server | Ubuntu 20 |  
| Scheduler | Linux cron job |  

<br>

### Demo Image  
[<img src="https://user-images.githubusercontent.com/35620531/147377250-c05a47f8-c1f7-4630-99ad-1249c005c857.png" width="400"/>](https://user-images.githubusercontent.com/35620531/147377250-c05a47f8-c1f7-4630-99ad-1249c005c857.png)



<br>
<br>


## [2] 지금 공연중인 뮤지컬 알림봇  
<br>

| Start Date      | 2021-03-30 |
|-----------------|------------|
| End Date        | 2021-05-11  |
| Twitter Account | [@now_performKr](https://twitter.com/kr_now_perform) |  

<br>

### Purpose of Project 
I watch musical once per month. Everytime when I reserve tickets, I have to go check which musical is now playing and it's bothering me a little. 
So I thought maybe it will be way easier for me to have a twitter bot about on-going musical in Korea. I also figured that musical and acting are like package because of this, I added acting info too. 

<br> 

### development stack
| stack      | info |
|-----------------|------------|
| Backend language       |   python         |
| Backend api | twitter api |  
| Server | Ubuntu 20 |  
| Scheduler | Linux cron job |  

<br>

### Demo Image 

Sample 1             |  Sample2
:-------------------------:|:-------------------------:
[<img src="https://user-images.githubusercontent.com/35620531/117728880-03125800-b225-11eb-804a-9be3572da1e2.png" width="400"/>](https://user-images.githubusercontent.com/35620531/117728880-03125800-b225-11eb-804a-9be3572da1e2.png) |  [<img src="https://user-images.githubusercontent.com/35620531/177594817-adab7f83-ebb5-482f-83f9-0d8759c26fa3.png" width="400"/>](https://user-images.githubusercontent.com/35620531/177594817-adab7f83-ebb5-482f-83f9-0d8759c26fa3.png)


<br>
<br>

## [3] {KR} 넷플릭스 상영 예정작 트윗봇 

<br>


| Start Date      | 2021-03-16 |
|-----------------|------------|
| End Date        | 2021-03-28 |
| Twitter Account | [@now_netflixKR](https://twitter.com/now_netflixKR) |  

<br>

### Purpose of Project 
tweeting netflix korea's upcoming movie and drama in twitter for myself.<br> 

<br>

### development stack
| stack      | info |
|-----------------|------------|
| Backend language       |   python         |
| Backend api | twitter api |  
| Server | server less |  
| Scheduler | github action |  

<br>

### Demo Image
<br>   

Sample 1             |  Sample2
:-------------------------:|:-------------------------:
![](https://user-images.githubusercontent.com/35620531/112839670-6adb6c00-90d9-11eb-8a74-3ad7b1c156ca.PNG)  |  ![](https://user-images.githubusercontent.com/35620531/112840270-184e7f80-90da-11eb-81dd-7984814ae9cf.PNG)

<br>

### flow chart
![flow_img](https://leeleelee3264.github.io/assets/img/post/twitter_flow.png)





