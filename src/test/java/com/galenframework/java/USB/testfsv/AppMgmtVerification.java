package com.galenframework.java.USB.testfsv;

import com.galenframework.java.USB.components.GalenTestBase;
import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class AppMgmtVerification extends GalenTestBase {

   @Test(dataProvider = "devices")
    public void verify_AppMgmtPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FSV, "/user");
       try{
           Thread.sleep(20000);
       }catch(Exception e)
       {
           // catch exception here
       }
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
        getDriver().findElement(By.xpath(".//*[@id='block-menu-menu-user-logged-in-menu']/ul/li/a[contains(@href,'apps')]")).click();
        try{
            Thread.sleep(15000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/FSV/Desktop/AppMgmtPageFSV.spec", device.getTags());
    }

    @Test(dataProvider = "devices")
    public void verify_AppMgmtCreate(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FSV, "/user");
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
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
        getDriver().findElement(By.xpath(".//*[@id='block-menu-menu-user-logged-in-menu']/ul/li/a[contains(@href,'apps')]")).click();
        try{
            Thread.sleep(15000);
        }catch(Exception e)
        {
            // catch exception here
        }
        getDriver().findElement(By.xpath(".//*[@id='add-app']//button/span[contains(@class, 'close-hide-icon')][not (contains(@class, 'glyphicon-remove'))]")).click();
        try{
            Thread.sleep(4000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/FSV/Desktop/AppMgmtCreateAppFSV.spec", device.getTags());
    }

    @Test(dataProvider = "devices")
    public void verify_AppMgmtDetails(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FSV, "/user");
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
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
        checkLayout("/specs/Sprint2/FSV/Desktop/AppMgmtAppDetailsFSV.spec", device.getTags());
    }

    @Test(dataProvider = "devices")
    public void verify_AppMgmtDeleteApp(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FSV, "/user");
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
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
        getDriver().findElement(By.xpath(".//*[@id='block-menu-menu-user-logged-in-menu']/ul/li/a[contains(@href,'apps')]")).click();
        try{
            Thread.sleep(15000);
        }catch(Exception e)
        {
            // catch exception here
        }
        getDriver().findElement(By.xpath("(.//*[@id='my-apps-accordion']/div//h4/a/span[contains(@class, 'circled-expand-icon')])[1]")).click();
        getDriver().findElement(By.xpath("//ul[contains(@class, 'nav-pills')]/li[contains(@class,'hidden-xs')]/a[contains(@data-target, 'delete')]")).click();
        try{
            Thread.sleep(4000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/FSV/Desktop/AppMgmtDeleteAppFSV.spec", device.getTags());
    }

}
