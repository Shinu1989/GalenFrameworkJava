@objects
    MAPAppDetailsAppDeleteBtn			xpath   //form[contains(@id,'application_delete')]//div/input[contains(@id, 'edit-submit')]
    MAPAppDetailsAppDeleteCancelBtn		xpath	//form[contains(@id,'application_delete')]//div/a[contains(@class, 'cancel-link')]


= App Mangement - Delete App =
     @on Mobile
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