package com.galenframework.java.USB.TestSUPER;

import com.galenframework.java.USB.components.GalenTestBase;
import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class APIPageVerification extends GalenTestBase {

    @Test(dataProvider = "devices")
    public void verify_SUPERAPIListiingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_ELAN, "/");
        getDriver().findElement(By.xpath("//header//ul/li/a[contains(@href, '/api')]")).click();
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/SUPER/DESKTOP/APIListPageSUPER.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_SUPERAPIDetailsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_ELAN, "/");
        getDriver().findElement(By.xpath("//header//ul/li/a[contains(@href, '/api')]")).click();
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        getDriver().findElement(By.xpath("(//div[contains(@class, 'list-item')]/div[2]/a)[1]")).click();
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/SUPER/DESKTOP/APIDetailsPageSUPER.spec", device.getTags());
    }

}
