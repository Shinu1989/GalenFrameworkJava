package com.galenframework.java.USB.tests;

import com.galenframework.java.USB.components.GalenTestBase;
import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class APIPageTablet extends GalenTestBase {

    @Test(dataProvider = "devices")
    public void verify_usbAPIListiingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_USB, "/");
        getDriver().findElement(By.xpath("//header/div/div/button")).click();
        getDriver().findElement(By.xpath("//header//ul/li/a[contains(@href, '/api')]")).click();
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/USB/Tablet/APIListPageUSB.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_usbAPIDetailsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_USB, "/");
        getDriver().findElement(By.xpath("//header/div/div/button")).click();
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
        checkLayout("/specs/Sprint2/USB/Tablet/APIDetailsPageUSB.spec", device.getTags());
    }

}
