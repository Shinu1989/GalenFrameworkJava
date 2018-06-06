@objects
    NoAppMsg			                xpath   //section/div/p[@class='no-app-msg']
    NoAppPageCreateAppBtn			    xpath   //section/div/a[contains(@href,'apps')]
    AddAppFormFromNoApp			        xpath   .//*[@id='add-app']/div[@class='add-app-form']
    AddAppFormFromNoAppCancelBtn		xpath 	//form[contains(@id,'apps-edit')]//div/div/a
    ErrorMessage			            xpath   .//div[@class='messages error']


= App Mangement - No App =
     @on Desktop
        NoAppMsg:
            css font-size is "34px"
            css line-height is "38px"
            css color is "rgba(199, 61, 72, 1)"
            css font-family matches ".*roboto.*"
        NoAppPageCreateAppBtn:
            css background-color "rgba(110, 196, 255, 1)"
            css font-size is "14px"
            css line-height is "16px"
            css color is "rgba(0, 0, 0, 1)"
            css font-family matches ".*roboto.*"