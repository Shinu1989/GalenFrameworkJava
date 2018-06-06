package com.galenframework.java.USB.testelavon;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class TermsAndConditionsVerification extends GalenTestBase {


    @Test(dataProvider = "devices")
    public void verify_elavonFontTermsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_TERMSELAVON, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/Elavon/DESKTOP/Font_TermsCondition_ELAVON.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_elavonPixelTermsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_TERMSELAVON, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/Elavon/DESKTOP/PIXELSTermsConditionsELAVON.spec", device.getTags());
    }

}
