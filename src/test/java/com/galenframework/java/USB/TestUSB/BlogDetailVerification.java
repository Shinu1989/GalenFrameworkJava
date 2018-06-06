package com.galenframework.java.USB.TestUSB;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class BlogDetailVerification extends GalenTestBase {


    @Test(dataProvider = "devices")
    public void verify_USBFontBlogDetailPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_BLOG_DetailUSB, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/USB/DESKTOP/BlogDetailPageUSB.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_USBPixelBlogDetailsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_BLOG_DetailUSB, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/USB/DESKTOP/PIXELBlogDetailPageUSB.spec", device.getTags());
    }

}
