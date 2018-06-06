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
            
   