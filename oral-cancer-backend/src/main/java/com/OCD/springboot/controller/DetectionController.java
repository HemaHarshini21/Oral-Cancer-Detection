package com.OCD.springboot.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import com.OCD.springboot.service.DetectionService;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins="*")
public class DetectionController {

    @Autowired
    private DetectionService detectionService;

    @PostMapping("/predict")
    public ResponseEntity<?> predict(@RequestParam("file") MultipartFile file) {

        try {
            String result = detectionService.analyzeImage(file);
            return ResponseEntity.ok(result);
        }
        catch (Exception e){
            e.printStackTrace();
            return ResponseEntity.status(500).body("Prediction Failed");
        }
    }
}