@objects
    TermsConditionTitle              xpath  //section[@id='terms-conditions']/div/div[1]/h1
    PostedByDate                     xpath  //section[@id='terms-conditions']/div//span[1]	
    TermConditionText                xpath  (//section[@id='terms-conditions']//p)[1]
    FirstTermConditionHeadline       xpath  (//section[@id='terms-conditions']//p[3]/strong)[1]
    FirstTermConditionText           xpath  (//section[@id='terms-conditions']//p)[2]

    
    
= Terms and Conditions =
    @on Desktop
        TermsConditionTitle:
             inside screen ~ 199px left           
                          
        PostedByDate:
             inside screen ~ 199px left
             below TermsConditionTitle ~ 16px 
            
        TermConditionText:
             inside screen ~ 199px left
             below PostedByDate ~ 93px 
            
        FirstTermConditionHeadline:
             inside screen ~ 199px left             
            
        FirstTermConditionText:
             inside screen ~ 199px left                      
                        
    @on tablet
        @on Desktop
        TermsConditionTitle:
             inside screen ~ 11px left           
                          
        PostedByDate:
             inside screen ~ 11px left
             below TermsConditionTitle ~ 16px 
            
        TermConditionText:
             inside screen ~ 11px left
             below PostedByDate ~ 93px 
            
        FirstTermConditionHeadline:
             inside screen ~ 11px left             
            
        FirstTermConditionText:
             inside screen ~ 11px left   
                    
       
    @on Mobile
        @on Desktop
        TermsConditionTitle:
             inside screen ~ 8px left           
                          
        PostedByDate:
             inside screen ~ 8px left
             below TermsConditionTitle ~ 11px 
            
        TermConditionText:
             inside screen ~ 8px left
             below PostedByDate ~ 93px 
            
        FirstTermConditionHeadline:
             inside screen ~ 8px left             
            
        FirstTermConditionText:
             inside screen ~ 8px left         