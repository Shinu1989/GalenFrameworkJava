package com.galenframework.java.USB.testfsv;

import com.galenframework.java.USB.components.GalenTestBase;
import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class APIPageVerification extends GalenTestBase {

    @Test(dataProvider = "devices")
    public void verify_fsvAPIListiingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FSV, "/user");
        getDriver().findElement(By.xpath(".//input[contains(@id, 'edit-name')]")).sendKeys("testuser@test.com");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-pass')]")).sendKeys("test@123");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-submit')]")).click();
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        getDriver().findElement(By.xpath(".//*[@id='secure-header']/nav/div[1]/button")).click();
        getDriver().findElement(By.xpath("//header//ul/li/a[contains(@href, '/api')]")).click();
        try{
            Thread.sleep(15000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/FSV/Desktop/APIListPageFSV.spec", device.getTags());
    }


    @Test(dataProvider = "devices")
    public void verify_fsvAPIDetailsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FSV, "/user");
        getDriver().findElement(By.xpath(".//input[contains(@id, 'edit-name')]")).sendKeys("testuser@test.com");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-pass')]")).sendKeys("test@123");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-submit')]")).click();
        try{
            Thread.sleep(15000);
        }catch(Exception e)
        {
            // catch exception here
        }
        getDriver().findElement(By.xpath(".//*[@id='secure-header']/nav/div[1]/button")).click();
        getDriver().findElement(By.xpath("//header//ul/li/a[contains(@href, '/api')]")).click();
        try{
            Thread.sleep(15000);
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
        checkLayout("/specs/Sprint2/FSV/Desktop/APIDetailsPageFSV.spec", device.getTags());
    }

}
