package com.galenframework.java.USB.testfsv;

import com.galenframework.java.USB.components.GalenTestBase;
import com.galenframework.java.USB.components.GalenTestBase.TestDevice;

import org.openqa.selenium.By;
import org.testng.annotations.Test;

import java.io.IOException;


public class BlogDetailVerification extends GalenTestBase {


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
    public void verify_FSVPixelBlogDetailsPage(TestDevice device) throws IOException {
        load(GalenTestBase.TEST_URL_BLOG_DetailFSV, "/");     
        try{
            Thread.sleep(20000);
        }catch(Exception e)
        {
            // catch exception here
        }       
        checkLayout("/specs/Sprint2/FSV/DESKTOP/PIXELBlogDetailPageFSV.spec", device.getTags());
    }

}
