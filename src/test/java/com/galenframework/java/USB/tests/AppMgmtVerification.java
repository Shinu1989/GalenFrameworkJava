package com.galenframework.java.USB.tests;

import com.galenframework.java.USB.components.GalenTestBase;
import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class AppMgmtVerification extends GalenTestBase {

   @Test(dataProvider = "devices")
    public void verify_usbAppMgmtPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_USB, "/user");
        getDriver().findElement(By.xpath(".//input[contains(@id, 'edit-name')]")).sendKeys("testuser@test.com");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-pass')]")).sendKeys("test@123");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-submit')]")).click();
        try{
            Thread.sleep(15000);
        }catch(Exception e)
        {
            // catch exception here
        }
        getDriver().findElement(By.xpath(".//*[@id='secure-header']/div/nav//button")).click();
        if (getDriver().findElement(By.xpath(".//*[@id='block-menu-menu-user-logged-in-menu']/ul/li/a[contains(@href,'apps')]")).isDisplayed()){
            getDriver().findElement(By.xpath(".//*[@id='block-menu-menu-user-logged-in-menu']/ul/li/a[contains(@href,'apps')]")).click();
        }
        try{
            Thread.sleep(15000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/USB/Desktop/AppMgmtPageUSB.spec", device.getTags());
    }

    @Test(dataProvider = "devices")
    public void verify_usbAppMgmtCreate(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_USB, "/user");
        getDriver().findElement(By.xpath(".//input[contains(@id, 'edit-name')]")).sendKeys("testuser@test.com");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-pass')]")).sendKeys("test@123");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-submit')]")).click();
        try{
            Thread.sleep(15000);
        }catch(Exception e)
        {
            // catch exception here
        }
        getDriver().findElement(By.xpath(".//*[@id='secure-header']/div/nav//button")).click();
        getDriver().findElement(By.xpath(".//*[@id='block-menu-menu-user-logged-in-menu']/ul/li/a[contains(@href,'apps')]")).click();
        try{
            Thread.sleep(25000);
        }catch(Exception e)
        {
            // catch exception here
        }
        getDriver().findElement(By.xpath(".//*[@id='add-app']//button/span[contains(@class, 'close-hide-icon')][not (contains(@class, 'circled-cross-icon'))]")).click();
        try{
            Thread.sleep(4000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/USB/Desktop/AppMgmtCreateAppUSB.spec", device.getTags());
    }

    @Test(dataProvider = "devices")
    public void verify_usbAppMgmtDetails(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_USB, "/user");
        getDriver().findElement(By.xpath(".//input[contains(@id, 'edit-name')]")).sendKeys("testuser@test.com");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-pass')]")).sendKeys("test@123");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-submit')]")).click();
        try{
            Thread.sleep(15000);
        }catch(Exception e)
        {
            // catch exception here
        }
        getDriver().findElement(By.xpath(".//*[@id='secure-header']/div/nav//button")).click();
        getDriver().findElement(By.xpath(".//*[@id='block-menu-menu-user-logged-in-menu']/ul/li/a[contains(@href,'apps')]")).click();
        try{
            Thread.sleep(15000);
        }catch(Exception e)
        {
            // catch exception here
        }
        getDriver().findElement(By.xpath("(.//*[@id='my-apps-accordion']/div//h4/a/span[contains(@class, 'circled-expand-icon')])[1]")).click();
        try{
            Thread.sleep(4000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/USB/Desktop/AppMgmtAppDetails.spec", device.getTags());
    }

    @Test(dataProvider = "devices")
    public void verify_usbAppMgmtDeleteApp(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_USB, "/user");
        getDriver().findElement(By.xpath(".//input[contains(@id, 'edit-name')]")).sendKeys("testuser@test.com");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-pass')]")).sendKeys("test@123");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-submit')]")).click();
        try{
            Thread.sleep(15000);
        }catch(Exception e)
        {
            // catch exception here
        }
        getDriver().findElement(By.xpath(".//*[@id='secure-header']/div/nav//button")).click();
        getDriver().findElement(By.xpath(".//*[@id='block-menu-menu-user-logged-in-menu']/ul/li/a[contains(@href,'apps')]")).click();
        try{
            Thread.sleep(15000);
        }catch(Exception e)
        {
            // catch exception here
        }
        getDriver().findElement(By.xpath("(.//*[@id='my-apps-accordion']/div//h4/a/span[contains(@class, 'circled-expand-icon')])[1]")).click();
        try{
            Thread.sleep(8000);
        }catch(Exception e)
        {
            // catch exception here
        }
        getDriver().findElement(By.xpath("//ul[contains(@class, 'nav-pills')]/li[contains(@class,'hidden-xs')]/a[contains(@data-target, 'delete')]")).click();
        try{
            Thread.sleep(4000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/USB/Desktop/AppMgmtDeleteApp.spec", device.getTags());
    }

}
