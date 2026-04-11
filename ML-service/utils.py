import tensorflow as tf
import numpy as np
import cv2

def generate_gradcam(model, img_array):

    # 🔥 Use LAST convolution layer (IMPORTANT)
    last_conv_layer = model.get_layer("out_relu")

    grad_model = tf.keras.models.Model(
        [model.inputs],
        [last_conv_layer.output, model.output]
    )

    with tf.GradientTape() as tape:
        conv_outputs, predictions = grad_model(img_array)

        # If binary → use index 0
        loss = predictions[:, 0]

    grads = tape.gradient(loss, conv_outputs)

    # Global average pooling
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

    conv_outputs = conv_outputs[0]

    # Multiply feature maps with gradients
    heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)

    # ReLU
    heatmap = tf.maximum(heatmap, 0)

    # Normalize
    heatmap /= (tf.reduce_max(heatmap) + 1e-8)

    heatmap = heatmap.numpy()

    return heatmap