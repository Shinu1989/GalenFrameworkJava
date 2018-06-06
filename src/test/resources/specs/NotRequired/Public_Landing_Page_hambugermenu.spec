@objects
    hamburger                xpath    .//button[contains(@class,'burger-menu')]
    right-menu-head          xpath .//header/div//ul[@class='menu']
    right-menuhead-items-*   xpath .//header/div//ul/li
    header-container         xpath    .//header/div/nav/div[@class='navbar-header']

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