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
            
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "32px"
            css font-family matches ".*roboto.*"
            
        BLDropDownlabel:
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            
        
            
        BlogListingTitle1:
          
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "22px"
            css font-family matches ".*roboto.*"
            
        BlogListingSummary1:
           
            css color is "rgba(81, 84, 117, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            
        BlogListingPostingDate:
           
            css color is "rgba(0, 25, 112, 1)"
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            
        DropDownSelect:
            
            css color is "(0, 25, 112, 1)"
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            
        DropDownSelectICON:
           
            css color is "rgba(10, 28, 118, 1)"
        