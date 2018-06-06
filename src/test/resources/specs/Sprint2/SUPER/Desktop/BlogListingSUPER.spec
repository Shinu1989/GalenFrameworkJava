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
    @on Desktop
        BlogListingHeadline:                
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "50px"
            css font-family is "roboto-bold"
            css line-height is "58px"
            
            
        BLDropDownlabel:              
            css color is "rgba(7, 21, 89, 1)" 
            css font-size is "14px"
            css font-family is "roboto-bold"
            css line-height is "18px"
                                       
        BlogListingTitle1:            
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "34px"
            css font-family is "roboto-bold"
            css line-height is "40px"
            
            
        BlogListingSummary1:               
            css color is "rgba(81, 84, 117, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"
            
        BlogListingPostingDate:                           
            css color is "rgba(220, 62, 75, 1)"
            css font-size is "14px"
            css font-family is "roboto-bold"
            css line-height is "18px"     
            
        DropDownSelect:           
            css color is "rgba(10, 28, 118, 1)"
            css font-size is "14px"
            css font-family is "roboto-bold"
            css line-height is "18px"
            
        DropDownSelectICON:             
            css color is "rgba(10, 28, 118, 1)"
            width 7.12px 
            height 3.56px
                    
        
        
    @on tablet
        BlogListingHeadline:         
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "50px"
            css font-family is "roboto-bold"
            css line-height is "58px"
            
        BLDropDownlabel:            
            css color is "rgba(7, 21, 89, 1)" 
            css font-size is "14px"
            css font-family is "roboto-bold"
            css line-height is "18px"
                        
        BlogListingTitle1:            
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "34px"
            css font-family is "roboto-bold"
            css line-height is "31px"
            
            
        BlogListingSummary1:           
            css color is "rgba(81, 84, 117, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"
            
        BlogListingPostingDate:            
            css color is "rgba(220, 62, 75, 1)"
            css font-size is "14px"
            css font-family is "roboto-bold"
            css line-height is "18px"
                        
        DropDownSelect:            
            css color is "rgba(10, 28, 118, 1)"
            css font-size is "14px"
            css font-family is "roboto-bold"
            css line-height is "18px"
            
        DropDownSelectICON:            
            css color is "rgba(10, 28, 118, 1)"
            width 7.12px 
            height 3.56px

    @on Mobile
        BlogListingHeadline:           
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "32px"
            css font-family is "roboto-bold"
            css line-height is "39px"
            
        BLDropDownlabel:           
            css color is "rgba(7, 21, 89, 1)" 
            css font-size is "14px"
            css font-family is "roboto-bold"
            css line-height is "18px"                
            
        BlogListingTitle1:            
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "22px"
            css font-family is "roboto-bold"
            css line-height is "25px"
                        
        BlogListingSummary1:          
            css color is "rgba(81, 84, 117, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"
            
        BlogListingPostingDate:            
            css color is "rgba(220, 62, 75, 1)"
            css font-size is "14px"
            css font-family is "roboto-bold"
            css line-height is "32px"           
            
        DropDownSelect:           
            css color is "rgba(10, 28, 118, 1)"
            css font-size is "14px"
            css font-family is "roboto-bold"
            css line-height is "18px"
            
        DropDownSelectICON:            
            css color is "rgba(10, 28, 118, 1)"
            width 7.12px 
            height 3.56px