package com.OCD.springboot.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import com.OCD.springboot.client.MLServiceClient;

@Service
public class DetectionService {

    @Autowired
    private MLServiceClient mlServiceClient;

    public String analyzeImage(MultipartFile file) throws Exception {

        if(file.isEmpty()){
            throw new RuntimeException("File is empty");
        }

        return mlServiceClient.sendImageToML(file);
    }
}