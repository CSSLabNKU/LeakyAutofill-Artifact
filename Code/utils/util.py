import win32gui
import win32process

""" Our Utils Class contains one function.

This function is used to retrieve all window handles associated with a specified process ID. 
If first defines a callback function that is called while enumerating all windows.
The callback function checks the visibility and availability of each window and retrieves the process ID for each window.
If the process ID of the window matches the provided PID, its handle is added to the result list. Finally, it returns all found window handles.

This function is particularly useful when testing Chromium-based PMs. 
This is because the pop-up windows of the built-in-Chromium-browser PMs belongs to the same process of the browser yet not the same window handle. 
If we want to conduct the click event in the pop-up window of the PM, we need to change our focus to the newly generated window handle.

"""
class Utils(object):
    # Get window handles by process ID (pid)
    def get_hwnds_by_pid(pid):
        def callback(hwnd, hwnds):
            # Check whether the window is visible and enabled
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                # Get the window's thread ID and process ID
                _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
                # If the found process ID matches, append the window handle to the list
                if found_pid == pid:
                    hwnds.append(hwnd)
            return True

        # The list storing window handles
        hwnds = [] 
        # Enumerate all windows and call the callback function. One webpage generally means one window.
        win32gui.EnumWindows(callback, hwnds)
        # Return the list
        return hwnds
