@objects
    MAPPageHeading			            xpath   .//*[@id='add-app']//h2[@class='app-heading']
    MAPAppsPill			                xpath   .//div[@id='my-apps-accordion']/div/div[1][contains(@class, 'app-detail')]
    MAPPlusIcon			                xpath   .//*[@id='add-app']//button/span[contains(@class, 'close-hide-icon')][not (contains(@class, 'glyphicon-remove'))]
    MAPCreateAppText			        xpath   .//*[@id='add-app']//button/span[contains(@class, 'heading-close')]
    MAPExpandAppIcon1			        xpath   (.//*[@id='my-apps-accordion']/div//h4/a/span[contains(@class, 'circled-expand-icon')])[1]
    MAPExpandAppIcon2			        xpath   (.//*[@id='my-apps-accordion']/div//h4/a/span[contains(@class, 'circled-expand-icon')])[2]
    MAPAppKeys			                xpath   //table[@class='table']/tbody/tr/td[@class='key']
    MAPAppName1			                xpath   (//*[@id='my-apps-accordion']/div//h4/a/span[contains(@class, 'app-title')])[1]
    MAPAppStatus			            xpath   .//*[@id='my-apps-accordion']/div//div[contains(@class, 'status-label')]

= App Mangement Page =
     @on Tablet
        MAPPageHeading:
            css font-size is "34px"
            css line-height is "38px"
            css color is "rgba(199, 61, 72, 1)"
            css font-family matches ".*roboto.*"
        MAPAppName1:
            css font-size is "20px"
            css line-height is "24px"
            css color is "rgba(10, 28, 118, 1)"
            css font-family matches ".*roboto.*"
        MAPExpandAppIcon1:
             css background-color is "rgba(110, 196, 255, 1)"
        MAPAppsPill:
             css background-color is "rgba(255, 255, 255, 1)"
        MAPAppStatus:
             css font-size is "20px"
             css line-height is "24px"
             css color is "rgba(10, 28, 118, 1)"
             css font-family matches ".*roboto.*"
        MAPCreateAppText:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(10, 28, 118, 1)"
             css font-family matches ".*roboto.*"
        MAPPlusIcon:
             css background-color is "rgba(110, 196, 255, 1)"


        MAPPageHeading:
             inside screen ~ 51px left, ~ 103px top
        MAPAppsPill:
             inside screen ~ 51px left
             below MAPPageHeading ~ 102px
        MAPAppName1:
            inside MAPAppsPill ~ 62px left
        MAPAppStatus:
            inside MAPAppsPill ~ 34px right
            right-of MAPAppName1
        MAPCreateAppText:
             inside screen ~ 782px left
             right-of  MAPPageHeading
        MAPPlusIcon:
             inside screen ~ 48px right
             right-of MAPCreateAppText