package com.galenframework.java.USB.TestUSB;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class ContactUSVerification extends GalenTestBase {

    @Test(dataProvider = "devices")
    public void verify_USBFontContactUSPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_CONTACTUSB, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/USB/DESKTOP/Font_CONTACT_USB.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_USBPixelContactUsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_CONTACTUSB, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/USB/DESKTOP/PIXELS_ContactUS_USB.spec", device.getTags());
    }

}
