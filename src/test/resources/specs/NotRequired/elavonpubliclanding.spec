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

    left-menu-head           xpath .//header//div[contains(@class,'logo-wrapper')]
    logo-img                 xpath (.//img[contains(@class,'logo-img')])[1]
    for-developers           xpath .//header//div/span[@class='for-dev']
    right-menu-head          xpath .//header/div//ul[@class='menu']
    right-menuhead-items-*   xpath .//header/div//ul/li
    footer-copy-right        xpath .//footer//div[contains(@class,'footer-left')]
    Mobile-footer-copy-right xpath .//footer//div[contains(@class,'mob-footer')]
    footer-right-menu        xpath .//footer//div/ul[@class='menu']
    footer-rtmenu-items-*    xpath .//footer//div/ul/li
    hero-banner              xpath .//section/div[@class='hero-banner-container']
    hero-head                xpath .//section[contains(@class,'hero-banner')]/div//h2
    hero-para                xpath .//section[contains(@class,'hero-banner')]/div//p
    hero-cta1                xpath .//div[@class='cta-hero-banner']
    headline-component       xpath .//section[contains(@class, 'comp comp-headline')]
    help-component           xpath .//section[contains(@class,'comp comp-help')]
    help-first-leaf          xpath .//span[@id='Create Account']
    help-last-leaf           xpath .//section[contains(@class,'comp-help')]//div/ul/li[2]
    hamburger                xpath .//button[contains(@class,'burger-menu')]

= Header Component =
    @on Desktop
        logo-img:
            inside screen  6 to 15px left
            inside screen  70 to 81px top

        for-developers:
            inside screen  135 to 145px left
            inside screen  73 to 85px top


    @on tablet
        logo-img:
            inside screen  119 to 130px left
            inside screen  7 to 19px top


        for-developers:
            inside screen  289 to 300px left
            inside screen  15 to 25px top


    @on Mobile
        logo-img:
            inside screen  140 to 150px left
            inside screen  7 to 19px top


= Menu Head =
    @on Desktop
        right-menu-head:
            inside screen  667 to 679px left
            inside screen  73 to 85px top
    @on Desktop
        right-menuhead-items-1:
            inside screen  667 to 679px left
            inside screen  73 to 85px top

        right-menuhead-items-*:
            inside screen  667 to 679px left
            inside screen  73 to 85px top
            
        @forEach [right-menuhead-items-*] as menuItem, prev as previousMenuItem
            ${menuItem}:
                right-of ${previousMenuItem} 30 to 42px
                aligned horizontally all ${previousMenuItem}


= Hero Component =
    @on Desktop
        hero-head:
            inside screen  404 to 415px left
            inside screen  206 to 216px top
            css font-size is "50px"
            css line-height is "58px"

        hero-para:
            inside screen  404 to 415px left
            inside screen  263 to 275px top            
            css font-size is "50px"
            css line-height is "58px"

        hero-cta1:
            inside screen  942 to 953px left
            inside screen  425 to 436px top
            css font-size is "16px"
            css line-height is "18px"

    @on tablet
        hero-head:
            inside screen  130 to 140px left           
            css font-size is "32px"
            css line-height is "38px"

        hero-para:
            inside screen  130 to 140px left
            inside screen  73 to 85px top
            
            css font-size is "32px"
            css line-height is "38px"

        hero-cta1:
            inside screen  387 to 400px left
            below hero-para ~ 71px            
            css font-size is "14px"
            css line-height is "16px"

    @on Mobile       
        hero-head:
            inside screen  3 to 14px left
            inside screen  71 to 83px top
            css font-size is "32px"
            css line-height is "39px"

        hero-para:
            inside screen  3 to 14px left
            inside screen  71 to 83px top           
            css font-size is "32px"
            css line-height is "39px"

        hero-cta1:
            inside screen  149 to 159px left
            inside screen  225 to 236px top
            css font-size is "14px"
            css line-height is "16px"

=  Highlights Component =
    @on Desktop
        Highlight1:                  
                  inside screen  105 to 115px left
                  below hero-cta1 501 to 512px

        Highlight2:                 
                  inside screen  404 to 414px left
                  below hero-para 650 to 661px

        Highlight3:               
                  inside screen  703 to 713px left                  

        Highlight4:                  
                  inside screen  1002 to 1013px left
                  

        HighlightTitle1:                      
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen 56 to 66px left
                       below Highlight1 ~ 36px


        HighlightTitle2:                    
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen  345 to 356px left
                       below Highlight2 19 to 23px                       
                       
        HighlightTitle3:                      
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen 602 to 614px left
                       below Highlight3 37px
                       
                       
        HighlightTitle4:                      
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen 916 to 930px left
                       below Highlight4 ~ 38px
                      
        HighligtSumary1:                       
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen 31 to 42px left
                       below HighlightTitle1 14 to 19px


        HighligtSumary2:                       
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen 332 to 345px left
                       below HighlightTitle2 14 to 19px
                       

        HighligtSumary3:                       
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen 632 to 644px left
                       below HighlightTitle3 14 to 19px
                       

        HighligtSumary4:                      
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen 938 to 950px left
                       below HighlightTitle3 14 to 19px
                       
    @on Mobile
        Highlight1:                  
                 inside screen  256 to 267px left                

        Highlight2:                     
                  inside screen 257 to 269px left                
                  below HighligtSumary1 77 to 87px
        Highlight3:                  
                  inside screen 188 to 200px left                 
                  below HighligtSumary1 62 to 73px
        Highlight4:                  
                  inside screen 188 to 200px left
                  below HighligtSumary1 61 to 72px
                  
        HighlightTitle1:                       
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen 73 to 83px left
                       below Highlight1 ~ 22px

        HighlightTitle2:                     
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen 73 to 83px left
                       below Highlight2 5 to 11px

        HighlightTitle3:                       
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen 73 to 83px left
                       below Highlight3 ~ 23px

        HighlightTitle4:                      
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen 73 to 83px left
                       below Highlight4 ~ 24px


        HighligtSumary1:                       
                       css font-size is "14px"
                       css line-height is "20px"
                       inside screen 73 to 83px left
                       below HighlightTitle1 12 to 18px


        HighligtSumary2:                       
                       css font-size is "14px"
                       css line-height is "20px"
                       inside screen 73 to 83px left
                       below HighlightTitle2 11 to 17px


        HighligtSumary3:                      
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen 73 to 83px left
                       below HighlightTitle3 12 to 18px


        HighligtSumary4:                      
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen 73 to 83px left
                       below HighlightTitle3 12 to 18px
    @on tablet
        Highlight1:                  
                  inside screen 264 to 276px left

        Highlight2:                 
                  inside screen 636 to 648px left                 

        Highlight3:                 
                  inside screen 262 to 274px left
                  below HighligtSumary1 ~ 51px


        Highlight4:                 
                  inside screen 636 to 648px left
                  below HighligtSumary3 ~ 71px

        HighlightTitle1:                    
                       css font-size is "21px"
                       css line-height is "26px"
                       inside screen 140 to 152px left
                       below Highlight1 ~ 33px


        HighlightTitle2:                      
                       css font-size is "21px"
                       css line-height is "26px"
                       inside screen 512 to 524px left
                       below Highlight2 16 to 23px
                     

        HighlightTitle3:                     
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen  140 to 152px left
                       below Highlight3 ~ 38px

        HighlightTitle4:                      
                       css font-size is "22px"
                       css line-height is "26px"
                       inside screen 512 to 524px left
                       below Highlight4 ~ 39px
                      

        HighligtSumary1:                       
                       css font-size is  "14px"
                       css line-height is "18px"
                       inside screen 140 to 152px left
                       below HighlightTitle1 5 to 12px


        HighligtSumary2:                      
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen 512 to 524px left
                       below HighlightTitle2 5 to 12px
                      

        HighligtSumary3:                                            
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen 140 to 152px left
                       below HighlightTitle3 9 to 14px


        HighligtSumary4:                      
                       css font-size is "14px"
                       css line-height is "18px"
                       inside screen 512 to 524px left
                       below HighlightTitle3 9 to 13px
                      

= CodeSnippet Component =
    @on Desktop
        ToolsDoc:               
                css font-size is "34px"
                css line-height is "29px"
                inside screen 404 to 415px left


        ToolSumry:                 
                 css font-size is "14px"
                 css line-height is "18px"
                 inside screen 404 to 415px left
                 below ToolsDoc ~ 36px
                 
        Tooltext:                
                css font-size is "12px"
                css line-height is "14px"
                inside screen 404 to 415px left
                below ToolSumry ~ 56px
 
        CodeSnippet:             
               inside screen 303 to 315px left
               below Tooltext ~ 31px
               css font-size is "14px"
               css line-height is "17px"

        CTA1:          
            inside screen 359 to 369px left
            css font-size is "14px"
            css line-height is "16px"
           
           
        CTA2:          
            inside screen  602 to 614px left
            css font-size is "14px"
            css line-height is "16px"
            
    @on Mobile     
        ToolsDoc:               
                css font-size is "28px"
                css line-height is "31.008px"
                inside screen 72 to 84px left

        ToolSumry:               
                 css font-size is "14px"
                 css line-height is "18px"
                 inside screen 60 to 72px left
                 below ToolsDoc ~ 20px
                 
        Tooltext:               
                css font-size is "12px"
                css line-height is "14px"
                inside screen 37 to 49px left
                below ToolSumry 19 to 26px
 
        CodeSnippet:            
               inside screen 10 to 22px left
               below Tooltext ~ 22px
               css font-size is "14px"
               css line-height is "17px"

        CTA1:           
            inside screen 10 to 22px left
            css font-size is "14px"
            css line-height is "16px"
           
           
        CTA2:            
            inside screen 297 to 310px left
            css font-size is "14px"
            css line-height is "16px"
            left-of CTA1 ~ 22px
            
    @on tablet     
        ToolsDoc:              
                css font-size is "28px"
                css line-height is "31px"
                inside screen 244 to 256px left
                

        ToolSumry:                 
                 css font-size is "14px"
                 css line-height is "18px"
                 inside screen 244 to 256px left
                 below ToolsDoc ~ 23px
                 
        Tooltext:               
                css font-size is "12px"
                css line-height is "14px"
                inside screen 120 to 132px left
                below ToolSumry ~ 26px
 
        CodeSnippet:              
               inside screen 118 to 130px left
               below Tooltext ~ 31px
               css font-size is "14px"
               css line-height is "17px"
        CTA1:            
            inside screen 264 to 276px left
            css font-size is "14px"
            css line-height is "16px"
            below CodeSnippet ~ 30px

        CTA2:            
            inside screen 512 to 524px left
            css font-size is "14px"
            css line-height is "16px"            
            below CodeSnippet ~ 30px
                     
= Help Component =
    @on Desktop        
        help-first-leaf:
            inside screen 404 to 413px left            
            css font-size is "34px"
            css line-height is "31px"

        help-last-leaf:
             inside screen 481 to 493px left
             below help-first-leaf 25 to 35px               
             css font-size is "14px"
             css line-height is "16px"
             
    @on Mobile      
        help-first-leaf:
             inside screen 71 to 84px left             
             css font-size is "28px"
             css line-height is "31px"

        help-last-leaf:
              inside screen 156 to 166px left
              below help-first-leaf 15 to 25px           
              css font-size is "14px"
              css line-height is "16px"

    @on tablet      
        help-first-leaf:
              inside screen 16 to 28px left
              css font-size is "34px"
              css line-height is "31px"

        help-last-leaf:
              inside screen 344 to 356px left
              below help-first-leaf 25 to 35px                   
              css font-size is "14px"
              css line-height is "16px"

= Footer =
    @on Desktop
        footer-copy-right:
            inside screen 6 to 16px left

    @on tablet        
        Mobile-footer-copy-right:
            inside screen 418 to 430px left

    @on Mobile
        Mobile-footer-copy-right:
            inside screen 11 to 21px left

= Menu Footer =
    @on Desktop
        footer-right-menu:
             inside screen 632 to 644px left
           

    @on Desktop
        footer-rtmenu-items-1:
            inside footer-right-menu 632 to 644px right           
            color-scheme = 5% #ffffff

        footer-rtmenu-items-*:
            inside footer-right-menu
            

        @forEach [footer-rtmenu-items-*] as menuItem, prev as previousMenuItem
            ${menuItem}:
                right-of ${previousMenuItem} 39 to 40px

    @on tablet
        footer-right-menu:
               inside screen 264 to 276px left
               right-of footer-copy-right

    @on tablet
        footer-rtmenu-items-1:
              inside footer-right-menu 264 to 276px right              
              color-scheme = 5% #ffffff

        footer-rtmenu-items-*:
              inside footer-right-menu
             

        @forEach [footer-rtmenu-items-*] as menuItem, prev as previousMenuItem
              ${menuItem}:
                  right-of ${previousMenuItem} 26 to 28px

    @on Mobile
        footer-right-menu:
             inside screen 10 to 22px left
             above footer-copy-right

    @on Mobile
        footer-rtmenu-items-1:
             inside footer-right-menu 10 to 22px right           
             color-scheme = 5% #ffffff

        footer-rtmenu-items-*:
            inside footer-right-menu            

        @forEach [footer-rtmenu-items-*] as menuItem, prev as previousMenuItem
            ${menuItem}:
                below ${previousMenuItem} 15 to 18px
           