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
     @on tablet
        MAPAppsPill:
            css background-color is "rgba(72, 168, 91, 1)"
        MAPAppDetailsKeyTab:
            css font-size is "14px"
            css line-height is "18px"
            css color is "rgba(0, 25, 112, 1)"
            css font-family matches ".*roboto.*"
        MAPAppDetailsTabDetails:
            css font-size is "14px"
            css line-height is "18px"
            css color is "rgba(0, 25, 112, 1)"
            css font-family matches ".*roboto.*"
        MAPAppDetailsTabAnalytics:
            css font-size is "14px"
            css line-height is "18px"
            css color is "rgba(0, 25, 112, 1)"
            css font-family matches ".*roboto.*"
        MAPAppDetailsEditLink:
            css font-size is "14px"
            css line-height is "18px"
            css color is "rgba(0, 25, 112, 1)"
            css font-family matches ".*roboto.*"
        MAPAppDetailsDeleteLink:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(0, 25, 112, 1)"
             css font-family matches ".*roboto.*"
        MAPAppName1:
             css font-size is "20px"
             css line-height is "24px"
             css color is "rgba(255, 255, 255, 1)"
             css font-family matches ".*roboto.*"
        MAPAppStatus:
             css font-size is "20px"
             css line-height is "24px"
             css color is "rgba(255, 255, 255, 1)"
             css font-family matches ".*roboto.*"