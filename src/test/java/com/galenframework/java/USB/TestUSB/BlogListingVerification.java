package com.galenframework.java.USB.TestUSB;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class BlogListingVerification extends GalenTestBase {


    @Test(dataProvider = "devices")
    public void verify_USBFontBlogListiingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_BLOG_LISTINGUSB, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/USB/DESKTOP/BlogListingUSB.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_USBPixelBlogListingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_BLOG_LISTINGUSB, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/USB/DESKTOP/PIXELSBlogListingUSB.spec", device.getTags());
    }

}
