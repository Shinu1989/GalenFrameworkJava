package com.galenframework.java.USB.testelavon;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class BlogDetailVerification extends GalenTestBase {


    @Test(dataProvider = "devices")
    public void verify_elavonFontBlogDetailPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_BLOG_DetailELAVON, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/Elavon/DESKTOP/BlogDetailPageELAVON.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_elavonPixelBlogDetailsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_BLOG_DetailELAVON, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/Elavon/DESKTOP/PIXELBlogDetailPageELAVON.spec", device.getTags());
    }

}
