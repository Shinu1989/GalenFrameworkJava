package com.galenframework.java.USB.TestUSB;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class FAQVerification extends GalenTestBase {


    @Test(dataProvider = "devices")
    public void verify_USBFAQFONTPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FAQUSB, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/USB/DESKTOP/Font_FAQ_USB.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_USBPIXELFAQPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FAQUSB, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/USB/DESKTOP/PIXELS_FAQ_USB.spec", device.getTags());
    }

}
