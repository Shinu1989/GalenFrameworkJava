
@objects
    header-container         xpath .//div[@class='container-fluid reset-padding']/header
    left-menu-head           xpath .//header/div[@class='header-left']
    logo-img                 xpath .//img[@class='logo-img']
    for-developers           xpath .//header//div/span[@class='for-dev']
    right-menu-head          xpath .//header/div/ul[@class='menu']
    right-menuhead-items-*   xpath .//header/div/ul/li
    footer-container         xpath .//footer[@class='comp comp-footer col-desk-12 col-mob-4 col-tab-8 usb-section']
    footer-copy-right        xpath .//footer/div[contains(@class,'footer-left')]
    footer-right-menu        xpath .//footer/div/ul[@class='menu']
    footer-rtmenu-items-*    xpath .//footer/div/ul/li
    hero-banner              xpath .//section/div[@class='hero-banner-container']
    highlight-component      xpath .//section[contains(@class,'comp comp-tiles')]
    tools-component          xpath .//section/div[contains(@class,'tool-container')]
    headline-component       xpath .//section[contains(@class, 'comp comp-headline')]
    help-component           xpath .//section[contains(@class,'comp comp-help')]


= Header =
    @on Desktop
        header-container:
            inside screen 0px top
            height ~ 190px
            color-scheme > 90% #e03e4b
            width 1000px

        left-menu-head:
            inside header-container 0px left, 80px top

        logo-img:
            inside left-menu-head 18 to 22px left, 0px top

        for-developers:
                    inside left-menu-head 145 to 150px left
                    right-of logo-img 18 to 20px


= Highlight Component =
        highlight-component:
                   below header-container

= Tools Component =
        tools-component:
                   below hero-banner

= Headline Component =
        headline-component:
                   below tools-component

= Help Component =
        help-component:
                   below headline-component

= Menu Head =
    @on Desktop
        right-menu-head:
             inside header-container 45 to 55px right
             right-of for-developers 10 to 15px

    @on Desktop
        right-menuhead-items-1:
            inside right-menu-head 700 to 800 px right, -2px top
            #height ~ 50px
            color-scheme > 20% #e03e4b

        right-menuhead-items-*:
            inside right-menu-head, -2px top
            height ~ 80px

        @forEach [right-menuhead-items-*] as menuItem, prev as previousMenuItem
            ${menuItem}:
                right-of ${previousMenuItem} 40 to 60px
                aligned horizontally all ${previousMenuItem}

= Footer Component =
    @on Desktop
        footer-container:
            inside screen 0px bottom
            height ~ 150px
            color-scheme > 80% #f14d5a
            width 1000px

        footer-copy-right:
            inside footer-container 50 to 55px left


= Menu Footer =
    @on Desktop
        footer-right-menu:
             inside footer-container 50 to 55px right
             right-of footer-copy-right 10 to 15px

    @on Desktop
        footer-rtmenu-items-1:
            inside footer-right-menu 500 to 505px right, 43px bottom
            #height ~ 20px
            color-scheme = 5% #ffffff

        footer-rtmenu-items-*:
            inside footer-right-menu
            height ~ 45px

        @forEach [footer-rtmenu-items-*] as menuItem, prev as previousMenuItem
            ${menuItem}:
                right-of ${previousMenuItem} -555 to 15px