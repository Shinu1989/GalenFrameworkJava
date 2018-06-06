@objects
    BlogDetailHEadline         xpath  //*[@class='titleTxtContent']

    BlogDeatilSubHeadline      xpath  (//*[@class='detailTxtContent']/p)[1]

    BlogDetailPostedBy         xpath  //*[contains(@class,'article-container')]/div/p
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
    @on tablet
        BlogDetailHEadline:
             inside screen 130 to 140px left
             inside screen 204 to 215px top
            
        BlogDeatilSubHeadline:
             inside screen 130 to 140px left
             inside screen 288 to 298px top
            
        BlogDetailPostedBy:
             inside screen 130 to 140px left
             inside screen 510 to 520px top
            
        BlogDetailCommentTitle:
             inside screen 6 to 16px left
            
            
        BLCommentByName:
             inside screen 45 to 55px left  
            
        BLCommentText:
             inside screen 45 to 55px left
             
        BLCommentReplyBtn:
             inside screen 45 to 55px left
            
            
        BLCommentShowReplyIcon:
             inside screen 44 to 54px left
            
        BLCommentShowReplyElemnt:
             inside screen 130 to 140px left
           
        BLDetailPageBlogText:
             inside screen 130 to 140px left
            
            
        BLDetailPageImage:
             inside screen 130 to 140px left

        BlogDetailFullWidthImage:
             inside screen 0px left
            	   
            
        BLTagAboveComment:
             inside screen 130 to 140px left
     
            
        BDshowcommentsPage:
             inside screen 422 to 432px left
             
        BlogDetailPostNewComntBtn:
             inside screen 583 to 593px left
            