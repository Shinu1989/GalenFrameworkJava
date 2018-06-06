@objects
    TermsConditionTitle              xpath  //section[@id='terms-conditions']/div/div[1]
    PostedByDate                     xpath  //section[@id='terms-conditions']/div//span[2]	
    TermConditionText                xpath  (//section[@id='terms-conditions']//p)[1]
    FirstTermConditionHeadline       xpath  (//section[@id='terms-conditions']//p[3]/strong)[1]
    FirstTermConditionText           xpath  (//section[@id='terms-conditions']//p)[2]
  
    
    
= Terms and Conditions =
    @on Desktop
        TermsConditionTitle:
             inside screen  194 to 204px left           
             
        PostedByDate:
             inside screen  317 to 329px left
             below TermsConditionTitle 78 to 89px 
            
        TermConditionText:
             inside screen  194 to 204px left
             below PostedByDate 20 to 32px 
            
        FirstTermConditionHeadline:
             inside screen  194 to 204px left             
            
        FirstTermConditionText:
             inside screen  194 to 204px left                      
                        
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
                    
       
    @on  Mobile
         TermsConditionTitle:
             inside screen  11 to 22px left
             
             
         PostedByDate:
             inside screen  215 to 227px left
             below TermsConditionTitle  6 to 16px
                        
         TermConditionText:
             inside screen  11 to 22px left
             below PostedByDate 87 to 99px  
            
         FirstTermConditionHeadline:
             inside screen  11 to 22px left
                       
         FirstTermConditionText:
             inside screen  11 to 22px left
       
       
          