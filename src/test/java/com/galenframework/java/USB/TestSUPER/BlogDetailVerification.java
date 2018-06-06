package com.galenframework.java.USB.TestSUPER;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class BlogDetailVerification extends GalenTestBase {


    @Test(dataProvider = "devices")
    public void verify_SUPERFontBlogDetailPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_BLOG_DetailSUPER, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/SUPERDESKTOP/BlogDetailPageSUPER.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_SUPERPixelBlogDetailsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_BLOG_DetailSUPER, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/Elan/DESKTOP/PIXELBlogDetailPageSUPER.spec", device.getTags());
    }

}
