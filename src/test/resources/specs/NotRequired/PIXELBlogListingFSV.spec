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
            inside screen ~ 76px left
            inside screen ~ 149px top
            
        BLDropDownlabel:
            inside screen 165px left
            inside screen 346px top
            
            
        BlogListingImage1:
            inside screen 165px left
            inside screen 507px top
            
            
        BlogListingTitle1:
            inside screen 520px left
            
            
        BlogListingSummary1:
            inside screen 520px left
           
        BlogListingPostingDate:
            inside screen 520px left
            inside screen 645px top
            
            
        DropDownSelect:
            inside screen 184px left
            inside screen 388px top
         
            
        DropDownSelectICON:
            inside screen 463px left
            inside screen 394px top
       
        
        
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