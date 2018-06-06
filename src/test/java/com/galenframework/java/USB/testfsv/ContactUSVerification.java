package com.galenframework.java.USB.testfsv;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class ContactUSVerification extends GalenTestBase {

    @Test(dataProvider = "devices")
    public void verify_FSVFontContactUSPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_CONTACTFSV, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/FSV/DESKTOP/Font_CONTACT_FSV.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_FSVPixelContactUsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_CONTACTFSV, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/FSV/DESKTOP/PIXELS_ContactUS_FSV.spec", device.getTags());
    }

}
