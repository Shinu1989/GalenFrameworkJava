package com.galenframework.java.USB.testelavon;

import com.galenframework.java.USB.components.GalenTestBase;
import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class APIPageVerification extends GalenTestBase {

    @Test(dataProvider = "devices")
    public void creativeVerification_elavonAPIListiingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_ELAVON, "/");
        getDriver().findElement(By.xpath("//header//ul/li/a[contains(@href, '/api')]")).click();
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/Elavon/DESKTOP/APIListPageElavon.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void creativeVerification_elavonAPIDetailsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_ELAVON, "/");
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
        checkLayout("/specs/Sprint2/Elavon/DESKTOP/APIDetailsPageElavon.spec", device.getTags());
    }

}
