@objects
    MAPCreateAppNameField			    xpath   .//div[@class='add-app-form']/form//div/input[contains(@id,'edit-human')]
    MAPCreateAppCallBackUrlField		xpath	.//div[@class='add-app-form']/form//div/input[contains(@id,'new_callback_url')]
    MAPCreateAppProductOption1			xpath   (.//div[@class='add-app-form']/form/div//div[@id='api_product']//label[@class='option'])[1]
    MAPCreateAppProductOption2			xpath   (.//div[@class='add-app-form']/form/div//div[@id='api_product']//label[@class='option'])[2]
    MAPCreateAppSaveButton			    xpath   //div[@class='add-app-form']/form//div/input[contains(@id, 'edit-submit')]
    MAPcreateAppCancelButton			xpath   //form[contains(@id,'apps-edit')]//div/span[contains(@class, 'hide-form')]
    MAPXIcon			                xpath   .//*[@id='add-app']//button/span[contains(@class, 'close-hide-icon')][contains(@class, 'glyphicon-remove')]
    MAPCreatingAppText			        xpath   .//*[@id='add-app']//button/span[contains(@class, 'heading-open')]
    MAPCreateAppNameLabel               xpath   .//div[@class='add-app-form']/form//div/label[contains(@for,'edit-human')]
    MAPCreateAppCallBackUrlLabel        xpath   .//div[@class='add-app-form']/form//div/label[contains(@for,'new_callback_url')]
    MAPcreateAppProducts                xpath   .//*[@id='api_product']/div/label[@class='option']

= App Mangement - Create App Page =
    @on tablet
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