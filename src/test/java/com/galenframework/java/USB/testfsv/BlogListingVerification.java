package com.galenframework.java.USB.testfsv;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class BlogListingVerification extends GalenTestBase {


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
    public void verify_FSVPixelBlogListingPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_BLOG_LISTINGFSV, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/FSV/DESKTOP/PIXELBlogListingFSV.spec", device.getTags());
    }

}
