@objects
    ContactUSHeadline           xpath  //section[@id='contact-us']//h2[contains(@class,'title')]
    ContactUSSubheadline        xpath  //section[@id='contact-us']//p[contains(@class,'description')]
    ContactFirstNameLabel       xpath  //section[@id='contact-us']//label[contains(@for,'first-name')]
    ContactLastNameLabel        xpath  //section[@id='contact-us']//label[contains(@for,'last-name')]
    ContactEmailLabel           xpath  //section[@id='contact-us']//label[contains(@for,'email-address')]
    ContactSubjectLabel         xpath  //section[@id='contact-us']//label[contains(@for,'edit-tid')]
    ContactDropDown             xpath  //section[@id='contact-us']//button[contains(@class,'select-button')]
    ContactMessageLabel         xpath  //section[@id='contact-us']//label[contains(@for,'message')]
    ContactSubmitButton         xpath  //section[@id='contact-us']//input[contains(@type,'submit')]
    ContactFirstNameField       xpath  //section[@id='contact-us']//input[contains(@id,'first-name')]
    ContactLastNameField        xpath  //section[@id='contact-us']//input[contains(@id,'last-name')] 
    ContactEmailNameField       xpath  //section[@id='contact-us']//input[contains(@id,'email-address')]
    ContactMessageNameField     xpath  //section[@id='contact-us']//textarea[contains(@id,'message')]
    ContactlleftSideText1       xpath  (//section[@id='contact-us']//p[contains(@class,'title')])[1]
    ContactleftSideText2        xpath  (//section[@id='contact-us']//p[contains(@class,'title')])[2]
    ContactleftSideContactNumber xpath (//section[@id='contact-us']//a[contains(@class,'contact-number')])[1]
    ContactleftSideContactEmail xpath  (//section[@id='contact-us']//a[contains(@class,'email')])[1]
    MobContactlleftSideText1    xpath  (//div[contains(@class,'contact-form-wrapper')]/following-sibling::div//p)[1]
    MobContactleftSideText2     xpath  (//div[contains(@class,'contact-form-wrapper')]/following-sibling::div//p)[2]
    MobContactleftSideContactNumber xpath  (//div[contains(@class,'contact-form-wrapper')]/following-sibling::div//p)[3]
    MobContactleftSideContactEmail  xpath  (//div[contains(@class,'contact-form-wrapper')]/following-sibling::div//p)[4]      
          
    
= CONTACT US =
    @on Desktop
        ContactUSHeadline :
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "34px"
            css font-family is "roboto-bold"
            css line-height is "38px"
            
        ContactUSSubheadline:
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "14px"
            css font-family is "roboto-bold"
            css line-height is "18px"            
            
            
        ContactFirstNameLabel:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"
            
            
        ContactLastNameLabel:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"
            
            
        ContactEmailLabel:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"                       
            
        ContactSubjectLabel:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"            
            
        ContactDropDown:
            css color is "rgba(0, 25, 112, 1)"
            css background-color is "rgba(255, 255, 255, 1)"  
            
        ContactMessageLabel:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"
            
        ContactSubmitButton:  
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "14px"
            css font-family is "roboto-bold"
            css line-height is "16px"
            css background-color is "rgba(35, 51, 129, 1)"                                                  
            
        ContactlleftSideText1:
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "20px"
            css font-family is "roboto-bold"
            css line-height is "24px"
            
        ContactleftSideText2:
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "20px"
            css font-family is "roboto-light"
            css line-height is "24px"
            
                    
        ContactleftSideContactNumber:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"
            
        ContactleftSideContactEmail:     
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "14px"
            css font-family is "roboto-bold"
            css line-height is "18px"
            
        
    @on tablet
        ContactUSHeadline :
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "34px"
            css font-family is "roboto-bold"
            css line-height is "38px"
            
        ContactUSSubheadline:
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "14px"
            css font-family is "roboto-bold"
            css line-height is "18px"            
            
            
        ContactFirstNameLabel:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"
            
            
        ContactLastNameLabel:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"
            
            
        ContactEmailLabel:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"                       
            
        ContactSubjectLabel:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"            
            
        ContactDropDown:
            css color is "rgba(0, 25, 112, 1)"   
            css background-color is "rgba(255, 255, 255, 1)"        
            
        ContactMessageLabel:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"
            
        ContactSubmitButton:  
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "14px"
            css font-family is "roboto-bold"
            css line-height is "16px"
            css background-color is "rgba(35, 51, 129, 1)"                                                 
            
        MobContactlleftSideText1:
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "20px"
            css font-family is "roboto-bold"
            css line-height is "24px"
            
        MobContactleftSideText2:
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "20px"
            css font-family is "roboto-light"
            css line-height is "24px"
            
                    
        MobContactleftSideContactNumber:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"
            
        MobContactleftSideContactEmail:     
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "14px"
            css font-family is "roboto-bold"
            css line-height is "18px"
            
       
       
    @on Mobile
        ContactUSHeadline :
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "20px"
            css font-family is "roboto-bold"
            css line-height is "31px"
            
        ContactUSSubheadline:
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "14px"
            css font-family is "roboto-bold"
            css line-height is "18px"            
            
            
        ContactFirstNameLabel:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"
            
            
        ContactLastNameLabel:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"
            
            
        ContactEmailLabel:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"                       
            
        ContactSubjectLabel:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"            
            
        ContactDropDown:
            css color is "rgba(0, 25, 112, 1)" 
            css background-color is "rgba(255, 255, 255, 1)"           
            
        ContactMessageLabel:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"
            
        ContactSubmitButton:  
            css color is "rgba(255, 255, 255, 1)" 
            css font-size is "14px"
            css font-family is "roboto-bold"
            css line-height is "16px"
            css background-color is "rgba(35, 51, 129, 1)"                                                 
            
        MobContactlleftSideText1:
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "20px"
            css font-family is "roboto-bold"
            css line-height is "24px"
            
        MobContactleftSideText2:
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "20px"
            css font-family is "roboto-light"
            css line-height is "24px"
            
                    
        MobContactleftSideContactNumber:
            css color is "rgba(0, 0, 0, 1)" 
            css font-size is "14px"
            css font-family is "roboto-light"
            css line-height is "18px"
            
        MobContactleftSideContactEmail:     
            css color is "rgba(0, 25, 112, 1)" 
            css font-size is "14px"
            css font-family is "roboto-bold"
            css line-height is "18px"
             