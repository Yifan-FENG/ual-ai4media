#adapted from https://www.pyimagedata.com/how-to-build-an-artificial-neural-network-with-python/
######Ignore this code unless you really want to get into back propagation######
import numpy as np

def get_gradients(inputs, output, a1, a2, w1, w2, bias, lr):
    b1 = bias[0]
    b2 = bias[1]
    error_d_a2 = (a2 - output)
    ### derivative of the a2 with respect to the z2
    a2_d_z2 = a2*(1 - a2)
    ### derivative of the z2 with respect to the w2
    z2_d_w2 = a1
    ### derivative of the z2 with respect to the b2_w
    z2_d_b2 = b2
    ### delta weights 2
    delta_w2 =  error_d_a2 * a2_d_z2
    delta_w2 = np.dot(z2_d_w2.T, delta_w2)
    ### delta biases
    delta_b2 =  error_d_a2 * a2_d_z2
    delta_b2 = delta_b2 * z2_d_b2
    delta_b2 = np.sum(delta_b2)
    ### Update weights and bias
    w2 = w2 - (delta_w2 * lr)
    ## LAYER 1
    ### derivative of the z2 with respect to the a1
    z2_d_a1 = w2
    ### derivative of the a1 with respect to the z1
    a1_d_z1 = a1*(1 - a1)
    ### derivative of the z1 with respect to the w1
    z1_d_w1 = inputs
    ### derivative of the z1 with respect to the b1_w
    z1_d_b1_w = b1
    ### delta weights 1
    delta_w1 =  error_d_a2 * a2_d_z2
    delta_w1 = np.dot(delta_w1,z2_d_a1.T)
    delta_w1 = delta_w1 * a1_d_z1
    delta_w1 = np.dot(inputs.T,delta_w1)
    ### delta bias 1
    delta_b1 =  error_d_a2 * a2_d_z2
    delta_b1 = np.dot(delta_b1,z2_d_a1.T)
    delta_b1 = delta_b1 * a1_d_z1
    delta_b1 = delta_b1 * z1_d_b1_w
    delta_b1 = np.sum(delta_b1)

    return delta_w1,delta_w2,np.array([delta_b1,delta_b2])

def get_gradients_bias(inputs, output, a1, a2, w1, w2, lr):
    error_d_a2 = (a2 - output)
    ### derivative of the a2 with respect to the z2
    a2_d_z2 = a2*(1 - a2)
    ### derivative of the z2 with respect to the w2
    z2_d_w2 = a1
    ### delta weights 2
    delta_w2 =  error_d_a2 * a2_d_z2
    delta_w2 = np.dot(z2_d_w2.T, delta_w2)
    ### Update weights and bias
    w2 = w2 - (delta_w2 * lr)
    ## LAYER 1
    ### derivative of the z2 with respect to the a1
    z2_d_a1 = w2
    ### derivative of the a1 with respect to the z1
    a1_d_z1 = a1*(1 - a1)
    ### derivative of the z1 with respect to the w1
    z1_d_w1 = inputs
    ### delta weights 1
    delta_w1 = error_d_a2 * a2_d_z2
    delta_w1 = np.dot(delta_w1,z2_d_a1.T)
    delta_w1 = delta_w1 * a1_d_z1
    delta_w1 = np.dot(inputs.T,delta_w1)
    delta_w1 = delta_w1[:,:-1]
    return delta_w1,delta_w2