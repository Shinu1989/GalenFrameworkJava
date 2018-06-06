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
    BLDetailPageImage          xpath  (//*[@id='image-copy']/*)[1]
    BLTagAboveComment          xpath  //div[@id='comments']/preceding-sibling::section/div/ul/li[contains(@class,'tag-item col-mob-1')]
    BDshowcommentsPage         xpath  //div[@class='comment-listing']//a[@class='show-comments']
    
= Blog Listing =
    @on Desktop
        BlogDetailHEadline:
             inside screen 343px left
             inside screen 149px top
            
        BlogDeatilSubHeadline:
             inside screen 343px left
             inside screen 212px top

        BlogDetailPostedBy:
            inside screen 343px left
            inside screen 395px top
            
        BlogDetailCommentTitle:
             inside screen 253px left
            
        BLCommentByName:
             inside screen 288px left
            
        BLCommentText:
             inside screen 288px left
                  
        BLCommentReplyBtn:
             inside screen 288px left
            
        BLCommentShowReplyIcon:
             inside screen 287px left
            
        BLCommentShowReplyElemnt:
             inside screen 332px left
            
        BLDetailPageBlogText:
             inside screen 343px left
                 
        BLDetailPageImage:
             inside screen 343px left
            
        BlogDetailFullWidthImage:
             inside screen 0px left
            
            
        BlogDetailImageCopy:
             inside screen 0px left
              
        BLTagAboveComment:
             inside screen 343px left
            
        BDshowcommentsPage:
             inside screen 503px left
            
      
    @on Mobile  
        BlogDetailHEadline:
             inside screen 18.4px left
             inside screen 254px top
            
        BlogDeatilSubHeadline:
             inside screen 16px left
             inside screen 325px top
            

        BlogDetailPostedBy:
             inside screen 18.4px left
             inside screen 567px top
            
            
        BlogDetailCommentTitle:
             inside screen 18.4px left
             
            
        BLCommentByName:
             inside screen 121px left
            
        BLCommentText:
             inside screen 76px left
             
               
        BLCommentReplyBtn:
             inside screen 76px left
            
        BLCommentShowReplyIcon:
             inside screen 76px left
            
        BLCommentShowReplyElemnt:
             inside screen 76px left
  
                   
        BLDetailPageBlogText:
             inside screen 18px left
            
            
        BLDetailPageImage:
             inside screen 18px left
              
        BlogDetailFullWidthImage:
             inside screen 0px left
            
        BlogDetailImageCopy:
             inside screen -1px left
            
        BLTagAboveComment:
             inside screen 18.4px left
                  
        BDshowcommentsPage:
             inside screen 121px left
            
              
    @on tablet
        BlogDetailHEadline:
             inside screen 151px left
             inside screen 209px top
            
        BlogDeatilSubHeadline:
             inside screen 151px left
             inside screen 293px top
            
        BlogDetailPostedBy:
             inside screen 152px left
             inside screen 515px top
            
        BlogDetailCommentTitle:
             inside screen 31px left
            
            
        BLCommentByName:
             inside screen 81px left  
            
        BLCommentText:
             inside screen 81px left
             
        BLCommentReplyBtn:
             inside screen 81px left
            
            
        BLCommentShowReplyIcon:
             inside screen 80px left
            
        BLCommentShowReplyElemnt:
             inside screen 145px left
           
        BLDetailPageBlogText:
             inside screen 151px left
            
            
        BLDetailPageImage:
             inside screen 151px left

        BlogDetailFullWidthImage:
             inside screen 0px left
            	   
            
        BLTagAboveComment:
             inside screen 151px left
     
            
        BDshowcommentsPage:
             inside screen 360px left
            