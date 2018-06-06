package com.galenframework.java.USB.TestSUPER;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class TermsAndConditionsVerification extends GalenTestBase {


    @Test(dataProvider = "devices")
    public void verify_SUPERFontTermsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_TERMSFSV, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/Elan/DESKTOP/Font_TermsCondition_SUPER.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_SUPERPixelTermsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_TERMSFSV, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/Elan/DESKTOP/PIXELSTermsConditionsSUPER.spec", device.getTags());
    }

}
