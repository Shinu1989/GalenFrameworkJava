@objects
    BlogListingHeadline        xpath  //section[contains(@class,'hero-left')]//h1
    BLDropDownlabel            xpath  //label[contains(@class,'filter-label')]
    BlogListingImage1          xpath  (//picture[@class='img-responsive']/img)[2] 
    BlogListingTitle1          xpath  (//h2[@class='article-title']/a)[1]
    BlogListingSummary1        xpath  (//div[@class='content']/p)[1]
    BlogListingPostingDate     xpath  (//div[@class='postedby']/*)[1] 
    DropDownContainer          xpath  //*[contains(@id,'filter')]
    DropDownSelect             xpath  //*[contains(@id,'filter')]//button
    DropDownSelectICON         xpath  //span[@class='select-icons']   
    BlogPageHeadlineImage      xpath  //section[@class='comp-hero-left']

    
= Blog Listing =
    @on Desktop
        BlogListingHeadline:
           inside screen ~ 11px left                      
           
        BLDropDownlabel:
           inside screen ~ 111px left            
           below BlogListingHeadline 161 to 167px
            
            
        BlogListingImage1:
           inside screen ~ 111px left            
           below BLDropDownlabel 97 to 103px 
            
            
        BlogListingTitle1:
           inside screen ~ 509px left            
           below BlogListingHeadline 291 to 294px 
            
            
        BlogListingSummary1:
           inside screen ~ 509px left        
           below BlogListingTitle1 25 to 31px
           
        BlogListingPostingDate:
           inside screen ~ 509px left         
           below  BlogListingSummary1 31 to 37px
            
        DropDownSelect:
           inside DropDownContainer ~ 22px left                       
            
        DropDownSelectICON:
           inside DropDownContainer ~ 36px right 
           
        DropDownContainer:                                 
           inside screen ~ 111px left         
           below BLDropDownlabel 10 to 16px 
        
    @on tablet
        BlogListingHeadline:
           inside screen ~ 11px left                      
           
        BLDropDownlabel:
           inside screen ~ 11px left            
           below BlogListingHeadline 107 to 113px
            
            
        BlogListingImage1:
           inside screen ~ 11px left            
           below BLDropDownlabel 157 to 163px 
            
            
        BlogListingTitle1:
           inside screen ~ 383px left            
           below BlogListingHeadline 285 to 291px 
            
            
        BlogListingSummary1:
           inside screen ~ 383px left        
           below BlogListingTitle1 24 to 30px
           
        BlogListingPostingDate:
           inside screen ~ 383px left         
           below  BlogListingSummary1 23 to 29px
            
        DropDownSelect:
           inside DropDownContainer ~ 22px left                       
            
        DropDownSelectICON:
           inside DropDownContainer ~ 31px right 
           
        DropDownContainer:                                 
           inside screen ~ 11px left 
           below BLDropDownlabel 17 to 23px               
           
           
    @on Mobile
        BlogListingHeadline:
           inside screen ~ 8px left                      
           
        BLDropDownlabel:
           inside screen ~ 8px left            
           below BlogListingHeadline 81 to 87px
            
            
        BlogListingImage1:
           inside screen ~ 8px left            
           below BLDropDownlabel 157 to 163px 
            
            
        BlogListingTitle1:
           inside screen ~ 8px left            
           below BlogListingImage1 23 to 28px 
            
            
        BlogListingSummary1:
           inside screen ~ 8px left        
           below BlogListingTitle1 7 to 13px
           
        BlogListingPostingDate:
           inside screen ~ 8px left         
           below  BlogListingSummary1 11 to 17px
            
        DropDownSelect:
           inside DropDownContainer ~ 22px left                       
            
        DropDownSelectICON:
           inside DropDownContainer ~ 33px left 
           
        DropDownContainer:                                 
           inside screen ~ 8px left  
           below BLDropDownlabel 17 to 23px         