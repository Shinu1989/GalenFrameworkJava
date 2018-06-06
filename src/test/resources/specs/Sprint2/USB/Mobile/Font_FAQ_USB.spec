@objects
    FAQPageTitle               xpath  //section[@id='faq']//h1
    FirstFAQTitle              xpath  (//section[@id='faq']//*[@class='accordion-tab']/div)[1]
    FirstFAQCollapsedSign      xpath  (//section[@id='faq']//*[@class='right-button']/span)[1]
   
   
    
    
= FAQ =                                     
    @on Mobile
        FAQPageTitle:
            css color is "rgbargba(35, 36, 96, 1)" 
            css font-size is "22px"
            css font-family matches ".*roboto.*"
            
        FirstFAQTitle:
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "14px"
            css font-family matches ".*roboto.*"
            css background-color is "rgba(241, 77, 90, 1)"
            
        FirstFAQCollapsedSign:
            css color is "rgba(255, 255, 255, 1)" 
             css background-color is "rgba(199, 58, 71, 1)" 
            
            
       