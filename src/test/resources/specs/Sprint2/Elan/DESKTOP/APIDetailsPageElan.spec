@objects
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
            css line-height is "38px"
            css color is "rgba(39, 69, 146, 1)"
            css font-family matches ".*roboto.*"
        APIDetailsPageSubHead:
            css font-size is "20px"
            css line-height is "24px"
            css color is "rgba(108, 32, 126, 1)"
            css font-family matches ".*roboto.*"
        APIDetailsDocumentation:
             css font-size is "20px"
             css line-height is "31px"
             css color is "rgba(81, 84, 117, 1)"
             css font-family matches ".*roboto.*"
        APISelectionSelectedValue:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(11, 19, 97, 1)"
             css font-family matches ".*roboto.*"
        APILeftNavOverView:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(38, 52, 69, 1)"
             css font-family matches ".*roboto.*"
        APILeftNavTextBelowOverView:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(38, 52, 69, 1)"
             css font-family matches ".*roboto.*"
        APIRightSectionContent:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(38, 52, 69, 1)"
             css font-family matches ".*roboto.*"
