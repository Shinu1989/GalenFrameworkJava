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
            inside screen 31px left
            inside screen 183px top
            
        BLDropDownlabel:
            inside screen 31px left
            inside screen 400px top
            
        BlogListingImage1:
            inside screen 31px left
            inside screen 630px top
            
            
        BlogListingTitle1:
            inside screen 391px left
            inside screen 630px top
            
            
        BlogListingSummary1:
            inside screen 391px left
            inside screen 705px top
            
        BlogListingPostingDate:
            inside screen 391px left
            inside screen 831px top
            
        DropDownSelect:
            inside screen 59px left
            inside screen 470px top
            
        DropDownSelectICON:
            inside screen 311px left
            inside screen 479px top

    