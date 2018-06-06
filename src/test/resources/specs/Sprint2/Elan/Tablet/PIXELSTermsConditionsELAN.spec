@objects
    TermsConditionTitle              xpath  //section[@id='terms-conditions']/div/div[1]/h1
    PostedByDate                     xpath  //section[@id='terms-conditions']/div//span[2]	
    TermConditionText                xpath  (//section[@id='terms-conditions']//p)[1]
    FirstTermConditionHeadline       xpath  (//section[@id='terms-conditions']//p[3]/strong)[1]
    FirstTermConditionText           xpath  (//section[@id='terms-conditions']//p)[2]
  
    
    
= Terms and Conditions =   
    @on tablet
        TermsConditionTitle:
             inside screen  16 to 28px left             
           
        PostedByDate:
             inside screen  222 to 335px left
             below TermsConditionTitle  11 to 22px 
            
        TermConditionText:
             inside screen  16 to 28px left
             below PostedByDate 87 to 99px            
            
        FirstTermConditionHeadline:
             inside screen  16 to 28px left             
            
        FirstTermConditionText:
             inside screen  16 to 28px left
                    
    