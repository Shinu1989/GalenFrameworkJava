package com.galenframework.java.USB.TestSUPER;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class BlogListingVerification extends GalenTestBase {


    @Test(dataProvider = "devices")
    public void verify_SUPERFontBlogListiingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_BLOG_LISTINGSUPER, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/SUPER/DESKTOP/BlogListingSUPER.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_SUPERPixelBlogListingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_BLOG_LISTINGSUPER, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/Elan/DESKTOP/PIXELSBlogListingSUPER.spec", device.getTags());
    }

}
