package com.galenframework.java.USB.testelavon;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class BlogListingVerification extends GalenTestBase {


    @Test(dataProvider = "devices")
    public void verify_elavonFontBlogListiingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_BLOG_LISTINGELAVON, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/Elavon/DESKTOP/BlogListingELAVON.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_elavonPixelBlogListingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_BLOG_LISTINGELAVON, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/Elavon/DESKTOP/PIXELBlogListingELAVON.spec", device.getTags());
    }

}
