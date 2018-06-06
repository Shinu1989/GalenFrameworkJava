@objects
    TermsConditionTitle              xpath  //section[@id='terms-conditions']/div/div[1]/h1
    PostedByDate                     xpath  //section[@id='terms-conditions']/div//span[1]	
    TermConditionText                xpath  (//section[@id='terms-conditions']//p)[1]
    FirstTermConditionHeadline       xpath  (//section[@id='terms-conditions']//p[3]/strong)[1]
    FirstTermConditionText           xpath  (//section[@id='terms-conditions']//p)[2]
    TermsandConditionFooter          xpath  //*[@class='menu']//a[contains(text(),'Terms')]
    
    
= TERMSAndCONDITIONS =
    @on Desktop
        TermsConditionTitle:
            css color is "rgba(7, 21, 89, 1)" 
            css font-size is "34px"
            css font-family matches ".*roboto.*"
            css line-height is "38px"
            
        PostedByDate:
            css color is "rgba(7, 21, 89, 1)" 
            css font-size is "20px"
            css font-family matches ".*roboto.*"
            css line-height is "24px"
            
        TermConditionText:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            css line-height is "18px" 
            
        FirstTermConditionHeadline:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            css line-height is "18px" 
            
        FirstTermConditionText:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            css line-height is "18px" 
            
        TermsandConditionFooter:
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "16px"
            css font-family matches ".*roboto.*"
            css line-height is "20px"
            
        
    @on tablet
        TermsConditionTitle:
            css color is "rgba(7, 21, 89, 1)" 
            css font-size is "34px"
            css font-family matches ".*roboto.*"
            css line-height is "38px"
            
        PostedByDate:
            css color is "rgba(7, 21, 89, 1)" 
            css font-size is "20px"
            css font-family matches ".*roboto.*"
            css line-height is "24px"
            
        TermConditionText:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            css line-height is "18px" 
            
        FirstTermConditionHeadline:
            css color is "rgba(0,0,0,1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            css line-height is "18px" 
            
        FirstTermConditionText:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            css line-height is "18px" 
            
        TermsandConditionFooter:
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "16px"
            css font-family matches ".*roboto.*"
            css line-height is "19px"
       
             
       
    @on Mobile
        TermsConditionTitle:
            css color is "rgba(7, 21, 89, 1)" 
            css font-size is "20px"
            css font-family matches ".*roboto.*"
            css line-height is "38px"
            
        PostedByDate:
            css color is "rgba(7, 21, 89, 1)" 
            css font-size is "20px"
            css font-family matches ".*roboto.*"
            css line-height is "24px"
            
        TermConditionText:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            css line-height is "18px" 
            
        FirstTermConditionHeadline:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            css line-height is "18px" 
            
        FirstTermConditionText:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            css line-height is "18px" 
            
        TermsandConditionFooter:
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "16px"
            css font-family matches ".*roboto.*"
          