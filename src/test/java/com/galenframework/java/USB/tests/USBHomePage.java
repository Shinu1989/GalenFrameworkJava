package com.galenframework.java.USB.tests;

import com.galenframework.java.USB.components.GalenTestBase;
import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class USBHomePage extends GalenTestBase {

   /* @Test(dataProvider = "devices")
    public void usbHomePage_creativeTest_onDeskTop(TestDevice device) throws IOException {
        load("/");
        checkLayout("/specs/elanpubliclanding.spec", device.getTags());
    }*/

   @Test(dataProvider = "devices")
    public void secureladingpage_shouldLookGood_onDevice(TestDevice device) throws IOException {
        load("/user/login?current=node/101");
        getDriver().findElement(By.xpath(".//input[contains(@id, 'edit-name')]")).sendKeys("gpahuja@sapient.com");
        getDriver().findElement(By.xpath(".//input[contains(@id,'edit-pass')]")).sendKeys("gpahuja@123");
        checkLayout("/specs/usbsecurelanding.spec", device.getTags());
    }

}
