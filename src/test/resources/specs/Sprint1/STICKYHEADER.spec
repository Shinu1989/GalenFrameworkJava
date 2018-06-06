@objects    
    header-container         xpath (//section[contains(@class,'comp')])[1]
    logo-img                 xpath //header[contains(@class,'app-header')]//img
    for-developers           xpath .//header//div/span[@class='for-dev']
    right-menu-head          xpath .//div/ul[@class='menu']
    right-menuhead-items-*   xpath .//div[@class='header-right']/ul/li
    right-menuhead-items-1   xpath (//div[@class='header-right']/ul/li/a)[1]   
    hamburger                xpath .//button[contains(@class,'burger-menu')]
    
= Header Component =
    @on Desktop
        logo-img:
            inside left-menu-head 0px left, 60px top
            height ~ 42px

        for-developers:           
            right-of logo-img 23 to 25px
            css font-size is "18px"
            css line-height is "21px"
            css color is "rgba(255, 255, 255, 1)"
            css font-family matches "roboto"
            css font-weight is "300"

    @on tablet

        logo-img:
            inside left-menu-head 6 to 16px left, ~77px top
            height ~ 42px

        for-developers:
            inside screen 229px left
            right-of logo-img 28 to 30px
            height ~ 21 px

    @on Mobile
        header-container:
            inside screen 0px top
            height ~ 607px
            color-scheme > 90% #1C3989

        left-menu-head:
            inside header-container 0px left

        logo-img:
            inside left-menu-head 90px left, 13px top
            height ~ 31px

