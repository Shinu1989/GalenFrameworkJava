@objects
    header-container      xpath    .//header/div/nav/div[@class='navbar-header']
    hamburger             xpath    .//header[@id='secure-header']//nav//button
    left-menu-head        xpath    .//header//nav//div[@class='header-left']
    logo-img              xpath    .//img[@class='logo-img']
    for-developers        xpath    .//header//nav//div/span[contains(@class, 'developers')]
    user-info-container   xpath    .//header/div/nav//ul/li[contains(@class,'name')]
    user-name             xpath    .//header/div/nav//ul/li[contains(@class,'name')]/a
    user-logo             xpath    .//header/div/nav//ul/li[contains(@class,'name')]/span
    search-icon-container xpath    .//header/div/nav//ul/li[@class='search-icon']
    search-icon           xpath    .//header/div/nav//ul/li[@class='search-icon']//span
    appsdropdown          id       menu1
    dateSelectordd        id       menu2
    exportdropdown        id       menu3
    headinggraph1         xpath    (.//*[@id='chart']/div/div[contains(@class, 'chart-heading')])[1]
    headinggraph2         xpath    (.//*[@id='chart']/div/div[contains(@class, 'chart-heading')])[2]
    headinggraph3         xpath    (.//*[@id='chart']/div/div[contains(@class, 'chart-heading')])[3]
    headinggraph4         xpath    (.//*[@id='chart']/div/div[contains(@class, 'chart-heading')])[4]
    graph1                id       myChart1
    graph2                id       myChart2
    graph3                id       myChart3
    graph4                id       myChart4

= Secure Header Component =
    @on Desktop
        hamburger:
            inside screen  6 to 16px left
            inside screen  73 to 85px top     
        logo-img:
            inside screen  51 to 62px left
            inside screen  73 to 85px top
        for-developers:
            inside screen  182 to 196px left
            inside screen  73 to 85px top      
        user-name:
            inside screen  1001 to 1013px left
            inside screen  73 to 85px top
            css font-size is "18px"
            css line-height is "21px"
        user-logo:
            inside screen  1100 to 1112px left
            inside screen  73 to 85px top
        search-icon-container:
            inside screen  1141 to 1152px left
            inside screen  73 to 85px top
        search-icon:
            inside screen  1175 to 1186px left
            inside screen  73 to 85px top

    @on Mobile
        hamburger:
            inside screen  3 to 13px left
            inside screen  0px top       
        logo-img:
            inside screen  130 to 140px left
            inside screen  7 to 19px top
        search-icon-container:
            inside screen  473 to 485px left
            inside screen  0px top
        search-icon:
            inside screen  533 to 544px left
            inside screen  18 to 28px top
    @on Tablet        
         hamburger:
            inside screen  6 to 16px left
            inside screen  0px top
         
         logo-img:
            inside screen  107 to 118px left
            inside screen  10 to 20px top
         for-developers:
            inside screen  283 to 295px left
            inside screen  15 to 25px top        
         user-name:
            inside screen  641 to 652px left
            inside screen  15 to 25px top
            css font-size is "18px"
            css line-height is "21px"
         user-logo:
            inside screen  852 to 862px left
            inside screen  13 to 23px top
         search-icon-container:
            inside screen  923 to 935px left
            inside screen  0px top
         search-icon:
            inside screen  938 to 950px left
            inside screen  18 to 29px top

= Fitler Component =
    @on Desktop
        appsdropdown:
            inside screen 6 to 16px left                       
          
        dateSelectordd:             
            right-of appsdropdown 0px    
                  
        exportdropdown:                             
            right-of dateSelectordd 0px
            
    @on Mobile
        appsdropdown:
            inside screen 11 to 22px left           
            
        dateSelectordd:
            below appsdropdown 0px            
           
        exportdropdown:            
            below appsdropdown 0px
            
            
            
= Graph Head Component =
    @on Desktop
        headinggraph1:
           inside screen 45 to 56px left
           below appsdropdown 29.34px          
           css font-size is "20px"
           css line-height is "24px"
        headinggraph2:           
           inside screen 640 to 650px left
           inside screen  73 to 85px top
           css font-size is "20px"
           css line-height is "24px"
        headinggraph3:
           inside screen 45 to 56px left            
           below headinggraph1 294px         
           css font-size is "20px"
           css line-height is "24px"
        headinggraph4:
           inside screen 640 to 650px left
           inside screen  73 to 85px top           
           css font-size is "20px"
           css line-height is "24px"

    @on Mobile
        headinggraph1:
           inside screen 49 to 59px left           
           below appsdropdown 90.34px          
           css font-size is "20px"
           css line-height is "24px"
        headinggraph2:
           inside screen 49 to 59px left          
           below headinggraph1 239 to 233px
           css font-size is "16px"
           css line-height is "20px"
        headinggraph3:
           inside screen 49 to 59px left
           below headinggraph2 239 to 233px         
           css font-size is "16px"
           css line-height is "20px"
        headinggraph4:
           inside screen 49 to 59px left
           below headinggraph3 239 to 233px           
           css font-size is "16px"
           css line-height is "20px"

    @on tablet
        headinggraph1:
           inside screen 69 to 79px left
           below appsdropdown 40.34px         
           css font-size is "22px"
           css line-height is "26px"
        headinggraph2:
           inside screen 69 to 79px left
           below headinggraph1 459 to 463px           
           css font-size is "22px"
           css line-height is "26px"
        headinggraph3:
           inside screen 69 to 79px left
           below headinggraph2 459 to 463px           
           css font-size is "22px"
           css line-height is "26px"
        headinggraph4:
           inside screen 69 to 79px left
           below headinggraph3 459 to 463px         
           css font-size is "22px"
           css line-height is "26px"

= Graph Component =
    @on Desktop
        graph1:
           inside screen 30 to 42px left
           below headinggraph1 7.5px
        graph2:
           inside screen 622 to 634px left
           below headinggraph2 7.5px
        graph3:
           inside screen 30 to 42px left
           below headinggraph3 7.5px
        graph4:
           inside screen 622 to 634px left
           below headinggraph4 7.5px

    @on Mobile
        graph1:
           inside screen 20 to 32px left
           below headinggraph1 9.64px
        graph2:
           inside screen 20 to 32px left
           below headinggraph2 9.64px
        graph3:
           inside screen 20 to 32px left
           below headinggraph2 9.64px
        graph4:
           inside screen 20 to 32px left
           below headinggraph2 9.64px

    @on tablet
        graph1:
           inside screen 28 to 40px left
           below headinggraph1 24.11px
        graph2:
           inside screen28 to 40px left
           below headinggraph2 24.11px
        graph3:
           inside screen 28 to 40px left
           below headinggraph2 24.11px
        graph4:
           inside screen 28 to 40px left
           below headinggraph3 24.11px
