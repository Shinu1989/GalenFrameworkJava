@objects
    MAPAppDetailsAppDeleteBtn			xpath   //form[contains(@id,'application_delete')]//div/input[contains(@id, 'edit-submit')]
    MAPAppDetailsAppDeleteCancelBtn		xpath	//form[contains(@id,'application_delete')]//div/a[contains(@class, 'cancel-link')]
    MAPAppDetailsKeyTab			        xpath   //ul[contains(@class, 'nav-pills')]/li/a[contains(@href, 'keys')]
    MAPAppsPill			                xpath   .//div[@id='my-apps-accordion']/div/div[1][contains(@class, 'app-detail')]

= App Mangement - Delete App =
     @on Desktop
        MAPAppDetailsAppDeleteBtn:
            css background-color is "rgba(110, 196, 255, 1)"
            css font-size is "14px"
            css line-height is "16px"
            css color is "rgba(0, 0, 0, 1)"
            css font-family matches ".*roboto.*"
        MAPAppDetailsAppDeleteCancelBtn:
            css background-color is "rgba(255, 255, 255, 1)"
            css font-size is "14px"
            css line-height is "16px"
            css color is "rgba(203, 52, 75, 1)"
            css font-family matches ".*roboto.*"

        MAPAppDetailsAppDeleteBtn:
            inside screen 133 to 143px left
            below MAPAppsPill ~ 157px
        MAPAppDetailsAppDeleteCancelBtn:
            inside screen 432 to 442px left
            below MAPAppsPill ~ 183px
            right-of MAPAppDetailsAppDeleteBtn
            aligned horizontally all MAPAppDetailsAppDeleteBtn
