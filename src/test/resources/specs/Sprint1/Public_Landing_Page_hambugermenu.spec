@objects
    hamburger                xpath    .//button[contains(@class,'navbar')]
    right-menu-head          xpath    (//section[contains(@id,'block')]//ul)[2]
    right-menuhead-items-*   xpath    //section[contains(@id,'block')]//ul//li
    Right-menu               xpath    //section[contains(@id,'block')]//ul//li/a
    header-container         xpath    //div[contains(@class,'navbar-header')]

=Public Header Component =
    @on Desktop
        hamburger:
            height 57 to 63px
            
        right-menuhead-items-1:
            right-of  413px
            
        right-menuhead-items-*:
            height ~ 21px

        @forEach [right-menuhead-items-*] as menuItem, prev as previousMenuItem
            ${menuItem}:
                right-of ${previousMenuItem} 52 to 54px
                aligned horizontally all ${previousMenuItem}
        

    @on Mobile
        hamburger:
            height 57 to 63px
            
        right-menuhead-items-1:            
            right-of  413px

        right-menuhead-items-*:           
            height ~ 21px

        @forEach [right-menuhead-items-*] as menuItem, prev as previousMenuItem
             ${menuItem}:
                right-of ${previousMenuItem} 52 to 54px
                aligned horizontally all ${previousMenuItem}
       
    @on Tablet
         hamburger:            
             height 57 to 63px
             
         right-menuhead-items-1:        
            right-of  413px

         right-menuhead-items-*:           
            height ~ 21px

         @forEach [right-menuhead-items-*] as menuItem, prev as previousMenuItem
            ${menuItem}:
                right-of ${previousMenuItem} 52 to 54px
                aligned horizontally all ${previousMenuItem}