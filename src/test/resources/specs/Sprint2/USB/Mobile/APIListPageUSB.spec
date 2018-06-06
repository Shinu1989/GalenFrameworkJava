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
     @on Mobile
        APIPageHeading:
            css font-size is "32px"
            css line-height is "36px"
            css color is "rgba(255, 255, 255, 1)"
            css font-family matches ".*roboto.*"
        APIPageSummary:
            css font-size is "14px"
            css line-height is "18px"
            css color is "rgba(255, 255, 255, 1)"
            css font-family matches ".*roboto.*"
        APIListTitle:
             css font-size is "22px"
             css line-height is "26px"
             css color is "rgba(35, 36, 96, 1)"
             css font-family matches ".*roboto.*"
        APIListTag:
             css font-size is "22px"
             css line-height is "28px"
             css color is "rgba(35, 36, 96, 1)"
             css font-family matches ".*roboto.*"
        APIListTextContent:
             css font-size is "14px"
             css line-height is "18px"
             css color is "rgba(81, 84, 117, 1)"
             css font-family matches ".*roboto.*"
        APIListCTA:
             css font-size is "14px"
             css line-height is "16px"
             css color is "rgba(0, 0, 0, 1)"
             css font-family matches ".*roboto.*"
             css background-color is "rgba(108, 196, 255, 1)"


        APIPageHeading:
             inside screen  3 to 13px left, 123 to 133px top
        APIPageSummary:
             inside screen 3 to 13px left, 330 to 340px top
             below APIPageHeading 33 to 43px
             aligned vertically left APIPageHeading
        APIListTitle1:
             inside screen 3 to 13px left
             below APIPageSummary
             aligned vertically left APIPageSummary
        APIListTag1:
             right-of APIListTitle1 ~ 6px
        APIListTextContent1:
             inside screen 3 to 13px left
             below APIListTitle1 26 to 36px
             aligned vertically left APIListTitle1
        APIListCTA1:
             inside screen 3 to 13px left
             below APIListTextContent1
             aligned vertically left APIListTextContent1
        APIListTitle2:
             inside screen 3 to 13px left
             below  APIListCTA1
             aligned vertically left APIListCTA1
        APIListTag2:
             right-of APIListTitle2 ~ 6px
        APIListTextContent2:
             inside screen 3 to 13px left
             below APIListTitle2 26 to 36px
             aligned vertically left APIListTitle2
        APIListCTA2:
             inside screen 3 to 13px left
             below APIListTextContent2
             aligned vertically left APIListTextContent2