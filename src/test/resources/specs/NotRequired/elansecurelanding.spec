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
        header-container:
            inside screen 0px top
        hamburger:
            inside header-container 0px left
            height 57 to 63px
        left-menu-head:
            inside header-container
            right-of hamburger 29.8px
        logo-img:
            inside left-menu-head 90px left, 14.19px top
            height 26 to 32px
        for-developers:
            inside left-menu-head 229px left
            right-of logo-img 28 to 30px
            height 18 to 24 px
        user-info-container:
            inside header-container 125px right
        user-name:
            inside user-info-container 125px right
            right-of for-developers 447px
            height 18 to 24 px
            css font-size is "18px"
            css line-height is "21px"
        user-logo:
            inside user-info-container 89.2px right
            right-of user-name 14.18px
            height 18 to 24 px
        search-icon-container:
           inside header-container 0px right
           right-of user-info-container 0px
        search-icon:
           inside search-icon-container 22.5px right
           right-of user-logo 48.7px

    @on Mobile
        header-container:
            inside screen 0px top
        hamburger:
            inside header-container 0px left
            height 57 to 63px
        left-menu-head:
            inside header-container
            right-of hamburger 29.8px
        logo-img:
            inside left-menu-head 90px left, 14.19px top
            height 26 to 32px
        search-icon-container:
           inside header-container 0px right, 0px top
           right-of left-menu-head
        search-icon:
           inside search-icon-container 22.5px right
           height 16 to 20px

    @on Tablet
        header-container:
             inside screen 0px top
        hamburger:
             inside header-container 0px left
             height 57 to 63px
        left-menu-head:
             inside header-container
             right-of hamburger 15px
        logo-img:
             inside left-menu-head 90px left, 14.19px top
             right-of hamburger 29.8px
             height 26 to 32px
        for-developers:
             inside left-menu-head 229px left
             right-of logo-img 28 to 30px
             height 18 to 24 px
        user-info-container:
             inside header-container
        user-name:
             inside user-info-container 125px right
             right-of for-developers 190px
             height 18 to 24 px
             css font-size is "18px"
             css line-height is "21px"
        user-logo:
             inside user-info-container 89.2px right
             right-of user-name 14.18px
             height 18 to 24 px
        search-icon-container:
            inside header-container 0px right
            right-of user-info-container 0px
        search-icon:
            inside search-icon-container 22.5px right
            right-of user-logo 48.7px


= Fitler Component =
    @on Desktop
        appsdropdown:
            inside screen 0px left
            below header-container 0px
            height 45.66 to 51.66px
        dateSelectordd:
            below header-container 0px
            right-of appsdropdown 0px
            height 45.66 to 51.66px
        exportdropdown:
            inside screen 0px right
            below header-container 0px
            right-of dateSelectordd 0px
            height 45.66 to 51.66px

    @on Mobile
        appsdropdown:
            inside screen 0px left
            below header-container 0px
            height 45 to 51px
        dateSelectordd:
            below appsdropdown 0px
            height 45 to 51px
        exportdropdown:
            inside screen 0px right
            below appsdropdown 0px
            right-of dateSelectordd 0px
            height 45 to 51px

= Graph Head Component =
    @on Desktop
        headinggraph1:
           inside screen 50px left, 138px top
           below appsdropdown 29.34px
           height 21 to 27px
           css font-size is "20px"
           css line-height is "24px"
        headinggraph2:
           inside screen 555px left, 138px top, 330px right
           right-of headinggraph1 350 to 353px
           height 21 to 27px
           css font-size is "20px"
           css line-height is "24px"
        headinggraph3:
           inside screen 50px left, 187px right
           below headinggraph1 294px
           height 21 to 27px
           css font-size is "20px"
           css line-height is "24px"
        headinggraph4:
           inside screen 555px left, 330px right
           below headinggraph1 294px
           height 21 to 27px
           css font-size is "20px"
           css line-height is "24px"

    @on Mobile
        headinggraph1:
           inside screen 35px left, 250px right
           below appsdropdown 90.34px
           height 17 to 23px
           css font-size is "20px"
           css line-height is "24px"
        headinggraph2:
           inside screen 35px left, 250px right
           below headinggraph1 239 to 233px
           height 21 to 27px
           css font-size is "16px"
           css line-height is "20px"
        headinggraph3:
           inside screen 35px left, 250px right
           below headinggraph2 239 to 233px
           height 21 to 27px
           css font-size is "16px"
           css line-height is "20px"
        headinggraph4:
           inside screen 35px left, 250px right
           below headinggraph3 239 to 233px
           height 21 to 27px
           css font-size is "16px"
           css line-height is "20px"

    @on tablet
        headinggraph1:
           inside screen 53px left, 149px top
           below appsdropdown 40.34px
           height 23 to 29px
           css font-size is "22px"
           css line-height is "26px"
        headinggraph2:
           inside screen 53px left
           below headinggraph1 459 to 463px
           height 23 to 29px
           css font-size is "22px"
           css line-height is "26px"
        headinggraph3:
           inside screen 53px left
           below headinggraph2 459 to 463px
           height 23 to 29px
           css font-size is "22px"
           css line-height is "26px"
        headinggraph4:
           inside screen 53px left
           below headinggraph3 459 to 463px
           height 23 to 29px
           css font-size is "22px"
           css line-height is "26px"

= Graph Component =
    @on Desktop
        graph1:
           inside screen 50px left, 169px top
           below headinggraph1 7.5px
        graph2:
           inside screen 553px left, 169px top, 17px right
           below headinggraph2 7.5px
        graph3:
           inside screen 50px left, 169px top
           below headinggraph3 7.5px
        graph4:
           inside screen 553px left, 169px top, 17px right
           below headinggraph4 7.5px

    @on Mobile
        graph1:
           inside screen 35.7px left, 12.15px right
           below headinggraph1 9.64px
        graph2:
           inside screen 35.7px left, 12.15px right
           below headinggraph2 9.64px
        graph3:
           inside screen 35.7px left, 12.15px right
           below headinggraph2 9.64px
        graph4:
           inside screen 35.7px left, 12.15px right
           below headinggraph2 9.64px

    @on tablet
        graph1:
           inside screen 54.81px left, 23px right
           below headinggraph1 24.11px
        graph2:
           inside screen 54.81px left, 23px right
           below headinggraph2 24.11px
        graph3:
           inside screen 54.81px left, 23px right
           below headinggraph2 24.11px
        graph4:
           inside screen 54.81px left, 23px right
           below headinggraph3 24.11px
