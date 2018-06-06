@objects

    MAPAppDetails			            xpath   .//*[contains(@id, 'my-apps-collapse')]/div[contains(@class, 'app-detail-body')]
    MAPAppDetailsKeyTab			        xpath   //ul[contains(@class, 'nav-pills')]/li/a[contains(@href, 'keys')]
    MAPAppDetailsTabDetails			    xpath   //ul[contains(@class, 'nav-pills')]/li/a[contains(@href, 'details')]
    MAPAppDetailsTabAnalytics			xpath   //ul[contains(@class, 'nav-pills')]/li/a[contains(@href, '/app-detail/')]
    MAPAppDetailsEditLink			    xpath   //ul[contains(@class, 'nav-pills')]/li[contains(@class,'hidden-xs')]/a[contains(@data-target, 'edit')]
    MAPAppDetailsDeleteLink			    xpath   //ul[contains(@class, 'nav-pills')]/li[contains(@class,'hidden-xs')]/a[contains(@data-target, 'delete')]
    MAPAppsPill			                xpath   .//div[@id='my-apps-accordion']/div/div[1][contains(@class, 'app-detail')]
    MAPAppName1			                xpath   (//*[@id='my-apps-accordion']/div//h4/a/span[contains(@class, 'app-title')])[1]
    MAPAppStatus			            xpath   .//*[@id='my-apps-accordion']/div//div[contains(@class, 'status-label')]

= App Mangement - App Details =
     @on Tablet
        APAppsPill:
            css background-color is "rgba(110, 196, 255, 1)"
        MAPAppDetailsKeyTab:
            css font-size is "14px"
            css line-height is "18px"
            css color is "rgba(10, 28, 118, 1)"
            css font-family matches ".*roboto.*"
        MAPAppDetailsTabDetails:
            css font-size is "14px"
            css line-height is "18px"
            css color is "rgba(10, 28, 118, 1)"
            css font-family matches ".*roboto.*"
        MAPAppDetailsTabAnalytics:
            css font-size is "14px"
            css line-height is "18px"
            css color is "rgba(10, 28, 118, 1)"
            css font-family matches ".*roboto.*"
        MAPAppDetailsEditLink:
            css font-size is "14px"
            css line-height is "18px"
            css color is "rgba(10, 28, 118, 1)"
            css font-family matches ".*roboto.*"
        MAPAppDetailsDeleteLink:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(10, 28, 118, 1)"
             css font-family matches ".*roboto.*"
        MAPAppName1:
             css font-size is "20px"
             css line-height is "24px"
             css color is "rgba(10, 28, 118, 1)"
             css font-family matches ".*roboto.*"
        MAPAppStatus:
             css font-size is "20px"
             css line-height is "24px"
             css color is "rgba(10, 28, 118, 1)"
             css font-family matches ".*roboto.*"

        MAPAppsPill:
             inside screen ~ 51px left
        MAPAppDetailsKeyTab:
             inside screen ~ 128px left
             below MAPAppsPill ~ 45px
        MAPAppDetailsTabDetails:
             inside screen ~ 176px left
             right-of MAPAppDetailsKeyTab
             aligned horizontally all MAPAppDetailsKeyTab
        MAPAppDetailsTabAnalytics:
             inside screen ~ 259px left
             right-of MAPAppDetailsTabDetails
             aligned horizontally all MAPAppDetailsTabDetails
        MAPAppDetailsEditLink:
              inside screen ~ 225px right
              right-of MAPAppDetailsTabAnalytics
              aligned horizontally all MAPAppDetailsTabAnalytics
        MAPAppDetailsDeleteLink:
              inside screen ~ 125px right
              right-of MAPAppDetailsEditLink
              aligned horizontally all MAPAppDetailsEditLink