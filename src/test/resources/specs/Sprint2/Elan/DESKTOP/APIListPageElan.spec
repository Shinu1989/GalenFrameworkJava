@objects
    APIPageHeading			            xpath   .//div/div[contains(@class,'titleTxtContent')]
    APIPageSummary			            xpath   .//div[contains(@class, 'detailTxtConten')]/p
    APIListTitle			            xpath   //span[1][contains(@class, 'list-title')]
    APIListTitle1			            xpath   (//span[1][contains(@class, 'list-title')])[1]
    APIListTag			                xpath   //span[2][contains(@class, 'list-title')]
    APIListTag1			                xpath   (//span[2][contains(@class, 'list-title')])[1]
    APIListTextContent			        xpath    //div/div[@class='list-text-content']/p
    APIListTextContent1			        xpath   (//div/div[@class='list-text-content']/p)[1]
    APIListCTA			                xpath   //div[contains(@class, 'list-item')]/div[2]/a
    APIListCTA1			                xpath   (//div[contains(@class, 'list-item')]/div[2]/a)[1]


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
             css color is "rgba(25, 57, 138, 1)"
             css font-family matches ".*roboto.*"
        APIListTag:
             css font-size is "34px"
             css line-height is "38px"
             css color is "rgba(25, 57, 138, 1)"
             css font-family matches ".*roboto.*"
        APIListTextContent:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(81, 84, 117, 1)"
             css font-family matches ".*roboto.*"
        APIListCTA:
             css font-size is "14px"
             css line-height is "16px"
             css color is "rgba(255, 255, 255, 1)"
             css font-family matches ".*roboto.*"
             css background-color is "rgba(108, 32, 126, 1)"

