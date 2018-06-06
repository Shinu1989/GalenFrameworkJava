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
    ContactleftSideContactEmail xpath  (//section[@id='contact-us']//a[contains(@class,'email mailto')])[1]
    MobContactlleftSideText1    xpath  (//div[contains(@class,'contact-form-wrapper')]/following-sibling::div//p)[1]
    MobContactleftSideText2     xpath  (//div[contains(@class,'contact-form-wrapper')]/following-sibling::div//p)[2]
    MobContactleftSideContactNumber xpath  (//div[contains(@class,'contact-form-wrapper')]/following-sibling::div//p)[3]
    MobContactleftSideContactEmail  xpath  (//div[contains(@class,'contact-form-wrapper')]/following-sibling::div//p)[4]      
    
    
= CONTACT US =
    @on Desktop
        ContactUSHeadline :
            inside screen  402 to 414px left
            inside screen  102 to 112px top
            
        ContactUSSubheadline:
            inside screen 402 to 414px left
            inside screen 155 to 165px top
            
            
        ContactFirstNameLabel:
            inside screen 402 to 414px left
            inside screen 258 to 269px top	
            
        ContactLastNameLabel:
            inside screen  402 to 414px left
            inside screen  258 to 269px top
                   
        ContactEmailLabel:
            inside screen  402 to 414px left
            inside screen  355 to 365px top
            
        ContactSubjectLabel:
            inside screen  402 to 414px left
            inside screen  454 to 464px top
            
        ContactDropDown:
            inside screen  402 to 414px left
            inside screen  481 to 492px top
            
        ContactMessageLabel:
            inside screen  194 to 204px left
            below ContactDropDown 35 to 45px      
            
        ContactSubmitButton:  
            inside screen  194 to 204px left
            below ContactDropDown 110 to 119px      
            
        ContactFirstNameField:
            inside screen  194 to 204px left
            below ContactFirstNameLabel 3 to 13px
            
        ContactLastNameField:
            inside screen  194 to 204px left
            below ContactLastNameLabel 3 to 13px
            
        ContactEmailNameField:
            inside screen  194 to 204px left
            below ContactEmailLabel 3 to 13px
            
        ContactMessageNameField:
            inside screen  194 to 204px left
            below ContactMessageLabel 3 to 13px
            
        ContactlleftSideText1:
            inside screen  6 to 17px left
            below ContactSubmitButton 109 to 119px
            
        ContactleftSideText2:
            inside screen  6 to 17px left
            below ContactlleftSideText1 3 to 12px
                    
        ContactleftSideContactNumber:
            inside screen  6 to 17px left
            below ContactMessageNameField 277 to 289px
            
        ContactleftSideContactEmail:     
            inside screen  6 to 17px left
            below ContactleftSideContactNumber 2 to 9px
        
        
        
    @on tablet
        ContactUSHeadline :
            inside screen  16 to 28px left
            inside screen  102 to 112px top
            
        ContactUSSubheadline:
            inside screen 16 to 28px left
            inside screen 155 to 165px top
            
            
        ContactFirstNameLabel:
            inside screen 16 to 28px left
            inside screen 258 to 269px top	
            
        ContactLastNameLabel:
            inside screen  16 to 28px left
            inside screen  258 to 269px top
                   
        ContactEmailLabel:
            inside screen  16 to 28px left
            inside screen  355 to 365px top
            
        ContactSubjectLabel:
            inside screen  16 to 28px left
            inside screen  454 to 464px top
            
        ContactDropDown:
            inside screen  16 to 28px left
            inside screen  481 to 492px top
            
        ContactMessageLabel:
            inside screen  16 to 28px left
            below ContactDropDown 35 to 45px      
            
        ContactSubmitButton:  
            inside screen  16 to 28px left
            below ContactDropDown 110 to 119px      
            
        ContactFirstNameField:
            inside screen  16 to 28px left
            below ContactFirstNameLabel 3 to 13px
            
        ContactLastNameField:
            inside screen  16 to 28px left
            below ContactLastNameLabel 3 to 13px
            
        ContactEmailNameField:
            inside screen  16 to 28px left
            below ContactEmailLabel 3 to 13px
            
        ContactMessageNameField:
            inside screen  16 to 28px left
            below ContactMessageLabel 3 to 13px
            
        MobContactlleftSideText1 :
            inside screen  16 to 28px left
            below ContactSubmitButton 109 to 119px
            
        MobContactleftSideText2:
            inside screen  16 to 28px left
            below ContactlleftSideText1 2 to 11px
                    
        MobContactleftSideContactNumber:
            inside screen  16 to 28px left
            below ContactMessageNameField 277 to 289px
            
        MobContactleftSideContactEmail:     
            inside screen  16 to 28px left
            below ContactleftSideContactNumber 2 to 8px
        
            
       
       
    @on Mobile
        ContactUSHeadline :
            inside screen  10 to 22px left
            inside screen  81 to 93px top
            
        ContactUSSubheadline:
            inside screen 10 to 22px left
            inside screen 128 to 139px top            
            
        ContactFirstNameLabel:
            inside screen 10 to 22px left
            inside screen 208 to 222px top	
            
        ContactLastNameLabel:
            inside screen  10 to 22px left
            inside screen  310 to 322px top
                   
        ContactEmailLabel:
            inside screen  10 to 22px left
            below ContactLastNameLabel 73 to 85px
            
        ContactSubjectLabel:
            inside screen  10 to 22px left
            below ContactEmailLabel 78 to 88px
            
        ContactDropDown:
            inside screen  10 to 22px left
            below ContactSubjectLabel 3 to 15px
            
        ContactMessageLabel:
            inside screen  10 to 22px left
            below ContactDropDown 25 to 36px      
            
        ContactSubmitButton:  
            inside screen 10 to 22px left
            below ContactDropDown 110 to 119px      
            
        ContactFirstNameField:
            inside screen  10 to 22px left
            below ContactFirstNameLabel 3 to 13px
            
        ContactLastNameField:
            inside screen 10 to 22px left
            below ContactLastNameLabel 3 to 13px
            
        ContactEmailNameField:
            inside screen  10 to 22px left
            below ContactEmailLabel 3 to 13px
            
        ContactMessageNameField:
            inside screen  10 to 22px left
            below ContactMessageLabel 3 to 13px
            
        MobContactlleftSideText1 :
            inside screen 10 to 22px left
            below ContactSubmitButton 99 to 109px
            
        MobContactleftSideText2:
            inside screen  10 to 22px left
            below ContactlleftSideText1 3 to 11px
                    
        MobContactleftSideContactNumber:
            inside screen  10 to 22px left
            below ContactleftSideText2 23 to 35px
            
        MobContactleftSideContactEmail:     
            inside screen  10 to 22px left
            below ContactleftSideContactNumber 2 to 8px
        
    
            