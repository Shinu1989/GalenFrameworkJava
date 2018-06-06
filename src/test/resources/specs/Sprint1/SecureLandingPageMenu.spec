@objects
    hamburger          xpath   .//button[contains(@class,'navbar')]
    menu-head          xpath   (//section[contains(@id,'block')]//ul)[2]
    menuhead-items-*   xpath   //section[contains(@id,'block')]//ul//li
    menu               xpath   //section[contains(@id,'block')]//ul//li/a
    header-container   xpath   //div[contains(@class,'navbar-header')]
    menu1              xpath   (//section[contains(@id,'block')]//ul//li/a)[5]
    menu2              xpath   (//section[contains(@id,'block')]//ul//li/a)[6]
    menu3              xpath   (//section[contains(@id,'block')]//ul//li/a)[7]
    menu4              xpath   (//section[contains(@id,'block')]//ul//li/a)[8]
    menu5              xpath   (//section[contains(@id,'block')]//ul//li/a)[9]
    menu6              xpath   (//section[contains(@id,'block')]//ul//li/a)[7]
   
 
=Public Header Component =
    @on Desktop
        hamburger:
            height 60px
            width  60px
                                      
        @forEach [menuhead-items-*] as menuItem
            ${menuItem}:
                inside screen 0px left right
                
         menu1:
            centered all inside menu-head
          
         menu2:
            centered all inside menu-head
            below menu1 49px
            
         menu3:
            centered all inside menu-head
            below menu2 57px
            
         menu4:
            centered all inside menu-head
            below menu3 57px
            
         menu5:
            centered all inside menu-head
            below menu4 57px
            
         menu6:
            centered all inside menu-head
            below menu5 57px
            
            

    @on Mobile
        @on Desktop
       hamburger:
            height 60px
            width  60px
                                      
        @forEach [menuhead-items-*] as menuItem
            ${menuItem}:
                inside screen 0px left right
                
         menu1:
            centered all inside menu-head
          
         menu2:
            centered all inside menu-head
            below menu1 49px
            
         menu3:
            centered all inside menu-head
            below menu2 57px
            
         menu4:
            centered all inside menu-head
            below menu3 57px
            
         menu5:
            centered all inside menu-head
            below menu4 57px
            
         menu6:
            centered all inside menu-head
            below menu5 57px
            
    @on Tablet
        @on Desktop
        hamburger:
            height 60px
            width  60px
                                      
        @forEach [menuhead-items-*] as menuItem
            ${menuItem}:
                inside screen 0px left right
                
         menu1:
            centered all inside menu-head
          
         menu2:
            centered all inside menu-head
            below menu1 49px
            
         menu3:
            centered all inside menu-head
            below menu2 57px
            
         menu4:
            centered all inside menu-head
            below menu3 57px
            
         menu5:
            centered all inside menu-head
            below menu4 57px
            
         menu6:
            centered all inside menu-head
            below menu5 57px