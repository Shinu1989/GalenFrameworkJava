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
    @on Desktop
        BlogListingHeadline:
            inside screen  6 to 16px left
            inside screen  144 to 154px top
            
        BLDropDownlabel:
            inside screen 105 to 115px left
            inside screen 341 to 347px top
            
            
        BlogListingImage1:
            inside screen 105 to 110px left
            inside screen 502 to 512px top
            
            
        BlogListingTitle1:
            inside screen 504 to 515px left
            
            
        BlogListingSummary1:
            inside screen 504 to 515px left
           
        BlogListingPostingDate:
            inside screen 504 to 515px left
            inside screen 640 to 650px top
            
            
        DropDownSelect:
            inside screen 105 to 115px left
            inside screen 383 to 393px top
         
            
        DropDownSelectICON:
            inside screen 439 to 449px left
            inside screen 389 to 399px top
       
        
        
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