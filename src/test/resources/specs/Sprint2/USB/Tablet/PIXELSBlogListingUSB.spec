@objects
    BlogListingHeadline        xpath  //section[contains(@class,'hero-left')]//h1
    BLDropDownlabel            xpath  //label[contains(@class,'filter-label')]
    BlogListingImage1          xpath  (//picture[@class='img-responsive']/img)[2] 
    BlogListingTitle1          xpath  (//h2[@class='article-title']/a)[1]
    BlogListingSummary1        xpath  (//div[@class='content']/p)[1]
    BlogListingPostingDate     xpath  (//div[@class='postedby']/*)[1]     
    DropDownSelect             xpath  //*[contains(@id,'filter')]//button
    DropDownSelectICON         xpath  //span[@class='select-icons']   
    BlogPageHeadlineImage      xpath  //section[@class='comp-hero-left']

= Blog Listing =                
    @on tablet
        BlogListingHeadline:
            inside screen 3 to 13px left
            inside screen 178 to 189px top
            
        BLDropDownlabel:
            inside screen 3 to 13px left
            inside screen 395 to 405px top
            
        BlogListingImage1:
            inside screen 3 to 13px left
            inside screen 625 to 635px top
            
            
        BlogListingTitle1:
            inside screen 3 to 13px left
            inside screen 625 to 635px top
            
            
        BlogListingSummary1:
            inside screen 8px left
            inside screen 705px top
            
        BlogListingPostingDate:
            inside screen 3 to 13px left
            inside screen 826 to 836px top
            
        DropDownSelect:
            inside screen 3 to 13px left
            inside screen 465 to 475px top
            
        DropDownSelectICON:
            inside screen 466 to 476px left
            inside screen 474 to 484px top

    