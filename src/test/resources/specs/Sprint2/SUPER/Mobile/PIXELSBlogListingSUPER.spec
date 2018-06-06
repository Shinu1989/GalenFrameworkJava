@objects
    BlogListingHeadline        xpath  .//section[@id='block-views-hero-details-block']//div[contains(@class,'titleTxtContent')]

    BLDropDownlabel            xpath  //label[contains(@class,'filter-label')]

    BlogListingImage1          xpath  (//picture[@class='img-responsive']/img)[2] 
    BlogListingTitle1          xpath  (//h2[@class='article-title']//a)[1]

    BlogListingSummary1        xpath  (//div[@class='content']/p)[1]
    BlogListingPostingDate     xpath  (//div[@class='postedby']/*)[1]
    BlogLiPostedByUSerName     xpath  //div[@class='tool-container float-reset']
 
    DropDownSelect             xpath  //section[@class='blog-listing']//button[contains(@id,'blog-selection')]
    DropDownSelectICON         xpath  //span[@class='select-icons']
    DropDownMenu               xpath  (//section[@class='blog-listing']//li[contains(@id,'edit-tid')]/a)[2]
    BlogPageHeadlineImage      xpath  //section[@class='comp-hero-left']
    DropDownSelectText         xpath  //button[@class='select-button']
    
= Blog Listing =    
    @on Mobile
        BlogListingHeadline:
            inside screen 6 to 16px left
            inside screen 6 to 16px top
            
        BLDropDownlabel:
            inside screen 6 to 16px left
            inside screen 6 to 16px top
            
        BlogListingImage1:
            inside screen 6 to 16px left
            inside screen 6 to 16px top
            
            
        BlogListingTitle1:
            inside screen 378 to 388px left
                       
        BlogListingSummary1:
            inside screen 378 to 388px left
            inside screen 980 to 990px top
            
        BlogListingPostingDate:
            inside screen 378 to 388px left
            inside screen 1140 to 1150px top
            
        DropDownSelect:
            inside screen 6 to 16px left
            inside screen 445 to 455px top
            
        DropDownSelectICON:
            inside screen 283 to 295px left
            inside screen 456 to 466px top