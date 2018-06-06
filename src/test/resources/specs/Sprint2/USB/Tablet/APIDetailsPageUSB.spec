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
     @on Tablet
        APIDetailsPageHead:
            css font-size is "34px"
            css line-height is "38px"
            css color is "rgba(13, 38, 126, 1)"
            css font-family matches ".*roboto.*"
        APIDetailsPageSubHead:
            css font-size is "20px"
            css line-height is "24px"
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
             inside screen 6 to 16px left
        APIDetailsDocumentation:
             inside screen 21 to 31px left
        LeftSectionAPIDropDown:
             inside APIDetailsLeftSection 6 to 16px left, 111 to 121px top
        APILeftNavOverView:
             inside APIDetailsLeftSection 6 to 16px left
             below LeftSectionAPIDropDown 10 to 20px
        APIDetailsPageHead:
             inside screen 6 to 16px left, 122 to 132px top
             below APIDetailsDocumentation
        APIDetailsPageSubHead:
            inside screen 6 to 16px left
            below APIDetailsPageHead 31 to 41px
            aligned vertically left APIDetailsPageHead

