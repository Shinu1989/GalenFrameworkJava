@objects
    BlogDetailHEadline         xpath  //section[contains(@class,'hero')]//h1/div		
    BlogDeatilSubHeadline      xpath  (//*[@class='detailTxtContent']/p)[1]
    BlogDetailPostedBy         xpath  (//section[contains(@id,'blog-detail')]//p)[1]
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
    BLTagAboveComment          xpath  (//section[contains(@id,'blog')]//ul//li)[1]
    BDshowcommentsPage         xpath  //div[@class='comment-listing']//a[@class='show-comments']
    
= Blog Listing =
    @on Desktop
        BlogDetailHEadline:            
            css color is "rgba(13, 8, 112, 1)" 
            css font-size is "50px"
            css font-family is "Roboto-bold"
            css line-height is "58px"
            
        BlogDeatilSubHeadline:          
            css color is "rgba(13, 8, 112, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "32px"


        BlogDetailPostedBy:            
            css color is "rgba(59, 59, 70, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "32px"
           
        BlogDetailCommentTitle:           
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "34px"
            css font-family is "Roboto-bold"
            css line-height is "31px"
            
        BlogDetailPostNewComntBtn:            
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "16px"
            css background-color is "rgba(108, 32, 126, 1)"
            width 218px 
            height 50px 
            
        BLCommentByName:          
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "20px"
            css font-family is "Roboto-bold"
            css line-height is "31px"
            
        BLCommentText:            
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-light"
            css line-height is "18px"
            
        BLCommentReplyBtn:       
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "32px"
            
        BLCommentShowReplyIcon:           
            css background-color is "rgba(72, 168, 91, 1)" 
            width 34px 
            height 34px
            
        BLCommentShowReplyElemnt:            
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "32px"
                   
        BLDetailPageBlogText:            
            css color is "rgba(59, 59, 70, 1)" 
            css font-size is "18px"
            css font-family is "Roboto"
            css line-height is "30px"
                    
            
        BLTagAboveComment:
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "32px"
            
        BDshowcommentsPage:           
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "16px"
            css background-color is "rgba(255, 255, 255, 1)" 
            width 218px 
            height 50px
            
            
    @on Mobile
        BlogDetailHEadline:            
            css color is "rgba(13, 8, 112, 1)" 
            css font-size is "32px"
            css font-family is "Roboto-bold"
            css line-height is "39px"
            
        BlogDeatilSubHeadline:            
            css color is "rgba(13, 8, 112, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "18px"
            
        BlogDetailPostedBy:            
            css color is "rgba(59, 59, 70, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "32px"
           
        BlogDetailCommentTitle:           
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "20px"
            css font-family is "Roboto-bold"
            css line-height is "31px"
            
        BlogDetailPostNewComntBtn:           
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "16px"
            css background-color is "rgba(108, 32, 126, 1)"
            width 218px 
            height 50px  
            
        BLCommentByName:            
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "20px"
            css font-family is "Roboto-bold"
            css line-height is "24px"
            
        BLCommentText:          
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "18px"
            
            
        BLCommentReplyBtn:           
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "18px"
            
        BLCommentShowReplyIcon:        
            css color is "rgba(72, 168, 91, 1)" 
            width 34px 
            height 34px 
            
        BLCommentShowReplyElemnt:          
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "18px"
                   
        BLDetailPageBlogText:           
            css color is "rgba(59, 59, 70, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-light"
            css line-height is "24px
            
        
        BLTagAboveComment:
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "32px"
            
            
        BDshowcommentsPage:           
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "16px"
            css background-color is "rgba(255, 255, 255, 1)" 
            width 218px 
            height 50px 
            
          
   
          
    @on tablet        
        BlogDetailHEadline:         
            css color is "rgba(13, 8, 112, 1)" 
            css font-size is "50px"
            css font-family is "Roboto-bold"
            css line-height is "58px"
            
            
        BlogDeatilSubHeadline:            
            css color is "rgba(13, 8, 112, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "18px"

        BlogDetailPostedBy:         
            css color is "rgba(59, 59, 70, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "32px"
           
        BlogDetailCommentTitle:        
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "34px"
            css font-family is "Roboto-bold"
            css line-height is "31px"
            
            
        BlogDetailPostNewComntBtn:            
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "16px"
            css background-color is "rgba(108, 32, 126, 1)" 
            width 218px 
            height 50px
            
        BLCommentByName:           
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "20px"
            css font-family is "Roboto-bold"
            css line-height is "31px"
            
        BLCommentText:           
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-light"
            css line-height is "18px"
            
            
        BLCommentReplyBtn:           
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "32px"
            
        BLCommentShowReplyIcon:           
            css color is "rgba(72, 168, 91, 1)" 
            width 34px 
            height 34px 
            
        BLCommentShowReplyElemnt:           
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "32px"
                   
        BLDetailPageBlogText:            
            css color is "rgba(59, 59, 70, 1)" 
            css font-size is "18px"
            css font-family is "Roboto"
            css line-height is "26px"
            
       
            
        BLTagAboveComment:
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "14px"
            css font-family is "Roboto-bold"
            css line-height is "32px"
            
        BDshowcommentsPage:            
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "14px"            
            css font-family is "Roboto-bold"
            css line-height is "16px"
            css background-color is "rgba(255, 255, 255, 1)"
            width 218px 
            height 50px
            
    