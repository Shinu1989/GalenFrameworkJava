@objects
    TermsConditionTitle              xpath  //section[@id='terms-conditions']/div/div[1]/h1
    PostedByDate                     xpath  //section[@id='terms-conditions']/div//span[2]	
    TermConditionText                xpath  (//section[@id='terms-conditions']//p)[1]
    FirstTermConditionHeadline       xpath  (//section[@id='terms-conditions']//p[3]/strong)[1]
    FirstTermConditionText           xpath  (//section[@id='terms-conditions']//p)[2]
  
    
    
= Terms and Conditions =         
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
       
       
             