package com.galenframework.java.USB.tests;

import com.galenframework.java.USB.components.GalenTestBase;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.testng.annotations.Test;

import java.io.IOException;


public class PublicLandingPage_creative_Verification extends GalenTestBase {

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
	/*
    @Test(dataProvider = "devices")
    public void usbPublicLandingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_USB, "/");       
        checkLayout("/specs/usbpubliclanding.spec", device.getTags());
    }
    

  

    /*
    *********  TEST SUITE RELATED TO ELAN SITE **********
    @AUTHOR
    */  /*  @Test(dataProvider = "devices")
    public void elanPublicLandingPage(TestDevice device) throws IOException {
        System.out.println("Entered landing page method ");
        load(GalenTestBase.TEST_URL_ELAN, "/");
        checkLayout("/specs/elanpubliclanding.spec", device.getTags());
    }
*/


    /*
    *********  TEST SUITE RELATED TO ELAVON SITE **********
    @AUTHOR
    */
   
    /*@Test(dataProvider = "devices")
    public void elavonPublicLandingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_ELAVON, "/");
        checkLayout("/specs/elavonpubliclanding.spec", device.getTags());
    }



    /*
    *********  TEST SUITE RELATED TO FSV SITE **********
    @AUTHOR
    *//*
    @Test(dataProvider = "devices")
    public void fsvPublicLandingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FSV, "/");
        checkLayout("/specs/fsvpubliclanding.spec", device.getTags());
    }
*/

    /*
    *********  TEST SUITE RELATED TO SUPER PORTAL SITE **********
    @AUTHOR
    *//*
    @Test(dataProvider = "devices")
    public void superPublicLandingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_SUPER, "/");
        checkLayout("/specs/superpubliclanding.spec", device.getTags());
    }
*/
}
