package com.galenframework.java.USB.TestSUPER;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class ContactUSVerification extends GalenTestBase {

    @Test(dataProvider = "devices")
    public void verify_SUPERFontContactUSPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_CONTACTFSV, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/SUPER/DESKTOP/Font_CONTACT_SUPER.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_SUPERPixelContactUsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_CONTACTFSV, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/Elan/DESKTOP/PIXELS_ContactUS_SUPER.spec", device.getTags());
    }

}
