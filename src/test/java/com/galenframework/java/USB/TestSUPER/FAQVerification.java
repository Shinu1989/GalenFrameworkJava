package com.galenframework.java.USB.TestSUPER;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class FAQVerification extends GalenTestBase {


    @Test(dataProvider = "devices")
    public void verify_SUPERFAQFONTPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FAQFSV, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/SUPER/DESKTOP/Font_FAQ_SUPER.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_SUPERPIXELFAQPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FAQFSV, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/SUPER/DESKTOP/PIXELS_FAQ_SUPER.spec", device.getTags());
    }

}
