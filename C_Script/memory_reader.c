#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include "memory_reader.h"
#include "node.h"

// Hook function to capture memory operations
LRESULT CALLBACK HookProc(int nCode, WPARAM wParam, LPARAM lParam) {
    // Check if the message is a memory operation
    if (nCode == WM_COPYDATA) {
        // Get the memory operation data
        PCOPYDATASTRUCT pData = (PCOPYDATASTRUCT)lParam;
        MEMORY_OPERATION op;
        op.address = pData->dwData;
        op.value = pData->cbData;
        op.operation = pData->dwType;

        // Send the data to the node (library)
        send_data_to_node(op);
    }

    return CallNextHookEx(NULL, nCode, wParam, lParam);
}

// Set up hook
HHOOK hHook = SetWindowsHookEx(WH_CALLWNDPROC, HookProc, NULL, 0);

// Send data to node (library)
void send_data_to_node(MEMORY_OPERATION op) {
    // Open the pipe to communicate with the node (library)
    HANDLE hPipe = CreateFile("\\\\.\\pipe\\MemoryReaderPipe", GENERIC_READ | GENERIC_WRITE, 0, NULL, OPEN_EXISTING, 0, NULL);

    // Write the data to the pipe
    DWORD dwWritten;
    WriteFile(hPipe, &op, sizeof(MEMORY_OPERATION), &dwWritten, NULL);

    // Close the pipe
    CloseHandle(hPipe);
}

// Unhook function
void unhook() {
    UnhookWindowsHookEx(hHook);
}