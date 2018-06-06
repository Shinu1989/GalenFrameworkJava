@objects
    FAQPageTitle               xpath  //section[@id='faq']//h1
    FirstFAQTitle              xpath  (//section[@id='faq']//*[@class='accordion-tab']/div)[1]
    FirstFAQCollapsedSign      xpath  (//section[@id='faq']//*[@class='right-button']/span)[1]
   
    
   
    
    
= Blog Listing =
    @on Mobile
        FAQPageTitle:
            inside screen  10 to 22px left
            
            
        FirstFAQTitle:
            inside screen 10 to 22px left
            below FAQPageTitle 21 to 36px       
            
        FirstFAQCollapsedSign:
            inside screen 466 to 482px left