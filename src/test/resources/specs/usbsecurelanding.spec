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
    search-icon           xpath    .//header/div/nav//ul/li[@class='search-icon']/span
    appsdropdown          id       menu1
    dateSelectordd        id       menu2
    exportdropdown        id       menu3
    headinggraph1         xpath    (.//*[@id='chart']/div/div[contains(@class, 'chart-heading')])[1]
    headinggraph2         xpath    (.//*[@id='chart']/div/div[contains(@class, 'chart-heading')])[2]
    headinggraph3         xpath    (.//*[@id='chart']/div/div[contains(@class, 'chart-heading')])[3]
    headinggraph4         xpath    (.//*[@id='chart']/div/div[contains(@class, 'chart-heading')])[4]
    graph1                id       myChart1
    graph2                id       myChart2
    graph1                id       myChart3
    graph2                id       myChart4

= Secure Header Compomnent =
    @on Desktop
        header-container:
            inside screen 0px top
            color-scheme > 90% #F94453

        hamburger:
            inside header-container 0px left
            height ~ 60px

        left-menu-head:
            inside header-container
            right-of hamburger 29.8px

        logo-img:
            inside left-menu-head 90px left, 14.19px top
            height ~ 29.17px

        for-developers:
            inside left-menu-head 229px left
            right-of logo-img 28 to 30px
            height ~ 21 px

        user-info-container:
            inside header-container 125px right
        user-name:
            inside user-info-container 125px right
            right-of for-developers 447px
            height ~ 21px
            css font-size is "18px"
            css line-height is "21px"
        user-logo:
            inside user-info-container 89.2px right
            right-of user-name 14.18px
            height ~ 21.55px

        search-icon-container:
           inside header-container 0px right
           right-of user-info-container 0px
        search-icon:
           inside search-icon-container 22.5px right
           right-of user-logo 48.7px

= Fitler Compomnent =

