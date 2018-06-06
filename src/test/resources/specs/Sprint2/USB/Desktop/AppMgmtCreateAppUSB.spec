@objects
    MAPCreateAppNameField			    xpath   .//div[@class='add-app-form']/form//div/input[contains(@id,'edit-human')]
    MAPCreateAppCallBackUrlField		xpath	.//div[@class='add-app-form']/form//div/input[contains(@id,'new_callback_url')]
    MAPCreateAppProductOption1			xpath   (.//div[@class='add-app-form']/form/div//div[@id='api_product']//label[@class='option'])[1]
    MAPCreateAppProductOption2			xpath   (.//div[@class='add-app-form']/form/div//div[@id='api_product']//label[@class='option'])[2]
    MAPCreateAppSaveButton			    xpath   //div[@class='add-app-form']/form//div/input[contains(@id, 'edit-submit')]
    MAPcreateAppCancelButton			xpath   //form[contains(@id,'apps-edit')]//div/span[contains(@class, 'hide-form')]
    MAPXIcon			                xpath   .//*[@id='add-app']//button/span[contains(@class, 'close-hide-icon')][contains(@class, 'circled-cross-icon')]
    MAPCreatingAppText			        xpath   .//*[@id='add-app']//button/span[contains(@class, 'heading-open')]
    MAPCreateAppNameLabel               xpath   .//div[@class='add-app-form']/form//div/label[contains(@for,'edit-human')]
    MAPCreateAppNameField               xpath   .//div[@class='add-app-form']/form//div/input[contains(@id,'edit-human')]
    MAPCreateAppCallBackUrlLabel        xpath   .//div[@class='add-app-form']/form//div/label[contains(@for,'new_callback_url')]
    MAPCreateAppCallBackUrlField        xpath   .//div[@class='add-app-form']/form//div/input[contains(@id,'new_callback_url')]
    MAPcreateAppProducts                xpath   .//*[@id='api_product']/div/label[@class='option']
    MAPcreateAppProducts1               xpath   (.//*[@id='api_product']/div/label[@class='option'])[1]
    MAPcreateAppProducts2               xpath   (.//*[@id='api_product']/div/label[@class='option'])[2]
    MAPPageHeading			            xpath   .//*[@id='add-app']//h2[@class='app-heading']

= App Mangement - Create App Page =
    @on Desktop
        MAPXIcon:
            css background-color is "rgba(0, 150, 232, 1)"
        MAPCreatingAppText:
            css font-size is "14px"
            css line-height is "18px"
            css color is "rgba(10, 28, 118, 1)"
            css font-family matches ".*roboto.*"
        MAPCreateAppNameLabel:
            css font-size is "14px"
            css line-height is "18px"
            css color is "rgba(0, 0, 0, 1)"
            css font-family matches ".*roboto.*"
        MAPCreateAppCallBackUrlLabel:
            css font-size is "14px"
            css line-height is "18px"
            css color is "rgba(0, 0, 0, 1)"
            css font-family matches ".*roboto.*"
        MAPCreateAppSaveButton:
             css font-size is "14px"
             css line-height is "16px"
             css color is "rgba(0, 0, 0, 1)"
             css font-family matches ".*roboto.*"
             css background-color is "rgba(110, 196, 255, 1)"
        MAPcreateAppCancelButton:
              css font-size is "14px"
              css line-height is "16px"
              css color is "rgba(203, 52, 75, 1)"
              css font-family matches ".*roboto.*"
        MAPcreateAppProducts:
              css font-size is "14px"
              css line-height is "16px"
              css color is "rgba(33, 33, 33, 1)"
              css font-family matches ".*roboto.*"

        MAPXIcon:
            inside screen 34 to 44px right, ~ 104px top
            right-of MAPCreatingAppText
        MAPCreatingAppText:
            inside screen 906 to 916px left
            left-of MAPXIcon
        MAPCreateAppNameLabel:
            inside screen 34 to 44px left
            below MAPPageHeading
            aligned vertically left MAPPageHeading
        MAPCreateAppNameField:
            inside screen 34 to 44px left right
            below MAPCreateAppNameLabel ~ 10px
            aligned vertically left MAPCreateAppNameLabel
        MAPCreateAppCallBackUrlField:
            inside screen 34 to 44px left right
            below MAPCreateAppNameField
            aligned vertically all MAPCreateAppNameField
        MAPcreateAppProducts1:
             inside screen 34 to 44px left
             below MAPCreateAppCallBackUrlField
             aligned vertically left MAPCreateAppCallBackUrlField
        MAPcreateAppProducts2:
             inside screen 293 to 303px left
             right-of MAPcreateAppProducts1
             aligned horizontally all MAPcreateAppProducts1
        MAPCreateAppSaveButton:
            inside screen 34 to 44px left
            below MAPcreateAppProducts1
            aligned vertically left MAPcreateAppProducts1
        MAPcreateAppCancelButton:
            inside screen 333 to 343px left
            right-of MAPCreateAppSaveButton
            aligned horizontally all MAPCreateAppSaveButton