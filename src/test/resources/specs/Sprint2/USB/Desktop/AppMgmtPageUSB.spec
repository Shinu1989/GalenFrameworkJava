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
     @on Desktop
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
             inside screen 34 to 44px left, ~ 125px top
        MAPAppsPill:
             inside screen 34 to 44px left
             below MAPPageHeading ~ 123px
             aligned vertically left MAPPageHeading
        MAPAppName1:
            inside MAPAppsPill 95 to 105px left
        MAPAppStatus:
            inside MAPAppsPill 36 to 46px right
            right-of MAPAppName1
            aligned horizontally all MAPAppName1
        MAPCreateAppText:
             inside screen 931 to 941px left
             right-of  MAPPageHeading
             aligned horizontally bottom MAPPageHeading
        MAPPlusIcon:
             inside screen 34 to 44px right
             right-of MAPCreateAppText