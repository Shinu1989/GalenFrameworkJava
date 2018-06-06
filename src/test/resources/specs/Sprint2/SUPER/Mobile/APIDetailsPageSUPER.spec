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
     @on Mobile
        APIDetailsPageHead:
            css font-size is "34px"
            css line-height is "38px"
            css color is "rgba(13, 38, 126, 1)"
            css font-family matches ".*roboto.*"
        APIDetailsPageSubHead:
            css font-size is "20px"
            css line-height is "31px"
            css color is "rgba(13, 38, 126, 1)"
            css font-family matches ".*roboto.*"
        APIDetailsDocumentation:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(66, 66, 66, 1)"
             css font-family matches ".*roboto.*"
        APISelectionSelectedValue:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(13, 38, 126, 1)"
             css font-family matches ".*roboto.*"
        APILeftNavOverView:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(66, 66, 66, 1)"
             css font-family matches ".*roboto.*"
        APILeftNavTextBelowOverView:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(66, 66, 66, 1)"
             css font-family matches ".*roboto.*"
        APIRightSectionContent:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(35, 36, 96, 1)"
             css font-family matches ".*roboto.*"

        APIDetailsLeftSection:
             inside screen 3 to 13px left
        APIDetailsDocumentation:
             inside screen 26 to 37px left, 64 to 74px top
        LeftSectionAPIDropDown:
             inside APIDetailsLeftSection 3 to 13px left
             below APIDetailsDocumentation 25 to 35px
        APILeftNavOverView:
             inside APIDetailsLeftSection 3 to 13px left
             below LeftSectionAPIDropDown 10 to 19px
        APIDetailsPageHead:
             inside screen 3 to 13px left, 120 to 130px top
        APIDetailsPageSubHead:
            inside screen 3 to 13px left, 231 to 241px top
            below APIDetailsPageHead
            aligned vertically left APIDetailsPageHead
        APIRightSectionContent:
             inside screen 3 to 13px left, 231 to 241px top
             below  APIDetailsPageSubHead
             aligned vertically left  APIDetailsPageSubHead