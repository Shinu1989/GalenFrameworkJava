@objects
    BlogDetailHEadline         xpath  //*[@class='titleTxtContent']
    BlogDeatilSubHeadline      xpath  (//*[@class='detailTxtContent']/p)[1]
    BlogDetailPostedBy         xpath  (//*[@class='detailTxtContent']/p)
    BlogDetailHeadlineImage    xpath  //picture[@class='img-responsive']
    BlogDetailCommentTitle     xpath  //*[@class='comment-title']
    BlogDetailFullWidthImage   xpath  //section[@id='full-width-image']
    BlogDetailImageCopy        xpath  (//picture[@class='img-responsive']//img)[2]
    BlogDetailPostNewComntBtn  xpath  //section[@id='comments-section']//a[@id='post-new-comment']
    BlogDetailCommentBox1      xpath  (//div[@class='submitted']/..)[1]
    BLCommentByName            xpath  (//div[@class='submitted']/span/span)[1]
    BLCommentText              xpath  (//div[@class='read-more']/..)[1]
    BLCommentReplyBtn          xpath  (//li[contains(@class,'comment-reply')]/a)[1]
    BLCommentShowReplyIcon     xpath  (//section[@id='comments-section']//a[@class='reply-button']/span)[1]
    BLCommentShowReplyElemnt   xpath  (//section[@id='comments-section']//a[@class='reply-button']/span)[2]
    BLDetailPageBlogText       xpath  (//div[contains(@class,'field-items')]/*/*)[1]
    BLDetailPageImage          xpath  //*[contains(@class,'field-item even')]//p[5]
    BLTagAboveComment          xpath  //div[@id='comments']/preceding-sibling::section/div/ul/li[contains(@class,'tag-item col-mob-1')]
    BDshowcommentsPage         xpath  //div[@class='comment-listing']//a[@class='show-comments']
    BDCommentContainer         xpath  (//section[contains(@id,'comment')]//div[contains(@class,'clearfix')])[1]
= Blog Detail = 
    @on Desktop
        BlogDetailHEadline:
             inside screen ~ 310px left
                                      
        BlogDeatilSubHeadline:
             inside screen ~ 310px left            
             below BlogDetailHEadline 10 to 16px

        BlogDetailPostedBy:
             inside screen ~ 310px left            
             below BlogDeatilSubHeadline 172 to 178px
            
        BlogDetailCommentTitle:
             inside screen ~ 210px left
             below BLTagAboveComment 158 to 164px
             
        BLCommentByName:
             inside BDCommentContainer ~ 38px left
             inside BDCommentContainer ~ 35px top 
             
        BLCommentText:
             inside BDCommentContainer ~ 38px left
             below BLCommentByName 1 to 8px
              
        BLCommentReplyBtn:
             inside BDCommentContainer ~ 38px left
             below BLCommentText 20 to 26px
             
        BLCommentShowReplyIcon:
             inside BDCommentContainer ~ 37px left
             below BLCommentReplyBtn 47 to 53px
             height ~ 34px
             width ~ 34px
             
        BLCommentShowReplyElemnt:
             inside BDCommentContainer ~ 88px left
             below BLCommentText 103 to 109px
             
        BLDetailPageBlogText:
             inside screen ~ 309px left  
             below BlogDetailPostedBy 39 to 45px    
             
        BLDetailPageImage:
             inside screen ~ 310px left               
             
        BlogDetailFullWidthImage:
             inside screen 11px left                         
            
        BlogDetailImageCopy:
             inside screen 11px left
             
        BLTagAboveComment:
             inside screen ~ 310px left  
              
        BDshowcommentsPage:
             inside screen ~ 487px left  
             below BLCommentText 222 to 236px
             
        BDCommentContainer:
             inside screen ~ 210px left  
             below BlogDetailCommentTitle 72 to 78px    
      
    @on Mobile  
        BlogDetailHEadline:
             inside screen ~ 8px left
                                      
        BlogDeatilSubHeadline:
             inside screen ~ 8px left            
             below BlogDetailHEadline ~ 7px

        BlogDetailPostedBy:
             inside screen ~ 8px left            
             below BlogDeatilSubHeadline ~ 140px
            
        BlogDetailCommentTitle:
             inside screen ~ 8px left
             below BLTagAboveComment ~ 69px
             
        BLCommentByName:
             inside BDCommentContainer ~ 38px left
             inside BDCommentContainer ~ 38px top 
             
        BLCommentText:
             inside BDCommentContainer ~ 38px left
             below BLCommentByName ~ 8px
              
        BLCommentReplyBtn:
             inside BDCommentContainer ~ 38px left
             below BLCommentText ~ 20px
             
        BLCommentShowReplyIcon:
             inside BDCommentContainer ~ 38px left
             below BLCommentReplyBtn ~ 56px
             height ~ 34px
             width ~ 34px
             
        BLCommentShowReplyElemnt:
             inside BDCommentContainer ~ 90px left
             below BLCommentText ~ 103px
             
        BLDetailPageBlogText:
             inside screen ~ 8px left  
             below BlogDetailPostedBy ~ 22px    
             
        BLDetailPageImage:
             inside screen ~ 8px left               
             
        BlogDetailFullWidthImage:
             inside screen 8px left                         
            
        BlogDetailImageCopy:
             inside screen 8px left
             
        BLTagAboveComment:
             inside screen ~ 8px left  
              
        BDshowcommentsPage:
             inside screen ~ 136px left  
             below BLCommentText ~ 185px
             
        BDCommentContainer:
             inside screen ~ 11px left  
             below BlogDetailCommentTitle ~ 90px    
            
              
    @on tablet
        BlogDetailHEadline:
             inside screen ~ 135px left
                                      
        BlogDeatilSubHeadline:
             inside screen ~ 135px left            
             below BlogDetailHEadline ~ 7px

        BlogDetailPostedBy:
             inside screen ~ 135px left            
             below BlogDeatilSubHeadline ~ 154px
            
        BlogDetailCommentTitle:
             inside screen ~ 11px left
             below BLTagAboveComment ~ 101px
             
        BLCommentByName:
             inside BDCommentContainer ~ 39px left
             inside BDCommentContainer ~ 35px top 
             
        BLCommentText:
             inside BDCommentContainer ~ 39px left
             below BLCommentByName ~ 4px
              
        BLCommentReplyBtn:
             inside BDCommentContainer ~ 39px left
             below BLCommentText ~ 5px
             
        BLCommentShowReplyIcon:
             inside BDCommentContainer ~ 38px left
             below BLCommentReplyBtn ~ 50px
             height ~ 34px
             width ~ 34px
             
        BLCommentShowReplyElemnt:
             inside BDCommentContainer ~ 89px left
             below BLCommentText ~ 88px
             
        BLDetailPageBlogText:
             inside screen ~ 135px left  
             below BlogDetailPostedBy ~ 44px    
             
        BLDetailPageImage:
             inside screen ~ 135px left               
             
        BlogDetailFullWidthImage:
             inside screen 11px left                         
            
        BlogDetailImageCopy:
             inside screen  11px left
             
        BLTagAboveComment:
             inside screen ~ 135px left  
              
        BDshowcommentsPage:
             inside screen ~ 361px left  
             below BLCommentText ~ 210px
             
        BDCommentContainer:
             inside screen ~ 11px left  
             below BlogDetailCommentTitle ~ 39px    
            
              