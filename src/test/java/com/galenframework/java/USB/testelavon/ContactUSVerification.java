package com.galenframework.java.USB.testelavon;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class ContactUSVerification extends GalenTestBase {

    @Test(dataProvider = "devices")
    public void verify_ELAVONFontContactUSPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_CONTACTELAVON, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/Elavon/DESKTOP/Font_CONTACT_ELAVON.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_ElavonPixelContactUsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_CONTACTELAVON, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/Elavon/DESKTOP/PIXELS_ContactUS_ELAVON.spec", device.getTags());
    }

}
