@objects
    FAQPageTitle               xpath  //section[@id='faq']//h1
    FirstFAQTitle              xpath  (//section[@id='faq']//*[@class='accordion-tab']/div)[1]
    HeadlineContainer          xpath  (//section[@id='faq']//*[@class='accordion-tab'])[1]
    FirstFAQCollapsedSign      xpath  (//section[@id='faq']//*[@class='right-button']/span)[1]
    CollapseContainer          xpath  (//section[@id='faq']//*[@class='right-button'])[1]
    
    
= FAQ =
    @on Desktop
        FAQPageTitle:
            inside screen ~ 199px left
           
        FirstFAQTitle:
            inside HeadlineContainer ~ 30px left
            inside HeadlineContainer ~ 14px top        
            
        FirstFAQCollapsedSign:
            inside CollapseContainer 19px left
            
        HeadlineContainer: 
            inside screen ~ 199px left
        
        CollapseContainer:
            inside screen ~ 990px left
                                                                         
        
    @on tablet
        FAQPageTitle:
            inside screen ~ 11px left
           
        FirstFAQTitle:
            inside HeadlineContainer ~ 34px left
            inside HeadlineContainer ~ 14px top    
            
        FirstFAQCollapsedSign:
            inside CollapseContainer ~ 20px left
            
        HeadlineContainer: 
            inside screen ~ 22px left
        
        CollapseContainer:
            inside screen ~ 890px left
                                          
            
            
       
            
       
    @on Mobile
        FAQPageTitle:
            inside screen ~ 8px left
           
        FirstFAQTitle:
            inside HeadlineContainer ~ 23px left
            inside HeadlineContainer ~ 14px top  
            
        FirstFAQCollapsedSign:
            inside CollapseContainer ~ 19px left
            
        HeadlineContainer: 
            inside screen ~ 16px left
        
        CollapseContainer:
            inside screen ~ 447px left