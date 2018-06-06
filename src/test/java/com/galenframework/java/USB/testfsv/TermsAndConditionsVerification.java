package com.galenframework.java.USB.testfsv;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class TermsAndConditionsVerification extends GalenTestBase {


    @Test(dataProvider = "devices")
    public void verify_FSVFontTermsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_TERMSFSV, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/FSV/DESKTOP/Font_TermsCondition_FSV.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_FSVPixelTermsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_TERMSFSV, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/FSV/DESKTOP/PIXELSTermsConditionsFSV.spec", device.getTags());
    }

}
