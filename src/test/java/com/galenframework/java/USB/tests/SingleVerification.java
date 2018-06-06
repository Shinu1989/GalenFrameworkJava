package com.galenframework.java.USB.tests;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class SingleVerification extends GalenTestBase {
	
//*******************************Blog Detail Font*****************************************************************	
	/*@Test(dataProvider = "devices")
    public void verify_elanFontBlogDetailPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_BLOG_DetailELAN, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/Elan/DESKTOP/BlogDetailPageELAN.spec", device.getTags());
    }
	
	 @Test(dataProvider = "devices")
	    public void verify_elavonFontBlogDetailPage(TestDevice device) throws IOException {
	        load(GalenTestBase.TEST_URL_BLOG_DetailELAVON, "/");       
	        try{
	            Thread.sleep(20000);
	        }catch(Exception e)
	        {
	            // catch exception here
	        }
	        checkLayout("/specs/Sprint2/Elavon/DESKTOP/BlogDetailPageELAVON.spec", device.getTags());
	    }
	 
	 @Test(dataProvider = "devices")
	    public void verify_FSVFontBlogDetailPage(TestDevice device) throws IOException {
	        load(GalenTestBase.TEST_URL_BLOG_DetailFSV, "/");       
	        try{
	            Thread.sleep(20000);
	        }catch(Exception e)
	        {
	            // catch exception here
	        }
	        checkLayout("/specs/Sprint2/FSV/DESKTOP/BlogDetailPageFSV.spec", device.getTags());
	    }

	 @Test(dataProvider = "devices")
	    public void verify_USBFontBlogDetailPage(TestDevice device) throws IOException {
	        load(GalenTestBase.TEST_URL_BLOG_DetailUSB, "/");       
	        try{
	            Thread.sleep(20000);
	        }catch(Exception e)
	        {
	            // catch exception here
	        }
	        checkLayout("/specs/Sprint2/USB/DESKTOP/BlogDetailPageUSB.spec", device.getTags());
	    }

	    @Test(dataProvider = "devices")
	    public void verify_SUPERFontBlogDetailPage(TestDevice device) throws IOException {
	        load(GalenTestBase.TEST_URL_BLOG_DetailSUPER, "/");       
	        try{
	            Thread.sleep(20000);
	        }catch(Exception e)
	        {
	            // catch exception here
	        }
	        checkLayout("/specs/Sprint2/SUPER/DESKTOP/BlogDetailPageSUPER.spec", device.getTags());
	    }
	    */
	//*******************************Blog Detail PIXEL*****************************************************************	
	/*@Test(dataProvider = "devices")
    public void verify_elanPIXELBlogDetailPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_BLOG_DetailELAN, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/Elan/DESKTOP/PIXELBlogDetailPageELAN.spec", device.getTags());
    }
	
	 @Test(dataProvider = "devices")
	    public void verify_elavonPIXELBlogDetailPage(TestDevice device) throws IOException {
	        load(GalenTestBase.TEST_URL_BLOG_DetailELAVON, "/");       
	        try{
	            Thread.sleep(20000);
	        }catch(Exception e)
	        {
	            // catch exception here
	        }
	        checkLayout("/specs/Sprint2/Elavon/DESKTOP/PIXELBlogDetailPageELAVON.spec", device.getTags());
	    }
	 
	 @Test(dataProvider = "devices")
	    public void verify_FSVPIXELlogDetailPage(TestDevice device) throws IOException {
	        load(GalenTestBase.TEST_URL_BLOG_DetailFSV, "/");       
	        try{
	            Thread.sleep(20000);
	        }catch(Exception e)
	        {
	            // catch exception here
	        }
	        checkLayout("/specs/Sprint2/FSV/DESKTOP/PIXELBlogDetailPageFSV.spec", device.getTags());
	    }

	 @Test(dataProvider = "devices")
	    public void verify_USBPIXELBlogDetailPage(TestDevice device) throws IOException {
	        load(GalenTestBase.TEST_URL_BLOG_DetailUSB, "/");       
	        try{
	            Thread.sleep(20000);
	        }catch(Exception e)
	        {
	            // catch exception here
	        }
	        checkLayout("/specs/Sprint2/USB/DESKTOP/PIXELBlogDetailPageUSB.spec", device.getTags());
	    }
	    
	    @Test(dataProvider = "devices")
	    public void verify_SUPERPIXELBlogDetailPage(TestDevice device) throws IOException {
	        load(GalenTestBase.TEST_URL_BLOG_DetailSUPER, "/");       
	        try{
	            Thread.sleep(20000);
	        }catch(Exception e)
	        {
	            // catch exception here
	        }
	        checkLayout("/specs/Sprint2/SUPER/DESKTOP/PIXELBlogDetailPageSUPER.spec", device.getTags());
	    }
	   */
	  //*******************************Blog Listing Font***********************************
	    /*
	    
	    public class BlogListingVerification extends GalenTestBase {

	  	  @Test(dataProvider = "devices")
	  	    public void verify_elanFontBlogListiingPage(TestDevice device) throws IOException {
	  	        load(GalenTestBase.TEST_URL_BLOG_LISTINGUSB, "/");       
	  	        try{
	  	            Thread.sleep(20000);
	  	        }catch(Exception e)
	  	        {
	  	            // catch exception here
	  	        }
	  	        checkLayout("/specs/Sprint2/Elan/DESKTOP/BlogListingELAN.spec", device.getTags());
	  	    }
	  	  
	      @Test(dataProvider = "devices")
	      public void verify_elavonFontBlogListiingPage(TestDevice device) throws IOException {
	          load(GalenTestBase.TEST_URL_BLOG_LISTINGELAVON, "/");       
	          try{
	              Thread.sleep(20000);
	          }catch(Exception e)
	          {
	              // catch exception here
	          }
	          checkLayout("/specs/Sprint2/Elavon/DESKTOP/BlogListingELAVON.spec", device.getTags());
	      }
	      
	      @Test(dataProvider = "devices")
	      public void verify_FSVFontBlogListiingPage(TestDevice device) throws IOException {
	          load(GalenTestBase.TEST_URL_BLOG_LISTINGFSV, "/");       
	          try{
	              Thread.sleep(20000);
	          }catch(Exception e)
	          {
	              // catch exception here
	          }
	          checkLayout("/specs/Sprint2/FSV/DESKTOP/BlogListingFSV.spec", device.getTags());
	          
	          
	      }
	      
	      @Test(dataProvider = "devices")
	      public void verify_USBFontBlogListiingPage(TestDevice device) throws IOException {
	          load(GalenTestBase.TEST_URL_BLOG_LISTINGUSB, "/");       
	          try{
	              Thread.sleep(20000);
	          }catch(Exception e)
	          {
	              // catch exception here
	          }
	          checkLayout("/specs/Sprint2/USB/DESKTOP/BlogListingUSB.spec", device.getTags());
	      }
	      
	      @Test(dataProvider = "devices")
	      public void verify_SUPERFontBlogListiingPage(TestDevice device) throws IOException {
	          load(GalenTestBase.TEST_URL_BLOG_LISTINGSUPER, "/");       
	          try{
	              Thread.sleep(20000);
	          }catch(Exception e)
	          {
	              // catch exception here
	          }
	          checkLayout("/specs/Sprint2/SUPER/DESKTOP/BlogListingSUPER.spec", device.getTags());
	      }
	      
	    */
	    
	//    **************************************BLOG LISTING PIXEL************************************
/*
	    
	    public class BlogListingVerification extends GalenTestBase {

	  	  @Test(dataProvider = "devices")
	  	    public void verify_elanFontBlogListiingPage(TestDevice device) throws IOException {
	  	        load(GalenTestBase.TEST_URL_BLOG_LISTINGUSB, "/");       
	  	        try{
	  	            Thread.sleep(20000);
	  	        }catch(Exception e)
	  	        {
	  	            // catch exception here
	  	        }
	  	        checkLayout("/specs/Sprint2/Elan/DESKTOP/PIXELBlogListingELAN.spec", device.getTags());
	  	    }
	  	  
	      @Test(dataProvider = "devices")
	      public void verify_elavonFontBlogListiingPage(TestDevice device) throws IOException {
	          load(GalenTestBase.TEST_URL_BLOG_LISTINGELAVON, "/");       
	          try{
	              Thread.sleep(20000);
	          }catch(Exception e)
	          {
	              // catch exception here
	          }
	          checkLayout("/specs/Sprint2/Elavon/DESKTOP/PIXELBlogListingELAVON.spec", device.getTags());
	      }
	      
	      @Test(dataProvider = "devices")
	      public void verify_FSVFontBlogListiingPage(TestDevice device) throws IOException {
	          load(GalenTestBase.TEST_URL_BLOG_LISTINGFSV, "/");       
	          try{
	              Thread.sleep(20000);
	          }catch(Exception e)
	          {
	              // catch exception here
	          }
	          checkLayout("/specs/Sprint2/FSV/DESKTOP/PIXELBlogListingFSV.spec", device.getTags());
	          
	          
	      }
	      
	      @Test(dataProvider = "devices")
	      public void verify_USBFontBlogListiingPage(TestDevice device) throws IOException {
	          load(GalenTestBase.TEST_URL_BLOG_LISTINGUSB, "/");       
	          try{
	              Thread.sleep(20000);
	          }catch(Exception e)
	          {
	              // catch exception here
	          }
	          checkLayout("/specs/Sprint2/USB/DESKTOP/PIXELSBlogListingUSB.spec", device.getTags());
	      }
	      
	      @Test(dataProvider = "devices")
	      public void verify_SUPERFontBlogListiingPage(TestDevice device) throws IOException {
	          load(GalenTestBase.TEST_URL_BLOG_LISTINGSUPER, "/");       
	          try{
	              Thread.sleep(20000);
	          }catch(Exception e)
	          {
	              // catch exception here
	          }
	          checkLayout("/specs/Sprint2/SUPER/DESKTOP/PIXELSBlogListingSUPER.spec", device.getTags());
	      }
	      
	    
	 //  **************************************Contact Us Font****************************************
	   /*  @Test(dataProvider = "devices")
    public void verify_elanFontBlogListiingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_CONTACTELAN, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/Elan/DESKTOP/Font_CONTACT_ELAN.spec", device.getTags());
    }
	      
	      @Test(dataProvider = "devices")
    public void verify_ELAVONFontContactUSPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_CONTACTELAVON, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/Elavon/DESKTOP/Font_CONTACT_ELAVON.spec", device.getTags());
    }
    
    @Test(dataProvider = "devices")
    public void verify_FSVFontContactUSPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_CONTACTFSV, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/FSV/DESKTOP/Font_CONTACT_FSV.spec", device.getTags());
    }
    
        @Test(dataProvider = "devices")
    public void verify_SUPERFontContactUSPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_CONTACTFSV, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/SUPER/DESKTOP/Font_CONTACT_SUPER.spec", device.getTags());
    }
    
        @Test(dataProvider = "devices")
    public void verify_USBFontContactUSPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_CONTACTUSB, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/USB/DESKTOP/Font_CONTACT_USB.spec", device.getTags());
        }
        
        */
   // *****************************************FAQ FONT***************************************
    /*
     @Test(dataProvider = "devices")
    public void verify_elanFontBlogListiingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FAQELAN, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/Elan/DESKTOP/Font_FAQ_ELAN.spec", device.getTags());
    }

 @Test(dataProvider = "devices")
    public void verify_ELAVONFAQFONTPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FAQELAVON, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/Elavon/DESKTOP/Font_FAQ_ELAVON.spec", device.getTags());
    }
    
    @Test(dataProvider = "devices")
    public void verify_FSVFAQFONTPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FAQFSV, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/FSV/DESKTOP/Font_FAQ_FSV.spec", device.getTags());
    }

 @Test(dataProvider = "devices")
    public void verify_SUPERFAQFONTPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FAQFSV, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/SUPER/DESKTOP/Font_FAQ_SUPER.spec", device.getTags());
    }
    
    @Test(dataProvider = "devices")
    public void verify_USBFAQFONTPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FAQUSB, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/USB/DESKTOP/Font_FAQ_USB.spec", device.getTags());
    }*/


  // *****************************TERMS AND CONDITION FONT*******************************************
  /* @Test(dataProvider = "devices")
    public void verify_elanFontTERMS(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_TERMSELAN, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/Elan/DESKTOP/Font_TermsCondition_ELAN.spec", device.getTags());
    }
    
     @Test(dataProvider = "devices")
    public void verify_elavonFontTermsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_TERMSELAVON, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/Elavon/DESKTOP/Font_TermsCondition_ELAVON.spec", device.getTags());
    }
    
       @Test(dataProvider = "devices")
    public void verify_FSVFontTermsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_TERMSFSV, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/FSV/DESKTOP/Font_TermsCondition_FSV.spec", device.getTags());
    }
    
      @Test(dataProvider = "devices")
    public void verify_USBFontTermsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_TERMSUSB, "/");       
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint2/USB/DESKTOP/Font_TermsCondition_USB.spec", device.getTags());
    }

   */ 
	     // ***************************************USB Public Landing*****************************************
/*
    @Test(dataProvider = "devices")
    public void creativeVerification_usbPublicLandingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_USB, "/");
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint1/usbpubliclanding.spec", device.getTags());
    }

    @Test(dataProvider = "devices")
    public void creativeVerification_usbAPIListiingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_FSV, "/");
        getDriver().findElement(By.xpath("//header//ul/li/a[contains(@href, '/api')]")).click();
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }
        checkLayout("/specs/Sprint1/fsvpubliclanding.spec", device.getTags());
    }*/


    /*@Test(dataProvider = "devices")
    public void creativeVerification_usbSecureLandingPage(TestDevice device) throws IOException {
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
        checkLayout("/specs/Sprint1/fsvsecurelanding.spec", device.getTags());
   ) }*/
}


