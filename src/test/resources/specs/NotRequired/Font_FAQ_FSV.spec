@objects
    FAQPageTitle               xpath  //section[@id='faq']//h2
    FirstFAQTitle              xpath  (//section[@id='faq']//div[@class='accordion-tab']/div)[1]
    FirstFAQCollapsedSign      xpath  (//section[@id='faq']//div[@class='right-button']/span)[1]
   
   
    
    
= Blog Listing =
    @on Desktop
        FAQPageTitle:
            css color is "rgba(24, 38, 117, 1)" 
            css font-size is "34px"
            css font-family matches ".*roboto.*"
            
        FirstFAQTitle:
            css color is "rgba(24, 38, 117, 1)" 
            css font-size is "22px"
            css font-family matches ".*roboto.*"
            
        FirstFAQCollapsedSign:
            css color is "rgba(24, 38, 117, 1)" 
            css background-color is "rgba(36,51,129,1)" 
        
            
      
        
    @on tablet
        FAQPageTitle:
            css color is "rgba(24, 38, 117, 1)" 
            css font-size is "34px"
            css font-family matches ".*roboto.*"
            
        FirstFAQTitle:
            css color is "rgba(24, 38, 117, 1)" 
            css font-size is "22px"
            css font-family matches ".*roboto.*"
            
        FirstFAQCollapsedSign:
            css color is "rgba(24, 38, 117, 1)" 
            css background-color is "rgba(36,51,129,1)" 
        
            
      
       
    @on Mobile
        FAQPageTitle:
            css color is "rgba(24, 38, 117, 1)" 
            css font-size is "22px"
            css font-family matches ".*roboto.*"
            
        FirstFAQTitle:
            css color is "rgba(24, 38, 117, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            
        FirstFAQCollapsedSign:
            css color is "rgba(24, 38, 117, 1)" 
            css background-color is "rgba(36,51,129,1)" 
        
            
   