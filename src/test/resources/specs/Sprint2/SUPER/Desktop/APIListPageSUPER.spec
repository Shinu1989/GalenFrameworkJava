@objects
    APIPageHeading			            xpath   .//div/div[contains(@class,'titleTxtContent')]
    APIPageSummary			            xpath   .//div[contains(@class, 'detailTxtConten')]/p
    APIListTitle			            xpath   //span[1][contains(@class, 'list-title')]
    APIListTitle1			            xpath   (//span[1][contains(@class, 'list-title')])[1]
    APIListTag			                xpath   //span[2][contains(@class, 'list-title')]
    APIListTitle2			            xpath   (//span[1][contains(@class, 'list-title')])[2]
    APIListTag1			                xpath   (//span[2][contains(@class, 'list-title')])[1]
    APIListTag2			                xpath   (//span[2][contains(@class, 'list-title')])[2]
    APIListTextContent			        xpath    //div/div[@class='list-text-content']/p
    APIListTextContent1			        xpath   (//div/div[@class='list-text-content']/p)[1]
    APIListTextContent2			        xpath   (//div/div[@class='list-text-content']/p)[2]
    APIListCTA			                xpath   //div[contains(@class, 'list-item')]/div[2]/a
    APIListCTA1			                xpath   (//div[contains(@class, 'list-item')]/div[2]/a)[1]
    APIListCTA2 		                xpath   (//div[contains(@class, 'list-item')]/div[2]/a)[2]


= API Page Heading =
     @on Desktop
        APIPageHeading:
            css font-size is "50px"
            css line-height is "58px"
            css color is "rgba(255, 255, 255, 1)"
            css font-family matches ".*roboto.*"
        APIPageSummary:
            css font-size is "14px"
            css line-height is "18px"
            css color is "rgba(255, 255, 255, 1)"
            css font-family matches ".*roboto.*"
        APIListTitle:
             css font-size is "34px"
             css line-height is "38px"
             css color is "rgba(35, 36, 96, 1)"
             css font-family matches ".*roboto.*"
        APIListTag:
             css font-size is "34px"
             css line-height is "38px"
             css color is "rgba(35, 36, 96, 1)"
             css font-family matches ".*roboto.*"
        APIListTextContent:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(81, 84, 117, 1)"
             css font-family matches ".*roboto.*"
        APIListCTA:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(0, 0, 0, 1)"
             css font-family matches ".*roboto.*"
             css background-color is "rgba(110, 196, 255, 1)"

        APIPageHeading:
            inside screen 6 to 16px left, ~ 168px top
        APIPageSummary:
            right-of APIPageHeading
            inside screen 703 to 713px left left
        APIListTitle1:
             inside screen 6 to 16px left
             below APIPageHeading
             aligned vertically left APIPageHeading
        APIListTag1:
             right-of APIListTitle1 ~ 8px
        APIListTextContent1:
             inside screen 6 to 16px left
             below APIListTitle1 ~ 30px
             aligned vertically left APIListTitle1
        APIListCTA1:
             inside screen 6 to 16px left
             below APIListTextContent
             aligned vertically left APIListTextContent
        APIListTitle2:
             inside screen 703 to 713px left
             right-of APIListTag1
             aligned horizontally all APIListTitle1
        APIListTag2:
             right-of APIListTitle2 ~ 8px
        APIListTextContent2:
             inside screen 703 to 713px left
             below APIListTitle2 ~ 30px
             aligned vertically left APIListTitle2
        APIListCTA2:
             inside screen 703 to 713px left
             below APIListTextContent2
             aligned vertically left APIListTextContent2