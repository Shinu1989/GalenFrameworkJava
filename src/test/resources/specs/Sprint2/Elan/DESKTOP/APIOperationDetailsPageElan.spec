@objects
    ODPOperationButton			        xpath   .//*[@id='method_content']/div//div//div/p[@data-role='verb']
    ODPOperationName			        xpath   .//div[@class='title_container']/h2
    ODPOperationDescription			    xpath   .//div[@data-role='method-description']
    ODPResourceURLHeading			    xpath   .//div[@class='description_and_url_container']/h3
    ODPResourceURL			            xpath   .//div[@class='description_and_url_container']/div/p
    ODPRequestTab			            xpath   .//*[@id='link_request_tab']
    ODPResponseTab			            xpath   .//*[@id='link_response_tab']
    ODPCurlTab			                xpath   .//*[@id='link_curl_tab']
    ODPResponseErrorHead			    xpath   .//*[@id='method_content']/div/h3
    ODPReponseErrorTableHeadHttp	    xpath   (.//*[@id='method_content']/div/ul/li[contains(@class,'title')]/div)[1]
    ODPReponseErrorTableHeadError		xpath 	(.//*[@id='method_content']/div/ul/li[contains(@class,'title')]/div)[1]
    ODPReponseErrorTableHeadDesc		xpath	(.//*[@id='method_content']/div/ul/li[contains(@class,'title')]/div)[1]
    ODPRequestfield			            xpath   .//div[contains(@class,'CodeMirror-sizer')]/div/div[@class='CodeMirror-lines']
    ODPSendRequestBtn			        xpath   .//button[@id='send_request']
    ODPResponseContainer			    xpath   .//div[@id='request_response_container']