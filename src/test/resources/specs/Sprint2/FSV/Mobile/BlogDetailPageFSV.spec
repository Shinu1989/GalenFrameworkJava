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
            css color is "rgba(13, 8, 112, 1)" 
            css font-size is "32px"
            css font-family matches ".*roboto.*"
            
        BlogDeatilSubHeadline:            
            css color is "rgba(13, 8, 112, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
        BlogDetailPostedBy:            
            css color is "rgba(59, 59, 70, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
           
        BlogDetailCommentTitle:           
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "20px"
            css font-family matches ".*roboto.*"
            
        BlogDetailPostNewComntBtn:           
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            css background-color is "rgba(36, 51, 129	, 1)" 
            
        BLCommentByName:            
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "20px"
            css font-family matches ".*roboto.*"
            
        BLCommentText:          
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            
        BLCommentReplyBtn:           
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            
        BLCommentShowReplyIcon:        
            css color is "rgba(72, 168, 91, 1)" 
            
        BLCommentShowReplyElemnt:          
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
                   
        BLDetailPageBlogText:           
            css color is "rgba(59, 59, 70, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            
        
        BLTagAboveComment:
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            
        BDshowcommentsPage:           
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            css background-color is "rgba(255, 255, 255, 1)" 
          
  