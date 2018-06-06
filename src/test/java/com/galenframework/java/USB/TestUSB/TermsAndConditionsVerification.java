package com.galenframework.java.USB.TestUSB;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class TermsAndConditionsVerification extends GalenTestBase {


    @Test(dataProvider = "devices")
    public void verify_USBFontTermsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_TERMSUSB, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/USB/DESKTOP/Font_TermsCondition_USB.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_USBPixelTermsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_TERMSUSB, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/USB/DESKTOP/PIXELSTermsConditionsUSB.spec", device.getTags());
    }

}
