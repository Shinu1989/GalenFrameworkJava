package com.galenframework.java.USB.testelan;

import com.galenframework.java.USB.components.GalenTestBase;
import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class APIPageVerification extends GalenTestBase {

    @Test(dataProvider = "devices")
    public void verify_elanAPIListiingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_ELAN, "/");
        getDriver().findElement(By.xpath("//header//ul/li/a[contains(@href, '/api')]")).click();
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/Elan/DESKTOP/APIListPageElan.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_elanAPIDetailsPage(TestDevice device) throws IOException {
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
        checkLayout("/specs/Sprint2/Elan/DESKTOP/APIDetailsPageElan.spec", device.getTags());
    }

}
