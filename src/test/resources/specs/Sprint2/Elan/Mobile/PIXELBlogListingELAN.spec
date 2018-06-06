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
    @on Mobile
        BlogListingHeadline:
            inside screen 18.4px left
            inside screen 179.4px top
            
        BLDropDownlabel:
            inside screen 18.4px left
            inside screen 368px top
            
        BlogListingImage1:
            inside screen 19px left
            inside screen 640px top
            
            
        BlogListingTitle1:
            inside screen 19px left
            inside screen 9322px top
            
            
        BlogListingSummary1:
            inside screen 19px left
            inside screen 985px top
            
        BlogListingPostingDate:
            inside screen 19px left
            inside screen 1145px top
            
        DropDownSelect:
            inside screen 52px left
            inside screen 450px top
            
        DropDownSelectICON:
            inside screen 495px left
            inside screen 461px top