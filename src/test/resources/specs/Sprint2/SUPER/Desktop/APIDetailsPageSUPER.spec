@objects
    APIDetailsLeftSection               xpath   .//*[@id='api-detail']
    LeftSectionAPIDropDown              xpath   .//*[@id='api-detail']/div/div[@class='app-drop-value']
    APIDetailsPageHead			        xpath   //section/h1[@class='api-page-title']
    APIDetailsPageSubHead			    xpath   //section/h1[@class='api-page-title']/following-sibling::h2
    APISelectionSelectedValue			xpath   .//*[@id='api-detail']//div[@class='app-drop-value']/div
    APIDetailsDocumentation             xpath   .//*[@id='api-detail']
    APILeftNavOverView                  xpath   (.//*[@id='api-detail']//p[@class='app-nav-sub-title']/a)[1]
    APILeftNavTextBelowOverView         xpath   (.//*[@id='api-detail']//p[@class='app-nav-sub-title']/a)[2]
    APIRightSectionContent              xpath   //section[2]//div[@class='field-items']

= API Details Page =
     @on Desktop
        APIDetailsPageHead:
            css font-size is "34px"
            css line-height is "40px"
            css color is "rgba(7, 21, 89, 1)"
            css font-family matches ".*roboto.*"
        APIDetailsPageSubHead:
            css font-size is "20px"
            css line-height is "24px"
            css color is "rgba(7, 21, 89, 1)"
            css font-family matches ".*roboto.*
        APISelectionSelectedValue:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(81, 84, 117, 1)"
             css font-family matches ".*roboto.*"
        APILeftNavOverView:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(7, 21, 89, 1)"
             css font-family matches ".*roboto.*"
        APILeftNavTextBelowOverView:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(81, 84, 117, 1)"
             css font-family matches ".*roboto.*"
        APIRightSectionContent:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(81, 84, 117, 1)"
             css font-family matches ".*roboto.*"

        APIDetailsLeftSection:
             inside screen 6 to 16px left
        LeftSectionAPIDropDown:
             inside APIDetailsLeftSection 6 to 16px left
        APILeftNavOverView:
             inside APIDetailsLeftSection 6 to 16px left
             below LeftSectionAPIDropDown ~ 17px
             aligned vertically left LeftSectionAPIDropDown
        APIDetailsPageHead:
             inside screen 205 to 215px left
             right-of APIDetailsLeftSection 17 to 27px
        APIDetailsPageSubHead:
            right-of APIDetailsLeftSection 17 to 27px
            below APIDetailsPageHead
            aligned vertically left APIDetailsPageHead
