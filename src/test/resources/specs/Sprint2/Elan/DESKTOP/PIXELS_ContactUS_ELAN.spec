@objects
    ContactUSHeadline           xpath  //section[@id='contact-us']//h2[contains(@class,'title')]
    ContactUSSubheadline        xpath  //section[@id='contact-us']//p[contains(@class,'description')]
    ContactFirstNameLabel       xpath  //section[@id='contact-us']//label[contains(@for,'first-name')]
    ContactLastNameLabel        xpath  //section[@id='contact-us']//label[contains(@for,'last-name')]
    ContactEmailLabel           xpath  //section[@id='contact-us']//label[contains(@for,'email-address')]
    ContactSubjectLabel         xpath  //section[@id='contact-us']//label[contains(@for,'edit-tid')]
    ContactDropDown             xpath  //section[@id='contact-us']//div[contains(@class,'custom-select')]
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
    ContactUSHeader             xpath   //header[contains(@class,'comp-header')]
    AllFieldsContainer          xpath   (//section[contains(@id,'contact')]//div[contains(@class,'form')])[8]
    
= CONTACT US =
    @on Desktop
        ContactUSHeadline :
            inside screen 406 to 416px left  
            below ContactUSHeader 93px to 99px           
            
        ContactUSSubheadline:
            inside screen 406 to 416px left
            below ContactUSHeadline 13 to 19px
            
            
        ContactFirstNameLabel:
            inside screen 406 to 416px left
            below ContactUSSubheadline 66 to 72px
                        
        ContactLastNameLabel:
            inside screen 704 to 714px left
            below ContactUSSubheadline 66 to 72px
                   
        ContactEmailLabel:
            inside screen 406 to 416px left
            below ContactFirstNameLabel 96 to 102px
            
        ContactSubjectLabel:
            inside screen 406 to 416px left
            below ContactEmailLabel 96 to 102px
            
        ContactDropDown:
            inside screen 406 to 416px left
            below ContactSubjectLabel 6 to 12px
            
        ContactMessageLabel:
            inside screen 406 to 416px left
            below ContactDropDown 24 to 30px      
            
        ContactSubmitButton:  
            inside screen 406 to 416px left
            below ContactMessageNameField 27 to 33px 
            inside AllFieldsContainer             	     
            
        ContactFirstNameField:
            inside screen 406 to 416px left
            below ContactFirstNameLabel 6 to 12px
            
        ContactLastNameField:
            inside screen 406 to 416px left
            below ContactLastNameLabel 6 to 12px
            
        ContactEmailNameField:
            inside screen 406 to 416px left
            below ContactEmailLabel 6 to 12px
            
        ContactMessageNameField:
            inside screen 406 to 416px left
            below ContactMessageLabel 6 to 12px
            
        ContactlleftSideText1:
            inside screen ~ 11px left
                        
        ContactleftSideText2:
            inside screen ~ 11px left
            below ContactlleftSideText1 3 to 9px
                    
        ContactleftSideContactNumber:
            inside screen ~ 11px left
            below ContactleftSideText2 29 to 35px
            
        ContactleftSideContactEmail:     
            inside screen ~ 11px left
            below ContactleftSideContactNumber 2 to 8px                
        
    @on tablet
        ContactUSHeadline :
            inside screen ~ 135px left            
            
        ContactUSSubheadline:
            inside screen ~ 135px left
            below ContactUSHeadline 13 to 19px
            
            
        ContactFirstNameLabel:
            inside screen ~ 135px left
            below ContactUSHeadline 116 to 122px
                        
        ContactLastNameLabel:
            inside screen ~ 507px left
            below ContactUSSubheadline 82 to 87px
                   
        ContactEmailLabel:
            inside screen ~ 135px left
            below ContactFirstNameLabel 76 to 82px
            
        ContactSubjectLabel:
            inside screen ~ 135px left
            below ContactEmailLabel 78 to 84px
            
        ContactDropDown:
            inside screen ~ 135px left
            below ContactSubjectLabel 6 to 12px
            
        ContactMessageLabel:
            inside screen ~ 135px left
            below ContactDropDown 37 to 43px      
            
        ContactSubmitButton:  
            inside screen ~ 135px left
            below ContactMessageNameField 111 to 118px      
            
        ContactFirstNameField:
            inside screen ~ 135px left
            below ContactFirstNameLabel 6 to 12px
            
        ContactLastNameField:
            inside screen ~ 507px left
            below ContactLastNameLabel 6 to 12px
            
        ContactEmailNameField:
            inside screen ~ 135px left
            below ContactEmailLabel 6 to 12px
            
        ContactMessageNameField:
            inside screen ~ 135px left
            below ContactMessageLabel 6 to 12px
            
        MobContactlleftSideText1:
            inside screen ~ 135px left
            below ContactSubmitButton 111 to 117px
                                    
        MobContactleftSideText2:
            inside screen ~ 135px left
            below ContactlleftSideText1 3 to 9px
                    
        MobContactleftSideContactNumber:
            inside screen ~ 631px left
            below ContactMessageNameField 279 to 285px
            
        MobContactleftSideContactEmail:     
            inside screen ~ 631px left
            below ContactleftSideContactNumber 2 to 8px                    
              
    @on Mobile
        ContactUSHeadline :
            inside screen ~ 8px left            
            
        ContactUSSubheadline:
            inside screen ~ 8px left
            below ContactUSHeadline 13 to 19px
            
            
        ContactFirstNameLabel:
            inside screen ~ 8px left
            below ContactUSSubheadline 44 to 50px
                        
        ContactLastNameLabel:
            inside screen ~ 8px left
            below ContactUSSubheadline 144 to 150px
                   
        ContactEmailLabel:
            inside screen ~ 8px left
            below ContactFirstNameLabel 176 to 182px
            
        ContactSubjectLabel:
            inside screen ~ 8px left
            below ContactEmailLabel 79 to 85px
            
        ContactDropDown:
            inside screen ~ 8px left
            below ContactSubjectLabel 6 to 12px
            
        ContactMessageLabel:
            inside screen ~ 8px left
            below ContactDropDown 28 to 34px      
            
        ContactSubmitButton:  
            inside screen ~ 8px left
            below ContactMessageNameField 111 to 117px      
            
        ContactFirstNameField:
            inside screen ~ 8px left
            below ContactFirstNameLabel 6 to 12px
            
        ContactLastNameField:
            inside screen ~ 8px left
            below ContactLastNameLabel 6 to 12px
            
        ContactEmailNameField:
            inside screen ~ 8px left
            below ContactEmailLabel 6 to 12px
            
        ContactMessageNameField:
            inside screen ~ 8px left
            below ContactMessageLabel 6 to 12px
            
        MobContactlleftSideText1:
            inside screen ~ 8px left
            below ContactSubmitButton 101 to 107px            
                        
        MobContactleftSideText2:
            inside screen ~ 8px left
            below ContactlleftSideText1 3 to 9px
                    
        MobContactleftSideContactNumber:
            inside screen ~ 8px left
            below ContactleftSideText2 26 to 32	px
            
        MobContactleftSideContactEmail:     
            inside screen ~ 8px left
            below ContactleftSideContactNumber 2 to 8px    