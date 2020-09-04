Inference Engine
================================

Inference Engine is a set of C++ libraries providing a common API to deliver inference solutions on the platform of your choice: CPU, GPU, VPU, or FPGA. Use the Inference Engine API to read the Intermediate Representation, set the input and output formats, and execute the model on devices. While the C++ libraries is the primary implementation, C libraries and Python bindings are also available.

Inference Engine uses a plugin architecture. Inference Engine plugin is a software component that contains complete implementation for inference on a certain Intel&reg; hardware device: CPU, GPU, VPU, FPGA, etc. Each plugin implements the unified API and provides additional hardware-specific APIs.

For complete API Reference, see the [API Reference](usergroup29.html) section.