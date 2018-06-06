package com.galenframework.java.USB.testelavon;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class FAQVerification extends GalenTestBase {


    @Test(dataProvider = "devices")
    public void verify_ELAVONFAQFONTPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FAQELAVON, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/Elavon/DESKTOP/Font_FAQ_ELAVON.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_ELAVONPIXELFAQPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FAQELAVON, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/Elavon/DESKTOP/PIXELS_FAQ_ELAVON.spec", device.getTags());
    }

}
