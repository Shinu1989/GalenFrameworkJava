@objects
    ToolsDoc        xpath  //div[@class='tool-container float-reset']/h1
    ToolSumry       xpath  //div[@class='tool-container float-reset']/p

    Tooltext        xpath  //div[@class='tool-container float-reset']/h2 
    CodeSnippet     xpath  //div[@class='tool-container float-reset']/pre
    CTA1            xpath  (//div[@class='tool-container float-reset']/div/a)[1]
    CTA2            xpath  (//div[@class='tool-container float-reset']/div/a)[2]
    ToolCntner      xpath  //div[@class='tool-container float-reset']
 
    Highlight1      xpath  (//div[@class='content-tile-img']/img)[1]
    Highlight2      xpath  (//div[@class='content-tile-img']/img)[2]
    Highlight3      xpath  (//div[@class='content-tile-img']/img)[3]
    Highlight4      xpath  (//div[@class='content-tile-img']/img)[4]
    HighlightTitle1 xpath  (//div[@class='content-tile-detail']/h3)[1]
    HighlightTitle2 xpath  (//div[@class='content-tile-detail']/h3)[2]
    HighlightTitle3 xpath  (//div[@class='content-tile-detail']/h3)[3]
    HighlightTitle4 xpath  (//div[@class='content-tile-detail']/h3)[4]
    HighligtSumary1 xpath  (//div[@class='content-tile-detail']/p)[1]
    HighligtSumary2 xpath  (//div[@class='content-tile-detail']/p)[2]
    HighligtSumary3 xpath  (//div[@class='content-tile-detail']/p)[3]
    HighligtSumary4 xpath  (//div[@class='content-tile-detail']/p)[4]

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
    hero-head                xpath .//section[contains(@class,'hero-banner')]/div/h2
    hero-para                xpath .//section[contains(@class,'hero-banner')]/div/p
    hero-cta1                xpath .//div[@class='cta-hero-banner']
    headline-component       xpath .//section[contains(@class, 'comp comp-headline')]
    help-component           xpath .//section[contains(@class,'comp comp-help')]
    help-first-leaf           xpath .//span[@id='Create Account']
    help-last-leaf           xpath .//section[contains(@class,'comp-help')]/div/ul/li[2]

= Header Component =
    @on Desktop
        header-container:
            inside screen 0px top
            height ~ 190px
            color-scheme > 90% #e03e4b

        left-menu-head:
            inside header-container 0px left

        logo-img:
            inside left-menu-head 75px left, 76px top
            height ~ 31px

        for-developers:
            inside left-menu-head 208px left
            right-of logo-img 23 to 25px
            height ~ 21 px

    @on tablet
        header-container:
            inside screen 0px top
            height ~ 60px
            color-scheme > 90% #e03e4b

        left-menu-head:
            inside header-container 0px left

        logo-img:
            inside left-menu-head 91px left, 13px top
            height ~ 31px

        for-developers:
            inside left-menu-head 229px left
            right-of logo-img 28 to 30px
            height ~ 21 px

    @on Mobile
        header-container:
            inside screen 0px top
            height ~ 607px
            color-scheme > 90% #e03e4b

        left-menu-head:
            inside header-container 0px left

        logo-img:
            inside left-menu-head 90px left, 13px top
            height ~ 31px

= Menu Head =
    @on Desktop
        right-menu-head:
             inside header-container
             right-of for-developers

    @on Desktop
        right-menuhead-items-1:
            inside right-menu-head
            right-of for-developers 413px

        right-menuhead-items-*:
            inside right-menu-head
            height ~ 21px

        @forEach [right-menuhead-items-*] as menuItem, prev as previousMenuItem
            ${menuItem}:
                right-of ${previousMenuItem} 52 to 54px
                aligned horizontally all ${previousMenuItem}

    @on tablet
        right-menu-head:
             inside header-container
             below left-menu-head 0px

    @on tablet
        right-menuhead-items-1:
            inside right-menu-head
            below for-developers 131px

        right-menuhead-items-*:
            inside right-menu-head
            height ~ 48px

        @forEach [right-menuhead-items-*] as menuItem, prev as previousMenuItem
            ${menuItem}:
                below ${previousMenuItem} 28 to 30px
                aligned horizontally all ${previousMenuItem}

    @on Mobile
        right-menu-head:
             inside header-container

    @on Mobile
        right-menuhead-items-1:
            inside right-menu-head 12px left
            below right-menu-head

        right-menuhead-items-*:
            inside right-menu-head
            height ~ 31px

        @forEach [right-menuhead-items-*] as menuItem, prev as previousMenuItem
            ${menuItem}:
                below ${previousMenuItem} 32 to 35px
                aligned horizontally all ${previousMenuItem}


= Hero Component =
    @on Desktop
        hero-banner:
            inside screen 0px top
            color-scheme > 90% #e03e4b

        hero-head:
            inside hero-banner 72px left, 212px top
            height ~ 60px
            css font-size is "50px"
            css line-height is "58px"

        hero-para:
            inside hero-banner 72px left, 270px top
            below hero-head 0px
            height ~ 58px
            css font-size is "50px"
            css line-height is "58px"

        hero-cta1:
            inside hero-banner 75px left, 432px top
            below hero-para 104 px
            height ~ 50px
            css font-size is "16px"
            css line-height is "18px"

    @on tablet
        hero-banner:
            inside screen 0px top
            color-scheme > 90% #e03e4b

        hero-head:
            inside hero-banner 52px left
            height ~ 38px
            css font-size is "32px"
            css line-height is "38px"

        hero-para:
            inside hero-banner 52px left
            below hero-head 0px
            height ~ 38px
            css font-size is "32px"
            css line-height is "38px"

        hero-cta1:
            inside hero-banner 52px left, 432px top
            below hero-para 71px
            height ~ 40px
            css font-size is "14px"
            css line-height is "16px"

    @on Mobile
        hero-banner:
            inside screen 0px top
            color-scheme > 90% #e03e4b

        hero-head:
            inside hero-banner 48px left, 77px top
            height ~ 60px
            css font-size is "32px"
            css line-height is "39px"

        hero-para:
            inside hero-banner 48px left, 270px top
            below hero-head 0px
            height ~ 58px
            css font-size is "32px"
            css line-height is "39px"

        hero-cta1:
            inside hero-banner 46px left, 263px top
            below hero-para 30px
            height ~ 40px
            css font-size is "14px"
            css line-height is "16px"

=  Highlights Component =
    @on Desktop

        Highlight1:
                  width 62 to 67px
                  height 81 to 87px
                  inside screen ~ 183px left

        Highlight2:
                  width 60 to 66px
                  height 98 to 104px
                  inside screen ~ 492px left
                  right-of Highlight1 ~ 244px


        Highlight3:
                  width 78 to 86px
                  height 78 to 86px
                  inside screen ~ 787px left
                  right-of Highlight2 ~ 233px


        Highlight4:
                  width 78 to 86px
                  height 78 to 86px
                  inside screen ~ 1093px left
                  right-of Highlight3 ~ 224px

        HighlightTitle1:
                       width 169 to 175px
                       height 23 to 31px
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen ~ 130px left
                       below Highlight1 ~ 36px


        HighlightTitle2:
                       width 186 to 192px
                       height 23 to 29px
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen ~ 427px left
                       below Highlight2 19 to 25px
                       right-of HighlightTitle1 ~ 124px
        HighlightTitle3:
                       width 282 to 289px
                       height 23 to 29px
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen ~ 684px left
                       below Highlight3 ~ 37px
                       right-of HighlightTitle2 ~ 67px
        HighlightTitle4:
                       width 234 to 242px
                       height 23 to 29px
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen ~ 1013px left
                       below Highlight4 ~ 37px
                       right-of HighlightTitle3 ~ 44px

        HighligtSumary1:
                       width 227 to 235px
                       height 51 to 57px
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen ~ 100px left
                       below HighlightTitle1 14 to 19px


        HighligtSumary2:
                       width 208 to 215px
                       height 33 to 39px
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen ~ 413	px left
                       below HighlightTitle2 14 to 19px
                       right-of HighligtSumary1 ~ 82px

        HighligtSumary3:
                       width 214 to 222px
                       height 51 to 57px
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen ~ 717px left
                       below HighlightTitle3 14 to 19px
                       right-of HighligtSumary2 ~ 92px

        HighligtSumary4:
                       width 196 to 204px
                       height 51 to 57px
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen ~ 1033px left
                       below HighlightTitle3 14 to 19px
                       right-of HighligtSumary3 ~ 97px

    @on Mobile

        Highlight1:
                  width 62 to 67px
                  height 81 to 87px
                  inside screen ~ 155px left

        Highlight2:
                  width 60 to 66px
                  height 98 to 104px
                  inside screen ~ 156px left
                  below Highlight1 ~ 185px


        Highlight3:
                  width 80 to 86px
                  height 80 to 86px
                  inside screen ~ 147px left
                  below Highlight2 ~ 155px


        Highlight4:
                  width 76 to 83px
                  height 76 to 83px
                  inside screen ~ 148px left
                  below Highlight3 ~ 166px

        HighlightTitle1:
                       width 260 to 266px
                       height 23 to 31px
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen ~ 53px left
                       below Highlight1 ~ 22px


        HighlightTitle2:
                       width 273 to 279px
                       height 23 to 29px
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen ~ 50px left
                       below Highlight2 5 to 11px

        HighlightTitle3:
                       width 273 to 279px
                       height 23 to 29px
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen ~ 52px left
                       below Highlight3 ~ 23px

        HighlightTitle4:
                       width 258 to 266px
                       height 23 to 29px
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen ~ 54px left
                       below Highlight4 ~ 24px


        HighligtSumary1:
                       width 272 to 278px
                       height 36 to 44px
                       css font-size is "14px"
                       css line-height is "20px"
                       inside screen ~ 51px left
                       below HighlightTitle1 12 to 18px


        HighligtSumary2:
                       width 279 to 285px
                       height 36 to 43px
                       css font-size is "14px"
                       css line-height is "20px"
                       inside screen ~ 53px left
                       below HighlightTitle2 11 to 17px


        HighligtSumary3:
                       width 274 to 280px
                       height 33 to 40px
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen ~ 52px left
                       below HighlightTitle3 12 to 18px


        HighligtSumary4:
                       width 260 to 267px
                       height 51 to 57px
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen ~ 53px left
                       below HighlightTitle3 12 to 18px
    @on tablet

        Highlight1:
                  width 62 to 67px
                  height 81 to 87px
                  inside screen ~ 212px left

        Highlight2:
                  width 60 to 66px
                  height 98 to 104px
                  inside screen ~ 494px left
                  right-of Highlight1 ~ 217px


        Highlight3:
                  width 80 to 86px
                  height 80 to 86px
                  inside screen ~ 202px left
                  below Highlight1 ~ 172px


        Highlight4:
                  width 76 to 83px
                  height 76 to 83px
                  inside screen ~ 485px left
                  below Highlight4 ~ 160px

        HighlightTitle1:
                       width 252 to 260px
                       height 23 to 31px
                       css font-size is "21px"
                       css line-height is "26px"
                       inside screen ~ 115px left
                       below Highlight1 ~ 33px


        HighlightTitle2:
                       width 252 to 260px
                       height 23 to 31px
                       css font-size is "21px"
                       css line-height is "26px"
                       inside screen ~ 50px left
                       below Highlight2 16 to 23px
                       right-of  HighlightTitle1 ~ 25px

        HighlightTitle3:
                       width 273 to 279px
                       height 23 to 29px
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen ~ 115px left
                       below Highlight3 ~ 38px

        HighlightTitle4:
                       width 273 to 279px
                       height 23 to 29px
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen ~ 406px left
                       below Highlight4 ~ 39px
                       right-of HighlightTitle3 ~ 35px


        HighligtSumary1:
                       width 253 to 259px
                       height 51 to 57px
                       css font-size is  "14px"
                       css line-height is "18px"
                       inside screen ~ 115px left
                       below HighlightTitle1 5 to 12px


        HighligtSumary2:
                       width 253 to 259px
                       height 33 to 39px
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen ~ 396px left
                       below HighlightTitle2 5 to 12px
                       right-of HighligtSumary1 ~ 25px


        HighligtSumary3:
                       width 253 to 259px
                       height 51 to 57px
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen ~ 115px left
                       below HighlightTitle3 9 to 14px


        HighligtSumary4:
                       width 253 to 259px
                       height 51 to 57px
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen ~ 53px left
                       below HighlightTitle3 9 to 13px
                       right-of HighligtSumary3 ~ 26px

= CodeSnippet Component =
    @on Desktop

        ToolsDoc:
                width 373 to 381px
                height 27 to 33px
                css font-size is "34px"
                css line-height is "31px"
                inside screen ~ 486px left


        ToolSumry:
                 width 373 to 381px
                 height 87 to 93px
                 css font-size is "14px"
                 css line-height is "18px"
                 inside screen ~ 486px left
                 below ToolsDoc ~ 27px

        Tooltext:
                width 373 to 381px
                height 11 to 17px
                css font-size is "12px"
                css line-height is "14px"
                inside screen ~ 486px left
                below ToolSumry ~ 29px

        CodeSnippet:
               width  584 to 592px
               height 313 to 320px
               inside screen ~ 381px left
               below Tooltext ~ 31px
               css font-size is "14px"
               css line-height is "17px"
        CTA1:
            width 215 to 221px
            height 47 to 53px
            inside screen ~ 446px left
            css font-size is "14px"
            css line-height is "16px"
            below CodeSnippet  ~ 28px

        CTA2:
            width 215 to 221px
            height 47 to 53px
            inside screen ~ 686px left
            css font-size is "14px"
            css line-height is "16px"
            below CodeSnippet  ~ 28px

	@on Mobile

        ToolsDoc:
                width 108 to 288px
                height 59 to 65px
                css font-size is "28px"
                css line-height is "31.008px"
                inside screen ~ 56px left


        ToolSumry:
                 width 285 to 290px
                 height 105 to 111px
                 css font-size is "14px"
                 css line-height is "18px"
                 inside screen ~ 44px left
                 below ToolsDoc ~ 20px

        Tooltext:
                width 297 to 303px
                height 11 to 17px
                css font-size is "12px"
                css line-height is "14px"
                inside screen ~ 38px left
                below ToolSumry 19 to 26px

        CodeSnippet:
               width  347 to 353px
               height 411 to 417px
               inside screen ~ 13px left
               below Tooltext ~ 22px
               css font-size is "14px"
               css line-height is "17px"
        CTA1:
            width 157 to 163px
            height 37 to 43px
            inside screen ~ 16px left
            css font-size is "14px"
            css line-height is "16px"
            below CodeSnippet ~ 30px

        CTA2:
            width 157 to 163px
            height 37 to 43px
            inside screen ~ 198px left
            css font-size is "14px"
            css line-height is "16px"
            right-of CTA1 ~ 22px
            below CodeSnippet ~ 30px

	@on tablet
     
        ToolsDoc:
                width 381 to 387px
                height 28 to 33px
                css font-size is "28px"
                css line-height is "31px"
                inside screen ~ 193px left
                

        ToolSumry:
                 width 381 to 387px
                 height 68 to 75px
                 css font-size is "14px"
                 css line-height is "18px"
                 inside screen ~ 193px left
                 below ToolsDoc ~ 23px
                 
        Tooltext:
                width 567 to 574px
                height 11 to 17px
                css font-size is "12px"
                css line-height is "14px"
                inside screen ~ 100px left
                below ToolSumry ~ 26px
 
        CodeSnippet:
               width  584 to 592px
               height 312 to 319px
               inside screen ~ 90px left
               below Tooltext ~ 31px
               css font-size is "14px"
               css line-height is "17px"
        CTA1:
            width 157 to 163px
            height 37 to 43px
            inside screen ~ 211px left
            css font-size is "14px"
            css line-height is "16px"
           
           
        CTA2: 
            width 157 to 163px
            height 37 to 43px
            inside screen ~ 397px left
            css font-size is "14px"
            css line-height is "16px"
            right-of CTA1 ~ 26px

= Help Component =
    @on Desktop
        help-component:
            below headline-component
            inside screen 0px left
            height ~ 240px

        help-first-leaf:
            inside help-component 486px left
            height ~ 31px
            css font-size is "34px"
            css line-height is "31px"

        help-last-leaf:
                    inside help-component 566px left
                    below help-first-leaf
                    height ~ 50px
                    css font-size is "14px"
                    css line-height is "16px"
    @on Mobile
        help-component:
            below headline-component
            inside screen 0px left
            height ~ 263px

        help-first-leaf:
             inside help-component 15px left
             height ~ 31px
             css font-size is "28px"
             css line-height is "31px"

        help-last-leaf:
              inside help-component 108px left
              below help-first-leaf
              height ~ 40px
              css font-size is "14px"
              css line-height is "16px"

    @on tablet
        help-component:
                    below headline-component
                    inside screen 0px left
                    height ~ 240px

        help-first-leaf:
                    inside help-component 0px left
                    height ~ 31px
                    css font-size is "34px"
                    css line-height is "31px"

        help-last-leaf:
                    inside help-component 270px left
                    below help-first-leaf 30px
                    height ~ 50px
                    css font-size is "14px"
                    css line-height is "16px"

= Footer =
    @on Desktop
        footer-container:
            inside screen 0px bottom
            height ~ 102px
            color-scheme > 80% #f14d5a

        footer-copy-right:
            inside footer-container 50 to 52px left

    @on tablet
        footer-container:
            inside screen 0px left, 0px bottom
            height ~ 102px
            color-scheme > 80% #f14d5a

        footer-copy-right:
            inside footer-container 53 to 55px left

    @on Mobile
        footer-container:
            inside screen 0px bottom
            height ~ 250px
            color-scheme > 80% #f14d5a

        footer-copy-right:
            inside footer-container 0px left
            height ~ 19px


= Menu Footer =
    @on Desktop
        footer-right-menu:
             inside footer-container
             right-of footer-copy-right

    @on Desktop
        footer-rtmenu-items-1:
            inside footer-right-menu 301 to 303px right
            height ~ 20px
            color-scheme = 5% #ffffff

        footer-rtmenu-items-*:
            inside footer-right-menu
            height ~ 20px

        @forEach [footer-rtmenu-items-*] as menuItem, prev as previousMenuItem
            ${menuItem}:
                right-of ${previousMenuItem} 39 to 40px

    @on tablet
        footer-right-menu:
               inside footer-container
               right-of footer-copy-right

    @on tablet
        footer-rtmenu-items-1:
              inside footer-right-menu 230 to 232px right
              height ~ 20px
              color-scheme = 5% #ffffff

        footer-rtmenu-items-*:
              inside footer-right-menu
              height ~ 20px

        @forEach [footer-rtmenu-items-*] as menuItem, prev as previousMenuItem
              ${menuItem}:
                  right-of ${previousMenuItem} 26 to 28px

    @on Mobile
        footer-right-menu:
             inside footer-container
             above footer-copy-right

    @on Mobile
        footer-rtmenu-items-1:
            inside footer-right-menu 0px right
            height ~ 20px
            color-scheme = 5% #ffffff

        footer-rtmenu-items-*:
            inside footer-right-menu
            height ~ 20px

        @forEach [footer-rtmenu-items-*] as menuItem, prev as previousMenuItem
            ${menuItem}:
                below ${previousMenuItem} 15 to 18px
           
           