@objects
    FAQPageTitle               xpath  //section[@id='faq']//h1
    FirstFAQTitle              xpath  (//section[@id='faq']//*[@class='accordion-tab']/div)[1]
    FirstFAQCollapsedSign      xpath  (//section[@id='faq']//*[@class='right-button']/span)[1]
   
   
    
    
= Blog Listing =           
    @on tablet
        FAQPageTitle:
            css color is "rgba(11, 19, 97, 1)" 
            css font-size is "34px"
            css font-family matches ".*roboto.*"
            
        FirstFAQTitle:
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "22px"
            css font-family matches ".*roboto.*"
            css background-color is "rgba(11, 19, 97, 1)"
            
        FirstFAQCollapsedSign:
            css color is "rgba(255, 255, 255, 1)" 
            css background-color is "rgba(11, 19, 97, 1)" 
       
  