@objects
    FAQPageTitle               xpath  //section[@id='faq']//h2
    FirstFAQTitle              xpath  (//section[@id='faq']//div[@class='accordion-tab']/div)[1]
    FirstFAQCollapsedSign      xpath  (//section[@id='faq']//div[@class='right-button']/span)[1]
    
   
    
    
= Blog Listing =
    @on Desktop
        FAQPageTitle:
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "34px"
            css font-family matches ".*roboto.*"
            
        FirstFAQTitle:
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "22px"
            css font-family matches ".*roboto.*"
            
        FirstFAQCollapsedSign:
            css color is "rgba(255, 255, 255, 1)" 
            css background-color is "rgba(44, 169, 242, 1)" 
        
            
     
        
    @on tablet
        FAQPageTitle:
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "34px"
            css font-family matches ".*roboto.*"
            
        FirstFAQTitle:
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "22px"
            css font-family matches ".*roboto.*"
            
        FirstFAQCollapsedSign:
            css color is "rgba(255,255,255, 1)" 
            css background-color is "rgba(44, 169, 242, 1)" 
        
            
       
       
    @on Mobile
        FAQPageTitle:
            css color is "rgba(35, 36, 96, 1)" 
            css font-size is "22px"
            css font-family matches ".*roboto.*"
            
        FirstFAQTitle:
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            
        FirstFAQCollapsedSign:
            css color is "rgba(255, 255, 255, 1)" 
            css background-color is "rgba(44, 169, 242, 1)" 
        
            
        
             