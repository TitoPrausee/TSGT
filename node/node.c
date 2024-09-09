#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include "node.h"
#include "python_interface.h"

// Named pipe to receive data from the memory reader
HANDLE hPipe;

// Function to receive data from the memory reader
void receive_data_from_memory_reader() {
    // Create the named pipe
    hPipe = CreateNamedPipe(
        "\\\\.\\pipe\\MemoryReaderPipe",
        PIPE_ACCESS_DUPLEX,
        PIPE_TYPE_MESSAGE | PIPE_WAIT,
        1,
        65536,
        65536,
        0,
        NULL
    );

    // Wait for a connection from the memory reader
    ConnectNamedPipe(hPipe, NULL);

    // Receive data from the memory reader
    while (1) {
        MEMORY_OPERATION op;
        DWORD dwRead;
        ReadFile(hPipe, &op, sizeof(MEMORY_OPERATION), &dwRead, NULL);

        // Send the data to the Python script
        send_data_to_python(op);
    }

    // Close the pipe
    CloseHandle(hPipe);
}

// Function to send data to the Python script
void send_data_to_python(MEMORY_OPERATION op) {
    // Use a Python-C API to send the data to the Python script
    PyObject* args = PyTuple_Pack(3, PyLong_FromUnsignedLong(op.address), PyLong_FromUnsignedLong(op.value), PyLong_FromUnsignedLong(op.operation));
    PyObject* result = PyObject_CallObject(python_interface_send_data, args);
    Py_XDECREF(args);
    Py_XDECREF(result);
}

// Initialize the node
void init_node() {
    // Initialize the Python-C API
    Py_Initialize();

    // Import the Python module
    PyObject* python_module = PyImport_ImportModule("memory_visualizer");
    if (python_module == NULL) {
        PyErr_Print();
        exit(1);
    }

    // Get the Python function to send data
    python_interface_send_data = PyObject_GetAttrString(python_module, "receive_data_from_node");
    if (python_interface_send_data == NULL) {
        PyErr_Print();
        exit(1);
    }
}

// Clean up the node
void cleanup_node() {
    // Clean up the Python-C API
    Py_Finalize();
}