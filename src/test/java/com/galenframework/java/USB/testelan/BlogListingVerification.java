package com.galenframework.java.USB.testelan;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class BlogListingVerification extends GalenTestBase {

	  @Test(dataProvider = "devices")
	    public void verify_elanFontBlogListiingPage(TestDevice device) throws IOException {
	        load(GalenTestBase.TEST_URL_BLOG_LISTINGUSB, "/");       
	        try{
	            Thread.sleep(20000);
	        }catch(Exception e)
	        {
	            // catch exception here
	        }
	        checkLayout("/specs/Sprint2/Elan/DESKTOP/BlogListingELAN.spec", device.getTags());
	    }

    @Test(dataProvider = "devices")
    public void verify_elanPixelBlogListingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_BLOG_LISTINGUSB, "/");        
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }     
        checkLayout("/specs/Sprint2/Elan/DESKTOP/PIXELBlogListingELAN.spec", device.getTags());
    }

}
