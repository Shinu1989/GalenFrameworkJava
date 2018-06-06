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
        
            
       
       
    