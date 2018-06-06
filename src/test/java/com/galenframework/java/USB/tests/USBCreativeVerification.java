package com.galenframework.java.USB.tests;

import com.galenframework.java.USB.components.GalenTestBase;
import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class USBCreativeVerification extends GalenTestBase {

   /*@Test(dataProvider = "devices")
    public void usbHomePage_creativeTest_onDeskTop(TestDevice device) throws IOException {
       System.out.println("Entered landing page method ");
        load("/");
        if(device.getName().equalsIgnoreCase("Mobile") || device.getName().equalsIgnoreCase("tablet")){
            getDriver().findElement(By.xpath("//header//div[@class='burger-menu']")).click();
            checkLayout("/specs/elanpubliclanding.spec", device.getTags());
        }else{
            checkLayout("/specs/elanpubliclanding.spec", device.getTags());
        }
       checkLayout("/specs/elanpubliclanding.spec", device.getTags());
    }*/


    /*
    *********  TEST SUITE RELATED TO USB SITE **********
    @AUTHOR
     */
    @Test(dataProvider = "devices")
    public void verify_usbPublicLandingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_USB, "/");
        checkLayout("/specs/Sprint1/usbpubliclanding.spec", device.getTags());
    }

    @Test(dataProvider = "devices")
    public void verify_usbSecureLandingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_USB, "/user");
        getDriver().findElement(By.xpath(".//input[contains(@id, 'edit-name')]")).sendKeys("ssinghal@sapient.com");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-pass')]")).sendKeys("ssinghal");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-submit')]")).click();
        try{
            getDriver().wait(15000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint1/usbsecurelanding.spec", device.getTags());
    }

    /*
    *********  TEST SUITE RELATED TO ELAN SITE **********
    @AUTHOR
    */
    @Test(dataProvider = "devices")
    public void verify_elanPublicLandingPage(TestDevice device) throws IOException {
        System.out.println("Entered landing page method ");
        load(GalenTestBase.TEST_URL_ELAN, "/");
        checkLayout("/specs/Sprint1/elanpubliclanding.spec", device.getTags());
    }

    @Test(dataProvider = "devices")
    public void verify_elanSecureLandingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_ELAN, "/user");
        getDriver().findElement(By.xpath(".//input[contains(@id, 'edit-name')]")).sendKeys("ssinghal@sapient.com");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-pass')]")).sendKeys("ssinghal");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-submit')]")).click();
        try{
            getDriver().wait(15000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint1/elansecurelanding.spec", device.getTags());
    }


    /*
    *********  TEST SUITE RELATED TO ELAVON SITE **********
    @AUTHOR
    */
    @Test(dataProvider = "devices")
    public void verify_elavonPublicLandingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_ELAVON, "/");
        checkLayout("/specs/Sprint1/elavonpubliclanding.spec", device.getTags());
    }

    @Test(dataProvider = "devices")
    public void verify_elavonSecureLandingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_ELAVON, "/user");
        getDriver().findElement(By.xpath(".//input[contains(@id, 'edit-name')]")).sendKeys("ssinghal@sapient.com");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-pass')]")).sendKeys("ssinghal");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-submit')]")).click();
        try{
            getDriver().wait(15000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint1/elavonsecurelanding.spec", device.getTags());
    }


    /*
    *********  TEST SUITE RELATED TO FSV SITE **********
    @AUTHOR
    */
    @Test(dataProvider = "devices")
    public void verify_fsvPublicLandingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FSV, "/");
        checkLayout("/specs/Sprint1/fsvpubliclanding.spec", device.getTags());
    }

    @Test(dataProvider = "devices")
    public void verify_fsvSecureLandingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FSV, "/user");
        getDriver().findElement(By.xpath(".//input[contains(@id, 'edit-name')]")).sendKeys("ssinghal@sapient.com");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-pass')]")).sendKeys("ssinghal");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-submit')]")).click();
        try{
            getDriver().wait(15000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint1/fsvsecurelanding.spec", device.getTags());
    }

    /*
    *********  TEST SUITE RELATED TO SUPER PORTAL SITE **********
    @AUTHOR
    */
    @Test(dataProvider = "devices")
    public void verify_superPublicLandingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_SUPER, "/");
        checkLayout("/specs/Sprint1/superpubliclanding.spec", device.getTags());
    }

    @Test(dataProvider = "devices")
    public void verify_superSecureLandingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_SUPER, "/user");
        getDriver().findElement(By.xpath(".//input[contains(@id, 'edit-name')]")).sendKeys("ssinghal@sapient.com");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-pass')]")).sendKeys("ssinghal");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-submit')]")).click();
        try{
            getDriver().wait(15000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint1/supersecurelanding.spec", device.getTags());
    }
}
