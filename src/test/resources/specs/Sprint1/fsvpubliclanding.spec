@objects
    ToolsDoc        xpath  .//div[contains(@class,'tool-container')]/h2
    ToolSumry       xpath  .//p[contains(@class,'tool-description')]
    Tooltext        xpath  .//div/p[@class='code-head']
    CodeSnippet     xpath  .//pre[@class='code-conatiner']
    CTA1            xpath  (//div[contains(@class,'code-wrap-cta')]/a)[1]
    CTA2            xpath  (//div[contains(@class,'code-wrap-cta')]/a)[2]
    ToolCntner      xpath  //div[@class='tool-container float-reset'] 
    Highlight1      xpath  (//div[@class='content-tile-img']/img)[1]
    Highlight2      xpath  (//div[@class='content-tile-img']/img)[2]
    Highlight3      xpath  (//div[@class='content-tile-img']/img)[3]
    Highlight4      xpath  (//div[@class='content-tile-img']/img)[4]
    HighlightContainer1 xpath  (//*[contains(@class,'content-tile')]/a)[1]
    HighlightContainer2 xpath  (//*[contains(@class,'content-tile')]/a)[2]
    HighlightContainer3 xpath  (//*[contains(@class,'content-tile')]/a)[3]
    HighlightContainer4 xpath  (//*[contains(@class,'content-tile')]/a)[4]
    HighlightContainer5 xpath  (//*[contains(@class,'content-tile')]/a)[5]
    HighlightTitle1 xpath  (//div[@class='content-tile-detail']/h3)[1]
    HighlightTitle2 xpath  (//div[@class='content-tile-detail']/h3)[2]
    HighlightTitle3 xpath  (//div[@class='content-tile-detail']/h3)[3]
    HighlightTitle4 xpath  (//div[@class='content-tile-detail']/h3)[4]
    HighligtSumary1 xpath  (//div[@class='content-tile-detail']/p)[1]
    HighligtSumary2 xpath  (//div[@class='content-tile-detail']/p)[2]
    HighligtSumary3 xpath  (//div[@class='content-tile-detail']/p)[3]
    HighligtSumary4 xpath  (//div[@class='content-tile-detail']/p)[4]

    header-container         xpath .//header[contains(@class,'home-header')]
    left-menu-head           xpath .//div[@class='logo-wrapper']
    logo-img                 xpath (.//a/img[contains(@class,'logo-img')])[2]
    for-developers           xpath .//header//div/span[@class='for-dev']
    right-menu-head          xpath .//div/ul[@class='menu']
    right-menuhead-items-*   xpath .//div[@class='header-right']/ul/li
    right-menuhead-items-1   xpath (//div[@class='header-right']/ul/li/a)[1]
    footer-container         xpath .//footer[contains(@class,'comp-footer')]
    footer-copy-right        xpath .//div[contains(@class,'footer-left')]
    footer-right-menu        xpath .//footer/div/div[@class='footer-right']
    footer-rtmenu-items-*    xpath .//footer/div/div[@class='footer-right']/ul/li
    hero-banner              xpath .//div[contains(@class,'comp-hero-banner')]
    hero-head                xpath .//h1[@class='hero-head']
    hero-para                xpath .//p[@class='hero-para']
    hero-cta1                xpath .//div[contains(@class,'cta-hero')]/a[1]
    headline-component       xpath .//section[contains(@class, 'comp comp-headline')]
    help-component           xpath .//section[contains(@class,'comp-help')]
    help-first-leaf          xpath .//li[contains(@class,'first leaf')]/span
    help-last-leaf           xpath .//section/div/div/ul/li[2]/a
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
            color-scheme > 90% #001970

        left-menu-head:
            inside header-container 0px left

        logo-img:
            inside left-menu-head 90px left, 13px top
            height ~ 31px

= Menu Head =

    @on Desktop
        right-menuhead-items-1:
            inside screen ~69px top
            aligned horizontally all for-developers

        right-menuhead-items-*:
            inside right-menu-head
            height ~ 21px

        @forEach [right-menuhead-items-*] as menuItem, prev as previousMenuItem
            ${menuItem}:
                right-of ${previousMenuItem} 0px
                aligned horizontally all ${previousMenuItem}
                css font-size is "18px"
                css line-height is "21px"
                css color is "rgba(255, 255, 255, 1)"
                css font-family matches "roboto-light"
                

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
                css font-size is "28px"
                css line-height is "31px"


= Hero Component =
    @on Desktop
        hero-banner:
            inside screen 0px top

        hero-head:
            inside screen ~ 409px left, ~212px top
            css font-size is "50px"
            css line-height is "58px"
            css color is "rgba(255, 255, 255, 1)"
            css font-family matches "roboto"
            css font-weight is "300"

        hero-para:
            inside screen ~ 409px left
            below hero-head 0px
            css font-size is "50px"
            css line-height is "58px"
            css color is "rgba(255, 255, 255, 1)"
            css font-family matches "roboto-bold"

        hero-cta1:
            inside hero-banner ~ 429px left
            below hero-para ~55 px
            css font-size is "14px"
            css line-height is "16px"
            css color is "rgba(255, 255, 255, 1)"
            css font-family matches "roboto-bold"
            css background-color is "rgba(0, 25, 112, 1)"
            

    @on tablet
        hero-banner:
            inside screen 0px top
            
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
            

        hero-head:
            inside hero-banner 48px left, 77px top
            height ~ 60px
            css font-size is "32px"
            css line-height is "19px"

        hero-para:
            inside hero-banner 48px left, 270px top
            below hero-head 0px
            height ~ 58px
            css font-size is "32px"
            css line-height is "19px"

        hero-cta1:
            inside hero-banner 46px left, 263px top
            below hero-para 30px
            height ~ 40px
            css font-size is "14px"
            css line-height is "16px"

=  Highlights Component =
   @on Desktop
       
        HighlightContainer1:
                  inside screen 0px left
                  
        HighlightContainer2:
                  right-of  HighlightContainer1 0px
                  
        HighlightContainer3:
                  right-of  HighlightContainer2 0px
                  
        HighlightContainer4:
                  right-of  HighlightContainer3 0px

        Highlight1:
                  centered horizontally inside HighlightContainer1
                  
        Highlight2:
                  centered horizontally inside HighlightContainer2

        Highlight3:
                  centered horizontally inside HighlightContainer3

        Highlight4:
                  centered horizontally inside HighlightContainer4

        HighlightTitle1:
                  centered horizontally inside HighlightContainer1
                  below Highlight1 ~ 34px                  
                  css font-size is "22px"
                  css line-height is "26px"
                  css color is "rgba(24, 38, 117, 1)"
                  css font-family matches "roboto-bold"

        HighlightTitle2:
                  centered horizontally inside HighlightContainer2
                  below Highlight2 ~ 22px   
                  css font-size is "22px"
                  css line-height is "26px"
                  css color is "rgba(24, 38, 117, 1)"
                  css font-family matches "roboto-bold"

        HighlightTitle3:
                  centered horizontally inside HighlightContainer3
                  below Highlight3 ~ 36px   
                  css font-size is "22px"
                  css line-height is "26px"
                  css color is "rgba(24, 38, 117, 1)"
                  css font-family matches "roboto-bold"
                  
        HighlightTitle4:
                  centered horizontally inside HighlightContainer4
                  below Highlight4 ~ 36px   
                  css font-size is "22px"
                  css line-height is "26px"
                  css color is "rgba(24, 38, 117, 1)"
                  css font-family matches "roboto-bold"

        HighligtSumary1:
                  centered horizontally inside HighlightContainer1
                  below HighlightTitle1 ~ 17px                  
                  css font-size is "14px"
                  css line-height is "18px"
                  css color is "rgba(81, 84, 117, 1)"
                  css font-family matches "roboto"
                  css font-weight is "300"

        HighligtSumary2:
                  centered horizontally inside HighlightContainer2      
                  below HighlightTitle1 ~ 17px                  
                  css font-size is "14px"
                  css line-height is "18px"
                  css color is "rgba(81, 84, 117, 1)"
                  css font-family matches "roboto"
                  css font-weight is "300"


        HighligtSumary3:
                  centered horizontally inside HighlightContainer3 
                  below HighlightTitle1 ~ 17px                  
                  css font-size is "14px"
                  css line-height is "18px"
                  css color is "rgba(81, 84, 117, 1)"
                  css font-family matches "roboto"
                  css font-weight is "300"


        HighligtSumary4:
                  centered horizontally inside HighlightContainer3 
                  below HighlightTitle1 ~ 17px                  
                  css font-size is "14px"
                  css line-height is "18px"
                  css color is "rgba(81, 84, 117, 1)"
                  css font-family matches "roboto"
                  css font-weight is "300"


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
                       css color is "rgba(35, 36, 96, 1)"


        HighlightTitle2:
                       width 273 to 279px
                       height 23 to 29px
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen ~ 50px left
                       below Highlight2 5 to 11px
                       css color is "rgba(35, 36, 96, 1)"

        HighlightTitle3:
                       width 273 to 279px
                       height 23 to 29px
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen ~ 52px left
                       below Highlight3 ~ 23px
                       css color is "rgba(35, 36, 96, 1)"

        HighlightTitle4:
                       width 273 to 279px
                       height 23 to 29px
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen ~ 54px left
                       below Highlight4 ~ 24px
                       css color is "rgba(35, 36, 96, 1)"


        HighligtSumary1:
                       width 272 to 278px
                       height 36 to 44px
                       css font-size is "14px"
                       css line-height is "20px"
                       inside screen ~ 51px left
                       below HighlightTitle1 12 to 18px
                       css color is "rgba(81, 84, 117, 1)"

        HighligtSumary2:
                       width 279 to 285px
                       height 36 to 43px
                       css font-size is "14px"
                       css line-height is "20px"
                       inside screen ~ 53px left
                       below HighlightTitle2 11 to 17px
                       css color is "rgba(81, 84, 117, 1)"

        HighligtSumary3:
                       width 274 to 280px
                       height 33 to 40px
                       css font-size is "14px"
                       css line-height is "20px"
                       inside screen ~ 52px left
                       below HighlightTitle3 12 to 18px
                       css color is "rgba(81, 84, 117, 1)"


        HighligtSumary4:
                       width 260 to 267px
                       height 51 to 57px
                       css font-size is "14px"
                       css line-height is "20px"
                       inside screen ~ 53px left
                       below HighlightTitle3 12 to 18px
                       css color is "rgba(81, 84, 117, 1)"
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
                       css color is "rgba(35, 36, 96, 1)"
                       css font-family matches "roboto-bold"


        HighlightTitle2:
                       width 252 to 260px
                       height 23 to 31px
                       css font-size is "21px"
                       css line-height is "26px"
                       inside screen ~ 50px left
                       below Highlight2 16 to 23px
                       right-of  HighlightTitle1 ~ 25px
                       css color is "rgba(35, 36, 96, 1)"
                       css font-family matches "roboto-bold"
        HighlightTitle3:
                       width 273 to 279px
                       height 23 to 29px
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen ~ 115px left
                       below Highlight3 ~ 38px
                       css color is "rgba(35, 36, 96, 1)"
                       css font-family matches "roboto-bold"

        HighlightTitle4:
                       width 273 to 279px
                       height 23 to 29px
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen ~ 406px left
                       below Highlight4 ~ 39px
                       right-of HighlightTitle3 ~ 35px
                       css color is "rgba(35, 36, 96, 1)"
                       css font-family matches "roboto-bold"


        HighligtSumary1:
                       width 253 to 259px
                       height 51 to 57px
                       css font-size is  "14px"
                       css line-height is "18px"
                       inside screen ~ 115px left
                       below HighlightTitle1 5 to 12px
                       css color is "rgba(81, 84, 117, 1)
                       css font-family matches "roboto-light"


        HighligtSumary2:
                       width 253 to 259px
                       height 33 to 39px
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen ~ 396px left
                       below HighlightTitle2 5 to 12px
                       right-of HighligtSumary1 ~ 25px
                       css color is "rgba(81, 84, 117, 1)
                       css font-family matches "roboto-light"


        HighligtSumary3:
                       width 253 to 259px
                       height 51 to 57px
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen ~ 115px left
                       below HighlightTitle3 9 to 14px
                       css color is "rgba(81, 84, 117, 1)
                       css font-family matches "roboto-light"


        HighligtSumary4:
                       width 253 to 259px
                       height 51 to 57px
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen ~ 53px left
                       below HighlightTitle3 9 to 13px
                       right-of HighligtSumary3 ~ 26px
                       css color is "rgba(81, 84, 117, 1)
                       css font-family matches "roboto-light"

= CodeSnippet Component =
   @on Desktop

        ToolsDoc:
                   inside screen ~409px left
                   below  HighligtSumary3 ~ 183px
                   css font-size is "34px"
                   css line-height is "31px"
                   css color is "rgba(24, 38, 117, 1)"
                   css font-family matches "roboto-bold"
        ToolSumry:
                    inside screen ~409px left
                    below ToolsDoc ~ 27px
                    aligned vertically all ToolsDoc
                    css font-size is "14px"
                    css line-height is "18px"
                    css color is "rgba(81, 84, 117, 1)"
                    css font-family matches "roboto"
                    css font-weight is "300"
        Tooltext:
                     inside screen ~409px left
                     below ToolSumry ~ 29px
                     aligned vertically centered ToolsDoc
                     css font-size is "12px"
                     css line-height is "14px"
                     css color is "rgba(74, 74, 74, 1)"
                     css font-family matches "roboto"
                     css font-weight is "500"
        CodeSnippet:
                     inside screen ~387px left
                     below Tooltext ~ 66px
                     aligned vertically centered Tooltext
        CTA1:
                      inside screen ~446px left
                      below CodeSnippet ~ 70px
                      css font-size is "14px"
                      css line-height is "16px"
                      css color is "rgba(255, 255, 255, 1)"
                      css font-family matches "roboto-bold"
        CTA2: 
                      right-of CTA1 ~ 23px
                      aligned horizontally all CTA1
                      below CodeSnippet ~ 70px
                      css font-size is "14px"
                      css line-height is "16px"
                      css color is "rgba(55, 91, 105, 1)"
                      css font-family matches "roboto-bold"
            
   @on Mobile
     
        ToolsDoc:
                width 260 to 267px
                height 59 to 65px
                css font-size is "28px"
                css line-height is "31px"
                inside screen ~ 56px left

        ToolSumry:
                 width 285 to 290px                 
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
           
           
        CTA2: 
            width 157 to 163px
            height 37 to 43px
            inside screen ~ 198px left
            css font-size is "14px"
            css line-height is "16px"
            left-of CTA1 ~ 22px
            
   @on tablet
     
        ToolsDoc:
                width 381 to 387px
                height 28 to 33px
                css font-size is "28px"
                css line-height is "31px"
                inside screen ~ 193px left
                css font-family matches "roboto-bold"
                

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
            below CodeSnippet ~ 30px

        CTA2: 
            width 157 to 163px
            height 37 to 43px
            inside screen ~ 397px left
            css font-size is "14px"
            css line-height is "16px"
            right-of CTA1 ~ 26px
            below Codesni ~ 30px
                     
= Help Component =
    @on Desktop
        help-component:
            inside screen 0px left
            below CTA1 ~ 133px
        help-first-leaf:
            inside screen ~ 486px left
            below CTA1 ~ 217px
            css font-size is "34px"
            css line-height is "31px"
            css color is "rgba(255, 255, 255, 1)"
            css font-family matches "roboto-bold"
        help-last-leaf:
            inside screen ~ 487px left
            below help-first-leaf ~ 30px
            aligned vertically centered help-first-leaf
            css font-size is "14px"
            css line-height is "16px"
            css color is "rgba(13, 38, 126, 1)"
            css font-family matches "roboto-bold"
            css background-color is "rgba(255, 255, 255, 1)"
            

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
        footer-copy-right:
            inside screen ~ 11px left
            

    @on tablet
        footer-container:
            inside screen 0px left, 0px bottom
            height ~ 102px

        footer-copy-right:
            inside footer-container 53 to 55px left

    @on Mobile
        footer-container:
            inside screen 0px bottom
            height ~ 250px
            color-scheme > 80% #0D267E

        footer-copy-right:
            inside footer-container 0px left
            height ~ 19px


= Menu Footer =
    @on Desktop
        footer-rtmenu-items-1:
            right-of footer-copy-right
        footer-rtmenu-items-*:            
             css font-size is "16px"
             css line-height is "19px"
             css color is "rgba(255, 255, 255, 1)"
             css font-family matches "roboto"
             css font-weight is "300"
        @forEach [footer-rtmenu-items-*] as menuItem, prev as previousMenuItem
            ${menuItem}:
                right-of ${previousMenuItem} 37 to 41px

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
                 css font-size is "16px"
                 
