package com.galenframework.java.USB.testelan;

import com.galenframework.java.USB.components.GalenTestBase;
import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class BlogDetailVerification extends GalenTestBase {

    @Test(dataProvider = "devices")
    public void verify_elanFontBlogDetailPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_BLOG_DetailELAN, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/Elan/DESKTOP/BlogDetailPageELAN.spec", device.getTags());
    }

/*
    @Test(dataProvider = "devices")
    public void verify_elanPixelBlogDetailsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_BLOG_DetailELAN, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/Elan/DESKTOP/PIXELBlogDetailPageELAN.spec", device.getTags());
    }
*/
}
