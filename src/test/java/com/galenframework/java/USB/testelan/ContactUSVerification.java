package com.galenframework.java.USB.testelan;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class ContactUSVerification extends GalenTestBase {


    @Test(dataProvider = "devices")
    public void verify_elanFontBlogListiingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_CONTACTELAN, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/Elan/DESKTOP/Font_CONTACT_ELAN.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_elanPixelBlogDetailsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_CONTACTELAN, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/Elan/DESKTOP/TEST_URL_BLOG_DetailUSB", device.getTags());
    }

}
