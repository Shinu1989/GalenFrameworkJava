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
    @on Desktop
        BlogDetailHEadline:
             inside screen 293 to 303px left
             inside screen 144 to 153px top
            
        BlogDeatilSubHeadline:
             inside screen 293 to 303px left
             inside screen 207 to 218px top

        BlogDetailPostedBy:
            inside screen 293 to 303px left
            inside screen 390 to 400px top
            
        BlogDetailCommentTitle:
             inside screen 150 to 160px left
            
        BLCommentByName:
             inside screen 232 to 243px left
            
        BLCommentText:
             inside screen 232 to 243px left
                  
        BLCommentReplyBtn:
             inside screen 232 to 243px left
            
        BLCommentShowReplyIcon:
             inside screen 231 to 241px left
            
        BLCommentShowReplyElemnt:
             inside screen 279to 289px left
            
        BLDetailPageBlogText:
             inside screen 293 to 303px left
                 
        BLDetailPageImage:
             inside screen 293 to 303px left
            
        BlogDetailFullWidthImage:
             inside screen 0px left       
            
        BlogDetailImageCopy:
             inside screen 0px left
              
        BLTagAboveComment:
             inside screen 293 to 303px left
            
        BDshowcommentsPage:
             inside screen 471 to 481px left
             
        BlogDetailPostNewComntBtn:
             inside screen 752 to 763px left
      
    @on Mobile  
        BlogDetailHEadline:
             inside screen 3 to 13px left
             inside screen 249 to 259px top
            
        BlogDeatilSubHeadline:
             inside screen 3 to 13px left
             inside screen 320 to 330px top
            

        BlogDetailPostedBy:
             inside screen 3 to 13px left
             inside screen 562 to 572px top
            
            
        BlogDetailCommentTitle:
             inside screen 3 to 13px left
             
            
        BLCommentByName:
             inside screen 41 to 51px left
            
        BLCommentText:
             inside screen 41 to 51px left
             
               
        BLCommentReplyBtn:
             inside screen 41 to 51px left
            
        BLCommentShowReplyIcon:
             inside screen 41 to 51px left
            
        BLCommentShowReplyElemnt:
             inside screen 71 to 81px left
  
                   
        BLDetailPageBlogText:
             inside screen 3 to 13px left
            
            
        BLDetailPageImage:
             inside screen 0px left
              
        BlogDetailFullWidthImage:
             inside screen 0px left
            
        BlogDetailImageCopy:
             inside screen 0px left
            
        BLTagAboveComment:
             inside screen 132 to 142px left
                  
        BDshowcommentsPage:
             inside screen 116 to 126px left
             
        BlogDetailPostNewComntBtn:
             inside screen 130 to 140px left
            
              
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
            