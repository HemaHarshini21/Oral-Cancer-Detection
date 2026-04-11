package com.OCD.springboot.dto;

public class PredictionResponse {

    private String label;
    private double confidence;
    private String heatmap;

    public PredictionResponse() {}

    public PredictionResponse(String label, double confidence, String heatmap) {
        this.label = label;
        this.confidence = confidence;
        this.heatmap = heatmap;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public double getConfidence() {
        return confidence;
    }

    public void setConfidence(double confidence) {
        this.confidence = confidence;
    }

    public String getHeatmap() {
        return heatmap;
    }

    public void setHeatmap(String heatmap) {
        this.heatmap = heatmap;
    }
}