@objects
    BlogListingHeadline        xpath  .//section[@id='block-views-hero-details-block']//div[contains(@class,'titleTxtContent')]

    BLDropDownlabel            xpath  //label[contains(@class,'filter-label')]

    BlogListingImage1          xpath  (//picture[@class='img-responsive']/img)[2] 
    BlogListingTitle1          xpath  (//h2[@class='article-title']//a[2])[1]

    BlogListingSummary1        xpath  (//div[@class='content']/p)[1]
    BlogListingPostingDate     xpath  (//div[@class='postedby']/*)[1]
    BlogLiPostedByUSerName     xpath  //div[@class='tool-container float-reset']
 
    DropDownSelect             xpath  //section[@class='blog-listing']//button[contains(@id,'blog-selection')]
    DropDownSelectICON         xpath  //span[@class='select-icons']
    DropDownMenu               xpath  (//section[@class='blog-listing']//li[contains(@id,'edit-tid')]/a)[2]
    BlogPageHeadlineImage      xpath  //section[@class='comp-hero-left']
    DropDownSelectText         xpath  //button[@class='select-button']
    
= Blog Listing =
    @on Desktop
        BlogListingHeadline:
            inside screen 76px left
            inside screen 149px top          
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "50px"
            css font-family matches ".*roboto.*"
            
        BLDropDownlabel:
            inside screen 165px left
            inside screen 346px top            
            css color is "rgba(7, 21, 89, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            
        BlogListingImage1:
            inside screen 165px left
            inside screen 507px top
        
            
        BlogListingTitle1:
            inside screen 520px left         
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "34px"
            css font-family matches ".*roboto.*"
            
            
        BlogListingSummary1:
            inside screen 520px left          
            css color is "rgba(81, 84, 117, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            
        BlogListingPostingDate:
            inside screen 520px left
            inside screen 645px top           
            css color is "rgba(220, 62, 75, 1)"
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            
            
        DropDownSelect:
            inside screen 184px left
            inside screen 388px top         
            css color is "rgba(10, 28, 118, 1)"
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            
        DropDownSelectICON:
            inside screen 463px left
            inside screen 394px top         
            css color is "rgba(10, 28, 118, 1)"
            
        
        
        
    @on tablet
        BlogListingHeadline:         
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "50px"
            css font-family matches ".*roboto.*"
            
        BLDropDownlabel:            
            css color is "rgba(7, 21, 89, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"               
                        
        BlogListingTitle1:            
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "34px"
            css font-family matches ".*roboto.*"
            
            
        BlogListingSummary1:           
            css color is "rgba(81, 84, 117, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            
        BlogListingPostingDate:            
            css color is "rgba(220, 62, 75, 1)"
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            
            
        DropDownSelect:            
            css color is "rgba(10, 28, 118, 1)"
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            
        DropDownSelectICON:            
            css color is "rgba(10, 28, 118, 1)"


    @on Mobile
        BlogListingHeadline:           
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "32px"
            css font-family matches ".*roboto.*"
            
        BLDropDownlabel:           
            css color is "rgba(7, 21, 89, 1)" 
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
            css color is "rgba(220, 62, 75, 1)"
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            
            
        DropDownSelect:           
            css color is "rgba(10, 28, 118, 1)"
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            
        DropDownSelectICON:            
            css color is "rgba(10, 28, 118, 1)"